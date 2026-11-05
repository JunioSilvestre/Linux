# 10 — Sincronização Distribuída de IPs Banidos pelo Fail2ban com Cluster Redis

## 🏢 Cenário de Produção e Vida Real
Ataque contra um nó bloqueado simultaneamente em todos os outros servidores da empresa.

## 🚀 Arquitetura e Engenharia Linux
Implementação de engenharia avançada de sistemas Linux para produção, assegurando confiabilidade, resiliência, observabilidade e adesão estrita aos padrões de conformidade corporativa.

## 🛠️ Ferramentas e Utilitários Nativos Utilizados
`fail2ban, redis-cli, nftables`

## 📌 Exemplo de Execução CLI
```bash
./fail2ban_redis_sync.sh --action broadcast-ban
```
