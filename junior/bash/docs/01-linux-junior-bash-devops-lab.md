# 📘 Laboratório Linux Junior — Bash, Automação e DevOps

> **Manual Prático e Guia Didático do Professor**  
> Este documento é o manual mestre de aprendizado do laboratório `/home/Projetos/Linux/junior`. Aqui você aprenderá Linux e Bash da forma como os Engenheiros de Infraestrutura e DevOps trabalham no mercado: investigando o sistema, escrevendo automações seguras, testando cenários de falha, diagnosticando a causa raiz e integrando soluções em esteiras de CI/CD.

---

## 👨‍🏫 Visão Geral da Metodologia Didática

A regra de ouro de todo o treinamento é o **Ciclo de Engenharia**:

> **Estudar → Implementar → Quebrar em ambiente controlado → Diagnosticar → Automatizar → Monitorar → Documentar → Melhorar.**

Nesta pasta `junior`, você não irá apenas memorizar comandos isolados. Cada tópico técnico exige:
1. Entendimento teórico da arquitetura do Linux.
2. Implementação em script Bash limpo e legível.
3. Testes em ambiente isolado (containers/VMCs).
4. Registro de evidências de execução (`evidence/`).
5. Documentação em Markdown do aprendizado obtido (`README.md`).

---

## 1. Princípios de Trabalho em Engenharia

### 1.1 Segurança antes da Velocidade
Nunca execute ou teste comandos destrutivos diretamente em máquinas de produção. Para praticar com segurança, utilize máquinas virtuais de desenvolvimento, containers Docker descartáveis e privilégios limitados.

Comandos de alto risco como `rm -rf`, `mkfs`, `dd`, `fdisk`, `parted`, `chmod -R`, `chown -R`, alterações em `/etc` ou alterações de firewall podem causar indisponibilidade imediata ou perda irrecuperável de dados.

**Checklist pré-execução (Execute antes de rodar qualquer comando privilegiado):**

```bash
pwd        # Em qual pasta eu estou exatamente?
whoami     # Qual é o meu usuário atual?
hostname   # Em qual servidor eu estou conectado?
id         # Quais são meus privilégios de grupo?
sudo -l    # O que posso executar com sudo sem senha?
```

---

### 1.2 Idempotência

> **Nota do Professor:** Um script é considerado **idempotente** quando pode ser executado 1, 10 ou 100 vezes seguidas no mesmo servidor, e o estado final do sistema permanece exatamente o mesmo, sem criar duplicidades ou erros.

#### ❌ Exemplo NÃO Idempotente (Ruim):
```bash
# Se rodar 5 vezes, adicionará 5 linhas idênticas ao arquivo!
echo "export APP_ENV=dev" >> ~/.bashrc
```

#### ✅ Exemplo Idempotente (Profissional):
```bash
# Verifica se a linha já existe antes de adicionar
grep -qxF 'export APP_ENV=dev' ~/.bashrc || echo 'export APP_ENV=dev' >> ~/.bashrc
```

---

### 1.3 Reprodutibilidade
Tudo o que for necessário para reproduzir um exercício ou automação deve estar versionado no repositório: o script principal, arquivos de configuração de exemplo, dados de teste (`fixtures`), scripts de teste automatizado e instruções claras.

---

### 1.4 Princípio do Menor Privilégio
Execute scripts com um usuário comum sem privilégios sempre que possível. Utilize o `sudo` pontualmente apenas para o comando específico que exige acesso root. NUNCA grave senhas, tokens de API ou chaves privadas dentro de scripts versionados.

---

### 1.5 Observabilidade desde o Início
Todo script operacional deve informar claramente o que está realizando através de logs estruturados (com marcação de data/hora), retornar códigos de saída (`exit codes`) corretos e direcionar mensagens de erro para a saída de erro padrão (`stderr`).

---

## 2. Estrutura de Diretórios Recomendada

A organização modular do repositório `/home/Projetos/Linux/junior` é mantida por tópicos de conhecimento:

```text
junior/
├── bash/                    → Fundamentos, sintaxe, controle de erro e bibliotecas
├── cron/                    → Tarefas agendadas e gerenciamento de locks
├── dns/                     → Resolução de nomes, dig, nslookup, bind
├── filesystem/              → Estrutura de arquivos, permissões, symlinks
├── logs/                    → Logrotate, journalctl, parsing com grep/awk/sed
├── networking/              → Endereçamento IP, rotas, ss, curl, firewalls
├── packages/                → Gestão de pacotes apt, repositórios, dpkg
├── processes/               → Gerenciamento de PIDs, sinais, recursos
├── services/                → Systemctl, recuperação de serviços
├── ssh/                     → Autenticação por chave, hardening, scp, rsync
├── storage/                 → Discos, mounts, LVM, backups e restauração
├── systemd/                 → Units customizadas, timers e logs
├── troubleshooting/         → Incidentes, evidencias e runbooks
├── users-permissions/       → Usuários, grupos, sudoers e ACLs
└── web-server/              → Nginx, health checks e reverse proxy
```

### Convenção Interna de Subpastas por Exercício
Dentro de cada tópico ou projeto prático, adote a seguinte divisão:

```text
<exercicio-ou-projeto>/
├── README.md              # Teoria, objetivo, pré-requisitos e instruções de uso
├── scripts/               # Scripts executáveis (.sh ou executável sem extensão)
├── configs/               # Arquivos de configuração modelo (.env.example, .conf)
├── fixtures/              # Dados estáticos para testes e mocks
├── tests/                 # Scripts de teste automatizado (BATS ou Bash)
├── evidence/              # Logs e provas de execução do exercício
└── notes/                 # Anotações de troubleshooting e postmortems
```

---

## 3. Guia Didático de Bash Essencial

### 3.1 Shebang e Permissão de Execução

Todo script Bash deve iniciar com a declaração do interpretador:

```bash
#!/usr/bin/env bash

printf 'Olá, Linux DevOps!\n'
```

#### Como Executar Corretamente:
```bash
# 1. Tornar o arquivo executável:
chmod +x hello.sh

# 2. Executar via caminho relativo ou absoluto:
./hello.sh

# 3. Ou invocar explicitamente pelo Bash (não exige chmod +x):
bash hello.sh
```

> **Diferença importante:** `./hello.sh` utiliza o interpretador definido no Shebang (`#!/usr/bin/env bash`). Invocá-lo com `sh hello.sh` usará o interpretador posix padronizado `/bin/sh` (que não suporta muitos recursos avançados do Bash como `[[ ]]` ou arrays).

---

### 3.2 Variáveis, Escopo e Aspas

```bash
readonly SCRIPT_NAME="inventory"  # Constante (não pode ser alterada)
export APP_ENV="dev"             # Exportada para processos filhos

nome="laboratorio"
printf 'Projeto: %s\n' "$nome"
```

#### 🚨 Por que usar ASPAS DUPLAS sempre?

```bash
arquivo="meu arquivo com espacos.txt"

# ❌ ERRADO: O Bash entenderá como 4 arquivos separados!
cat $arquivo

# ✅ CORRETO: O Bash preserva o nome como uma única string!
cat "$arquivo"
```

---

### 3.3 Redirecionamentos de Entrada e Saída

```text
  >    Sobrescreve o arquivo com a saída padrão (stdout - 1)
  >>   Adiciona ao final do arquivo (append - stdout - 1)
  2>   Redireciona a saída de erros (stderr - 2)
  &>   Redireciona stdout e stderr juntos para o mesmo local
  <    Lê o conteúdo de um arquivo para o comando (stdin - 0)
```

```bash
# Exemplo de busca limpa ignorando erros de permissão negada:
find /var/log -name "*.log" 2>/dev/null

# Filtrar processos do Nginx sem exibir o próprio grep no resultado:
ps aux | grep '[n]ginx'
```

---

### 3.4 Códigos de Saída (`Exit Status`)

Por convenção universal nos sistemas Unix:
* **`0`**: Sucesso total.
* **`1 a 255`**: Erro ou falha na execução.

```bash
if [[ -f /etc/hosts ]]; then
  printf '[OK] Arquivo de hosts encontrado.\n'
  exit 0
else
  printf '[ERRO] Arquivo /etc/hosts ausente!\n' >&2
  exit 1
fi
```

---

### 3.5 Modelo de Script Operacional Seguro (Template de Produção)

Utilize este modelo como esqueleto base para todos os seus scripts de produção:

```bash
#!/usr/bin/env bash
# =============================================================================
# ARQUIVO: template-seguro.sh
# DESCRIÇÃO: Template robusto com controle de erro, logs e traps
# =============================================================================
set -Eeuo pipefail

readonly SCRIPT_NAME="$(basename "$0")"
readonly SCRIPT_DIR="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"

# Função de Log Estruturado
log() {
  local level="$1"
  shift
  printf '[%s] [%s] %s\n' "$(date --iso-8601=seconds)" "$level" "$*"
}

die() {
  log ERROR "$*"
  exit 1
}

# Limpeza automática ao encerrar (Garanta que não fiquem temporários soltos)
cleanup() {
  local status=$?
  # Remova arquivos temporários aqui
  exit "$status"
}
trap cleanup EXIT
trap 'die "Falha crítica na linha $LINENO executando: $BASH_COMMAND"' ERR

usage() {
  cat <<EOF
Uso: $SCRIPT_NAME [opções]

Opções:
  -h, --help    Exibe esta ajuda.
EOF
}

main() {
  log INFO "Iniciando $SCRIPT_NAME..."
  
  if [[ "${1:-}" == "-h" || "${1:-}" == "--help" ]]; then
    usage
    exit 0
  fi

  log INFO "Processamento finalizado com sucesso."
}

main "$@"
```

---

## 4. Principais Ferramentas Linux que Você Vai Dominar

```
 ┌────────────────────────────────────────────────────────────────────────┐
 │ FERRAMENTAS CLAVE DO ENGENHEIRO LINUX & DEVOPS                        │
 │                                                                        │
 │  • Navegação & Arquivos: pwd, ls, cd, find, stat, file, realpath       │
 │  • Texto & Dados:        grep, cut, sort, uniq, awk, sed, tr, jq       │
 │  • Permissões & Usuários: whoami, id, chmod, chown, umask, getfacl     │
 │  • Processos & Recursos: ps, top, pgrep, kill, free, uptime, vmstat    │
 │  • Serviços & Logs:      systemctl, journalctl, logrotate, dmesg       │
 │  • Redes & HTTP:         ip, ss, ping, dig, curl, wget, nc, ufw        │
 │  • Storage & Backup:     df, du, lsblk, mount, tar, sha256sum, rsync   │
 └────────────────────────────────────────────────────────────────────────┘
```

### Exemplos Práticos Rápidos

```bash
# 1. Buscar a palavra "error" nos logs ignorando maiúsculas:
grep -Rni --include='*.log' 'error' /var/log/

# 2. Extrair apenas o nome dos usuários do arquivo /etc/passwd:
cut -d: -f1 /etc/passwd

# 3. Contar IPs únicos que mais fizeram requisições em um log:
awk '{print $1}' access.log | sort | uniq -c | sort -nr | head -n 10

# 4. Verificar se a porta 8080 está aberta no servidor:
ss -tulpn | grep 8080

# 5. Medir o tempo de resposta HTTP com curl:
curl -fsS -o /dev/null -w "Status: %{http_code} - Tempo Total: %{time_total}s\n" https://example.com
```

---

## 5. Automação com Cron vs Systemd Timers

| Característica | Cron | Systemd Timer |
|---|---|---|
| **Facilidade de configuração** | Alta (`crontab -e`) | Média (exige `.service` e `.timer`) |
| **Ambiente de execução** | Reduzido (PATH limitado) | Completo e configurável no `.service` |
| **Gerenciamento de Logs** | Exige redirecionar para arquivo | Integrado nativamente no `journalctl` |
| **Controle de Dependências** | Não possui | Nativo (ex: aguardar rede ativa) |
| **Proteção de Execução Simultânea** | Requer `flock` externo | Nativo |

### Exemplo de Timer no Systemd

#### 1. Arquivo de Serviço (`/etc/systemd/system/health-check.service`):
```ini
[Unit]
Description=Laboratório - Verificação de Saúde do Servidor

[Service]
Type=oneshot
ExecStart=/home/Projetos/Linux/junior/bash/projects/junior-08-automation/health-check/scripts/health-check.sh
```

#### 2. Arquivo de Timer (`/etc/systemd/system/health-check.timer`):
```ini
[Unit]
Description=Executa o Health Check a cada 5 minutos

[Timer]
OnBootSec=1min
OnUnitActiveSec=5min
Persistent=true

[Install]
WantedBy=timers.target
```

```bash
# Ativar e testar o timer:
sudo systemctl daemon-reload
sudo systemctl enable --now health-check.timer
systemctl list-timers
```

---

## 6. Qualidade, Testes e Integração Contínua (CI/CD)

Antes de considerar qualquer script pronto:
1. **Validação de Sintaxe:** `bash -n script.sh`
2. **Análise Estática de Qualidade:** `shellcheck script.sh`
3. **Testes Automatizados:** Escreva testes usando `BATS` em `tests/*.bats`.

```bash
# Exemplo de comando do pipeline CI/CD no GitHub Actions:
find . -type f -name '*.sh' -print0 | xargs -0 -r shellcheck
```

---

## 🎓 Conclusão e Próximos Passos

Agora que você conhece todos os princípios de engenharia, a estrutura de pastas e a metodologia de aprendizado:

1. Acesse a pasta `projects/junior-01-fundamentos/hello-bash/`.
2. Analise a arquitetura explicada no arquivo [04 - Lista de Pastas](04-lista-Pastas.md).
3. Consulte o catálogo dos 139 projetos em [04 - Lista Geral](04-lista-geral.md).
4. Bom aprendizado e excelente prática! 🚀
