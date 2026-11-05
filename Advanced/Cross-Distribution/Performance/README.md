# System Performance Analysis

**Level:** Advanced
**Scope:** Cross-Distribution
**Prerequisites:** [Processes](../../../Foundations/Cross-Distribution/Processes/README.md), [Storage](../../../Intermediate/Cross-Distribution/Storage/README.md)

## Purpose

Identify and analyze performance bottlenecks across CPU, memory, disk I/O, and network. This guide covers systematic methodology, not just a list of tools.

## Methodology: USE Method

For each resource, examine:
1. **Utilization** — how busy is it?
2. **Saturation** — is work waiting (queue depth)?
3. **Errors** — are there error events?

## CPU Analysis

```bash
# Snapshot CPU utilization
top -b -n 1
mpstat -P ALL 1 5      # per-CPU, 5 samples at 1s interval
sar -u 1 5             # CPU utilization via sysstat

# Interpreting top output:
# us (user): time in user space
# sy (system): time in kernel
# wa (iowait): idle waiting for I/O  → disk bottleneck indicator
# st (steal): time stolen by hypervisor  → VM resource contention

# Find CPU-intensive processes
ps aux --sort=-%cpu | head -15
ps -eo pid,ppid,cmd,%cpu,%mem --sort=-%cpu | head -15

# CPU runqueue length (saturation)
vmstat 1 10
# Column 'r': processes runnable but waiting for CPU
# If r > number of CPUs consistently, CPU is saturated

# Perf: CPU profiling (requires linux-tools or perf)
sudo perf top                    # live view by function
sudo perf stat sleep 5          # hardware counter stats
sudo perf record -ag sleep 30   # record 30 seconds
sudo perf report                # analyze recording
```

## Memory Analysis

```bash
# Memory overview
free -h
free -m
cat /proc/meminfo

# Key metrics:
# MemAvailable: usable memory for new processes (not just MemFree)
# Buffers/Cached: kernel caches (can be reclaimed)
# SwapUsed: if nonzero, system is under memory pressure

# Memory utilization
vmstat -s
sar -r 1 5              # memory stats

# Find memory-intensive processes
ps aux --sort=-%mem | head -15

# OOM (Out Of Memory) killer events
journalctl -k | grep -i 'oom\|killed'
dmesg | grep -i 'oom\|killed'
grep -i 'oom' /var/log/messages   # RHEL
grep -i 'oom' /var/log/syslog     # Ubuntu

# Memory map for a specific process
pmap -x <PID>
cat /proc/<PID>/smaps | grep -i 'rss\|pss' | awk '{sum += $2} END {print sum " kB"}'
```

## Disk I/O Analysis

```bash
# Disk I/O statistics
iostat -x 1 5
# Key columns:
# await: average time per request (ms) → high = slow disk or saturation
# %util: percentage of time disk was busy → 100% = saturated disk
# r/s, w/s: reads and writes per second

# Find I/O-intensive processes
iotop -o         # --only: show processes doing I/O
iotop -o -b -n 5 # batch mode, 5 iterations

# Block device statistics
cat /sys/block/sda/stat

# I/O wait monitoring
vmstat 1 10
# Column 'b': processes in uninterruptible sleep (waiting for I/O)
# Column 'wa': iowait percentage

# Check disk errors
dmesg | grep -i 'error\|fail\|warn' | grep -i 'sd[a-z]\|nvme'
journalctl -k | grep -i 'error' | grep -i 'sd[a-z]\|nvme'

# SMART disk health
sudo smartctl -H /dev/sda     # health summary
sudo smartctl -a /dev/sda     # detailed attributes
```

## Network Analysis

```bash
# Network interface statistics
ip -s link show eth0
sar -n DEV 1 5
watch -n 1 cat /proc/net/dev

# Bandwidth measurement
bandwidth in real time:
nload eth0
iftop -i eth0    # per-connection bandwidth

# Connection states
ss -s
ss -tlnp

# TCP retransmissions (saturation indicator)
ss -ti dst host         # TCP info for specific host
netstat -s | grep -i retransmit
cat /proc/net/snmp | grep -i tcp

# Network latency
ping -c 20 target_host   # latency and loss
mtr target_host           # continuous traceroute (requires mtr)

# Packet capture
sudo tcpdump -i eth0 -nn -c 100 port 80
sudo tcpdump -i eth0 -w /tmp/capture.pcap -c 1000
```

## Load Average Interpretation

```bash
uptime
# 14:30:00 up 5 days, 3:12, 2 users, load average: 0.45, 0.38, 0.35
#                                                    1min  5min  15min

# Load average meaning:
# 1.0 per CPU core = fully utilized (not saturated)
# > 1.0 per CPU core = saturation (work queuing)

# Get number of CPU cores
nproc
grep -c ^processor /proc/cpuinfo

# Rule of thumb:
# On a 4-core system, load average of 4.0 = fully utilized
# Load average > 4 * nproc = system is saturated
```

## Performance Baseline Creation

```bash
# Capture a baseline
sar -A -o /var/log/sar-baseline.bin 1 300  # 5 minutes of all stats

# Report from baseline
sar -f /var/log/sar-baseline.bin -u        # CPU from file
sar -f /var/log/sar-baseline.bin -r        # memory
sar -f /var/log/sar-baseline.bin -d        # disk

# Enable sysstat (if not already active)
sudo systemctl enable --now sysstat
# Data collected hourly in /var/log/sa/
sar -u        # today's CPU usage
sar -u -f /var/log/sa/sa01   # specific day
```

## Exercises

1. Use `vmstat 1 30` to observe system behavior while running a CPU-intensive command (`stress-ng --cpu 4 --timeout 20s`). Identify the change in the `r` and `us` columns.
2. Use `iotop` to identify which process is causing disk I/O when running `dd if=/dev/zero of=/tmp/test bs=1M count=1000`.
3. Create a 5-minute performance snapshot with `sar`. Report CPU, memory, and disk statistics from the file.

## References

- `man sar`
- `man iostat`
- `man vmstat`
- `man mpstat`
- [Brendan Gregg: Linux Performance](https://www.brendangregg.com/linuxperf.html)
- [USE Method](https://www.brendangregg.com/usemethod.html)
- [sysstat documentation](http://sebastien.godard.pagesperso-orange.fr/)
