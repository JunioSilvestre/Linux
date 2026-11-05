# 10 — Criação de Jail Chroot Segura para Acessos SFTP com Isolamento Estrito

## 🏢 Cenário de Produção e Vida Real
Compartilhamento de arquivos com fornecedores terceiros sem permitir escape de shell.

## 🚀 Arquitetura e Engenharia Linux
Implementação de engenharia avançada de sistemas Linux para produção, assegurando confiabilidade, resiliência, observabilidade e adesão estrita aos padrões de conformidade corporativa.

## 🛠️ Ferramentas e Utilitários Nativos Utilizados
`sshd_config, chroot, setfacl`

## 📌 Exemplo de Execução CLI
```bash
sshd -t && systemctl reload sshd
```
