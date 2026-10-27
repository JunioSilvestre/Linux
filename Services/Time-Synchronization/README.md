# Time Synchronization — Chrony and NTP

**Domain:** Services
**Prerequisites:** [Host Networking](../../Intermediate/Cross-Distribution/Networking/README.md)
**Distributions:** Ubuntu 22.04/24.04, RHEL 9

## Purpose

Configure accurate system time synchronization using Chrony. Accurate time is critical for logs, certificates, Kerberos authentication, and distributed systems.

## Why Time Matters

- Log correlation across multiple servers requires synchronized clocks.
- TLS certificates have validity windows checked against system time.
- Kerberos (Active Directory integration) fails if clocks differ by more than 5 minutes.
- Databases and distributed systems depend on consistent timestamps.

## Chrony vs systemd-timesyncd

| Tool | Use case |
|---|---|
| `chrony` | Production servers, NTP server role, accurate synchronization |
| `systemd-timesyncd` | Simple client-only SNTP (lightweight, suitable for desktops) |

On servers, prefer Chrony. RHEL 9 uses Chrony by default. Ubuntu 22.04+ uses either.

## Installation

```bash
# Ubuntu (chrony may already be installed)
sudo apt install -y chrony

# RHEL 9 (installed by default)
sudo dnf install -y chrony

# Enable and start
sudo systemctl enable --now chronyd
```

## Configuration

`/etc/chrony.conf` (RHEL) or `/etc/chrony/chrony.conf` (Ubuntu):

```
# NTP servers (use pool for geographic distribution)
pool 2.rhel.pool.ntp.org iburst    # RHEL default
pool ntp.ubuntu.com        iburst  # Ubuntu default
pool 0.pool.ntp.org        iburst
pool 1.pool.ntp.org        iburst

# Use local hardware clock as last resort
local stratum 10

# Allow NTP traffic from local network (if acting as server)
allow 10.0.0.0/8

# Record time drift
driftfile /var/lib/chrony/drift

# Step clock on startup if offset > 1 second
makestep 1.0 3

# Enable kernel synchronization
rtcsync

# Log directory
logdir /var/log/chrony
```

```bash
# Validate configuration
sudo chronyd -Q    # check config without starting
```

## Operations

```bash
# Status overview
chronyc tracking

# Output fields:
# Reference ID   — the server chrony is syncing from
# Stratum        — distance from the reference clock (1 = directly connected to atomic clock)
# System time    — offset from true time
# Last offset    — last measured offset
# RMS offset     — long-term average offset
# Frequency      — rate at which the system clock drifts
# Residual freq  — residual error after correction

# List NTP sources and their status
chronyc sources
chronyc sources -v    # verbose with column descriptions

# Source status:
# * = currently selected source
# + = acceptable alternative
# ? = unreachable
# x = not used (too far off)

# Source statistics
chronyc sourcestats

# Force immediate sync
sudo chronyc makestep

# Check if synchronized
timedatectl
timedatectl show    # machine-readable
```

## Setting Timezone

```bash
# List all timezones
timedatectl list-timezones
timedatectl list-timezones | grep America

# Set timezone
sudo timedatectl set-timezone America/New_York
sudo timedatectl set-timezone UTC    # recommended for servers

# Verify
timedatectl
date
```

## Using Chrony as a Local NTP Server

To provide NTP service to other hosts on your network:

```bash
# Add to /etc/chrony.conf:
# allow 192.168.1.0/24
echo "allow 192.168.1.0/24" | sudo tee -a /etc/chrony/chrony.conf
sudo systemctl restart chronyd

# Firewall
# Ubuntu
sudo ufw allow 123/udp
# RHEL
sudo firewall-cmd --add-service=ntp --permanent
sudo firewall-cmd --reload

# On client machines, point to this server:
# server 192.168.1.1 iburst
```

## Troubleshooting

```bash
# Is chrony running?
systemctl status chronyd

# Is it syncing?
chronyc tracking | grep -E 'Reference|System time|Stratum'

# Are sources reachable?
chronyc sources
# If all show ?, check network and firewall (UDP 123)

# Is NTP blocked by firewall?
sudo tcpdump -i eth0 udp port 123 -c 5

# Force immediate time update
sudo chronyc makestep

# Restart and watch logs
sudo systemctl restart chronyd
journalctl -u chronyd -f
```

## Exercises

1. Install Chrony. Set the timezone to `UTC`. Verify `timedatectl` shows NTP synchronized.
2. Run `chronyc sources -v`. Identify which server is the active reference. Explain the stratum value.
3. Configure Chrony to act as an NTP server for your test network. Verify a client can synchronize from it.

## References

- [Chrony documentation](https://chrony-project.org/documentation.html)
- `man chrony.conf`
- `man chronyc`
- [RHEL 9 Time synchronization](https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/9/html/configuring_basic_system_settings/assembly_managing-time-synchronization_configuring-basic-system-settings)
- [Ubuntu Time synchronization](https://ubuntu.com/server/docs/time-synchronization)
