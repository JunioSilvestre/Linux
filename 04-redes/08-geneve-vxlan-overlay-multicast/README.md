# 08 — Túneis Overlay GENEVE e VXLAN com Sinalização Multicast para Redes SD-WAN

## 🏢 Cenário de Produção e Vida Real
Interconexão de data centers através de túneis encapsulados com metadados de telemetria.

## 🚀 Arquitetura e Engenharia Linux
Implementação de engenharia avançada de sistemas Linux para produção, assegurando confiabilidade, resiliência, observabilidade e adesão estrita aos padrões de conformidade corporativa.

## 🛠️ Ferramentas e Utilitários Nativos Utilizados
`ip link, bridge fdb`

## 📌 Exemplo de Execução CLI
```bash
ip link add dev geneve0 type geneve id 42 remote 192.168.1.5
```
