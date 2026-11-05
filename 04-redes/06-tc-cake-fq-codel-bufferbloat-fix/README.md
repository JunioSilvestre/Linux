# 06 — Mitigação de Bufferbloat e QoS com Algoritmo CAKE e FQ-CoDel no Linux tc

## 🏢 Cenário de Produção e Vida Real
Eliminação de latência alta em conexões saturadas priorizando pacotes interativos e DNS.

## 🚀 Arquitetura e Engenharia Linux
Implementação de engenharia avançada de sistemas Linux para produção, assegurando confiabilidade, resiliência, observabilidade e adesão estrita aos padrões de conformidade corporativa.

## 🛠️ Ferramentas e Utilitários Nativos Utilizados
`tc qdisc, ip link`

## 📌 Exemplo de Execução CLI
```bash
tc qdisc add dev eth0 root cake bandwidth 100mbit
```
