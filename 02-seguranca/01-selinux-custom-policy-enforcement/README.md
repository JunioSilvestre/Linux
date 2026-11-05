# 01 — Criação e Compilação de Políticas Customizadas do SELinux para Daemons

## 🏢 Cenário de Produção e Vida Real
Serviços rodando em portas não padrão bloqueados pelo SELinux sem precisar desativá-lo.

## 🚀 Arquitetura e Engenharia Linux
Implementação de engenharia avançada de sistemas Linux para produção, assegurando confiabilidade, resiliência, observabilidade e adesão estrita aos padrões de conformidade corporativa.

## 🛠️ Ferramentas e Utilitários Nativos Utilizados
`audit2allow, semodule, semanage`

## 📌 Exemplo de Execução CLI
```bash
semanage port -a -t http_port_t -p tcp 8088
```
