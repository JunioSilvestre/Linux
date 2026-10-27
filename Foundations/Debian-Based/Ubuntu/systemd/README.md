# systemd Service Management — Ubuntu

**Level:** Foundations
**Scope:** Debian-Based — Ubuntu 22.04 LTS, Ubuntu 24.04 LTS
**Prerequisites:** [APT Package Management](../APT/README.md)

## Purpose

systemd is the init system and service manager on Ubuntu. It manages the boot process, services (units), and the system state. This guide covers starting, stopping, enabling, and inspecting services.

## Unit Types

| Type | Extension | Purpose |
|---|---|---|
| Service | `.service` | A running daemon or program |
| Socket | `.socket` | Socket-activated service |
| Timer | `.timer` | Scheduled activation (cron replacement) |
| Target | `.target` | Group of units (like runlevels) |
| Mount | `.mount` | Filesystem mount point |
| Path | `.path` | File/directory monitoring |

## systemctl: Service Control

```bash
# Start and stop services
sudo systemctl start nginx
sudo systemctl stop nginx
sudo systemctl restart nginx       # stop + start
sudo systemctl reload nginx        # reload config without stopping (if supported)
sudo systemctl try-restart nginx   # restart only if running

# Enable and disable (persist across reboots)
sudo systemctl enable nginx        # enable at boot
sudo systemctl disable nginx       # disable at boot
sudo systemctl enable --now nginx  # enable AND start immediately
sudo systemctl disable --now nginx # disable AND stop immediately

# Inspect service state
systemctl status nginx
systemctl is-active nginx          # prints 'active' or 'inactive'
systemctl is-enabled nginx         # prints 'enabled' or 'disabled'
systemctl is-failed nginx          # prints 'failed' or 'active'

# List all units
systemctl list-units --type=service
systemctl list-units --type=service --state=failed
systemctl list-unit-files --type=service
```

## Targets (Boot States)

```bash
# Show current target (similar to runlevel)
systemctl get-default

# Common targets
# multi-user.target  = command line, no GUI (like runlevel 3)
# graphical.target   = GUI (like runlevel 5)
# rescue.target      = single-user mode
# emergency.target   = minimal emergency shell

# Change default target
sudo systemctl set-default multi-user.target

# Switch to a different target immediately (does not persist)
sudo systemctl isolate rescue.target
```

## Reading Logs with journalctl

```bash
# View all logs (paginated)
journalctl

# View logs for a specific service
journalctl -u nginx
journalctl -u nginx -n 50       # last 50 lines
journalctl -u nginx -f          # follow (live)
journalctl -u nginx --since today
journalctl -u nginx --since "2024-10-01 08:00" --until "2024-10-01 09:00"

# View current boot
journalctl -b
journalctl -b -1   # previous boot

# Filter by priority
journalctl -p err  # only errors
journalctl -p warning..err

# Show kernel messages only
journalctl -k

# Disk usage of journal
journalctl --disk-usage

# Vacuum old logs
sudo journalctl --vacuum-time=7d     # keep last 7 days
sudo journalctl --vacuum-size=500M   # keep at most 500 MB
```

## Writing a Service Unit File

```bash
# Service unit files location:
# /lib/systemd/system/    — package-installed (do not edit)
# /etc/systemd/system/    — system-wide administrator overrides
# ~/.config/systemd/user/ — user-level services
```

Example: `/etc/systemd/system/myapp.service`

```ini
[Unit]
Description=My Application Server
Documentation=https://example.com/docs
After=network.target
Requires=network.target

[Service]
Type=simple
User=myapp
Group=myapp
WorkingDirectory=/opt/myapp
EnvironmentFile=/etc/myapp/environment
ExecStart=/opt/myapp/bin/server --config /etc/myapp/config.json
ExecReload=/bin/kill -HUP $MAINPID
Restart=on-failure
RestartSec=5
StandardOutput=journal
StandardError=journal
SyslogIdentifier=myapp

[Install]
WantedBy=multi-user.target
```

```bash
# After creating or modifying a unit file:
sudo systemctl daemon-reload
sudo systemctl enable --now myapp
systemctl status myapp
```

## Override Unit Settings (Drop-in Files)

```bash
# Do not edit files in /lib/systemd/system/ directly
# Instead, create an override:
sudo systemctl edit nginx
# This creates /etc/systemd/system/nginx.service.d/override.conf
# and opens an editor

# Example override content (add restart policy):
# [Service]
# Restart=always
# RestartSec=10

sudo systemctl daemon-reload
sudo systemctl restart nginx

# View the full effective configuration
systemctl cat nginx
```

## Exercises

1. Install `nginx`. Enable it to start at boot, then verify it is running. Stop it, verify it is stopped, then start it again.
2. View the last 30 lines of the `ssh` service journal. Identify what log level the messages use.
3. Write a service unit for a simple script (e.g., one that echoes a timestamp to a file every time it starts). Enable, start, and inspect it.
4. Use `systemctl list-units --state=failed` to identify any failed services. Use `journalctl -u <service>` to diagnose the cause.

## References

- `man systemctl`
- `man journalctl`
- `man systemd.service(5)`
- `man systemd.unit(5)`
- [systemd Documentation](https://systemd.io/)
- [Ubuntu systemd Guide](https://ubuntu.com/blog/ubuntu-bionic-systemd)
