# SELinux Production Architecture & Policy

## Core Concepts
- **Enforcing**: Policy is actively enforced; unauthorized actions blocked and logged.
- **Permissive**: Policy violations are logged but not blocked (diagnostic mode).
- **Disabled**: SELinux subsystem turned off (never recommended in production).

## Restoring Security Contexts
```bash
# Check file security context
ls -lZ /var/www/html/

# Restore default SELinux context recursively
sudo restorecon -Rv /var/www/html/
```
