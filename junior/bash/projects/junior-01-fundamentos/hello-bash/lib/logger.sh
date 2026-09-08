#!/usr/bin/env bash
# =============================================================================
# ARQUIVO: lib/logger.sh
# PROPÓSITO: Biblioteca de funções para saída padronizada no terminal.
#            Centraliza toda a comunicação com o usuário em um único lugar,
#            garantindo consistência visual e facilitando manutenção.
#
# RESPONSABILIDADE:
#   - log::info  "mensagem"  → saída informativa (stdout, prefixo [INFO])
#   - log::error "mensagem"  → saída de erro     (stderr, prefixo [ERROR])
#   - log::debug "mensagem"  → saída de depuração (apenas se DEBUG=1)
#   - log::warn  "mensagem"  → saída de aviso     (stdout, prefixo [WARN])
#   Cores ANSI opcionais controladas pela variável NO_COLOR
#
# USO:
#   source "$(dirname "${BASH_SOURCE[0]}")/logger.sh"
# =============================================================================

# Prevenir múltipla inclusão (include guard)
if [[ -n "${_LOGGER_SH_LOADED:-}" ]]; then
  return 0
fi
readonly _LOGGER_SH_LOADED=1

# Variáveis globais de controle
LOG_DEBUG_ENABLED="${DEBUG:-0}"
NO_COLOR="${NO_COLOR:-0}"

# Códigos de cor ANSI
if [[ "${NO_COLOR}" -eq 1 ]] || [[ ! -t 1 && "${FORCE_COLOR:-0}" -eq 0 ]]; then
  COLOR_RESET=""
  COLOR_BLUE=""
  COLOR_GREEN=""
  COLOR_YELLOW=""
  COLOR_RED=""
  COLOR_GRAY=""
else
  COLOR_RESET="\033[0m"
  COLOR_BLUE="\033[1;34m"
  COLOR_GREEN="\033[1;32m"
  COLOR_YELLOW="\033[1;33m"
  COLOR_RED="\033[1;31m"
  COLOR_GRAY="\033[0;90m"
fi

# Função auxiliar para gerar timestamp
log::_timestamp() {
  date +"%Y-%m-%d %H:%M:%S"
}

# Log de Informação (stdout)
log::info() {
  local msg="$*"
  printf "${COLOR_GRAY}[%s]${COLOR_RESET} ${COLOR_BLUE}[INFO]${COLOR_RESET} %s\n" "$(log::_timestamp)" "${msg}"
}

# Log de Sucesso (stdout)
log::success() {
  local msg="$*"
  printf "${COLOR_GRAY}[%s]${COLOR_RESET} ${COLOR_GREEN}[OK]${COLOR_RESET} %s\n" "$(log::_timestamp)" "${msg}"
}

# Log de Aviso (stdout)
log::warn() {
  local msg="$*"
  printf "${COLOR_GRAY}[%s]${COLOR_RESET} ${COLOR_YELLOW}[WARN]${COLOR_RESET} %s\n" "$(log::_timestamp)" "${msg}"
}

# Log de Erro (stderr)
log::error() {
  local msg="$*"
  printf "${COLOR_GRAY}[%s]${COLOR_RESET} ${COLOR_RED}[ERROR]${COLOR_RESET} %s\n" "$(log::_timestamp)" "${msg}" >&2
}

# Log de Depuração (stdout, visível apenas se DEBUG=1)
log::debug() {
  if [[ "${LOG_DEBUG_ENABLED}" -eq 1 ]]; then
    local msg="$*"
    printf "${COLOR_GRAY}[%s] ${COLOR_GRAY}[DEBUG] %s${COLOR_RESET}\n" "$(log::_timestamp)" "${msg}"
  fi
}
