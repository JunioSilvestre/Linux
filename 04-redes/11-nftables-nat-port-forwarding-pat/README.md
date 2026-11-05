# 11 — Firewall de Borda e Roteador NAT/PAT de Alta Velocidade com nftables

## 🏢 Cenário de Produção e Vida Real
Substituição moderna de iptables para tradução de endereços de rede em roteadores Linux.

## 🚀 Arquitetura e Engenharia Linux
Implementação de engenharia avançada de sistemas Linux para produção, assegurando confiabilidade, resiliência, observabilidade e adesão estrita aos padrões de conformidade corporativa.

## 🛠️ Ferramentas e Utilitários Nativos Utilizados
`nft, nftables.conf, conntrack`

## 📌 Exemplo de Execução CLI
```bash
nft add rule ip nat prerouting dnat to 10.0.0.5:80
```
