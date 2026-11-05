# 03 — Gestão de Snapshots Btrfs em Linha do Tempo com Snapper e Rollback

## 🏢 Cenário de Produção e Vida Real
Recuperação de estado do sistema de arquivos para qualquer hora dos últimos 30 dias.

## 🚀 Arquitetura e Engenharia Linux
Implementação de engenharia avançada de sistemas Linux para produção, assegurando confiabilidade, resiliência, observabilidade e adesão estrita aos padrões de conformidade corporativa.

## 🛠️ Ferramentas e Utilitários Nativos Utilizados
`snapper, btrfs subvolume, btrfs filesystem`

## 📌 Exemplo de Execução CLI
```bash
snapper -c root create -d 'Pre-Update'
```
