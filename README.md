# 🐧 Engenharia de Sistemas Linux & Administração de Servidores

<div align="center">

![Domain](https://img.shields.io/badge/Domain-Linux%20Kernel%20%2F%20POSIX-orange)
![Platform](https://img.shields.io/badge/Architecture-Production--Grade-success)
![Quality](https://img.shields.io/badge/Standard-Enterprise%20Ready-blue)

<p align="center">
  <b>Repositório abrangente de engenharia e administração de sistemas Linux corporativos: systemd, storage/LVM, redes, segurança, auditoria, serviços de infraestrutura e troubleshooting avançado.</b>
</p>

</div>

---

## 📌 Visão Geral

Este repositório faz parte da suíte de competências em **Linux Engineering, Cloud e Platform Engineering**, estruturado para refletir a maturidade e a profundidade técnica exigidas no mercado internacional de engenharia de software e infraestrutura.

A organização adota uma abordagem modular e declarativa, onde cada módulo isola um domínio específico de conhecimento prático e pronto para produção.

---

## 🏗️ Matriz Arquitetural dos Módulos

| # | Módulo | Foco Técnico | Subáreas em Destaque |
|---|---|---|---|
| **01** | [`01-administracao`](./01-administracao) | Administração de Sistemas e Gerenciamento do Host | `usuarios-grupos`, `processos-servicos` |
| **02** | [`02-seguranca`](./02-seguranca) | Segurança, Hardening e Auditoria | `firewall-iptables-nftables`, `selinux-apparmor` |
| **03** | [`03-storage`](./03-storage) | Storage, Particionamento e Sistemas de Arquivos | `particoes-lvm`, `nfs-samba` |
| **04** | [`04-redes`](./04-redes) | Redes, Protocolos e Conectividade | `tcp-ip`, `diagnostico` |
| **05** | [`05-servicos`](./05-servicos) | Serviços Essenciais de Infraestrutura | `nginx-apache`, `chrony` |
| **06** | [`06-monitoramento`](./06-monitoramento) | Monitoramento e Coleta de Telemetria no Host | `metricas`, `diagnostico` |
| **07** | [`07-automacao`](./07-automacao) | Automação Operacional de Infraestrutura | `ansible`, `bash` |
| **08** | [`08-troubleshooting`](./08-troubleshooting) | Guia de Resolução de Problemas (Troubleshooting) | `cpu-memoria`, `boot-systemd` |
| **09** | [`09-projetos-laboratorio`](./09-projetos-laboratorio) | Laboratórios Práticos e Projetos de Engenharia | `servidor-web-seguro`, `auditoria-hardening-cis` |

---

## 🛡️ Padrões de Engenharia & Segurança

1. **Abordagem Declarativa:** Toda configuração de infraestrutura, cluster ou serviço deve ser versionada como código.
2. **Segurança em Primeiro Lugar:** Nenhum segredo, certificado ou credencial real deve ser commitado no repositório.
3. **Reproducibilidade:** Ambientes devem ser facilmente reconstituídos via scripts ou manifests declarativos.

---

## 👤 Autor e Manutenção

- **Mantenedor:** Junio Silvestre
- **Repositório:** [https://github.com/JunioSilvestre/Linux.git](https://github.com/JunioSilvestre/Linux.git)
