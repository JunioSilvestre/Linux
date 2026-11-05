# 03 — Backup Incremental Atômico com rsync, Hardlinks e Espaço Otimizado

## 🏢 Cenário de Produção e Vida Real
Cópia diária de terabytes parecendo backups completos em segundos através de links físicos.

## 🚀 Arquitetura e Engenharia Linux
Implementação de engenharia avançada de sistemas Linux para produção, assegurando confiabilidade, resiliência, observabilidade e adesão estrita aos padrões de conformidade corporativa.

## 🛠️ Ferramentas e Utilitários Nativos Utilizados
`rsync, cp -al, date`

## 📌 Exemplo de Execução CLI
```bash
./rsync_backup.sh --source /srv --dest /backups/daily
```
