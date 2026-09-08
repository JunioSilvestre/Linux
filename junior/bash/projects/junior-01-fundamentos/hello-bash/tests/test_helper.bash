#!/usr/bin/env bash
# =============================================================================
# ARQUIVO: tests/test_helper.bash
# PROPÓSITO: Runner de testes funcionais automatizados em Bash puro (sem dependências externas).
# =============================================================================

set -Eeuo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
BIN_PATH="${SCRIPT_DIR}/bin/hello-bash"

PASSED=0
FAILED=0

assert_contains() {
  local test_name="$1"
  local output="$2"
  local expected="$3"

  if [[ "${output}" == *"${expected}"* ]]; then
    printf "\033[32m[PASS]\033[0m %s\n" "${test_name}"
    PASSED=$((PASSED + 1))
  else
    printf "\033[31m[FAIL]\033[0m %s\n" "${test_name}"
    printf "   Esperado encontrar: '%s'\n" "${expected}"
    printf "   Obtido: '%s'\n" "${output}"
    FAILED=$((FAILED + 1))
  fi
}

assert_exit_code() {
  local test_name="$1"
  local expected_code="$2"
  local actual_code="$3"

  if [[ "${actual_code}" -eq "${expected_code}" ]]; then
    printf "\033[32m[PASS]\033[0m %s\n" "${test_name}"
    PASSED=$((PASSED + 1))
  else
    printf "\033[31m[FAIL]\033[0m %s\n" "${test_name}"
    printf "   Código de saída esperado: %d, obtido: %d\n" "${expected_code}" "${actual_code}"
    FAILED=$((FAILED + 1))
  fi
}

echo "=== Executando Suite de Testes Funcionais do hello-bash ==="

# Teste 1: Help Menu
out="$("${BIN_PATH}" --help)"
assert_contains "Menu de ajuda --help" "${out}" "Uso: hello-bash"

# Teste 2: Version Flag
out="$("${BIN_PATH}" --version)"
assert_contains "Exibição de versão --version" "${out}" "hello-bash versão"

# Teste 3: Execution Standard
out="$("${BIN_PATH}")"
assert_contains "Execução padrão (Mundo)" "${out}" "Olá, Mundo!"

# Teste 4: Custom Name
out="$("${BIN_PATH}" -n "Engenheiro DevOps")"
assert_contains "Saudação com nome customizado -n" "${out}" "Olá, Engenheiro DevOps!"

# Teste 5: Invalid Option
set +e
"${BIN_PATH}" --invalid-flag >/dev/null 2>&1
exit_code=$?
set -e
assert_exit_code "Código de saída de erro para opção inválida" 1 "${exit_code}"

echo "=========================================================="
printf "Resultado dos Testes: \033[32m%d Passaram\033[0m, \033[31m%d Falharam\033[0m\n" "${PASSED}" "${FAILED}"

if [[ "${FAILED}" -gt 0 ]]; then
  exit 1
fi
