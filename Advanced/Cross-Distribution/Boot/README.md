# Boot Troubleshooting and Recovery

**Level:** Advanced
**Scope:** Cross-Distribution
**Prerequisites:** [systemd Foundations](../../../Foundations/Debian-Based/Ubuntu/systemd/README.md)

## Purpose

Diagnose and recover from boot failures at the GRUB, initramfs, and systemd layers.

## Boot Sequence Overview

```
Firmware (UEFI/BIOS)
    ↓
GRUB2 bootloader (/boot/grub2/ or /boot/grub/)
    ↓
Kernel loaded + initramfs mounted
    ↓
initramfs: mounts root filesystem, unlocks encryption, activates LVM/RAID
    ↓
Kernel hands off to /sbin/init → systemd
    ↓
systemd loads default.target (multi-user.target or graphical.target)
    ↓
Services start
```

## Reading Boot Logs

```bash
# Current boot
journalctl -b
journalctl -b -p err    # errors only in current boot
journalctl -b -1        # previous boot
journalctl -b -2        # two boots ago

# List boots with timestamps
journalctl --list-boots

# Kernel ring buffer (hardware initialization, driver errors)
dmesg
dmesg -T              # with human-readable timestamps
dmesg | grep -i 'fail\|error\|warn'

# systemd analysis
systemd-analyze           # total boot time
systemd-analyze blame     # time per unit
systemd-analyze critical-chain  # critical path
systemd-analyze plot > boot.svg  # visual timeline
```

## systemd Boot Diagnostics

```bash
# Services that failed during boot
systemctl list-units --state=failed

# Detailed status of a failed service
systemctl status servicename
journalctl -u servicename -b   # service logs from current boot

# Show systemd unit dependency tree
systemctl list-dependencies
systemctl list-dependencies --before sshd.service
systemctl list-dependencies --after sshd.service

# Mask a failing service to allow boot to complete (emergency measure)
# Use only when the service failure is preventing other services from starting
sudo systemctl mask broken-service
# Remember to investigate and unmask:
sudo systemctl unmask broken-service
```

## Recovery Mode

### Ubuntu recovery mode

1. Reboot and hold `Shift` (BIOS) or `Esc` (UEFI) to show GRUB menu.
2. Select **Advanced options for Ubuntu**.
3. Select the **recovery mode** entry for your kernel.
4. From the recovery menu, select **root** for a root shell.

### RHEL rescue mode

1. Reboot and press `e` at the GRUB menu to edit the boot entry.
2. Find the `linux` line, add `systemd.unit=rescue.target` at the end.
3. Press `Ctrl+X` to boot with the modified entry.

### Emergency mode

```bash
# In the GRUB editor, add to the linux line:
systemd.unit=emergency.target

# Emergency mode mounts only the root filesystem (read-only)
# Remount root read-write if needed:
mount -o remount,rw /
```

## GRUB Recovery

```bash
# View GRUB configuration
cat /boot/grub2/grub.cfg        # RHEL
cat /boot/grub/grub.cfg         # Ubuntu

# GRUB configuration source (edit these, not grub.cfg)
cat /etc/default/grub
ls /etc/grub.d/

# Regenerate grub.cfg
sudo grub2-mkconfig -o /boot/grub2/grub.cfg   # RHEL
sudo update-grub                              # Ubuntu

# If GRUB itself is missing, boot from installation media:
# Mount root filesystem
mount /dev/sda2 /mnt
# On Ubuntu:
mount --bind /dev /mnt/dev
mount --bind /proc /mnt/proc
mount --bind /sys /mnt/sys
chroot /mnt
update-grub
grub-install /dev/sda
exit
umount -R /mnt
```

## initramfs Rebuild

```bash
# Ubuntu: rebuild initramfs
sudo update-initramfs -u -k all   # all kernels
sudo update-initramfs -u -k $(uname -r)  # current kernel only

# RHEL: rebuild initramfs
sudo dracut --force
sudo dracut --force --verbose /boot/initramfs-$(uname -r).img $(uname -r)

# Verify the initramfs contains expected modules
lsinitrd /boot/initramfs-$(uname -r).img | grep -i lvm
lsinitrd /boot/initramfs-$(uname -r).img | grep -i raid
```

## Exercises

1. Use `systemd-analyze blame` to identify the three slowest-starting services on your system. Investigate whether any can safely be disabled or parallelized.
2. Boot into rescue mode and examine the `/etc/fstab`. Intentionally introduce an error (on a test VM), reboot, and use emergency mode to fix it.
3. Rebuild the initramfs on a test VM. Verify the system boots normally afterward.

## References

- `man systemd-analyze`
- `man journalctl`
- `man dracut`
- `man update-initramfs`
- [RHEL 9 Managing and monitoring systemd](https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/9/html/configuring_basic_system_settings/managing-systemd_configuring-basic-system-settings)
- [Ubuntu Boot Process](https://ubuntu.com/server/docs/boot-process)
