# 04 — Análise de Disputa de Locks no Kernel (Lock Contention) com perf lock

## 🏢 Cenário de Produção e Vida Real
Servidores com dezenas de CPUs apresentando performance horrível por contenção de mutexes do kernel.

## 🚀 Arquitetura e Engenharia Linux
Implementação de engenharia avançada de sistemas Linux para produção, assegurando confiabilidade, resiliência, observabilidade e adesão estrita aos padrões de conformidade corporativa.

## 🛠️ Ferramentas e Utilitários Nativos Utilizados
`perf lock record, perf lock report`

## 📌 Exemplo de Execução CLI
```bash
perf lock record -a -- sleep 10
```
