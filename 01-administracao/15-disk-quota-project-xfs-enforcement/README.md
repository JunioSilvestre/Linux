# 15 — Imposição de Project Quotas em Sistemas de Arquivos XFS para Tenants

## 🏢 Cenário de Produção e Vida Real
Isolamento de espaço em disco por projeto/diretório compartilhado entre múltiplos usuários.

## 🚀 Arquitetura e Engenharia Linux
Implementação de engenharia avançada de sistemas Linux para produção, assegurando confiabilidade, resiliência, observabilidade e adesão estrita aos padrões de conformidade corporativa.

## 🛠️ Ferramentas e Utilitários Nativos Utilizados
`xfs_quota, /etc/projects, /etc/projid`

## 📌 Exemplo de Execução CLI
```bash
xfs_quota -x -c 'report -h' /srv
```
