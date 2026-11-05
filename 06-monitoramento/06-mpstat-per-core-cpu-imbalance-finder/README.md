# 06 — Detector de Desbalanceamento de Carga entre Cores de CPU com mpstat

## 🏢 Cenário de Produção e Vida Real
Identificação de interrupções de hardware (IRQs) concentradas em um único núcleo da CPU.

## 🚀 Arquitetura e Engenharia Linux
Implementação de engenharia avançada de sistemas Linux para produção, assegurando confiabilidade, resiliência, observabilidade e adesão estrita aos padrões de conformidade corporativa.

## 🛠️ Ferramentas e Utilitários Nativos Utilizados
`mpstat, /proc/interrupts, awk`

## 📌 Exemplo de Execução CLI
```bash
./cpu_imbalance_check.sh --max-skew 40
```
