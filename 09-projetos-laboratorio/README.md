# 09-projetos-laboratorio — Laboratórios e Projetos Integradores de Engenharia Linux

Projetos completos de ponta a ponta integrando alta disponibilidade, virtualização KVM, automação de rede, storage SAN e segurança corporativa.

---

## 🏛️ Trilha de Projetos Práticos de Engenharia Linux Nível Sênior (20 Projetos Reais)

| # | Projeto | Título / Foco Técnico | Ferramentas Chave |
|---|---|---|---|
| **01** | [`01-kvm-qemu-automated-vm-hypervisor/`](./01-kvm-qemu-automated-vm-hypervisor) | **Provisionador Autônomo de Máquinas Virtuais KVM/QEMU com Cloud-Init e Bridges** | `virsh, qemu-img, virt-install` |
| **02** | [`02-pki-three-tier-ca-enterprise-setup/`](./02-pki-three-tier-ca-enterprise-setup) | **Construção e Governança de Infraestrutura de Chaves Públicas (PKI) de 3 Camadas** | `openssl, date, shred` |
| **03** | [`03-drbd-corosync-pacemaker-ha-cluster/`](./03-drbd-corosync-pacemaker-ha-cluster) | **Cluster de Alta Disponibilidade Ativo-Passivo com DRBD, Corosync e Pacemaker** | `crm, pcs, drbdadm, corosync` |
| **04** | [`04-centralized-syslog-elk-vector-pipeline/`](./04-centralized-syslog-elk-vector-pipeline) | **Concentrador Centralizado de Logs de Alta Escala com Vector e Elasticsearch** | `vector, elasticsearch, curl` |
| **05** | [`05-linux-router-bgp-anycast-dns-cluster/`](./05-linux-router-bgp-anycast-dns-cluster) | **Roteador Linux com BGP Anycast para Cluster de Servidores DNS Altamente Disponíveis** | `bird, bind9, ip addr` |
| **06** | [`06-zero-trust-ssh-bastion-teleport-alternative/`](./06-zero-trust-ssh-bastion-teleport-alternative) | **Bastion Host Zero Trust com Sessões Gravadas, Autenticação MFA e RBAC** | `script, pam_oath, ttyrec` |
| **07** | [`07-baremetal-pxe-ipxe-automated-installer/`](./07-baremetal-pxe-ipxe-automated-installer) | **Servidor de Boot PXE / iPXE com Inicialização Automatizada de Distribuições Linux** | `dnsmasq, tftp, ipxe, syslinux` |
| **08** | [`08-iscsi-target-san-ceph-gateway/`](./08-iscsi-target-san-ceph-gateway) | **Gateway SAN Corporativo com LIO iSCSI Target Exportando Volumes Distribuídos Ceph** | `targetcli, rbd, iscsiadm` |
| **09** | [`09-wireguard-site-to-site-redundant-mesh/`](./09-wireguard-site-to-site-redundant-mesh) | **Malha de VPN Site-to-Site Redundante com WireGuard e Failover Dinâmico OSPF** | `wg, frr, ip` |
| **10** | [`10-prometheus-grafana-linux-monitoring-stack/`](./10-prometheus-grafana-linux-monitoring-stack) | **Stack Completa de Observabilidade Linux com Prometheus, Node Exporter e Grafana** | `prometheus, grafana-server, curl` |
| **11** | [`11-immutable-hardened-os-golden-image/`](./11-immutable-hardened-os-golden-image) | **Pipeline de Construção de Imagens de SO Imutáveis e Blindadas (CIS L2) com Packer** | `packer, qemu, ansible` |
| **12** | [`12-local-package-mirror-airgapped-sync/`](./12-local-package-mirror-airgapped-sync) | **Servidor de Espelhamento Local de Repositórios APT e DNF com Assinatura GPG** | `apt-mirror, reposync, gpg` |
| **13** | [`13-multi-tenant-sftp-server-chroot-quotas/`](./13-multi-tenant-sftp-server-chroot-quotas) | **Servidor SFTP Multi-Tenant com Chroot, Cotas Rígidas e Monitoramento em Tempo Real** | `sshd, setfacl, xfs_quota` |
| **14** | [`14-disaster-recovery-baremetal-rear-nfs/`](./14-disaster-recovery-baremetal-rear-nfs) | **Laboratório de Recuperação de Desastres Bare-Metal com Relax-and-Recover (ReaR)** | `rear, nfs-common, grub2` |
| **15** | [`15-haproxy-keepalived-waf-modsecurity/`](./15-haproxy-keepalived-waf-modsecurity) | **Borda Web de Alta Disponibilidade com HAProxy, Keepalived e WAF ModSecurity** | `haproxy, keepalived, modsecurity` |
| **16** | [`16-autofs-nfs4-kerberos-enterprise-storage/`](./16-autofs-nfs4-kerberos-enterprise-storage) | **Montagem Automática de Diretórios de Rede Corporativos com AutoFS e NFSv4 Kerberos** | `autofs, krb5-user, nfs-common` |
| **17** | [`17-linux-traffic-generator-network-stress/`](./17-linux-traffic-generator-network-stress) | **Gerador de Tráfego de Alta Vazão e Testador de Stress de Switches de Rede** | `trafgen, iperf3, tc` |
| **18** | [`18-vault-consul-secure-infrastructure-mesh/`](./18-vault-consul-secure-infrastructure-mesh) | **Cluster de Segredos e Configurações Distribuídas com HashiCorp Vault e Consul** | `vault, consul, systemctl` |
| **19** | [`19-ebpf-based-firewall-observability-agent/`](./19-ebpf-based-firewall-observability-agent) | **Agente Leve de Observabilidade e Filtragem de Rede Baseado em Programas eBPF** | `bpftool, clang, llvm` |
| **20** | [`20-mission-critical-high-availability-watchdog/`](./20-mission-critical-high-availability-watchdog) | **Orquestrador Autônomo de Alta Disponibilidade e Auto-Recuperação de Serviços Críticos** | `systemd, ss, ip, logger` |
