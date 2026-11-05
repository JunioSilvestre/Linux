# 07 — Criação de Bridges Linux com Isolamento de Portas e Filtragem L2 com ebtables

## 🏢 Cenário de Produção e Vida Real
Rede virtual para máquinas virtuais e containers impedindo comunicação direta L2 entre clientes.

## 🚀 Arquitetura e Engenharia Linux
Implementação de engenharia avançada de sistemas Linux para produção, assegurando confiabilidade, resiliência, observabilidade e adesão estrita aos padrões de conformidade corporativa.

## 🛠️ Ferramentas e Utilitários Nativos Utilizados
`brctl, ip link, ebtables`

## 📌 Exemplo de Execução CLI
```bash
ip link add name br0 type bridge
```
