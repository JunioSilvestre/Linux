# DHCP — Dynamic Host Configuration Protocol

**Domain:** Services
**Prerequisites:** [Host Networking](../../Intermediate/Cross-Distribution/Networking/README.md)
**Distributions:** Ubuntu 22.04/24.04, RHEL 9

## Purpose

Configure a DHCP server to assign IP addresses, gateways, and DNS servers to network clients automatically.

## Distribution Notes

| Aspect | Ubuntu | RHEL 9 |
|---|---|---|
| Legacy package | `isc-dhcp-server` | `dhcp-server` |
| Modern alternative | `kea` (Kea DHCP) | `kea` |
| Config file (ISC) | `/etc/dhcp/dhcpd.conf` | `/etc/dhcp/dhcpd.conf` |
| Service | `isc-dhcp-server` | `dhcpd` |

## ISC DHCP Configuration

### Installation

```bash
# Ubuntu
sudo apt install -y isc-dhcp-server

# RHEL 9
sudo dnf install -y dhcp-server
```

### Configuration file: `/etc/dhcp/dhcpd.conf`

```dhcpd
# Global settings
default-lease-time 86400;        # 24 hours in seconds
max-lease-time 172800;           # 48 hours
authoritative;

# Specify the DNS server clients should use
option domain-name-servers 8.8.8.8, 1.1.1.1;
option domain-name "example.com";

# Subnet declaration
subnet 192.168.1.0 netmask 255.255.255.0 {
    range 192.168.1.100 192.168.1.200;
    option routers 192.168.1.1;
    option broadcast-address 192.168.1.255;
}

# Static assignment by MAC address
host fileserver {
    hardware ethernet 00:11:22:33:44:55;
    fixed-address 192.168.1.50;
    option host-name "fileserver";
}
```

### Configure the listening interface

```bash
# Ubuntu: /etc/default/isc-dhcp-server
# Specify which interface to listen on
sudo sed -i 's/INTERFACESv4=""/INTERFACESv4="eth0"/' /etc/default/isc-dhcp-server

# RHEL: specify in the service unit or command line
# /etc/sysconfig/dhcpd
# DHCPDARGS="eth0"
```

### Start and enable

```bash
# Ubuntu
sudo systemctl enable --now isc-dhcp-server
systemctl status isc-dhcp-server

# RHEL
sudo systemctl enable --now dhcpd
systemctl status dhcpd
```

### Firewall rules

```bash
# Ubuntu (UFW)
sudo ufw allow 67/udp    # DHCP server port

# RHEL (firewalld)
sudo firewall-cmd --add-service=dhcp --permanent
sudo firewall-cmd --reload
```

## Viewing Leases

```bash
# Current active leases
cat /var/lib/dhcp/dhcpd.leases       # Ubuntu
cat /var/lib/dhcpd/dhcpd.leases     # RHEL

# Active leases formatted
dhcp-lease-list     # requires parsing script or tool
```

## Troubleshooting

```bash
# Check service status and recent logs
systemctl status isc-dhcp-server    # Ubuntu
systemctl status dhcpd              # RHEL
journalctl -u dhcpd -n 50

# Verify configuration syntax
sudo dhcpd -t -cf /etc/dhcp/dhcpd.conf

# Capture DHCP traffic (DORA: Discover, Offer, Request, Acknowledge)
sudo tcpdump -i eth0 -nn port 67 or port 68

# Client-side: request a new lease
sudo dhclient -v eth0       # Ubuntu
sudo nmcli device modify eth0 ipv4.method auto  # RHEL
```

## Exercises

1. Configure ISC DHCP to assign addresses in the range 10.0.0.100–10.0.0.150 on a test VM. Verify a client receives a lease.
2. Add a static reservation for a test client by MAC address. Verify it always gets the same IP.
3. Use `tcpdump` to capture a complete DORA exchange.

## References

- [ISC DHCP Documentation](https://www.isc.org/dhcp/)
- [Ubuntu DHCP](https://ubuntu.com/server/docs/network-dhcp)
- [RHEL 9 DHCP](https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/9/html/managing_networking_infrastructure_services/providing-dhcp-services_networking-infrastructure-services)
