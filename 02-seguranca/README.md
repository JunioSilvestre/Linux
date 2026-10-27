# 02-seguranca — Segurança, Hardening e Auditoria

Firewall de kernel, benchmarks de conformidade CIS, auditoria do sistema e controle de acesso obrigatório (MAC).

## 📂 Subáreas
- [`firewall-iptables-nftables/`](./firewall-iptables-nftables) — **Stack:** `iptables, nftables, ufw, conntrack` — Filtragem de pacotes em nível de kernel, regras de NAT e mitigação de scans.
- [`auditoria/`](./auditoria) — **Stack:** `auditd, aureport, ausearch, audit.rules` — Auditoria contínua de syscalls, acessos a arquivos críticos e login no sistema.
- [`ssh-hardening/`](./ssh-hardening) — **Stack:** `sshd_config, chaves Ed25519, banners, fail2ban` — Políticas restritivas de acesso remoto seguro e proteção contra ataques de dicionário.
- [`selinux-apparmor/`](./selinux-apparmor) — **Stack:** `apparmor_status, aa-enforce, sestatus, semanage` — Implementação de MAC para isolar daemons e conter elevações de privilégio.

## 📌 Guia de Execução & Padrões
- Todas as implementações desta pasta seguem os padrões de produção estabelecidos para Linux.
- Consulte os READMEs de cada subárea para detalhes sobre ferramentas e boas práticas.
