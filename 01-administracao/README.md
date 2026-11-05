# 01-administracao — Administração de Sistemas Linux Enterprise

Projetos práticos para gestão de processos, ciclo de vida do kernel, systemd profundo, quotas, PAM e gerência de usuários em escala.

---

## 🏛️ Trilha de Projetos Práticos de Engenharia Linux Nível Sênior (20 Projetos Reais)

| # | Projeto | Título / Foco Técnico | Ferramentas Chave |
|---|---|---|---|
| **01** | [`01-systemd-cgroup-resource-slices/`](./01-systemd-cgroup-resource-slices) | **Gestão de Fatias de Recursos (Resource Slices) com cgroups v2 no Systemd** | `systemctl set-property, systemd-cgls, cgroups v2` |
| **02** | [`02-pam-auth-sssd-ldap-integration/`](./02-pam-auth-sssd-ldap-integration) | **Configuração e Auditoria de Módulos PAM com SSSD para Autenticação Centralizada** | `pam-auth-update, sssd, pam_faillock` |
| **03** | [`03-kernel-kpatch-livepatching/`](./03-kernel-kpatch-livepatching) | **Aplicação de Patches de Kernel em Tempo Real sem Reboot com kpatch / Livepatch** | `kpatch, canonical-livepatch, dmesg` |
| **04** | [`04-advanced-journald-forward-syslog/`](./04-advanced-journald-forward-syslog) | **Otimização de Journald com Rate-Limiting, Retenção e Encaminhamento Syslog** | `journald.conf, systemd-journal-remote, logger` |
| **05** | [`05-user-lifecycle-rbac-sudoers-ldap/`](./05-user-lifecycle-rbac-sudoers-ldap) | **Automação de Ciclo de Vida de Usuários com RBAC via Sudoers e Grupos LDAP** | `visudo, sudoers.d, id, getent` |
| **06** | [`06-systemd-socket-activation-services/`](./06-systemd-socket-activation-services) | **Implementação de Socket Activation do Systemd para Serviços sob Demanda** | `systemd.socket, systemd.service, ss` |
| **07** | [`07-unattended-upgrades-kernel-freeze/`](./07-unattended-upgrades-kernel-freeze) | **Orquestração de Unattended-Upgrades com Congelamento (Apt-Mark Hold) de Kernel** | `unattended-upgrades, apt-mark, needrestart` |
| **08** | [`08-posix-shared-memory-dev-shm-audit/`](./08-posix-shared-memory-dev-shm-audit) | **Auditoria e Dimensionamento Seguro de Memória Compartilhada POSIX (/dev/shm)** | `mount, df, fstab, sysctl` |
| **09** | [`09-coredump-compression-systemd-coredump/`](./09-coredump-compression-systemd-coredump) | **Gerenciamento e Compressão ZSTD de Core Dumps com systemd-coredump** | `coredump.conf, coredumpctl, gdb` |
| **10** | [`10-chroot-jail-sftp-only-service/`](./10-chroot-jail-sftp-only-service) | **Criação de Jail Chroot Segura para Acessos SFTP com Isolamento Estrito** | `sshd_config, chroot, setfacl` |
| **11** | [`11-systemd-inhibitor-locks-backup/`](./11-systemd-inhibitor-locks-backup) | **Bloqueios de Inibição do Systemd (systemd-inhibit) durante Backups Críticos** | `systemd-inhibit, loginctl` |
| **12** | [`12-locale-keyboard-console-timezone/`](./12-locale-keyboard-console-timezone) | **Padronização Imutável de Timezone, Locales e Console em Frotas Linux** | `timedatectl, localectl, dpkg-reconfigure` |
| **13** | [`13-multi-seat-display-seatd-manager/`](./13-multi-seat-display-seatd-manager) | **Gerenciamento de Assentos (Multi-Seat) e Acesso a Dispositivos com logind** | `loginctl, seatd, systemd-logind` |
| **14** | [`14-audit-immutable-binaries-chattr/`](./14-audit-immutable-binaries-chattr) | **Travamento e Garantia de Imutabilidade de Binários Críticos com chattr (+i)** | `chattr, lsattr, e2fsprogs` |
| **15** | [`15-disk-quota-project-xfs-enforcement/`](./15-disk-quota-project-xfs-enforcement) | **Imposição de Project Quotas em Sistemas de Arquivos XFS para Tenants** | `xfs_quota, /etc/projects, /etc/projid` |
| **16** | [`16-grub2-recovery-fallback-kernel/`](./16-grub2-recovery-fallback-kernel) | **Automação de Fallback Seguro no GRUB2 para Inicialização em Caso de Falha de Kernel** | `grub-reboot, grubby, efibootmgr` |
| **17** | [`17-zram-compressed-swap-allocator/`](./17-zram-compressed-swap-allocator) | **Implementação de Swap Comprimido em Memória RAM com ZRAM para Alta Performance** | `zramctl, mkswap, swapon` |
| **18** | [`18-hugepages-transparent-tuning-db/`](./18-hugepages-transparent-tuning-db) | **Configuração e Otimização de Transparent Hugepages (THP) para Bancos de Dados** | `sysfs, /sys/kernel/mm/transparent_hugepage` |
| **19** | [`19-ephemeral-port-range-fin-tuning/`](./19-ephemeral-port-range-fin-tuning) | **Ajuste Fino de Portas Efêmeras e Timeouts TCP FIN em Servidores Web** | `sysctl, /proc/sys/net/ipv4` |
| **20** | [`20-decommission-safe-system-zeroing/`](./20-decommission-safe-system-zeroing) | **Procedimento de Descomissionamento Seguro de Servidor com Sanitização NIST** | `shred, blkdiscard, wipefs` |
