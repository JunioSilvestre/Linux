# Advanced Linux Administration — RHEL (Enterprise Linux)

**Level:** Advanced  
**Target:** RHEL 9 / Rocky Linux 9 / AlmaLinux 9  
**Prerequisites:** [Intermediate RHEL](../../../Intermediate/Red-Hat-Based/RHEL/Firewalld/README.md), [Foundations SELinux](../../../Foundations/Red-Hat-Based/RHEL/SELinux/README.md)

## Enterprise Topics

### 1. Tuned Profiles for Workload Optimization
RHEL includes `tuned` to automatically optimize kernel, I/O schedulers, and CPU power states for specific workloads.
```bash
# Check current profile
tuned-adm active

# List available tuned profiles
tuned-adm list

# Apply high-throughput low-latency profile for databases
sudo tuned-adm profile throughput-performance

# Verify applied settings
tuned-adm verify
```

### 2. SELinux Custom Policy & Port Binding
When services bind to non-standard ports, SELinux blocks them by default.
```bash
# Allow Nginx/Apache to bind to custom port 8088
sudo semanage port -a -t http_port_t -p tcp 8088
sudo semanage port -l | grep http_port_t

# Allow web server network connect (e.g. reverse proxy to upstream socket)
sudo setsebool -P httpd_can_network_connect 1

# Analyze SELinux AVC denials
sudo ausearch -m avc -ts recent
sudo ausearch -m avc -ts recent | audit2why
```

### 3. Stratis & VDO Storage (Virtual Data Optimizer)
Deduplication and compression for enterprise block devices:
```bash
sudo dnf install -y stratisd stratis-cli
sudo systemctl enable --now stratisd
sudo stratis pool create pool1 /dev/sdb
sudo stratis fs create pool1 fs1
```
