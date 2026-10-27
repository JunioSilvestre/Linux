# APT Package Management — Ubuntu

**Level:** Foundations
**Scope:** Debian-Based — Ubuntu 22.04 LTS, Ubuntu 24.04 LTS
**Prerequisites:** [CLI Fundamentals](../../../Cross-Distribution/CLI/README.md)

## Purpose

APT (Advanced Package Tool) is the package manager for Debian-based systems. This guide covers installing, updating, removing, and inspecting packages using `apt` (interactive) and `apt-get` (scripting-friendly).

## Package Index

```bash
# Update the local package index (list of available packages and versions)
# This does NOT install or upgrade anything
sudo apt update

# Show pending upgrades
apt list --upgradable
```

## Installing Packages

```bash
# Install one or more packages
sudo apt install nginx
sudo apt install curl wget git

# Install without confirmation prompt (for scripting)
sudo apt install -y nginx

# Install a specific version
sudo apt install nginx=1.24.0-1ubuntu2

# Reinstall a package (repair broken installation)
sudo apt reinstall nginx

# Install a local .deb file
sudo apt install ./package.deb
```

## Upgrading

```bash
# Upgrade all installed packages
sudo apt upgrade

# Upgrade and allow package removal/addition (handles dependency changes)
sudo apt full-upgrade

# Upgrade a single package
sudo apt install --only-upgrade nginx

# Do not reboot interactively (for servers)
sudo DEBIAN_FRONTEND=noninteractive apt upgrade -y
```

## Removing Packages

```bash
# Remove a package (preserve config files)
sudo apt remove nginx

# Remove a package AND its configuration files
sudo apt purge nginx

# Remove automatically installed dependencies that are no longer needed
sudo apt autoremove

# Remove all cached .deb files
sudo apt clean

# Remove outdated cached .deb files
sudo apt autoclean
```

## Searching and Inspecting

```bash
# Search for a package by name or description
apt search nginx
apt-cache search nginx

# Show package details
apt show nginx
apt-cache show nginx

# List installed packages
dpkg -l
dpkg -l | grep nginx
apt list --installed

# Show files installed by a package
dpkg -L nginx

# Find which package owns a file
dpkg -S /usr/sbin/nginx
which nginx | xargs dpkg -S

# Show package dependencies
apt-cache depends nginx
apt-cache rdepends nginx    # reverse: what depends on nginx?
```

## Repositories and Sources

```bash
# List configured repositories
cat /etc/apt/sources.list
ls /etc/apt/sources.list.d/

# Modern Ubuntu uses deb822 format in /etc/apt/sources.list.d/
cat /etc/apt/sources.list.d/ubuntu.sources    # Ubuntu 24.04+

# Add a PPA (Personal Package Archive)
sudo add-apt-repository ppa:ondrej/php
sudo apt update

# Add a repository manually (example: Docker)
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | \
  sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg

echo "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] \
  https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" | \
  sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

sudo apt update
```

## Holding Packages

```bash
# Prevent a package from being upgraded
sudo apt-mark hold nginx

# Allow a held package to be upgraded again
sudo apt-mark unhold nginx

# List held packages
apt-mark showhold
```

## dpkg: Low-Level Package Tool

```bash
# Install .deb directly
sudo dpkg -i package.deb

# Fix broken dependencies after dpkg install
sudo apt install -f

# Remove package
sudo dpkg -r package-name

# Purge package and configs
sudo dpkg -P package-name

# List all installed packages
dpkg -l

# Query package database
dpkg-query -l 'nginx*'
```

## Unattended Upgrades (Security Updates)

```bash
# Install unattended-upgrades
sudo apt install unattended-upgrades

# Configure (interactive)
sudo dpkg-reconfigure -plow unattended-upgrades

# Configuration file
sudo nano /etc/apt/apt.conf.d/50unattended-upgrades

# Test dry-run
sudo unattended-upgrades --dry-run --debug
```

## Exercises

1. Install `tree` using `apt`. Use `dpkg -L tree` to list every file it installed. Purge it and verify the files are gone.
2. Search for all packages related to "network monitoring". Install one and test it.
3. Use `dpkg -S` to find which package owns `/bin/ls`.
4. Configure automatic security updates using `unattended-upgrades`. Verify the configuration is syntactically valid.

## References

- `man apt`
- `man apt-get`
- `man dpkg`
- [Ubuntu APT documentation](https://help.ubuntu.com/community/AptGet/Howto)
- [Debian APT User's Guide](https://www.debian.org/doc/manuals/apt-guide/)
