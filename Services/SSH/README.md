# SSH — OpenSSH Administration

**Domain:** Services
**Prerequisites:** [Permissions](../../Foundations/Cross-Distribution/Permissions/README.md)
**Distributions:** Ubuntu 22.04/24.04, RHEL 9

## Purpose

Administer OpenSSH: key-based authentication, server hardening, client configuration, and troubleshooting. SSH is the primary remote access method for Linux servers — correct configuration is a security requirement, not optional.

## Distribution Differences

| Aspect | Ubuntu | RHEL 9 |
|---|---|---|
| Package | `openssh-server` | `openssh-server` |
| Service name | `ssh` | `sshd` |
| Config file | `/etc/ssh/sshd_config` | `/etc/ssh/sshd_config` |
| Drop-in dir | `/etc/ssh/sshd_config.d/` | `/etc/ssh/sshd_config.d/` |
| SELinux port | N/A | Must be labeled if non-standard |

## Key-Based Authentication Setup

### On the client (generate key pair)

```bash
# Generate Ed25519 key (recommended — modern, secure, compact)
ssh-keygen -t ed25519 -C "user@hostname-$(date +%Y%m%d)"

# RSA 4096 if Ed25519 is not supported by the target
ssh-keygen -t rsa -b 4096 -C "user@hostname"

# Keys are stored in:
# ~/.ssh/id_ed25519      (private key — protect this)
# ~/.ssh/id_ed25519.pub  (public key — safe to share)

# Permissions on .ssh directory (required)
chmod 700 ~/.ssh
chmod 600 ~/.ssh/id_ed25519
chmod 644 ~/.ssh/id_ed25519.pub
```

### On the server (authorize the client key)

```bash
# Method 1: ssh-copy-id (simplest)
ssh-copy-id -i ~/.ssh/id_ed25519.pub user@server

# Method 2: manual
ssh user@server "mkdir -p ~/.ssh && chmod 700 ~/.ssh"
cat ~/.ssh/id_ed25519.pub | ssh user@server "tee -a ~/.ssh/authorized_keys && chmod 600 ~/.ssh/authorized_keys"

# Verify the key was added
ssh user@server cat ~/.ssh/authorized_keys
```

### Test key-based authentication

```bash
# Connect using a specific key
ssh -i ~/.ssh/id_ed25519 user@server

# Verbose output for debugging
ssh -v user@server
ssh -vvv user@server    # maximum verbosity
```

## Server Hardening Configuration

> Always test that you can still connect with your key before closing the current session.

`/etc/ssh/sshd_config.d/99-hardening.conf` (preferred — drop-in, survives package updates):

```sshd
# Authentication
PermitRootLogin no
PasswordAuthentication no
PubkeyAuthentication yes
AuthenticationMethods publickey
PermitEmptyPasswords no
ChallengeResponseAuthentication no

# Connection limits
MaxAuthTries 3
MaxSessions 5
LoginGraceTime 20

# Session keepalive
ClientAliveInterval 300
ClientAliveCountMax 2

# Disable unnecessary features
AllowTcpForwarding no
X11Forwarding no
AllowAgentForwarding no
PrintMotd no

# Restrict access to specific users (optional)
# AllowUsers alice bob ops-team
# AllowGroups sshusers

# Secure algorithms
KexAlgorithms curve25519-sha256,diffie-hellman-group16-sha512
Ciphers aes256-gcm@openssh.com,chacha20-poly1305@openssh.com
MACs hmac-sha2-256,hmac-sha2-512
HostKeyAlgorithms ssh-ed25519,rsa-sha2-512
```

```bash
# Validate configuration syntax (BEFORE restarting)
sudo sshd -t
echo "Config is valid: $?"

# Show effective configuration (all settings including defaults)
sudo sshd -T

# Restart service
sudo systemctl restart ssh     # Ubuntu
sudo systemctl restart sshd    # RHEL

# Verify from another terminal before closing current session
ssh -v user@server 'echo connected'
```

## Changing the SSH Port

```bash
# Step 1: Add new port to sshd config
echo "Port 2222" | sudo tee -a /etc/ssh/sshd_config.d/99-port.conf

# Step 2: Update firewall BEFORE restarting
# Ubuntu:
sudo ufw allow 2222/tcp
# RHEL:
sudo firewall-cmd --add-port=2222/tcp --permanent
sudo firewall-cmd --reload

# Step 3: On RHEL — add SELinux label for new port
sudo semanage port -a -t ssh_port_t -p tcp 2222

# Step 4: Validate and restart
sudo sshd -t
sudo systemctl restart sshd

# Step 5: Verify connection on new port before closing old session
ssh -p 2222 user@server 'echo connected on 2222'

# Step 6: Remove old port from firewall only after confirming new port works
sudo ufw delete allow 22/tcp     # Ubuntu
sudo firewall-cmd --remove-service=ssh --permanent && sudo firewall-cmd --reload  # RHEL
```

## SSH Client Configuration

`~/.ssh/config` — define connection profiles:

```sshconfig
# Default settings for all hosts
Host *
    ServerAliveInterval 60
    ServerAliveCountMax 3
    IdentityFile ~/.ssh/id_ed25519

# Production server
Host prod-web
    HostName 10.0.1.50
    User deploy
    Port 22
    IdentityFile ~/.ssh/deploy_ed25519

# Bastion/jump host
Host bastion
    HostName bastion.example.com
    User ops
    Port 2222

# Host behind bastion
Host internal-server
    HostName 192.168.10.20
    User admin
    ProxyJump bastion
```

```bash
# Use config-defined host
ssh prod-web
ssh internal-server    # automatically jumps through bastion

# Permissions required on config file
chmod 600 ~/.ssh/config
```

## SSH Agent

```bash
# Start agent
eval "$(ssh-agent -s)"

# Add key to agent (avoids typing passphrase every time)
ssh-add ~/.ssh/id_ed25519

# List keys in agent
ssh-add -l

# Remove all keys from agent
ssh-add -D
```

## Firewall Requirements

```bash
# Ubuntu (UFW)
sudo ufw allow ssh          # port 22
sudo ufw allow 2222/tcp     # custom port

# RHEL (firewalld)
sudo firewall-cmd --add-service=ssh --permanent
sudo firewall-cmd --add-port=2222/tcp --permanent
sudo firewall-cmd --reload
```

## Security Considerations

- **Never disable host key checking** in production. `StrictHostKeyChecking no` is acceptable only in controlled automation with known trusted hosts.
- **Rotate SSH keys** when team members leave. Audit `~/.ssh/authorized_keys` on all servers.
- **Use SSH certificate authority (CA)** for large environments — avoids the need to distribute individual public keys.
- **Log all SSH sessions:** ensure `/var/log/auth.log` (Ubuntu) or `/var/log/secure` (RHEL) is monitored.
- **Fail2ban** or firewall rate limiting reduces brute-force exposure.

## Troubleshooting

| Symptom | Probable Cause | Diagnostic |
|---|---|---|
| `Permission denied (publickey)` | Key not in authorized_keys or wrong permissions | `ssh -v user@server` |
| `Connection refused` | Service not running or port blocked | `systemctl status sshd; ss -tlnp \| grep ssh` |
| `Host key verification failed` | Server key changed (or MITM warning) | `ssh-keygen -R hostname` to clear old key |
| Auth works but slow | DNS reverse lookup timeout | Add `UseDNS no` to sshd config |
| RHEL: port change fails | SELinux not labeled | `semanage port -l \| grep ssh` |

```bash
# Debug server-side authentication
journalctl -u sshd -f      # RHEL
journalctl -u ssh -f       # Ubuntu

# Check permissions on server (common cause of key auth failure)
ls -la ~/.ssh/
stat ~/.ssh/authorized_keys
# authorized_keys must be: 600 (rw-------)
# .ssh directory must be: 700 (rwx------)
# Home directory must NOT be world-writable

# Test login with verbose output
ssh -vvv user@server 2>&1 | grep -E 'Offering|Accepted|denied|Failed'
```

## Exercises

1. Generate an Ed25519 key pair. Copy the public key to a test VM using `ssh-copy-id`. Verify you can log in without a password.
2. Apply the hardening configuration. Verify password authentication is rejected. Verify root login is rejected.
3. Configure `~/.ssh/config` with a jump host. Test connecting through it with `ssh -v`.
4. Change the SSH port on a test VM to 2222. Update the firewall and SELinux. Confirm the connection succeeds on the new port.

## References

- `man sshd_config`
- `man ssh_config`
- `man ssh-keygen`
- [OpenSSH documentation](https://www.openssh.com/manual.html)
- [Mozilla SSH Security Guidelines](https://infosec.mozilla.org/guidelines/openssh)
