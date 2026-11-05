# Backup and Restoration

**Level:** Intermediate
**Scope:** Cross-Distribution
**Prerequisites:** [Storage](../Storage/README.md)

## Purpose

Implement reliable backup procedures using standard Linux tools. Understand backup strategies, validation, and restoration.

## Backup Strategy Principles

- **3-2-1 Rule:** 3 copies of data, 2 different media types, 1 offsite copy.
- **Test restoration regularly.** An untested backup is not a backup.
- **Validate integrity** after every backup.
- **Document RTO and RPO:** Recovery Time Objective (how fast), Recovery Point Objective (how much data loss is acceptable).

## rsync: Incremental File Synchronization

```bash
# Basic local sync
rsync -av /source/dir/ /destination/dir/
# Trailing / on source = sync contents (not the dir itself)

# Dry run (show what would be done without doing it)
rsync -av --dry-run /source/dir/ /destination/dir/

# Archive mode (preserves permissions, timestamps, symlinks, owner, group)
rsync -a /source/ /destination/

# Delete files in destination not in source
rsync -av --delete /source/ /destination/

# Exclude patterns
rsync -av --exclude='*.log' --exclude='.git' /source/ /destination/

# Remote sync via SSH
rsync -avz -e ssh /local/path/ user@remote:/remote/path/
rsync -avz user@remote:/remote/path/ /local/path/  # pull

# Common options reference:
# -a  archive (equals -rlptgoD)
# -v  verbose
# -z  compress during transfer
# -n  dry run
# -P  show progress + keep partial files
# --delete   delete extraneous files in destination
# --backup   keep older versions with a suffix
# --backup-dir=DIR  put backups in this directory
```

## tar: Archiving

```bash
# Create an archive
tar -czf backup.tar.gz /etc/
# c = create, z = gzip compress, f = filename

# Create with bzip2 compression (smaller, slower)
tar -cjf backup.tar.bz2 /etc/

# Create with xz compression (smallest, slowest)
tar -cJf backup.tar.xz /etc/

# List contents without extracting
tar -tzf backup.tar.gz

# Extract
tar -xzf backup.tar.gz -C /restore/path/

# Extract a single file
tar -xzf backup.tar.gz etc/nginx/nginx.conf

# Preserve permissions and ownership
tar -czf backup.tar.gz --preserve-permissions /etc/
sudo tar -xzf backup.tar.gz -C / --preserve-permissions  # restore as root
```

## Backup Script Example

```bash
#!/usr/bin/env bash
# backup.sh — simple incremental backup with rsync
set -euo pipefail

SOURCE="/etc /home /var/www"
DESTINATION="/mnt/backup"
DATE=$(date +%Y-%m-%d)
LOGFILE="/var/log/backup.log"

if [[ ! -d "${DESTINATION}" ]]; then
  echo "ERROR: Backup destination ${DESTINATION} does not exist" | tee -a "${LOGFILE}"
  exit 1
fi

echo "[${DATE}] Starting backup" | tee -a "${LOGFILE}"

for src in ${SOURCE}; do
  dest_dir="${DESTINATION}/$(basename ${src})"
  mkdir -p "${dest_dir}"
  rsync -a --delete "${src}/" "${dest_dir}/" >> "${LOGFILE}" 2>&1
  echo "[${DATE}] Synced ${src} -> ${dest_dir}" | tee -a "${LOGFILE}"
done

echo "[${DATE}] Backup complete" | tee -a "${LOGFILE}"
```

```bash
# Validate syntax
bash -n backup.sh

# Test with dry-run modifications (add --dry-run to rsync calls)
```

## Verifying Backup Integrity

```bash
# Generate a checksum file
sha256sum important_file.tar.gz > important_file.tar.gz.sha256

# Verify
sha256sum -c important_file.tar.gz.sha256

# Generate checksums for a directory tree
find /backup -type f -exec sha256sum {} \; > /backup/checksums.txt

# Verify all checksums
sha256sum -c /backup/checksums.txt
```

## Exercises

1. Use `rsync` to back up `/etc` to a local directory. Modify a file in `/etc`, run the sync again, and verify only the modified file was transferred (`--itemize-changes`).
2. Create a `tar.gz` backup of a directory. Verify its contents without extracting. Extract it to a different path and compare the file tree.
3. Automate the backup with a cron job or systemd timer. Add integrity verification.

## References

- `man rsync`
- `man tar`
- `man sha256sum`
- [rsync documentation](https://rsync.samba.org/documentation.html)
