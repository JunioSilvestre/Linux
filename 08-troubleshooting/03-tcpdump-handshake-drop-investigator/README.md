# 03 — Investigador de Descarte de Pacotes no Three-Way Handshake TCP com tcpdump

## 🏢 Cenário de Produção e Vida Real
Clientes relatando timeouts de conexão que não aparecem nos logs da aplicação.

## 🚀 Arquitetura e Engenharia Linux
Implementação de engenharia avançada de sistemas Linux para produção, assegurando confiabilidade, resiliência, observabilidade e adesão estrita aos padrões de conformidade corporativa.

## 🛠️ Ferramentas e Utilitários Nativos Utilizados
`tcpdump, tshark, awk`

## 📌 Exemplo de Execução CLI
```bash
tcpdump -i eth0 'tcp[tcpflags] & (tcp-syn) != 0'
```
