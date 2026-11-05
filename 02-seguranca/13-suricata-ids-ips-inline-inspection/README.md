# 13 — Configuração de IDS/IPS Suricata em Modo Inline com NFQueue do Linux

## 🏢 Cenário de Produção e Vida Real
Inspeção profunda de pacotes (DPI) em servidores de borda para bloqueio de exploits.

## 🚀 Arquitetura e Engenharia Linux
Implementação de engenharia avançada de sistemas Linux para produção, assegurando confiabilidade, resiliência, observabilidade e adesão estrita aos padrões de conformidade corporativa.

## 🛠️ Ferramentas e Utilitários Nativos Utilizados
`suricata, iptables, nfq`

## 📌 Exemplo de Execução CLI
```bash
suricata -c /etc/suricata/suricata.yaml -q 0
```
