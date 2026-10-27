# systemd Service Management — RHEL 9

**Level:** Foundations
**Scope:** Red Hat-Based — RHEL 9, Rocky Linux 9, AlmaLinux 9
**Prerequisites:** [DNF Package Management](../DNF/README.md)

## Purpose

systemd on RHEL 9 is functionally similar to Ubuntu but has some important differences in log storage, service defaults, and integration with SELinux. This guide covers service management on RHEL and highlights RHEL-specific behaviors.

## Differences from Ubuntu's systemd

| Aspect | Ubuntu | RHEL 9 |
|---|---|---|
| Journal persistence | Volatile by default on some releases | Persistent by default (in /var/log/journal) |
| Traditional syslog | rsyslog installed by default | rsyslog installed by default |
| Firewall integration | UFW (wrapper around nftables/iptables) | firewalld |
| SELinux | AppArmor (default) | SELinux (default, Enforcing) |
| Unit file paths | Same | Same |

## Service Control

```bash
# The systemctl commands are identical to Ubuntu
sudo systemctl start nginx
sudo systemctl stop nginx
sudo systemctl restart nginx
sudo systemctl reload nginx
sudo systemctl enable --now nginx
sudo systemctl disable --now nginx

systemctl status nginx
systemctl is-active nginx
systemctl is-enabled nginx
systemctl is-failed nginx

# List all service units
systemctl list-units --type=service
systemctl list-units --type=service --state=failed
```

## Targets

```bash
systemctl get-default
# multi-user.target  (server default)
# graphical.target   (desktop)

sudo systemctl set-default multi-user.target
```

## Persistent Journal on RHEL 9

On RHEL 9, the journal is persistent by default:

```bash
ls /var/log/journal/
# Each directory contains one machine ID's logs

# Inspect logs across reboots
journalctl --list-boots
journalctl -b -1   # previous boot

# View disk usage
journalctl --disk-usage

# Control retention in /etc/systemd/journald.conf
# SystemMaxUse=500M
# MaxRetentionSec=1month
```

## journalctl

```bash
# Service logs
journalctl -u nginx
journalctl -u nginx -n 50
journalctl -u nginx -f
journalctl -u nginx --since "1 hour ago"

# Priority filter
journalctl -p err
journalctl -p warning..crit

# Current boot
journalctl -b

# Kernel messages
journalctl -k
```

## RHEL-Specific: rsyslog Integration

```bash
# rsyslog reads from journald and writes to files
systemctl status rsyslog

# Log files populated by rsyslog on RHEL
ls /var/log/
# /var/log/messages   — general messages (equivalent of /var/log/syslog on Ubuntu)
# /var/log/secure     — authentication (equivalent of /var/log/auth.log on Ubuntu)
# /var/log/cron       — cron job logs
# /var/log/maillog    — mail service logs

tail -f /var/log/messages
tail -f /var/log/secure
```

## Writing Service Units on RHEL

Unit files are identical in syntax to Ubuntu. Key RHEL consideration: SELinux contexts.

```bash
# If a service binary is in a non-standard path, SELinux may block it
# Correct approach: apply the correct SELinux type to the binary
chcon -t bin_t /opt/myapp/bin/server
# Or better: define a fcontext rule
semanage fcontext -a -t bin_t '/opt/myapp/bin(/.*)?'
restorecon -Rv /opt/myapp/bin/
```

## Exercises

1. Install `httpd` (Apache on RHEL). Enable and start it. Confirm it is active with `systemctl status httpd`.
2. View its journal with `journalctl -u httpd`. Compare the log paths under `/var/log/httpd/` with what journald records.
3. Simulate a failure (stop httpd, break its config, start it), then use `journalctl -u httpd --since today` to diagnose.
4. Read `/var/log/secure` to identify the last 5 SSH login attempts.

## References

- `man systemctl`
- `man journalctl`
- [RHEL 9 Configuring basic system settings](https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/9/html/configuring_basic_system_settings/)
- [systemd.io](https://systemd.io/)
