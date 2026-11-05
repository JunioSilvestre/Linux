# 02 — Monitor de Pressão do Sistema em Tempo Real com PSI (CPU, Memória, I/O)

## 🏢 Cenário de Produção e Vida Real
Detecção antecipada de saturação de recursos antes que cause travamento perceptível.

## 🚀 Arquitetura e Engenharia Linux
Implementação de engenharia avançada de sistemas Linux para produção, assegurando confiabilidade, resiliência, observabilidade e adesão estrita aos padrões de conformidade corporativa.

## 🛠️ Ferramentas e Utilitários Nativos Utilizados
`cat /proc/pressure/*, awk`

## 📌 Exemplo de Execução CLI
```bash
./psi_monitor.sh --cpu-warn 25 --mem-warn 30
```
