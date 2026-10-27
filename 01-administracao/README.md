# 01-administracao — Administração de Sistemas e Gerenciamento do Host

Gerenciamento de contas de usuários, grupos, permissões POSIX/ACLs, pacotes e Systemd.

## 📂 Subáreas
- [`usuarios-grupos/`](./usuarios-grupos) — **Stack:** `useradd, usermod, groupadd, chage, /etc/passwd` — Criação, auditoria e controle de ciclo de vida de identidades e grupos locais.
- [`permissoes-acl/`](./permissoes-acl) — **Stack:** `chmod, chown, setfacl, getfacl, umask` — Modelos de controle de acesso discricionário (DAC) e listas de controle de acesso (ACL).
- [`pacotes/`](./pacotes) — **Stack:** `apt, dpkg, yum, dnf, rpm, repositórios` — Gerenciamento de pacotes, compilação, repositórios privados e atualizações de segurança.
- [`systemd/`](./systemd) — **Stack:** `systemctl, journalctl, systemd-analyze, unit files` — Arquitetura de init, gerenciamento de targets, timers, sockets e serviços customizados.
- [`processos-servicos/`](./processos-servicos) — **Stack:** `ps, top, htop, nice, renice, kill, signals` — Controle de execução, prioridades de agendamento CPU e sinais de terminação.

## 📌 Guia de Execução & Padrões
- Todas as implementações desta pasta seguem os padrões de produção estabelecidos para Linux.
- Consulte os READMEs de cada subárea para detalhes sobre ferramentas e boas práticas.
