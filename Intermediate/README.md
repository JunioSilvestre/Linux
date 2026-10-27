# Intermediate Linux Administration

This level builds on Foundations. The focus is operational administration: managing services, storage, users, scheduled tasks, scripting, SSH, and networking in a real environment.

## Prerequisites

- Comfortable navigating the filesystem and working with files from the CLI.
- Able to install packages and manage services with systemd.
- Understand file permissions and basic user accounts.
- Equivalent to completing all [Foundations](../Foundations/README.md) topics.

## Learning Objectives

1. Configure and manage disks: partition, format, mount, and make mounts persistent.
2. Manage LVM volumes: create, extend, shrink, snapshot.
3. Manage users, groups, sudo policies, and access boundaries.
4. Schedule tasks with cron and systemd timers.
5. Administer SSH: key-based authentication, configuration hardening.
6. Configure host networking and name resolution.
7. Write operational Bash scripts with error handling.
8. Perform and validate system backups.
9. Manage service dependencies and diagnose startup failures.
10. Read and interpret system logs systematically.

## Required Practical Skills

- Extend a filesystem online without data loss.
- Diagnose why a service fails to start.
- Write a Bash script that validates its inputs and handles errors.
- Configure a cron job and verify it runs.
- Set up SSH key authentication and disable password login.

## Structure

| Directory | Scope | Description |
|---|---|---|
| [Cross-Distribution/Scheduling](./Cross-Distribution/Scheduling/README.md) | All | cron, at, systemd timers |
| [Cross-Distribution/Networking](./Cross-Distribution/Networking/README.md) | All | Host networking, name resolution |
| [Cross-Distribution/Storage](./Cross-Distribution/Storage/README.md) | All | Partitioning, filesystems, LVM, mounts |
| [Cross-Distribution/Backup](./Cross-Distribution/Backup/README.md) | All | rsync, tar, backup strategy |
| [Debian-Based/Ubuntu/APT-Advanced](./Debian-Based/Ubuntu/APT-Advanced/README.md) | Ubuntu | Repository management, pinning, PPAs |
| [Debian-Based/Ubuntu/UFW](./Debian-Based/Ubuntu/UFW/README.md) | Ubuntu | Host firewall with UFW |
| [Red-Hat-Based/RHEL/DNF-Advanced](./Red-Hat-Based/RHEL/DNF-Advanced/README.md) | RHEL | Modules, groups, custom repos |
| [Red-Hat-Based/RHEL/Firewalld](./Red-Hat-Based/RHEL/Firewalld/README.md) | RHEL | Host firewall with firewalld |

## Next Level

→ [Advanced](../Advanced/README.md)
