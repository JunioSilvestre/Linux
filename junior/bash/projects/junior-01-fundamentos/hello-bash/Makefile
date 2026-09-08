# =============================================================================
# ARQUIVO: Makefile
# PROPÓSITO: Interface universal de tarefas do projeto hello-bash.
# =============================================================================

.PHONY: help run test lint build clean install

SHELL := /usr/bin/env bash

# Alvo padrão quando apenas 'make' é executado
.DEFAULT_GOAL := help

help: ## Exibe este menu de ajuda
	@echo "Alvos disponíveis no Makefile do hello-bash:"
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "  \033[36m%-15s\033[0m %s\n", $$1, $$2}'

run: ## Executa a CLI localmente
	@./bin/hello-bash

test: ## Executa a suite de testes funcionais
	@./tests/test_helper.bash

lint: ## Valida a sintaxe do Bash em todos os arquivos
	@echo "Validando sintaxe com bash -n..."
	@bash -n bin/hello-bash lib/logger.sh lib/utils.sh scripts/hello-bash.sh
	@echo "Sintaxe OK!"

build: ## Empacota a aplicação na pasta dist/
	@echo "Empacotando aplicação em dist/..."
	@mkdir -p dist/bin dist/lib dist/config
	@cp bin/hello-bash dist/bin/
	@cp lib/*.sh dist/lib/
	@cp config/default.env dist/config/
	@chmod +x dist/bin/hello-bash
	@echo "Pacote gerado em dist/"

clean: ## Remove arquivos temporários e diretório dist/
	@echo "Limpando artefatos de build..."
	@rm -rf dist/
	@echo "Limpeza concluída."

install: build ## Instala o binário em /usr/local/bin (requer sudo)
	@echo "Instalando bin/hello-bash em /usr/local/bin/..."
	@sudo cp dist/bin/hello-bash /usr/local/bin/hello-bash
	@echo "Instalação concluída. Execute 'hello-bash' em qualquer terminal."
