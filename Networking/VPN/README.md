# Enterprise WireGuard Site-to-Site VPN

## Hub Server Configuration (`/etc/wireguard/wg0.conf`)
```ini
[Interface]
Address = 10.50.0.1/24
ListenPort = 51820
PrivateKey = <SERVER_PRIVATE_KEY>
PostUp = nft add rule inet filter input udp dport 51820 accept
PostDown = nft delete rule inet filter input udp dport 51820 accept

# Peer: Branch Office Gateway
[Peer]
PublicKey = <CLIENT_PUBLIC_KEY>
AllowedIPs = 10.50.0.2/32, 192.168.10.0/24
```

Lifecycle Management:
```bash
# Enable WireGuard service
sudo systemctl enable --now wg-quick@wg0

# Check handshake and transfer statistics
sudo wg show
```
