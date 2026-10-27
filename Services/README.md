# Services

Infrastructure services: configuration, lifecycle, security, and troubleshooting.
Each subdirectory covers both Ubuntu and RHEL where behavior differs.

## Contents

| Directory | Service | Tools |
|---|---|---|
| [DNS](./DNS/README.md) | Domain Name System | BIND9, named, dig |
| [DHCP](./DHCP/README.md) | IP address assignment | ISC DHCP, Kea |
| [Web-Servers](./Web-Servers/README.md) | HTTP/HTTPS | Nginx, Apache |
| [SSH](./SSH/README.md) | Secure Shell | OpenSSH |
| [Time-Synchronization](./Time-Synchronization/README.md) | NTP | Chrony |

## Cross-References

- Firewall rules → [Networking/Firewalls](../Networking/Firewalls/README.md)
- Service hardening → [Security/Hardening](../Security/Hardening/README.md)
- Troubleshooting → [Troubleshooting/Services](../Troubleshooting/Services/README.md)
