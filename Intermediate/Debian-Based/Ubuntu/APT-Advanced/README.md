# Advanced APT Management — Ubuntu

**Level:** Intermediate
**Scope:** Debian-Based — Ubuntu 22.04 LTS, Ubuntu 24.04 LTS
**Prerequisites:** [APT Foundations](../../../../Foundations/Debian-Based/Ubuntu/APT/README.md)

## Purpose

Advanced APT topics: repository configuration, package pinning, private repositories, and dependency management.

## Repository Configuration

### deb822 format (Ubuntu 24.04+)

`/etc/apt/sources.list.d/ubuntu.sources`:

```yaml
Types: deb
URIs: http://archive.ubuntu.com/ubuntu
Suites: noble noble-updates noble-backports
Components: main restricted universe multiverse
Signed-By: /usr/share/keyrings/ubuntu-archive-keyring.gpg
```

### One-line format (older Ubuntu)

```
deb http://archive.ubuntu.com/ubuntu jammy main restricted universe multiverse
deb-src http://archive.ubuntu.com/ubuntu jammy main restricted restricted universe multiverse
```

## Adding Repositories Securely

```bash
# Step 1: Download and store the GPG key
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | \
  sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg
sudo chmod a+r /etc/apt/keyrings/docker.gpg

# Step 2: Add repository with signed-by reference
echo "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] \
https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" | \
  sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

# Step 3: Update and install
sudo apt update
sudo apt install docker-ce
```

## Package Pinning

Pinning controls which package version or repository is preferred.

`/etc/apt/preferences.d/pin-nginx`:

```
# Prefer nginx from the official nginx repo over Ubuntu's
Package: nginx
Pin: origin nginx.org
Pin-Priority: 1000

# Pin a specific version
Package: nginx
Pin: version 1.25.*
Pin-Priority: 1001

# Prevent a package from being upgraded
Package: linux-image-*
Pin: release a=jammy
Pin-Priority: -1
```

```bash
# Show effective pin priorities
apt-cache policy nginx

# Install the pinned version
sudo apt install nginx
```

## Simulating Changes

```bash
# Simulate install without doing it
sudo apt install --simulate nginx
sudo apt install -s nginx

# Show what will change
sudo apt install --dry-run nginx
```

## References

- `man apt_preferences`
- `man sources.list`
- [Debian APT Preferences](https://wiki.debian.org/AptPreferences)
