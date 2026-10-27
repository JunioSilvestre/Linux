# Security Hardening Baseline

**Level:** Advanced
**Scope:** Cross-Distribution
**Prerequisites:** [Permissions](../../../Foundations/Cross-Distribution/Permissions/README.md), [UFW](../../../Intermediate/Debian-Based/Ubuntu/UFW/README.md) or [firewalld](../../../Intermediate/Red-Hat-Based/RHEL/Firewalld/README.md)

## Purpose

Implement a security hardening baseline aligned with CIS (Center for Internet Security) benchmarks. This guide covers kernel parameters, SSH hardening, user privilege controls, and audit logging.

## Kernel Security Parameters (sysctl)

```bash
# Apply hardening parameters
sudo tee /etc/sysctl.d/99-hardening.conf << 'EOF'
# Network hardening
net.ipv4.ip_forward = 0                    # disable IP forwarding (unless router)
net.ipv4.conf.all.send_redirects = 0       # do not send ICMP redirects
net.ipv4.conf.default.send_redirects = 0
net.ipv4.conf.all.accept_redirects = 0     # do not accept ICMP redirects
net.ipv4.conf.default.accept_redirects = 0
net.ipv4.conf.all.accept_source_route = 0  # disable source routing
net.ipv6.conf.all.accept_redirects = 0
net.ipv4.icmp_echo_ignore_broadcasts = 1   # ignore broadcast pings
net.ipv4.icmp_ignore_bogus_error_responses = 1
net.ipv4.conf.all.rp_filter = 1           # enable reverse path filtering
net.ipv4.conf.default.rp_filter = 1
net.ipv4.tcp_syncookies = 1               # SYN flood protection
# Kernel hardening
kernel.randomize_va_space = 2             # full ASLR
kernel.dmesg_restrict = 1                 # restrict dmesg to root
kernel.kptr_restrict = 2                  # hide kernel pointers
fs.suid_dumpable = 0                      # disable setuid core dumps
