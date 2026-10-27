# 04-redes — Redes, Protocolos e Conectividade

Pilha TCP/IP em Linux, roteamento, VLANs, túneis VPN, diagnósticos e resolução de nomes.

## 📂 Subáreas
- [`tcp-ip/`](./tcp-ip) — **Stack:** `ip route, ip addr, ss, sysctl network tunning` — Gerenciamento da pilha de rede, interfaces, MTU e parâmetros TCP de alta performance.
- [`routing-vlan/`](./routing-vlan) — **Stack:** `ip route, vlan tagging, bridge-utils, bond/team` — Roteamento estático, criação de pontes virtuais e agregação de interfaces.
- [`dns-dhcp/`](./dns-dhcp) — **Stack:** `systemd-resolved, /etc/hosts, resolv.conf, bind9` — Mecanismos de resolução de nomes, cache DNS e serviços de atribuição de IP.
- [`vpn/`](./vpn) — **Stack:** `wireguard, openvpn, ipsec` — Comunicação criptografada site-to-site e client-to-gateway.
- [`diagnostico/`](./diagnostico) — **Stack:** `tcpdump, traceroute, ping, mtr, nc, curl` — Identificação de gargalos, perda de pacotes e análise profunda de tráfego.

## 📌 Guia de Execução & Padrões
- Todas as implementações desta pasta seguem os padrões de produção estabelecidos para Linux.
- Consulte os READMEs de cada subárea para detalhes sobre ferramentas e boas práticas.
