# 🏗️ Arquitetura Padronizada de Projetos Bash & DevOps

> **Padrão de Engenharia:** Este documento define a estrutura de diretórios e arquivos exigida para projetos Shell/Bash de nível profissional em ambientes de produção e DevOps.

---

## 🌳 Árvore de Arquitetura do Projeto (`hello-bash` como referência)

```text
hello-bash/
├── .github/                  
│   └── workflows/            → Pipelines de CI/CD (Integração Contínua)
│       ├── lint.yml          → Executa linter estático (ShellCheck) a cada PR/push
│       └── test.yml          → Executa a suite de testes automatizados (BATS)
├── bin/                      
│   └── hello-bash            → Entrypoint executável principal (chmod +x, SEM extensão .sh)
├── lib/                      
│   ├── utils.sh              → Funções utilitárias genéricas e validações exportadas
│   └── logger.sh             → Funções padronizadas de log (log::info, log::error, log::debug)
├── tests/                    
│   ├── fixtures/             → Dados mock estáticos e arquivos de entrada para testes
│   ├── test_hello.bats       → Casos de teste escritos no framework BATS (Bash Automated Testing System)
│   └── test_helper.bash      → Scripts de setup(), teardown() e helpers para os testes
├── config/                   
│   ├── default.env           → Variáveis de ambiente padrão (padrões seguros e padrão de fábrica)
│   └── .env.example          → Template contendo as variáveis obrigatórias para o desenvolvedor copiar (.env)
├── docs/                     
│   └── architecture.md       → Registro de Decisões de Arquitetura (ADRs - Architecture Decision Records)
├── Makefile                  → Interface universal de tarefas (make help, make lint, make test, make build)
├── Dockerfile                → Especificação de container OCI para rodar a CLI isolada em qualquer SO
├── .shellcheckrc             → Regras de qualidade de código e análise estática do ShellCheck
├── .gitignore                → Regras de exclusão do Git (impede commit de .env, logs e temporários)
├── README.md                 → Manual do usuário, pré-requisitos, guia de uso e badges de status do CI
└── LICENSE                   → Termos legais e licença de uso (ex: MIT, Apache 2.0)
```

---

## 👨‍🏫 Explicação Didática: Por que Cada Pasta/Arquivo Existe?

### 1. `bin/hello-bash` (O Entrypoint Executável)
* **Por que não tem extensão `.sh`?** Na convenção de ferramentas CLI de mercado (como `docker`, `kubectl`, `git`), o comando é invocado pelo nome da ferramenta. A extensão `.sh` é um detalhe de implementação interna e não deve ser exposta na interface do usuário.
* **Permissão:** Deve possuir permissão de execução ativa (`chmod +x bin/hello-bash`).
* **Função:** Atua como orquestrador. Ele não deve ter 500 linhas de código bagunçado; ele apenas lê argumentos, carrega as bibliotecas em `lib/` e chama as funções correspondentes.

### 2. `lib/` (Camada de Bibliotecas e Módulos Reutilizáveis)
* **O que colocar aqui?** Módulos de funções coesas. 
  * `logger.sh`: Centraliza formatação de mensagens, cores ANSI e redirecionamentos para `stderr`.
  * `utils.sh`: Contém validações de IP, checagens de existência de dependências (`command -v`), saneamento de strings, etc.
* **Como carregar:** O entrypoint usa o comando `source` (ou `.`) apontando para o caminho relativo dinâmico:
  ```bash
  readonly SCRIPT_DIR="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")/.." && pwd)"
  source "${SCRIPT_DIR}/lib/logger.sh"
  source "${SCRIPT_DIR}/lib/utils.sh"
  ```

### 3. `tests/` (Garantia de Qualidade e Suites de Testes)
* **Por que usar BATS?** O BATS (Bash Automated Testing System) permite escrever testes automatizados em sintaxe idêntica ao Bash, validando se a saída (`stdout`), erros (`stderr`) e códigos de retorno (`exit status`) estão corretos.
* **`test_helper.bash`:** Define a função `setup()` (executada antes de cada teste) para criar pastas temporárias limpas e `teardown()` (executada após cada teste) para remover sujeira do sistema.
* **`fixtures/`:** Guarda arquivos de exemplo, arquivos de log falsos ou respostas de chamadas HTTP mockadas para que os testes não dependam de serviços externos reais.

### 4. `config/` (Gerenciamento de Ambientes)
* **`default.env`:** Contém os parâmetros padrão que o script usa caso o usuário não informe configurações específicas.
* **`.env.example`:** Serve como um "contrato". Ele é commitado no repositório com valores de exemplo (`DB_HOST=localhost`). O desenvolvedor copia esse arquivo para `.env` (que está no `.gitignore`) e coloca suas credenciais locais sem risco de vazar segredos no Git.

### 5. `.github/workflows/` (CI/CD - Integração Contínua)
* **Por que CI/CD no dia 0?** Erros em scripts Shell costumam ser silenciosos ou ocorrer apenas no cliente final. Ter pipelines automatizadas que rodam o **ShellCheck** e os **Testes BATS** em cada `git push` garante que nenhum código quebrado chegue à branch principal (`main`).

### 6. `Makefile` (Interface Universal de Desenvolvedor)
* **Por que ter um Makefile em projeto Bash?** O Makefile unifica os comandos do projeto. Em vez de memorizar comandos longos de teste ou lint, o desenvolvedor digita apenas:
  * `make lint` → Roda o ShellCheck em todo o repositório.
  * `make test` → Executa a suite BATS.
  * `make build` → Garante permissões e prepara a distribuição.

### 7. `Dockerfile` (Containerização)
* **Benefício:** Permite rodar a sua CLI em ambientes heterogêneos (Alpine Linux, Ubuntu, Debian, RedHat, macOS, Windows via WSL) com a garantia de que a versão exata do Bash e das dependências do sistema estarão presentes.

### 8. `.shellcheckrc` (Análise Estática de Código)
* **Função:** Define as regras ativas da ferramenta `shellcheck`. Ele obriga a citar variáveis com aspas `"$VAR"`, avisa sobre vazamentos de escopo de variáveis e aponta trechos vulneráveis a injeção de comandos.

---

## 📋 Resumo da Regra de Ouro da Arquitetura

```text
 ┌────────────────────────────────────────────────────────────────────────┐
 │ REGRA DA ENGENHARIA DE BASH:                                           │
 │                                                                        │
 │  1. O arquivo em bin/ orquestra a execução.                           │
 │  2. O código reutilizável fica em lib/*.sh.                            │
 │  3. Os parâmetros ficam em config/*.env.                               │
 │  4. As validações de segurança ficam em tests/*.bats.                  │
 │  5. A automação de build fica no Makefile e .github/workflows/.        │
 └────────────────────────────────────────────────────────────────────────┘
```