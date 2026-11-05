# 08 — Renovação Automatizada de Certificados Digitais Internos via HashiCorp Vault

## 🏢 Cenário de Produção e Vida Real
Emissão e substituição de certificados TLS de microsserviços sem intervenção humana.

## 🚀 Arquitetura e Engenharia Linux
Implementação de engenharia avançada de sistemas Linux para produção, assegurando confiabilidade, resiliência, observabilidade e adesão estrita aos padrões de conformidade corporativa.

## 🛠️ Ferramentas e Utilitários Nativos Utilizados
`vault, openssl, systemctl`

## 📌 Exemplo de Execução CLI
```bash
./renew_certs_vault.sh --role web-cert --dest /etc/ssl
```
