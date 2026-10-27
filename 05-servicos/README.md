# 05-servicos — Serviços Essenciais de Infraestrutura

Instalação, configuração de alta performance e operação dos principais daemons de rede Linux.

## 📂 Subáreas
- [`nginx-apache/`](./nginx-apache) — **Stack:** `nginx, apache2, reverse proxy, ssl termination` — Servidores HTTP/HTTPS de alta performance e balanceamento de carga.
- [`openssh/`](./openssh) — **Stack:** `openssh-server, sshd_config, tunnels, sftp` — Operação corporativa de SSH com segregação de usuários e restrições de chaves.
- [`dns/`](./dns) — **Stack:** `bind9, named, dnsmasq` — Servidores autoritativos de zona interna e servidores de encaminhamento DNS.
- [`chrony/`](./chrony) — **Stack:** `chrony, chronyc, ntp.conf, sincronização de tempo` — Sincronização precisa de relógio entre servidores via protocolo NTP.

## 📌 Guia de Execução & Padrões
- Todas as implementações desta pasta seguem os padrões de produção estabelecidos para Linux.
- Consulte os READMEs de cada subárea para detalhes sobre ferramentas e boas práticas.
