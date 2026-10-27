# Enterprise Firewall Architectures (nftables, firewalld, ufw)

## 1. nftables Standard Configuration
`nftables` is the default Linux packet classification framework replacing `iptables`.

```nft
# /etc/nftables.conf
flush ruleset

table inet filter {
    chain input {
        type filter hook input priority filter; policy drop;

        # Connection tracking: accept established and related traffic
        ct state established,related accept
        ct state invalid drop

        # Loopback interface
        iifname "lo" accept

        # ICMP / Ping rate limited
        ip protocol icmp icmp type echo-request limit rate 5/second accept
        ip6 nexthdr icmpv6 accept

        # Open management ports
        tcp dport 22 accept
        tcp dport { 80, 443 } accept

        # Log dropped packets (rate limited)
        limit rate 3/minute log prefix "[NFT DROP]: " drop
    }

    chain forward {
        type filter hook forward priority filter; policy drop;
    }

    chain output {
        type filter hook output priority filter; policy accept;
    }
}
```

Apply and verify:
```bash
sudo nft -f /etc/nftables.conf
sudo nft list ruleset
```
