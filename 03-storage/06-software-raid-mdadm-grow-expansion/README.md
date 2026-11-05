# 06 — Expansão Online de Volume RAID 5 para RAID 6 com mdadm sem Perda de Dados

## 🏢 Cenário de Produção e Vida Real
Migração de nível de tolerância a falhas em arrays corporativos em produção.

## 🚀 Arquitetura e Engenharia Linux
Implementação de engenharia avançada de sistemas Linux para produção, assegurando confiabilidade, resiliência, observabilidade e adesão estrita aos padrões de conformidade corporativa.

## 🛠️ Ferramentas e Utilitários Nativos Utilizados
`mdadm --grow, cat /proc/mdstat`

## 📌 Exemplo de Execução CLI
```bash
mdadm --grow /dev/md0 --level=6 --raid-devices=5
```
