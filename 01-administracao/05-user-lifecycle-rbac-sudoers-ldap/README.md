# 05 — Automação de Ciclo de Vida de Usuários com RBAC via Sudoers e Grupos LDAP

## 🏢 Cenário de Produção e Vida Real
Governança de privilégios mínimos para administradores e desenvolvedores com auditoria de comandos.

## 🚀 Arquitetura e Engenharia Linux
Implementação de engenharia avançada de sistemas Linux para produção, assegurando confiabilidade, resiliência, observabilidade e adesão estrita aos padrões de conformidade corporativa.

## 🛠️ Ferramentas e Utilitários Nativos Utilizados
`visudo, sudoers.d, id, getent`

## 📌 Exemplo de Execução CLI
```bash
visudo -cf /etc/sudoers.d/99-secops-rbac
```
