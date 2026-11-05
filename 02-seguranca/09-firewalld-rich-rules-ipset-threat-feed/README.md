# 09 — Firewall Dinâmico com Firewalld Rich Rules e Conjuntos IPSet de Threat Intel

## 🏢 Cenário de Produção e Vida Real
Bloqueio automatizado de redes maliciosas e botnets conhecidas em tempo real.

## 🚀 Arquitetura e Engenharia Linux
Implementação de engenharia avançada de sistemas Linux para produção, assegurando confiabilidade, resiliência, observabilidade e adesão estrita aos padrões de conformidade corporativa.

## 🛠️ Ferramentas e Utilitários Nativos Utilizados
`firewall-cmd, ipset, curl`

## 📌 Exemplo de Execução CLI
```bash
firewall-cmd --permanent --add-rich-rule='rule family="ipv4" source ipset="threat_list" drop'
```
