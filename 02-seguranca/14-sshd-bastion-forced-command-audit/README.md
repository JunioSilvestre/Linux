# 14 — Configuração de Bastion Host SSH com Forced Commands e Sessões Imutáveis

## 🏢 Cenário de Produção e Vida Real
Restrição de acesso a servidores onde engenheiros executam apenas rotinas pré-autorizadas.

## 🚀 Arquitetura e Engenharia Linux
Implementação de engenharia avançada de sistemas Linux para produção, assegurando confiabilidade, resiliência, observabilidade e adesão estrita aos padrões de conformidade corporativa.

## 🛠️ Ferramentas e Utilitários Nativos Utilizados
`sshd_config, script, logger`

## 📌 Exemplo de Execução CLI
```bash
sshd_config: ForceCommand /usr/local/bin/restricted-menu
```
