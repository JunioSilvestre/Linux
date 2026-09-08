#!/usr/bin/env bash
# =============================================================================
# ARQUIVO: scripts/hello-bash.sh
# PROPÓSITO: Wrapper de conveniência para execução direta a partir da pasta scripts/.
#            Delega a execução para o entrypoint principal bin/hello-bash.
# =============================================================================

set -Eeuo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
exec "${SCRIPT_DIR}/bin/hello-bash" "$@"
