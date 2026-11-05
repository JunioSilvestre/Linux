# 05-servicos — Serviços de Infraestrutura, Daemons e Servidores

Projetos em Bash para provisionamento e gestão de serviços essenciais: DNS Bind9, Web Nginx/Apache, Bancos PostgreSQL, Proxy HAProxy e NTP Chrony.

---

## 🏛️ Trilha de Projetos Práticos de Engenharia Linux Nível Sênior (20 Projetos Reais)

| # | Projeto | Título / Foco Técnico | Ferramentas Chave |
|---|---|---|---|
| **01** | [`01-bind9-authoritative-dnssec-signing/`](./01-bind9-authoritative-dnssec-signing) | **Servidor DNS Autoritativo Bind9 com Assinatura Automática DNSSEC e KSK/ZSK** | `named, named-checkconf, dnssec-signzone` |
| **02** | [`02-nginx-reverse-proxy-http3-quic/`](./02-nginx-reverse-proxy-http3-quic) | **Proxy Reverso Nginx de Alta Performance com Suporte a HTTP/3 e QUIC** | `nginx, openssl, curl --http3` |
| **03** | [`03-haproxy-tcp-layer4-ddos-protection/`](./03-haproxy-tcp-layer4-ddos-protection) | **Balanceador de Carga HAProxy Camada 4 com Stick Tables e Limitação de Taxa** | `haproxy, socat, awk` |
| **04** | [`04-postgresql-streaming-replication-patroni/`](./04-postgresql-streaming-replication-patroni) | **Cluster de Banco de Dados PostgreSQL com Streaming Replication e Patroni HA** | `patronictl, psql, pg_basebackup` |
| **05** | [`05-chrony-ptp-hardware-time-server/`](./05-chrony-ptp-hardware-time-server) | **Servidor de Tempo Stratum-1 com Chrony e Sincronização PTP por Hardware** | `chronyc, ptp4l, phc2sys` |
| **06** | [`06-postfix-opendkim-dmarc-mail-server/`](./06-postfix-opendkim-dmarc-mail-server) | **Servidor de Envio de E-mails Transacionais com DKIM, SPF e Política DMARC Estrita** | `postfix, opendkim, opendkim-genkey` |
| **07** | [`07-apache-httpd-event-mpm-phpfpm-tuning/`](./07-apache-httpd-event-mpm-phpfpm-tuning) | **Otimização Extrema de Apache HTTPD com Event MPM e Pools Dinâmicos PHP-FPM** | `httpd, apachectl, php-fpm` |
| **08** | [`08-squid-forward-proxy-ssl-bump-audit/`](./08-squid-forward-proxy-ssl-bump-audit) | **Proxy de Saída Squid com SSL Bumping e Filtragem de Domínios para Compliance** | `squid, openssl, certtool` |
| **09** | [`09-redis-sentinel-failover-orchestration/`](./09-redis-sentinel-failover-orchestration) | **Cluster de Cache Redis com Sentinel e Comutação Automática de Mestre/Réplica** | `redis-cli, redis-sentinel` |
| **10** | [`10-vsftpd-tls-virtual-users-mysql/`](./10-vsftpd-tls-virtual-users-mysql) | **Servidor FTP Seguro (FTPS) com Usuários Virtuais Isolados e Autenticação SQL** | `vsftpd, pam_mysql, openssl` |
| **11** | [`11-isc-kea-dhcp-high-availability/`](./11-isc-kea-dhcp-high-availability) | **Servidor DHCP Corporativo de Alta Concorrência com Kea DHCP e Replicação** | `kea-dhcp4, keactl` |
| **12** | [`12-unbound-recursive-dns-caching-dnsdist/`](./12-unbound-recursive-dns-caching-dnsdist) | **Resolver DNS Recursivo de Baixa Latência com Unbound e Balanceador dnsdist** | `unbound, unbound-control, dnsdist` |
| **13** | [`13-rabbitmq-cluster-quorum-queues/`](./13-rabbitmq-cluster-quorum-queues) | **Cluster de Mensageria RabbitMQ com Filas Quorum Baseadas no Algoritmo Raft** | `rabbitmqctl, rabbitmq-diagnostics` |
| **14** | [`14-vault-agent-auto-auth-approle-daemon/`](./14-vault-agent-auto-auth-approle-daemon) | **Daemon Local de Injeção de Segredos com HashiCorp Vault Agent e Auto-Auth** | `vault, vault-agent, systemctl` |
| **15** | [`15-samba-active-directory-domain-controller/`](./15-samba-active-directory-domain-controller) | **Controlador de Domínio Active Directory no Linux com Samba 4 e Kerberos** | `samba-tool, kinit, smbclient` |
| **16** | [`16-wireguard-gateway-multi-client-server/`](./16-wireguard-gateway-multi-client-server) | **Servidor Concentrador de Acesso Remoto Seguro com WireGuard e Gerenciamento de Peers** | `wg, wg-quick, qrencode` |
| **17** | [`17-rsyslog-tls-remote-centralized-logging/`](./17-rsyslog-tls-remote-centralized-logging) | **Servidor Centralizador de Logs com rsyslog sobre TLS com Autenticação Mútua** | `rsyslog, openssl, gnutls` |
| **18** | [`18-mosquitto-mqtt-broker-mTLS-iot/`](./18-mosquitto-mqtt-broker-mTLS-iot) | **Broker de Mensageria IoT Mosquitto com Autenticação mTLS e Controle ACL** | `mosquitto, mosquitto_pub, mosquitto_sub` |
| **19** | [`19-mariadb-galera-cluster-multi-master/`](./19-mariadb-galera-cluster-multi-master) | **Cluster de Banco de Dados Multi-Mestre com MariaDB Galera Cluster e SST** | `garbd, mariadb, mysqladmin` |
| **20** | [`20-traefik-edge-router-acme-dashboard/`](./20-traefik-edge-router-acme-dashboard) | **Roteador de Borda Traefik com Descoberta Dinâmica e Certificados Let's Encrypt** | `traefik, curl, jq` |
