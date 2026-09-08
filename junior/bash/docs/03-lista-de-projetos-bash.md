# 🛠️ Guia Prático de Desenvolvimento dos Projetos Bash

> **Manual de Engenharia do Estudante:** Este documento ensina como criar, estruturar, testar e documentar cada um dos projetos da trilha. O objetivo não é apenas gerar um código `.sh`, mas sim construir uma solução completa de automação com testes, controle de erros e documentação.

---

## 📐 1. Estrutura Padrão de um Projeto

Todo projeto dentro das pastas de `projects/` deve seguir uma das duas estruturas abaixo:

### Estrutura Mínima (Projetos Iniciais / Níveis 1 a 3)

```text
projects/<nivel>/<nome-do-projeto>/
├── README.md             ← Documentação (objetivo, como rodar, erros esperados)
├── scripts/
│   └── projeto.sh        ← Script principal em Bash
├── tests/
│   └── test.sh           ← Teste de validação funcional
├── configs/
│   └── projeto.conf.example ← Template de configuração (quando necessário)
├── fixtures/             ← Dados estáticos de teste (quando necessário)
└── evidence/             ← Registros de execução e logs gerados
```

### Estrutura Profissional (Projetos Avançados / Níveis 4 a 10)

```text
projects/<nivel>/<nome-do-projeto>/
├── .github/workflows/
│   ├── lint.yml          ← Lint automatizado no CI
│   └── test.yml          ← Testes automatizados no CI
├── bin/
│   └── projeto           ← Executável principal (sem .sh, chmod +x)
├── lib/
│   ├── logger.sh         ← Módulo de logging
│   └── utils.sh          ← Módulo de funções auxiliares
├── tests/
│   ├── test_projeto.bats ← Testes em BATS
│   └── test_helper.bash  ← Setup e teardown dos testes
├── config/
│   ├── default.env       ← Configurações padrão
│   └── .env.example      ← Template de ambiente
├── Makefile              ← make lint, make test, make build
├── .shellcheckrc         ← Regras do ShellCheck
├── .gitignore            ← Exclusões do Git
└── README.md             ← Documentação principal
```

---

## 🏷️ 2. Regras de Nomenclatura e Convenções

### Nomes de Arquivos e Diretores
* Use sempre letras minúsculas separadas por hífen (`kebab-case`).
* ✅ **Correto:** `health-check.sh`, `system-inventory.sh`, `log-analyzer.sh`
* ❌ **Incorreto:** `MeuScript.sh`, `script_v2_final.sh`, `HEALTH_CHECK.SH`, `script 1.sh`

### Padrão de Shebang e Flags de Segurança
Todo arquivo Bash **DEVE** iniciar obrigatoriamente com o Shebang moderno e as opções de controle estrito de erro:

```bash
#!/usr/bin/env bash
set -Eeuo pipefail
```

**O que cada flag significa (Nota do Professor):**
* `#!/usr/bin/env bash` → Localiza o executável do Bash dinamicamente no `PATH` do sistema (portável entre diferentes distribuições Linux).
* `set -e` (`errexit`) → Aborta a execução imediatamente se qualquer comando retornar um código de saída diferente de 0.
* `set -u` (`nounset`) → Trata o uso de qualquer variável não declarada como um erro fatal.
* `set -o pipefail` → Se qualquer comando dentro de um pipeline (`cmd1 | cmd2`) falhar, o pipeline inteiro falhará com o erro dessa etapa.
* `set -E` (`errtrace`) → Garante que gatilhos `trap ERR` sejam herdados por funções e subshells.

---

## 🔄 3. Ciclo de Desenvolvimento de um Projeto (Passo a Passo)

Para cada projeto da lista, siga este roteiro de trabalho:

```text
  1. Entender o problema no README
        │
        ▼
  2. Escrever o script em scripts/projeto.sh
        │
        ▼
  3. Aplicar permissão de execução: chmod +x scripts/projeto.sh
        │
        ▼
  4. Validar sintaxe: bash -n scripts/projeto.sh
        │
        ▼
  5. Análise estática: shellcheck scripts/projeto.sh
        │
        ▼
  6. Escrever e rodar os testes em tests/
        │
        ▼
  7. Simular falhas (arquivos ausentes, permissão negada)
        │
        ▼
  8. Registrar a evidência e atualizar a documentação
```

---

## 📄 4. Modelos de Código para Uso nos Projetos

### Modelo A: Template de Script Principal (`scripts/projeto.sh`)

```bash
#!/usr/bin/env bash
# =============================================================================
# PROJETO: system-info
# DESCRIÇÃO: Coleta e exibe informações essenciais do sistema operando
# AUTOR: Estudante Linux DevOps
# =============================================================================
set -Eeuo pipefail

# Constantes globais legíveis
readonly SCRIPT_NAME="$(basename "$0")"
readonly SCRIPT_DIR="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"

# Função para exibição de mensagens de log
log_info() {
  printf '[INFO] [%s] %s\n' "$(date --iso-8601=seconds)" "$*"
}

log_error() {
  printf '[ERROR] [%s] %s\n' "$(date --iso-8601=seconds)" "$*" >&2
}

# Tratamento de saída limpa (Limpeza de temporários)
cleanup() {
  local exit_code=$?
  # Remova arquivos temporários aqui, se houver
  exit "$exit_code"
}
trap cleanup EXIT

# Exibição de Ajuda
usage() {
  cat <<EOF
Uso: $SCRIPT_NAME [OPÇÕES]

Opções:
  -h, --help      Exibe este menu de ajuda e sai.
  -v, --verbose   Ativa o modo detalhado de execução.

Exemplos:
  ./$SCRIPT_NAME
  ./$SCRIPT_NAME --help
EOF
}

# Função Principal
main() {
  if [[ "${1:-}" == "-h" || "${1:-}" == "--help" ]]; then
    usage
    exit 0
  fi

  log_info "Iniciando verificação do sistema..."

  local host_name kernel_version uptime_info
  host_name="$(hostname)"
  kernel_version="$(uname -r)"
  uptime_info="$(uptime -p 2>/dev/null || uptime)"

  printf '\n--- RELATÓRIO DO SISTEMA ---\n'
  printf 'Hostname: %s\n' "$host_name"
  printf 'Kernel:   %s\n' "$kernel_version"
  printf 'Uptime:   %s\n' "$uptime_info"
  printf '-----------------------------\n\n'

  log_info "Execução concluída com sucesso."
}

main "$@"
```

---

### Modelo B: Template de Teste Funcional (`tests/test.sh`)

```bash
#!/usr/bin/env bash
# =============================================================================
# ARQUIVO DE TESTE: tests/test.sh
# DESCRIÇÃO: Valida o comportamento do script principal
# =============================================================================
set -Eeuo pipefail

readonly BASE_DIR="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")/.." && pwd)"
readonly SCRIPT="${BASE_DIR}/scripts/system-info.sh"

pass_count=0
fail_count=0

assert_success() {
  local test_name="$1"
  shift
  if "$@">/dev/null 2>&1; then
    printf '  [PASS] %s\n' "$test_name"
    ((pass_count++))
  else
    printf '  [FAIL] %s\n' "$test_name" >&2
    ((fail_count++))
  fi
}

printf '=== Executando Testes para: %s ===\n' "$(basename "$SCRIPT")"

# Teste 1: O arquivo existe e é executável
assert_success "O script é executável" test -x "$SCRIPT"

# Teste 2: O parâmetro --help retorna exit code 0
assert_success "Opção --help funciona" "$SCRIPT" --help

# Resumo dos testes
printf '\nResultado: %d passou, %d falhou.\n' "$pass_count" "$fail_count"

if [[ "$fail_count" -gt 0 ]]; then
  exit 1
fi
```

---

### Modelo C: Template de Documentação (`README.md`)

```markdown
# 📦 Nome do Projeto

## 🎯 Objetivo
Descreva em 2 a 3 frases o objetivo prático que este script resolve no Linux/DevOps.

## 📋 Pré-requisitos
* Bash versão 4.0 ou superior
* Utilitários necessários: `grep`, `awk`, `curl`, `systemctl`

## 🚀 Como Executar

### Execução Direta
```bash
./scripts/nome-do-projeto.sh
```

### Execução dos Testes
```bash
./tests/test.sh
```

## ⚠️ Cenários de Erro e Validação
* **Erro 1:** Parâmetro ausente → Retorna `Exit Code 2`.
* **Erro 2:** Permissão negada → Retorna `Exit Code 1` com mensagem legível em `stderr`.

## 💡 Aprendizados
Liste os conceitos técnicos aprendidos durante o desenvolvimento deste exercício.
```

---

## 🚨 5. Os 10 Erros Mais Comuns em Scripts Bash (Evite!)

1. **Esquecer aspas nas variáveis (`$VAR` em vez de `"$VAR"`):**
   * *Problema:* Se `$VAR` contiver espaços, o comando entenderá como múltiplos argumentos.
2. **Usar `for file in $(ls)`:**
   * *Problema:* Quebra se o nome do arquivo tiver espaços. Use `for file in *` ou `while read`.
3. **Não tratar o erro em buscas com `grep`:**
   * *Problema:* `grep` retorna exit code 1 se não encontrar a string. Em scripts com `set -e`, o script morre. Use `grep ... || true` ou `if grep ...`.
4. **Hardcoding de caminhos (ex: `/home/srv/script`):**
   * *Problema:* O script não rodará no computador de outros desenvolvedores. Use caminhos relativos derivados de `$(dirname "${BASH_SOURCE[0]}")`.
5. **Usar `eval` para executar strings:**
   * *Problema:* Cria vulnerabilidades críticas de Injeção de Comandos.
6. **Gravar senhas e segredos dentro do arquivo `.sh`:**
   * *Problema:* Vazamento de credenciais no Git. Use arquivos `.env` ou variáveis de ambiente.
7. **Confundir `[` com `[[`:**
   * *Problema:* `[[ ]]` é a sintaxe nativa estendida do Bash, muito mais segura contra substituição de palavras e com suporte a regex (`=~`).
8. **Não especificar timeout em requisições de rede (`curl` sem `--max-time`):**
   * *Problema:* O script pode travar indefinidamente se a rede cair.
9. **Não usar funções locais (`local var`):**
   * *Problema:* Variáveis dentro de funções vazam para o escopo global do script, sobrescrevendo valores acidentalmente.
10. **Usar `rm -rf $DIR/*` sem validar se `$DIR` está vazio ou definido:**
    * *Problema:* Se `$DIR` estiver vazio, o comando vira `rm -rf /*` e apaga todo o sistema! Use `${DIR:?variável não definida}`.
