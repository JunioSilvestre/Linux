# Linux Routing and Policy-Based Routing (PBR)

## 1. Multi-Homed Routing Table Configuration
When a Linux server has multiple NICs connected to different subnets or ISPs, policy-based routing ensures responses exit through the same interface they entered.

```bash
# Define custom routing tables in /etc/iproute2/rt_tables
echo "200 isp2" | sudo tee -a /etc/iproute2/rt_tables

# Add default route to custom table
sudo ip route add 192.168.2.0/24 dev eth1 src 192.168.2.10 table isp2
sudo ip route add default via 192.168.2.1 dev eth1 table isp2

# Add policy routing rules based on source IP
sudo ip rule add from 192.168.2.10/32 table isp2
sudo ip rule add to 192.168.2.10/32 table isp2

# Verify active rules and routes
ip rule show
ip route show table isp2
```
