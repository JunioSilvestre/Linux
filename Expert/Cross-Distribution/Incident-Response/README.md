# Incident Response and Root-Cause Analysis

**Level:** Expert
**Scope:** Cross-Distribution
**Prerequisites:** [Advanced Performance](../../../Advanced/Cross-Distribution/Performance/README.md), [Advanced Boot](../../../Advanced/Cross-Distribution/Boot/README.md)

## Purpose

Apply a structured methodology to complex system incidents. Distinguish symptoms from causes. Document findings systematically to prevent recurrence.

## Incident Response Phases

1. **Detection** — Identify that an incident exists.
2. **Triage** — Determine severity and scope.
3. **Containment** — Stop the bleeding without destroying evidence.
4. **Diagnosis** — Understand the root cause.
5. **Resolution** — Implement a corrective action.
6. **Verification** — Confirm the system is behaving correctly.
7. **Post-incident review** — Document findings and prevention.

## Evidence Collection

Collect evidence before making changes. Changes destroy evidence.

```bash
# Timestamp every action
date --iso-8601=seconds

# System state snapshot
uptime > /tmp/ir/state.txt
ps auxf >> /tmp/ir/state.txt
ss -tlnp >> /tmp/ir/state.txt
ip addr >> /tmp/ir/state.txt
ip route >> /tmp/ir/state.txt
df -h >> /tmp/ir/state.txt
free -m >> /tmp/ir/state.txt
w >> /tmp/ir/state.txt  # who is logged in
last | head -20 >> /tmp/ir/state.txt
journalctl -b -p err --no-pager >> /tmp/ir/journal-errors.txt

# Network state
ss -s >> /tmp/ir/network.txt
netstat -rn >> /tmp/ir/network.txt
ip neigh >> /tmp/ir/network.txt

# Open files
lsof > /tmp/ir/lsof.txt

# Package changes (identify recent installs)
# Ubuntu:
grep ' install ' /var/log/dpkg.log | tail -50 >> /tmp/ir/pkg-changes.txt
# RHEL:
grep 'Installed' /var/log/dnf.log | tail -50 >> /tmp/ir/pkg-changes.txt
dnf history | head -20 >> /tmp/ir/pkg-changes.txt

# Recent file modifications
find /etc -newer /var/log/apt/history.log -type f >> /tmp/ir/modified-etc.txt 2>/dev/null
find /bin /sbin /usr/bin /usr/sbin -newer /tmp/reference -type f >> /tmp/ir/modified-bins.txt 2>/dev/null

# Scheduled tasks (check for unexpected entries)
crontab -l >> /tmp/ir/crontabs.txt
cat /etc/cron* /var/spool/cron/crontabs/* >> /tmp/ir/crontabs.txt 2>/dev/null
systemctl list-timers --all >> /tmp/ir/timers.txt
```

## Systematic Diagnosis Workflow

```bash
# 1. Is the system responding?
uptime

# 2. Is it overloaded?
vmstat 1 5
top -b -n 1 | head -30

# 3. Is a specific service failing?
systemctl list-units --state=failed
journalctl -u failing-service -b --no-pager | tail -50

# 4. Is disk full?
df -h
du -sh /* 2>/dev/null | sort -h | tail -10

# 5. Is memory exhausted?
free -m
dmesg | grep -i oom | tail -10

# 6. Is it a network issue?
ping -c 3 8.8.8.8
dig @8.8.8.8 google.com
ss -tlnp

# 7. Is something consuming all of a resource?
iostat -x 1 5 | grep -v '^$'
iotop -o -b -n 3 | head -20
```

## Root-Cause Analysis Template

```markdown
# Incident Report: [Short Description]

**Date:** YYYY-MM-DD
**Severity:** P1 / P2 / P3
**Duration:** HH:MM (detected HH:MM — resolved HH:MM)
**Systems Affected:** [hostnames, services]

## Summary
[One paragraph: what happened, what was the impact, how it was resolved]

## Timeline
| Time (UTC) | Event |
|---|---|
| 14:00 | Monitoring alert fired: service down |
| 14:05 | Engineer paged |
| 14:10 | Evidence collected |
| 14:25 | Root cause identified |
| 14:35 | Fix applied |
| 14:40 | Service verified healthy |

## Root Cause
[Specific technical cause, not a symptom]

## Contributing Factors
- [Factor 1]
- [Factor 2]

## Resolution
[Exact steps taken to resolve the incident]

## Prevention
| Action | Owner | Due Date | Status |
|---|---|---|---|
| [Action 1] | [Name] | YYYY-MM-DD | Open |

## Lessons Learned
[What we learned, what we would do differently]
```

## Exercises

1. On a test VM, cause a specific service failure (e.g., break `nginx.conf`). Practice the evidence collection steps before and after fixing it. Write a brief RCA.
2. Simulate an OOM event with `stress-ng --vm 1 --vm-bytes 90%`. Observe OOM killer behavior in the journal. Document the RCA.
3. Create an incident response checklist for a service that handles web traffic.

## References

- [Google SRE Book: Effective Troubleshooting](https://sre.google/sre-book/effective-troubleshooting/)
- [Brendan Gregg's Debugging Methodology](https://www.brendangregg.com/methodology.html)
- [ITIL Incident Management](https://www.axelos.com/)
