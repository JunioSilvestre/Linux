# 16 — Concessão Temporária de Acesso Administrativo com Expiração Automática

## 🏢 Cenário de Produção e Vida Real
Permissão sudo concedida por 2 horas para resolução de incidentes com revogação via timer.

## 🚀 Arquitetura e Engenharia Linux
Implementação de engenharia avançada de sistemas Linux para produção, assegurando confiabilidade, resiliência, observabilidade e adesão estrita aos padrões de conformidade corporativa.

## 🛠️ Ferramentas e Utilitários Nativos Utilizados
`at, visudo, logger`

## 📌 Exemplo de Execução CLI
```bash
./grant_sudo_temp.sh --user dev.silva --hours 2
```
