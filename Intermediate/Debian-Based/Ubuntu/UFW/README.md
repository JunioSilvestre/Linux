# Host Firewall with UFW — Ubuntu

**Level:** Intermediate
**Scope:** Debian-Based — Ubuntu 22.04 LTS, Ubuntu 24.04 LTS
**Prerequisites:** [Host Networking](../../../Cross-Distribution/Networking/README.md)

## Purpose

UFW (Uncomplicated Firewall) is the default host firewall management tool on Ubuntu. It provides a simplified interface over nftables/iptables. This guide covers enabling UFW, writing rules, and validating firewall state.

## Enable and Status

```bash
# Check current status
sudo ufw status
sudo ufw status verbose    # more detail
sudo ufw status numbered   # show rules with numbers

# Enable (accepts all incoming SSH first to avoid lockout)
sudo ufw allow ssh
sudo ufw enable

# Disable (allow all traffic)
sudo ufw disable

# Reset all rules
sudo ufw reset
```

## Default Policies

```bash
# Best practice: deny all incoming, allow all outgoing
sudo ufw default deny incoming
sudo ufw default allow outgoing

# More restrictive: also deny forwarding
sudo ufw default deny forward
```

## Allowing and Denying Services

```bash
# By service name (from /etc/services)
sudo ufw allow ssh
sudo ufw allow http
sudo ufw allow https

# By port
sudo ufw allow 22/tcp
sudo ufw allow 80/tcp
sudo ufw allow 443/tcp
sudo ufw allow 8080/tcp

# By port range
sudo ufw allow 1000:2000/tcp

# By application profile
sudo ufw app list            # list available profiles
sudo ufw allow 'Nginx Full'  # allow both 80 and 443

# From specific IP
sudo ufw allow from 192.168.1.50
sudo ufw allow from 192.168.1.50 to any port 22

# From a subnet
sudo ufw allow from 10.0.0.0/8

# Deny a specific port
sudo ufw deny 23/tcp

# Delete a rule
sudo ufw status numbered
sudo ufw delete 3              # delete rule number 3
sudo ufw delete allow http    # delete by specification
```

## Rate Limiting

```bash
# Limit connections (drop after 6 connections in 30 seconds)
# Useful for SSH brute force mitigation
sudo ufw limit ssh
sudo ufw limit 22/tcp
```

## Logging

```bash
# Enable logging
sudo ufw logging on
sudo ufw logging medium    # off, low, medium, high, full

# Logs go to /var/log/ufw.log
tail -f /var/log/ufw.log
grep 'BLOCK' /var/log/ufw.log | tail -20
```

## Application Profiles

```bash
# Profiles are in /etc/ufw/applications.d/
ls /etc/ufw/applications.d/
cat /etc/ufw/applications.d/openssh-server

# Create a custom profile
sudo tee /etc/ufw/applications.d/myapp << 'EOF2'
[MyApp]
title=My Application
description=Custom application
ports=8443/tcp
EOF2

sudo ufw app update MyApp
sudo ufw allow MyApp
```

## Verify and Test

```bash
# Show current rules
sudo ufw status verbose

# Test from another host
nc -zv target_host 22
curl -I http://target_host

# Show underlying nftables rules
sudo nft list ruleset

# Show iptables rules (legacy)
sudo iptables -L -n -v
```

## Exercises

1. Configure UFW to allow SSH and HTTPS only. Deny all other incoming traffic. Verify with `ufw status verbose`.
2. Enable rate limiting on SSH. Use `curl` in a loop from another host to trigger the limit and observe the logs.
3. Create an application profile for a custom service on port 9000/tcp. Allow it in UFW.

## References

- `man ufw`
- [Ubuntu UFW documentation](https://help.ubuntu.com/community/UFW)
- [Ubuntu Security Guide](https://ubuntu.com/security)
