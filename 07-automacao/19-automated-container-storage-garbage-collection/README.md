# 19 — Coletor de Lixo e Higienização de Storage de Runtimes de Containers (crictl/docker)

## 🏢 Cenário de Produção e Vida Real
Purga de volumes anônimos, imagens não referenciadas e caches de build acumulados.

## 🚀 Arquitetura e Engenharia Linux
Implementação de engenharia avançada de sistemas Linux para produção, assegurando confiabilidade, resiliência, observabilidade e adesão estrita aos padrões de conformidade corporativa.

## 🛠️ Ferramentas e Utilitários Nativos Utilizados
`crictl rmi --prune, docker system prune`

## 📌 Exemplo de Execução CLI
```bash
./clean_container_storage.sh --threshold 85
```
