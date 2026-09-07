# Lista de Projetos Bash (`.sh`)

## 1. Como vamos organizar

Sim, a ideia é exatamente esta:

```text
projeto/
├── README.md
├── scripts/
│   └── projeto.sh
├── tests/
│   └── test.sh
├── fixtures/
│   └── dados-exemplo.txt
├── configs/
│   └── projeto.conf.example
└── evidence/
    └── resultado.txt
```

O arquivo `.sh` contém o código Bash executável. Porém, um projeto profissional não deve conter apenas o `.sh`; ele também precisa explicar como executar, testar, configurar e corrigir problemas.

### Exemplo mínimo

```text
projects/system-inventory/
├── README.md
├── scripts/
│   └── system-inventory.sh
└── tests/
    └── test.sh
```

### Exemplo com vários scripts

```text
projects/backup-manager/
├── README.md
├── scripts/
│   ├── backup.sh
│   ├── restore.sh
│   └── verify-backup.sh
├── configs/
│   └── backup.conf.example
├── tests/
│   └── test.sh
└── evidence/
```

Portanto, **sim, vamos criar as pastas e dentro delas os arquivos `.sh`**. Em projetos maiores, podemos ter vários scripts com responsabilidades diferentes.

---

## 2. Regra de nomenclatura

Use nomes em minúsculas, separados por hífen:

```text
health-check.sh
backup-manager.sh
log-analyzer.sh
```

Evite:

```text
Meu Script.sh
script_final_definitivo_v2.sh
SCRIPT1.SH
```

Nomes recomendados:

| Tipo | Padrão | Exemplo |
|---|---|---|
| Script principal | `nome-do-projeto.sh` | `system-inventory.sh` |
| Teste | `test.sh` | `tests/test.sh` |
| Configuração modelo | `.conf.example` | `backup.conf.example` |
| Biblioteca Bash | `.lib.sh` | `common.lib.sh` |
| Execução simulada | `dry-run.sh` ou opção `--dry-run` | `deploy.sh --dry-run` |

Todo script deve começar com:

```bash
#!/usr/bin/env bash
set -Eeuo pipefail
```

Depois de criar o arquivo:

```bash
chmod +x scripts/nome-do-projeto.sh
bash -n scripts/nome-do-projeto.sh
```

---

## 3. Lista de projetos por nível

## Nível 1 — Bash e Linux básico

Criar dentro de:

```text
projects/01-fundamentos/
```

| Nº | Pasta do projeto | Arquivo principal | Objetivo |
|---:|---|---|---|
| 01 | `hello-bash` | `hello-bash.sh` | Primeiro script Bash |
| 02 | `system-info` | `system-info.sh` | Exibir hostname, usuário, kernel e uptime |
| 03 | `date-report` | `date-report.sh` | Gerar relatório com data e hora |
| 04 | `argument-reader` | `argument-reader.sh` | Ler argumentos posicionais |
| 05 | `interactive-menu` | `interactive-menu.sh` | Criar menu com `select` ou `case` |
| 06 | `calculator` | `calculator.sh` | Operações matemáticas básicas |
| 07 | `file-creator` | `file-creator.sh` | Criar estrutura de arquivos |
| 08 | `directory-checker` | `directory-checker.sh` | Verificar se diretórios existem |
| 09 | `file-counter` | `file-counter.sh` | Contar arquivos por extensão |
| 10 | `text-transformer` | `text-transformer.sh` | Converter, filtrar e formatar texto |

Exemplo:

```text
projects/01-fundamentos/hello-bash/
├── README.md
├── scripts/
│   └── hello-bash.sh
└── tests/
    └── test.sh
```

---

## Nível 2 — Arquivos e filesystem

Criar dentro de:

```text
projects/02-filesystem/
```

| Nº | Pasta do projeto | Arquivo principal | Objetivo |
|---:|---|---|---|
| 11 | `file-organizer` | `file-organizer.sh` | Organizar arquivos por extensão |
| 12 | `duplicate-finder` | `duplicate-finder.sh` | Encontrar arquivos duplicados por checksum |
| 13 | `large-files-report` | `large-files-report.sh` | Listar arquivos grandes |
| 14 | `empty-files-cleaner` | `empty-files-cleaner.sh` | Localizar arquivos vazios com modo seguro |
| 15 | `temporary-files-cleaner` | `temporary-files-cleaner.sh` | Limpar arquivos temporários controlados |
| 16 | `directory-backup` | `directory-backup.sh` | Compactar um diretório |
| 17 | `permissions-report` | `permissions-report.sh` | Gerar relatório de permissões |
| 18 | `symlink-manager` | `symlink-manager.sh` | Criar e validar links simbólicos |
| 19 | `disk-usage-report` | `disk-usage-report.sh` | Gerar relatório de uso do disco |
| 20 | `inode-monitor` | `inode-monitor.sh` | Verificar consumo de inodes |

Exemplo:

```text
projects/02-filesystem/directory-backup/
├── README.md
├── scripts/
│   ├── backup.sh
│   └── verify-backup.sh
├── configs/
│   └── backup.conf.example
├── tests/
│   └── test.sh
└── evidence/
```

---

## Nível 3 — Usuários e permissões

Criar dentro de:

```text
projects/03-users-permissions/
```

| Nº | Pasta do projeto | Arquivo principal | Objetivo |
|---:|---|---|---|
| 21 | `user-report` | `user-report.sh` | Listar usuários do sistema |
| 22 | `group-report` | `group-report.sh` | Listar grupos e membros |
| 23 | `permission-audit` | `permission-audit.sh` | Encontrar permissões inadequadas |
| 24 | `home-audit` | `home-audit.sh` | Verificar diretórios home |
| 25 | `sudo-audit` | `sudo-audit.sh` | Relatar configurações de sudo |
| 26 | `ssh-key-report` | `ssh-key-report.sh` | Inventariar chaves públicas |
| 27 | `shared-directory-setup` | `setup-shared-directory.sh` | Criar diretório compartilhado controlado |
| 28 | `inactive-users-report` | `inactive-users-report.sh` | Identificar contas sem atividade |

Esses exercícios devem ser feitos primeiro em ambiente de laboratório. Scripts que criam usuários, alteram grupos ou modificam `sudoers` precisam de revisão cuidadosa.

---

## Nível 4 — Processos e recursos

Criar dentro de:

```text
projects/04-processes/
```

| Nº | Pasta do projeto | Arquivo principal | Objetivo |
|---:|---|---|---|
| 29 | `process-report` | `process-report.sh` | Listar processos por CPU e memória |
| 30 | `process-monitor` | `process-monitor.sh` | Monitorar um processo específico |
| 31 | `high-cpu-alert` | `high-cpu-alert.sh` | Alertar CPU acima do limite |
| 32 | `high-memory-alert` | `high-memory-alert.sh` | Alertar memória acima do limite |
| 33 | `zombie-process-report` | `zombie-process-report.sh` | Detectar processos zumbis |
| 34 | `service-process-check` | `service-process-check.sh` | Relacionar serviço e processo |
| 35 | `graceful-stop` | `graceful-stop.sh` | Encerrar processo com tentativa controlada |
| 36 | `resource-snapshot` | `resource-snapshot.sh` | Salvar fotografia de recursos do host |

---

## Nível 5 — Serviços e systemd

Criar dentro de:

```text
projects/05-services/
```

| Nº | Pasta do projeto | Arquivo principal | Objetivo |
|---:|---|---|---|
| 37 | `service-status` | `service-status.sh` | Verificar status de serviços |
| 38 | `service-health-check` | `service-health-check.sh` | Validar serviço e endpoint |
| 39 | `service-restart` | `service-restart.sh` | Reiniciar serviço com controle |
| 40 | `service-watchdog` | `service-watchdog.sh` | Monitorar e registrar falhas |
| 41 | `systemd-report` | `systemd-report.sh` | Relatar units ativas e falhas |
| 42 | `systemd-timer-manager` | `timer-manager.sh` | Criar e validar timers |
| 43 | `failed-units-report` | `failed-units-report.sh` | Listar units que falharam |

O projeto `service-restart` deve começar com modo somente leitura e exigir `--repair` para tentar uma correção.

---

## Nível 6 — Rede, DNS e HTTP

Criar dentro de:

```text
projects/06-networking/
```

| Nº | Pasta do projeto | Arquivo principal | Objetivo |
|---:|---|---|---|
| 44 | `network-report` | `network-report.sh` | Relatar interfaces e endereços |
| 45 | `route-report` | `route-report.sh` | Relatar tabela de rotas |
| 46 | `port-check` | `port-check.sh` | Verificar porta TCP |
| 47 | `dns-check` | `dns-check.sh` | Resolver nomes e registrar resultado |
| 48 | `dns-record-report` | `dns-record-report.sh` | Consultar registros DNS |
| 49 | `http-health-check` | `http-health-check.sh` | Verificar URL, status e tempo |
| 50 | `endpoint-monitor` | `endpoint-monitor.sh` | Monitorar várias URLs |
| 51 | `certificate-expiry-check` | `certificate-expiry-check.sh` | Verificar validade de certificado |
| 52 | `network-diagnostics` | `network-diagnostics.sh` | Coletar diagnóstico de rede |

Exemplo de projeto com endpoints:

```text
projects/06-networking/endpoint-monitor/
├── README.md
├── scripts/
│   └── endpoint-monitor.sh
├── configs/
│   └── endpoints.txt
├── tests/
│   └── test.sh
└── evidence/
```

---

## Nível 7 — Logs e troubleshooting

Criar dentro de:

```text
projects/07-logs-troubleshooting/
```

| Nº | Pasta do projeto | Arquivo principal | Objetivo |
|---:|---|---|---|
| 53 | `log-summary` | `log-summary.sh` | Resumir quantidade de linhas e erros |
| 54 | `error-counter` | `error-counter.sh` | Contar erros por tipo |
| 55 | `journal-report` | `journal-report.sh` | Extrair eventos do journald |
| 56 | `failed-login-report` | `failed-login-report.sh` | Relatar tentativas de login falhas |
| 57 | `log-rotation-check` | `log-rotation-check.sh` | Verificar rotação de logs |
| 58 | `incident-evidence` | `collect-evidence.sh` | Coletar evidências de incidente |
| 59 | `service-diagnosis` | `diagnose-service.sh` | Diagnosticar serviço indisponível |
| 60 | `disk-full-diagnosis` | `diagnose-disk.sh` | Investigar disco cheio |

---

## Nível 8 — Agendamento e automação

Criar dentro de:

```text
projects/08-automation/
```

| Nº | Pasta do projeto | Arquivo principal | Objetivo |
|---:|---|---|---|
| 61 | `scheduled-report` | `scheduled-report.sh` | Gerar relatório agendado |
| 62 | `lock-manager` | `lock-manager.sh` | Impedir execuções simultâneas |
| 63 | `job-runner` | `job-runner.sh` | Executar tarefas com logs |
| 64 | `retry-command` | `retry-command.sh` | Repetir comando com limite |
| 65 | `notification-wrapper` | `notification-wrapper.sh` | Encapsular sucesso e erro |
| 66 | `config-loader` | `config-loader.sh` | Carregar configurações externas |
| 67 | `dry-run-automation` | `automation.sh` | Simular mudanças sem aplicá-las |
| 68 | `cleanup-manager` | `cleanup-manager.sh` | Limpar artefatos antigos com retenção |

---

## Nível 9 — Projetos integradores de DevOps

Criar dentro de:

```text
projects/09-devops/
```

| Nº | Pasta do projeto | Arquivo principal | Objetivo |
|---:|---|---|---|
| 69 | `system-inventory` | `system-inventory.sh` | Inventário completo do servidor |
| 70 | `health-check` | `health-check.sh` | Verificação geral de saúde |
| 71 | `backup-manager` | `backup.sh` | Backup, checksum, retenção e restauração |
| 72 | `log-analyzer` | `log-analyzer.sh` | Análise automatizada de logs |
| 73 | `service-monitor` | `service-monitor.sh` | Monitoramento e recuperação controlada |
| 74 | `deployment-helper` | `deploy.sh` | Deploy com validação e rollback |
| 75 | `release-manager` | `release.sh` | Criar e validar versões |
| 76 | `environment-check` | `environment-check.sh` | Validar pré-requisitos de ambiente |
| 77 | `server-readiness` | `readiness.sh` | Verificar se servidor está pronto |
| 78 | `operations-dashboard-data` | `collect-metrics.sh` | Coletar dados para observabilidade |

---

## 4. Comando para criar a estrutura inicial

Execute na raiz do laboratório:

```bash
cd /home/Projetos/Linux/junior

mkdir -p projects/{01-fundamentos,02-filesystem,03-users-permissions,04-processes,05-services,06-networking,07-logs-troubleshooting,08-automation,09-devops}
```

Para criar todos os projetos listados:

```bash
cd /home/Projetos/Linux/junior

projects=(
  hello-bash system-info date-report argument-reader interactive-menu calculator
  file-creator directory-checker file-counter text-transformer
  file-organizer duplicate-finder large-files-report empty-files-cleaner
  temporary-files-cleaner directory-backup permissions-report symlink-manager
  disk-usage-report inode-monitor
  user-report group-report permission-audit home-audit sudo-audit ssh-key-report
  shared-directory-setup inactive-users-report
  process-report process-monitor high-cpu-alert high-memory-alert
  zombie-process-report service-process-check graceful-stop resource-snapshot
  service-status service-health-check service-restart service-watchdog systemd-report
  systemd-timer-manager failed-units-report
  network-report route-report port-check dns-check dns-record-report http-health-check
  endpoint-monitor certificate-expiry-check network-diagnostics
  log-summary error-counter journal-report failed-login-report log-rotation-check
  incident-evidence service-diagnosis disk-full-diagnosis
  scheduled-report lock-manager job-runner retry-command notification-wrapper
  config-loader dry-run-automation cleanup-manager
  system-inventory health-check backup-manager log-analyzer service-monitor
  deployment-helper release-manager environment-check server-readiness
  operations-dashboard-data
)

for projeto in "${projects[@]}"; do
  mkdir -p "projects/$projeto/{scripts,tests,fixtures,configs,evidence}"
  touch "projects/$projeto/README.md"
done
```

> Observação: em Bash, a expansão com chaves dentro de uma string entre aspas não cria todas as subpastas. Para garantir o resultado corretamente, use o comando abaixo no lugar do loop anterior.

```bash
for projeto in "${projects[@]}"; do
  mkdir -p "projects/$projeto"/scripts \
           "projects/$projeto"/tests \
           "projects/$projeto"/fixtures \
           "projects/$projeto"/configs \
           "projects/$projeto"/evidence
  touch "projects/$projeto/README.md"
done
```

Validar:

```bash
find projects -maxdepth 3 -type f | sort
find projects -maxdepth 2 -type d | sort
```

---

## 5. Criar o primeiro script

Exemplo para o projeto `hello-bash`:

```bash
cd /home/Projetos/Linux/junior

cat > projects/01-fundamentos/hello-bash/scripts/hello-bash.sh <<'EOF'
#!/usr/bin/env bash
set -Eeuo pipefail

name="${1:-Linux}"
printf 'Olá, %s!\n' "$name"
EOF

chmod +x projects/01-fundamentos/hello-bash/scripts/hello-bash.sh
bash -n projects/01-fundamentos/hello-bash/scripts/hello-bash.sh
projects/01-fundamentos/hello-bash/scripts/hello-bash.sh DevOps
```

Resultado esperado:

```text
Olá, DevOps!
```

---

## 6. Modelo de `README.md` de cada projeto

```markdown
# Nome do projeto

## Objetivo

Explique qual problema o script resolve.

## Pré-requisitos

- Bash 5 ou superior
- Comandos necessários
- Permissões necessárias

## Arquivos

| Arquivo | Função |
|---|---|
| `scripts/nome.sh` | Script principal |
| `tests/test.sh` | Testes |
| `configs/nome.conf.example` | Configuração modelo |

## Execução

```bash
bash scripts/nome.sh
```

## Opções

```text
--help
--dry-run
--verbose
```

## Resultado esperado

## Cenários de erro

## Limpeza

## Limitações

## Aprendizados
```

---

## 7. Modelo de teste

Arquivo `tests/test.sh`:

```bash
#!/usr/bin/env bash
set -Eeuo pipefail

readonly SCRIPT="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")/../scripts" && pwd)/hello-bash.sh"

output="$($SCRIPT DevOps)"

if [[ "$output" == 'Olá, DevOps!' ]]; then
  printf '[PASS] saudação com nome\n'
else
  printf '[FAIL] saída inesperada: %s\n' "$output" >&2
  exit 1
fi
```

Executar:

```bash
chmod +x tests/test.sh
bash tests/test.sh
```

---

## 8. Ordem recomendada de estudo

Não é necessário criar todos os 78 projetos de uma vez. A ordem recomendada é:

```text
1. hello-bash
2. system-info
3. argument-reader
4. file-counter
5. directory-checker
6. file-organizer
7. permissions-report
8. process-report
9. service-status
10. disk-usage-report
11. dns-check
12. http-health-check
13. log-summary
14. backup-manager
15. system-inventory
16. health-check
17. service-monitor
18. deployment-helper
```

A cada projeto, pratique:

```text
entender o problema
  ↓
criar o README
  ↓
criar o script .sh
  ↓
testar entrada válida
  ↓
testar entrada inválida
  ↓
executar ShellCheck
  ↓
documentar o resultado
  ↓
criar commit Git
```

---

## Resposta direta

Sim. A estrutura será baseada em:

```text
pasta do projeto/
├── README.md
├── scripts/
│   └── projeto.sh
└── tests/
    └── test.sh
```

O `.sh` é o script Bash principal. À medida que o projeto ficar maior, podemos adicionar outros `.sh`, arquivos de configuração, dados de teste e scripts de validação.

O primeiro objetivo não é criar centenas de scripts sem organização. É criar projetos pequenos, completos, testados e documentados. Depois agruparemos os projetos menores em automações maiores de DevOps.
