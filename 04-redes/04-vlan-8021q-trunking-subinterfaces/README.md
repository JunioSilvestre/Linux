# 04 — Criação e Gestão de Troncos de Rede e Subinterfaces VLAN 802.1Q

## 🏢 Cenário de Produção e Vida Real
Segmentação de tráfego de gerenciamento, dados e DMZ na mesma placa de rede física.

## 🚀 Arquitetura e Engenharia Linux
Implementação de engenharia avançada de sistemas Linux para produção, assegurando confiabilidade, resiliência, observabilidade e adesão estrita aos padrões de conformidade corporativa.

## 🛠️ Ferramentas e Utilitários Nativos Utilizados
`ip link, modprobe 8021q`

## 📌 Exemplo de Execução CLI
```bash
ip link add link eth0 name eth0.100 type vlan id 100
```
