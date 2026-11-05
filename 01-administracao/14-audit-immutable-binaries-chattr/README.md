# 14 — Travamento e Garantia de Imutabilidade de Binários Críticos com chattr (+i)

## 🏢 Cenário de Produção e Vida Real
Proteção de arquivos essenciais (/bin/login, /etc/resolv.conf) contra alteração por rootkits.

## 🚀 Arquitetura e Engenharia Linux
Implementação de engenharia avançada de sistemas Linux para produção, assegurando confiabilidade, resiliência, observabilidade e adesão estrita aos padrões de conformidade corporativa.

## 🛠️ Ferramentas e Utilitários Nativos Utilizados
`chattr, lsattr, e2fsprogs`

## 📌 Exemplo de Execução CLI
```bash
chattr +i /etc/passwd /etc/shadow
```
