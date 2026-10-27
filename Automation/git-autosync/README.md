# 🛡️ Git AutoSync & Rollback Engine

Sistema inteligente e resiliente para sincronização automática com o GitHub em segundo plano no macOS.

---

## 💡 O que foi pensado (e que normalmente é esquecido)

Automatizar `git add . && git commit && git push` a cada salvamento parece simples, mas em ambientes reais pode causar problemas graves. Este projeto foi desenvolvido para tratar esses riscos:

### 1. 🚨 Vazamento Acidental de Segredos (Chaves / Tokens)
* **O Risco:** No momento em que você cola uma senha, API Key, Token da AWS ou GitHub para testar e salva o arquivo (`Cmd+S`), um script comum enviaria imediatamente para o GitHub público.
* **A Proteção:** O `git_autosync.py` roda um **scanner regex pré-commit**. Se detectar padrões como `ghp_...`, `AKIA...`, `BEGIN PRIVATE KEY` ou senhas em texto puro, ele **bloqueia a sincronização**, notifica na tela do Mac e não sobe nada.

### 2. ⚡ "Commit Storm" (Falta de Debounce)
* **O Risco:** Se você salvar 5 vezes em 20 segundos enquanto edita, geraria 5 commits e 5 pushes, poluindo o histórico e quebrando builds parciais.
* **A Proteção:** Possui um **Debounce Timer** (configurável, padrão 15s). Ele só inicia o commit quando você parar de salvar por 15 segundos.

### 3. 🌐 Queda de Conexão (Modo Offline)
* **O Risco:** Se você estiver sem internet, o comando `git push` falharia e poderia abortar ou corromper o fluxo.
* **A Proteção:** O script detecta falha no `fetch/push`, mantém o commit seguro localmente e sincroniza tudo automaticamente quando a internet voltar.

### 4. 🔀 Divergência com o Remoto (Conflitos)
* **O Risco:** Se você editar um arquivo direto no site do GitHub e localmente ao mesmo tempo, um `push` ingênuo quebraria ou exigiria `--force` (o que apagaria código).
* **A Proteção:** Ele tenta um `git pull --rebase` seguro. Se houver conflito de merge, ele **aborta o rebase**, não perde suas alterações locais e dispara uma notificação na tela para você decidir com calma.

### 5. 🛡️ Plano de Rollback Inteligente
* **A Solução:** Mantém um histórico de checkpoints (`.checkpoints.json`). Você pode rodar `./autosync.sh rollback` a qualquer momento para desfazer o último envio, com opção de **Soft Rollback** (mantém seus arquivos salvos no disco e desfaz apenas o commit/remoto) ou **Hard Rollback**.

### 6. 🍏 Notificações Nativas do macOS
* Como roda em segundo plano, você recebe avisos sutis na Central de Notificações do macOS informando o sucesso ou qualquer bloqueio.

---

## 🚀 Como Usar

No terminal, dentro de `Automation/git-autosync`:

```bash
cd /Volumes/HD-EXTERNO/Projetos/Linux/Automation/git-autosync
```

### Iniciar em segundo plano
```bash
./autosync.sh start
```

### Ver o status
```bash
./autosync.sh status
```

### Acompanhar logs em tempo real
```bash
./autosync.sh logs
```

### Pausar temporariamente (ex: ao fazer grandes refatorações)
```bash
./autosync.sh pause
```
*(Para voltar a sincronizar: `./autosync.sh resume`)*

### 🛡️ Fazer Rollback Inteligente
Você pode rodar no modo interativo ou usar os novos comandos diretos:
```bash
# Listar os últimos checkpoints registrados (com SHA, Data e Mensagem)
./autosync.sh rollback list

# Desfazer o último commit mantendo seus arquivos intactos no disco (Soft)
./autosync.sh rollback --last

# Desfazer o último commit descartando alterações (Hard)
./autosync.sh rollback --last --hard

# Restaurar para um SHA específico
./autosync.sh rollback <SHA>
./autosync.sh rollback <SHA> --hard

# Ou abrir o menu interativo com lista e confirmação
./autosync.sh rollback
```

### Rodar os Testes Automatizados
```bash
python3 -m unittest tests/test_autosync.py
```

### Parar a automação
```bash
./autosync.sh stop
```

---

## ⚙️ Configurações (`config.json`)

Você pode customizar o comportamento no arquivo `config.json`:

```json
{
  "poll_interval": 10,
  "check_interval_seconds": 10,
  "debounce_seconds": 15,
  "network_timeout_seconds": 15,
  "alert_cooldown_seconds": 300,
  "notify_macos": true,
  "max_checkpoints": 20,
  "ignored_patterns": [
    ".git/*",
    ".DS_Store",
    "*.swp",
    "*.tmp",
    "*~",
    "*.log"
  ]
}
```

