# Host Firewall with firewalld — RHEL 9

**Level:** Intermediate
**Scope:** Red Hat-Based — RHEL 9, Rocky Linux 9, AlmaLinux 9
**Prerequisites:** [Host Networking](../../../Cross-Distribution/Networking/README.md)

## Purpose

firewalld is the default firewall management service on RHEL 9. It uses nftables as its backend and manages rules through the concept of zones. This guide covers zone-based firewall configuration.

## Concepts

- **Zone:** A named policy profile. Each network interface is assigned to a zone.
- **Service:** A named rule set (ports + protocols) for a known service.
- **Runtime vs Permanent:** Changes are runtime by default. Use `--permanent` to persist.

## Status and Zones

```bash
# Check firewalld status
sudo systemctl status firewalld
firewall-cmd --state

# List available zones
firewall-cmd --get-zones

# Show active zones and their interfaces
firewall-cmd --get-active-zones

# Show default zone
firewall-cmd --get-default-zone

# List all rules in the default zone
firewall-cmd --list-all

# List a specific zone
firewall-cmd --zone=public --list-all
```

## Managing Services

```bash
# List available service definitions
firewall-cmd --get-services

# Show what ports a service opens
firewall-cmd --info-service=http

# Allow a service (runtime only)
firewall-cmd --add-service=http
firewall-cmd --add-service=https
firewall-cmd --add-service=ssh

# Allow a service permanently
firewall-cmd --add-service=http --permanent
firewall-cmd --add-service=https --permanent

# Apply permanent rules to runtime
firewall-cmd --reload

# Remove a service
firewall-cmd --remove-service=http --permanent
firewall-cmd --reload
```

## Managing Ports

```bash
# Open a specific port
firewall-cmd --add-port=8080/tcp --permanent
firewall-cmd --add-port=1000-2000/tcp --permanent
firewall-cmd --reload

# Remove a port
firewall-cmd --remove-port=8080/tcp --permanent
firewall-cmd --reload

# List open ports
firewall-cmd --list-ports
```

## Rich Rules

Rich rules allow more specific conditions:

```bash
# Allow SSH only from a specific IP
firewall-cmd --add-rich-rule='rule family=ipv4 source address=192.168.1.50 service name=ssh accept' --permanent

# Block a specific IP
firewall-cmd --add-rich-rule='rule family=ipv4 source address=10.0.0.5 drop' --permanent

# Rate limit connections
firewall-cmd --add-rich-rule='rule service name=ssh accept limit value=3/m' --permanent

firewall-cmd --reload

# List rich rules
firewall-cmd --list-rich-rules
```

## Zone Assignment

```bash
# Assign an interface to a zone
sudo firewall-cmd --zone=trusted --add-interface=eth1 --permanent
firewall-cmd --reload

# Change default zone
sudo firewall-cmd --set-default-zone=public
```

## Exercises

1. Allow HTTP and HTTPS permanently. Block port 23 (Telnet). Reload and verify.
2. Allow SSH only from a specific subnet (e.g., 192.168.1.0/24) using a rich rule.
3. Change the default zone to `dmz` and inspect what services are allowed.

## References

- `man firewall-cmd`
- [RHEL 9 Controlling traffic with firewalld](https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/9/html/securing_networks/using-and-configuring-firewalld_securing-networks)
- [firewalld Documentation](https://firewalld.org/documentation/)
