# 🗺️ Lista Geral dos 139 Projetos Práticos — Trilhas Junior (Bash & DevOps)

> **Guia do Professor:** Esta é a matriz curricular completa dos 139 projetos práticos de automação Linux e DevOps. Cada projeto foi desenhado para ser desenvolvido dentro da sua respectiva pasta em `projects/`, contendo a estrutura padronizada com `scripts/`, `tests/`, `configs/`, `fixtures/` e `README.md`.

---

## 🟢 Nível Junior 1 — Fundamentos do Bash
> **Foco Didático:** Aprender sintaxe básica de Shell, declaração de variáveis, passagem de argumentos posicionais, manipulação de strings, condicionais (`if/else/case`), loops (`for/while`), funções e códigos de saída (`exit status`).  
> **Caminho das pastas:** `projects/junior-01-fundamentos/<nome-do-projeto>/`

### 🎓 Nota do Professor (Nível 1):
*Neste nível inicial, o maior aprendizado é entender que todo comando executado no terminal retorna um número entre 0 e 255 (o `exit status`, acessado via `$?`). Aprenda a usar sempre `set -Eeuo pipefail` e a colocar todas as expansões de variáveis entre aspas duplo `"$VAR"` para evitar quebras por espaços ou expansão de globbing inadequada.*

| Nº | Projeto | Script Principal | Objetivo Didático | Comandos Chave |
|---|---|---|---|---|
| 01 | `hello-bash` | `hello-bash.sh` | Criar o primeiro script Bash executável com tratamento de argumentos | `printf`, `chmod`, `read` |
| 02 | `system-info` | `system-info.sh` | Exibir informações básicas de hostname, kernel, sistema operacional e uptime | `hostname`, `uname`, `uptime` |
| 03 | `date-report` | `date-report.sh` | Gerar relatórios formatados contendo data, hora e marcações ISO-8601 | `date`, `printf`, `strftime` |
| 04 | `argument-reader` | `argument-reader.sh` | Ler, validar e iterar sobre argumentos posicionais (`$1`, `$2`, `$#`, `"$@"`) | `$1`, `$#`, `"$@"`, `shift` |
| 05 | `variable-manager` | `variable-manager.sh` | Trabalhar com variáveis locais, exportadas, constantes `readonly` e escopos | `export`, `readonly`, `unset` |
| 06 | `interactive-menu` | `interactive-menu.sh` | Criar menus de opções interativos utilizando `select` ou blocos `case` | `select`, `case`, `PS3` |
| 07 | `calculator` | `calculator.sh` | Operações matemáticas básicas e expressões aritméticas no Shell | `$((...))`, `bc`, `expr` |
| 08 | `number-validator` | `number-validator.sh` | Validar entradas numéricas e intervalos usando Expressões Regulares em `[[ ]]` | `[[ =~ ]]`, `integer check` |
| 09 | `string-validator` | `string-validator.sh` | Validar tamanho de strings, textos vazios e buscas de sub-strings | `${#var}`, `[[ -z ]]`, `[[ -n ]]` |
| 10 | `user-greeting` | `user-greeting.sh` | Cumprimentar o usuário dinamicamente com base no horário do sistema | `date +%H`, `if/elif/else` |
| 11 | `file-creator` | `file-creator.sh` | Criar arquivos a partir de parâmetros passados com checagem de erros | `touch`, `mkdir`, `test -f` |
| 12 | `directory-creator` | `directory-creator.sh` | Criar estrutura de diretórios com validação de existência prévia | `mkdir -p`, `[[ -d ]]` |
| 13 | `command-checker` | `command-checker.sh` | Verificar se utilitários necessários estão instalados no sistema | `command -v`, `type`, `which` |
| 14 | `exit-code-demo` | `exit-code-demo.sh` | Praticar tratamento e retornos de códigos de saída (`exit 0`, `exit 1`) | `exit`, `$?`, `return` |
| 15 | `simple-menu-system` | `menu.sh` | Sistema de menu robusto com tratamento de erros de navegação | `while true`, `read -r`, `trap` |

---

## 🔵 Nível Junior 2 — Arquivos e Filesystem
> **Foco Didático:** Manipulação avançada do sistema de arquivos do Linux, navegação, gerenciamento de permissões octais/simbólicas, links simbólicos (`symlinks`), busca refinada de arquivos (`find`), ordenação, temporários e validação de integridade (`checksums`).  
> **Caminho das pastas:** `projects/junior-02-filesystem/<nome-do-projeto>/`

### 🎓 Nota do Professor (Nível 2):
*O sistema de arquivos do Linux trata tudo como arquivo (incluindo dispositivos e sockets). Aprenda a usar o comando `find` com a opção `-print0` combinado com `xargs -0` para processar arquivos que possuem espaços ou caracteres especiais no nome de maneira 100% segura.*

| Nº | Projeto | Script Principal | Objetivo Didático | Comandos Chave |
|---|---|---|---|---|
| 16 | `file-counter` | `file-counter.sh` | Contar arquivos por extensão e tipo em uma árvore de diretórios | `find`, `wc -l`, `sort` |
| 17 | `directory-checker` | `directory-checker.sh` | Verificar e auditar a existência e acessibilidade de diretórios | `[[ -d ]]`, `[[ -r ]]`, `[[ -w ]]` |
| 18 | `file-checker` | `file-checker.sh` | Verificar metadados, permissões e tipos MIME de arquivos | `stat`, `file`, `ls -l` |
| 19 | `file-organizer` | `file-organizer.sh` | Reorganizar automaticamente arquivos soltos em subpastas por extensão | `mv`, `mkdir -p`, `basename` |
| 20 | `extension-report` | `extension-report.sh` | Gerar relatórios estatísticos sobre o volume ocupado por cada extensão | `awk`, `du`, `sort -n` |
| 21 | `large-files-report` | `large-files-report.sh` | Localizar arquivos que excedem um limite de tamanho predefinido | `find -size`, `ls -lh`, `du` |
| 22 | `empty-files-report` | `empty-files-report.sh` | Encontrar e auditar arquivos e diretórios vazios no sistema | `find -empty`, `rmdir` |
| 23 | `duplicate-finder` | `duplicate-finder.sh` | Identificar arquivos duplicados comparando hashes MD5/SHA256 | `sha256sum`, `sort`, `uniq -w` |
| 24 | `temporary-files-cleaner` | `clean-temporary.sh` | Limpar arquivos temporários antigos de forma segura (com `--dry-run`) | `mktemp`, `find -mtime`, `rm` |
| 25 | `old-files-report` | `old-files-report.sh` | Listar arquivos não modificados há mais de X dias | `find -mtime`, `stat` |
| 26 | `permissions-report` | `permissions-report.sh` | Auditar arquivos com permissões abertas demais (ex: 777) | `find -perm`, `ls -l` |
| 27 | `symlink-manager` | `symlink-manager.sh` | Criar, auditar e corrigir links simbólicos quebrados (`broken symlinks`) | `ln -s`, `readlink -f`, `test -L` |
| 28 | `directory-backup` | `directory-backup.sh` | Compactar diretórios em arquivos `.tar.gz` preservando atributos | `tar -czfp`, `gzip` |
| 29 | `checksum-manager` | `checksum-manager.sh` | Gerar e verificar arquivos `.sha256` para auditoria de arquivos | `sha256sum -c` |
| 30 | `file-integrity-check` | `integrity-check.sh` | Monitorar alterações não autorizadas em arquivos críticos de sistema | `diff`, `cmp`, `sha256sum` |

---

## 🟡 Nível Junior 3 — Processos, Usuários e Permissões
> **Foco Didático:** Administração básica do sistema operando como Administrador de Sistemas. Monitoramento de processos, gerenciamento de sinais (`kill`, `trap`), privilégios `sudo`, grupos, auditoria de usuários e gerenciamento de chaves SSH.  
> **Caminho das pastas:** `projects/junior-03-system-administration/<nome-do-projeto>/`

### 🎓 Nota do Professor (Nível 3):
*Segurança e o Princípio do Menor Privilégio são a regra. Nunca execute scripts como `root` a menos que seja estritamente necessário. Aprenda a diferença entre enviar um sinal `SIGTERM (15)` para encerramento gracioso e um `SIGKILL (9)` que força a destruição do processo sem liberar recursos.*

| Nº | Projeto | Script Principal | Objetivo Didático | Comandos Chave |
|---|---|---|---|---|
| 31 | `user-report` | `user-report.sh` | Listar e auditar contas de usuários cadastradas no sistema | `getent passwd`, `cut`, `awk` |
| 32 | `group-report` | `group-report.sh` | Listar grupos do sistema e seus respectivos membros | `getent group`, `members` |
| 33 | `home-directory-audit` | `home-audit.sh` | Verificar permissões e donos dos diretórios `/home/*` | `ls -ld`, `stat`, `chown` |
| 34 | `inactive-users-report` | `inactive-users.sh` | Identificar usuários que não fazem login há mais de X dias | `lastlog`, `last`, `chage` |
| 35 | `permission-audit` | `permission-audit.sh` | Procurar arquivos com SUID/SGID ativados que representam risco | `find -perm /4000`, `chmod` |
| 36 | `sudo-audit` | `sudo-audit.sh` | Relatar usuários com privilégios administrativos no `/etc/sudoers` | `sudo -l`, `cat /etc/sudoers` |
| 37 | `ssh-key-report` | `ssh-key-report.sh` | Inventariar chaves SSH públicas autorizadas nos diretórios dos usuários | `cat ~/.ssh/authorized_keys` |
| 38 | `process-report` | `process-report.sh` | Listar todos os processos ativos e seus respectivos PIDs e donos | `ps aux`, `pstree`, `pgrep` |
| 39 | `top-processes` | `top-processes.sh` | Exibir os Top N processos que mais consomem CPU e Memória RAM | `ps aux --sort=-%cpu`, `head` |
| 40 | `process-monitor` | `process-monitor.sh` | Monitorar a execução contínua de um processo específico pelo nome | `pgrep -x`, `pidof`, `sleep` |
| 41 | `high-cpu-alert` | `high-cpu-alert.sh` | Detectar e emitir alerta quando o uso de CPU ultrapassar um limite | `uptime`, `awk`, `mpstat` |
| 42 | `high-memory-alert` | `high-memory-alert.sh` | Detectar e alertar sobre consumo crítico de memória RAM e Swap | `free -m`, `awk`, `vmstat` |
| 43 | `zombie-process-report` | `zombie-process.sh` | Identificar e relatar processos no estado Zumbi (Defunct) | `ps aux | grep Z`, `awk` |
| 44 | `process-killer` | `process-killer.sh` | Encerrar processos com segurança (primeiro SIGTERM, depois SIGKILL) | `kill -15`, `kill -9`, `pkill` |
| 45 | `resource-snapshot` | `resource-snapshot.sh` | Salvar uma foto instantânea do estado geral dos recursos da máquina | `top -b -n1`, `free`, `df` |

---

## 🟣 Nível Junior 4 — Serviços e Systemd
> **Foco Didático:** Gerenciamento do init system moderno do Linux (`systemd`). Inspecionar unidades (`services`, `timers`, `targets`), analisar logs via `journalctl`, reiniciar serviços com controle de taxa de falhas e criar watchdogs de automação.  
> **Caminho das pastas:** `projects/junior-04-services/<nome-do-projeto>/`

### 🎓 Nota do Professor (Nível 4):
*O Systemd é o padrão de facto na maioria das distribuições Linux empresariais (Debian, Ubuntu, RHEL, CentOS). Aprenda a criar scripts de recuperação (`service-recovery`) que usam `--dry-run` para diagnosticar problemas antes de tentar comandos modificadores como `systemctl restart`.*

| Nº | Projeto | Script Principal | Objetivo Didático | Comandos Chave |
|---|---|---|---|---|
| 46 | `service-status` | `service-status.sh` | Verificar o status detalhado de execução de um serviço | `systemctl status`, `is-active` |
| 47 | `service-list` | `service-list.sh` | Listar todas as unidades de serviço ativas e carregadas | `systemctl list-units --type=service` |
| 48 | `failed-services-report` | `failed-services.sh` | Gerar relatório de todos os serviços em estado de falha (`failed`) | `systemctl --failed` |
| 49 | `service-health-check` | `service-health-check.sh` | Validar se o serviço está ativo e respondendo na porta configurada | `systemctl is-active`, `ss` |
| 50 | `service-restart` | `service-restart.sh` | Reiniciar serviços com logs de justificativa e checagem pós-restart | `systemctl restart`, `journalctl` |
| 51 | `service-watchdog` | `service-watchdog.sh` | Daemon em background que reinicia o serviço caso ele caia acidentalmente | `while true`, `systemctl start` |
| 52 | `systemd-report` | `systemd-report.sh` | Gerar relatório completo de governança do Systemd do servidor | `systemctl list-unit-files` |
| 53 | `systemd-log-report` | `systemd-log-report.sh` | Consultar e filtrar logs de uma unit específica no Journald | `journalctl -u --since` |
| 54 | `systemd-timer-check` | `timer-check.sh` | Listar e validar a próxima execução de timers configurados | `systemctl list-timers` |
| 55 | `service-dependency-report` | `dependency-report.sh` | Mapear e exibir a árvore de dependências de um serviço no Systemd | `systemctl list-dependencies` |
| 56 | `service-recovery` | `service-recovery.sh` | Tentar recuperação automática com suporte a `--dry-run` e `--repair` | `systemctl reset-failed` |
| 57 | `unit-validator` | `unit-validator.sh` | Validar a sintaxe de arquivos de configuração de Unit `.service` | `systemd-analyze verify` |

---

## 🟠 Nível Junior 5 — Rede, DNS e HTTP
> **Foco Didático:** Diagnóstico e solução de problemas de conectividade de rede no Linux. Inspeção de tabelas de roteamento, portas abertas, resolução de nomes DNS, chamadas de API/HTTP com `curl`, monitoramento de tempos de resposta e expiração de certificados SSL.  
> **Caminho das pastas:** `projects/junior-05-networking/<nome-do-projeto>/`

### 🎓 Nota do Professor (Nível 5):
*Em redes e DevOps, "nunca é problema de rede até que seja, e quase sempre é problema de DNS". Domine o uso de `curl -fsS --max-time 10` e saiba interpretar os códigos HTTP (2xx Sucesso, 3xx Redirecionamento, 4xx Erro do Cliente, 5xx Erro do Servidor).*

| Nº | Projeto | Script Principal | Objetivo Didático | Comandos Chave |
|---|---|---|---|---|
| 58 | `network-report` | `network-report.sh` | Listar interfaces físicas/virtuais, relatar estados e estatísticas | `ip addr`, `ip link` |
| 59 | `ip-address-report` | `ip-address-report.sh` | Extrair IPs IPv4/IPv6 atribuídos e mascaras de sub-rede | `ip -4 addr show`, `awk` |
| 60 | `route-report` | `route-report.sh` | Analisar a tabela de roteamento e identificar o Gateway Padrão | `ip route`, `traceroute` |
| 61 | `port-check` | `port-check.sh` | Testar se uma porta TCP remota ou local está aberta e aceitando conexões | `nc -zv`, `ss -tulpn` |
| 62 | `socket-report` | `socket-report.sh` | Listar todos os sockets ativas relacionando ao PID do processo dono | `ss -tanp`, `lsof -i` |
| 63 | `connectivity-check` | `connectivity-check.sh` | Testar latência e perda de pacotes para múltiplos destinos | `ping -c 4`, `fping` |
| 64 | `dns-check` | `dns-check.sh` | Validar resolução de nomes DNS contra servidores específicos | `dig`, `host`, `nslookup` |
| 65 | `dns-record-report` | `dns-record-report.sh` | Consultar e comparar registros A, CNAME, MX, TXT e NS de um domínio | `dig +short`, `getent hosts` |
| 66 | `http-health-check` | `http-health-check.sh` | Verificar o código de status HTTP retornado por um endpoint da web | `curl -I`, `curl -s -o /dev/null` |
| 67 | `endpoint-monitor` | `endpoint-monitor.sh` | Monitorar uma lista de URLs cadastradas em arquivo de configuração | `curl -fsS`, `while read` |
| 68 | `http-status-report` | `http-status-report.sh` | Gerar relatório de cabeçalhos HTTP e servidores web detectados | `curl -i`, `grep -i server` |
| 69 | `response-time-check` | `response-time-check.sh` | Medir o tempo exato de resposta DNS, Conexão TCP e Handshake TTFB | `curl -w '%{time_total}'` |
| 70 | `certificate-expiry-check` | `certificate-expiry.sh` | Alertar quantos dias faltam para a expiração de um Certificado SSL/TLS | `openssl s_client`, `date` |
| 71 | `network-diagnostics` | `network-diagnostics.sh` | Coletar um bundle completo de diagnóstico de rede para troubleshooting | `ip`, `ss`, `dig`, `ping`, `mtr` |
| 72 | `service-connectivity-check` | `service-connectivity.sh` | Testar o fluxo ponta a ponta: DNS → Rota → Porta TCP → Requisição HTTP | `dig`, `nc`, `curl` |

---

## 🔴 Nível Junior 6 — Logs e Troubleshooting
> **Foco Didático:** Engenharia de confiabilidade e investigação de incidentes. Filtragem avançada de logs com `grep`, `awk`, `sed`, análise do Syslog e Journald, contagem de erros por padrão, retenção, criação de bundles de evidência de incidentes e relatórios de Postmortem.  
> **Caminho das pastas:** `projects/junior-06-logs-troubleshooting/<nome-do-projeto>/`

### 🎓 Nota do Professor (Nível 6):
*Quando o sistema para de funcionar às 3h da manhã, o Engenheiro DevOps não tenta dar palpites: ele investiga os logs! Aprenda a buscar padrões sem alterar os arquivos originais e crie scripts que isolam a causa raiz com base em evidências.*

| Nº | Projeto | Script Principal | Objetivo Didático | Comandos Chave |
|---|---|---|---|---|
| 73 | `log-summary` | `log-summary.sh` | Resumir total de linhas, tamanho e primeiras/últimas entradas de um log | `wc -l`, `head`, `tail`, `du` |
| 74 | `error-counter` | `error-counter.sh` | Contar ocorrências de erros contendo strings como `ERROR`, `FATAL`, `FAIL` | `grep -c -i`, `awk` |
| 75 | `warning-counter` | `warning-counter.sh` | Contar e agrupar mensagens de alerta de um sistema | `grep -i 'warn'`, `sort`, `uniq` |
| 76 | `journal-report` | `journal-report.sh` | Extrair logs do Systemd ordenados por severidade (`warning..emerg`) | `journalctl -p`, `journalctl -b` |
| 77 | `service-log-report` | `service-log-report.sh` | Isolar e salvar em arquivo os últimos logs de um determinado serviço | `journalctl -u --since` |
| 78 | `failed-login-report` | `failed-login-report.sh` | Analisar tentativas de autenticação SSH com falha para detectar ataques | `grep 'Failed password'`, `lastb` |
| 79 | `log-rotation-check` | `log-rotation-check.sh` | Verificar se as regras do `logrotate` estão configuradas e operacionais | `logrotate -d`, `cat /etc/logrotate.d` |
| 80 | `log-size-monitor` | `log-size-monitor.sh` | Alertar se um arquivo de log cresceu desproporcionalmente | `du -m`, `find -size` |
| 81 | `incident-evidence` | `collect-evidence.sh` | Empacotar logs, lista de processos, estado de rede e disco durante incidente | `tar -czf`, `dmesg`, `ss` |
| 82 | `service-diagnosis` | `diagnose-service.sh` | Executar árvore de decisão para diagnosticar por que um serviço caiu | `systemctl`, `journalctl`, `ss` |
| 83 | `disk-full-diagnosis` | `diagnose-disk.sh` | Identificar exatamente quais diretórios ou arquivos consumiram 100% do disco | `du -xhd1`, `sort -hr`, `find` |
| 84 | `high-load-diagnosis` | `diagnose-load.sh` | Correlacionar alta carga do sistema com processos ou I/O de disco pesado | `uptime`, `iostat`, `pidstat` |
| 85 | `network-failure-diagnosis` | `diagnose-network.sh` | Identificar em qual camada ocorreu a falha (Interface, Rota, DNS ou Firewall) | `ip link`, `ip route`, `dig` |
| 86 | `postmortem-generator` | `postmortem-generator.sh` | Gerar template preenchido de Postmortem para incidentes de infraestrutura | `cat <<EOF > postmortem.md` |

---

## 🟤 Nível Junior 7 — Storage, Backup e Restauração
> **Foco Didático:** Gestão de armazenamento persistente. Uso de disco (`df`), verificação de inodes, gerenciamento de pontos de montagem (`mount`), automação de rotinas de backup comprimido, validação de hashes SHA256, política de retenção e testes de restauração.  
> **Caminho das pastas:** `projects/junior-07-storage-backup/<nome-do-projeto>/`

### 🎓 Nota do Professor (Nível 7):
*A Regra de Ouro do Backup: "Um backup que nunca foi testado para restauração NÃO É UM BACKUP". Todo script desta fase deve incluir ou ser acompanhado por um script de validação e restauração em ambiente isolado.*

| Nº | Projeto | Script Principal | Objetivo Didático | Comandos Chave |
|---|---|---|---|---|
| 87 | `disk-usage-report` | `disk-usage-report.sh` | Gerar relatório legível por humanos (`df -h`) com alertas acima de 85% | `df -h`, `awk`, `column -t` |
| 88 | `inode-monitor` | `inode-monitor.sh` | Alertar sobre esgotamento de Inodes (situação em que o disco parece ter espaço) | `df -i`, `awk` |
| 89 | `mount-report` | `mount-report.sh` | Listar pontos de montagem, verificar opções (`rw/ro`) e tipos de sistema | `findmnt`, `cat /etc/fstab` |
| 90 | `filesystem-report` | `filesystem-report.sh` | Relatar detalhes dos sistemas de arquivos (`ext4`, `xfs`, `btrfs`) e UUIDs | `lsblk -f`, `blkid` |
| 91 | `backup-manager` | `backup.sh` | Criar backup compactado `.tar.gz` de pastas selecionadas com marcação de data | `tar -czf`, `date +%Y%m%d` |
| 92 | `backup-verify` | `verify-backup.sh` | Testar se o arquivo de backup `.tar.gz` está integro e não corrompido | `tar -tzf`, `sha256sum -c` |
| 93 | `backup-restore` | `restore.sh` | Extrair e restaurar o conteúdo de um backup em diretório de destino | `tar -xzf -C` |
| 94 | `backup-retention` | `retention.sh` | Aplicar política de retenção apagando backups mais antigos que X dias | `find -mtime +N -delete` |
| 95 | `backup-report` | `backup-report.sh` | Gerar relatório de status com tamanho, duração e sucesso dos backups | `stat`, `du`, `date` |
| 96 | `backup-test` | `backup-test.sh` | Automação que restaura o backup em pasta temporária e valida checksum dos dados | `mktemp -d`, `cmp` |
| 97 | `directory-sync` | `directory-sync.sh` | Sincronizar diretórios locais ou remotos de forma eficiente usando `rsync` | `rsync -avz --delete` |
| 98 | `storage-alert` | `storage-alert.sh` | Notificar o administrador caso a partição `/` ou `/var` atinja nível crítico | `df`, `mail`, `curl` |

---

## 🟨 Nível Junior 8 — Cron, Timers e Automação Operacional
> **Foco Didático:** Automação de tarefas recorrentes em segundo plano. Agendamento com `crontab` e `systemd timers`, prevenção de execuções simultâneas via `flock`, retentativas automáticas (`retries`) com expiração (`exponential backoff`), notificação de resultados e limpeza.  
> **Caminho das pastas:** `projects/junior-08-automation/<nome-do-projeto>/`

### 🎓 Nota do Professor (Nível 8):
*Scripts rodando em Cron não possuem o mesmo ambiente (`PATH`, variáveis) do seu terminal interativo. Sempre defina caminhos absolutos para executáveis (`/usr/bin/tar`) e use travas de arquivo (`flock`) para evitar que uma tarefa lenta seja executada duas vezes ao mesmo tempo.*

| Nº | Projeto | Script Principal | Objetivo Didático | Comandos Chave |
|---|---|---|---|---|
| 99 | `scheduled-report` | `scheduled-report.sh` | Script formatado especificamente para rodar no Cron e salvar relatórios | `crontab -e`, `date` |
| 100 | `cron-health-check` | `cron-health-check.sh` | Verificar se as tarefas agendadas no Cron estão sendo disparadas corretamente | `grep CRON /var/log/syslog` |
| 101 | `lock-manager` | `lock-manager.sh` | Garantir que apenas uma instância do script seja executada simultaneamente | `flock -n /tmp/app.lock` |
| 102 | `retry-command` | `retry-command.sh` | Executar um comando e tentar novamente N vezes em caso de falha transitória | `until`, `sleep`, `exit status` |
| 103 | `job-runner` | `job-runner.sh` | Executar uma lista de tarefas sequenciais registrando tempo e status | `time`, `tee`, `logger` |
| 104 | `cleanup-manager` | `cleanup-manager.sh` | Limpar artefatos de build, caches e logs antigos respeitando a retenção | `find -mtime -exec rm` |
| 105 | `config-loader` | `config-loader.sh` | Carregar dinamicamente variáveis de arquivos `.env` com fallback seguro | `source`, `[[ -f ]]` |
| 106 | `dry-run-automation` | `automation.sh` | Implementar o flag `--dry-run` em scripts para simular alterações | `if [[ "$DRY_RUN" == 1 ]]` |
| 107 | `notification-wrapper` | `notification-wrapper.sh` | Encapsular a execução de qualquer comando e notificar o resultado via webhook | `curl -X POST -d` |
| 108 | `parallel-runner` | `parallel-runner.sh` | Executar tarefas em paralelo controlando a quantidade de jobs concorrentes | `xargs -P`, `&`, `wait` |
| 109 | `execution-report` | `execution-report.sh` | Gerar relatórios detalhados com horário de início, fim, duração e exit code | `date +%s`, `bc` |
| 110 | `timer-manager` | `timer-manager.sh` | Criar, ativar e inspecionar Timers nativos do Systemd como alternativa ao Cron | `systemctl enable --now *.timer` |

---

## 🟩 Nível Junior 9 — Bash Avançado e Qualidade
> **Foco Didático:** Elevar a qualidade de código em Shell Script a padrões corporativos. Uso do `getopts` para parsing profissional de argumentos `--flag`, construção de bibliotecas de funções `.lib.sh`, geração de relatórios JSON/CSV, tratamento de sinais com `trap` e testes estáticos.  
> **Caminho das pastas:** `projects/junior-09-bash-advanced/<nome-do-projeto>/`

### 🎓 Nota do Professor (Nível 9):
*Aqui você deixa de ser um "criador de scripts" e passa a ser um "desenvolvedor de software em Shell". Seu código deve ter documentação integrada (`--help`), ser modularizado em bibliotecas e passar sem nenhum aviso pelo ShellCheck.*

| Nº | Projeto | Script Principal | Objetivo Didático | Comandos Chave |
|---|---|---|---|---|
| 111 | `argument-parser` | `argument-parser.sh` | Tratar argumentos curtos e longos usando `getopts` e blocos de opções | `getopts`, `OPTIND`, `OPTARG` |
| 112 | `help-generator` | `help-generator.sh` | Gerar menu de ajuda padronizado (`--help`) extraindo comentários do cabeçalho | `sed`, `cat <<EOF` |
| 113 | `logging-library` | `logging.lib.sh` | Biblioteca exportável para formatação de logs coloridos com marcas de tempo | `source`, `printf`, `ANSI colors` |
| 114 | `validation-library` | `validation.lib.sh` | Conjunto de funções para validar IPs, URLs, inteiros e emails | `regex`, `return 0/1` |
| 115 | `common-library` | `common.lib.sh` | Central de utilitários reutilizáveis para inclusão em qualquer projeto | `source`, `readonly` |
| 116 | `config-manager` | `config-manager.sh` | Ler, alterar e validar chave/valor em arquivos de configuração no formato INI | `awk`, `sed -i` |
| 117 | `environment-validator` | `environment-validator.sh` | Validar a presença de dependências, permissões de root e variáveis de ambiente | `command -v`, `[[ -w ]]` |
| 118 | `safe-command-runner` | `safe-run.sh` | Executor de comandos com timeout, captura de stderr e tratamento de falhas | `timeout`, `eval`, `trap` |
| 119 | `parallel-job-manager` | `parallel-jobs.sh` | Gerenciador de fila de tarefas em background usando controle de PIDs | `wait -n`, `jobs -p` |
| 120 | `shell-test-runner` | `test-runner.sh` | Executor customizado para rodar múltiplos arquivos de testes `.bats` ou `.sh` | `find`, `bash`, `bats` |
| 121 | `report-generator` | `report-generator.sh` | Gerar dados tabulados em texto plano formatado e formato CSV exportável | `printf`, `column -s, -t` |
| 122 | `json-report-generator` | `json-report.sh` | Construir e validar saídas no formato JSON nativo para integração com APIs | `jq`, `cat <<EOF` |
| 123 | `dry-run-framework` | `dry-run.lib.sh` | Biblioteca que intercepta comandos destrutivos quando o modo dry-run está ativo | `function run_cmd()` |
| 124 | `rollback-manager` | `rollback-manager.sh` | Sistema de transação com suporte a desfazer alterações (`rollback`) em erro | `trap cleanup ERR` |

---

## 🏁 Nível Junior 10 — Projetos Integradores de DevOps
> **Foco Didático:** Consolidação completa de todo o conhecimento acumulado. Construção de ferramentas completas de infraestrutura: inventários de servidores, auditorias de segurança, pipelines de implantação com rollback automatizado, gestão de releases e ferramentas CLI completas.  
> **Caminho das pastas:** `projects/junior-10-devops-projects/<nome-do-projeto>/`

### 🎓 Nota do Professor (Nível 10):
*Parabéns por chegar ao nível integrador! Aqui os projetos combinam auditoria, segurança, rede, serviços, logs e automação. Estes projetos servem como portfólio real de Engenharia DevOps para apresentar em entrevistas de emprego e demonstrar domínio produtivo.*

| Nº | Projeto | Script Principal | Objetivo Didático | Comandos Chave Integrados |
|---|---|---|---|---|
| 125 | `system-inventory` | `system-inventory.sh` | Ferramenta completa de inventário de hardware, OS, rede e pacotes do host | `uname`, `lscpu`, `free`, `ip`, `dpkg` |
| 126 | `server-health-check` | `server-health-check.sh` | Verificação geral de saúde (CPU, RAM, Disco, Serviços, Porta, DNS, HTTP) | `df`, `free`, `systemctl`, `curl` |
| 127 | `server-readiness` | `readiness.sh` | Validar se um servidor recém-provisionado atende a todos os pré-requisitos | `command -v`, `netstat`, `ping` |
| 128 | `linux-audit` | `linux-audit.sh` | Auditoria de segurança de acordo com diretrizes de hardening (SUID, Sudo, SSH) | `find`, `grep /etc/passwd`, `ss` |
| 129 | `deployment-helper` | `deploy.sh` | Automação de deploy de aplicação com download, backup, substituição e restart | `tar`, `rsync`, `systemctl` |
| 130 | `deployment-validator` | `validate-deployment.sh` | Smoke tests automatizados após a implantação para confirmar disponibilidade | `curl`, `journalctl`, `systemctl` |
| 131 | `deployment-rollback` | `rollback.sh` | Reversão automática instantânea da versão anterior caso o smoke test falhe | `ln -snf`, `systemctl restart` |
| 132 | `release-manager` | `release.sh` | Gerenciar a criação de tags Git, changelogs e empacotamento de releases | `git tag`, `git log`, `tar` |
| 133 | `environment-manager` | `environment.sh` | Alternar e aplicar configurações de ambiente (`dev`, `staging`, `prod`) | `cp`, `ln -sf`, `source` |
| 134 | `configuration-manager` | `config-manager.sh` | Garantir que o estado dos arquivos de configuração esteja no padrão esperado | `diff`, `sed`, `systemctl reload` |
| 135 | `operations-toolkit` | `ops.sh` | CLI unificada que agrupa comandos de healthcheck, logs, restart e backup | `getopts`, `source lib/*` |
| 136 | `maintenance-manager` | `maintenance.sh` | Automatizar janela de manutenção (colocar página estática, parar apps, limpar, rodar updates) | `systemctl`, `nginx`, `apt update` |
| 137 | `incident-response-toolkit` | `incident.sh` | Coleta automática de emergência em incidentes gerando pacote zip com evidências | `tar`, `journalctl`, `dmesg`, `ss` |
| 138 | `backup-and-monitoring` | `backup-monitor.sh` | Integração completa entre rotina de backup, validação de checksum e alerta HTTP | `tar`, `sha256sum`, `curl` |
| 139 | `linux-automation-platform` | `platform.sh` | Plataforma inteiramente modular em Shell para governança de infraestrutura | `bin/`, `lib/`, `config/`, `tests/` |

---

## 📊 Matriz Resumo dos 139 Projetos

```text
 ┌────────────────────────────────────────────────────────────────────────┐
 │ RESUMO DA DISTRIBUIÇÃO DOS PROJETOS                                    │
 │                                                                        │
 │  • Nível 1 (Fundamentos):       15 projetos  (01 ao 15)                │
 │  • Nível 2 (Filesystem):        15 projetos  (16 ao 30)                │
 │  • Nível 3 (Admin & Processos): 15 projetos  (31 ao 45)                │
 │  • Nível 4 (Serviços & Systemd):12 projetos  (46 ao 57)                │
 │  • Nível 5 (Rede, DNS e HTTP):  15 projetos  (58 ao 72)                │
 │  • Nível 6 (Logs & Incidente):  14 projetos  (73 ao 86)                │
 │  • Nível 7 (Storage & Backup):  12 projetos  (87 ao 98)                │
 │  • Nível 8 (Cron & Automação):  12 projetos  (99 ao 110)               │
 │  • Nível 9 (Bash Avançado):     14 projetos  (111 ao 124)              │
 │  • Nível 10 (DevOps Integrador):15 projetos  (125 ao 139)              │
 │                                                                        │
 │  TOTAL: 139 PROJETOS PRÁTICOS                                          │
 └────────────────────────────────────────────────────────────────────────┘
```