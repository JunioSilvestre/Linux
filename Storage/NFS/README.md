# Enterprise NFSv4 Share Administration

## Server Configuration (`/etc/exports`)
```
/srv/nfs/shared 192.168.1.0/24(rw,sync,no_subtree_check,no_root_squash)
/srv/nfs/backup 192.168.1.50(ro,sync,root_squash,no_subtree_check)
```

Apply exports:
```bash
sudo exportfs -rav
sudo exportfs -v
```

## Client Mount with Systemd Automount
Add to `/etc/fstab`:
```
storage.corp.internal:/srv/nfs/shared  /mnt/shared  nfs4  defaults,_netdev,x-systemd.automount,x-systemd.idle-timeout=300  0 0
```
