# Enterprise Filesystem Administration (XFS & Ext4)

## XFS Administration & Maintenance
XFS is the standard filesystem for RHEL. It scales exceptionally well for multi-terabyte volumes and parallel I/O.

```bash
# Format block device with XFS
sudo mkfs.xfs -f -L DATA_VOL /dev/sdb1

# Inspect filesystem geometry
sudo xfs_info /dev/sdb1

# Online growth (XFS cannot be shrunk, only grown)
sudo xfs_growfs /mnt/data

# Filesystem freeze for consistent SAN/Cloud snapshots
sudo xfs_freeze -f /mnt/data
# ... execute cloud snapshot ...
sudo xfs_freeze -u /mnt/data
```
