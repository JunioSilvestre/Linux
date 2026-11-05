# 03 — Profiler Contínuo de Latência de I/O de Disco com iostat e Alerta de Gargalo

## 🏢 Cenário de Produção e Vida Real
Identificação de dispositivos de bloco operando com tempo de espera await elevado.

## 🚀 Arquitetura e Engenharia Linux
Implementação de engenharia avançada de sistemas Linux para produção, assegurando confiabilidade, resiliência, observabilidade e adesão estrita aos padrões de conformidade corporativa.

## 🛠️ Ferramentas e Utilitários Nativos Utilizados
`iostat, awk, mailx`

## 📌 Exemplo de Execução CLI
```bash
./disk_io_alert.sh --await-threshold 20
```
