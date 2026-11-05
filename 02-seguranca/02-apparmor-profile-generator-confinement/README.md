# 02 — Confinamento Estrito de Aplicações e Daemons Web com Perfis AppArmor

## 🏢 Cenário de Produção e Vida Real
Garantir que um container ou serviço comprometido não consiga ler arquivos fora do seu diretório.

## 🚀 Arquitetura e Engenharia Linux
Implementação de engenharia avançada de sistemas Linux para produção, assegurando confiabilidade, resiliência, observabilidade e adesão estrita aos padrões de conformidade corporativa.

## 🛠️ Ferramentas e Utilitários Nativos Utilizados
`aa-genprof, aa-complain, aa-enforce`

## 📌 Exemplo de Execução CLI
```bash
aa-enforce /etc/apparmor.d/usr.bin.nginx
```
