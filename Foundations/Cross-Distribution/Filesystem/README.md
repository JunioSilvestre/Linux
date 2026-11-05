# Linux Filesystem Hierarchy

**Level:** Foundations
**Scope:** Cross-Distribution
**Prerequisites:** Basic CLI navigation

## Purpose

Understand the Linux Filesystem Hierarchy Standard (FHS), file types, and hard and symbolic links. This knowledge is required to locate configuration files, logs, binaries, and data on any Linux system without guessing.

## Filesystem Hierarchy Standard

```
/
├── bin/      # Essential user command binaries (ln -s to /usr/bin on modern systems)
├── boot/     # Kernel, initramfs, GRUB bootloader
├── dev/      # Device files (block, character, pseudo-devices)
├── etc/      # System-wide configuration files (text-editable)
├── home/     # User home directories (/home/username)
├── lib/      # Shared libraries for /bin and /sbin
├── media/    # Mount points for removable media
├── mnt/      # Temporary mount points
├── opt/      # Optional third-party software
├── proc/     # Virtual FS: kernel and process information
├── root/     # Home directory for the root account
├── run/      # Runtime data (PID files, sockets)
├── sbin/     # System administration binaries
├── srv/      # Data for services (web, FTP content)
├── sys/      # Virtual FS: hardware and kernel information
├── tmp/      # Temporary files (cleared on reboot or by policy)
├── usr/      # Read-only user data, programs, and libraries
│   ├── bin/      # Non-essential user binaries
│   ├── lib/      # Libraries for /usr/bin
│   ├── local/    # Locally installed software (not managed by package manager)
│   └── share/    # Architecture-independent data (docs, man pages)
└── var/      # Variable data: logs, spools, caches, databases
    ├── log/      # Log files
    ├── spool/    # Queues (print, mail, cron)
    └── tmp/      # Persistent temp data (not cleared on reboot)
```

### Important locations

| Path | Purpose |
|---|---|
| `/etc/passwd` | User account database |
| `/etc/shadow` | Password hashes (root-readable only) |
| `/etc/sudoers` | sudo policy |
| `/etc/hostname` | System hostname |
| `/etc/hosts` | Static DNS entries |
| `/etc/fstab` | Persistent mount configuration |
| `/etc/crontab` | System cron jobs |
| `/var/log/auth.log` | Authentication log (Debian/Ubuntu) |
| `/var/log/secure` | Authentication log (RHEL) |
| `/var/log/syslog` | General system log (Debian/Ubuntu) |
| `/var/log/messages` | General system log (RHEL) |
| `/proc/cpuinfo` | CPU information |
| `/proc/meminfo` | Memory information |
| `/proc/net/` | Network state |

## Virtual Filesystems: /proc and /sys

`/proc` and `/sys` are not stored on disk. They are dynamic views of kernel state.

```bash
# Read CPU information
cat /proc/cpuinfo

# Read memory information
cat /proc/meminfo

# Inspect a specific process (replace PID)
ls /proc/1234/
cat /proc/1234/status
ls -la /proc/1234/fd     # open file descriptors

# Inspect a kernel parameter
cat /proc/sys/net/ipv4/ip_forward

# Set a kernel parameter at runtime (non-persistent)
echo 1 > /proc/sys/net/ipv4/ip_forward
# Persistent: use sysctl instead
sysctl -w net.ipv4.ip_forward=1
echo 'net.ipv4.ip_forward = 1' >> /etc/sysctl.d/99-custom.conf
sysctl -p /etc/sysctl.d/99-custom.conf
```

## File Types

```bash
# Identify file type
file /bin/bash
file /etc/passwd
file /dev/sda

# ls -l prefix meanings:
# - : regular file
# d : directory
# l : symbolic link
# b : block device
# c : character device
# p : named pipe (FIFO)
# s : socket

ls -la /dev/ | head -20
```

## Hard Links and Symbolic Links

### Hard links

```bash
# Create a hard link
ln original.txt hardlink.txt

# Both point to the same inode (same data on disk)
# The file is only deleted when ALL hard links are removed
ls -li original.txt hardlink.txt    # same inode number

# Hard links cannot span filesystems or point to directories
```

### Symbolic links (symlinks)

```bash
# Create a symbolic link
ln -s /path/to/target linkname

# Example: link current nginx config
ln -s /etc/nginx/sites-available/mysite.conf /etc/nginx/sites-enabled/mysite.conf

# Inspect
ls -la /etc/nginx/sites-enabled/

# Broken symlinks: point to a target that no longer exists
find /etc -xtype l    # find broken symlinks

# Remove a symlink (do not add trailing /)
rm linkname
unlink linkname
```

### Differences

| Property | Hard Link | Symbolic Link |
|---|---|---|
| Inode | Same as original | New inode |
| Cross-filesystem | No | Yes |
| Points to directories | No (usually) | Yes |
| Survives target deletion | Yes (data preserved) | No (becomes broken) |
| Shows as | Same as original | `l` in `ls -l` |

## Disk Usage

```bash
# Filesystem usage
df -h                   # human-readable, all mounted filesystems
df -h /var              # specific path
df -i                   # inode usage (not block usage)

# Directory size
du -sh /var/log         # total size of /var/log
du -sh /var/log/*       # size of each item
du -sh /* 2>/dev/null   # size of each top-level directory

# Find large files
find / -size +100M -not -path '/proc/*' -not -path '/sys/*' 2>/dev/null
```

## Exercises

1. List every mounted filesystem and identify which type (ext4, xfs, tmpfs, etc.) each one is.
2. Explain why `/proc/cpuinfo` exists but takes no disk space.
3. Create a file, make a hard link and a symlink to it. Delete the original file. What happens to each link?
4. Find the five largest files under `/var` on your system.

## References

- [Filesystem Hierarchy Standard](https://refspecs.linuxfoundation.org/FHS_3.0/fhs-3.0.html)
- `man hier`
- `man ln`
- `man df`
- `man du`
