# 02 — Isolamento Completo de Processos em Network Namespaces com VPN Dedicada

## 🏢 Cenário de Produção e Vida Real
Execução de um único processo roteado por VPN enquanto o restante do servidor usa a internet local.

## 🚀 Arquitetura e Engenharia Linux
Implementação de engenharia avançada de sistemas Linux para produção, assegurando confiabilidade, resiliência, observabilidade e adesão estrita aos padrões de conformidade corporativa.

## 🛠️ Ferramentas e Utilitários Nativos Utilizados
`ip netns, ip link, wg-quick`

## 📌 Exemplo de Execução CLI
```bash
ip netns exec vpn-ns curl ifconfig.me
```
