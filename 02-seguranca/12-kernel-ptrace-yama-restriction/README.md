# 12 — Bloqueio de Injeção de Código em Memória com Restrição Yama Ptrace

## 🏢 Cenário de Produção e Vida Real
Prevenção de ataques de leitura de memória de processos privilegiados por usuários comuns.

## 🚀 Arquitetura e Engenharia Linux
Implementação de engenharia avançada de sistemas Linux para produção, assegurando confiabilidade, resiliência, observabilidade e adesão estrita aos padrões de conformidade corporativa.

## 🛠️ Ferramentas e Utilitários Nativos Utilizados
`sysctl, /proc/sys/kernel/yama/ptrace_scope`

## 📌 Exemplo de Execução CLI
```bash
sysctl -w kernel.yama.ptrace_scope=2
```
