# IEEE 802.1Q VLAN Tagging & Link Aggregation (Bonding/Teaming)

## Netplan (Ubuntu) VLAN & Bond Configuration
```yaml
# /etc/netplan/01-netcfg.yaml
network:
  version: 2
  renderer: networkd
  ethernets:
    ens18: {}
    ens19: {}
  bonds:
    bond0:
      interfaces: [ens18, ens19]
      parameters:
        mode: 802.3ad
        lacp-rate: fast
        mii-monitor-interval: 100
  vlans:
    vlan100:
      id: 100
      link: bond0
      addresses: [10.100.0.15/24]
      routes:
        - to: default
          via: 10.100.0.1
```

Apply: `sudo netplan apply`
