# 01 — Roteamento Baseado em Políticas (Policy Routing) com Múltiplas Tabelas no Linux

## 🏢 Cenário de Produção e Vida Real
Servidores com múltiplos uplinks roteando tráfego com base no IP de origem ou marcação de pacote.

## 🚀 Arquitetura e Engenharia Linux
Implementação de engenharia avançada de sistemas Linux para produção, assegurando confiabilidade, resiliência, observabilidade e adesão estrita aos padrões de conformidade corporativa.

## 🛠️ Ferramentas e Utilitários Nativos Utilizados
`ip rule, ip route, rt_tables`

## 📌 Exemplo de Execução CLI
```bash
ip rule add from 10.0.1.100 table 100
```
