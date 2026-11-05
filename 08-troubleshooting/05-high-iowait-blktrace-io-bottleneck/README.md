# 05 — Localizador da Causa Raiz de Alto I/O Wait com blktrace e btt

## 🏢 Cenário de Produção e Vida Real
Identificação de quais setores e arquivos do disco estão sofrendo lentidão de leitura.

## 🚀 Arquitetura e Engenharia Linux
Implementação de engenharia avançada de sistemas Linux para produção, assegurando confiabilidade, resiliência, observabilidade e adesão estrita aos padrões de conformidade corporativa.

## 🛠️ Ferramentas e Utilitários Nativos Utilizados
`blktrace, btt, iostat`

## 📌 Exemplo de Execução CLI
```bash
blktrace -d /dev/sda -w 10
```
