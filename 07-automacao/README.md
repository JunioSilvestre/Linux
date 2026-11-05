# 07-automacao — Automação Operacional e Engenharia de Scripts Linux

Projetos em Bash para provisionamento autônomo, sincronização rsync com locks, rotação de chaves SSH, manutenção periódica e idempotência.

---

## 🏛️ Trilha de Projetos Práticos de Engenharia Linux Nível Sênior (20 Projetos Reais)

| # | Projeto | Título / Foco Técnico | Ferramentas Chave |
|---|---|---|---|
| **01** | [`01-ansible-pull-autonomous-node-config/`](./01-ansible-pull-autonomous-node-config) | **Configuração Autônoma de Nós Linux com Ansible-Pull e Repositório Git Central** | `ansible-pull, git, systemd-timer` |
| **02** | [`02-cloud-init-baremetal-custom-templating/`](./02-cloud-init-baremetal-custom-templating) | **Gerador Dinâmico de Manifestos cloud-init para Provisionamento Bare-Metal e VMs** | `cloud-init, jinja2, yq` |
| **03** | [`03-rsync-atomic-incremental-backup-hardlinks/`](./03-rsync-atomic-incremental-backup-hardlinks) | **Backup Incremental Atômico com rsync, Hardlinks e Espaço Otimizado** | `rsync, cp -al, date` |
| **04** | [`04-automated-ssh-key-rotation-agent/`](./04-automated-ssh-key-rotation-agent) | **Agente Automatizado de Rotação Periódica de Chaves SSH com Teste de Conexão** | `ssh-keygen, ssh-copy-id, ssh` |
| **05** | [`05-logrotate-custom-compression-pipeline/`](./05-logrotate-custom-compression-pipeline) | **Pipeline Customizado de Rotação e Compressão ZSTD de Logs de Alta Vazão** | `logrotate, zstd, systemctl` |
| **06** | [`06-systemd-timer-declarative-scheduler/`](./06-systemd-timer-declarative-scheduler) | **Gerenciador Declarativo de Agendamentos com Systemd Timers e Logs no Journal** | `systemctl, systemd-analyze verify` |
| **07** | [`07-dynamic-motd-system-dashboard/`](./07-dynamic-motd-system-dashboard) | **Painel Dinâmico de Boas-Vindas no Terminal (MOTD) com Status de Saúde do Nó** | `update-motd, figlet, bash` |
| **08** | [`08-automated-certificate-renewal-vault/`](./08-automated-certificate-renewal-vault) | **Renovação Automatizada de Certificados Digitais Internos via HashiCorp Vault** | `vault, openssl, systemctl` |
| **09** | [`09-unattended-package-cache-cleaner/`](./09-unattended-package-cache-cleaner) | **Limpador Inteligente de Caches de Pacotes (APT/DNF) e Imagens Órfãs** | `apt-get clean, dnf clean, find` |
| **10** | [`10-multi-server-parallel-command-execution/`](./10-multi-server-parallel-command-execution) | **Executor Paralelo de Comandos em Frotas de Servidores via SSH com pdsh/xargs** | `pdsh, xargs -P, ssh` |
| **11** | [`11-bare-metal-firmware-update-fwupd/`](./11-bare-metal-firmware-update-fwupd) | **Atualização Automatizada de Firmware de Servidores e Controladoras com fwupd** | `fwupdmgr, systemctl` |
| **12** | [`12-automated-chroot-maintenance-rescue/`](./12-automated-chroot-maintenance-rescue) | **Script de Montagem Automática de Ambientes Chroot de Recuperação de Sistema** | `mount --bind, chroot, grub-install` |
| **13** | [`13-network-failover-automated-healthcheck/`](./13-network-failover-automated-healthcheck) | **Comutador Automático de Interfaces de Rede por Detecção de Falha de Rota** | `ip route, ping, logger` |
| **14** | [`14-zfs-snapshot-replication-remote-sync/`](./14-zfs-snapshot-replication-remote-sync) | **Replicador Automatizado de Snapshots ZFS para Servidor Remoto via SSH** | `zfs send, zfs recv, mbuffer` |
| **15** | [`15-ephemeral-scratchpad-tmpfs-allocator/`](./15-ephemeral-scratchpad-tmpfs-allocator) | **Alocador de Espaços Temporários Efêmeros em Memória (tmpfs) com Auto-Destruição** | `mount -t tmpfs, mktemp, rm` |
| **16** | [`16-dynamic-sudoers-grant-temporary-access/`](./16-dynamic-sudoers-grant-temporary-access) | **Concessão Temporária de Acesso Administrativo com Expiração Automática** | `at, visudo, logger` |
| **17** | [`17-automated-iptables-state-backup-git/`](./17-automated-iptables-state-backup-git) | **Versionamento e Backup Automatizado de Regras de Firewall em Repositório Git** | `iptables-save, nft list ruleset, git` |
| **18** | [`18-kernel-dump-kdump-automated-collector/`](./18-kernel-dump-kdump-automated-collector) | **Configurador e Testador de Crash Dump de Kernel (kdump) com Kdumpctl** | `kdumpctl, crash, makedumpfile` |
| **19** | [`19-automated-container-storage-garbage-collection/`](./19-automated-container-storage-garbage-collection) | **Coletor de Lixo e Higienização de Storage de Runtimes de Containers (crictl/docker)** | `crictl rmi --prune, docker system prune` |
| **20** | [`20-disaster-recovery-baremetal-restore-iso/`](./20-disaster-recovery-baremetal-restore-iso) | **Gerador Automatizado de Imagens ISO de Recuperação Bare-Metal (ReaR - Relax-and-Recover)** | `rear, mkrescue, nfs` |
