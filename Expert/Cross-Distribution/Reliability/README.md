# Reliability Engineering and SLOs

**Level:** Expert
**Scope:** Cross-Distribution
**Prerequisites:** [Incident Response](../Incident-Response/README.md)

## Purpose

Design reliability controls, define service level objectives, and implement proactive monitoring and recovery.

## Service Level Concepts

- **SLI (Service Level Indicator):** A quantitative measure of service behavior (e.g., request error rate, latency p99).
- **SLO (Service Level Objective):** A target for an SLI (e.g., 99.9% of requests succeed within 500ms over 30 days).
- **SLA (Service Level Agreement):** A contractual commitment with consequences.
- **Error Budget:** Allowed downtime within the SLO period. SLO of 99.9% = 43.8 minutes/month of allowed downtime.

## Availability Calculation

```
Availability = uptime / (uptime + downtime)

99.9%  = 8.76 hours downtime/year = 43.8 minutes/month
99.95% = 4.38 hours downtime/year = 21.9 minutes/month
99.99% = 52.6 minutes downtime/year = 4.38 minutes/month
```

## Runbook Structure

Every critical service should have a runbook. A runbook documents how to operate a service, including routine procedures and incident response.

```markdown
# Runbook: [Service Name]

**Last reviewed:** YYYY-MM-DD
**Owner:** [team or individual]

## Service Overview
[What this service does and why it matters]

## SLOs
| SLI | Objective | Measurement |
|---|---|---|
| Availability | 99.9% over 30 days | Successful health check responses |
| Latency p99 | < 500ms | Request response time |

## Architecture
[Brief architecture description, key dependencies]

## Monitoring and Alerting
- Health check URL: `http://localhost:8080/health`
- Key metrics to watch
- Alert thresholds

## Routine Operations
### Start/Stop
```bash
systemctl start servicename
systemctl stop servicename
```

### Rolling restart
```bash
systemctl reload servicename   # if supported
# Otherwise: traffic drain, restart, verify, restore traffic
```

### Configuration change
1. Validate config: `service --test-config`
2. Backup current config
3. Apply change
4. Verify service is healthy
5. Roll back if health check fails

## Common Failure Scenarios

| Symptom | Probable Cause | Diagnostic Command | Resolution |
|---|---|---|---|
| Service not responding | Process crashed | `systemctl status servicename` | Restart; investigate journal |
| High latency | Disk I/O saturation | `iostat -x 1 5` | Identify I/O source; optimize or scale |
| Connection refused | Port not listening | `ss -tlnp \| grep PORT` | Check service and firewall |

## On-call Escalation
[Who to contact, how]
```

## System Health Checks

```bash
#!/usr/bin/env bash
# health-check.sh — validate system health
set -euo pipefail

errors=0

check() {
  local name="$1"
  local cmd="$2"
  if eval "${cmd}" > /dev/null 2>&1; then
    echo "[OK] ${name}"
  else
    echo "[FAIL] ${name}"
    errors=$((errors + 1))
  fi
}

check "nginx running" "systemctl is-active nginx"
check "port 80 listening" "ss -tlnp | grep -q ':80'"
check "disk usage < 85%" "[ $(df / | awk 'NR==2 {print $5}' | tr -d '%') -lt 85 ]"
check "load average < 4" "[ $(uptime | awk -F'load average:' '{print $2}' | awk -F, '{print int($1)}') -lt 4 ]"

if [[ ${errors} -gt 0 ]]; then
  echo "${errors} check(s) failed"
  exit 1
fi

echo "All checks passed"
exit 0
```

## References

- [Google SRE Book](https://sre.google/sre-book/)
- [The SRE Workbook](https://sre.google/workbook/)
- [DORA Research](https://dora.dev/)
