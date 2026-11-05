# 19 — Firewall de Chamadas de Sistema (Syscalls) com Seccomp BPF e Restrição Estrita

## 🏢 Cenário de Produção e Vida Real
Bloqueio de chamadas perigosas como reboot, kexec_load e swapon em aplicações web.

## 🚀 Arquitetura e Engenharia Linux
Implementação de engenharia avançada de sistemas Linux para produção, assegurando confiabilidade, resiliência, observabilidade e adesão estrita aos padrões de conformidade corporativa.

## 🛠️ Ferramentas e Utilitários Nativos Utilizados
`seccomp, bpf, prctl`

## 📌 Exemplo de Execução CLI
```bash
./apply_seccomp_filter.sh --profile webserver
```
