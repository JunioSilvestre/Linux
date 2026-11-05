# 09 — Auditoria de Prioridades do OOM-Killer (oom_score_adj) para Proteção de Daemons

## 🏢 Cenário de Produção e Vida Real
Evitar que o kernel mate o banco de dados principal ao invés de matar processos de relatórios pesados.

## 🚀 Arquitetura e Engenharia Linux
Implementação de engenharia avançada de sistemas Linux para produção, assegurando confiabilidade, resiliência, observabilidade e adesão estrita aos padrões de conformidade corporativa.

## 🛠️ Ferramentas e Utilitários Nativos Utilizados
`/proc/[pid]/oom_score, sysctl`

## 📌 Exemplo de Execução CLI
```bash
echo -1000 > /proc/$DB_PID/oom_score_adj
```
