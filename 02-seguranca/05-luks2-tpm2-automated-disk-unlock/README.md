# 05 — Desbloqueio Seguro de Discos LUKS2 com Chip TPM 2.0 (Trusted Platform Module)

## 🏢 Cenário de Produção e Vida Real
Proteção de dados em repouso contra roubo físico de servidores sem exigir digitação manual de senha no boot.

## 🚀 Arquitetura e Engenharia Linux
Implementação de engenharia avançada de sistemas Linux para produção, assegurando confiabilidade, resiliência, observabilidade e adesão estrita aos padrões de conformidade corporativa.

## 🛠️ Ferramentas e Utilitários Nativos Utilizados
`systemd-cryptenroll, tpm2-tools, cryptsetup`

## 📌 Exemplo de Execução CLI
```bash
systemd-cryptenroll --tpm2-device=auto /dev/nvme0n1p3
```
