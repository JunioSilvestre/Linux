# 04-redes — Redes Avançadas, Roteamento e Protocolos Linux

Projetos em Bash para roteamento avançado com iproute2, namespaces de rede, túneis WireGuard, bonding LACP, VLANs e QoS com tc.

---

## 🏛️ Trilha de Projetos Práticos de Engenharia Linux Nível Sênior (20 Projetos Reais)

| # | Projeto | Título / Foco Técnico | Ferramentas Chave |
|---|---|---|---|
| **01** | [`01-policy-routing-multiple-routing-tables/`](./01-policy-routing-multiple-routing-tables) | **Roteamento Baseado em Políticas (Policy Routing) com Múltiplas Tabelas no Linux** | `ip rule, ip route, rt_tables` |
| **02** | [`02-network-namespace-vpn-isolation/`](./02-network-namespace-vpn-isolation) | **Isolamento Completo de Processos em Network Namespaces com VPN Dedicada** | `ip netns, ip link, wg-quick` |
| **03** | [`03-lacp-bonding-active-backup-teaming/`](./03-lacp-bonding-active-backup-teaming) | **Agregação de Links de Rede com LACP (802.3ad) e Failover de Interfaces** | `ip link, teamd, /proc/net/bonding` |
| **04** | [`04-vlan-8021q-trunking-subinterfaces/`](./04-vlan-8021q-trunking-subinterfaces) | **Criação e Gestão de Troncos de Rede e Subinterfaces VLAN 802.1Q** | `ip link, modprobe 8021q` |
| **05** | [`05-wireguard-mesh-dynamic-routing-bird/`](./05-wireguard-mesh-dynamic-routing-bird) | **Rede Mesh Criptografada com WireGuard e Roteamento Dinâmico via BIRD** | `wg, bird, birdc, ip` |
| **06** | [`06-tc-cake-fq-codel-bufferbloat-fix/`](./06-tc-cake-fq-codel-bufferbloat-fix) | **Mitigação de Bufferbloat e QoS com Algoritmo CAKE e FQ-CoDel no Linux tc** | `tc qdisc, ip link` |
| **07** | [`07-bridge-isolated-ebtables-filtering/`](./07-bridge-isolated-ebtables-filtering) | **Criação de Bridges Linux com Isolamento de Portas e Filtragem L2 com ebtables** | `brctl, ip link, ebtables` |
| **08** | [`08-geneve-vxlan-overlay-multicast/`](./08-geneve-vxlan-overlay-multicast) | **Túneis Overlay GENEVE e VXLAN com Sinalização Multicast para Redes SD-WAN** | `ip link, bridge fdb` |
| **09** | [`09-keepalived-vrrp-virtual-ip-clustering/`](./09-keepalived-vrrp-virtual-ip-clustering) | **Cluster de Alta Disponibilidade com Keepalived VRRP e IP Virtual Flutuante** | `keepalived, ip addr, arping` |
| **10** | [`10-tcp-bbr-congestion-control-tuning/`](./10-tcp-bbr-congestion-control-tuning) | **Habilitação e Otimização do Algoritmo de Controle de Congestionamento TCP BBR** | `sysctl, /proc/sys/net/ipv4/tcp_congestion_control` |
| **11** | [`11-nftables-nat-port-forwarding-pat/`](./11-nftables-nat-port-forwarding-pat) | **Firewall de Borda e Roteador NAT/PAT de Alta Velocidade com nftables** | `nft, nftables.conf, conntrack` |
| **12** | [`12-ipip-gre-tunnel-site-to-site/`](./12-ipip-gre-tunnel-site-to-site) | **Provisionamento de Túneis GRE e IPIP Ponto a Ponto entre Redes Corporativas** | `ip tunnel, ip route` |
| **13** | [`13-dhcp-snooping-arp-inspection-linux/`](./13-dhcp-snooping-arp-inspection-linux) | **Monitoramento e Defesa contra Rogue DHCP e ARP Spoofing na Interface de Rede** | `tcpdump, arptables, ip neigh` |
| **14** | [`14-packet-drop-ebpf-xdp-ddos-shield/`](./14-packet-drop-ebpf-xdp-ddos-shield) | **Filtro de Descarte Ultrarrápido de Ataques DDoS com XDP (eBPF) no Driver** | `xdp, bpftool, ip link set xdp` |
| **15** | [`15-network-bond-failover-lldp-neighbor/`](./15-network-bond-failover-lldp-neighbor) | **Monitoramento de Vizinhança de Switches Físicos com LLDP (lldpd) e LACP** | `lldpcli, lldpd` |
| **16** | [`16-dynamic-dns-nsupdate-tsig-secure/`](./16-dynamic-dns-nsupdate-tsig-secure) | **Atualização Automatizada de Registros DNS com nsupdate e Autenticação TSIG** | `nsupdate, krb5, dig` |
| **17** | [`17-ip-multicast-routing-pim-sm/`](./17-ip-multicast-routing-pim-sm) | **Roteamento Multicast de Baixa Latência com smcroute e PIM-SM** | `smcroute, ip mroute, ss -u` |
| **18** | [`18-linux-router-frr-ospf-area-sync/`](./18-linux-router-frr-ospf-area-sync) | **Configuração de Roteador Linux Corporativo com FRR rodando OSPF em Múltiplas Áreas** | `vtysh, frr, systemctl` |
| **19** | [`19-tcpdump-sslkeylog-traffic-decryption/`](./19-tcpdump-sslkeylog-traffic-decryption) | **Captura de Tráfego de Rede Correlacionada com Chaves TLS (SSLKEYLOGFILE)** | `tcpdump, tshark, openssl` |
| **20** | [`20-network-latency-jitter-mtr-report/`](./20-network-latency-jitter-mtr-report) | **Auditor Contínuo de Latência, Perda de Pacotes e Jitter com MTR e Exportação JSON** | `mtr, awk, jq` |
