# Foundations

This level covers the core concepts required to work confidently with any Linux system. Content is organized by whether it applies to all distributions (Cross-Distribution) or is specific to a distribution family.

## Prerequisites

- Access to a Linux system (physical, VM, container, or WSL2).
- Ability to open a terminal and run basic commands.
- No prior Linux experience required.

## Learning Objectives

By completing this level, you will be able to:

1. Navigate the filesystem confidently using the CLI.
2. Understand and apply the Linux filesystem hierarchy.
3. Create, move, copy, delete, and link files and directories.
4. Read and modify file ownership and permissions, including ACLs.
5. Inspect and manage running processes and system resources.
6. Configure environment variables and shell startup files.
7. Install, update, and remove packages using the distribution's package manager.
8. Start, stop, enable, and inspect systemd services and targets.
9. Read system logs using journalctl and traditional log files.
10. Create, modify, and remove user and group accounts.

## Required Practical Skills

- Execute commands using pipes, redirection, and command substitution.
- Find files using `find` and `locate`.
- Read and write text files with `cat`, `less`, `nano`, and `vim`.
- Set and use environment variables.
- Read `man` pages and `--help` output.

## Recommended Exercises

1. Navigate the filesystem to `/proc`, `/sys`, `/etc`, `/var`, and `/tmp`. Describe the purpose of each.
2. Create a file hierarchy, set permissions recursively, and verify with `ls -la` and `getfacl`.
3. Launch a background process, inspect it with `ps` and `top`, and terminate it with a signal.
4. Install a package, inspect what it installed, start its service, and verify it with `systemctl status`.
5. Create a user, add them to a group, test sudo access, and then remove them.

## Completion Criteria

- You can explain the purpose of each standard directory in `/` without looking at notes.
- You can determine why a user cannot access a file and correct the permissions without trial and error.
- You can identify, inspect, and manage any running process.
- You can install a package, start its service, and read its logs without guidance.

## Structure

| Directory | Scope | Description |
|---|---|---|
| [Cross-Distribution/CLI](./Cross-Distribution/CLI/README.md) | All | Shell navigation, command composition, I/O |
| [Cross-Distribution/Filesystem](./Cross-Distribution/Filesystem/README.md) | All | FHS, file types, links |
| [Cross-Distribution/Permissions](./Cross-Distribution/Permissions/README.md) | All | Ownership, permissions, ACLs |
| [Cross-Distribution/Processes](./Cross-Distribution/Processes/README.md) | All | Processes, signals, jobs, resource inspection |
| [Debian-Based/Ubuntu/APT](./Debian-Based/Ubuntu/APT/README.md) | Ubuntu | Package management with APT |
| [Debian-Based/Ubuntu/systemd](./Debian-Based/Ubuntu/systemd/README.md) | Ubuntu | Service management with systemd |
| [Red-Hat-Based/RHEL/DNF](./Red-Hat-Based/RHEL/DNF/README.md) | RHEL 9 | Package management with DNF |
| [Red-Hat-Based/RHEL/SELinux](./Red-Hat-Based/RHEL/SELinux/README.md) | RHEL 9 | SELinux concepts and basic operations |
| [Red-Hat-Based/RHEL/systemd](./Red-Hat-Based/RHEL/systemd/README.md) | RHEL 9 | Service management with systemd on RHEL |

## Next Level

→ [Intermediate](../Intermediate/README.md)
