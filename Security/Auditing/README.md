# Linux Audit Subsystem (`auditd`) Architecture

## Production Audit Rules (`/etc/audit/rules.d/audit.rules`)
```audit
## Monitor changes to system authentication
-w /etc/passwd -p wa -k identity
-w /etc/shadow -p wa -k identity
-w /etc/group -p wa -k identity
-w /etc/sudoers -p wa -k privilege_escalation
-w /etc/sudoers.d/ -p wa -k privilege_escalation

## Monitor administrative shell commands (UID >= 1000)
-a always,exit -F arch=b64 -S execve -F auid>=1000 -F auid!=4294967295 -k command_execution
```
