# Linux Systems Engineering

<div align="center">

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](./LICENSE)
![Domain](https://img.shields.io/badge/Domain-Linux%20Systems%20Engineering-orange)
![Distributions](https://img.shields.io/badge/Distributions-Ubuntu%20%7C%20RHEL-blue)
![Standard](https://img.shields.io/badge/Standard-Production--Grade-success)

**A structured, progressive reference for Linux systems administration and engineering.**
Covers Ubuntu (Debian-based) and RHEL/Rocky/AlmaLinux (Red Hat-based) from foundational
concepts through expert-level incident response, reliability engineering, and infrastructure automation.

</div>

---

## Table of Contents

- [Project Purpose](#project-purpose)
- [Supported Systems](#supported-systems)
- [Repository Architecture](#repository-architecture)
- [Learning Progression](#learning-progression)
- [Technical Domains](#technical-domains)
- [Directory Navigation](#directory-navigation)
- [Running the Labs](#running-the-labs)
- [Automation and Testing Conventions](#automation-and-testing-conventions)
- [Safety Requirements](#safety-requirements)
- [Contribution Guidelines](#contribution-guidelines)
- [Official Documentation](#official-documentation)
- [Project Status](#project-status)

---

## Project Purpose

This repository is a professional reference and learning resource for Linux systems engineering. It provides:

- A structured progression from foundational to expert-level Linux administration.
- Distribution-specific documentation for Ubuntu and RHEL, with clear coverage differences.
- Reusable automation scripts and Ansible playbooks for operational tasks.
- Reproducible lab scenarios for practical skill development.
- Technical decision records, architecture notes, and operational runbooks.
- Troubleshooting guides organized by symptom and domain.

The content reflects real operational requirements, not synthetic tutorials. Every guide identifies its prerequisites, learning level, target distribution, and practical validation steps.

---

## Supported Systems

| Distribution Family | Specific Systems | Status |
|---|---|---|
| Debian-based | Ubuntu 22.04 LTS, Ubuntu 24.04 LTS | Active |
| Red Hat-based | RHEL 9, Rocky Linux 9, AlmaLinux 9 | Active |
| Cross-distribution | Concepts valid across both families | Active |

Where behavior differs between RHEL and related distributions (Rocky Linux, AlmaLinux, Fedora), the difference is documented explicitly.

---

## Repository Architecture

```
Linux/
├── Foundations/          # Core concepts: CLI, filesystem, permissions, processes
├── Intermediate/         # Service management, storage, scheduling, scripting
├── Advanced/             # Performance, boot recovery, security baselines
├── Expert/               # Incident response, reliability, capacity planning
├── Services/             # DNS, DHCP, Web, SSH, Time synchronization
├── Networking/           # Routing, VLANs, firewalls, VPN, diagnostics
├── Storage/              # LVM, RAID, NFS, filesystems, backup
├── Security/             # Hardening, SELinux, auditing
├── Automation/           # Bash, Python, Ansible
├── Troubleshooting/      # Symptom-based diagnostic guides
├── Labs/                 # Reproducible practical scenarios
└── docs/                 # Architecture, standards, decisions, runbooks
```

---

## Learning Progression

The four progression levels have distinct technical boundaries. They do not represent a simple count of commands.

| Level | Audience | Focus |
|---|---|---|
| [Foundations](./Foundations/README.md) | New to Linux | Core OS concepts, navigation, permissions, services |
| [Intermediate](./Intermediate/README.md) | Comfortable with the shell | Storage, scheduling, scripting, service administration |
| [Advanced](./Advanced/README.md) | Experienced administrator | Performance analysis, boot recovery, security baselines |
| [Expert](./Expert/README.md) | Senior engineer/SRE | Incident response, reliability, infrastructure design |

Each level contains a README that defines prerequisites, learning objectives, practical skills, exercises, and completion criteria.

---

## Technical Domains

Domain directories organize content by specialty area rather than learning level. They cross-reference the progression levels.

| Domain | Description |
|---|---|
| [Services](./Services/README.md) | DNS, DHCP, Nginx, Apache, SSH, Chrony — configuration, operations, security |
| [Networking](./Networking/README.md) | Routing, VLANs, firewalls, VPN, packet diagnostics |
| [Storage](./Storage/README.md) | LVM, RAID, NFS, filesystem administration, backup, recovery |
| [Security](./Security/README.md) | Hardening baselines, SELinux, auditing, privilege management |
| [Automation](./Automation/README.md) | Bash scripts, Python tools, Ansible playbooks |
| [Troubleshooting](./Troubleshooting/README.md) | Symptom-based guides: boot, performance, storage, network, services |

---

## Directory Navigation

### Find content by learning level

- New to Linux → [Foundations/Cross-Distribution/CLI](./Foundations/Cross-Distribution/CLI/README.md)
- Ubuntu package management → [Foundations/Debian-Based/Ubuntu/APT](./Foundations/Debian-Based/Ubuntu/APT/README.md)
- RHEL package management → [Foundations/Red-Hat-Based/RHEL/DNF](./Foundations/Red-Hat-Based/RHEL/DNF/README.md)
- Scheduling tasks → [Intermediate/Cross-Distribution/Scheduling](./Intermediate/Cross-Distribution/Scheduling/README.md)
- Performance analysis → [Advanced/Cross-Distribution/Performance](./Advanced/Cross-Distribution/Performance/README.md)
- Incident response → [Expert/Cross-Distribution/Incident-Response](./Expert/Cross-Distribution/Incident-Response/README.md)

### Find content by domain

- Configure BIND DNS → [Services/DNS](./Services/DNS/README.md)
- Configure Nginx → [Services/Web-Servers/Nginx](./Services/Web-Servers/Nginx/README.md)
- Configure SSH hardening → [Security/Hardening/SSH](./Security/Hardening/SSH/README.md)
- LVM operations → [Storage/LVM](./Storage/LVM/README.md)
- RAID configuration → [Storage/RAID](./Storage/RAID/README.md)
- Firewall rules → [Networking/Firewalls](./Networking/Firewalls/README.md)
- SELinux troubleshooting → [Security/SELinux](./Security/SELinux/README.md)
- Ansible automation → [Automation/Ansible](./Automation/Ansible/README.md)

### Find content by task

- Diagnose boot failure → [Troubleshooting/Boot](./Troubleshooting/Boot/README.md)
- Diagnose high CPU or memory → [Troubleshooting/Performance](./Troubleshooting/Performance/README.md)
- Diagnose disk issues → [Troubleshooting/Storage](./Troubleshooting/Storage/README.md)
- Diagnose network connectivity → [Troubleshooting/Network](./Troubleshooting/Network/README.md)
- CIS hardening audit lab → [Labs/CIS-Hardening-Audit](./Labs/CIS-Hardening-Audit/README.md)
- Secure web server lab → [Labs/Secure-Web-Server](./Labs/Secure-Web-Server/README.md)

---

## Running the Labs

Labs in [`Labs/`](./Labs/) are designed for local virtualization or containers. Requirements:

- **Virtualization:** VirtualBox, KVM/QEMU, or VMware Workstation with at least 2 vCPUs and 2 GB RAM per VM.
- **Containers:** Docker or Podman for service-level labs not requiring kernel-level features.
- **Network:** Host-only or NAT networking; no public internet exposure required.
- **Snapshots:** Take a VM snapshot before each lab step that modifies system state.

Each lab directory contains:
- A README with objectives, prerequisites, and setup instructions.
- Step-by-step execution with expected results.
- Validation commands and failure scenarios.
- Cleanup and rollback instructions.

Paid cloud infrastructure is not required. Where a cloud provider is used as an option, it is documented as optional.

---

## Automation and Testing Conventions

### Bash

- All scripts use `#!/usr/bin/env bash`.
- Consequential scripts use `set -euo pipefail`.
- Syntax validated with `bash -n script.sh`.
- Scripts support `--dry-run` or `--help` where applicable.

### Python

- Dependencies documented in `requirements.txt` or `pyproject.toml`.
- Type hints used throughout.
- Tests located in `tests/` subdirectories.
- No hardcoded paths or credentials.

### Ansible

- Playbooks are idempotent.
- Roles follow the standard `roles/<name>/{tasks,handlers,defaults,files,templates,meta}` layout.
- Validated with `ansible-playbook --syntax-check`.

---

## Safety Requirements

1. **No secrets in the repository.** Passwords, API keys, tokens, private keys, and real IP addresses must never be committed.
2. **No production risk in examples.** All destructive examples use loopback devices, virtual machines, or containers. Real disk device names (e.g., `/dev/sda`) are labeled as examples requiring substitution.
3. **No security-defeating shortcuts.** SELinux and firewalls are never disabled to resolve a service issue. The documentation explains correct diagnostic and remediation paths.
4. **Privilege scope documented.** Commands requiring elevated privileges identify the scope and risks.
5. **Reversibility documented.** Every consequential change documents the rollback or recovery path.

---

## Contribution Guidelines

See [CONTRIBUTING.md](./CONTRIBUTING.md) for naming conventions, content standards, commit message format, and the pull request process.

---

## Official Documentation

| Resource | URL |
|---|---|
| Ubuntu Documentation | <https://help.ubuntu.com/> |
| Ubuntu Server Guide | <https://ubuntu.com/server/docs> |
| RHEL 9 Documentation | <https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/9> |
| Rocky Linux Docs | <https://docs.rockylinux.org/> |
| AlmaLinux Wiki | <https://wiki.almalinux.org/> |
| systemd Documentation | <https://systemd.io/> |
| Ansible Documentation | <https://docs.ansible.com/> |
| Linux man-pages | <https://man7.org/linux/man-pages/> |
| CIS Benchmarks | <https://www.cisecurity.org/cis-benchmarks> |

---

## Project Status

| Area | Status |
|---|---|
| Foundations | Active — documented |
| Intermediate | Active — documented |
| Advanced | Active — documented |
| Expert | Active — documented |
| Services | Active — documented |
| Networking | Active — documented |
| Storage | Active — documented |
| Security | Active — documented |
| Automation | Active — documented |
| Troubleshooting | Active — documented |
| Labs | Active — documented |
| docs/ | Active — documented |

**Maintainer:** Junio Silvestre
**Repository:** <https://github.com/JunioSilvestre/Linux>
