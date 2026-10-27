# Disk Partitioning, Filesystems, LVM, and Mounts

**Level:** Intermediate
**Scope:** Cross-Distribution
**Prerequisites:** [Filesystem Hierarchy](../../../Foundations/Cross-Distribution/Filesystem/README.md)

## Purpose

Manage physical storage: partition disks, create and mount filesystems, configure persistent mounts, and use LVM for flexible storage management.

> **SAFETY:** All examples in this guide use loopback devices or assume a dedicated test disk. Never run destructive storage commands against a disk containing data you cannot afford to lose. Replace `/dev/sdX` with the actual device for your environment.

## Identifying Storage Devices

```bash
# List block devices
lsblk
lsblk -f           # include filesystem type and UUID
lsblk -o NAME,SIZE,TYPE,FSTYPE,MOUNTPOINT

# List disks with partition info
fdisk -l
fdisk -l /dev/sdb   # specific disk

# Show disk hardware details
hdparm -i /dev/sda

# Check SMART status
sudo smartctl -a /dev/sda   # requires smartmontools
```

## Partitioning with fdisk (MBR)

```bash
# Interactive partitioning (MBR/DOS)
sudo fdisk /dev/sdb
# Commands inside fdisk:
# n  — new partition
# d  — delete partition
# p  — print partition table
# w  — write and exit
# q  — quit without saving
# m  — help
```

## Partitioning with gdisk (GPT)

```bash
# GPT partitioning (required for disks >2TB or UEFI)
sudo gdisk /dev/sdb
# Same interactive interface as fdisk
# n  — new partition
# p  — print
# w  — write and exit
```

## Partitioning with parted

```bash
# Non-interactive, scriptable
sudo parted /dev/sdb mklabel gpt
sudo parted /dev/sdb mkpart primary ext4 1MiB 10GiB
sudo parted /dev/sdb print
```

## Creating Filesystems

```bash
# ext4
sudo mkfs.ext4 /dev/sdb1
sudo mkfs.ext4 -L data-volume /dev/sdb1   # set label

# XFS (default on RHEL)
sudo mkfs.xfs /dev/sdb1
sudo mkfs.xfs -L data-volume /dev/sdb1

# Check before formatting (verify device path!)
lsblk /dev/sdb1
```

## Mounting Filesystems

```bash
# Create mount point
sudo mkdir -p /mnt/data

# Mount (temporary, not persistent)
sudo mount /dev/sdb1 /mnt/data
sudo mount -t xfs /dev/sdb1 /mnt/data   # specify type

# List all mounted filesystems
mount
mount | grep /mnt
findmnt
findmnt --real

# Unmount
sudo umount /mnt/data
sudo umount /dev/sdb1   # by device

# Check if mount point is in use before unmounting
lsof /mnt/data
fuser -m /mnt/data
```

## Persistent Mounts: /etc/fstab

```bash
# IMPORTANT: always backup before editing
sudo cp /etc/fstab /etc/fstab.bak

# Get the UUID (preferred over device name which can change)
blkid /dev/sdb1
# /dev/sdb1: UUID="a1b2c3d4-..." TYPE="ext4"
```

Add to `/etc/fstab`:

```
# <device/UUID>                            <mountpoint>  <type>  <options>  <dump>  <pass>
UUID=a1b2c3d4-e5f6-7890-abcd-ef1234567890  /mnt/data     ext4    defaults   0       2
```

```bash
# Validate without rebooting
sudo mount -a   # mount everything in fstab that isn't mounted

# If this command fails, the system may not boot properly
# Fix the fstab entry and try again before rebooting

# Use systemd-mount-check (RHEL/newer Ubuntu)
sudo systemd-analyze verify
```

### fstab options reference

| Option | Meaning |
|---|---|
| `defaults` | rw, suid, dev, exec, auto, nouser, async |
| `ro` | Read-only |
| `noexec` | Disallow execution of binaries |
| `noatime` | Do not update access time (performance) |
| `nofail` | Do not fail boot if device is missing |
| `_netdev` | Wait for network before mounting |
| `0 2` | 0=no dump, 2=fsck pass order (0 for non-root) |

## LVM: Logical Volume Manager

### Concepts

```
Physical Device (/dev/sdb1)
    ↓
Physical Volume (PV)
    ↓
Volume Group (VG) — pool of storage
    ↓
Logical Volume (LV) — like a virtual partition
    ↓
Filesystem (ext4, XFS)
    ↓
Mount point
```

### Creating LVM

```bash
# Step 1: Initialize physical volumes
sudo pvcreate /dev/sdb1 /dev/sdc1

# Step 2: Create a volume group
sudo vgcreate data-vg /dev/sdb1 /dev/sdc1

# Step 3: Create a logical volume
sudo lvcreate -L 50G -n data-lv data-vg    # fixed size
sudo lvcreate -l 100%FREE -n data-lv data-vg  # all remaining space

# Step 4: Create filesystem on the LV
sudo mkfs.xfs /dev/data-vg/data-lv

# Step 5: Mount
sudo mkdir -p /mnt/data
sudo mount /dev/data-vg/data-lv /mnt/data

# Add to fstab for persistence
echo '/dev/data-vg/data-lv  /mnt/data  xfs  defaults  0  2' | sudo tee -a /etc/fstab
```

### Inspecting LVM

```bash
pvs        # physical volumes
pvdisplay  # detailed
vgs        # volume groups
vgdisplay
lvs        # logical volumes
lvdisplay
```

### Extending an LV online

```bash
# Add a new physical volume to the VG first (if more space needed)
sudo pvcreate /dev/sdd1
sudo vgextend data-vg /dev/sdd1

# Extend the LV (e.g., add 10G)
sudo lvextend -L +10G /dev/data-vg/data-lv

# Resize the filesystem (ONLINE, no unmount needed for XFS and ext4)
# For XFS:
sudo xfs_growfs /mnt/data

# For ext4:
sudo resize2fs /dev/data-vg/data-lv

# Verify
df -h /mnt/data
lvs
```

### LVM Snapshots

```bash
# Create a read-only snapshot of a logical volume
sudo lvcreate -L 5G -s -n data-snap /dev/data-vg/data-lv

# Mount the snapshot (read-only)
sudo mount -o ro /dev/data-vg/data-snap /mnt/snapshot

# Unmount and remove snapshot when done
sudo umount /mnt/snapshot
sudo lvremove /dev/data-vg/data-snap
```

## Exercises

1. Create a loopback device (`dd if=/dev/zero of=/tmp/disk.img bs=1M count=1024; losetup -f /tmp/disk.img`), partition it, format it with XFS, mount it, and add it to `/etc/fstab`.
2. Create an LVM setup on a loopback device. Extend the logical volume by 200 MB while it is mounted and verify the new size.
3. Create an LVM snapshot, mount it, and read a file from it. Then remove the snapshot.

## References

- `man lvm`
- `man pvcreate`, `man vgcreate`, `man lvcreate`, `man lvextend`
- `man fstab`
- `man mount`
- [RHEL 9 Configuring and managing logical volumes](https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/9/html/configuring_and_managing_logical_volumes/)
- [Ubuntu LVM Guide](https://help.ubuntu.com/community/LVM)
