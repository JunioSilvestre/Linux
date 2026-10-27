# Enterprise Network Diagnostics & Packet Inspection

## Essential Toolkit

| Command | Usage | Description |
|---|---|---|
| `ip -brief address` | Interface overview | Quick view of all interface states and IPs |
| `ip -s link show dev eth0` | Drop/Error counters | Check for framing errors, collisions, drops |
| `ss -tulnp` | Listening sockets | Socket statistics with process PID and name |
| `ss -s` | Socket summary | Total TCP sockets by state (TIME-WAIT, ESTAB) |
| `tcpdump -nn -i eth0 port 443` | Packet capture | Inspect traffic without DNS resolution |
| `ethtool eth0` | Physical link speed | Verify speed, duplex, autonegotiation |

### Advanced tcpdump Recipes
```bash
# Capture packets with SYN or RST flags set
sudo tcpdump -nn -i any "tcp[tcpflags] & (tcp-syn|tcp-rst) != 0"

# Capture and write to pcap for Wireshark analysis
sudo tcpdump -nn -i eth0 -w /tmp/capture.pcap host 10.0.0.50 and port 80

# Monitor dropped packets at the kernel level
sudo perf record -e skb:kfree_skb -a sleep 10
sudo perf script
```
