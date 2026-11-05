# 06-monitoramento — Monitoramento de Performance e Métricas de Infraestrutura

Projetos em Bash para coleta de métricas de SO, telemetria de CPU/RAM/Disco, exportadores Prometheus, análise de PSI e logs de saturação.

---

## 🏛️ Trilha de Projetos Práticos de Engenharia Linux Nível Sênior (20 Projetos Reais)

| # | Projeto | Título / Foco Técnico | Ferramentas Chave |
|---|---|---|---|
| **01** | [`01-node-exporter-textfile-custom-metrics/`](./01-node-exporter-textfile-custom-metrics) | **Coletor de Métricas de Negócio e Infraestrutura para Prometheus Node Exporter** | `prom-tool, awk, logger` |
| **02** | [`02-psi-pressure-stall-information-monitor/`](./02-psi-pressure-stall-information-monitor) | **Monitor de Pressão do Sistema em Tempo Real com PSI (CPU, Memória, I/O)** | `cat /proc/pressure/*, awk` |
| **03** | [`03-iostat-disk-latency-profiler-alert/`](./03-iostat-disk-latency-profiler-alert) | **Profiler Contínuo de Latência de I/O de Disco com iostat e Alerta de Gargalo** | `iostat, awk, mailx` |
| **04** | [`04-vmstat-memory-swap-pagein-analyzer/`](./04-vmstat-memory-swap-pagein-analyzer) | **Analisador de Paginação e Taxa de Troca de Memória com vmstat** | `vmstat, awk, sort` |
| **05** | [`05-ss-tcp-socket-buffer-backlog-monitor/`](./05-ss-tcp-socket-buffer-backlog-monitor) | **Monitor de Fila de Backlog e Saturação de Buffers de Sockets TCP com ss** | `ss, sysctl, awk` |
| **06** | [`06-mpstat-per-core-cpu-imbalance-finder/`](./06-mpstat-per-core-cpu-imbalance-finder) | **Detector de Desbalanceamento de Carga entre Cores de CPU com mpstat** | `mpstat, /proc/interrupts, awk` |
| **07** | [`07-sar-sysstat-historical-capacity-report/`](./07-sar-sysstat-historical-capacity-report) | **Gerador Automatizado de Relatórios de Capacidade Histórica com sar (sysstat)** | `sar, sadf, gnuplot` |
| **08** | [`08-oom-kill-event-extractor-journalctl/`](./08-oom-kill-event-extractor-journalctl) | **Extrator de Eventos de OOM Killer com Stack Trace Completo do Kernel** | `journalctl, dmesg, awk` |
| **09** | [`09-smartd-automated-disk-predictive-alert/`](./09-smartd-automated-disk-predictive-alert) | **Configurador e Notificador de Diagnóstico Preditivo SMART com smartd** | `smartd.conf, smartctl, logger` |
| **10** | [`10-network-interface-errors-drops-watchdog/`](./10-network-interface-errors-drops-watchdog) | **Watchdog de Pacotes Descartados e Erros de CRC em Interfaces de Rede** | `ip -s link, ethtool, awk` |
| **11** | [`11-conntrack-table-saturation-alert/`](./11-conntrack-table-saturation-alert) | **Monitor e Ajustador Dinâmico da Tabela de Rastreamento de Conexões (conntrack)** | `conntrack, sysctl, awk` |
| **12** | [`12-linux-load-average-runqueue-analyzer/`](./12-linux-load-average-runqueue-analyzer) | **Analisador de Filas de Processos em Execução (Runqueue) e Carga de Sistema** | `cat /proc/loadavg, ps, awk` |
| **13** | [`13-perf-top-kernel-cpu-profiling/`](./13-perf-top-kernel-cpu-profiling) | **Profiler de Funções do Kernel e Código de Usuário com perf top em Produção** | `perf, perf-report, awk` |
| **14** | [`14-bpftrace-disk-latency-histogram/`](./14-bpftrace-disk-latency-histogram) | **Histograma de Latência de Bloco em Tempo Real com bpftrace (eBPF)** | `bpftrace, eBPF` |
| **15** | [`15-file-descriptor-leak-detector-lsof/`](./15-file-descriptor-leak-detector-lsof) | **Detector de Vazamentos de Descritores de Arquivos e Sockets Zumbis com lsof** | `lsof, /proc/sys/fs/file-nr, sort` |
| **16** | [`16-sensor-temperature-fan-speed-monitor/`](./16-sensor-temperature-fan-speed-monitor) | **Monitor de Sensores de Temperatura, Ventoinhas e Fontes com lm-sensors** | `sensors, ipmitool, logger` |
| **17** | [`17-systemd-service-restarts-counter/`](./17-systemd-service-restarts-counter) | **Contador e Analisador de Reinicializações Frequentes de Serviços do Systemd** | `systemctl, journalctl, awk` |
| **18** | [`18-dns-resolution-latency-synthetic-probe/`](./18-dns-resolution-latency-synthetic-probe) | **Sonda Sintética de Latência de Resolução DNS com dig e Estatísticas** | `dig, awk, bc` |
| **19** | [`19-swap-usage-per-process-finder/`](./19-swap-usage-per-process-finder) | **Rastreador de Consumo de Memória Swap por Processo Lendo /proc/[pid]/smaps** | `cat /proc/*/smaps, awk, sort` |
| **20** | [`20-synthetic-http-end-to-end-blackbox/`](./20-synthetic-http-end-to-end-blackbox) | **Sonda Sintética de Transações HTTP com Medição de Tempo e DNS/TLS com curl** | `curl, jq, date` |
