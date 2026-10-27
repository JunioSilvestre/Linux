# Production Backup Strategies with Restic & Borg

## Restic Encrypted S3/Local Backup
```bash
# Initialize encrypted repository
export RESTIC_REPOSITORY="/mnt/backup/repo"
export RESTIC_PASSWORD_FILE="/etc/restic.secret"
restic init

# Execute snapshot
restic backup /etc /var/www /home --exclude="*.tmp"

# List snapshots
restic snapshots

# Retention policy enforcement
restic forget --keep-daily 7 --keep-weekly 4 --keep-monthly 12 --prune
```
