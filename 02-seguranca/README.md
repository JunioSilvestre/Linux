# 02-seguranca — Segurança Defensiva, Hardening e Auditoria Linux

Projetos práticos de segurança do kernel, SELinux/AppArmor, auditd avançado, chaves criptográficas, firewalls e conformidade CIS.

---

## 🏛️ Trilha de Projetos Práticos de Engenharia Linux Nível Sênior (20 Projetos Reais)

| # | Projeto | Título / Foco Técnico | Ferramentas Chave |
|---|---|---|---|
| **01** | [`01-selinux-custom-policy-enforcement/`](./01-selinux-custom-policy-enforcement) | **Criação e Compilação de Políticas Customizadas do SELinux para Daemons** | `audit2allow, semodule, semanage` |
| **02** | [`02-apparmor-profile-generator-confinement/`](./02-apparmor-profile-generator-confinement) | **Confinamento Estrito de Aplicações e Daemons Web com Perfis AppArmor** | `aa-genprof, aa-complain, aa-enforce` |
| **03** | [`03-auditd-fim-file-integrity-monitoring/`](./03-auditd-fim-file-integrity-monitoring) | **Monitoramento Contínuo de Integridade de Arquivos (FIM) com auditd e ausearch** | `auditctl, ausearch, auditd.rules` |
| **04** | [`04-cis-benchmark-automated-remediation/`](./04-cis-benchmark-automated-remediation) | **Script de Remediação Automatizada de Não-Conformidades CIS Benchmark Nível 2** | `cis-cat, lynis, sysctl, chmod` |
| **05** | [`05-luks2-tpm2-automated-disk-unlock/`](./05-luks2-tpm2-automated-disk-unlock) | **Desbloqueio Seguro de Discos LUKS2 com Chip TPM 2.0 (Trusted Platform Module)** | `systemd-cryptenroll, tpm2-tools, cryptsetup` |
| **06** | [`06-ssh-hardware-security-keys-fido2/`](./06-ssh-hardware-security-keys-fido2) | **Autenticação SSH Restrita a Chaves Criptográficas de Hardware FIDO2 (YubiKey)** | `ssh-keygen, libfido2, sshd_config` |
| **07** | [`07-rootkit-ebpf-hidden-process-hunter/`](./07-rootkit-ebpf-hidden-process-hunter) | **Caçador de Rootkits e Processos Ocultos via eBPF e Inspeção de Syscalls** | `bpftool, unhide, rkhunter` |
| **08** | [`08-usbguard-device-authorization-policy/`](./08-usbguard-device-authorization-policy) | **Bloqueio e Autorização Criptográfica de Dispositivos USB com USBGuard** | `usbguard, usbguard-tools` |
| **09** | [`09-firewalld-rich-rules-ipset-threat-feed/`](./09-firewalld-rich-rules-ipset-threat-feed) | **Firewall Dinâmico com Firewalld Rich Rules e Conjuntos IPSet de Threat Intel** | `firewall-cmd, ipset, curl` |
| **10** | [`10-fail2ban-distributed-redis-sync/`](./10-fail2ban-distributed-redis-sync) | **Sincronização Distribuída de IPs Banidos pelo Fail2ban com Cluster Redis** | `fail2ban, redis-cli, nftables` |
| **11** | [`11-aide-automated-database-update/`](./11-aide-automated-database-update) | **Verificação Automatizada de Hash SHA-512 de Arquivos do Sistema com AIDE** | `aide, sha512sum, logger` |
| **12** | [`12-kernel-ptrace-yama-restriction/`](./12-kernel-ptrace-yama-restriction) | **Bloqueio de Injeção de Código em Memória com Restrição Yama Ptrace** | `sysctl, /proc/sys/kernel/yama/ptrace_scope` |
| **13** | [`13-suricata-ids-ips-inline-inspection/`](./13-suricata-ids-ips-inline-inspection) | **Configuração de IDS/IPS Suricata em Modo Inline com NFQueue do Linux** | `suricata, iptables, nfq` |
| **14** | [`14-sshd-bastion-forced-command-audit/`](./14-sshd-bastion-forced-command-audit) | **Configuração de Bastion Host SSH com Forced Commands e Sessões Imutáveis** | `sshd_config, script, logger` |
| **15** | [`15-clamav-on-access-systemd-scan/`](./15-clamav-on-access-systemd-scan) | **Varredura Antivírus em Tempo Real com ClamAV On-Access Scan e Fanotify** | `clamd, clamonacc, fanotify` |
| **16** | [`16-cryptography-post-quantum-openssh/`](./16-cryptography-post-quantum-openssh) | **Ativação de Criptografia Pós-Quântica Híbrida (sntrup761x25519) no OpenSSH** | `sshd_config, ssh, openssl` |
| **17** | [`17-linux-capabilities-drop-daemons/`](./17-linux-capabilities-drop-daemons) | **Auditoria e Remoção de Linux Capabilities Desnecessárias em Binários do Sistema** | `getcap, setcap, capsh` |
| **18** | [`18-shadow-password-sha512-rounds-tuning/`](./18-shadow-password-sha512-rounds-tuning) | **Aumento de Rondas Criptográficas de Hash de Senha em /etc/shadow** | `login.defs, authselect, crypt` |
| **19** | [`19-ebpf-seccomp-syscall-firewall/`](./19-ebpf-seccomp-syscall-firewall) | **Firewall de Chamadas de Sistema (Syscalls) com Seccomp BPF e Restrição Estrita** | `seccomp, bpf, prctl` |
| **20** | [`20-pci-dss-compliance-scanner-evidence/`](./20-pci-dss-compliance-scanner-evidence) | **Coletor de Evidências Técnicas e Verificação de Requisitos PCI-DSS para Linux** | `lynis, openssl, tar, gpg` |
