# 03-storage — Storage, Particionamento e Sistemas de Arquivos

Gerenciamento de discos, volumes lógicos (LVM), RAID por software e compartilhamento de arquivos de rede.

## 📂 Subáreas
- [`particoes-lvm/`](./particoes-lvm) — **Stack:** `fdisk, parted, pvcreate, vgcreate, lvcreate` — Alocação dinâmica de armazenamento, snapshots de volumes e redimensionamento online.
- [`filesystems/`](./filesystems) — **Stack:** `ext4, xfs, btrfs, zfs, mkfs, tune2fs` — Criação, otimização de parâmetros de montagem, integridade (fsck) e tunning.
- [`raid/`](./raid) — **Stack:** `mdadm, /proc/mdstat, monitoramento de arrays` — Implementação de redundância e performance com RAID 0, 1, 5, 10 por software.
- [`nfs-samba/`](./nfs-samba) — **Stack:** `nfs-kernel-server, smb.conf, mount, exportfs` — Compartilhamento de arquivos entre sistemas Linux e heterogêneos na rede.

## 📌 Guia de Execução & Padrões
- Todas as implementações desta pasta seguem os padrões de produção estabelecidos para Linux.
- Consulte os READMEs de cada subárea para detalhes sobre ferramentas e boas práticas.
