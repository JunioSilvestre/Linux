# Web Servers — Nginx and Apache

**Domain:** Services
**Prerequisites:** [Firewall](../../Networking/Firewalls/README.md), [SSH](../SSH/README.md)
**Distributions:** Ubuntu 22.04/24.04, RHEL 9

## Contents

| Directory | Description |
|---|---|
| [Nginx](./Nginx/README.md) | High-performance web server and reverse proxy |
| [Apache](./Apache/README.md) | Apache HTTP Server (httpd) |

## Choosing Between Nginx and Apache

| Factor | Nginx | Apache |
|---|---|---|
| Architecture | Event-driven, non-blocking | Process/thread-based |
| Static files | Excellent performance | Good performance |
| Dynamic content | Via reverse proxy (PHP-FPM, etc.) | Via mod_php (embedded) or proxy |
| Configuration | Single flat config per server block | Per-directory .htaccess supported |
| US market preference | Preferred for new deployments | Legacy systems, cPanel environments |
| Reverse proxy | Native, widely used | Supported via mod_proxy |
