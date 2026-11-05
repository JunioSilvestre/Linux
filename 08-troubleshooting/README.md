# 08-troubleshooting — Troubleshooting Avançado, Diagnóstico e Resolução de Incidentes

Projetos em Bash para análise forense, rastreamento de syscalls com strace, vazamentos de conexões, pânicos de kernel e bloqueios de I/O.

---

## 🏛️ Trilha de Projetos Práticos de Engenharia Linux Nível Sênior (20 Projetos Reais)

| # | Projeto | Título / Foco Técnico | Ferramentas Chave |
|---|---|---|---|
| **01** | [`01-strace-slow-syscall-latency-analyzer/`](./01-strace-slow-syscall-latency-analyzer) | **Rastreamento e Análise de Syscalls Lentas com strace em Processos de Produção** | `strace -T -tt -p, awk, sort` |
| **02** | [`02-hung-task-dmesg-stacktrace-parser/`](./02-hung-task-dmesg-stacktrace-parser) | **Extrator e Analisador de Tarefas Presas em D-State (Uninterruptible Sleep)** | `dmesg, /proc/sys/kernel/hung_task_timeout_secs, ps` |
| **03** | [`03-tcpdump-handshake-drop-investigator/`](./03-tcpdump-handshake-drop-investigator) | **Investigador de Descarte de Pacotes no Three-Way Handshake TCP com tcpdump** | `tcpdump, tshark, awk` |
| **04** | [`04-perf-kernel-lock-contention-profiler/`](./04-perf-kernel-lock-contention-profiler) | **Análise de Disputa de Locks no Kernel (Lock Contention) com perf lock** | `perf lock record, perf lock report` |
| **05** | [`05-high-iowait-blktrace-io-bottleneck/`](./05-high-iowait-blktrace-io-bottleneck) | **Localizador da Causa Raiz de Alto I/O Wait com blktrace e btt** | `blktrace, btt, iostat` |
| **06** | [`06-zombie-parent-ppid-dependency-tracer/`](./06-zombie-parent-ppid-dependency-tracer) | **Rastreador da Árvore de Dependências de Processos Pais Geradores de Zumbis** | `pstree, ps, awk` |
| **07** | [`07-dns-lookup-failure-packet-trace/`](./07-dns-lookup-failure-packet-trace) | **Diagnóstico de Falhas de Resolução DNS com Captura Simultânea de Tráfego de Rede** | `dig, tcpdump, tshark` |
| **08** | [`08-file-descriptor-exhaustion-deep-trace/`](./08-file-descriptor-exhaustion-deep-trace) | **Investigação Forense de Esgotamento de File Descriptors por Processo** | `ls -l /proc/*/fd, lsof, awk` |
| **09** | [`09-oom-killer-score-tuning-investigation/`](./09-oom-killer-score-tuning-investigation) | **Auditoria de Prioridades do OOM-Killer (oom_score_adj) para Proteção de Daemons** | `/proc/[pid]/oom_score, sysctl` |
| **10** | [`10-network-mtu-blackhole-path-detector/`](./10-network-mtu-blackhole-path-detector) | **Detector de MTU Black Hole e Perda de ICMP Fragmentation Needed** | `tracepath, ping -M do, tcpdump` |
| **11** | [`11-ebpf-opensnoop-file-access-tracer/`](./11-ebpf-opensnoop-file-access-tracer) | **Rastreamento de Todos os Arquivos Acessados por um Processo com opensnoop (eBPF)** | `opensnoop, bpftrace` |
| **12** | [`12-memory-leak-valgrind-massif-profiler/`](./12-memory-leak-valgrind-massif-profiler) | **Diagnóstico de Vazamentos de Memória em Binários C/C++ com Valgrind Massif** | `valgrind --tool=massif, ms_print` |
| **13** | [`13-packet-drop-dropwatch-kernel-tracer/`](./13-packet-drop-dropwatch-kernel-tracer) | **Localização Exata da Função do Kernel que está Descartando Pacotes com dropwatch** | `dropwatch, dtrace, bpftool` |
| **14** | [`14-core-dump-gdb-segfault-root-cause/`](./14-core-dump-gdb-segfault-root-cause) | **Análise de Causa Raiz de Segmentation Fault com GDB em Modo Não-Interativo** | `gdb -batch -ex bt, coredumpctl` |
| **15** | [`15-slow-disk-latency-biolatency-ebpf/`](./15-slow-disk-latency-biolatency-ebpf) | **Medição da Latência de Dispositivos de Bloco com biolatency (BCC Tools)** | `biolatency, bcc-tools` |
| **16** | [`16-conntrack-packet-drop-investigator/`](./16-conntrack-packet-drop-investigator) | **Investigação de Descarte de Pacotes na Tabela Conntrack do Netfilter** | `dmesg, conntrack -S, sysctl` |
| **17** | [`17-systemd-boot-blame-chain-analyzer/`](./17-systemd-boot-blame-chain-analyzer) | **Análise e Otimização do Tempo de Inicialização do Servidor com systemd-analyze** | `systemd-analyze blame, critical-chain` |
| **18** | [`18-kernel-soft-lockup-cpu-stuck-tracer/`](./18-kernel-soft-lockup-cpu-stuck-tracer) | **Diagnóstico de Soft Lockup e CPUs Presas em Loops Infinitos de Kernel** | `sysctl, dmesg, /proc/sys/kernel/watchdog` |
| **19** | [`19-network-tcp-retransmissions-rate-meter/`](./19-network-tcp-retransmissions-rate-meter) | **Medidor em Tempo Real da Taxa de Retransmissão de Pacotes TCP com tcpretrans** | `tcpretrans, bcc-tools, ss -ti` |
| **20** | [`20-blackbox-flight-recorder-incident-triage/`](./20-blackbox-flight-recorder-incident-triage) | **Coletor Forense de Evidências em Tempo Real no Momento Exato de um Incidente** | `tar, ss, ps, /proc, dmesg` |
