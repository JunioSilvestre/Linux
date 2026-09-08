#!/usr/bin/env bash
# =============================================================================
# ARQUIVO: lib/utils.sh
# PROPÓSITO: Biblioteca de funções utilitárias reutilizáveis.
#            É carregada (source) pelo entrypoint bin/hello-bash e por outros
#            módulos que precisem de utilidades genéricas.
#
# RESPONSABILIDADE:
#   - Funções de validação de argumentos e entradas do usuário
#   - Funções de manipulação de strings e arrays
#   - Funções de verificação de dependências do sistema (command -v)
#   - Helpers genéricos que não pertencem a nenhum módulo específico
#
# USO:
#   source "$(dirname "${BASH_SOURCE[0]}")/utils.sh"
# =============================================================================

# Prevenir múltipla inclusão (include guard)
if [[ -n "${_UTILS_SH_LOADED:-}" ]]; then
  return 0
fi
readonly _UTILS_SH_LOADED=1

# Verifica se um ou mais comandos existem no PATH
utils::check_cmd() {
  local missing=0
  for cmd in "$@"; do
    if ! command -v "${cmd}" >/dev/null 2>&1; then
      log::error "Dependência não encontrada no sistema: ${cmd}"
      missing=$((missing + 1))
    fi
  done
  return "${missing}"
}

# Remove espaços em branco nas extremidades de uma string
utils::trim() {
  local var="$*"
  # Remove leading space
  var="${var#"${var%%[![:space:]]*}"}"
  # Remove trailing space
  var="${var%"${var##*[![:space:]]}"}"
  printf "%s\n" "${var}"
}

# Valida se o argumento passado é um número inteiro
utils::is_integer() {
  local val="$1"
  [[ "${val}" =~ ^-?[0-9]+$ ]]
}

# Verifica se um arquivo existe e tem permissão de leitura
utils::is_readable_file() {
  local file="$1"
  [[ -f "${file}" && -r "${file}" ]]
}

# Imprime banner estilizado da aplicação
utils::print_banner() {
  local name="${1:-hello-bash}"
  local version="${2:-1.0.0}"
  cat <<EOF
 ┌────────────────────────────────────────────────────────────┐
 │  ${name} v${version}                                         │
 │  Projeto Didático DevOps & Linux Engineering               │
 └────────────────────────────────────────────────────────────┘
EOF
}
