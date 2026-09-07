# Cheat Sheet — Bash, Linux e DevOps

Referência rápida: **comando → finalidade → exemplo**.

---

## 1. Sintaxe básica do Bash

| Sintaxe | Serve para | Exemplo |
|---|---|---|
| `#!/usr/bin/env bash` | Define o interpretador | `#!/usr/bin/env bash` |
| `# comentário` | Adiciona comentário | `# backup diário` |
| `comando` | Executa comando | `ls` |
| `comando1; comando2` | Executa os dois | `pwd; ls` |
| `comando1 && comando2` | Executa o segundo se o primeiro funcionar | `mkdir app && cd app` |
| `comando1 || comando2` | Executa o segundo se o primeiro falhar | `test -f a || echo ausente` |
| `comando &` | Executa em segundo plano | `sleep 10 &` |
| `$(comando)` | Substituição de comando | `data=$(date)` |
| `` `comando` `` | Substituição antiga | `` `pwd` `` |
| `\` | Continua comando na próxima linha | `echo ola \` |
| `#` | Comentário | `echo oi # texto` |

### Execução de scripts

| Comando | Serve para |
|---|---|
| `bash script.sh` | Executa pelo Bash |
| `./script.sh` | Executa diretamente |
| `chmod +x script.sh` | Torna executável |
| `bash -n script.sh` | Verifica sintaxe |
| `bash -x script.sh` | Mostra comandos executados |
| `source script.sh` | Executa no shell atual |
| `. script.sh` | Forma curta de `source` |
| `command script` | Executa ignorando funções/aliases |
| `type comando` | Mostra origem do comando |
| `which comando` | Mostra caminho do executável |
| `whereis comando` | Localiza binário, manual e fonte |

### Opções de segurança

| Sintaxe | Serve para |
|---|---|
| `set -e` | Para ao ocorrer erro |
| `set -u` | Erra com variável não definida |
| `set -o pipefail` | Detecta erro em qualquer etapa do pipe |
| `set -Eeuo pipefail` | Combinação recomendada para scripts |
| `set -x` | Ativa modo debug |
| `set +x` | Desativa debug |
| `set -- args` | Redefine argumentos posicionais |

---

## 2. Variáveis e argumentos

| Sintaxe | Serve para | Exemplo |
|---|---|---|
| `VAR=valor` | Cria variável | `NAME=linux` |
| `"$VAR"` | Expande variável | `echo "$NAME"` |
| `'texto'` | Texto literal | `'Olá $NAME'` |
| `"texto"` | Permite expansão | `"Olá $NAME"` |
| `export VAR=valor` | Exporta para processos filhos | `export APP_ENV=dev` |
| `readonly VAR=valor` | Torna variável somente leitura | `readonly VERSION=1` |
| `${VAR:-valor}` | Usa valor padrão | `${PORT:-8080}` |
| `${VAR:=valor}` | Define padrão se vazia | `${DIR:=/tmp}` |
| `${VAR:?mensagem}` | Erra se não definida | `${TOKEN:?obrigatório}` |
| `${#VAR}` | Tamanho da string | `${#NAME}` |
| `${VAR:0:5}` | Recorta string | `${NAME:0:5}` |
| `${VAR/foo/bar}` | Substitui primeira ocorrência | `${FILE/.txt/.log}` |
| `${VAR//foo/bar}` | Substitui todas | `${TEXT// /_}` |
| `${VAR##*/}` | Remove prefixo maior | `${PATH##*/}` |
| `${VAR%/*}` | Remove sufixo maior | `${PATH%/*}` |
| `$0` | Nome do script | `echo "$0"` |
| `$1`, `$2` | Argumentos posicionais | `echo "$1"` |
| `$#` | Quantidade de argumentos | `echo "$#"` |
| `"$@"` | Todos os argumentos separados | `for x in "$@"` |
| `"$*"` | Todos como uma string | `echo "$*"` |
| `$?` | Código do último comando | `echo "$?"` |
| `$$` | PID do shell atual | `echo "$$"` |
| `$!` | PID do último processo em background | `echo "$!"` |
| `$-` | Opções atuais do shell | `echo "$-"` |
| `env` | Lista variáveis exportadas | `env` |
| `printenv VAR` | Mostra variável de ambiente | `printenv PATH` |
| `unset VAR` | Remove variável | `unset TOKEN` |

---

## 3. Entrada e saída

| Comando/sintaxe | Serve para | Exemplo |
|---|---|---|
| `echo` | Imprime texto simples | `echo "Olá"` |
| `printf` | Imprime com controle de formato | `printf '%s\n' "$NAME"` |
| `read` | Lê entrada | `read -r NAME` |
| `read -p` | Lê com mensagem | `read -r -p 'Nome: ' NAME` |
| `read -s` | Lê sem mostrar | `read -rs PASSWORD` |
| `read -n 1` | Lê quantidade de caracteres | `read -n 1 KEY` |
| `>` | Sobrescreve arquivo | `echo oi > file` |
| `>>` | Adiciona ao arquivo | `echo oi >> file` |
| `<` | Usa arquivo como entrada | `sort < file` |
| `2>` | Redireciona erros | `cmd 2> error.log` |
| `2>>` | Adiciona erros | `cmd 2>> error.log` |
| `&>` | Redireciona saída e erro | `cmd &> all.log` |
| `2>&1` | Junta stderr ao stdout | `cmd > all.log 2>&1` |
| `/dev/null` | Descarta saída | `cmd >/dev/null` |
| `tee` | Exibe e salva saída | `cmd | tee output.log` |
| `tee -a` | Exibe e adiciona ao arquivo | `cmd | tee -a output.log` |
| `<<EOF` | Here document | `cat <<EOF ... EOF` |
| `<<<` | Here string | `grep x <<< "$TEXT"` |

---

## 4. Navegação e diretórios

| Comando | Serve para | Exemplo |
|---|---|---|
| `pwd` | Mostra diretório atual | `pwd` |
| `ls` | Lista conteúdo | `ls` |
| `ls -l` | Lista detalhada | `ls -l` |
| `ls -a` | Inclui ocultos | `ls -a` |
| `ls -h` | Tamanhos legíveis | `ls -lh` |
| `ls -R` | Lista recursiva | `ls -R dir` |
| `ls -t` | Ordena por data | `ls -lt` |
| `ls -S` | Ordena por tamanho | `ls -lS` |
| `ls -d */` | Lista diretórios | `ls -d */` |
| `cd dir` | Entra no diretório | `cd /var/log` |
| `cd ..` | Sobe um nível | `cd ..` |
| `cd -` | Volta ao diretório anterior | `cd -` |
| `cd ~` | Vai para home | `cd ~` |
| `pushd dir` | Entra e salva caminho | `pushd /tmp` |
| `popd` | Retorna caminho salvo | `popd` |
| `mkdir dir` | Cria diretório | `mkdir app` |
| `mkdir -p a/b/c` | Cria pais necessários | `mkdir -p logs/app` |
| `rmdir dir` | Remove diretório vazio | `rmdir old` |
| `tree` | Exibe árvore | `tree -L 2` |
| `find` | Pesquisa arquivos | `find . -name '*.sh'` |
| `locate` | Pesquisa banco de nomes | `locate nginx.conf` |
| `realpath` | Mostra caminho absoluto | `realpath file` |
| `basename` | Extrai nome final | `basename /a/b.txt` |
| `dirname` | Extrai diretório | `dirname /a/b.txt` |

---

## 5. Arquivos e links

| Comando | Serve para | Exemplo |
|---|---|---|
| `touch` | Cria arquivo vazio/atualiza data | `touch file.txt` |
| `cat` | Exibe arquivo | `cat file.txt` |
| `cat -n` | Exibe com números | `cat -n file.txt` |
| `less` | Lê arquivo paginado | `less /var/log/syslog` |
| `head` | Primeiras linhas | `head -n 10 file` |
| `tail` | Últimas linhas | `tail -n 10 file` |
| `tail -f` | Acompanha arquivo | `tail -f app.log` |
| `cp` | Copia arquivo | `cp a b` |
| `cp -r` | Copia diretório | `cp -r src backup` |
| `cp -a` | Copia preservando atributos | `cp -a src backup` |
| `mv` | Move/renomeia | `mv old new` |
| `rm` | Remove arquivo | `rm file` |
| `rm -i` | Confirma remoção | `rm -i file` |
| `rm -r` | Remove recursivamente | `rm -r dir` |
| `rm -f` | Força remoção | `rm -f file` |
| `ln` | Cria hard link | `ln file link` |
| `ln -s` | Cria link simbólico | `ln -s target link` |
| `readlink` | Lê link simbólico | `readlink link` |
| `stat` | Metadados do arquivo | `stat file` |
| `file` | Identifica tipo | `file archive` |
| `truncate` | Redimensiona arquivo | `truncate -s 0 log` |
| `shred` | Sobrescreve arquivo | `shred -u secret` |
| `mktemp` | Cria temporário seguro | `mktemp` |

**Atenção:** evite `rm -rf` até entender exatamente o caminho expandido.

---

## 6. Busca de arquivos

| Comando | Serve para | Exemplo |
|---|---|---|
| `find . -type f` | Lista arquivos | `find . -type f` |
| `find . -type d` | Lista diretórios | `find . -type d` |
| `find . -name '*.log'` | Busca por nome | `find . -name '*.log'` |
| `find . -iname '*.LOG'` | Busca ignorando maiúsculas | `find . -iname '*.log'` |
| `find . -size +100M` | Busca por tamanho | `find . -size +100M` |
| `find . -mtime +7` | Modificados há mais de 7 dias | `find . -mtime +7` |
| `find . -mmin -30` | Modificados nos últimos 30 min | `find . -mmin -30` |
| `find . -empty` | Busca vazios | `find . -empty` |
| `find . -perm /111` | Busca executáveis | `find . -perm /111` |
| `find . -user root` | Busca por proprietário | `find . -user root` |
| `find . -exec cmd {} \;` | Executa por resultado | `find . -type f -exec file {} \;` |
| `find . -print0` | Saída segura para nomes especiais | `find . -print0` |
| `xargs -0` | Lê saída separada por NUL | `find . -print0 \| xargs -0 rm` |

---

## 7. Permissões e propriedade

| Comando | Serve para | Exemplo |
|---|---|---|
| `ls -l` | Mostra permissões | `ls -l file` |
| `chmod` | Altera permissões | `chmod 640 file` |
| `chmod +x` | Adiciona execução | `chmod +x script.sh` |
| `chmod u+x` | Execução para proprietário | `chmod u+x script.sh` |
| `chmod g+r` | Leitura para grupo | `chmod g+r file` |
| `chmod o-r` | Remove leitura de outros | `chmod o-r file` |
| `chmod -R` | Recursivo | `chmod -R 750 dir` |
| `chown` | Altera proprietário | `sudo chown user file` |
| `chown user:group` | Altera dono e grupo | `sudo chown user:group file` |
| `chgrp` | Altera grupo | `chgrp dev file` |
| `umask` | Mostra padrão de permissões | `umask` |
| `getfacl` | Lê ACLs | `getfacl file` |
| `setfacl` | Define ACL | `setfacl -m u:ana:r file` |
| `namei` | Mostra permissões do caminho | `namei -l /a/b/file` |
| `sudo` | Executa com privilégio | `sudo systemctl status ssh` |
| `id` | Mostra identidade | `id user` |

### Permissões octais

| Valor | Permissão |
|---:|---|
| `0` | `---` |
| `1` | `--x` |
| `2` | `-w-` |
| `3` | `-wx` |
| `4` | `r--` |
| `5` | `r-x` |
| `6` | `rw-` |
| `7` | `rwx` |

Exemplo: `chmod 750 script.sh` = proprietário `rwx`, grupo `r-x`, outros `---`.

---

## 8. Texto e processamento de dados

| Comando | Serve para | Exemplo |
|---|---|---|
| `grep texto file` | Pesquisa texto | `grep error app.log` |
| `grep -i` | Ignora maiúsculas | `grep -i error log` |
| `grep -n` | Mostra linha | `grep -n error log` |
| `grep -r` | Pesquisa recursiva | `grep -r TODO .` |
| `grep -v` | Exclui correspondências | `grep -v debug log` |
| `grep -E` | Regex estendida | `grep -E 'error|fail' log` |
| `grep -F` | Texto literal | `grep -F '[ERROR]' log` |
| `grep -c` | Conta ocorrências | `grep -c error log` |
| `cut -d: -f1` | Seleciona coluna | `cut -d: -f1 /etc/passwd` |
| `sort` | Ordena linhas | `sort names` |
| `sort -n` | Ordena numericamente | `sort -n values` |
| `sort -r` | Ordem reversa | `sort -r names` |
| `uniq` | Remove repetidas consecutivas | `sort file \| uniq` |
| `uniq -c` | Conta repetidas | `sort file \| uniq -c` |
| `wc -l` | Conta linhas | `wc -l file` |
| `wc -w` | Conta palavras | `wc -w file` |
| `wc -c` | Conta bytes | `wc -c file` |
| `tr` | Substitui caracteres | `tr a-z A-Z` |
| `tr -d` | Remove caracteres | `tr -d ':'` |
| `sed -n` | Imprime linhas selecionadas | `sed -n '1,5p' file` |
| `sed 's/a/b/'` | Substitui primeira ocorrência | `sed 's/http/https/' file` |
| `sed 's/a/b/g'` | Substitui todas na linha | `sed 's/http/https/g' file` |
| `sed -i` | Altera arquivo | `sed -i 's/a/b/g' file` |
| `awk` | Processa colunas e padrões | `awk '{print $1}' file` |
| `awk -F:` | Define separador | `awk -F: '{print $1}' /etc/passwd` |
| `paste` | Junta colunas | `paste names ids` |
| `join` | Cruza arquivos ordenados | `join users groups` |
| `diff` | Compara arquivos | `diff old new` |
| `comm` | Compara linhas ordenadas | `comm a b` |
| `column -t` | Alinha colunas | `cat data \| column -t` |
| `jq` | Processa JSON | `jq '.items[]' data.json` |
| `yq` | Processa YAML | `yq '.services' compose.yml` |

---

## 9. Pipes e filtros

| Sintaxe | Serve para | Exemplo |
|---|---|---|
| `cmd1 \| cmd2` | Saída vira entrada | `ps aux \| grep nginx` |
| `cmd \| head` | Primeiros resultados | `ls \| head` |
| `cmd \| tail` | Últimos resultados | `ls \| tail` |
| `cmd \| less` | Pagina resultado | `journalctl \| less` |
| `cmd \| tee file` | Exibe e salva | `date \| tee date.txt` |
| `cmd \| xargs` | Usa linhas como argumentos | `cat files \| xargs rm` |
| `cmd \| awk` | Filtra colunas | `ps aux \| awk '{print $1}'` |
| `cmd \| grep -v grep` | Exclui texto | `ps \| grep nginx \| grep -v grep` |

---

## 10. Testes e condicionais

| Sintaxe | Serve para |
|---|---|
| `if comando; then ... fi` | Condicional por código de saída |
| `if [[ condição ]]; then` | Condicional Bash |
| `elif` | Outra condição |
| `else` | Caso contrário |
| `case valor in ... esac` | Vários casos |
| `for x in lista; do ... done` | Loop sobre lista |
| `while condição; do ... done` | Loop enquanto condição verdadeira |
| `until condição; do ... done` | Loop até condição verdadeira |
| `break` | Sai do loop |
| `continue` | Pula para próxima iteração |
| `return 0` | Retorna sucesso de função |
| `exit 1` | Encerra script com erro |

### Testes de arquivos

| Teste | Significado |
|---|---|
| `-e file` | Existe |
| `-f file` | É arquivo regular |
| `-d dir` | É diretório |
| `-L link` | É link simbólico |
| `-r file` | Pode ler |
| `-w file` | Pode escrever |
| `-x file` | Pode executar |
| `-s file` | Não está vazio |
| `file1 -nt file2` | Mais novo que |
| `file1 -ot file2` | Mais antigo que |

### Testes de strings e números

| Sintaxe | Significado |
|---|---|
| `-z "$VAR"` | String vazia |
| `-n "$VAR"` | String não vazia |
| `"$A" = "$B"` | Strings iguais |
| `"$A" != "$B"` | Strings diferentes |
| `"$A" == pattern` | String com padrão |
| `A -eq B` | Igual numericamente |
| `A -ne B` | Diferente |
| `A -lt B` | Menor |
| `A -le B` | Menor ou igual |
| `A -gt B` | Maior |
| `A -ge B` | Maior ou igual |
| `! condição` | Negação |
| `cond1 && cond2` | E |
| `cond1 || cond2` | Ou |

---

## 11. Loops e funções

```bash
for item in one two three; do
  printf '%s\n' "$item"
done
```

```bash
while IFS= read -r line; do
  printf '%s\n' "$line"
done < file.txt
```

```bash
function log_info() {
  printf '[INFO] %s\n' "$*"
}

log_info 'processando'
```

| Sintaxe | Serve para |
|---|---|
| `function nome {}` | Declara função |
| `nome() {}` | Declara função |
| `local VAR` | Variável local da função |
| `$FUNCNAME` | Nome da função atual |
| `return N` | Retorna código |
| `shift` | Remove primeiro argumento |
| `shift 2` | Remove dois argumentos |
| `getopts` | Processa opções curtas |
| `select` | Cria menu numerado |

---

## 12. Arrays

| Sintaxe | Serve para |
|---|---|
| `arr=(a b c)` | Cria array |
| `arr[0]=a` | Define posição |
| `${arr[0]}` | Lê posição |
| `${arr[@]}` | Todos os itens |
| `${#arr[@]}` | Quantidade de itens |
| `arr+=(d)` | Adiciona item |
| `unset 'arr[1]'` | Remove item |
| `for x in "${arr[@]}"` | Percorre preservando itens |

---

## 13. Processos e jobs

| Comando | Serve para | Exemplo |
|---|---|---|
| `ps` | Lista processos | `ps aux` |
| `ps aux` | Todos os processos | `ps aux` |
| `ps -ef` | Formato completo | `ps -ef` |
| `top` | Monitor interativo | `top` |
| `htop` | Monitor melhorado | `htop` |
| `pgrep` | Pesquisa PID | `pgrep nginx` |
| `pidof` | PIDs de programa | `pidof nginx` |
| `pstree` | Árvore de processos | `pstree -p` |
| `jobs` | Jobs do shell | `jobs` |
| `bg` | Envia job para background | `bg %1` |
| `fg` | Traz job para foreground | `fg %1` |
| `nohup` | Continua após logout | `nohup cmd &` |
| `nice` | Inicia com prioridade | `nice -n 10 cmd` |
| `renice` | Altera prioridade | `renice 10 -p PID` |
| `kill -TERM PID` | Solicita encerramento | `kill -TERM 123` |
| `kill -KILL PID` | Força encerramento | `kill -KILL 123` |
| `killall` | Envia sinal por nome | `killall nginx` |
| `watch` | Repete comando | `watch -n 2 df -h` |
| `timeout` | Limita duração | `timeout 10s cmd` |
| `time` | Mede duração | `time ./script.sh` |
| `sleep` | Aguarda | `sleep 5` |
| `wait` | Aguarda job | `wait "$PID"` |
| `flock` | Cria lock | `flock -n /tmp/app.lock cmd` |

---

## 14. CPU, memória e desempenho

| Comando | Serve para |
|---|---|
| `uptime` | Carga e tempo ligado |
| `free -h` | Memória e swap |
| `vmstat 1` | Estatísticas do sistema |
| `iostat` | CPU e I/O de discos |
| `sar` | Histórico de desempenho |
| `mpstat` | Uso por CPU |
| `lscpu` | Informações da CPU |
| `lsmem` | Informações da memória |
| `dmesg` | Mensagens do kernel |
| `pidstat` | Estatísticas por processo |
| `strace` | Rastreia chamadas do sistema |
| `perf` | Perfil de desempenho |
| `iotop` | I/O por processo |
| `iotop -o` | Mostra somente processos com I/O |

---

## 15. Usuários e grupos

| Comando | Serve para |
|---|---|
| `whoami` | Usuário atual |
| `id` | UID, GID e grupos |
| `who` | Usuários conectados |
| `w` | Usuários e atividade |
| `last` | Histórico de logins |
| `lastlog` | Último login por usuário |
| `users` | Usuários conectados |
| `getent passwd` | Consulta usuários |
| `getent group` | Consulta grupos |
| `useradd` | Cria usuário |
| `usermod` | Altera usuário |
| `userdel` | Remove usuário |
| `groupadd` | Cria grupo |
| `groupmod` | Altera grupo |
| `groupdel` | Remove grupo |
| `passwd` | Altera senha |
| `su - user` | Troca de usuário |
| `sudo -l` | Mostra sudo permitido |
| `chage` | Gerencia validade de senha |

---

## 16. Serviços e systemd

| Comando | Serve para |
|---|---|
| `systemctl status serviço` | Status do serviço |
| `systemctl start serviço` | Inicia serviço |
| `systemctl stop serviço` | Para serviço |
| `systemctl restart serviço` | Reinicia serviço |
| `systemctl reload serviço` | Recarrega configuração |
| `systemctl enable serviço` | Ativa no boot |
| `systemctl disable serviço` | Remove do boot |
| `systemctl is-active serviço` | Testa se ativo |
| `systemctl is-enabled serviço` | Testa se habilitado |
| `systemctl list-units` | Lista units carregadas |
| `systemctl list-timers` | Lista timers |
| `systemctl --failed` | Lista falhas |
| `systemctl daemon-reload` | Recarrega units |
| `systemd-analyze verify file` | Valida unit |
| `journalctl -u serviço` | Logs do serviço |
| `journalctl -f` | Acompanha logs |
| `journalctl -b` | Logs do boot atual |
| `journalctl -p err` | Apenas erros |
| `journalctl --since today` | Logs desde hoje |

---

## 17. Pacotes Ubuntu/Debian

| Comando | Serve para |
|---|---|
| `apt update` | Atualiza índice |
| `apt upgrade` | Atualiza pacotes |
| `apt install pacote` | Instala pacote |
| `apt remove pacote` | Remove pacote |
| `apt purge pacote` | Remove pacote e configurações |
| `apt autoremove` | Remove dependências não usadas |
| `apt search termo` | Pesquisa pacotes |
| `apt show pacote` | Detalhes do pacote |
| `apt list --installed` | Lista instalados |
| `apt-cache policy pacote` | Versões e repositório |
| `dpkg -l` | Lista pacotes instalados |
| `dpkg -S /path/file` | Descobre pacote de arquivo |
| `dpkg -i arquivo.deb` | Instala `.deb` |
| `apt-mark hold pacote` | Bloqueia atualização |

---

## 18. Rede e sockets

| Comando | Serve para |
|---|---|
| `ip addr` | Interfaces e IPs |
| `ip link` | Estado das interfaces |
| `ip route` | Tabela de rotas |
| `ip neigh` | Vizinhos ARP/ND |
| `ss -tulpn` | Portas ouvindo |
| `ss -tan` | Conexões TCP |
| `ping -c 4 host` | Testa ICMP |
| `traceroute host` | Mostra rota |
| `tracepath host` | Traça caminho |
| `curl URL` | Faz requisição HTTP |
| `curl -I URL` | Cabeçalhos HTTP |
| `curl -f URL` | Falha em HTTP 4xx/5xx |
| `curl -sS URL` | Silencioso com erros |
| `curl -L URL` | Segue redirecionamentos |
| `curl -o file URL` | Salva resposta |
| `curl -w '%{http_code}'` | Mostra status HTTP |
| `wget URL` | Baixa recurso |
| `nc -vz host port` | Testa porta |
| `nmap host` | Varre portas; usar autorizado |
| `ethtool eth0` | Dados da interface |
| `nmcli` | Gerencia NetworkManager |
| `ufw status` | Status do firewall |
| `ufw allow 22/tcp` | Libera SSH no UFW |
| `ufw deny 23/tcp` | Bloqueia Telnet |

---

## 19. DNS

| Comando | Serve para |
|---|---|
| `hostname` | Nome do host |
| `hostnamectl` | Gerencia hostname |
| `getent hosts domain` | Resolve nome usando sistema |
| `dig domain` | Consulta DNS detalhada |
| `dig +short domain` | Resposta curta |
| `dig MX domain` | Consulta MX |
| `dig NS domain` | Consulta NS |
| `dig TXT domain` | Consulta TXT |
| `host domain` | Consulta simples |
| `nslookup domain` | Consulta DNS tradicional |
| `resolvectl status` | Estado do resolvedor |
| `resolvectl query domain` | Resolve via systemd-resolved |

---

## 20. Discos e armazenamento

| Comando | Serve para |
|---|---|
| `df -h` | Espaço dos filesystems |
| `df -i` | Inodes |
| `du -sh dir` | Tamanho do diretório |
| `du -h --max-depth=1` | Tamanho por nível |
| `lsblk` | Discos e partições |
| `lsblk -f` | Filesystem e UUID |
| `blkid` | Identifica dispositivos |
| `findmnt` | Mostra mounts |
| `mount` | Monta filesystem |
| `umount` | Desmonta filesystem |
| `sync` | Sincroniza buffers |
| `fdisk -l` | Lista partições |
| `parted -l` | Lista discos/partições |
| `lsof +L1` | Arquivos apagados ainda abertos |
| `tune2fs` | Ajusta ext filesystem |
| `fsck` | Verifica filesystem desmontado |
| `tar -czf` | Cria `.tar.gz` |
| `tar -xzf` | Extrai `.tar.gz` |
| `gzip` | Compacta gzip |
| `gunzip` | Descompacta gzip |
| `zip` | Cria ZIP |
| `unzip` | Extrai ZIP |
| `sha256sum` | Calcula checksum |
| `rsync -av` | Sincroniza arquivos |
| `rsync --delete` | Remove destino não existente na origem; cuidado |

---

## 21. SSH

| Comando | Serve para |
|---|---|
| `ssh user@host` | Acessa servidor |
| `ssh -p 2222 user@host` | Usa porta específica |
| `ssh -i key user@host` | Usa chave específica |
| `ssh-keygen` | Cria chave SSH |
| `ssh-copy-id user@host` | Copia chave pública |
| `scp file user@host:/tmp/` | Copia para servidor |
| `scp user@host:/tmp/file .` | Copia do servidor |
| `rsync -avz -e ssh src host:/dest` | Sincroniza via SSH |
| `ssh -L 8080:localhost:80 host` | Port forwarding local |
| `ssh -J jump user@host` | Usa bastion/jump host |
| `ssh-keyscan host` | Consulta chave pública do host |
| `ssh -o ConnectTimeout=5` | Define timeout |
| `~.` | Encerra sessão SSH travada |

---

## 22. Logs e auditoria

| Comando | Serve para |
|---|---|
| `journalctl` | Consulta journald |
| `journalctl -f` | Segue logs |
| `journalctl -u nginx` | Logs de unit |
| `journalctl -p warning` | Logs a partir de warning |
| `journalctl --since '1 hour ago'` | Período relativo |
| `dmesg -T` | Kernel com data legível |
| `logger 'mensagem'` | Envia mensagem ao syslog |
| `logrotate -d config` | Simula rotação |
| `logrotate -f config` | Força rotação |
| `last` | Logins anteriores |
| `lastb` | Logins falhos |
| `lastlog` | Último login |
| `ausearch` | Pesquisa auditoria |
| `auditctl` | Configura auditoria |
| `lsof` | Lista arquivos abertos |
| `fuser` | Mostra processo usando recurso |

---

## 23. Datas e cálculos

| Comando | Serve para |
|---|---|
| `date` | Data/hora atual |
| `date --iso-8601=seconds` | ISO 8601 |
| `date -u` | UTC |
| `date +%Y%m%d` | Formata data |
| `date -d 'tomorrow'` | Calcula data |
| `cal` | Calendário |
| `bc` | Calculadora CLI |
| `seq 1 10` | Gera sequência |
| `expr` | Operações simples |
| `$((1 + 2))` | Aritmética Bash |
| `printf '%02d' 5` | Formatação numérica |

---

## 24. Compactação e transferência

| Comando | Serve para |
|---|---|
| `tar -cf archive.tar dir` | Cria tar |
| `tar -xf archive.tar` | Extrai tar |
| `tar -czf archive.tar.gz dir` | Cria tar gzip |
| `tar -xzf archive.tar.gz` | Extrai tar gzip |
| `tar -cjf archive.tar.bz2 dir` | Cria tar bzip2 |
| `tar -xjf archive.tar.bz2` | Extrai tar bzip2 |
| `gzip file` | Compacta arquivo |
| `gzip -d file.gz` | Descompacta |
| `zip -r archive.zip dir` | Cria ZIP |
| `unzip archive.zip` | Extrai ZIP |
| `curl -O URL` | Baixa mantendo nome |
| `wget -c URL` | Continua download |

---

## 25. Git

| Comando | Serve para |
|---|---|
| `git init` | Inicializa repositório |
| `git clone URL` | Clona repositório |
| `git status` | Mostra estado |
| `git add file` | Prepara arquivo |
| `git add .` | Prepara alterações |
| `git diff` | Mostra alterações não preparadas |
| `git diff --cached` | Mostra staged |
| `git commit -m 'msg'` | Cria commit |
| `git log --oneline` | Histórico curto |
| `git show` | Mostra commit |
| `git branch` | Lista branches |
| `git switch -c nome` | Cria e muda branch |
| `git switch main` | Muda branch |
| `git merge branch` | Mescla branch |
| `git fetch` | Busca alterações remotas |
| `git pull` | Busca e integra |
| `git push` | Envia commits |
| `git remote -v` | Mostra remotos |
| `git tag v1.0.0` | Cria tag |
| `git stash` | Guarda alterações temporariamente |
| `git restore file` | Descarta alterações locais |
| `git reset` | Remove do staging |
| `git revert COMMIT` | Cria reversão segura |
| `git blame file` | Mostra autor por linha |
| `git clean -nd` | Simula limpeza |

---

## 26. ShellCheck, testes e qualidade

| Comando | Serve para |
|---|---|
| `bash -n script.sh` | Verifica sintaxe |
| `shellcheck script.sh` | Analisa boas práticas Bash |
| `shfmt -d script.sh` | Verifica formatação |
| `shfmt -w script.sh` | Formata script |
| `bats tests/` | Executa testes Bats |
| `make test` | Executa alvo de testes |
| `command -v cmd` | Verifica comando disponível |
| `test -f file` | Testa arquivo |
| `assert` | Afirmação em framework de teste |

---

## 27. Docker

| Comando | Serve para |
|---|---|
| `docker version` | Versão do Docker |
| `docker info` | Informações do daemon |
| `docker pull image` | Baixa imagem |
| `docker images` | Lista imagens |
| `docker build -t name .` | Cria imagem |
| `docker run image` | Executa container |
| `docker run --rm image` | Remove ao sair |
| `docker run -it image sh` | Terminal interativo |
| `docker run -d image` | Executa em background |
| `docker ps` | Containers ativos |
| `docker ps -a` | Todos os containers |
| `docker logs container` | Logs |
| `docker logs -f container` | Acompanha logs |
| `docker exec -it c sh` | Entra no container |
| `docker stop c` | Para container |
| `docker start c` | Inicia container parado |
| `docker restart c` | Reinicia container |
| `docker rm c` | Remove container |
| `docker rm -f c` | Força remoção |
| `docker rmi image` | Remove imagem |
| `docker inspect c` | Metadados |
| `docker stats` | Recursos em uso |
| `docker network ls` | Lista redes |
| `docker volume ls` | Lista volumes |
| `docker system df` | Uso de espaço |
| `docker system prune` | Limpa recursos não usados |

---

## 28. Docker Compose

| Comando | Serve para |
|---|---|
| `docker compose up` | Sobe serviços |
| `docker compose up -d` | Sobe em background |
| `docker compose down` | Derruba serviços |
| `docker compose ps` | Lista serviços |
| `docker compose logs` | Logs |
| `docker compose logs -f` | Acompanha logs |
| `docker compose exec svc sh` | Entra no serviço |
| `docker compose build` | Cria imagens |
| `docker compose pull` | Baixa imagens |
| `docker compose restart` | Reinicia serviços |
| `docker compose config` | Valida/renderiza configuração |
| `docker compose run --rm svc cmd` | Executa tarefa temporária |

---

## 29. Ansible

| Comando | Serve para |
---|---|
| `ansible --version` | Versão |
| `ansible all -i inventory -m ping` | Testa hosts |
| `ansible all -m setup` | Coleta facts |
| `ansible all -m shell -a 'cmd'` | Executa shell; usar com cautela |
| `ansible-playbook playbook.yml` | Executa playbook |
| `ansible-playbook --check file.yml` | Simula mudanças |
| `ansible-playbook --diff file.yml` | Mostra diferenças |
| `ansible-playbook -l host file.yml` | Limita hosts |
| `ansible-inventory --list` | Mostra inventário |
| `ansible-lint` | Analisa playbooks |
| `ansible-vault create secrets.yml` | Cria arquivo criptografado |
| `ansible-vault encrypt file` | Criptografa arquivo |
| `ansible-galaxy init role` | Cria role |

---

## 30. Terraform

| Comando | Serve para |
---|---|
| `terraform version` | Versão |
| `terraform init` | Inicializa projeto |
| `terraform fmt` | Formata arquivos |
| `terraform validate` | Valida configuração |
| `terraform providers` | Lista providers |
| `terraform plan` | Mostra mudanças |
| `terraform apply` | Aplica mudanças |
| `terraform apply -auto-approve` | Aplica sem confirmação; cuidado |
| `terraform destroy` | Destrói infraestrutura; cuidado |
| `terraform show` | Mostra estado/plan |
| `terraform output` | Mostra outputs |
| `terraform state list` | Lista recursos no state |
| `terraform state show recurso` | Mostra recurso |
| `terraform workspace list` | Lista workspaces |
| `terraform fmt -check` | Verifica formatação |

Fluxo recomendado:

```text
terraform fmt
terraform init
terraform validate
terraform plan
terraform apply
```

---

## 31. Kubernetes (`kubectl`)

| Comando | Serve para |
---|---|
| `kubectl version` | Versão |
| `kubectl cluster-info` | Informações do cluster |
| `kubectl get nodes` | Lista nodes |
| `kubectl get pods` | Lista pods |
| `kubectl get pods -A` | Pods em todos namespaces |
| `kubectl get deploy` | Lista deployments |
| `kubectl get svc` | Lista services |
| `kubectl get ns` | Lista namespaces |
| `kubectl describe pod POD` | Detalha pod |
| `kubectl logs POD` | Logs do pod |
| `kubectl logs -f POD` | Acompanha logs |
| `kubectl exec -it POD -- sh` | Terminal no pod |
| `kubectl apply -f file.yml` | Aplica manifesto |
| `kubectl delete -f file.yml` | Remove manifesto |
| `kubectl diff -f file.yml` | Mostra diferenças |
| `kubectl rollout status deploy/app` | Status do rollout |
| `kubectl rollout history deploy/app` | Histórico |
| `kubectl rollout undo deploy/app` | Reverte rollout |
| `kubectl scale deploy/app --replicas=3` | Altera réplicas |
| `kubectl port-forward svc/app 8080:80` | Encaminha porta |
| `kubectl config current-context` | Contexto atual |
| `kubectl config use-context ctx` | Troca contexto |

---

## 32. CI/CD e DevOps

| Conceito/comando | Serve para |
---|---|
| `lint` | Detecta problemas de estilo/qualidade |
| `test` | Executa testes |
| `build` | Gera artefato |
| `artifact` | Resultado versionado do build |
| `package` | Empacota aplicação |
| `deploy` | Publica versão |
| `rollback` | Retorna versão anterior |
| `health check` | Verifica funcionamento |
| `smoke test` | Teste rápido pós-deploy |
| `dry-run` | Simula sem alterar |
| `idempotent` | Repetição segura |
| `pipeline` | Fluxo automatizado |
| `registry` | Armazena imagens/pacotes |
| `secrets` | Guarda dados sensíveis |
| `SAST` | Análise de código estático |
| `DAST` | Teste dinâmico de aplicação |
| `SBOM` | Inventário de componentes |
| `IaC` | Infraestrutura como código |
| `GitOps` | Operação orientada por Git |
| `SLO` | Objetivo de nível de serviço |
| `SLI` | Indicador de nível de serviço |
| `SLA` | Acordo de nível de serviço |
| `RPO` | Perda de dados aceitável |
| `RTO` | Tempo aceitável de recuperação |

Pipeline básico:

```text
git commit
  ↓
syntax check
  ↓
lint
  ↓
test
  ↓
build
  ↓
security scan
  ↓
deploy
  ↓
health check
  ↓
monitoring
```

---

## 33. Observabilidade

| Ferramenta/comando | Serve para |
---|---|
| `Prometheus` | Métricas e alertas |
| `Grafana` | Dashboards |
| `Loki` | Logs |
| `ELK` | Elasticsearch, Logstash e Kibana |
| `OpenTelemetry` | Telemetria |
| `curl /metrics` | Consulta endpoint de métricas |
| `journalctl` | Logs do sistema |
| `top` | Recursos em tempo real |
| `ss` | Sockets e conexões |
| `df` | Espaço em disco |
| `free` | Memória |
| `uptime` | Carga |
| `systemctl --failed` | Serviços falhos |

Três sinais principais:

```text
Metrics → métricas
Logs    → eventos
Traces  → caminho da requisição
```

---

## 34. Comandos de troubleshooting

| Comando | Pergunta respondida |
---|---|
| `hostname` | Em qual máquina estou? |
| `whoami` | Qual usuário estou usando? |
| `id` | Quais são meus privilégios? |
| `pwd` | Em qual diretório estou? |
| `date` | Qual é o horário do sistema? |
| `uptime` | Há quanto tempo está ligado e qual a carga? |
| `df -h` | Há espaço em disco? |
| `df -i` | Há inodes disponíveis? |
| `free -h` | Há memória disponível? |
| `ps aux --sort=-%cpu` | Quem consome CPU? |
| `ps aux --sort=-%mem` | Quem consome memória? |
| `ss -tulpn` | Quais portas estão abertas? |
| `ip route` | Qual é a rota padrão? |
| `getent hosts domain` | DNS resolve? |
| `curl -v URL` | O que ocorre na conexão HTTP? |
| `systemctl status service` | O serviço está ativo? |
| `journalctl -u service` | O que o serviço registrou? |
| `dmesg -T` | O kernel registrou problema? |
| `lsof -i :PORT` | Quem usa a porta? |
| `fuser -v file` | Quem usa o arquivo? |
| `strace -p PID` | O que o processo está chamando? |
| `find / -xdev -type f -size +1G` | Quais arquivos são grandes? |

---

## 35. Padrão de script Bash recomendado

```bash
#!/usr/bin/env bash
set -Eeuo pipefail

readonly SCRIPT_NAME="$(basename "$0")"

log() {
  printf '[%s] %s\n' "$(date --iso-8601=seconds)" "$*"
}

die() {
  printf '[ERROR] %s\n' "$*" >&2
  exit 1
}

usage() {
  printf 'Uso: %s [opções]\n' "$SCRIPT_NAME"
}

main() {
  log 'Iniciando script'
  # implementação
  log 'Finalizado com sucesso'
}

main "$@"
```

---

## 36. Traps e limpeza

| Sintaxe | Serve para |
---|---|
| `trap 'cmd' EXIT` | Executa ao sair |
| `trap 'cmd' ERR` | Executa em erro |
| `trap 'cmd' INT` | Trata Ctrl+C |
| `trap -p` | Lista traps |
| `trap - ERR` | Remove trap |

Exemplo:

```bash
tmp_file="$(mktemp)"
trap 'rm -f -- "$tmp_file"' EXIT
```

---

## 37. Cron

Formato:

```text
MINUTO HORA DIA_MÊS MÊS DIA_SEMANA COMANDO
```

| Sintaxe | Frequência |
---|---|
| `* * * * *` | A cada minuto |
| `*/5 * * * *` | A cada 5 minutos |
| `0 * * * *` | A cada hora |
| `0 0 * * *` | Diariamente à meia-noite |
| `0 0 * * 0` | Domingo à meia-noite |
| `crontab -e` | Edita jobs do usuário |
| `crontab -l` | Lista jobs |
| `crontab -r` | Remove jobs; cuidado |
| `flock -n file cmd` | Evita sobreposição |

---

## 38. Regras rápidas de segurança

```text
Sempre use aspas:              "$VAR"
Valide entradas:               [[ -f "$FILE" ]]
Use caminhos controlados:      realpath
Evite eval:                    não execute entrada como código
Use --:                        rm -- "$file"
Use temporário seguro:         mktemp
Use timeout em rede:           curl --max-time 10
Teste antes de alterar:        --dry-run
Não versionar segredos:        .env, tokens, chaves privadas
Use menor privilégio:          sudo somente quando necessário
Teste restauração:             backup não testado não é confiável
Revise antes de apagar:        find ... -print antes de -delete
```

---

## 39. Sequência diária de prática

```bash
pwd
whoami
hostname
uptime
df -h
free -h
systemctl --failed
journalctl -p warning..alert --since today
ss -tulpn
```

## 40. Validação rápida de um script

```bash
bash -n script.sh
shellcheck script.sh
chmod +x script.sh
./script.sh --help
./script.sh --dry-run
```

---

> Use este arquivo como referência rápida. Para aprender de verdade, transforme cada grupo de comandos em um projeto `.sh`, documente o objetivo, crie testes e registre os resultados.
