# File Ownership, Permissions, and ACLs

**Level:** Foundations
**Scope:** Cross-Distribution
**Prerequisites:** [CLI Fundamentals](../CLI/README.md), [Filesystem Hierarchy](../Filesystem/README.md)

## Purpose

Linux uses a discretionary access control model. Every file has an owner user, an owner group, and a permission set. Access Control Lists (ACLs) extend this model. This guide covers reading, interpreting, and correctly setting permissions.

## Permission Basics

```bash
ls -la /etc/passwd
# -rw-r--r-- 1 root root 2847 Oct 15 09:12 /etc/passwd
#  ^^^^^^^^^
#  ||| |||  Permission bits
#  ||| ||+- Others: read
#  ||| |+-- Others: (no write)
#  ||| +--- Others: (no execute)
#  ||+----- Group: read
#  |+------ Group: (no write)
#  +------- Owner (user): read+write
```

### Permission values

| Symbol | Numeric | Meaning (file) | Meaning (directory) |
|---|---|---|---|
| r | 4 | Read file content | List directory contents |
| w | 2 | Write/modify file | Create, delete, rename entries |
| x | 1 | Execute file | Enter directory (traverse) |
| - | 0 | No permission | No permission |

## Changing Permissions

```bash
# Symbolic mode
chmod u+x script.sh         # add execute for owner
chmod g-w file.txt          # remove write for group
chmod o-r private.txt       # remove read for others
chmod a+r public.txt        # add read for all (a = ugo)
chmod u=rw,g=r,o= file.txt  # set exact permissions

# Numeric (octal) mode
chmod 644 file.txt    # rw-r--r--
chmod 755 script.sh   # rwxr-xr-x
chmod 600 private.key # rw-------
chmod 700 ~/.ssh      # rwx------

# Recursive
chmod -R 755 /var/www/html
```

### Common permission patterns

| Octal | Symbolic | Typical use |
|---|---|---|
| 644 | rw-r--r-- | Regular files (configs, docs) |
| 755 | rwxr-xr-x | Executables, public directories |
| 600 | rw------- | Private files (SSH keys, secrets) |
| 700 | rwx------ | Private directories |
| 640 | rw-r----- | Group-readable configs |
| 750 | rwxr-x--- | Group-executable directories |

## Changing Ownership

```bash
# Change owner
chown alice file.txt

# Change owner and group
chown alice:developers file.txt

# Change group only
chgrp developers file.txt

# Recursive
chown -R www-data:www-data /var/www/html

# Verify
ls -la file.txt
stat file.txt
```

## Special Permission Bits

### setuid (SUID) — numeric 4000

```bash
# When set on an executable, it runs as the file owner, not the caller
ls -la /usr/bin/passwd
# -rwsr-xr-x 1 root root ... /usr/bin/passwd
#      ^ s = setuid + execute

# Set setuid
chmod u+s /path/to/file
chmod 4755 /path/to/file

# Find setuid files (security audit)
find / -perm -4000 -type f 2>/dev/null
```

### setgid (SGID) — numeric 2000

```bash
# On executable: runs as group owner
# On directory: new files inherit the directory's group (useful for shared dirs)
chmod g+s /srv/shared
chmod 2775 /srv/shared
```

### sticky bit — numeric 1000

```bash
# On a directory: users can only delete their own files, not others'
# Classic example: /tmp
ls -la / | grep tmp
# drwxrwxrwt ... tmp    (t = sticky + execute)

chmod +t /shared
chmod 1777 /tmp
```

## Default Permissions: umask

```bash
# umask subtracts permissions from the maximum (666 for files, 777 for dirs)
umask              # show current umask (e.g., 0022)
# Files created with umask 0022: 666 - 022 = 644 (rw-r--r--)
# Dirs created with umask 0022:  777 - 022 = 755 (rwxr-xr-x)

# Set umask (current session)
umask 027   # files=640, dirs=750

# Persistent: add to ~/.bashrc or /etc/profile.d/custom.sh
echo 'umask 027' >> ~/.bashrc
```

## Access Control Lists (ACLs)

ACLs allow granting permissions to specific users or groups beyond the owner/group/other model.

```bash
# Check if ACL support is enabled (most modern filesystems)
getfacl /etc/passwd

# Set ACL: give user bob read access to a file
setfacl -m u:bob:r file.txt

# Set ACL: give group devs read+write
setfacl -m g:devs:rw file.txt

# Set default ACL on a directory (inherited by new files)
setfacl -m d:u:bob:r /shared/dir
setfacl -d -m g:devs:rw /shared/dir

# View ACLs (a '+' at the end of permissions in ls -l indicates ACLs)
getfacl file.txt

# Remove a specific ACL entry
setfacl -x u:bob file.txt

# Remove all ACLs
setfacl -b file.txt
```

> **Note:** ACL support depends on the filesystem (ext4, XFS both support ACLs) and the mount options. Ubuntu and RHEL enable ACLs by default on ext4 and XFS.

## Diagnosing Permission Errors

```bash
# Check effective permissions for the current user
# 1. Identify the file's owner, group, and permissions
ls -la /path/to/file

# 2. Identify who you are and your groups
id

# 3. Read the ACL
getfacl /path/to/file

# Common causes of 'Permission denied':
# - User is not the owner AND not in the file's group AND others have no access
# - A parent directory lacks execute (traverse) permission
# - SELinux or AppArmor policy is blocking access (check: getenforce; ausearch -m avc)

# Test permission as another user
sudo -u alice ls /path/to/file
```

## Exercises

1. Create a directory `/tmp/shared` with permissions that allow: the owner (you) full access, your primary group read+write, and others no access.
2. Create a script, set it to executable only by the owner, and verify that another user cannot execute it.
3. Use `setfacl` to grant a specific user read access to a file they otherwise cannot read. Verify with `su - otheruser` and `cat file`.
4. Find all setuid executables on your system. Explain why `/usr/bin/sudo` has setuid set.

## References

- `man chmod`
- `man chown`
- `man setfacl`
- `man getfacl`
- `man umask`
- [Linux File Permission Tutorial](https://linuxcommand.org/lc3_lts0090.php)
