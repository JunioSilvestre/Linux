#!/usr/bin/env python3
"""
Git AutoSync Daemon - Sincronização inteligente, resiliente e segura em segundo plano.
Recursos:
- Timeouts em comandos de rede Git (evita travamento do daemon)
- Mute de alertas repetidos com cooldown configurável para detecção de segredos
- Filtro inteligente com ignored_patterns do config.json e git check-ignore
- Checkpoints detalhados com SHA antes e depois para rollback preciso
- Debounce configurável para agrupamento de commits
- Polling otimizado para redução de I/O em discos externos
- Notificações nativas no macOS
"""

import fnmatch
import json
import os
import re
import signal
import subprocess
import sys
import time
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Optional, Tuple

BASE_DIR = Path(__file__).resolve().parent
REPO_ROOT = BASE_DIR.parent.parent
CONFIG_FILE = BASE_DIR / "config.json"
CHECKPOINTS_FILE = BASE_DIR / ".checkpoints.json"
PID_FILE = BASE_DIR / ".autosync.pid"
PAUSE_FILE = BASE_DIR / ".autosync.pause"
LOGS_DIR = BASE_DIR / "logs"
LOG_FILE = LOGS_DIR / "autosync.log"


def log(message: str, level: str = "INFO") -> None:
    """Registra mensagens formatadas no console e no arquivo de log."""
    try:
        LOGS_DIR.mkdir(parents=True, exist_ok=True)
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        formatted = f"[{timestamp}] [{level}] {message}"
        print(formatted, flush=True)
        with open(LOG_FILE, "a", encoding="utf-8") as f:
            f.write(formatted + "\n")
    except Exception:
        pass


def notify_macos(title: str, message: str) -> None:
    """Dispara uma notificação nativa na Central de Notificações do macOS."""
    try:
        # Sanitiza aspas para prevenir erros de interpolação no AppleScript
        safe_title = title.replace('"', '\\"')
        safe_msg = message.replace('"', '\\"')
        script = f'display notification "{safe_msg}" with title "{safe_title}"'
        subprocess.run(
            ["osascript", "-e", script],
            check=False,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
            timeout=5,
        )
    except Exception:
        pass


class AutoSync:
    """Daemon de automação Git com segurança e resiliência."""

    def __init__(self, repo_root: Path = REPO_ROOT, base_dir: Path = BASE_DIR):
        self.repo_root = repo_root
        self.base_dir = base_dir
        self.config_file = base_dir / "config.json"
        self.checkpoints_file = base_dir / ".checkpoints.json"
        self.pid_file = base_dir / ".autosync.pid"
        self.pause_file = base_dir / ".autosync.pause"

        self.running = True
        self.config = self.load_config()

        # Rastreamento de alertas de segredos: {filepath: {"last_alert": float, "pattern": str}}
        self.secret_alerts: Dict[str, Dict[str, any]] = {}

    def load_config(self) -> dict:
        """Carrega configurações do config.json com valores padrão seguros."""
        defaults = {
            "poll_interval": 10,
            "check_interval_seconds": 10,
            "debounce_seconds": 15,
            "network_timeout_seconds": 15,
            "alert_cooldown_seconds": 300,
            "notify_macos": True,
            "max_checkpoints": 20,
            "ignored_patterns": [
                ".git/*",
                ".DS_Store",
                "*.swp",
                "*.swo",
                "*.tmp",
                "*~",
                "*.log",
                "Automation/git-autosync/logs/*",
                "Automation/git-autosync/.checkpoints.json",
                "Automation/git-autosync/.autosync.pid",
                "Automation/git-autosync/.autosync.pause",
            ],
            "sensitive_patterns": [
                r"(?i)(password|passwd|secret|api_key|token)\s*[:=]\s*['\"][^'\"]{8,}['\"]",
                r"-----BEGIN (RSA |EC |DSA |OPENSSH )?PRIVATE KEY-----",
                r"ghp_[A-Za-z0-9]{36}",
                r"AIza[0-9A-Za-z-_]{35}",
                r"xox[baprs]-[0-9a-zA-Z]{10,48}",
                r"AKIA[0-9A-Z]{16}",
            ],
        }
        if self.config_file.exists():
            try:
                with open(self.config_file, "r", encoding="utf-8") as f:
                    loaded = json.load(f)
                    defaults.update(loaded)
            except Exception as e:
                log(f"Erro ao carregar config.json ({e}), usando defaults.", "WARN")
        return defaults

    def run_cmd(
        self, cmd: list, cwd: Optional[Path] = None, timeout: Optional[int] = None
    ) -> Tuple[int, str, str]:
        """
        Executa um comando no shell com proteção de timeout obrigatória.

        Args:
            cmd: Lista com comando e argumentos
            cwd: Diretório de execução (padrão: repo_root)
            timeout: Tempo limite em segundos (padrão: network_timeout_seconds ou 15s)

        Returns:
            Tuple[int, str, str]: (returncode, stdout, stderr)
        """
        if cwd is None:
            cwd = self.repo_root
        if timeout is None:
            timeout = self.config.get("network_timeout_seconds", 15)

        cmd_repr = " ".join(cmd) if isinstance(cmd, list) else str(cmd)
        try:
            result = subprocess.run(
                cmd,
                cwd=cwd,
                text=True,
                capture_output=True,
                timeout=timeout,
            )
            return result.returncode, result.stdout.strip(), result.stderr.strip()
        except subprocess.TimeoutExpired:
            log(f"Timeout após {timeout}s no comando: {cmd_repr}", "WARN")
            return 124, "", f"Command timed out after {timeout}s: {cmd_repr}"
        except Exception as e:
            log(f"Erro inesperado no comando '{cmd_repr}': {e}", "ERROR")
            return 1, "", str(e)

    def should_ignore(self, filepath: str) -> bool:
        """
        Verifica se um arquivo deve ser ignorado com base em:
        1. Ignorados internos da automação (Automation/git-autosync/)
        2. ignored_patterns definidos no config.json (via fnmatch)
        3. Regras de .gitignore via git check-ignore
        """
        norm_path = filepath.strip().replace("\\", "/")

        basename = os.path.basename(norm_path)
        patterns = self.config.get("ignored_patterns", [])

        for pattern in patterns:
            if fnmatch.fnmatch(norm_path, pattern) or fnmatch.fnmatch(basename, pattern):
                return True

        # Verifica regras de .gitignore
        code, _, _ = self.run_cmd(["git", "check-ignore", "--quiet", norm_path], timeout=5)
        if code == 0:
            return True

        return False

    def get_git_status(self) -> List[str]:
        """Retorna lista de alterações do git status filtrando padrões ignorados."""
        code, out, err = self.run_cmd(["git", "status", "--porcelain"], timeout=10)
        if code != 0:
            log(f"Falha ao obter git status: {err}", "WARN")
            return []

        filtered = []
        for line in out.splitlines():
            line_str = line.strip()
            if not line_str or len(line_str) < 4:
                continue

            # Formato do porcelain: XY path/to/file ou XY orig -> dest
            file_part = line[3:].strip()
            if " -> " in file_part:
                file_part = file_part.split(" -> ")[-1].strip()

            if not self.should_ignore(file_part):
                filtered.append(line_str)

        return filtered

    def get_current_branch(self) -> str:
        """Obtém o nome do branch atual."""
        code, out, _ = self.run_cmd(["git", "rev-parse", "--abbrev-ref", "HEAD"], timeout=5)
        return out if (code == 0 and out and out != "HEAD") else "main"

    def get_current_head(self) -> str:
        """Obtém o hash SHA atual do HEAD."""
        code, out, _ = self.run_cmd(["git", "rev-parse", "HEAD"], timeout=5)
        return out if code == 0 else ""

    def scan_for_secrets(self) -> List[Tuple[str, str]]:
        """
        Escaneia alterações para detecção prévia de segredos/chaves de API por arquivo.

        Returns:
            List[Tuple[str, str]]: Lista de pares (filepath, pattern_matched)
        """
        patterns = self.config.get("sensitive_patterns", [])
        if not patterns:
            return []

        detected: List[Tuple[str, str]] = []

        # 1. Verifica alterações em arquivos rastreados (git diff HEAD)
        code, diff_out, _ = self.run_cmd(["git", "diff", "HEAD"], timeout=15)
        if code == 0 and diff_out:
            current_file = "diff"
            for line in diff_out.splitlines():
                if line.startswith("+++ b/"):
                    current_file = line[6:].strip()
                elif line.startswith("+") and not line.startswith("+++"):
                    added_line = line[1:]
                    for pattern in patterns:
                        if re.search(pattern, added_line):
                            detected.append((current_file, pattern))
                            break

        # 2. Verifica arquivos untracked (novos)
        code2, untracked_out, _ = self.run_cmd(["git", "status", "--porcelain"], timeout=10)
        if code2 == 0 and untracked_out:
            for line in untracked_out.splitlines():
                if line.startswith("??"):
                    filepath = line[3:].strip()
                    if self.should_ignore(filepath):
                        continue
                    full_path = self.repo_root / filepath
                    if full_path.is_file() and full_path.stat().st_size < 500_000:
                        try:
                            content = full_path.read_text(encoding="utf-8", errors="ignore")
                            for pattern in patterns:
                                if re.search(pattern, content):
                                    detected.append((filepath, pattern))
                                    break
                        except Exception:
                            pass

        return detected

    def handle_secret_alerts(self, detected_secrets: List[Tuple[str, str]]) -> bool:
        """
        Gerencia o envio de alertas de segredos aplicando cooldown para evitar notificações repetidas.

        Returns:
            bool: True se há segredos detectados (bloqueando commit), False caso contrário.
        """
        if not detected_secrets:
            # Limpa alertas antigos resolvidos
            self.secret_alerts.clear()
            return False

        now = time.time()
        cooldown = self.config.get("alert_cooldown_seconds", 300)
        current_files = {filepath for filepath, _ in detected_secrets}

        # Remove arquivos que já foram corrigidos
        resolved = [f for f in self.secret_alerts if f not in current_files]
        for f in resolved:
            del self.secret_alerts[f]

        notified_any = False
        for filepath, pattern in detected_secrets:
            last_record = self.secret_alerts.get(filepath)
            should_notify = False

            if not last_record:
                should_notify = True
            else:
                last_time = last_record.get("last_alert", 0)
                last_pattern = last_record.get("pattern", "")
                if (now - last_time > cooldown) or (pattern != last_pattern):
                    should_notify = True

            if should_notify:
                log(
                    f"Sincronização BLOQUEADA! Segredo detectado em '{filepath}' (Padrão: {pattern})",
                    "SECURITY",
                )
                if self.config.get("notify_macos") and not notified_any:
                    notify_macos(
                        "🚨 Git AutoSync - Alerta de Segurança",
                        f"Bloqueado: Segredo detectado em {Path(filepath).name}!",
                    )
                    notified_any = True
                self.secret_alerts[filepath] = {"last_alert": now, "pattern": pattern}
            else:
                log(
                    f"Segredo ainda presente em '{filepath}', suprimindo notificação repetida (cooldown de {cooldown}s ativo).",
                    "WARN",
                )

        return True

    def save_checkpoint(
        self,
        sha_before: str,
        sha_after: str,
        branch: str,
        commit_msg: str,
        changed_files: List[str],
    ) -> None:
        """Salva metadados de checkpoint em .checkpoints.json para rollback seguro."""
        checkpoints = []
        if self.checkpoints_file.exists():
            try:
                with open(self.checkpoints_file, "r", encoding="utf-8") as f:
                    checkpoints = json.load(f)
            except Exception:
                checkpoints = []

        new_checkpoint = {
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "sha": sha_after[:8] if sha_after else "",
            "sha_full": sha_after,
            "sha_before": sha_before[:8] if sha_before else "",
            "sha_before_full": sha_before,
            "branch": branch,
            "commit_message": commit_msg,
            "files_count": len(changed_files),
            "files": changed_files[:10],
        }
        checkpoints.append(new_checkpoint)

        max_c = self.config.get("max_checkpoints", 20)
        if len(checkpoints) > max_c:
            checkpoints = checkpoints[-max_c:]

        try:
            with open(self.checkpoints_file, "w", encoding="utf-8") as f:
                json.dump(checkpoints, f, indent=2, ensure_ascii=False)
        except Exception as e:
            log(f"Falha ao salvar checkpoint em {self.checkpoints_file}: {e}", "WARN")

    def sync_repo(self) -> None:
        """Executa o ciclo completo de sincronização segura."""
        status_lines = self.get_git_status()
        if not status_lines:
            return

        # 1. Scanner de segredos com cooldown
        secrets = self.scan_for_secrets()
        if self.handle_secret_alerts(secrets):
            return

        branch = self.get_current_branch()
        head_before = self.get_current_head()

        # 2. git add
        code, _, err = self.run_cmd(["git", "add", "."], timeout=15)
        if code != 0:
            log(f"Erro no 'git add': {err}", "ERROR")
            return

        # 3. git commit
        ts = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        file_count = len(status_lines)
        commit_msg = f"auto(sync): update {file_count} file(s) [{ts}]"
        detailed_body = "\n".join(status_lines[:15])

        code, _, err = self.run_cmd(
            ["git", "commit", "-m", commit_msg, "-m", detailed_body], timeout=15
        )
        if code != 0:
            log(f"Erro no 'git commit': {err}", "ERROR")
            return

        head_after = self.get_current_head()

        # 4. Salvar Checkpoint para Rollback
        self.save_checkpoint(head_before, head_after, branch, commit_msg, status_lines)
        log(f"Commit gerado com sucesso: {commit_msg} ({head_after[:8]})")

        # 5. Push com verificação prévia segura e timeout de rede
        net_timeout = self.config.get("network_timeout_seconds", 15)
        log("Verificando atualizações remotas antes do push...")

        code, _, _ = self.run_cmd(["git", "fetch", "origin", branch], timeout=net_timeout)
        if code != 0:
            log(
                "Sem conexão ou timeout ao buscar 'origin'. Commit salvo localmente; será sincronizado no próximo ciclo.",
                "WARN",
            )
            if self.config.get("notify_macos"):
                notify_macos(
                    "⚠️ Git AutoSync",
                    f"Salvo localmente ({file_count} arquivos). Modo offline.",
                )
            return

        code, _, err = self.run_cmd(["git", "push", "origin", branch], timeout=net_timeout)
        if code == 0:
            log(f"Push concluído com sucesso para origin/{branch}!", "SUCCESS")
            if self.config.get("notify_macos"):
                notify_macos(
                    "✅ Git AutoSync",
                    f"{file_count} arquivo(s) sincronizados com o GitHub!",
                )
        else:
            log(f"Push rejeitado ({err}). Tentando rebase seguro...", "WARN")
            rebase_code, _, _ = self.run_cmd(
                ["git", "pull", "--rebase", "origin", branch], timeout=net_timeout
            )
            if rebase_code == 0:
                push_code, _, push_err = self.run_cmd(
                    ["git", "push", "origin", branch], timeout=net_timeout
                )
                if push_code == 0:
                    log("Rebase e Push concluídos com sucesso!", "SUCCESS")
                    if self.config.get("notify_macos"):
                        notify_macos("✅ Git AutoSync", "Sincronizado após rebase seguro.")
                else:
                    log(f"Falha ao enviar mesmo após rebase: {push_err}", "ERROR")
            else:
                self.run_cmd(["git", "rebase", "--abort"], timeout=10)
                log(
                    "Conflito detectado com o GitHub! Rebase abortado por segurança para proteger seu trabalho.",
                    "ALERT",
                )
                if self.config.get("notify_macos"):
                    notify_macos(
                        "⚠️ Git AutoSync - Conflito",
                        "Conflito remoto detectado. Trabalho salvo localmente.",
                    )

    def run(self) -> None:
        """Loop principal do daemon."""
        with open(self.pid_file, "w") as f:
            f.write(str(os.getpid()))

        def handle_signal(signum, frame):
            log("Encerrando daemon Git AutoSync (sinal recebido)...")
            self.running = False

        signal.signal(signal.SIGINT, handle_signal)
        signal.signal(signal.SIGTERM, handle_signal)

        log(f"Git AutoSync Daemon iniciado no repositório {self.repo_root} (PID: {os.getpid()})")
        if self.config.get("notify_macos"):
            notify_macos("🚀 Git AutoSync", "Monitoramento em segundo plano ativo!")

        last_change_time = None
        last_status_snapshot = ""

        # Lê intervalo (suporta poll_interval e check_interval_seconds)
        poll_interval = self.config.get(
            "poll_interval", self.config.get("check_interval_seconds", 10)
        )
        debounce_delay = self.config.get("debounce_seconds", 15)

        while self.running:
            if self.pause_file.exists():
                time.sleep(2)
                continue

            try:
                status = self.get_git_status()
                current_snapshot = "\n".join(status) if status else ""

                if current_snapshot:
                    if current_snapshot != last_status_snapshot:
                        last_status_snapshot = current_snapshot
                        last_change_time = time.time()
                        log(f"Alterações detectadas ({len(status)} arquivos). Aguardando estabilização...")

                    if last_change_time and (time.time() - last_change_time >= debounce_delay):
                        log(
                            f"Tempo de espera ({debounce_delay}s) concluído. Iniciando sincronização segura..."
                        )
                        self.sync_repo()
                        last_change_time = None
                        last_status_snapshot = ""
                else:
                    last_change_time = None
                    last_status_snapshot = ""

            except Exception as e:
                log(f"Erro inesperado no ciclo de sincronização: {e}", "ERROR")

            time.sleep(poll_interval)

        if self.pid_file.exists():
            try:
                self.pid_file.unlink()
            except Exception:
                pass
        log("Git AutoSync Daemon finalizado.")


if __name__ == "__main__":
    daemon = AutoSync()
    daemon.run()
