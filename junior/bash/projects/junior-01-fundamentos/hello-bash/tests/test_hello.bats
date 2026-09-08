#!/usr/bin/env bats
# =============================================================================
# ARQUIVO: tests/test_hello.bats
# PROPÓSITO: Suite de testes automatizados escritos no framework BATS.
# =============================================================================

setup() {
  DIR="$(cd "$(dirname "$BATS_TEST_FILENAME")/.." && pwd)"
  PATH="$DIR/bin:$PATH"
}

@test "exibe menu de ajuda com --help" {
  run hello-bash --help
  [ "$status" -eq 0 ]
  [[ "$output" =~ "Uso: hello-bash" ]]
}

@test "exibe versão com --version" {
  run hello-bash --version
  [ "$status" -eq 0 ]
  [[ "$output" =~ "hello-bash versão" ]]
}

@test "executa saudação padrão sem argumentos" {
  run hello-bash
  [ "$status" -eq 0 ]
  [[ "$output" =~ "Olá, Mundo!" ]]
}

@test "saúda nome personalizado com -n" {
  run hello-bash -n "DevOps"
  [ "$status" -eq 0 ]
  [[ "$output" =~ "Olá, DevOps!" ]]
}

@test "falha com opção inválida" {
  run hello-bash --opcao-invalida
  [ "$status" -ne 0 ]
}
