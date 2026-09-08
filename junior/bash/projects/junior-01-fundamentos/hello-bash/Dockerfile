# =============================================================================
# ARQUIVO: Dockerfile
# PROPÓSITO: Empacotamento da CLI em um container Docker isolado.
# =============================================================================

FROM bash:5.2-alpine

# Instalar dependências básicas
RUN apk add --no-color --no-cache coreutils ncurses

# Definir diretório de trabalho
WORKDIR /app

# Copiar arquivos do projeto
COPY bin/ ./bin/
COPY lib/ ./lib/
COPY config/ ./config/

# Definir permissões de execução
RUN chmod +x ./bin/hello-bash

# Entrypoint padrão
ENTRYPOINT ["./bin/hello-bash"]
CMD []
