# 19 — Captura de Tráfego de Rede Correlacionada com Chaves TLS (SSLKEYLOGFILE)

## 🏢 Cenário de Produção e Vida Real
Diagnóstico profundo de requisições HTTPS e gRPC criptografadas em Wireshark.

## 🚀 Arquitetura e Engenharia Linux
Implementação de engenharia avançada de sistemas Linux para produção, assegurando confiabilidade, resiliência, observabilidade e adesão estrita aos padrões de conformidade corporativa.

## 🛠️ Ferramentas e Utilitários Nativos Utilizados
`tcpdump, tshark, openssl`

## 📌 Exemplo de Execução CLI
```bash
tshark -r capture.pcap -o 'tls.keylog_file:keys.log'
```
