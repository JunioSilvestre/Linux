# 13 — Servidor SFTP Multi-Tenant com Chroot, Cotas Rígidas e Monitoramento em Tempo Real

## 🏢 Cenário de Produção e Vida Real
Isolamento absoluto de pastas de clientes com controle estrito de espaço em disco.

## 🚀 Arquitetura e Engenharia Linux
Implementação de engenharia avançada de sistemas Linux para produção, assegurando confiabilidade, resiliência, observabilidade e adesão estrita aos padrões de conformidade corporativa.

## 🛠️ Ferramentas e Utilitários Nativos Utilizados
`sshd, setfacl, xfs_quota`

## 📌 Exemplo de Execução CLI
```bash
./create_sftp_tenant.sh --client client_a --quota 100G
```
