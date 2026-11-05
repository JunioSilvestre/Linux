# 03 — Balanceador de Carga HAProxy Camada 4 com Stick Tables e Limitação de Taxa

## 🏢 Cenário de Produção e Vida Real
Proteção de portas de banco de dados e APIs gRPC contra abusos de conexão.

## 🚀 Arquitetura e Engenharia Linux
Implementação de engenharia avançada de sistemas Linux para produção, assegurando confiabilidade, resiliência, observabilidade e adesão estrita aos padrões de conformidade corporativa.

## 🛠️ Ferramentas e Utilitários Nativos Utilizados
`haproxy, socat, awk`

## 📌 Exemplo de Execução CLI
```bash
echo 'show info' | socat stdio /var/run/haproxy.sock
```
