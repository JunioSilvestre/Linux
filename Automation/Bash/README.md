# Enterprise Bash Automation Standards

## Standard Script Template with Error Trapping
All production scripts must use `set -euo pipefail` and a dedicated cleanup trap.
