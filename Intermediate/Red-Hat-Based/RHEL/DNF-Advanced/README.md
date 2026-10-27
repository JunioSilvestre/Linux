# Advanced DNF Management — RHEL 9

**Level:** Intermediate
**Scope:** Red Hat-Based — RHEL 9
**Prerequisites:** [DNF Foundations](../../../../Foundations/Red-Hat-Based/RHEL/DNF/README.md)

## Purpose

Advanced DNF topics: module streams, group management, custom repositories, subscription management, and transaction history.

## Transaction History

```bash
# Show transaction history
dnf history

# Show details of a transaction
dnf history info 5

# Undo a transaction (rollback)
sudo dnf history undo 5

# Redo a rolled-back transaction
sudo dnf history redo 5
```

## DNF Groups

```bash
# List available groups
dnf group list
dnf group list --available
dnf group list --installed

# Show group details
dnf group info "Development Tools"

# Install a group
sudo dnf group install "Development Tools"

# Remove a group
sudo dnf group remove "Development Tools"
```

## RHEL Subscription Management

```bash
# Register with Red Hat (RHEL only, not Rocky/Alma)
sudo subscription-manager register --username=<user> --password=<password>

# List available subscriptions
sudo subscription-manager list --available

# Attach a subscription
sudo subscription-manager attach --auto

# Enable repositories
sudo subscription-manager repos --list
sudo subscription-manager repos --enable rhel-9-for-x86_64-baseos-rpms
sudo subscription-manager repos --enable rhel-9-for-x86_64-appstream-rpms
```

## References

- [RHEL 9 Subscription Management](https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/9/html/managing_systems_by_using_the_rhel_web_console/managing-subscriptions-in-the-web-console_system-management-using-the-rhel-web-console)
- `man dnf`
- `man subscription-manager`
