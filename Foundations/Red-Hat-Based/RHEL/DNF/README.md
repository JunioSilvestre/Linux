# DNF Package Management — RHEL 9

**Level:** Foundations
**Scope:** Red Hat-Based — RHEL 9, Rocky Linux 9, AlmaLinux 9
**Prerequisites:** [CLI Fundamentals](../../../Cross-Distribution/CLI/README.md)

## Purpose

DNF (Dandified YUM) is the package manager for Red Hat-based systems starting with RHEL 8. This guide covers package management on RHEL 9 and compatible distributions. Commands differ significantly from APT on Debian/Ubuntu.

## Distribution Notes

| Distribution | DNF behavior | Notes |
|---|---|---|
| RHEL 9 | Identical | Requires valid subscription for some repositories |
| Rocky Linux 9 | Identical | Community RHEL rebuild, no subscription required |
| AlmaLinux 9 | Identical | Community RHEL rebuild, no subscription required |
| Fedora | Similar, different defaults | Bleeding edge; packages differ |

## Package Index

```bash
# Check for updates (does not install)
dnf check-update

# List available updates
dnf list updates
```

## Installing Packages

```bash
# Install a package
sudo dnf install nginx

# Install without confirmation
sudo dnf install -y nginx

# Install a specific version
sudo dnf install 'nginx-1.20.1'

# Install a local RPM file
sudo dnf install ./package.rpm
sudo dnf localinstall ./package.rpm   # equivalent

# Install from URL
sudo dnf install https://example.com/package.rpm

# Install a package group
sudo dnf group install "Development Tools"
sudo dnf groupinstall "Server with GUI"  # equivalent
```

## Upgrading

```bash
# Upgrade all packages
sudo dnf upgrade

# Upgrade a single package
sudo dnf upgrade nginx

# Check what will be upgraded without doing it
sudo dnf upgrade --assumeno
sudo dnf upgrade -n   # equivalent
```

## Removing Packages

```bash
# Remove a package
sudo dnf remove nginx

# Remove a package group
sudo dnf group remove "Development Tools"

# Remove unused dependencies
sudo dnf autoremove

# Clean all cached data
sudo dnf clean all
sudo dnf clean packages   # cached RPMs only
sudo dnf clean metadata   # cached metadata only
```

## Searching and Inspecting

```bash
# Search by name or summary
dnf search nginx

# Search all metadata (slower but thorough)
dnf search all nginx

# Show package details
dnf info nginx

# List installed packages
dnf list installed
dnf list installed | grep nginx

# Find which package provides a command or file
dnf provides /usr/sbin/nginx
dnf provides '*/sshd'

# List files installed by a package
rpm -ql nginx

# Find which package owns a file
rpm -qf /usr/sbin/nginx
dnf provides /usr/sbin/nginx

# Show package dependencies
dnf repoquery --requires nginx
dnf repoquery --whatrequires nginx   # reverse
```

## Repositories

```bash
# List configured repositories
dnf repolist
dnf repolist all      # include disabled repos
dnf repolist enabled  # only enabled repos

# Repository files location
ls /etc/yum.repos.d/

# Enable/disable a repository for the current command
sudo dnf install --enablerepo=crb nginx    # CRB = CodeReady Builder
sudo dnf install --disablerepo=appstream nginx

# Enable/disable a repo permanently
sudo dnf config-manager --enable crb
sudo dnf config-manager --disable crb

# Add the EPEL repository (common for RHEL)
sudo dnf install epel-release    # Rocky/Alma
# For RHEL (requires subscription):
sudo subscription-manager repos --enable codeready-builder-for-rhel-9-x86_64-rpms
sudo dnf install https://dl.fedoraproject.org/pub/epel/epel-release-latest-9.noarch.rpm

# Add a custom repository
sudo tee /etc/yum.repos.d/myrepo.repo << 'REPO'
[myrepo]
name=My Custom Repository
baseurl=https://repo.example.com/rhel9/
enabled=1
gpgcheck=1
gpgkey=https://repo.example.com/RPM-GPG-KEY
REPO
sudo dnf update
```

## RPM: Low-Level Package Tool

```bash
# Query installed package info
rpm -qi nginx

# List files installed by a package
rpm -ql nginx

# Find which package owns a file
rpm -qf /usr/sbin/nginx

# Verify package integrity
rpm -V nginx
# Output: missing (missing file), M (permissions changed), 5 (checksum mismatch)

# Import a GPG key
sudo rpm --import https://example.com/RPM-GPG-KEY
```

## Locking Package Versions

```bash
# Install version-lock plugin
sudo dnf install python3-dnf-plugin-versionlock

# Lock a package at its current version
sudo dnf versionlock add nginx

# List locked packages
dnf versionlock list

# Remove a lock
sudo dnf versionlock delete nginx
```

## Module Streams (RHEL 9)

Modules allow installing different versions of a package (e.g., Python 3.9 vs 3.11).

```bash
# List available modules
dnf module list
dnf module list nodejs

# Enable a specific module stream
sudo dnf module enable nodejs:20

# Install from a module
sudo dnf module install nodejs:20

# Show active module information
dnf module info nodejs

# Reset a module to default
sudo dnf module reset nodejs
```

## Exercises

1. Install `tree`. Use `rpm -ql tree` to list all installed files. Remove it with `dnf remove`. Verify the files are gone.
2. Use `dnf provides` to find which package provides the `ss` command.
3. Add the EPEL repository and install `htop`. Verify it is working.
4. Lock the `kernel` package version and verify the lock is applied.

## References

- `man dnf`
- `man rpm`
- [RHEL 9 Managing software with DNF](https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/9/html/managing_software_with_the_dnf_tool/)
- [EPEL documentation](https://docs.fedoraproject.org/en-US/epel/)
