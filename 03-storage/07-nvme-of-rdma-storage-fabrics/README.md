# 07 — Configuração de Storage NVMe-over-Fabrics (NVMe-oF) via RDMA / TCP

## 🏢 Cenário de Produção e Vida Real
Acesso a storages remotos com latência próxima à de discos conectados localmente no barramento PCIe.

## 🚀 Arquitetura e Engenharia Linux
Implementação de engenharia avançada de sistemas Linux para produção, assegurando confiabilidade, resiliência, observabilidade e adesão estrita aos padrões de conformidade corporativa.

## 🛠️ Ferramentas e Utilitários Nativos Utilizados
`nvme-cli, modprobe nvme-rdma`

## 📌 Exemplo de Execução CLI
```bash
nvme connect -t tcp -a 10.0.1.50 -s 4420 -n nqn.target
```
