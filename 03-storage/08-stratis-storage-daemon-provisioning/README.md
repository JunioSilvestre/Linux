# 08 — Gerenciamento Simplificado de Storage em Camadas com Stratis Daemon

## 🏢 Cenário de Produção e Vida Real
Provisionamento de pools híbridos (NVMe + HDD) com thin provisioning e snapshots.

## 🚀 Arquitetura e Engenharia Linux
Implementação de engenharia avançada de sistemas Linux para produção, assegurando confiabilidade, resiliência, observabilidade e adesão estrita aos padrões de conformidade corporativa.

## 🛠️ Ferramentas e Utilitários Nativos Utilizados
`stratis, stratis-cli, systemctl`

## 📌 Exemplo de Execução CLI
```bash
stratis pool create pool1 /dev/sdb /dev/sdc
```
