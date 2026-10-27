# Task Scheduling: cron and systemd Timers

**Level:** Intermediate
**Scope:** Cross-Distribution
**Prerequisites:** [systemd Foundations](../../Foundations/Debian-Based/Ubuntu/systemd/README.md)

## Purpose

Schedule recurring and one-time tasks reliably. Understand when to prefer cron and when systemd timers are more appropriate.

## cron

### Cron syntax

```
* * * * *  command-to-execute
│ │ │ │ │
│ │ │ │ └─ Day of week (0-7, 0 and 7 = Sunday)
│ │ │ └─── Month (1-12)
│ │ └───── Day of month (1-31)
│ └─────── Hour (0-23)
└───────── Minute (0-59)
```

Common examples:

```bash
# Every 5 minutes
*/5 * * * *  /usr/local/bin/check.sh

# Every day at 2:30 AM
30 2 * * *   /usr/local/bin/backup.sh

# Every Monday at 8:00 AM
0 8 * * 1    /usr/local/bin/weekly-report.sh

# First day of each month at midnight
0 0 1 * *    /usr/local/bin/monthly-cleanup.sh

# Shortcuts
@reboot      /usr/local/bin/startup.sh
@daily       /usr/local/bin/daily.sh
@weekly      /usr/local/bin/weekly.sh
@monthly     /usr/local/bin/monthly.sh
```

### Managing crontabs

```bash
# Edit current user's crontab
crontab -e

# List current user's crontab
crontab -l

# Remove current user's crontab
crontab -r

# Edit another user's crontab (as root)
sudo crontab -u alice -e

# System-wide cron (requires root)
# /etc/crontab         — has an extra 'user' field
# /etc/cron.d/         — drop-in files, same syntax as /etc/crontab
# /etc/cron.daily/     — scripts run daily
# /etc/cron.weekly/    — scripts run weekly
# /etc/cron.monthly/   — scripts run monthly
```

### Best practices for cron jobs

```bash
# Use full paths in cron commands (PATH is limited in cron)
30 2 * * * /usr/bin/find /tmp -mtime +7 -delete

# Capture output to a log file
30 2 * * * /usr/local/bin/backup.sh >> /var/log/backup.log 2>&1

# Discard output (use only if you are confident the job works)
30 2 * * * /usr/local/bin/backup.sh > /dev/null 2>&1

# Lock file to prevent overlapping executions
30 2 * * * flock -n /tmp/backup.lock /usr/local/bin/backup.sh
```

### Controlling access to cron

```bash
# Allowlist: only users in /etc/cron.allow can use crontab
# Blocklist: users in /etc/cron.deny are prohibited
cat /etc/cron.allow
cat /etc/cron.deny
# If neither exists, behavior depends on distribution (usually all users allowed)
```

## systemd Timers

systemd timers are a modern alternative to cron with better logging, dependency management, and missed-run handling.

### Timer unit file

`/etc/systemd/system/mybackup.timer`:

```ini
[Unit]
Description=Run mybackup daily at 2:30 AM

[Timer]
# OnCalendar uses systemd time specification
OnCalendar=*-*-* 02:30:00
# Run immediately if the last scheduled time was missed
Persistent=true

[Install]
WantedBy=timers.target
```

### Corresponding service unit

`/etc/systemd/system/mybackup.service`:

```ini
[Unit]
Description=My Backup Job
After=network.target

[Service]
Type=oneshot
User=backupuser
ExecStart=/usr/local/bin/backup.sh
StandardOutput=journal
StandardError=journal
```

```bash
# Enable and start the timer (NOT the service directly)
sudo systemctl daemon-reload
sudo systemctl enable --now mybackup.timer

# List all timers
systemctl list-timers
systemctl list-timers --all   # include inactive

# Test by running the service manually
sudo systemctl start mybackup.service

# View logs
journalctl -u mybackup.service
```

### Time specification examples

```bash
# Every 5 minutes
OnCalendar=*:0/5

# Every day at 2:30 AM
OnCalendar=*-*-* 02:30:00

# Every Monday at 8:00 AM
OnCalendar=Mon *-*-* 08:00:00

# Every hour
OnCalendar=hourly

# Validate a time specification
systemd-analyze calendar "Mon *-*-* 08:00:00"
```

## at: One-time Scheduling

```bash
# Schedule a command to run once
echo '/usr/local/bin/report.sh' | at 14:30
echo '/usr/local/bin/report.sh' | at 14:30 tomorrow
echo '/usr/local/bin/report.sh' | at now + 2 hours

# List pending at jobs
atq

# Remove a pending at job
atrm <job_number>
```

## Choosing Between cron and systemd timers

| Feature | cron | systemd timer |
|---|---|---|
| Logging | Only if redirected | Automatic via journald |
| Missed runs | Not handled by default | Persistent=true handles missed runs |
| Dependencies | None | Full systemd dependency support |
| Complexity | Simple | More files required |
| User timers | Yes (crontab) | Yes (~/.config/systemd/user/) |
| Monitoring | Difficult | `systemctl list-timers` |

## Exercises

1. Create a cron job that appends the current disk usage to `/var/log/disk-usage.log` every 10 minutes. Verify the log is growing.
2. Create a systemd timer that runs a script every 5 minutes. Use `journalctl` to verify it ran.
3. Explain what happens if a cron job or systemd timer has `Persistent=true` and the system was off during the scheduled run time.

## References

- `man 5 crontab`
- `man at`
- `man systemd.timer`
- `man systemd.time`
- `systemd-analyze calendar`
