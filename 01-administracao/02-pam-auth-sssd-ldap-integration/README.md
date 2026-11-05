# 02 — Configuração e Auditoria de Módulos PAM com SSSD para Autenticação Centralizada

## 🏢 Cenário de Produção e Vida Real
Servidores corporativos que exigem autenticação segura via LDAP/Kerberos com fallback offline.

## 🚀 Arquitetura e Engenharia Linux
Implementação de engenharia avançada de sistemas Linux para produção, assegurando confiabilidade, resiliência, observabilidade e adesão estrita aos padrões de conformidade corporativa.

## 🛠️ Ferramentas e Utilitários Nativos Utilizados
`pam-auth-update, sssd, pam_faillock`

## 📌 Exemplo de Execução CLI
```bash
authselect select sssd with-mfa with-silent-lastlog
```
