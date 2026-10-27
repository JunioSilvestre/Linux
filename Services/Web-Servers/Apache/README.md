# Apache HTTP Server Enterprise Administration

**Domain:** Services / Web-Servers  
**Distributions:** Ubuntu 22.04/24.04 (`apache2`), RHEL 9 (`httpd`)

## 1. Installation & Service Management

### Ubuntu (apache2)
```bash
sudo apt update && sudo apt install -y apache2
sudo systemctl enable --now apache2
sudo systemctl status apache2
```

### RHEL 9 (httpd)
```bash
sudo dnf install -y httpd
sudo systemctl enable --now httpd
sudo firewall-cmd --permanent --add-service=http --add-service=https
sudo firewall-cmd --reload
```

## 2. Hardened VirtualHost Configuration (TLS 1.3)
```apache
<VirtualHost *:443>
    ServerName app.corp.internal
    ServerAdmin admin@corp.internal
    DocumentRoot /var/www/app/public

    SSLEngine on
    SSLCertificateFile /etc/ssl/certs/app.corp.internal.crt
    SSLCertificateKeyFile /etc/ssl/private/app.corp.internal.key
    SSLProtocol all -SSLv3 -TLSv1 -TLSv1.1 -TLSv1.2
    SSLCipherSuite HIGH:!aNULL:!MD5:!3DES

    Header always set X-Content-Type-Options "nosniff"
    Header always set X-Frame-Options "DENY"
    Header always set X-XSS-Protection "1; mode=block"
    Header always set Strict-Transport-Security "max-age=63072000; includeSubDomains; preload"

    <Directory /var/www/app/public>
        AllowOverride None
        Require all granted
        Options -Indexes -FollowSymLinks
    </Directory>

    ErrorLog ${APACHE_LOG_DIR}/app_error.log
    CustomLog ${APACHE_LOG_DIR}/app_access.log combined
</VirtualHost>
```

## 3. Security Hardening Directives
In `/etc/apache2/conf-available/security.conf` (Ubuntu) or `/etc/httpd/conf.d/security.conf` (RHEL):
```apache
ServerTokens Prod
ServerSignature Off
TraceEnable Off
```
