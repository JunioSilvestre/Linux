# 17 — Auditoria e Remoção de Linux Capabilities Desnecessárias em Binários do Sistema

## 🏢 Cenário de Produção e Vida Real
Serviços que rodam com privilégios de rede sem necessitar de controle total de sistema.

## 🚀 Arquitetura e Engenharia Linux
Implementação de engenharia avançada de sistemas Linux para produção, assegurando confiabilidade, resiliência, observabilidade e adesão estrita aos padrões de conformidade corporativa.

## 🛠️ Ferramentas e Utilitários Nativos Utilizados
`getcap, setcap, capsh`

## 📌 Exemplo de Execução CLI
```bash
setcap 'cap_net_bind_service=+ep' /usr/local/bin/proxy
```
