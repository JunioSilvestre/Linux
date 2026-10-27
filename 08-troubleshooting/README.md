# 08-troubleshooting — Guia de Resolução de Problemas (Troubleshooting)

Metodologia sistemática de diagnóstico para contenção de incidentes de infraestrutura.

## 📂 Subáreas
- [`cpu-memoria/`](./cpu-memoria) — **Stack:** `OOM killer, load average, htop, perf` — Identificação de gargalos de processamento, vazamento de memória e processos zumbis.
- [`disco/`](./disco) — **Stack:** `df (inodes vs blocos), badblocks, fsck, iotop` — Resolução de esgotamento de inodes, lentidão de leitura/escrita e corrupção de partição.
- [`rede/`](./rede) — **Stack:** `netstat/ss, tc, drops de pacotes, DNS timeout` — Diagnóstico de falhas de conectividade, firewall bloqueando tráfego e latência.
- [`boot-systemd/`](./boot-systemd) — **Stack:** `rescue mode, initramfs, journalctl -xb` — Recuperação de falhas de inicialização do kernel, GRUB e dependências de serviços.

## 📌 Guia de Execução & Padrões
- Todas as implementações desta pasta seguem os padrões de produção estabelecidos para Linux.
- Consulte os READMEs de cada subárea para detalhes sobre ferramentas e boas práticas.
