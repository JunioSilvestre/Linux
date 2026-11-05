# SELinux Foundations — RHEL 9

**Level:** Foundations
**Scope:** Red Hat-Based — RHEL 9, Rocky Linux 9, AlmaLinux 9
**Prerequisites:** [DNF Package Management](../DNF/README.md), [Permissions](../../../Cross-Distribution/Permissions/README.md)

## Purpose

SELinux (Security-Enhanced Linux) is a mandatory access control (MAC) system built into the Linux kernel. On RHEL, it is enabled by default in Enforcing mode. This guide covers reading SELinux status, interpreting denials, and resolving policy violations correctly.

> **Critical principle:** Do not disable SELinux to make a service work. Doing so removes a major security layer and leaves you unable to diagnose real policy violations. Always investigate and resolve the actual policy requirement.

## Key Concepts

- **Label (context):** Every process and file has an SELinux context: `user:role:type:level`. The type is the most important for daily administration.
- **Policy:** A set of rules that defines which types are allowed to interact with which.
- **Mode:**
  - `Enforcing`: Policy is enforced. Violations are blocked and logged.
  - `Permissive`: Policy is NOT enforced but violations are logged. Used for troubleshooting.
  - `Disabled`: SELinux is off entirely (requires reboot to change from/to disabled).
- **AVC denial:** A log entry recording an access attempt that was denied by policy.

## Checking SELinux Status

```bash
# Check current mode
getenforce
# Output: Enforcing, Permissive, or Disabled

# Show detailed status
sestatus
sestatus -v

# Configuration file (permanent mode setting)
cat /etc/selinux/config
# SELINUX=enforcing   ← set this, then reboot for change to take effect
# SELINUXTYPE=targeted
```

## Viewing Contexts

```bash
# File context
ls -lZ /var/www/html/
# -rw-r--r--. root root system_u:object_r:httpd_sys_content_t:s0 index.html
#                       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#                       user:role:type:level

# Process context
ps auxZ | grep nginx
ps -eZ | grep httpd

# Port context
semanage port -l | grep http
```

## Reading AVC Denials

```bash
# Check for recent denials
ausearch -m avc --start recent
avsearch -m avc -ts today

# Using audit log directly
grep 'denied' /var/log/audit/audit.log | tail -20

# More human-readable output
audit2why < /var/log/audit/audit.log

# Human-readable denial summary
sealert -a /var/log/audit/audit.log
# (requires: sudo dnf install setroubleshoot-server)
```

### Reading an AVC message

```
type=AVC msg=audit(1698400000.000:12345): avc: denied { read } for
  pid=1234 comm="nginx" name="secret.txt" dev="sda1" ino=56789
  scontext=system_u:system_r:httpd_t:s0
  tcontext=system_u:object_r:admin_home_t:s0 tclass=file permissive=0
```

Interpretation:
- Process: `nginx` (type `httpd_t`)
- Tried to: `read`
- Target file: `secret.txt` (type `admin_home_t`)
- Result: `denied` (permissive=0 means Enforcing mode)
- Problem: `httpd_t` is not allowed to read `admin_home_t` files. The file's label is wrong.

## Common Resolution: Fixing File Labels

```bash
# Check the expected context for a path
semanage fcontext -l | grep '/var/www'

# Show current vs expected context
restorecon -nv /var/www/html/   # dry run

# Apply the correct context based on policy rules
restorecon -Rv /var/www/html/   # recursive, verbose

# Verify
ls -lZ /var/www/html/
```

## Setting Custom File Contexts

```bash
# Add a new file context rule (survives relabeling)
sudo semanage fcontext -a -t httpd_sys_content_t '/srv/mysite(/.*)?'

# Apply the rule
sudo restorecon -Rv /srv/mysite

# List custom rules
semanage fcontext -l -C
```

## SELinux Booleans

Booleans are on/off switches that enable specific policy behaviors without needing a policy recompile.

```bash
# List all booleans
getsebool -a
getsebool -a | grep httpd

# Check a specific boolean
getsebool httpd_can_network_connect

# Set a boolean (current session only)
sudo setsebool httpd_can_network_connect on

# Set a boolean persistently (survives reboot)
sudo setsebool -P httpd_can_network_connect on

# Common booleans for web servers:
# httpd_can_network_connect      = allow httpd to connect to network
# httpd_can_network_connect_db   = allow httpd to connect to databases
# httpd_enable_homedirs          = allow httpd to serve files from home dirs
```

## Temporarily Using Permissive Mode

```bash
# Switch to permissive mode (does NOT persist across reboots)
sudo setenforce 0
getenforce  # Permissive

# Test your service — if it works in Permissive, the issue is SELinux

# Collect denials while in permissive
ausearch -m avc -ts recent

# Generate a policy module from the denials
ausearch -m avc -ts recent | audit2allow -M mymodule

# Install the generated module
semodule -i mymodule.pp

# Switch back to enforcing
sudo setenforce 1
getenforce  # Enforcing
```

> Permissive mode is a diagnostic tool, not a solution. Always re-enable Enforcing mode.

## Exercises

1. Install `nginx`. Move a file into `/srv/mysite/`. Attempt to serve it. If denied, read the AVC, fix the label with `semanage` and `restorecon`, and confirm nginx can serve it.
2. Enable the boolean `httpd_can_sendmail` persistently. Verify the change survived a service restart.
3. Use `sealert` to interpret an AVC denial from `/var/log/audit/audit.log`.

## References

- [RHEL 9 SELinux User and Administrator Guide](https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/9/html/using_selinux/)
- `man semanage`
- `man restorecon`
- `man setsebool`
- `man audit2allow`
- [SELinux Notebook](https://github.com/SELinuxProject/selinux-notebook)
