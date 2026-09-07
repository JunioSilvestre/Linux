# Laboratório Linux Junior — Bash, Automação e DevOps

## Objetivo deste documento

Este documento define a primeira etapa prática do laboratório `/home/Projetos/Linux/junior`. O foco é aprender Linux e Bash fazendo: observar o sistema, executar operações com segurança, automatizar tarefas repetitivas, testar falhas, investigar resultados, documentar procedimentos e evoluir gradualmente para práticas de DevOps.

A regra principal será:

> **Estudar → Implementar → Quebrar em ambiente controlado → Diagnosticar → Automatizar → Monitorar → Documentar → Melhorar.**

A pasta `junior` não será apenas uma coleção de comandos. Cada tópico deve resultar em exercícios, scripts, evidências de execução, testes e documentação.

---

## 1. Princípios de trabalho

### 1.1 Segurança antes da velocidade

Nunca teste comandos destrutivos diretamente em um servidor de produção. Para aprender, use uma máquina virtual, container, usuário de laboratório e diretórios de teste.

Comandos como `rm -rf`, `mkfs`, `dd`, `fdisk`, `parted`, `chmod -R`, `chown -R`, alterações em `/etc`, reinício de serviços e regras de firewall podem causar perda de dados ou indisponibilidade.

Antes de uma mudança importante:

```bash
pwd
whoami
hostname
id
sudo -l
```

Confirme onde está, qual usuário está usando, em qual host está conectado e quais privilégios possui.

### 1.2 Idempotência

Um script idempotente pode ser executado várias vezes e produz o mesmo estado final sem duplicar arquivos, usuários, serviços ou configurações.

Exemplo não idempotente:

```bash
echo "export APP_ENV=dev" >> ~/.bashrc
```

Cada execução adiciona outra linha. Uma alternativa mais segura:

```bash
grep -qxF 'export APP_ENV=dev' ~/.bashrc || echo 'export APP_ENV=dev' >> ~/.bashrc
```

### 1.3 Reprodutibilidade

Tudo que for necessário para repetir o exercício deve estar no repositório: script, configuração, dados de exemplo, instruções, teste e resultado esperado.

### 1.4 Princípio do menor privilégio

Execute como usuário normal sempre que possível. Use `sudo` somente para a operação que realmente precisa de privilégio. Não coloque senhas ou tokens dentro de scripts versionados.

### 1.5 Observabilidade desde o início

Todo script operacional deve informar o que está fazendo, retornar códigos de saída úteis e registrar erros de forma compreensível.

---

## 2. Estrutura existente e organização recomendada

A estrutura inicial informada é:

```text
junior/
├── bash/
├── cron/
├── dns/
├── filesystem/
├── logs/
├── networking/
├── packages/
├── processes/
├── services/
├── ssh/
├── storage/
├── systemd/
├── troubleshooting/
├── users-permissions/
└── web-server/
```

A recomendação é manter essas áreas e adicionar uma convenção interna a cada uma:

```text
<topico>/
├── README.md              # teoria, objetivo e como executar
├── scripts/               # scripts executáveis
├── configs/               # arquivos de configuração de exemplo
├── fixtures/              # dados controlados para teste
├── tests/                 # testes automatizados ou checklists
├── evidence/              # saídas e evidências, quando necessário
└── notes/                 # troubleshooting e aprendizados
```

Não é obrigatório criar todas as subpastas em todos os tópicos no primeiro dia. Crie-as conforme o exercício crescer.

---

## 3. Lista de pastas de exercícios a criar

Execute a partir da raiz do laboratório. O comando abaixo cria áreas para exercícios, scripts, testes e projetos integradores sem apagar nada existente:

```bash
cd /home/Projetos/Linux/junior

mkdir -p \
  bash/{fundamentos,variaveis,entrada-saida,condicionais,loops,funcoes,arrays,strings,arquivos,processamento-texto,erros,debug,portabilidade,boas-praticas,tests,lib,bin} \
  filesystem/{navegacao,arquivos-diretorios,links,permissoes,arquivos-temporarios,limpeza,fixtures,tests} \
  users-permissions/{usuarios,grupos,sudo,permissoes-acl,ssh-keys,tests} \
  processes/{ps-top,signals,job-control,prioridades,resource-limits,tests} \
  services/{systemctl,health-checks,service-recovery,tests} \
  systemd/{units,timers,logs,service-examples,tests} \
  packages/{apt,repositories,cache,package-inventory,tests} \
  networking/{ip-route,ports,sockets,curl,wget,firewall,tests} \
  ssh/{client,hardening,automation,known-hosts,tests} \
  storage/{disk-usage,mounts,filesystems,lvm,backups,restore,tests} \
  logs/{journalctl,grep-awk-sed,rotation,parsing,alerts,fixtures,tests} \
  cron/{jobs,environment,locking,logging,tests} \
  dns/{dig,host,nslookup,resolution,tests} \
  web-server/{nginx,health-check,static-site,reverse-proxy,tests} \
  troubleshooting/{runbooks,incidents,diagnostics,postmortems,evidence} \
  automation/{inventory,backup,health-check,reporting,deployment,cleanup,tests} \
  devops/{git,ci,artifacts,containers,compose,security,observability} \
  projects/{system-inventory,backup-manager,service-monitor,log-analyzer,web-health-monitor}
```

### 3.1 Descrição das pastas principais

| Pasta | O que praticar |
|---|---|
| `bash/fundamentos` | shebang, execução, comandos, variáveis e códigos de saída |
| `bash/processamento-texto` | `grep`, `cut`, `sort`, `uniq`, `tr`, `sed`, `awk`, `xargs` |
| `bash/erros` | `set -Eeuo pipefail`, traps, validação e tratamento de erro |
| `filesystem` | caminhos, arquivos, links, permissões, temporários e limpeza |
| `users-permissions` | usuários, grupos, `sudo`, ownership e acesso mínimo |
| `processes` | processos, sinais, jobs, prioridades e consumo de recursos |
| `services` / `systemd` | status, logs, reinício, units e timers |
| `networking` / `dns` | IP, rotas, portas, HTTP, DNS e diagnóstico |
| `storage` | espaço, inodes, mounts, backup e restauração |
| `logs` | journald, filtros, parsing, rotação e alertas |
| `cron` | tarefas agendadas, ambiente, locking e logs |
| `web-server` | Nginx, health checks e reverse proxy |
| `automation` | scripts operacionais reutilizáveis |
| `devops` | Git, CI, artefatos, containers, segurança e observabilidade |
| `projects` | projetos integradores com documentação e testes |
| `troubleshooting` | runbooks, incidentes, evidências e postmortems |

Para confirmar a estrutura:

```bash
tree -d -L 3 /home/Projetos/Linux/junior
```

Caso `tree` não esteja instalado:

```bash
find /home/Projetos/Linux/junior -type d | sort
```

---

## 4. Convenção para cada exercício

Cada exercício deve conter, no mínimo:

```text
exercicio-01/
├── README.md
├── scripts/
│   └── exercicio.sh
├── fixtures/
├── tests/
│   └── test.sh
└── evidence/
```

O `README.md` deve explicar:

1. Qual problema o exercício resolve.
2. Pré-requisitos.
3. Como executar.
4. Entradas esperadas.
5. Saídas esperadas.
6. Possíveis falhas.
7. Como desfazer ou limpar.
8. O que foi aprendido.

Modelo inicial:

```markdown
# Exercício: nome

## Objetivo

## Pré-requisitos

## Execução

```bash
bash scripts/exercicio.sh
```

## Resultado esperado

## Cenários de erro

## Limpeza

## Aprendizados
```

---

## 5. Bash essencial

### 5.1 Shebang e execução

Um script Bash deve declarar seu interpretador:

```bash
#!/usr/bin/env bash

printf 'Olá, Linux!\n'
```

Salve como `hello.sh`, dê permissão e execute:

```bash
chmod +x hello.sh
./hello.sh
```

Também é possível executar explicitamente pelo Bash:

```bash
bash hello.sh
```

Diferença importante: `./hello.sh` depende da permissão de execução e do shebang; `bash hello.sh` chama o Bash diretamente.

### 5.2 Variáveis e aspas

```bash
nome="laboratorio"
ambiente="dev"

printf 'Projeto: %s\n' "$nome"
printf 'Ambiente: %s\n' "$ambiente"
```

Use aspas em expansões de variáveis:

```bash
arquivo="meu arquivo.txt"
cat "$arquivo"
```

Sem aspas, espaços e caracteres especiais podem quebrar o comando.

Convenções úteis:

```bash
readonly SCRIPT_NAME="inventory"
readonly VERSION="1.0.0"

export APP_ENV="dev"
```

Use `readonly` para valores que não devem mudar. Use `export` somente quando um processo filho precisa receber a variável.

### 5.3 Entrada, saída e redirecionamento

```bash
read -r -p 'Informe o ambiente: ' ambiente
printf 'Ambiente selecionado: %s\n' "$ambiente"
```

Redirecionamentos:

```bash
comando > saida.txt       # substitui stdout
comando >> saida.txt      # adiciona stdout
comando 2> erro.txt       # salva stderr
comando > saida.txt 2>&1  # salva stdout e stderr
comando &> tudo.txt       # Bash: salva os dois
```

Pipe:

```bash
ps aux | grep '[n]ginx'
```

O padrão `'[n]ginx'` evita que o próprio `grep nginx` apareça no resultado.

### 5.4 Códigos de saída

Por convenção, `0` significa sucesso; qualquer valor diferente de zero indica falha.

```bash
true
echo "$?"

false
echo "$?"
```

Exemplo de validação:

```bash
if [[ -f /etc/hosts ]]; then
  printf 'Arquivo encontrado.\n'
else
  printf 'Arquivo ausente.\n' >&2
  exit 1
fi
```

### 5.5 Condicionais

```bash
if [[ "${1:-}" == "prod" ]]; then
  printf 'Atenção: ambiente de produção.\n'
elif [[ "${1:-}" == "dev" ]]; then
  printf 'Ambiente de desenvolvimento.\n'
else
  printf 'Uso: %s {dev|prod}\n' "$0" >&2
  exit 2
fi
```

Testes frequentes:

```bash
[[ -f arquivo ]]   # arquivo regular
[[ -d pasta ]]     # diretório
[[ -r arquivo ]]   # legível
[[ -w arquivo ]]   # gravável
[[ -x arquivo ]]   # executável
[[ -n "$valor" ]] # string não vazia
[[ "$a" == "$b" ]]
```

### 5.6 Loops

Percorrer arquivos com segurança:

```bash
while IFS= read -r arquivo; do
  printf 'Processando: %s\n' "$arquivo"
done < <(find . -maxdepth 1 -type f -print)
```

Percorrer argumentos:

```bash
for argumento in "$@"; do
  printf 'Argumento: %s\n' "$argumento"
done
```

Evite `for arquivo in $(find ...)`, porque quebra nomes contendo espaços, tabs ou novas linhas.

### 5.7 Funções

```bash
log_info() {
  printf '[INFO] %s\n' "$*"
}

log_error() {
  printf '[ERROR] %s\n' "$*" >&2
}

require_command() {
  command -v "$1" >/dev/null 2>&1 || {
    log_error "Comando obrigatório não encontrado: $1"
    return 1
  }
}
```

Funções devem ter responsabilidade clara e retornar sucesso ou falha de forma previsível.

### 5.8 Arrays

```bash
servicos=(ssh cron systemd-timesyncd)

for servico in "${servicos[@]}"; do
  printf 'Serviço: %s\n' "$servico"
done
```

Sempre use `"${array[@]}"` para preservar cada elemento como uma unidade.

---

## 6. Modelo de script operacional seguro

Use este esqueleto como ponto de partida:

```bash
#!/usr/bin/env bash
set -Eeuo pipefail

readonly SCRIPT_NAME="$(basename "$0")"
readonly SCRIPT_DIR="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"

log() {
  local level="$1"
  shift
  printf '[%s] [%s] %s\n' "$(date --iso-8601=seconds)" "$level" "$*"
}

die() {
  log ERROR "$*"
  exit 1
}

cleanup() {
  local status=$?
  # Remova arquivos temporários aqui, se existirem.
  exit "$status"
}
trap cleanup EXIT
trap 'die "Falha na linha $LINENO: $BASH_COMMAND"' ERR

usage() {
  printf 'Uso: %s [opções]\n' "$SCRIPT_NAME"
  printf '  -h, --help    mostra esta ajuda\n'
}

main() {
  log INFO "Iniciando $SCRIPT_NAME"
  usage
  log INFO "Finalizado com sucesso"
}

main "$@"
```

### 6.1 Quando usar `set -Eeuo pipefail`

- `-e`: interrompe quando um comando falha, salvo em contextos condicionais específicos.
- `-u`: trata variáveis não definidas como erro.
- `-o pipefail`: faz um pipeline falhar se qualquer etapa falhar.
- `-E`: preserva o comportamento de `trap ERR` em funções e subshells.

Teste a sintaxe antes de executar:

```bash
bash -n script.sh
```

Analise problemas de estilo:

```bash
shellcheck script.sh
```

Formate de maneira consistente, se `shfmt` estiver disponível:

```bash
shfmt -w script.sh
```

---

## 7. Comandos Linux que serão praticados

### 7.1 Navegação e arquivos

```bash
pwd                         # diretório atual
ls -lah                     # lista detalhada, incluindo ocultos
cd /var/log                 # muda de diretório
find . -type f -name '*.log' # encontra arquivos
stat arquivo.txt            # metadados
file arquivo.txt            # identifica tipo
realpath arquivo.txt        # mostra caminho absoluto
```

Criação e cópia:

```bash
mkdir -p fixtures/input
printf 'linha 1\n' > fixtures/input/exemplo.txt
cp fixtures/input/exemplo.txt fixtures/
mv fixtures/exemplo.txt fixtures/input/renomeado.txt
```

Links:

```bash
ln -s "$(realpath fixtures/input/renomeado.txt)" fixtures/atalho.txt
readlink -f fixtures/atalho.txt
```

### 7.2 Texto e dados

```bash
grep -Rni --include='*.log' 'error' logs/
cut -d: -f1 /etc/passwd
sort arquivo.txt | uniq -c | sort -nr
awk '{print $1, $NF}' arquivo.txt
sed -n '1,20p' arquivo.txt
tr '[:lower:]' '[:upper:]' < arquivo.txt
```

Para dados delimitados, prefira `awk` ou Python quando o formato for complexo. Antes de alterar muitos arquivos, teste a expressão sem `-i` no `sed`.

### 7.3 Usuários e permissões

```bash
whoami
id
getent passwd
getent group
ls -l arquivo
chmod 640 arquivo
chown usuario:grupo arquivo
```

Interpretação de `-rwxr-x---`:

```text
-       tipo: arquivo regular
rwx     proprietário: leitura, escrita, execução
r-x     grupo: leitura e execução
---     outros: nenhum acesso
```

Use notação simbólica quando ela comunicar melhor a intenção:

```bash
chmod u=rw,g=r,o= arquivo
chmod u+x script.sh
```

### 7.4 Processos

```bash
ps aux --sort=-%cpu | head
pgrep -a nginx
pstree -p
free -h
uptime
```

Sinais:

```bash
kill -TERM PID   # solicita encerramento limpo
kill -KILL PID   # força encerramento; último recurso
```

Nunca use `kill -9` como primeira tentativa. Investigue o processo e tente `TERM` antes.

### 7.5 Serviços e systemd

```bash
systemctl status ssh
systemctl is-active ssh
systemctl is-enabled ssh
sudo systemctl restart ssh
journalctl -u ssh --since '1 hour ago'
```

Antes de reiniciar um serviço, observe o status e os logs. Após a alteração, valide novamente.

### 7.6 Pacotes

Em Ubuntu/Debian:

```bash
apt-cache policy curl
sudo apt update
apt list --upgradable
sudo apt install curl
sudo apt remove pacote-exemplo
```

Não rode `apt upgrade` automaticamente em um script de produção sem política explícita, janela de mudança, logs e estratégia de rollback.

### 7.7 Rede e HTTP

```bash
ip addr
ip route
ss -tulpn
ping -c 3 1.1.1.1
getent hosts example.com
curl -I --max-time 10 https://example.com
curl -fsS --max-time 10 https://example.com >/dev/null
```

Diferença prática: `curl -I` inspeciona cabeçalhos; `curl -fsS` é adequado para health checks porque falha em HTTP 4xx/5xx e mostra erro sem ruído desnecessário.

### 7.8 Disco e armazenamento

```bash
df -h
df -ih
du -xhd1 /var 2>/dev/null | sort -h
lsblk -f
findmnt
```

Observe tanto espaço em bytes quanto inodes. Um sistema pode ter espaço livre e ainda falhar por falta de inodes.

### 7.9 Logs

```bash
journalctl -b
journalctl -p warning..alert
journalctl -u nginx --since today
journalctl -f
```

Leia logs com contexto: horário, host, serviço, usuário, correlação com uma mudança e impacto observado.

---

## 8. Projetos Bash obrigatórios

### Projeto 1 — `system-inventory`

Objetivo: gerar relatório de host contendo hostname, kernel, uptime, CPU, memória, discos, interfaces, usuários e serviços ativos.

Saída sugerida:

```text
reports/hostname-2026-09-07T153000Z.txt
```

Requisitos:

- Não depender de saída visual difícil de processar.
- Retornar erro se algum comando obrigatório estiver ausente.
- Permitir `--output arquivo`.
- Não expor segredos.

### Projeto 2 — `health-check`

Objetivo: verificar disco, memória, carga, DNS, conectividade HTTP e serviços.

Códigos de saída sugeridos:

```text
0 = saudável
1 = alerta
2 = erro de configuração
```

Exemplo de verificação HTTP:

```bash
if curl -fsS --max-time 5 https://example.com >/dev/null; then
  printf '[OK] HTTP disponível\n'
else
  printf '[CRITICAL] HTTP indisponível\n' >&2
  exit 1
fi
```

### Projeto 3 — `backup-manager`

Objetivo: compactar diretórios selecionados, gerar checksum, manter retenção e validar restauração.

Ferramentas:

```bash
tar -czf backup.tar.gz diretorio/
sha256sum backup.tar.gz > backup.tar.gz.sha256
sha256sum -c backup.tar.gz.sha256
tar -tzf backup.tar.gz
```

Nunca considere um backup válido sem testar a restauração:

```bash
mkdir -p restore-test
tar -xzf backup.tar.gz -C restore-test
```

### Projeto 4 — `log-analyzer`

Objetivo: contar erros por serviço, extrair períodos críticos e gerar resumo.

Requisitos:

- Aceitar arquivo como argumento.
- Não modificar o log original.
- Diferenciar ausência de arquivo de ausência de ocorrências.
- Gerar saída legível e, opcionalmente, CSV.

### Projeto 5 — `service-monitor`

Objetivo: verificar serviços, reiniciar somente quando autorizado e registrar todas as decisões.

Requisitos:

- Modo somente leitura por padrão.
- `--repair` habilita tentativa de recuperação.
- Limite de tentativas para não criar loop de reinício.
- Validação posterior com `systemctl is-active`.

### Projeto 6 — `web-health-monitor`

Objetivo: monitorar endpoints HTTP com timeout, código esperado e tempo de resposta.

Exemplo:

```bash
curl -fsS -o /dev/null \
  -w 'status=%{http_code} time=%{time_total}\n' \
  --connect-timeout 3 --max-time 10 \
  https://example.com
```

---

## 9. Automação com cron e systemd timer

### 9.1 Cron

Formato:

```text
MINUTO HORA DIA_DO_MÊS MÊS DIA_DA_SEMANA COMANDO
```

Exemplo a cada cinco minutos:

```cron
*/5 * * * * /home/usuario/lab/automation/health-check.sh >> /home/usuario/lab/logs/cron.log 2>&1
```

O cron possui ambiente reduzido. Use caminhos absolutos, defina `PATH` quando necessário e registre stdout/stderr.

Proteja contra execução sobreposta com `flock`:

```cron
*/5 * * * * flock -n /tmp/health-check.lock /home/usuario/lab/health-check.sh
```

### 9.2 systemd timer

O systemd oferece logs integrados, dependências e melhor controle operacional.

Exemplo de unit:

```ini
[Unit]
Description=Laboratório - verificação de saúde

[Service]
Type=oneshot
ExecStart=/home/usuario/lab/automation/health-check.sh
```

Exemplo de timer:

```ini
[Unit]
Description=Executa health check periodicamente

[Timer]
OnBootSec=2min
OnUnitActiveSec=5min
Persistent=true

[Install]
WantedBy=timers.target
```

Validação:

```bash
systemd-analyze verify health-check.service health-check.timer
systemctl --user daemon-reload
systemctl --user enable --now health-check.timer
systemctl --user list-timers
journalctl --user -u health-check.service
```

Use `systemd` em vez de cron quando precisar de dependências, status operacional, logs via journald e controle mais explícito.

---

## 10. Testes de scripts

### 10.1 Teste manual mínimo

Para cada script, teste:

```text
1. execução normal
2. argumento ausente
3. arquivo inexistente
4. permissão insuficiente
5. comando dependente ausente
6. entrada vazia
7. entrada com espaços
8. execução repetida
9. interrupção durante execução
10. falha de rede ou serviço
```

### 10.2 Testes Bash simples

```bash
#!/usr/bin/env bash
set -Eeuo pipefail

script="../scripts/system-inventory.sh"

[[ -x "$script" ]] || { echo 'script não executável' >&2; exit 1; }

if "$script" --help >/dev/null 2>&1; then
  echo '[PASS] --help'
else
  echo '[FAIL] --help' >&2
  exit 1
fi
```

Para projetos maiores, use Bats quando disponível:

```bash
bats tests/
```

### 10.3 Lint e sintaxe

```bash
bash -n script.sh
shellcheck script.sh
```

O lint não substitui teste funcional, mas encontra variáveis sem aspas, expansões frágeis, testes incorretos e vários erros comuns.

---

## 11. Git e fluxo de DevOps

Inicialize ou verifique o repositório:

```bash
git status
git branch --show-current
git log --oneline --decorate -5
```

Fluxo recomendado:

```bash
git checkout -b feat/system-inventory
git add bash/automation projects/system-inventory
git diff --cached
git commit -m 'feat: add system inventory exercise'
git status
```

Boas práticas:

- Commits pequenos e descritivos.
- Nunca versionar senhas, tokens, chaves privadas ou dumps sensíveis.
- Adicionar `.gitignore` para relatórios locais, caches e evidências grandes.
- Revisar `git diff --cached` antes do commit.
- Documentar mudanças que afetam execução ou permissões.

Exemplo de `.gitignore`:

```gitignore
*.log
*.tmp
.env
.env.*
!.env.example
reports/generated/
evidence/local/
__pycache__/
```

---

## 12. Evolução para CI/CD

Depois que os scripts estiverem funcionando localmente, automatize a validação:

```text
commit
  ↓
lint Bash com ShellCheck
  ↓
verificação bash -n
  ↓
testes funcionais
  ↓
criação de artefato
  ↓
publicação ou implantação controlada
  ↓
health check
```

Pipeline mínimo deve executar:

```bash
find . -type f -name '*.sh' -print0 | xargs -0 -r -n1 bash -n
find . -type f -name '*.sh' -print0 | xargs -0 -r shellcheck
```

Para implantação, sempre separe:

```text
validate → plan/dry-run → apply → verify → rollback
```

Scripts perigosos devem ter modo `--dry-run` antes de alterar o sistema.

---

## 13. Containers e automação reproduzível

A evolução natural dos scripts é executá-los em ambientes reproduzíveis.

Conceitos a praticar:

```text
imagem → container → volume → rede → health check → logs → limites de recursos
```

Exemplo seguro de exploração:

```bash
docker run --rm -it ubuntu:latest bash
```

O `--rm` remove o container ao sair. Não use imagens não confiáveis em ambientes importantes e não coloque segredos em Dockerfiles.

Quando houver aplicação ou serviço, adicione:

```text
Dockerfile
compose.yaml
.env.example
README.md
healthcheck
```

---

## 14. Segurança e DevSecOps no nível junior

A segurança começa nos scripts:

- Validar argumentos e caminhos.
- Evitar `eval`.
- Evitar interpolar entrada do usuário em comandos sem validação.
- Usar `--` antes de nomes que podem começar com hífen.
- Criar arquivos temporários com `mktemp`.
- Restringir permissões de arquivos sensíveis.
- Não registrar tokens e senhas nos logs.
- Aplicar timeout em chamadas de rede.
- Usar allowlist quando a entrada deve pertencer a um conjunto conhecido.

Exemplo de arquivo temporário:

```bash
tmp_file="$(mktemp)"
trap 'rm -f -- "$tmp_file"' EXIT
printf 'dados temporários\n' > "$tmp_file"
```

Exemplo de validação de ambiente:

```bash
case "${ENVIRONMENT:-}" in
  dev|test) ;;
  prod)
    printf 'Operação em produção exige revisão adicional.\n' >&2
    exit 3
    ;;
  *)
    printf 'Ambiente inválido. Use dev ou test.\n' >&2
    exit 2
    ;;
esac
```

---

## 15. Troubleshooting e incidentes

Cada falha deve virar um registro reproduzível:

```text
Data e hora:
Host:
Serviço afetado:
Sintoma:
Impacto:
Última mudança conhecida:
Comandos executados:
Evidências:
Hipótese:
Mitigação:
Causa raiz:
Ação preventiva:
```

Sequência operacional:

```text
Detectar
  ↓
Investigar
  ↓
Conter ou mitigar
  ↓
Recuperar
  ↓
Validar
  ↓
Documentar
  ↓
Prevenir recorrência
```

Incidentes para simular apenas em laboratório:

```text
serviço parado
arquivo de configuração inválido
permissão incorreta
disco quase cheio
processo consumindo CPU
DNS indisponível
endpoint HTTP retornando erro
job cron não executando
backup não restaurável
```

Não provoque falhas em sistemas de terceiros ou produção sem autorização explícita.

---

## 16. Plano de progressão sugerido

| Fase | Conteúdo | Entrega |
|---|---|---|
| 1 | Terminal, arquivos, permissões e texto | 20 exercícios pequenos |
| 2 | Bash, funções, argumentos e erros | 5 scripts reutilizáveis |
| 3 | Processos, serviços, logs e systemd | monitor de serviços |
| 4 | Rede, DNS e HTTP | health check completo |
| 5 | Backup e restauração | backup-manager testado |
| 6 | Git, ShellCheck e testes | pipeline de validação |
| 7 | Cron e systemd timers | automação periódica com logs |
| 8 | Docker e Compose | serviço reproduzível |
| 9 | Ansible e Terraform | configuração/IaC declarativa |
| 10 | Observabilidade e incidentes | métricas, logs, alertas e postmortem |

Critério para avançar: não basta o script funcionar uma vez. Ele deve ser compreensível, repetível, testado, documentado e capaz de falhar de forma controlada.

---

## 17. Checklist de qualidade para qualquer script

Antes de considerar um script concluído:

```text
[ ] possui shebang correto
[ ] possui README
[ ] valida argumentos
[ ] usa aspas nas variáveis
[ ] trata caminhos com espaços
[ ] retorna códigos de saída coerentes
[ ] possui mensagens de erro úteis
[ ] não expõe segredos
[ ] usa timeout em rede
[ ] é idempotente ou documenta a limitação
[ ] possui modo dry-run quando altera estado
[ ] foi validado com bash -n
[ ] foi analisado pelo ShellCheck
[ ] foi testado em cenário de sucesso
[ ] foi testado em cenário de falha
[ ] pode ser executado novamente
[ ] registra o que mudou
[ ] possui procedimento de limpeza ou rollback
```

---

## 18. Primeiro roteiro de execução

A sequência inicial recomendada é:

```bash
cd /home/Projetos/Linux/junior

# 1. Criar a estrutura de pastas deste documento.
# 2. Criar um README em cada área que receber exercício.
# 3. Implementar bash/fundamentos/hello.sh.
# 4. Implementar bash/erros/template-seguro.sh.
# 5. Implementar projects/system-inventory.
# 6. Executar bash -n e shellcheck.
# 7. Registrar evidências em evidence/.
# 8. Criar um commit pequeno.
# 9. Quebrar intencionalmente uma cópia em ambiente de teste.
# 10. Criar o primeiro runbook de troubleshooting.
```

Exercício inicial recomendado:

```bash
mkdir -p bash/fundamentos/hello/{scripts,tests,evidence}
cat > bash/fundamentos/hello/scripts/hello.sh <<'EOF'
#!/usr/bin/env bash
set -Eeuo pipefail

name="${1:-Linux}"
printf 'Olá, %s!\n' "$name"
EOF
chmod +x bash/fundamentos/hello/scripts/hello.sh
bash -n bash/fundamentos/hello/scripts/hello.sh
bash bash/fundamentos/hello/scripts/hello.sh DevOps
```

Saída esperada:

```text
Olá, DevOps!
```

---

## 19. Resultado esperado do laboratório

Ao concluir esta etapa, você deverá conseguir:

- Navegar e investigar um sistema Linux com segurança.
- Escrever scripts Bash legíveis e robustos.
- Automatizar tarefas administrativas repetitivas.
- Diagnosticar processos, serviços, rede, DNS, disco e logs.
- Criar health checks, inventários, backups e relatórios.
- Agendar tarefas com cron e systemd timers.
- Testar, validar e versionar scripts.
- Trabalhar com idempotência, dry-run, logs e rollback.
- Preparar scripts para CI/CD, containers e automação declarativa.
- Registrar incidentes, evidências, causa raiz e prevenção.

A trilha maior do repositório pode evoluir depois para Python, Ansible, Terraform, Docker, Kubernetes, observabilidade, SRE, DevSecOps e platform engineering. O fundamento, porém, será a capacidade de operar e automatizar Linux com Bash de maneira segura, reproduzível e observável.

---

## 20. Regra final do repositório

> **Toda tecnologia estudada precisa terminar em uma implementação prática, um teste, uma falha controlada, uma explicação e uma melhoria automatizada.**

Esse padrão transforma o diretório `junior` em um laboratório de engenharia, e não somente em uma lista de comandos.

---

*Documento inicial do laboratório Linux/DevOps — foco Bash e automação.*
