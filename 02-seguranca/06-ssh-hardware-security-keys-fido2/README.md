# 06 — Autenticação SSH Restrita a Chaves Criptográficas de Hardware FIDO2 (YubiKey)

## 🏢 Cenário de Produção e Vida Real
Eliminação de chaves privadas em disco sujeitas a roubo por trojans locais.

## 🚀 Arquitetura e Engenharia Linux
Implementação de engenharia avançada de sistemas Linux para produção, assegurando confiabilidade, resiliência, observabilidade e adesão estrita aos padrões de conformidade corporativa.

## 🛠️ Ferramentas e Utilitários Nativos Utilizados
`ssh-keygen, libfido2, sshd_config`

## 📌 Exemplo de Execução CLI
```bash
ssh-keygen -t ed25519-sk -O resident
```
