Nível Junior 1 — Fundamentos do Bash
Foco: aprender comandos, variáveis, argumentos, condições, loops e funções.
text
projects/junior-01-fundamentos/
Nº
Projeto
Script principal
Objetivo
01
hello-bash
hello-bash.sh
Criar o primeiro script Bash
02
system-info
system-info.sh
Exibir informações básicas do sistema
03
date-report
date-report.sh
Gerar relatório de data e hora
04
argument-reader
argument-reader.sh
Ler argumentos passados pela linha de comando
05
variable-manager
variable-manager.sh
Trabalhar com variáveis e ambiente
06
interactive-menu
interactive-menu.sh
Criar menu interativo
07
calculator
calculator.sh
Criar calculadora simples
08
number-validator
number-validator.sh
Validar números informados pelo usuário
09
string-validator
string-validator.sh
Validar textos e strings
10
user-greeting
user-greeting.sh
Cumprimentar usuário conforme horário
11
file-creator
file-creator.sh
Criar arquivos através de argumentos
12
directory-creator
directory-creator.sh
Criar diretórios com validação
13
command-checker
command-checker.sh
Verificar se comandos existem
14
exit-code-demo
exit-code-demo.sh
Praticar códigos de saída
15
simple-menu-system
menu.sh
Criar menu com múltiplas opções
Exemplo de estrutura:
text
projects/junior-01-fundamentos/hello-bash/
├── README.md
├── scripts/
│   └── hello-bash.sh
└── tests/
    └── test.sh
Nível Junior 2 — Arquivos e filesystem
Foco: arquivos, diretórios, permissões, links, busca e organização.
text
projects/junior-02-filesystem/
Nº
Projeto
Script principal
Objetivo
16
file-counter
file-counter.sh
Contar arquivos em um diretório
17
directory-checker
directory-checker.sh
Verificar se diretórios existem
18
file-checker
file-checker.sh
Verificar tipo e permissões de arquivos
19
file-organizer
file-organizer.sh
Organizar arquivos por extensão
20
extension-report
extension-report.sh
Gerar relatório por extensão
21
large-files-report
large-files-report.sh
Encontrar arquivos grandes
22
empty-files-report
empty-files-report.sh
Encontrar arquivos vazios
23
duplicate-finder
duplicate-finder.sh
Encontrar arquivos duplicados
24
temporary-files-cleaner
clean-temporary.sh
Limpar arquivos temporários
25
old-files-report
old-files-report.sh
Listar arquivos antigos
26
permissions-report
permissions-report.sh
Gerar relatório de permissões
27
symlink-manager
symlink-manager.sh
Criar e validar links simbólicos
28
directory-backup
directory-backup.sh
Compactar diretórios
29
checksum-manager
checksum-manager.sh
Criar e validar checksums
30
file-integrity-check
integrity-check.sh
Verificar alterações em arquivos
Nível Junior 3 — Processos, usuários e permissões
Foco: administração básica do sistema Linux.
text
projects/junior-03-system-administration/
Nº
Projeto
Script principal
Objetivo
31
user-report
user-report.sh
Listar usuários do sistema
32
group-report
group-report.sh
Listar grupos do sistema
33
home-directory-audit
home-audit.sh
Verificar diretórios home
34
inactive-users-report
inactive-users.sh
Identificar usuários inativos
35
permission-audit
permission-audit.sh
Procurar permissões inadequadas
36
sudo-audit
sudo-audit.sh
Relatar permissões de sudo
37
ssh-key-report
ssh-key-report.sh
Listar chaves SSH públicas
38
process-report
process-report.sh
Listar processos do sistema
39
top-processes
top-processes.sh
Mostrar processos por CPU e memória
40
process-monitor
process-monitor.sh
Monitorar processo específico
41
high-cpu-alert
high-cpu-alert.sh
Detectar alto consumo de CPU
42
high-memory-alert
high-memory-alert.sh
Detectar alto consumo de memória
43
zombie-process-report
zombie-process.sh
Encontrar processos zumbis
44
process-killer
process-killer.sh
Encerrar processo com segurança
45
resource-snapshot
resource-snapshot.sh
Salvar estado dos recursos
Projetos que criam usuários ou alteram permissões devem ser executados primeiro em laboratório. O modo inicial deve ser somente leitura ou --dry-run.
Nível Junior 4 — Serviços e systemd
Foco: verificar, iniciar, parar e monitorar serviços Linux.
text
projects/junior-04-services/
Nº
Projeto
Script principal
Objetivo
46
service-status
service-status.sh
Verificar status de um serviço
47
service-list
service-list.sh
Listar serviços ativos
48
failed-services-report
failed-services.sh
Listar serviços com falha
49
service-health-check
service-health-check.sh
Validar serviço em execução
50
service-restart
service-restart.sh
Reiniciar serviço controladamente
51
service-watchdog
service-watchdog.sh
Monitorar serviço continuamente
52
systemd-report
systemd-report.sh
Gerar relatório do systemd
53
systemd-log-report
systemd-log-report.sh
Consultar logs de uma unit
54
systemd-timer-check
timer-check.sh
Verificar timers configurados
55
service-dependency-report
dependency-report.sh
Mostrar dependências de serviço
56
service-recovery
service-recovery.sh
Tentar recuperação controlada
57
unit-validator
unit-validator.sh
Validar arquivos de unit
O projeto service-recovery deve obedecer esta regra:
text
modo padrão       → apenas diagnostica
--dry-run         → mostra o que faria
--repair          → executa a recuperação
Nível Junior 5 — Rede, DNS e HTTP
Foco: diagnosticar conectividade e validar serviços de rede.
text
projects/junior-05-networking/
Nº
Projeto
Script principal
Objetivo
58
network-report
network-report.sh
Relatar interfaces de rede
59
ip-address-report
ip-address-report.sh
Listar endereços IP
60
route-report
route-report.sh
Relatar tabela de rotas
61
port-check
port-check.sh
Verificar porta TCP
62
socket-report
socket-report.sh
Listar sockets em uso
63
connectivity-check
connectivity-check.sh
Testar conectividade
64
dns-check
dns-check.sh
Validar resolução DNS
65
dns-record-report
dns-record-report.sh
Consultar registros DNS
66
http-health-check
http-health-check.sh
Verificar endpoint HTTP
67
endpoint-monitor
endpoint-monitor.sh
Monitorar várias URLs
68
http-status-report
http-status-report.sh
Relatar códigos HTTP
69
response-time-check
response-time-check.sh
Medir tempo de resposta
70
certificate-expiry-check
certificate-expiry.sh
Verificar validade de certificados
71
network-diagnostics
network-diagnostics.sh
Coletar diagnóstico de rede
72
service-connectivity-check
service-connectivity.sh
Validar conexão com serviço
Exemplo de configuração:
text
projects/junior-05-networking/endpoint-monitor/
├── README.md
├── scripts/
│   └── endpoint-monitor.sh
├── configs/
│   └── endpoints.txt
├── tests/
│   └── test.sh
└── evidence/
Nível Junior 6 — Logs e troubleshooting
Foco: investigar problemas e criar evidências técnicas.
text
projects/junior-06-logs-troubleshooting/
Nº
Projeto
Script principal
Objetivo
73
log-summary
log-summary.sh
Resumir arquivo de log
74
error-counter
error-counter.sh
Contar mensagens de erro
75
warning-counter
warning-counter.sh
Contar alertas
76
journal-report
journal-report.sh
Consultar logs do journald
77
service-log-report
service-log-report.sh
Gerar relatório de serviço
78
failed-login-report
failed-login-report.sh
Relatar tentativas de login
79
log-rotation-check
log-rotation-check.sh
Verificar rotação de logs
80
log-size-monitor
log-size-monitor.sh
Monitorar tamanho de logs
81
incident-evidence
collect-evidence.sh
Coletar evidências de incidente
82
service-diagnosis
diagnose-service.sh
Diagnosticar serviço parado
83
disk-full-diagnosis
diagnose-disk.sh
Investigar disco cheio
84
high-load-diagnosis
diagnose-load.sh
Investigar carga elevada
85
network-failure-diagnosis
diagnose-network.sh
Diagnosticar falha de rede
86
postmortem-generator
postmortem-generator.sh
Criar modelo de postmortem
Nível Junior 7 — Storage, backup e restauração
Foco: espaço em disco, backups, retenção e recuperação.
text
projects/junior-07-storage-backup/
Nº
Projeto
Script principal
Objetivo
87
disk-usage-report
disk-usage-report.sh
Relatar uso de disco
88
inode-monitor
inode-monitor.sh
Monitorar inodes
89
mount-report
mount-report.sh
Listar pontos de montagem
90
filesystem-report
filesystem-report.sh
Relatar sistemas de arquivos
91
backup-manager
backup.sh
Criar backups compactados
92
backup-verify
verify-backup.sh
Validar integridade do backup
93
backup-restore
restore.sh
Restaurar backup
94
backup-retention
retention.sh
Remover backups antigos
95
backup-report
backup-report.sh
Gerar relatório de backups
96
backup-test
backup-test.sh
Testar restauração automaticamente
97
directory-sync
directory-sync.sh
Sincronizar diretórios
98
storage-alert
storage-alert.sh
Alertar espaço abaixo do limite
Regra importante:
text
backup criado ≠ backup confiável
O backup só deve ser considerado confiável depois de testar a restauração.
Nível Junior 8 — Cron, timers e automação operacional
Foco: executar tarefas automaticamente e com controle.
text
projects/junior-08-automation/
Nº
Projeto
Script principal
Objetivo
99
scheduled-report
scheduled-report.sh
Gerar relatório agendado
100
cron-health-check
cron-health-check.sh
Verificar execução de jobs
101
lock-manager
lock-manager.sh
Evitar execução simultânea
102
retry-command
retry-command.sh
Repetir comando com limite
103
job-runner
job-runner.sh
Executar jobs com logs
104
cleanup-manager
cleanup-manager.sh
Limpar arquivos antigos
105
config-loader
config-loader.sh
Carregar configurações externas
106
dry-run-automation
automation.sh
Simular alterações
107
notification-wrapper
notification-wrapper.sh
Registrar sucesso e falha
108
parallel-runner
parallel-runner.sh
Executar tarefas em paralelo
109
execution-report
execution-report.sh
Gerar relatório de execução
110
timer-manager
timer-manager.sh
Gerenciar systemd timers
Todo script agendado deve ter:
text
caminho absoluto
logs
tratamento de erro
lock
timeout
código de saída
documentação
Nível Junior 9 — Bash avançado e qualidade
Foco: transformar scripts simples em ferramentas confiáveis.
text
projects/junior-09-bash-advanced/
Nº
Projeto
Script principal
Objetivo
111
argument-parser
argument-parser.sh
Usar opções com getopts
112
help-generator
help-generator.sh
Criar ajuda padronizada
113
logging-library
logging.lib.sh
Criar biblioteca de logs
114
validation-library
validation.lib.sh
Criar funções de validação
115
common-library
common.lib.sh
Reutilizar funções comuns
116
config-manager
config-manager.sh
Gerenciar arquivos de configuração
117
environment-validator
environment-validator.sh
Validar ambiente de execução
118
safe-command-runner
safe-run.sh
Executar comandos com segurança
119
parallel-job-manager
parallel-jobs.sh
Controlar jobs paralelos
120
shell-test-runner
test-runner.sh
Executar vários testes
121
report-generator
report-generator.sh
Criar relatórios em texto e CSV
122
json-report-generator
json-report.sh
Gerar saída em JSON
123
dry-run-framework
dry-run.lib.sh
Criar biblioteca para dry-run
124
rollback-manager
rollback-manager.sh
Implementar rollback de mudanças
Nível Junior 10 — Projetos integradores de DevOps
Foco: juntar os conhecimentos anteriores em projetos maiores.
text
projects/junior-10-devops-projects/
Nº
Projeto
Script principal
Objetivo
125
system-inventory
system-inventory.sh
Inventário completo do servidor
126
server-health-check
server-health-check.sh
Verificação geral de saúde
127
server-readiness
readiness.sh
Validar se servidor está pronto
128
linux-audit
linux-audit.sh
Auditoria básica do sistema
129
deployment-helper
deploy.sh
Automatizar implantação
130
deployment-validator
validate-deployment.sh
Validar implantação
131
deployment-rollback
rollback.sh
Reverter implantação
132
release-manager
release.sh
Gerenciar versões
133
environment-manager
environment.sh
Gerenciar ambientes dev/test/prod
134
configuration-manager
config-manager.sh
Aplicar configurações
135
operations-toolkit
ops.sh
Centralizar ferramentas operacionais
136
maintenance-manager
maintenance.sh
Automatizar rotinas de manutenção
137
incident-response-toolkit
incident.sh
Coletar dados de incidentes
138
backup-and-monitoring
backup-monitor.sh
Integrar backup e monitoramento
139
linux-automation-platform
platform.sh
Criar uma ferramenta Bash integrada
Estrutura final recomendada
text
projects/
├── junior-01-fundamentos/
├── junior-02-filesystem/
├── junior-03-system-administration/
├── junior-04-services/
├── junior-05-networking/
├── junior-06-logs-troubleshooting/
├── junior-07-storage-backup/
├── junior-08-automation/
├── junior-09-bash-advanced/
└── junior-10-devops-projects/
Dentro de cada nível:
text
junior-01-fundamentos/
├── hello-bash/
├── system-info/
├── date-report/
├── argument-reader/
├── interactive-menu/
└── calculator/
Dentro de cada projeto:
text
hello-bash/
├── README.md
├── scripts/
│   └── hello-bash.sh
├── tests/
│   └── test.sh
├── fixtures/
├── configs/
└── evidence/
Ordem prática recomendada
Não precisa criar e desenvolver os 139 projetos de uma vez. A ordem ideal é:
text
1. hello-bash
2. system-info
3. argument-reader
4. interactive-menu
5. file-counter
6. directory-checker
7. file-organizer
8. permissions-report
9. process-report
10. service-status
11. disk-usage-report
12. dns-check
13. http-health-check
14. log-summary
15. backup-manager
16. scheduled-report
17. system-inventory
18. server-health-check
19. deployment-helper
20. linux-automation-platform
A progressão será:
text
comando simples
    ↓
script pequeno
    ↓
script com argumentos
    ↓
script com validação
    ↓
script com logs
    ↓
script com testes
    ↓
script agendado
    ↓
script com recuperação
    ↓
projeto integrado de DevOps