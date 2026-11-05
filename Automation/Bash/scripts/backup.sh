#!/usr/bin/env bash
set -euo pipefail
IFS=$'\n\t'

readonly BACKUP_SRC="${1:-/var/www}"
readonly BACKUP_DEST="${2:-/var/backups}"
readonly TIMESTAMP="$(date +%Y%m%d_%H%M%S)"
readonly ARCHIVE="${BACKUP_DEST}/backup_${TIMESTAMP}.tar.gz"

log() {
    echo "[$(date -u +'%Y-%m-%dT%H:%M:%SZ')] $*"
}

cleanup() {
    log "Performing cleanup..."
}
trap cleanup EXIT ERR

log "Starting backup of ${BACKUP_SRC} to ${ARCHIVE}"
mkdir -p "${BACKUP_DEST}"
tar -czf "${ARCHIVE}" -C "$(dirname "${BACKUP_SRC}")" "$(basename "${BACKUP_SRC}")"
log "Backup successfully completed. Size: $(du -h "${ARCHIVE}" | awk '{print $1}')"
