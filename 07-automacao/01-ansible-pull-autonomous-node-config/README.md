# 01 — Configuração Autônoma de Nós Linux com Ansible-Pull e Repositório Git Central

## 🏢 Cenário de Produção e Vida Real
Servidores bare-metal que se auto-configuram ao ligar baixando playbooks do Git.

## 🚀 Arquitetura e Engenharia Linux
Implementação de engenharia avançada de sistemas Linux para produção, assegurando confiabilidade, resiliência, observabilidade e adesão estrita aos padrões de conformidade corporativa.

## 🛠️ Ferramentas e Utilitários Nativos Utilizados
`ansible-pull, git, systemd-timer`

## 📌 Exemplo de Execução CLI
```bash
ansible-pull -U https://github.com/corp/infra.git site.yml
```
