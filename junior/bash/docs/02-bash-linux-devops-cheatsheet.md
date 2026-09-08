# ⚡ Cheat Sheet Didática — Bash, Linux e DevOps

> **Guia Didático do Professor:** Esta é a sua referência de consulta rápida de comandos e sintaxes para Linux, Bash, Automação, Redes, Containers e DevOps. Cada seção traz tabelas diretas de **sintaxe → finalidade → exemplo**, enriquecidas com **Dicas do Professor**, **Armadilhas Comuns** e **Aplicações Reais**.

---

## 1. Sintaxe Básica do Bash

| Sintaxe | Serve para | Exemplo | Nota do Professor |
|---|---|---|---|
| `#!/usr/bin/env bash` | Define o interpretador de forma portável | `#!/usr/bin/env bash` | Sempre use a primeira linha do script assim |
| `# comentário` | Adiciona comentário descritivo | `# Backup do banco` | Explique o *porquê*, não apenas o *o que* |
| `comando` | Executa um utilitário do sistema | `ls` | Retorna um exit code de 0 a 255 |
| `cmd1; cmd2` | Executa os dois comandos em sequência | `pwd; ls` | Executa o 2º mesmo que o 1º falhe |
| `cmd1 && cmd2` | Executa o 2º **apenas se** o 1º tiver sucesso | `mkdir app && cd app` | Controle lógico de fluxo seguro |
| `cmd1 \|\| cmd2` | Executa o 2º **apenas se** o 1º falhar | `test -f a \|\| echo ausente` | Útil para mensagens de erro fallback |
| `comando &` | Executa em segundo plano (background) | `sleep 10 &` | Retorna o PID no terminal via `$!` |
| `$(comando)` | Substituição moderna de comando | `data=$(date)` | Preferível em relação a crases `` `date` `` |
| `\` | Continua o comando na linha seguinte | `echo "linha 1" \` | Melhora a legibilidade de comandos longos |

### Execução e Diagnóstico de Scripts

| Comando | Serve para | Exemplo Prático |
|---|---|---|
| `chmod +x script.sh` | Concede permissão de execução | `chmod +x bin/hello-bash` |
| `./script.sh` | Executa invocando o Shebang | `./bin/hello-bash` |
| `bash script.sh` | Executa forçando o interpretador Bash | `bash scripts/hello.sh` |
| `bash -n script.sh` | **Verifica a sintaxe** sem executar o script | `bash -n bin/hello-bash` |
| `bash -x script.sh` | **Modo Debug:** Exibe cada comando e expansão | `bash -x scripts/hello.sh` |
| `source script.sh` ou `. script.sh` | Carrega funções/variáveis no shell **atual** | `source lib/logger.sh` |
| `type comando` | Identifica se o comando é um builtin, alias ou binário | `type cd` |
| `which comando` | Localiza o caminho absoluto do executável no `PATH` | `which nginx` |

### Opções de Segurança Integradas (`set`)

```bash
set -Eeuo pipefail
```

* 🛡️ **`set -e`**: Aborta imediatamente no primeiro comando que falhar.
* 🛡️ **`set -u`**: Trata variáveis não inicializadas como erro.
* 🛡️ **`set -o pipefail`**: Captura erros em qualquer etapa de comandos com `|`.
* 🛡️ **`set -E`**: Garante que os gatilhos `trap` continuem ativos dentro de funções.

---

## 2. Variáveis e Manipulação de Strings

| Sintaxe | Serve para | Exemplo | Dica do Professor |
|---|---|---|---|
| `VAR=valor` | Declara variável (sem espaços!) | `NAME="Linux"` | NUNCA coloque espaços ao redor do `=` |
| `"$VAR"` | Expande valor da variável | `echo "$NAME"` | **Sempre use aspas duplas!** |
| `'texto'` | String literal (não expande nada) | `'Olá $NAME'` | Imprime `$NAME` literalmente |
| `export VAR=valor` | Torna a variável visível para subprocessos | `export APP_ENV=dev` | Passa a variável para scripts filhos |
| `readonly VAR=valor` | Cria uma constante imutável | `readonly PORT=8080` | O Bash impede alterações futuras |
| `${VAR:-padrao}` | Retorna `padrao` se `VAR` estiver vazia | `${PORT:-8080}` | Excelente para valores padrão |
| `${VAR:=padrao}` | Define `VAR=padrao` se estiver vazia | `${DIR:=/tmp}` | Atribui e retorna o valor |
| `${VAR:?mensagem}` | Interrompe com erro se `VAR` for vazia | `${TOKEN:?Falta token}` | Validação de variáveis obrigatórias |
| `${#VAR}` | Retorna o tamanho (comprimento) da string | `${#NAME}` | Útil em validações de tamanho |
| `${VAR:inicio:tam}` | Extrai sub-string a partir da posição | `${NAME:0:3}` | Extrai os 3 primeiros caracteres |
| `${VAR/busca/subst}` | Substitui a primeira ocorrência | `${FILE/.txt/.log}` | Renomeia extensões em memória |
| `${VAR//busca/subst}`| Substitui todas as ocorrências | `${TEXT// /_}` | Troca espaços por underscores |
| `$0` | Nome do script invocado | `echo "$0"` | Nome do executável |
| `$1`, `$2` ... | Argumentos posicionais passados | `echo "$1"` | Primeiro argumento |
| `$#` | Quantidade total de argumentos passados | `if [[ $# -lt 1 ]]` | Validação de quantidade de parâmetros |
| `"$@"` | Lista de todos os argumentos preservando espaços | `for arg in "$@"` | **Preferido** em relação a `$*` |
| `$?` | Exit code do último comando executado (0 a 255) | `echo "$?"` | 0 = Sucesso, >0 = Falha |
| `$$` | PID (Process ID) do script atual | `echo "$$"` | Útil para arquivos de lock em `/tmp` |

---

## 3. Redirecionamentos, Streams e Pipes

No Linux, os três fluxos padrão são:
* **0 - `stdin`** (Entrada padrão - Teclado)
* **1 - `stdout`** (Saída padrão - Tela)
* **2 - `stderr`** (Saída de erro - Tela)

```
        ┌───────────────┐  stdout (1) ──> Tela / Arquivo
stdin ─>│  Comando CLI  │
        └───────────────┘  stderr (2) ──> Tela / Arquivo de Log
```

| Sintaxe | Função | Exemplo Prático |
|---|---|---|
| `cmd > file` | Redireciona `stdout` sobrescrevendo o arquivo | `date > data.txt` |
| `cmd >> file` | Redireciona `stdout` adicionando ao final do arquivo | `echo "Log" >> app.log` |
| `cmd 2> file` | Redireciona apenas os erros (`stderr`) | `ls /root 2> erros.log` |
| `cmd > file 2>&1` | Redireciona tanto `stdout` quanto `stderr` para o mesmo arquivo | `backup.sh > all.log 2>&1` |
| `cmd &> file` | Forma curta do Bash para juntar `stdout` e `stderr` | `backup.sh &> all.log` |
| `cmd > /dev/null 2>&1` | Silencia completamente qualquer saída do comando | `grep -q "root" /etc/passwd >/dev/null 2>&1` |
| `cmd1 \| cmd2` | Conecta o `stdout` do 1º comando ao `stdin` do 2º | `ps aux \| grep nginx` |
| `cmd \| tee file` | Exibe a saída na tela **E** salva simultaneamente em arquivo | `make test \| tee test.log` |
| `cmd \| tee -a file` | Exibe na tela e adiciona ao arquivo (`append`) | `systemctl status \| tee -a audit.log` |

---

## 4. Condicionais e Testes (`[[ ]]`)

Sempre prefira `[[ ]]` (sintaxe estendida do Bash) ao invés do `[` antigo.

### Testes de Arquivos e Diretórios

| Teste | Verdadeiro se... | Exemplo |
|---|---|---|
| `[[ -f file ]]` | O arquivo existe e é um **arquivo regular** | `[[ -f /etc/hosts ]]` |
| `[[ -d dir ]]` | O caminho existe e é um **diretório** | `[[ -d /var/log ]]` |
| `[[ -e path ]]` | O caminho existe (qualquer tipo) | `[[ -e /tmp/app.sock ]]` |
| `[[ -L link ]]` | O caminho é um **link simbólico** | `[[ -L /bin/sh ]]` |
| `[[ -r file ]]` | O arquivo tem permissão de **leitura** para o usuário | `[[ -r config.env ]]` |
| `[[ -w file ]]` | O arquivo tem permissão de **escrita** para o usuário | `[[ -w /var/log/app.log ]]` |
| `[[ -x file ]]` | O arquivo tem permissão de **execução** | `[[ -x /usr/bin/curl ]]` |
| `[[ -s file ]]` | O arquivo existe e **NÃO está vazio** (tamanho > 0) | `[[ -s output.txt ]]` |

### Comparação Numérica vs Comparação de String

```text
  NUMÉRICO:   -eq (equal), -ne (not equal), -lt (less than), -le (less equal), -gt (greater than), -ge (greater equal)
  STRINGS:    == (igual), != (diferente), -z (vazia), -n (não vazia), =~ (regex match)
```

```bash
# Exemplo de Condicional Completo:
if [[ -z "${1:-}" ]]; then
  echo "Erro: Informe o nome do usuário como argumento!" >&2
  exit 1
elif [[ "$1" =~ ^[a-z_][a-z0-9_-]*$ ]]; then
  echo "Usuário válido: $1"
else
  echo "Erro: Formato de nome de usuário inválido!" >&2
  exit 2
fi
```

---

## 5. Processamento de Texto: Grep, Awk e Sed

Estes três utilitários são a espinha dorsal da manipulação de dados em Linux.

### 5.1 Grep (Busca de Padrões)
* `grep 'erro' app.log` → Busca a palavra 'erro' no arquivo.
* `grep -i 'error' app.log` → Ignora diferença entre maiúsculas e minúsculas (`case-insensitive`).
* `grep -v 'DEBUG' app.log` → Inverte a busca (mostra tudo que **NÃO** contém 'DEBUG').
* `grep -r 'TODO' src/` → Busca recursiva em todos os arquivos da pasta.
* `grep -E 'ERROR|FATAL' app.log` → Usa Expressões Regulares Estendidas (OU lógico).
* `grep -c 'FAIL' test.log` → Conta o número de linhas correspondentes.

### 5.2 Awk (Processamento de Colunas e Dados Tabulares)
* `awk '{print $1}' log.txt` → Imprime apenas a **1ª coluna** da entrada.
* `awk '{print $1, $NF}' log.txt` → Imprime a **1ª coluna** e a **última coluna** (`$NF`).
* `awk -F: '{print $1, $6}' /etc/passwd` → Define o separador de campos como `:` (ex: `/etc/passwd`).
* `awk '$3 > 80 {print $1, $3}' disco.txt` → Filtra linhas onde a 3ª coluna é maior que 80.

### 5.3 Sed (Edição de Texto em Fluxo)
* `sed 's/http/https/' file.txt` → Substitui a **primeira** ocorrência de 'http' por 'https' em cada linha.
* `sed 's/http/https/g' file.txt` → Substitui **todas** as ocorrências na linha (`g` = global).
* `sed -i 's/dev/prod/g' config.env` → **Edita o arquivo diretamente** no disco (`in-place`).
* `sed -n '10,20p' file.txt` → Imprime apenas as linhas de 10 a 20.

---

## 6. Gerenciamento de Processos, Recursos e Sinais

### Sinais do Linux (`kill`)
* 🟢 **`SIGTERM (15)`**: Solicitação graciosa de encerramento. O processo pode capturar e fechar arquivos/conexões antes de sair.
* 🔴 **`SIGKILL (9)`**: Destruição imediata pelo Kernel. O processo não pode capturar nem ignorar. **Use apenas em último caso!**
* 🟡 **`SIGHUP (1)`**: Sinal de recarregamento de configuração (muito usado por serviços como Nginx/Apache).

```bash
# Monitorar quem mais consome CPU:
ps aux --sort=-%cpu | head -n 10

# Monitorar quem mais consome Memória RAM:
ps aux --sort=-%mem | head -n 10

# Matar processo graciosamente pelo nome:
pkill -15 -x nginx

# Garantir execução sem travar o script concorrente:
flock -n /tmp/meu-script.lock ./meu-script.sh
```

---

## 7. Serviços e Systemd

```bash
# Verificar status de um serviço:
systemctl status nginx

# Iniciar, Parar e Reiniciar:
sudo systemctl start nginx
sudo systemctl stop nginx
sudo systemctl restart nginx

# Habilitar no boot do sistema:
sudo systemctl enable nginx
sudo systemctl disable nginx

# Listar unidades que falharam no boot:
systemctl --failed

# Visualizar logs em tempo real do serviço:
journalctl -u nginx -f --since "1 hour ago"
```

---

## 8. Rede, HTTP e Diagnóstico CLI

```bash
# Verificar endereços IP e interfaces:
ip addr show

# Verificar a tabela de roteamento e Gateway:
ip route

# Listar portas TCP/UDP abertas escutando e seus PIDs:
ss -tulpn

# Fazer requisição HTTP trazendo apenas o status code:
curl -s -o /dev/null -w "%{http_code}\n" --max-time 5 https://example.com

# Inspecionar cabeçalhos de resposta HTTP:
curl -I https://example.com

# Consultar registros DNS A de forma limpa:
dig +short A example.com

# Testar se a porta 22 de um servidor remoto está aberta:
nc -zv 192.168.1.100 22
```

---

## 9. Discos, Backup e Compactação

```bash
# Relatório de espaço em disco legível:
df -h

# Relatório de Inodes livres:
df -i

# Identificar as maiores pastas dentro de /var:
du -xhd1 /var | sort -hr | head -n 10

# Criar backup compactado .tar.gz:
tar -czfp backup-$(date +%Y%m%d).tar.gz /etc /var/www

# Validar integridade sem extrair:
tar -tzf backup.tar.gz >/dev/null && echo "Backup OK"

# Extrair em diretório específico:
tar -xzf backup.tar.gz -C /tmp/restauracao/
```

---

## 10. Referência Rápida para DevOps (Docker, Git e CI/CD)

### 🐙 Git Essencial
```bash
git status                            # Estado atual dos arquivos
git checkout -b feat/nova-funcionalidade # Cria e muda para nova branch
git add .                             # Prepara alterações para commit
git commit -m "feat: adiciona script" # Cria commit com mensagem padronizada
git pull origin main --rebase         # Atualiza branch com rebase limpo
git push origin feat/nova-funcionalidade # Envia para o repositório remoto
```

### 🐳 Docker & Containers
```bash
docker build -t minha-cli:1.0 .       # Constrói imagem Docker local
docker run --rm -it minha-cli:1.0     # Executa container removendo ao sair
docker ps -a                           # Lista todos os containers
docker logs -f <container_id>          # Acompanha logs do container
docker exec -it <container_id> bash    # Abre shell dentro do container ativo
```

---

## 💡 Regra Final do Engenheiro

> **Instale e use sempre o ShellCheck:**
> Antes de subir qualquer script para repositório ou produção, execute:
> ```bash
> shellcheck scripts/meu-script.sh
> ```
> O ShellCheck detecta antecipadamente mais de 90% dos erros de execução comuns em scripts Bash.
