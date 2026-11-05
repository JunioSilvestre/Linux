# 01 — Gestão de Fatias de Recursos (Resource Slices) com cgroups v2 no Systemd

## 🏢 Cenário de Produção e Vida Real
Controle rigoroso de limites de memória e CPU por tipo de serviço (system.slice vs user.slice).

## 🚀 Arquitetura e Engenharia Linux
Implementação de engenharia avançada de sistemas Linux para produção, assegurando confiabilidade, resiliência, observabilidade e adesão estrita aos padrões de conformidade corporativa.

## 🛠️ Ferramentas e Utilitários Nativos Utilizados
`systemctl set-property, systemd-cgls, cgroups v2`

## 📌 Exemplo de Execução CLI
```bash
systemctl set-property app.slice MemoryMax=4G CPUQuota=200%
```
