# Processes, Signals, Jobs, and Resource Inspection

**Level:** Foundations
**Scope:** Cross-Distribution
**Prerequisites:** [CLI Fundamentals](../CLI/README.md)

## Purpose

Every running program is a process. Understanding how to inspect, control, and terminate processes is essential for administration, performance analysis, and troubleshooting.

## Process Concepts

- **PID (Process ID):** A unique integer assigned to each running process.
- **PPID (Parent PID):** The PID of the process that spawned this one.
- **UID/GID:** The user and group that own the process.
- **State:** R (running), S (sleeping), D (uninterruptible sleep), Z (zombie), T (stopped).

## Listing Processes

```bash
# Snapshot of current processes
ps aux
# a = all users, u = user-oriented format, x = include processes without a terminal

# Column meanings:
# USER PID %CPU %MEM VSZ RSS TTY STAT START TIME COMMAND
# VSZ  = virtual memory size (KB)
# RSS  = resident set size = actual RAM used (KB)

# Show process tree
ps auxf
pstree
pstree -p      # include PIDs

# Find a process by name
ps aux | grep nginx
pgrep nginx              # returns PIDs only
pgrep -la nginx          # PIDs + command

# Show all threads
ps -eLf
```

## Real-Time Monitoring

```bash
# Interactive process viewer
top
# Key bindings inside top:
# q       quit
# k       kill a process (enter PID)
# r       renice (change priority)
# M       sort by memory
# P       sort by CPU
# 1       toggle per-CPU view

# htop (more user-friendly; may need installation)
htop

# Show system-wide resource summary
vmstat 1 5      # memory, IO, CPU every 1 second, 5 samples
iostat 1 5      # disk I/O
mpstat -P ALL 1 # per-CPU statistics
```

## Signals

Signals are software interrupts sent to a process. The process handles or ignores them (except SIGKILL and SIGSTOP, which cannot be caught).

| Signal | Number | Default action | Typical use |
|---|---|---|---|
| SIGHUP | 1 | Terminate | Reload config (many daemons) |
| SIGINT | 2 | Terminate | Ctrl+C |
| SIGQUIT | 3 | Core dump | Ctrl+\ |
| SIGKILL | 9 | Terminate immediately | Force-kill (cannot be caught) |
| SIGTERM | 15 | Terminate | Graceful shutdown (default) |
| SIGSTOP | 19 | Stop | Pause process (cannot be caught) |
| SIGCONT | 18 | Continue | Resume a stopped process |
| SIGUSR1/2 | 10/12 | User-defined | Application-specific reload/action |

```bash
# Send a signal by PID
kill 1234               # send SIGTERM (graceful)
kill -9 1234            # send SIGKILL (force)
kill -SIGHUP 1234       # reload config
kill -s TERM 1234       # equivalent to SIGTERM

# Send a signal by process name
pkill nginx             # SIGTERM to all nginx processes
pkill -9 nginx          # SIGKILL
pkill -HUP nginx        # reload

# Kill all processes matching a pattern
killall apache2

# Preferred order for terminating a process:
# 1. kill <PID>           (SIGTERM — allow graceful cleanup)
# 2. Wait a few seconds
# 3. kill -9 <PID>        (SIGKILL — only if SIGTERM did not work)
```

## Process Priority: nice and renice

The scheduling priority ranges from -20 (highest priority) to 19 (lowest). Default is 0.

```bash
# Start a process with lower priority
nice -n 10 long_script.sh

# Change priority of a running process
renice -n 5 -p 1234      # set PID 1234 to nice value 5
renice -n 5 -u alice     # all processes owned by alice

# Only root can set negative nice values (higher priority)
sudo renice -n -5 -p 1234
```

## Background and Foreground Jobs

```bash
# Start in background
sleep 300 &

# List jobs in current shell
jobs
jobs -l    # include PIDs

# Bring job to foreground
fg %1
fg %sleep   # by name

# Send foreground job to background
# 1. Suspend with Ctrl+Z (sends SIGSTOP)
# 2. Resume in background:
bg %1

# Disown: remove job from shell's job table (survives shell exit)
disown %1

# nohup: keep running even if the shell exits
nohup long_script.sh > output.log 2>&1 &
```

## Inspecting /proc

```bash
# Each running process has a directory /proc/<PID>
ls /proc/1/
cat /proc/1/status          # status information
cat /proc/1/cmdline         # command line (null-separated)
cat /proc/1/environ         # environment variables
ls -la /proc/1/fd           # open file descriptors
cat /proc/1/maps            # memory map

# Open files for a process
lsof -p 1234
lsof -u alice               # all files opened by user
lsof /var/log/syslog        # which processes have this file open
lsof -i :80                 # which process listens on port 80
```

## Resource Limits: ulimit

```bash
# Show all limits for the current shell
ulimit -a

# Common limits
ulimit -n 65536   # max open file descriptors
ulimit -u 4096    # max user processes
ulimit -c 0       # disable core dumps
ulimit -c unlimited  # enable core dumps

# Persistent limits: /etc/security/limits.conf
# Example:
# alice  soft  nofile  4096
# alice  hard  nofile  65536
```

## Zombie Processes

A zombie (state Z) is a process that has exited but whose parent has not yet read its exit status. Zombies hold a PID but consume no CPU or memory (only a process table slot).

```bash
# Identify zombies
ps aux | awk '$8 == "Z"'

# Cannot kill a zombie directly. The parent must call wait().
# Send SIGCHLD to the parent to prompt it to reap the zombie:
kill -SIGCHLD <parent_PID>

# If the parent itself is stuck, killing the parent will reparent
# the zombie to init (PID 1), which will reap it automatically.
```

## Exercises

1. Start `sleep 1000` in the background. Find its PID using `pgrep`. Send it SIGSTOP, verify it is stopped, then send SIGCONT.
2. Use `lsof -i :22` to identify the process listening on the SSH port.
3. Start a process with `nice -n 15`. Use `renice` to change its priority to -5 (requires root). Observe the change in `top`.
4. Explain the difference between a zombie process and an orphan process.

## References

- `man ps`
- `man kill`
- `man signal(7)`
- `man nice`
- `man lsof`
- `man proc(5)`
