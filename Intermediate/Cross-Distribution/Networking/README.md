# Host Networking and Name Resolution

**Level:** Intermediate
**Scope:** Cross-Distribution
**Prerequisites:** [CLI Fundamentals](../../../Foundations/Cross-Distribution/CLI/README.md)

## Purpose

Configure and manage host networking, DNS resolution, and connectivity. This guide covers the tools and configuration files used on both Ubuntu and RHEL.

## Distribution Differences

| Aspect | Ubuntu | RHEL 9 |
|---|---|---|
| Network management | NetworkManager + Netplan | NetworkManager |
| Config files | /etc/netplan/*.yaml | /etc/NetworkManager/system-connections/ |
| CLI tool | nmcli, ip | nmcli, ip |
| Legacy ifconfig | Deprecated (use `ip`) | Deprecated (use `ip`) |

## Inspecting Network State

```bash
# Show all interfaces and addresses
ip addr show
ip a                     # short form
ip addr show eth0        # specific interface

# Show routing table
ip route show
ip r                     # short form

# Show neighbor (ARP) table
ip neigh show

# Show interface statistics
ip -s link show eth0

# Show listening sockets and connections
ss -tlnp                 # TCP, listening, numeric, process
ss -tulnp                # TCP + UDP
ss -s                    # summary statistics
netstat -tlnp            # legacy (deprecated, use ss)
```

## Testing Connectivity

```bash
# ICMP ping
ping -c 4 8.8.8.8
ping6 -c 4 ::1           # IPv6

# DNS lookup
nslookup example.com
dig example.com
dig example.com @8.8.8.8 # use specific DNS server
dig +short example.com   # short output
dig -x 8.8.8.8           # reverse lookup

# Trace route
traceroute example.com
tracepath example.com    # alternative (no root required)

# Test TCP connection
curl -v telnet://host:port
nc -zv host port         # netcat connection test
telnet host port         # legacy

# HTTP test
curl -I https://example.com    # headers only
curl -o /dev/null -w '%{http_code}' https://example.com
wget --spider https://example.com
```

## Static IP Configuration

### Ubuntu (Netplan)

`/etc/netplan/01-network.yaml`:

```yaml
network:
  version: 2
  renderer: NetworkManager
  ethernets:
    eth0:
      addresses:
        - 192.168.1.100/24
      routes:
        - to: default
          via: 192.168.1.1
      nameservers:
        addresses: [8.8.8.8, 1.1.1.1]
        search: [example.com]
      dhcp4: false
```

```bash
# Validate configuration
sudo netplan try     # apply temporarily with rollback
sudo netplan apply   # apply permanently

# Verify
ip addr show eth0
ip route show
```

### RHEL 9 (NetworkManager via nmcli)

```bash
# Create a static IP connection
sudo nmcli connection add \
  type ethernet \
  con-name static-eth0 \
  ifname eth0 \
  ipv4.method manual \
  ipv4.addresses 192.168.1.100/24 \
  ipv4.gateway 192.168.1.1 \
  ipv4.dns '8.8.8.8 1.1.1.1' \
  connection.autoconnect yes

# Activate
sudo nmcli connection up static-eth0

# Verify
nmcli connection show static-eth0
ip addr show eth0
```

## Name Resolution

```bash
# Resolution order is controlled by /etc/nsswitch.conf
cat /etc/nsswitch.conf | grep hosts
# hosts: files dns myhostname
# Order: /etc/hosts first, then DNS, then mDNS

# Static hostname entries
cat /etc/hosts
# Add entry:
echo '192.168.1.50  webserver.local webserver' | sudo tee -a /etc/hosts

# DNS configuration
cat /etc/resolv.conf
# nameserver 8.8.8.8
# search example.com

# On systemd-resolved systems, this is a symlink
ls -la /etc/resolv.conf
resolvectl status       # systemd-resolved status
resolvectl query example.com

# Hostname management
hostname               # show current hostname
hostnamectl            # show all hostname info
sudo hostnamectl set-hostname server01.example.com
```

## Exercises

1. Use `ss -tlnp` to find every service listening on your host. Identify the process owning each port.
2. Configure a static IP on a test VM. Verify it survives a reboot.
3. Add a custom entry to `/etc/hosts` and verify it resolves with `dig @localhost` and with `ping`.
4. Use `traceroute` to trace the path to an external host and identify where latency increases.

## References

- `man ip`
- `man ss`
- `man nmcli`
- `man netplan`
- [Ubuntu Networking](https://ubuntu.com/server/docs/network-configuration)
- [RHEL 9 Configuring and managing networking](https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/9/html/configuring_and_managing_networking/)
