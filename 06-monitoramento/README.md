# 06-monitoramento — Monitoramento e Coleta de Telemetria no Host

Métricas de recursos de hardware, rotação e agregação de logs do kernel e serviços.

## 📂 Subáreas
- [`metricas/`](./metricas) — **Stack:** `vmstat, iostat, sar, mpstat, free` — Coleta contínua de estatísticas de CPU, memória, swap e throughput de I/O de disco.
- [`logs/`](./logs) — **Stack:** `journalctl, rsyslog, logrotate` — Retenção, compactação e envio centralizado de logs do sistema operacional.
- [`diagnostico/`](./diagnostico) — **Stack:** `dmesg, /proc, /sys filesystem inspection` — Extração de parâmetros em tempo de execução via sistema de arquivos virtual.

## 📌 Guia de Execução & Padrões
- Todas as implementações desta pasta seguem os padrões de produção estabelecidos para Linux.
- Consulte os READMEs de cada subárea para detalhes sobre ferramentas e boas práticas.
