# Logical Volume Manager (LVM2) Administration

## Standard Storage Provisioning
```bash
# 1. Initialize physical volumes
sudo pvcreate /dev/sdb /dev/sdc

# 2. Create volume group
sudo vgcreate vg_enterprise /dev/sdb /dev/sdc

# 3. Create logical volume
sudo lvcreate -L 100G -n lv_database vg_enterprise

# 4. Format and mount
sudo mkfs.xfs /dev/vg_enterprise/lv_database
sudo mount /dev/vg_enterprise/lv_database /srv/database

# 5. Online extension
sudo lvextend -L +50G -r /dev/vg_enterprise/lv_database
```

## LVM Snapshots for Backups
```bash
# Create 10GB snapshot
sudo lvcreate -L 10G -s -n lv_db_snap /dev/vg_enterprise/lv_database

# Mount snapshot (read-only)
sudo mount -o nouuid,ro /dev/vg_enterprise/lv_db_snap /mnt/snapshot

# Remove snapshot after backup
sudo umount /mnt/snapshot
sudo lvremove -y /dev/vg_enterprise/lv_db_snap
```
