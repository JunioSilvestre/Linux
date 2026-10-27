# Capacity Planning

**Level:** Expert
**Scope:** Cross-Distribution
**Prerequisites:** [Performance Analysis](../../../Advanced/Cross-Distribution/Performance/README.md), [Reliability](../Reliability/README.md)

## Purpose

Anticipate resource requirements before they become incidents. Plan capacity based on measured growth trends, not guesses.

## Metrics to Collect

| Resource | Metrics | Tool |
|---|---|---|
| CPU | Utilization %, runqueue length | sar, mpstat |
| Memory | Used MB, swap activity | free, sar |
| Disk space | Used GB, growth rate GB/day | df, sar |
| Disk I/O | IOPS, throughput, await | iostat |
| Network | Bandwidth in/out, packet rate | sar -n DEV |
| Connections | Open connections, connection rate | ss -s |

## Growth Rate Modeling

```bash
# Collect daily disk usage data
df -h / | awk 'NR==2 {print $3}' >> /var/log/disk-usage-history.log

# After 30+ days, calculate daily growth rate
# Linear regression or simple average:
# growth_rate = (last_value - first_value) / days
# days_to_full = (capacity - current) / growth_rate

# With sar historical data (if sysstat is enabled):
sar -r -f /var/log/sa/sa* | grep -v RESTART | awk '{print $1, $5}'
```

## Alerting Thresholds

| Resource | Warning | Critical |
|---|---|---|
| Disk usage | 75% | 85% |
| CPU (15min avg) | 70% | 90% |
| Memory usage | 80% | 90% |
| Swap usage | 10% | 25% |
| Load average | nproc * 0.8 | nproc * 1.5 |

## Capacity Planning Report Template

```markdown
# Capacity Planning Report: [hostname]

**Date:** YYYY-MM-DD
**Period:** 30-day average

## Current State
| Resource | Current Usage | Capacity | % Used |
|---|---|---|---|
| CPU | 2.3 cores avg | 8 cores | 29% |
| Memory | 6.2 GB | 16 GB | 39% |
| Root disk | 45 GB | 100 GB | 45% |
| Data disk | 380 GB | 500 GB | 76% |

## Trends
| Resource | 30-day growth | Projected 6-month | Action needed |
|---|---|---|---|
| CPU | +5% | 54% | No action |
| Memory | +8% | 63% | Monitor |
| Root disk | +1 GB/week | 69 GB (69%) | No action |
| Data disk | +15 GB/week | 740 GB (148%) | **Urgent: expand storage** |

## Recommendations
1. Expand data disk capacity by 300 GB within 30 days.
2. Schedule monthly review of data disk growth.
```

## References

- [Brendan Gregg: Capacity Planning](https://www.brendangregg.com/blog/2014-05-25/capacity-planning-for-performance.html)
- [Google SRE: Managing Load](https://sre.google/sre-book/managing-load/)
