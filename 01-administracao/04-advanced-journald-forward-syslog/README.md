# 04 — Otimização de Journald com Rate-Limiting, Retenção e Encaminhamento Syslog

## 🏢 Cenário de Produção e Vida Real
Servidores de alta densidade onde logs do journald corrompem o disco ou sofrem descarte por burst.

## 🚀 Arquitetura e Engenharia Linux
Implementação de engenharia avançada de sistemas Linux para produção, assegurando confiabilidade, resiliência, observabilidade e adesão estrita aos padrões de conformidade corporativa.

## 🛠️ Ferramentas e Utilitários Nativos Utilizados
`journald.conf, systemd-journal-remote, logger`

## 📌 Exemplo de Execução CLI
```bash
journalctl --vacuum-size=2G --vacuum-time=30d
```
