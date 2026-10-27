# Contributing Guide

Thank you for your interest in contributing to this Linux Systems Engineering repository.

## Scope

This repository documents Linux systems administration, engineering, and operations across Debian-based (Ubuntu) and Red Hat-based (RHEL/Rocky/Alma) distributions. Contributions must be accurate, safe, and technically justified.

## Before You Contribute

1. Read the [README](./README.md) for the overall structure and learning progression.
2. Understand the [architecture document](./docs/architecture/README.md) before adding new directories.
3. Check existing documentation to avoid duplicating content. Link to it instead.

## Standards

### Language and Style

- Write all documentation, directory names, filenames, scripts, and comments in English.
- Use clear, precise technical language. Avoid marketing language.
- Use active voice. Prefer short sentences.
- Define acronyms on first use.

### Directory and File Naming

- Use `PascalCase` for top-level directories (e.g., `Foundations/`, `Services/`).
- Use `PascalCase` or `kebab-case` for subdirectories based on their type.
- Use `kebab-case` for filenames (e.g., `lvm-operations.md`).
- Shell scripts end with `.sh`; Python files end with `.py`.
- Every non-trivial directory must contain a `README.md`.

### Content Requirements

- Every guide must state: scope, learning level, supported distributions, and prerequisites.
- All commands must be explained. Do not list commands without context.
- Distinguish: read-only diagnostics, reversible changes, privileged operations, and destructive operations.
- Commands requiring `sudo` must explain the scope and risks.
- Never embed passwords, API keys, or real credentials.
- Use loopback devices, VM snapshots, or containers for destructive examples.
- Do not disable SELinux or firewalls to make a service work.

### Bash Scripts

- Use `#!/usr/bin/env bash` shebang.
- Apply `set -euo pipefail` for consequential scripts.
- Quote all variables: `"${variable}"`.
- Validate required inputs and provide usage/help.
- Provide meaningful exit codes.
- Support `--dry-run` for consequential operations where practical.
- Use `bash -n script.sh` to validate syntax before committing.

### Python Tools

- Include a `requirements.txt` or `pyproject.toml`.
- Use type hints (`def foo(x: int) -> str:`).
- Handle exceptions explicitly.
- Include automated tests in a `tests/` directory.
- No hardcoded paths or credentials.

### Configuration Files

- Label examples as examples, not production-ready configurations.
- State the distribution and version assumption.
- Validate with available native tools (e.g., `nginx -t`, `named-checkconf`).
- Include backup and rollback instructions.

## Commit Messages

Follow the Conventional Commits format:

```
<type>(<scope>): <short description>

[optional body]
[optional footer]
```

Types: `feat`, `fix`, `docs`, `refactor`, `test`, `chore`.

Examples:
```
docs(foundations): add filesystem hierarchy guide for Ubuntu 24.04
feat(automation): add idempotent user-provisioning bash script
fix(security): correct SELinux boolean for HTTPD file access
```

## Pull Request Process

1. Fork the repository and create a feature branch.
2. Follow all standards above.
3. Run `bash -n` on all shell scripts you added or modified.
4. Verify no secrets or machine-specific paths are present.
5. Verify all internal Markdown links point to real files.
6. Open a pull request with a clear description of what was added, changed, or fixed.
7. Reference any issues or decisions the PR resolves.

## Security

Do not commit secrets, private keys, tokens, or real IP addresses. If you discover a security issue in the documentation or scripts, open a private disclosure rather than a public issue.

## Questions

Open an issue with the label `question` if you are unsure about classification, scope, or technical accuracy.
