# Advanced Storage: RAID, LVM Striping, Filesystem Tuning

**Level:** Advanced
**Scope:** Cross-Distribution
**Prerequisites:** [Storage Intermediate](../../../Intermediate/Cross-Distribution/Storage/README.md)

## RAID with mdadm

> **SAFETY:** All examples use virtual or loopback devices. Never run RAID creation commands against disks with existing data without verifying device paths.

```bash
# Create loopback devices for testing
for i in 1 2 3 4; do
  dd if=/dev/zero of=/tmp/disk${i}.img bs=1M count=512
  sudo losetup -f /tmp/disk${i}.img
done

# Check which loopback devices were created
losetup -a
```

### RAID 1 (Mirror)

```bash
# Create RAID 1 array (2 devices)
sudo mdadm --create /dev/md0 --level=1 --raid-devices=2 /dev/loop0 /dev/loop1

# Monitor creation progress
cat /proc/mdstat

# Get array details
sudo mdadm --detail /dev/md0
```

### RAID 5 (Striping with parity)

```bash
# Requires minimum 3 devices
sudo mdadm --create /dev/md1 --level=5 --raid-devices=3 /dev/loop0 /dev/loop1 /dev/loop2

cat /proc/mdstat
```

### Managing RAID

```bash
# Save RAID configuration
sudo mdadm --detail --scan | sudo tee -a /etc/mdadm/mdadm.conf   # Ubuntu
sudo mdadm --detail --scan | sudo tee -a /etc/mdadm.conf         # RHEL

# Rebuild initramfs to include RAID config
sudo update-initramfs -u    # Ubuntu
sudo dracut --force          # RHEL

# Simulate disk failure (test recovery)
sudo mdadm --fail /dev/md0 /dev/loop1
sudo mdadm --remove /dev/md0 /dev/loop1

# Add a replacement disk
sudo mdadm --add /dev/md0 /dev/loop2

# Watch rebuild
watch cat /proc/mdstat

# Stop and remove array (test teardown)
sudo mdadm --stop /dev/md0
sudo mdadm --remove /dev/md0
```

## LVM on RAID

```bash
# After creating /dev/md0, use it as a physical volume
sudo pvcreate /dev/md0
sudo vgcreate raid-vg /dev/md0
sudo lvcreate -L 400M -n data-lv raid-vg
sudo mkfs.xfs /dev/raid-vg/data-lv
```

## Filesystem Tuning

### ext4

```bash
# Show filesystem parameters
tune2fs -l /dev/sdb1

# Set reserved blocks to 1% (default is 5%)
sudo tune2fs -m 1 /dev/sdb1

# Enable journal checksums
sudo tune2fs -E metadata_csum_seed -O metadata_csum /dev/sdb1

# Check and repair (unmounted)
sudo fsck.ext4 -f /dev/sdb1

# Schedule periodic check
sudo tune2fs -c 30 /dev/sdb1   # check every 30 mounts
```

### XFS

```bash
# XFS info
xfs_info /dev/sdb1

# Check for corruption (read-only)
sudo xfs_check /dev/sdb1   # deprecated on RHEL 9, use xfs_repair -n
sudo xfs_repair -n /dev/sdb1   # dry-run check

# Repair (unmounted)
sudo xfs_repair /dev/sdb1

# Freeze/unfreeze (for consistent snapshots)
sudo xfs_freeze -f /mnt/data
# Take snapshot here
sudo xfs_freeze -u /mnt/data
```

## References

- `man mdadm`
- `man tune2fs`
- `man xfs_repair`
- [RHEL 9 Managing RAID](https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/9/html/managing_storage_devices/managing-raid_managing-storage-devices)
- [Ubuntu mdadm](https://help.ubuntu.com/community/Installation/SoftwareRAID)
