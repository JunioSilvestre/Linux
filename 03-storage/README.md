# 03-storage — Storage, Sistemas de Arquivos, LVM e Software RAID

Projetos em Bash para provisionamento de LVM, expansão a quente, ZFS on Linux, Btrfs, multipath SAN iSCSI e reparo de volumes.

---

## 🏛️ Trilha de Projetos Práticos de Engenharia Linux Nível Sênior (20 Projetos Reais)

| # | Projeto | Título / Foco Técnico | Ferramentas Chave |
|---|---|---|---|
| **01** | [`01-lvm-snapshot-merge-rollback/`](./01-lvm-snapshot-merge-rollback) | **Snapshots LVM Consistentes com Reversão Atômica (Snapshot Merge)** | `lvcreate, lvconvert --merge, lvs` |
| **02** | [`02-zfs-raidz2-scrub-auto-trim/`](./02-zfs-raidz2-scrub-auto-trim) | **Agendador e Auditor de Scrub e TRIM em Pools ZFS de Alta Densidade** | `zpool scrub, zpool trim, zpool status` |
| **03** | [`03-btrfs-subvolume-snapper-timeline/`](./03-btrfs-subvolume-snapper-timeline) | **Gestão de Snapshots Btrfs em Linha do Tempo com Snapper e Rollback** | `snapper, btrfs subvolume, btrfs filesystem` |
| **04** | [`04-iscsi-multipath-failover-san/`](./04-iscsi-multipath-failover-san) | **Configuração de SAN iSCSI com DM-Multipath e Redundância Ativa** | `iscsiadm, multipath, multipathd` |
| **05** | [`05-nfs-v42-sec-krb5p-kerberos/`](./05-nfs-v42-sec-krb5p-kerberos) | **Provisionamento de NFS v4.2 com Segurança e Criptografia Total via Kerberos (krb5p)** | `exportfs, rpc.gssd, krb5.conf` |
| **06** | [`06-software-raid-mdadm-grow-expansion/`](./06-software-raid-mdadm-grow-expansion) | **Expansão Online de Volume RAID 5 para RAID 6 com mdadm sem Perda de Dados** | `mdadm --grow, cat /proc/mdstat` |
| **07** | [`07-nvme-of-rdma-storage-fabrics/`](./07-nvme-of-rdma-storage-fabrics) | **Configuração de Storage NVMe-over-Fabrics (NVMe-oF) via RDMA / TCP** | `nvme-cli, modprobe nvme-rdma` |
| **08** | [`08-stratis-storage-daemon-provisioning/`](./08-stratis-storage-daemon-provisioning) | **Gerenciamento Simplificado de Storage em Camadas com Stratis Daemon** | `stratis, stratis-cli, systemctl` |
| **09** | [`09-xfs-online-grow-filesystem-expansion/`](./09-xfs-online-grow-filesystem-expansion) | **Expansão a Quente (Online) de Sistemas de Arquivos XFS sem Desmontagem** | `xfs_growfs, lvextend, df` |
| **10** | [`10-ext4-badblocks-recovery-e2fsck/`](./10-ext4-badblocks-recovery-e2fsck) | **Varredura Não Destrutiva de Setores Defeituosos com badblocks e e2fsck** | `badblocks, e2fsck, dumpe2fs` |
| **11** | [`11-autofs-dynamic-mount-on-demand/`](./11-autofs-dynamic-mount-on-demand) | **Montagem Dinâmica de Volumes de Rede sob Demanda com AutoFS** | `autofs, auto.master, systemctl` |
| **12** | [`12-ceph-rbd-kernel-module-mapping/`](./12-ceph-rbd-kernel-module-mapping) | **Mapeamento Direto no Kernel de Volumes Ceph RBD com Cache Writeback** | `rbd, krbd, lsblk` |
| **13** | [`13-loop-device-sparse-image-creator/`](./13-loop-device-sparse-image-creator) | **Criação de Dispositivos Loopback Esparsos e Criptografados para Testes** | `losetup, truncate, mkfs` |
| **14** | [`14-smartmontools-automated-disk-replacement/`](./14-smartmontools-automated-disk-replacement) | **Detecção Antecipada de Falhas SMART e Notificação para Troca Preventiva** | `smartctl, smartd, mailx` |
| **15** | [`15-glusterfs-georeplication-disaster-recovery/`](./15-glusterfs-georeplication-disaster-recovery) | **Replicação Geográfica Assíncrona de Dados com GlusterFS Geo-Replication** | `gluster volume geo-replication, rsync` |
| **16** | [`16-fstrim-batch-scheduler-performance/`](./16-fstrim-batch-scheduler-performance) | **Agendador Otimizado de Descarte TRIM com fstrim para Frotas de SSDs** | `fstrim, systemd-timer, lsblk` |
| **17** | [`17-quota-enforcement-grace-period-manager/`](./17-quota-enforcement-grace-period-manager) | **Auditoria de Período de Graça e Limites Rígidos de Cotas de Usuário** | `repquota, edquota, warnquota` |
| **18** | [`18-storage-benchmark-fio-iops-latency/`](./18-storage-benchmark-fio-iops-latency) | **Bateria Automatizada de Testes de Stress de Storage com FIO e Relatório** | `fio, jq, awk` |
| **19** | [`19-drbd-high-availability-block-replication/`](./19-drbd-high-availability-block-replication) | **Replicação Síncrona de Blocos em Nível de Rede com DRBD para Alta Disponibilidade** | `drbdadm, drbdsetup, systemctl` |
| **20** | [`20-luks-wipe-header-secure-erasure/`](./20-luks-wipe-header-secure-erasure) | **Destruição Criptográfica Instantânea (Crypto-Shredding) de Cabeçalho LUKS** | `cryptsetup, shred, dd` |
