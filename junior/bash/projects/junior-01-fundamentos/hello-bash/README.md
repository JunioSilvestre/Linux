# 🚀 hello-bash — CLI de Demonstração e Arquitetura Shell

[![Lint](https://github.com/JunioSilvestre/Linux/actions/workflows/lint.yml/badge.svg)](../../.github/workflows)
[![Tests](https://github.com/JunioSilvestre/Linux/actions/workflows/test.yml/badge.svg)](../../.github/workflows)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

O **hello-bash** é o projeto modelo e de referência do **Nível 1 — Fundamentos do Bash** do repositório de Engenharia Linux e DevOps.

Ele demonstra como estruturar uma ferramenta de linha de comando (CLI) profissional usando Bash, aplicando modularidade, parsing seguro de argumentos, saída colorida de logs, suporte a Docker, testes funcionais e Makefile.

---

## 📐 Arquitetura do Projeto

```text
hello-bash/
├── bin/
│   └── hello-bash          # Entrypoint executável da CLI (sem extensão .sh)
├── lib/
│   ├── logger.sh           # Biblioteca de log (info, warn, error, debug, OK)
│   └── utils.sh            # Funções utilitárias (banners, checagem de comandos)
├── config/
│   ├── default.env         # Configurações padrão de ambiente
│   └── .env.example        # Modelo de configuração customizada
├── docs/
│   └── architecture.md     # ADR-001 de arquitetura do projeto
├── scripts/
│   └── hello-bash.sh       # Wrapper de compatibilidade
├── tests/
│   ├── test_hello.bats     # Suite de testes BATS
│   └── test_helper.bash    # Runner de testes funcionais em Bash puro
├── Dockerfile              # Imagem minimalista em Alpine/Bash
├── Makefile                # Target runner universal (make run, test, lint, build)
└── README.md               # Documentação principal
```

---

## 🛠️ Pré-requisitos

- **Bash** `>= 4.4` (recomendado `>= 5.0`)
- **Make** (opcional, para atalhos)
- **Docker** (opcional, para execução isolada em container)

---

## 🚀 Como Executar

### 1. Execução Direta
```bash
./bin/hello-bash
```

### 2. Com Parâmetros e Flags
```bash
# Saudação personalizada
./bin/hello-bash --name "Engenheiro DevOps"

# Modo de depuração (Verbose)
./bin/hello-bash -n "Linux" --verbose

# Sem cores ANSI
./bin/hello-bash --no-color

# Exibir versão ou ajuda
./bin/hello-bash --version
./bin/hello-bash --help
```

### 3. Execução via Makefile
```bash
make help    # Lista todos os alvos disponíveis
make run     # Executa o projeto localmente
make lint    # Verifica a sintaxe do Bash
make test    # Executa os testes funcionais
make build   # Gera o pacote de distribuição na pasta dist/
```

### 4. Execução via Docker
```bash
docker build -t hello-bash .
docker run --rm hello-bash --name "Containers Docker"
```

---

## 🧪 Testes e Qualidade

O projeto possui um runner de testes em Bash puro para execução imediata em qualquer ambiente Linux sem dependências extras:

```bash
./tests/test_helper.bash
```

Caso você tenha o framework [BATS (Bash Automated Testing System)](https://github.com/bats-core/bats-core) instalado:

```bash
bats tests/test_hello.bats
```

---

## 📜 Licença

Este projeto é disponibilizado sob a licença **MIT**. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.
