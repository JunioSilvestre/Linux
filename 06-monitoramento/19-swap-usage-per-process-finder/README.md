# 19 — Rastreador de Consumo de Memória Swap por Processo Lendo /proc/[pid]/smaps

## 🏢 Cenário de Produção e Vida Real
Identificação exata de quais daemons foram movidos para o swap e estão degradando a máquina.

## 🚀 Arquitetura e Engenharia Linux
Implementação de engenharia avançada de sistemas Linux para produção, assegurando confiabilidade, resiliência, observabilidade e adesão estrita aos padrões de conformidade corporativa.

## 🛠️ Ferramentas e Utilitários Nativos Utilizados
`cat /proc/*/smaps, awk, sort`

## 📌 Exemplo de Execução CLI
```bash
./swap_by_process.sh --top 15
```
