# Software RAID Administration with mdadm

## Creating RAID 10 Array
```bash
# Create RAID 10 array across 4 disks
sudo mdadm --create --verbose /dev/md0 --level=10 --raid-devices=4 /dev/sdb /dev/sdc /dev/sdd /dev/sde

# Save RAID configuration
sudo mdadm --detail --scan | sudo tee -a /etc/mdadm/mdadm.conf

# Check array sync status
cat /proc/mdstat
sudo mdadm --detail /dev/md0
```

## Drive Failure & Recovery Procedure
```bash
# 1. Mark disk as faulty
sudo mdadm /dev/md0 --fail /dev/sdc

# 2. Remove failed disk
sudo mdadm /dev/md0 --remove /dev/sdc

# 3. Physically replace drive, then add replacement
sudo mdadm /dev/md0 --add /dev/sdc

# 4. Monitor rebuild progress
watch cat /proc/mdstat
```
