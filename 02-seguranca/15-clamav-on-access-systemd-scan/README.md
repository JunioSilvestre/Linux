# 15 — Varredura Antivírus em Tempo Real com ClamAV On-Access Scan e Fanotify

## 🏢 Cenário de Produção e Vida Real
Inspeção imediata de qualquer arquivo gravado no diretório de uploads do servidor web.

## 🚀 Arquitetura e Engenharia Linux
Implementação de engenharia avançada de sistemas Linux para produção, assegurando confiabilidade, resiliência, observabilidade e adesão estrita aos padrões de conformidade corporativa.

## 🛠️ Ferramentas e Utilitários Nativos Utilizados
`clamd, clamonacc, fanotify`

## 📌 Exemplo de Execução CLI
```bash
clamonacc --foreground --log=/var/log/clamonacc.log
```
