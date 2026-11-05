# Advanced Linux Administration — Ubuntu (Debian-Based)

**Level:** Advanced  
**Target:** Ubuntu 22.04 LTS / 24.04 LTS  
**Prerequisites:** [Intermediate Ubuntu](../../../Intermediate/Debian-Based/Ubuntu/UFW/README.md), [Linux Foundations](../../../Foundations/README.md)

## Enterprise Topics

### 1. Kernel Parameter Optimization (sysctl)
Configure enterprise sysctl parameters for high-throughput network and memory performance:
```bash
sudo tee /etc/sysctl.d/99-enterprise-tuning.conf << 'CONF'
# Network performance tuning
net.core.somaxconn = 65535
net.ipv4.tcp_max_syn_backlog = 65535
net.ipv4.tcp_fin_timeout = 15
net.ipv4.tcp_tw_reuse = 1
net.ipv4.ip_local_port_range = 1024 65535

# Memory and Swappiness
vm.swappiness = 10
vm.dirty_ratio = 15
vm.dirty_background_ratio = 5
vm.vfs_cache_pressure = 50
CONF

sudo sysctl --system
```

### 2. AppArmor Deep Dive & Profile Enforcement
Ubuntu uses AppArmor as its default MAC (Mandatory Access Control) mechanism.
- Check enforcement status: `sudo aa-status`
- Enforce mode for a profile: `sudo aa-enforce /etc/apparmor.d/usr.sbin.nginx`
- Complain (audit) mode: `sudo aa-complain /etc/apparmor.d/usr.sbin.nginx`
- View AppArmor denial logs: `sudo dmesg | grep -i apparmor` or `sudo journalctl -k | grep -i apparmor`

### 3. Livepatch & Kernel Management
Canonical Livepatch allows kernel security patching without immediate reboot:
```bash
sudo snap install canonical-livepatch
sudo canonical-livepatch enable <YOUR_TOKEN>
canonical-livepatch status --verbose
```
