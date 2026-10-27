# DNS — Domain Name System

**Domain:** Services
**Prerequisites:** [Host Networking](../../Intermediate/Cross-Distribution/Networking/README.md)
**Distributions:** Ubuntu 22.04/24.04, RHEL 9

## Purpose

Configure, operate, and troubleshoot a DNS server using BIND9. Covers authoritative name service, recursive resolution, zone configuration, firewall requirements, and validation.

## Distribution Differences

| Aspect | Ubuntu | RHEL 9 |
|---|---|---|
| Package | `bind9` | `bind` |
| Service name | `named` | `named` |
| Config dir | `/etc/bind/` | `/etc/named.conf`, `/etc/named/` |
| Zone dir | `/var/lib/bind/` | `/var/named/` |
| SELinux | No | Yes — requires correct labels |

## Installation

```bash
# Ubuntu
sudo apt install -y bind9 bind9utils bind9-doc

# RHEL 9
sudo dnf install -y bind bind-utils
```

## Core Concepts

- **Authoritative server:** Holds the definitive records for a zone. Returns definitive answers.
- **Recursive resolver:** Queries other servers on behalf of clients. Not authoritative.
- **Zone:** A portion of the DNS namespace managed by a server (e.g., `example.com`).
- **Record types:**
  - `A` — IPv4 address
  - `AAAA` — IPv6 address
  - `CNAME` — Canonical name (alias)
  - `MX` — Mail exchanger
  - `NS` — Name server
  - `PTR` — Reverse lookup
  - `SOA` — Start of Authority
  - `TXT` — Text record (SPF, DKIM, verification)

## Configuration: Ubuntu

Primary config: `/etc/bind/named.conf.options`

```named
options {
    directory "/var/cache/bind";

    // Allow recursive queries only from trusted clients
    recursion yes;
    allow-recursion { 127.0.0.1; 10.0.0.0/8; };

    // Listen on specific interfaces
    listen-on { 127.0.0.1; 10.0.0.1; };
    listen-on-v6 { ::1; };

    // Do not allow zone transfers to arbitrary hosts
    allow-transfer { none; };

    // Query forwarding (forward unresolved queries to upstream)
    forwarders { 8.8.8.8; 1.1.1.1; };
    forward only;

    // DNSSEC
    dnssec-validation auto;
};
```

### Adding a zone (Ubuntu)

`/etc/bind/named.conf.local`:

```named
zone "example.com" {
    type master;
    file "/var/lib/bind/example.com.zone";
    allow-transfer { none; };
};

zone "0.0.10.in-addr.arpa" {
    type master;
    file "/var/lib/bind/10.0.0.rev";
};
```

### Zone file

`/var/lib/bind/example.com.zone`:

```dns-zone
$TTL 86400
@   IN  SOA ns1.example.com. admin.example.com. (
            2024101501  ; Serial (YYYYMMDDnn)
            3600        ; Refresh
            1800        ; Retry
            604800      ; Expire
            86400 )     ; Minimum TTL

; Name servers
@   IN  NS  ns1.example.com.
@   IN  NS  ns2.example.com.

; A records
ns1     IN  A   10.0.0.1
ns2     IN  A   10.0.0.2
www     IN  A   10.0.0.10
mail    IN  A   10.0.0.20

; MX record
@   IN  MX  10  mail.example.com.

; CNAME
ftp     IN  CNAME   www.example.com.
```

```bash
# Set correct ownership
sudo chown root:bind /var/lib/bind/example.com.zone
sudo chmod 640 /var/lib/bind/example.com.zone

# Validate zone file syntax before restarting
sudo named-checkzone example.com /var/lib/bind/example.com.zone

# Validate named.conf syntax
sudo named-checkconf

# Start and enable
sudo systemctl enable --now named

# Reload after config changes (no service interruption)
sudo rndc reload
sudo systemctl reload named
```

## Configuration: RHEL 9

Primary config: `/etc/named.conf`

```named
options {
    listen-on port 53 { 127.0.0.1; 10.0.0.1; };
    listen-on-v6 port 53 { ::1; };
    directory   "/var/named";
    dump-file   "/var/named/data/cache_dump.db";
    statistics-file "/var/named/data/named_stats.txt";
    memstatistics-file "/var/named/data/named_mem_stats.txt";
    recursion yes;
    allow-recursion { 127.0.0.1; 10.0.0.0/8; };
    allow-transfer { none; };
    dnssec-validation yes;
};

zone "example.com" IN {
    type master;
    file "example.com.zone";
    allow-update { none; };
};
```

Zone file location on RHEL: `/var/named/example.com.zone`

```bash
# Validate config
sudo named-checkconf /etc/named.conf
sudo named-checkzone example.com /var/named/example.com.zone

# SELinux: set correct context for zone files
sudo restorecon -Rv /var/named/

# Firewall
sudo firewall-cmd --add-service=dns --permanent
sudo firewall-cmd --reload

# Enable and start
sudo systemctl enable --now named
```

## Firewall Rules

```bash
# Ubuntu (UFW)
sudo ufw allow 53/tcp
sudo ufw allow 53/udp

# RHEL (firewalld)
sudo firewall-cmd --add-service=dns --permanent
sudo firewall-cmd --reload
```

## Testing and Validation

```bash
# Query your DNS server directly
dig @10.0.0.1 www.example.com
dig @10.0.0.1 www.example.com A
dig @10.0.0.1 example.com MX
dig @10.0.0.1 example.com NS
dig @10.0.0.1 -x 10.0.0.10        # reverse lookup

# Check SOA (useful to verify serial after zone update)
dig @10.0.0.1 example.com SOA

# Check DNSSEC
dig @10.0.0.1 example.com +dnssec

# Verify the service is listening
ss -tlnup | grep ':53'
```

## Security Considerations

- Never run BIND as root. On Ubuntu it runs as `bind`; on RHEL as `named`.
- Restrict `allow-recursion` to known client networks — open recursion enables DNS amplification attacks.
- Disable `allow-transfer { any; }` — only allow zone transfers to authoritative secondaries.
- Use `rndc` for runtime management instead of restarting the service.
- Keep BIND updated: it has historically had critical CVEs.
- On RHEL, verify SELinux context: `ls -lZ /var/named/`

## Troubleshooting

| Symptom | Check | Command |
|---|---|---|
| Service won't start | Config syntax error | `named-checkconf` |
| Zone not loading | Zone file syntax error | `named-checkzone zone file` |
| Query returns SERVFAIL | Forwarder unreachable | `dig @forwarder example.com` |
| Clients cannot reach server | Firewall blocking | `ss -tlnup \| grep 53` |
| RHEL SELinux denial | Wrong file context | `ausearch -m avc \| grep named` |

```bash
# View named logs
journalctl -u named -f
journalctl -u bind9 -f     # Ubuntu

# Enable query logging (temporarily — high volume on busy resolvers)
# Add to named.conf options:
# querylog yes;
sudo rndc querylog on
sudo rndc querylog off     # disable when done
```

## Rollback

```bash
# Restore original config
sudo cp /etc/bind/named.conf.options.bak /etc/bind/named.conf.options
sudo named-checkconf
sudo systemctl restart named
```

## Practical Exercises

1. Configure a BIND9 authoritative server for `lab.local`. Add A, MX, and CNAME records. Validate with `dig`.
2. Add a second zone and verify zone transfer is blocked from unauthorized hosts.
3. Enable query logging. Run several lookups and trace them in the log.
4. Simulate a misconfigured zone file (syntax error). Verify that `named-checkzone` catches it before restart.

## References

- [BIND9 Administrator Reference Manual](https://bind9.readthedocs.io/)
- [Ubuntu DNS configuration](https://ubuntu.com/server/docs/dns-introduction)
- [RHEL 9 Setting up BIND](https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/9/html/managing_networking_infrastructure_services/assembly_setting-up-and-configuring-a-bind-dns-server_networking-infrastructure-services)
- `man named.conf`
- `man dig`
