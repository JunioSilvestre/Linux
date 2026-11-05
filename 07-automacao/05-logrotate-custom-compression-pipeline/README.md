# 05 — Pipeline Customizado de Rotação e Compressão ZSTD de Logs de Alta Vazão

## 🏢 Cenário de Produção e Vida Real
Substituição do gzip tradicional por zstandard no logrotate para reduzir consumo de CPU.

## 🚀 Arquitetura e Engenharia Linux
Implementação de engenharia avançada de sistemas Linux para produção, assegurando confiabilidade, resiliência, observabilidade e adesão estrita aos padrões de conformidade corporativa.

## 🛠️ Ferramentas e Utilitários Nativos Utilizados
`logrotate, zstd, systemctl`

## 📌 Exemplo de Execução CLI
```bash
logrotate -f /etc/logrotate.d/custom-apps
```
