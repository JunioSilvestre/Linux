# 13 — Monitoramento e Defesa contra Rogue DHCP e ARP Spoofing na Interface de Rede

## 🏢 Cenário de Produção e Vida Real
Garantia de que nenhuma estação maliciosa sequestre o tráfego do gateway da rede local.

## 🚀 Arquitetura e Engenharia Linux
Implementação de engenharia avançada de sistemas Linux para produção, assegurando confiabilidade, resiliência, observabilidade e adesão estrita aos padrões de conformidade corporativa.

## 🛠️ Ferramentas e Utilitários Nativos Utilizados
`tcpdump, arptables, ip neigh`

## 📌 Exemplo de Execução CLI
```bash
tcpdump -i eth0 -n -p port 67 or port 68
```
