# Nginx — Web Server and Reverse Proxy

**Domain:** Services / Web-Servers
**Prerequisites:** [Firewall](../../../Networking/Firewalls/README.md), [SSH](../../SSH/README.md)
**Distributions:** Ubuntu 22.04/24.04, RHEL 9

## Purpose

Configure, secure, and operate Nginx as a web server and reverse proxy. Covers virtual hosts, TLS, logging, and performance tuning.

## Installation

```bash
# Ubuntu — from Ubuntu repositories
sudo apt install -y nginx

# Ubuntu — from official Nginx repository (newer versions)
curl -fsSL https://nginx.org/keys/nginx_signing.key | \
  sudo gpg --dearmor -o /etc/apt/keyrings/nginx.gpg
echo "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/nginx.gpg] \
  http://nginx.org/packages/ubuntu $(lsb_release -cs) nginx" | \
  sudo tee /etc/apt/sources.list.d/nginx.list
sudo apt update && sudo apt install -y nginx

# RHEL 9
sudo dnf install -y nginx

# Enable and start
sudo systemctl enable --now nginx
```

## Directory Layout

```
# Ubuntu
/etc/nginx/
├── nginx.conf              # global configuration
├── sites-available/        # defined virtual hosts
├── sites-enabled/          # symlinks to active hosts
├── conf.d/                 # additional configuration files
└── modules-enabled/        # enabled modules

# RHEL 9
/etc/nginx/
├── nginx.conf              # global configuration
├── conf.d/                 # virtual host configs (default.conf)
└── default.d/              # server block snippets
```

## Nginx Core Configuration

`/etc/nginx/nginx.conf`:

```nginx
user www-data;             # Ubuntu: www-data; RHEL: nginx
worker_processes auto;     # one per CPU core
error_log /var/log/nginx/error.log warn;
pid /run/nginx.pid;

events {
    worker_connections 1024;
    multi_accept on;
}

http {
    include /etc/nginx/mime.types;
    default_type application/octet-stream;

    log_format main '$remote_addr - $remote_user [$time_local] '
                    '"$request" $status $body_bytes_sent '
                    '"$http_referer" "$http_user_agent"';

    access_log /var/log/nginx/access.log main;
    sendfile on;
    tcp_nopush on;
    keepalive_timeout 65;
    gzip on;

    include /etc/nginx/conf.d/*.conf;
    include /etc/nginx/sites-enabled/*;  # Ubuntu only
}
```

## Virtual Host Configuration

### HTTP virtual host (Ubuntu: sites-available)

`/etc/nginx/sites-available/example.com`:

```nginx
server {
    listen 80;
    listen [::]:80;
    server_name example.com www.example.com;

    root /var/www/example.com/html;
    index index.html index.htm;

    access_log /var/log/nginx/example.com.access.log main;
    error_log /var/log/nginx/example.com.error.log warn;

    location / {
        try_files $uri $uri/ =404;
    }

    # Block access to hidden files
    location ~ /\. {
        deny all;
    }
}
```

```bash
# Enable the site (Ubuntu)
sudo ln -s /etc/nginx/sites-available/example.com /etc/nginx/sites-enabled/
sudo nginx -t
sudo systemctl reload nginx
```

### RHEL virtual host (conf.d)

Create `/etc/nginx/conf.d/example.com.conf` with the same content (no symlink needed).

```bash
sudo nginx -t
sudo systemctl reload nginx
```

### HTTPS with TLS

```nginx
server {
    listen 80;
    server_name example.com www.example.com;
    # Redirect all HTTP to HTTPS
    return 301 https://$host$request_uri;
}

server {
    listen 443 ssl http2;
    server_name example.com www.example.com;

    ssl_certificate /etc/ssl/certs/example.com.crt;
    ssl_certificate_key /etc/ssl/private/example.com.key;

    # Secure TLS settings
    ssl_protocols TLSv1.2 TLSv1.3;
    ssl_ciphers ECDHE-ECDSA-AES128-GCM-SHA256:ECDHE-RSA-AES128-GCM-SHA256:ECDHE-ECDSA-AES256-GCM-SHA384;
    ssl_prefer_server_ciphers off;
    ssl_session_timeout 1d;
    ssl_session_cache shared:SSL:50m;

    # HSTS (6 months)
    add_header Strict-Transport-Security "max-age=15768000" always;

    # Security headers
    add_header X-Content-Type-Options nosniff always;
    add_header X-Frame-Options DENY always;

    root /var/www/example.com/html;
    index index.html;

    location / {
        try_files $uri $uri/ =404;
    }
}
```

### Reverse proxy configuration

```nginx
server {
    listen 80;
    server_name app.example.com;

    location / {
        proxy_pass http://127.0.0.1:8080;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
        proxy_connect_timeout 30;
        proxy_send_timeout 60;
        proxy_read_timeout 60;
    }
}
```

## Validation and Operations

```bash
# Test configuration syntax (always before reload/restart)
sudo nginx -t
sudo nginx -T    # dump effective configuration

# Reload without dropping connections
sudo systemctl reload nginx

# Restart (drops active connections)
sudo systemctl restart nginx

# Check process and worker count
ps aux | grep nginx

# Watch access log live
sudo tail -f /var/log/nginx/access.log

# Watch error log live
sudo tail -f /var/log/nginx/error.log

# Check open files and connections
sudo nginx -V                          # compile options and modules
sudo ss -tlnp | grep nginx             # listening ports
```

## Firewall Rules

```bash
# Ubuntu (UFW)
sudo ufw allow 'Nginx Full'     # allows 80 and 443
sudo ufw allow 80/tcp
sudo ufw allow 443/tcp

# RHEL (firewalld)
sudo firewall-cmd --add-service=http --permanent
sudo firewall-cmd --add-service=https --permanent
sudo firewall-cmd --reload

# RHEL — SELinux: allow nginx to connect to upstream
sudo setsebool -P httpd_can_network_connect 1
```

## Security Considerations

- Run Nginx as a non-root user (`www-data` on Ubuntu, `nginx` on RHEL).
- Use TLS 1.2 and 1.3 only. Disable TLS 1.0 and 1.1.
- Set security headers: `X-Frame-Options`, `X-Content-Type-Options`, `Strict-Transport-Security`.
- Do not expose version information: `server_tokens off;` in nginx.conf http block.
- Restrict access to sensitive paths (`/admin`, `/.git`, `/.env`).
- On RHEL: configure SELinux booleans for reverse proxy scenarios.

## Troubleshooting

| Symptom | Check | Command |
|---|---|---|
| 502 Bad Gateway | Upstream not running | `systemctl status upstream-service` |
| 403 Forbidden | Permissions on web root | `ls -la /var/www/`; `nginx -T \| grep root` |
| Config won't load | Syntax error | `nginx -t` |
| RHEL SELinux block | Boolean not set | `ausearch -m avc \| grep nginx` |
| SSL handshake fails | Certificate path wrong | `nginx -T \| grep ssl_certificate` |

## Exercises

1. Configure two virtual hosts (`site1.local` and `site2.local`) on the same server. Verify each serves different content.
2. Add HTTPS with a self-signed certificate. Verify with `curl -k https://site1.local`.
3. Configure a reverse proxy for a simple Python HTTP server (`python3 -m http.server 8080`).
4. Add rate limiting: `limit_req_zone` for `/login`. Test that repeated requests are throttled.

## References

- [Nginx Documentation](https://nginx.org/en/docs/)
- [Mozilla SSL Configuration Generator](https://ssl-config.mozilla.org/)
- [Ubuntu Nginx](https://ubuntu.com/server/docs/how-to-install-nginx)
- [RHEL 9 Setting up Nginx](https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/9/html/deploying_web_servers_and_reverse_proxies/setting-up-and-configuring-nginx_deploying-web-servers-and-reverse-proxies)
