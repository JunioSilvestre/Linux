# 08 — Investigação Forense de Esgotamento de File Descriptors por Processo

## 🏢 Cenário de Produção e Vida Real
Mapeamento de conexões TCP, arquivos abertos e pipes que causaram 'Too many open files'.

## 🚀 Arquitetura e Engenharia Linux
Implementação de engenharia avançada de sistemas Linux para produção, assegurando confiabilidade, resiliência, observabilidade e adesão estrita aos padrões de conformidade corporativa.

## 🛠️ Ferramentas e Utilitários Nativos Utilizados
`ls -l /proc/*/fd, lsof, awk`

## 📌 Exemplo de Execução CLI
```bash
./investigate_fd_exhaustion.sh --pid 2045
```
