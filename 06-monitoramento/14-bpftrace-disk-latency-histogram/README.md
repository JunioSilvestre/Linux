# 14 — Histograma de Latência de Bloco em Tempo Real com bpftrace (eBPF)

## 🏢 Cenário de Produção e Vida Real
Visualização gráfica da distribuição de latência das operações de I/O dos discos.

## 🚀 Arquitetura e Engenharia Linux
Implementação de engenharia avançada de sistemas Linux para produção, assegurando confiabilidade, resiliência, observabilidade e adesão estrita aos padrões de conformidade corporativa.

## 🛠️ Ferramentas e Utilitários Nativos Utilizados
`bpftrace, eBPF`

## 📌 Exemplo de Execução CLI
```bash
bpftrace -e 'kprobe:vfs_read { @start[tid] = nsecs; }'
```
