# Documentação de Arquitetura e Decisões de Design (ADR)

## ADR-001: Estrutura Modular de CLI para Scripts em Bash

* **Status:** Aceito
* **Data:** 2026-09-08
* **Autor:** Laboratório de Engenharia Linux & DevOps

### Contexto
Scripts em Shell Script frequentemente crescem de forma desorganizada, transformando-se em arquivos únicos imensos ("monólitos .sh"), difíceis de testar, sem separação entre entrypoint e lógica de negócio, e sem convenções para logs ou tratamento de erro.

Para o laboratório de DevOps, precisávamos de um projeto modelo (modelo mental de excelência) para o Nível 1 (Fundamentos do Bash) que demonstrasse como elevar scripts Bash aos padrões de engenharia de software corporativo.

### Decisão
Adotar uma estrutura de diretórios padronizada inspirada em aplicações distribuídas e ferramentas de linha de comando corporativas:

```text
hello-bash/
├── .github/workflows/   → Integração Contínua (ShellCheck e BATS)
├── bin/                 → Entrypoints executáveis do usuário (sem extensão .sh)
├── config/              → Arquivos de configuração de ambiente (.env)
├── docs/                → Registros de decisões de arquitetura (ADR)
├── lib/                 → Bibliotecas modularizadas com funções (logger.sh, utils.sh)
├── scripts/             → Scripts de conveniência/automação
├── tests/               → Testes funcionais e unitários (BATS e bash pura)
├── Dockerfile           → Empacotamento em container minimalista
├── Makefile             → Interface universal de automação (make run, make test)
└── README.md            → Documentação e guia rápido do usuário
```

### Princípios Arquiteturais Aplicados:
1. **Separação de Responsabilidades:** O binário em `bin/` orquestra argumentos e chamadas; as bibliotecas em `lib/` contêm funções reutilizáveis; as configurações ficam em `config/`.
2. **Defensibilidade e Robustez:** Uso obrigatório de `set -Eeuo pipefail` e guards de inclusão (`_LOGGER_SH_LOADED`) para prevenir loop de `source`.
3. **Observabilidade:** Logs padronizados (`log::info`, `log::error`, `log::debug`) direcionados corretamente para `stdout` e `stderr`.
4. **Testabilidade:** Lógica isolada em funções permitindo testes unitários e de integração com BATS.

### Consequências
* **Positivas:** Reutilização de código, facilidade de manutenção, conformidade com linter `shellcheck`, e facilidade de integração em pipelines CI/CD.
* **Negativas:** Requer disciplina inicial para não colocar lógica diretamente no entrypoint e exige navegação entre múltiplos arquivos.
