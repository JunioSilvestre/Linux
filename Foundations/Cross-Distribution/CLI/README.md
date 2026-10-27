# Command-Line Interface Fundamentals

**Level:** Foundations
**Scope:** Cross-Distribution (valid on all Linux systems)
**Prerequisites:** Access to a Linux terminal

## Purpose

This guide covers the essential skills needed to navigate and operate a Linux system from the command line. Mastery of these fundamentals is required before proceeding to any other topic in this repository.

## Shell Basics

### Reading the prompt

```
user@hostname:/current/directory$ _
```

- `user` — the currently logged-in user.
- `hostname` — the machine name.
- `/current/directory` — the working directory (`$PWD`).
- `$` — indicates a regular user. `#` indicates root.

### Getting help

```bash
# Read the manual for a command
man ls

# Short help
ls --help

# Find which manual section covers a topic
man -k keyword

# Show the type of a command (builtin, alias, function, or binary)
type ls
type cd
type ll

# Find the path of an executable
which bash
whereis nginx
```

## Navigation

```bash
# Print working directory
pwd

# Change directory
cd /etc/nginx
cd ..           # up one level
cd ~            # home directory
cd -            # previous directory

# List files
ls              # basic listing
ls -l           # long format (permissions, owner, size, date)
ls -la          # include hidden files
ls -lh          # human-readable sizes
ls -lt          # sort by modification time
ls -lR          # recursive

# Show directory tree
find . -type d | head -20
```

## Working with Files and Directories

```bash
# Create
touch file.txt             # create empty file or update timestamp
mkdir newdir               # create directory
mkdir -p a/b/c             # create nested directories

# Copy
cp source.txt dest.txt
cp -r sourcedir/ destdir/  # recursive (directories)
cp -p file.txt dest/       # preserve permissions and timestamps

# Move and rename
mv old.txt new.txt
mv file.txt /tmp/

# Delete — CAUTION: no undo
rm file.txt
rm -r directory/           # recursive delete
rm -i file.txt             # interactive, prompts before each deletion

# Verify a path before deleting
ls -la /path/to/target
```

> **WARNING:** `rm` is irreversible. There is no Recycle Bin on Linux. Always verify the target before removing.

## Viewing Files

```bash
cat file.txt               # dump entire file
less file.txt              # paged viewer (q to quit, /search)
head -20 file.txt          # first 20 lines
tail -20 file.txt          # last 20 lines
tail -f /var/log/syslog    # follow new lines as they are appended

# Count lines, words, bytes
wc -l file.txt
wc -w file.txt
```

## Text Processing

```bash
# Search
grep 'pattern' file.txt
grep -r 'pattern' /etc/      # recursive
grep -i 'pattern' file.txt   # case-insensitive
grep -n 'pattern' file.txt   # show line numbers
grep -v 'pattern' file.txt   # invert match (lines NOT matching)

# Sort and unique
sort file.txt
sort -n numbers.txt          # numeric sort
sort -r file.txt             # reverse
uniq file.txt                # collapse consecutive duplicates
sort file.txt | uniq -c     # count occurrences

# Cut fields
cut -d: -f1 /etc/passwd      # first colon-delimited field
cut -d, -f2,4 data.csv

# Stream editor (non-interactive substitution)
sed 's/old/new/g' file.txt
sed -i 's/old/new/g' file.txt  # edit in place

# Pattern-based processing
awk '{print $1, $3}' file.txt         # print columns 1 and 3
awk -F: '{print $1}' /etc/passwd      # use : as delimiter
awk 'NR>1 {print $2}' file.txt        # skip header line
```

## I/O Redirection and Pipes

```bash
# Redirect stdout to file (overwrite)
command > output.txt

# Append stdout to file
command >> output.txt

# Redirect stderr
command 2> errors.txt

# Redirect both stdout and stderr
command > output.txt 2>&1
command &> output.txt       # equivalent shorthand

# Discard output
command > /dev/null 2>&1

# Pipe: send stdout of one command as stdin to the next
ps aux | grep nginx
cat /var/log/auth.log | grep 'Failed' | tail -20

# tee: write to both stdout and a file
command | tee output.txt

# Here document
cat << 'EOF' > file.txt
line one
line two
