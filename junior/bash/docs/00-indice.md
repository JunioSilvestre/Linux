# 📚 Índice Geral e Guia Didático do Laboratório Bash & DevOps

> **Bem-vindo ao seu Laboratório Prático de Linux, Bash e DevOps!**  
> Este repositório foi construído com a filosofia de **Aprender Fazendo (Learning by Doing)**. Aqui você não é um mero leitor de teoria: você irá analisar, implementar, testar, simular falhas, diagnosticar e automatizar rotinas reais de um Engenheiro DevOps / Administrador de Sistemas Linux.

---

## 🎯 Metodologia Didática de Aprendizado

Para absorver 100% do conteúdo, siga o **Ciclo do Engenheiro**:

```
 ┌────────────────────────────────────────────────────────────────────────┐
 │                                                                        │
 │  1. ESTUDAR (Leia o lab e a cheatsheet)                               │
 │       │                                                                │
 │       ▼                                                                │
 │  2. IMPLEMENTAR (Crie o script na estrutura padronizada)              │
 │       │                                                                │
 │       ▼                                                                │
 │  3. TESTAR & LINT (Verifique com bash -n, ShellCheck e BATS)          │
 │       │                                                                │
 │       ▼                                                                │
 │  4. QUEBRAR EM AMBIENTE CONTROLADO (Simule falhas e permissões)        │
 │       │                                                                │
 │       ▼                                                                │
 │  5. DIAGNOSTICAR (Leia logs, entenda o exit code e descubra a causa)   │
 │       │                                                                │
 │       ▼                                                                │
 │  6. DOCUMENTAR & AUTOMATIZAR (Gere evidências e integre em pipelines) │
 │                                                                        │
 └────────────────────────────────────────────────────────────────────────┘
```

---

## 📖 Guia de Navegação da Documentação

Abaixo está o mapa completo de toda a documentação disponível na pasta `docs/`. Recomendamos seguir a leitura na ordem abaixo:

### 1. 📘 [01 - Laboratório Linux Junior, Bash e DevOps](01-linux-junior-bash-devops-lab.md)
* **O que é:** O manual guia principal do estudante.
* **O que você vai aprender:**
  * Princípios fundamentais: Idempotência, Menor Privilégio, Observabilidade, Segurança antes da velocidade.
  * Estrutura de pastas e boas práticas de organização de código.
  * Sintaxe essencial de Bash (Shebang, `set -Eeuo pipefail`, loops seguros, funções, arrays, traps).
  * Principais ferramentas Linux CLI (`find`, `grep`, `awk`, `sed`, `systemctl`, `journalctl`, `ip`, `ss`, `df`, `tar`).
  * Automação com Cron vs Systemd Timers.
  * Testes, CI/CD com GitHub Actions, Docker, DevSecOps e Postmortems de incidentes.

### 2. ⚡ [02 - Cheat Sheet Bash, Linux e DevOps](02-bash-linux-devops-cheatsheet.md)
* **O que é:** O seu guia de consulta rápida no dia a dia do terminal.
* **O que você vai encontrar:**
  * 40 seções temáticas de comandos com sintaxe, finalidade e exemplos reais.
  * Comandos de navegação, manipulação de arquivos, busca, permissões, processamento de texto.
  * Comandos de rede, DNS, HTTP (`curl`), monitoramento de recursos (`top`, `free`, `vmstat`), serviços e pacotes.
  * Referência rápida de Git, Docker, Docker Compose, Ansible, Terraform e Kubernetes (`kubectl`).
  * Checklist de segurança e scripts utilitários com notas do professor.

### 3. 📂 [03 - Lista de Projetos Bash](03-lista-de-projetos-bash.md)
* **O que é:** O catálogo prático dos projetos por nível.
* **O que você vai aprender:**
  * Regras de nomenclatura e convenções de arquivos em Shell.
  * Estruturação de projetos em diretórios (`scripts/`, `tests/`, `configs/`, `fixtures/`, `evidence/`).
  * Roteiro passo a passo de desenvolvimento de cada projeto.
  * Modelos de `README.md` e scripts de teste funcional para validar seu código.

### 4. 🗂️ [04 - Lista Geral de Projetos](04-lista-geral.md)
* **O que é:** O mapa completo dos **139 Projetos Práticos**, divididos do Nível 1 ao Nível 10.
* **Tabela de Níveis:**
  * **Nível 1:** Fundamentos do Bash (Variáveis, Argumentos, Condições)
  * **Nível 2:** Filesystem & Arquivos (Permissões, Busca, Links, Reorganização)
  * **Nível 3:** Processos, Usuários & Permissões (Auditoria, Sudo, Chaves SSH)
  * **Nível 4:** Serviços & Systemd (Watchdogs, Recovery, Timers)
  * **Nível 5:** Rede, DNS & HTTP (Port-checks, Health checks, Certificados SSL)
  * **Nível 6:** Logs & Troubleshooting (Parsing de logs, Evidências, Postmortems)
  * **Nível 7:** Storage, Backup & Restauração (Tar, Checksum, Retenção, Restore test)
  * **Nível 8:** Cron, Timers & Automação (Locks, Retries, Notificações)
  * **Nível 9:** Bash Avançado & Qualidade (Bibliotecas `.lib.sh`, Parsers, Dry-run)
  * **Nível 10:** Projetos Integradores DevOps (Plataforma de Automação, Deployments, CI/CD)

### 5. 🏗️ [04 - Lista de Pastas e Arquitetura de Projetos](04-lista-Pastas.md)
* **O que é:** O padrão arquitetural de engenharia para projetos CLI profissionais.
* **O que você vai aprender:**
  * Por que separar `bin/` de `lib/`, `tests/` e `config/`.
  * Como transformar um simples `.sh` em uma ferramenta de linha de comando de nível corporativo.
  * Papel do CI/CD (`.github/workflows`), Dockerfile, Makefile e ShellCheck no ciclo de vida de uma aplicação.

---

## 🗺️ Mapa de Diretórios dos Projetos no Repositório

Os projetos práticos desenvolvidos por você ficarão organizados na seguinte árvore de diretórios:

```text
/home/Projetos/Linux/junior/bash/projects/
├── junior-01-fundamentos/             → (Projetos 01 a 15)
├── junior-02-filesystem/              → (Projetos 16 a 30)
├── junior-03-system-administration/   → (Projetos 31 a 45)
├── junior-04-services/                → (Projetos 46 a 57)
├── junior-05-networking/              → (Projetos 58 a 72)
├── junior-06-logs-troubleshooting/    → (Projetos 73 a 86)
├── junior-07-storage-backup/          → (Projetos 87 a 98)
├── junior-08-automation/              → (Projetos 99 a 110)
├── junior-09-bash-advanced/           → (Projetos 111 a 124)
└── junior-10-devops-projects/         → (Projetos 125 a 139)
```

---

## 🎓 Dica do Professor: Por Onde Começar Hoje?

1. Comece lendo a **Seção 1 e 5** do [01 - Laboratório Linux Junior](01-linux-junior-bash-devops-lab.md).
2. Abra o primeiro projeto de treino em `projects/junior-01-fundamentos/hello-bash/`.
3. Inspecione a estrutura profissional explicada em [04 - Lista de Pastas](04-lista-Pastas.md).
4. Mantenha a [02 - Cheat Sheet](02-bash-linux-devops-cheatsheet.md) aberta em uma aba para consultar comandos rapidamente.
5. Bons estudos e excelente código! 🚀
