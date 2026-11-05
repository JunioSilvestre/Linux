# Operating System Security Hardening Standards

## Hardening Directives

### 1. Disable Unused Filesystems & Protocols
Create `/etc/modprobe.d/security-blacklist.conf`:
```
install cramfs /bin/true
install freevxfs /bin/true
install jffs2 /bin/true
install hfs /bin/true
install hfsplus /bin/true
install squashfs /bin/true
install udf /bin/true
install dccp /bin/true
install sctp /bin/true
install rds /bin/true
install tipc /bin/true
```

### 2. Core Dump Restriction
```bash
# /etc/security/limits.d/10-coredump.conf
* hard core 0
```
