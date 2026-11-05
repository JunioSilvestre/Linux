#!/usr/bin/env python3
"""
Testes unitários e de integração para o Git AutoSync.
Cobre:
- Timeouts no run_cmd
- Filtro de ignored_patterns e check-ignore
- Scanner de segredos e cooldown de alertas (mute)
- Checkpoints e rollback
- Configurações e intervalos
"""

import os
import shutil
import tempfile
import time
import unittest
from pathlib import Path
from unittest.mock import MagicMock, patch

# Import do módulo alvo
import git_autosync
from git_autosync import AutoSync


class TestGitAutoSync(unittest.TestCase):

    def setUp(self):
        self.test_dir = Path(tempfile.mkdtemp(prefix="autosync_test_"))
        self.daemon = AutoSync(repo_root=self.test_dir, base_dir=self.test_dir)
        self.daemon.config_file = self.test_dir / "config.json"
        self.daemon.checkpoints_file = self.test_dir / ".checkpoints.json"
        self.daemon.pid_file = self.test_dir / ".autosync.pid"
        self.daemon.pause_file = self.test_dir / ".autosync.pause"

    def tearDown(self):
        shutil.rmtree(self.test_dir, ignore_errors=True)

    def test_01_run_cmd_timeout(self):
        """Verifica se o run_cmd respeita o timeout e não trava indefinidamente."""
        start = time.time()
        # Comando de sleep de 3s com timeout de 1s
        code, out, err = self.daemon.run_cmd(["sleep", "3"], timeout=1)
        elapsed = time.time() - start

        self.assertEqual(code, 124, "Deveria retornar código 124 para timeout")
        self.assertIn("timed out", err.lower())
        self.assertLess(elapsed, 2.5, "Deveria abortar logo após o timeout de 1s")

    def test_02_should_ignore(self):
        """Verifica se os padrões ignored_patterns e arquivos de autosync são ignorados."""
        self.daemon.config["ignored_patterns"] = [
            ".DS_Store",
            "*.swp",
            "*.tmp",
            "logs/*",
            "Automation/git-autosync/logs/*",
            "Automation/git-autosync/.checkpoints.json",
        ]


        # Arquivos que DEVEM ser ignorados
        self.assertTrue(self.daemon.should_ignore(".DS_Store"))
        self.assertTrue(self.daemon.should_ignore("subfolder/.DS_Store"))
        self.assertTrue(self.daemon.should_ignore("main.py.swp"))
        self.assertTrue(self.daemon.should_ignore("temp.tmp"))
        self.assertTrue(self.daemon.should_ignore("logs/app.log"))
        self.assertTrue(self.daemon.should_ignore("Automation/git-autosync/logs/autosync.log"))
        self.assertTrue(self.daemon.should_ignore("Automation/git-autosync/.checkpoints.json"))

        # Arquivos normais que NÃO devem ser ignorados
        with patch.object(self.daemon, "run_cmd", return_value=(1, "", "")):
            self.assertFalse(self.daemon.should_ignore("main.py"))
            self.assertFalse(self.daemon.should_ignore("docs/README.md"))

    def test_03_secret_alert_cooldown_mute(self):
        """Verifica se o cooldown evita disparar alertas repetidos para o mesmo arquivo/segredo."""
        self.daemon.config["alert_cooldown_seconds"] = 300
        self.daemon.config["notify_macos"] = False

        secrets_pass1 = [("app/secrets.py", "ghp_[A-Za-z0-9]{36}")]

        # 1. Primeiro alerta: deve bloquear e registrar no dicionário de alertas
        blocked = self.daemon.handle_secret_alerts(secrets_pass1)
        self.assertTrue(blocked)
        self.assertIn("app/secrets.py", self.daemon.secret_alerts)
        first_alert_time = self.daemon.secret_alerts["app/secrets.py"]["last_alert"]

        # 2. Segundo alerta 1s depois: deve bloquear, mas MANTER o timestamp do alerta original (suprimido)
        time.sleep(0.1)
        with patch("git_autosync.notify_macos") as mock_notify:
            blocked2 = self.daemon.handle_secret_alerts(secrets_pass1)
            self.assertTrue(blocked2)
            mock_notify.assert_not_called()
            self.assertEqual(
                self.daemon.secret_alerts["app/secrets.py"]["last_alert"],
                first_alert_time,
                "Timestamp não deveria mudar pois o alerta foi suprimido pelo cooldown",
            )

        # 3. Se o arquivo for corrigido (sem segredos), histórico de alertas é limpo
        self.daemon.handle_secret_alerts([])
        self.assertEqual(len(self.daemon.secret_alerts), 0)

    def test_04_save_and_list_checkpoints(self):
        """Verifica a gravação e estrutura dos checkpoints em .checkpoints.json."""
        self.daemon.save_checkpoint(
            sha_before="aaa11111",
            sha_after="bbb22222",
            branch="main",
            commit_msg="auto(sync): update 2 file(s)",
            changed_files=["file1.txt", "file2.txt"],
        )

        self.assertTrue(self.daemon.checkpoints_file.exists())
        with open(self.daemon.checkpoints_file, "r") as f:
            data = git_autosync.json.load(f)

        self.assertEqual(len(data), 1)
        self.assertEqual(data[0]["sha"], "bbb22222")
        self.assertEqual(data[0]["sha_before"], "aaa11111")
        self.assertEqual(data[0]["files_count"], 2)

    def test_05_config_defaults(self):
        """Verifica se os defaults carregam poll_interval e timeouts recomendados."""
        cfg = self.daemon.load_config()
        self.assertGreaterEqual(cfg.get("poll_interval", 0), 10)
        self.assertEqual(cfg.get("network_timeout_seconds"), 15)
        self.assertEqual(cfg.get("alert_cooldown_seconds"), 300)


if __name__ == "__main__":
    unittest.main()
