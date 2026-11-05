# 03 — Monitoramento Contínuo de Integridade de Arquivos (FIM) com auditd e ausearch

## 🏢 Cenário de Produção e Vida Real
Detecção instantânea de modificações em arquivos de configuração sensíveis com contexto de PID e UID.

## 🚀 Arquitetura e Engenharia Linux
Implementação de engenharia avançada de sistemas Linux para produção, assegurando confiabilidade, resiliência, observabilidade e adesão estrita aos padrões de conformidade corporativa.

## 🛠️ Ferramentas e Utilitários Nativos Utilizados
`auditctl, ausearch, auditd.rules`

## 📌 Exemplo de Execução CLI
```bash
ausearch -f /etc/shadow -i
```
