#!/usr/bin/env bash
#
# Git AutoSync CLI - Controle do Daemon de Sincronização e Rollback Inteligente
#

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PID_FILE="$SCRIPT_DIR/.autosync.pid"
PAUSE_FILE="$SCRIPT_DIR/.autosync.pause"
LOG_FILE="$SCRIPT_DIR/logs/autosync.log"
PYTHON_SCRIPT="$SCRIPT_DIR/git_autosync.py"
CHECKPOINTS_FILE="$SCRIPT_DIR/.checkpoints.json"

is_running() {
    if [ -f "$PID_FILE" ]; then
        PID=$(cat "$PID_FILE")
        if ps -p "$PID" > /dev/null 2>&1; then
            return 0
        fi
    fi
    return 1
}

start() {
    if is_running; then
        echo "⚠️  Git AutoSync já está rodando (PID: $(cat "$PID_FILE"))."
        exit 0
    fi

    # Garante que pause está desativado ao iniciar
    rm -f "$PAUSE_FILE"
    mkdir -p "$SCRIPT_DIR/logs"

    echo "🚀 Iniciando Git AutoSync em segundo plano..."
    nohup /usr/bin/env python3 "$PYTHON_SCRIPT" >> "$LOG_FILE" 2>&1 &
    sleep 1

    if is_running; then
        echo "✅ Git AutoSync iniciado com sucesso! (PID: $(cat "$PID_FILE"))"
        echo "   Para acompanhar: ./autosync.sh logs"
        echo "   Para verificar status: ./autosync.sh status"
    else
        echo "❌ Falha ao iniciar. Verifique os logs em $LOG_FILE"
    fi
}

stop() {
    if ! is_running; then
        echo "ℹ️  Git AutoSync não está em execução."
        rm -f "$PID_FILE"
        exit 0
    fi

    PID=$(cat "$PID_FILE")
    echo "🛑 Parando Git AutoSync (PID: $PID)..."
    kill "$PID" 2>/dev/null
    sleep 1
    if is_running; then
        kill -9 "$PID" 2>/dev/null
    fi
    rm -f "$PID_FILE" "$PAUSE_FILE"
    echo "✅ Git AutoSync finalizado."
}

status() {
    echo "========================================"
    echo "       Git AutoSync - Status            "
    echo "========================================"

    if is_running; then
        PID=$(cat "$PID_FILE")
        if [ -f "$PAUSE_FILE" ]; then
            echo "Status: ⏸️  PAUSADO (PID: $PID)"
        else
            echo "Status: 🟢 RODANDO (PID: $PID)"
        fi
    else
        echo "Status: ⚪ PARADO"
    fi

    echo ""
    echo "Últimas 5 linhas de log:"
    if [ -f "$LOG_FILE" ]; then
        tail -n 5 "$LOG_FILE"
    else
        echo "  (Nenhum log encontrado ainda)"
    fi
    echo "========================================"
}

pause() {
    if ! is_running; then
        echo "⚠️  O daemon não está rodando. Inicie com: ./autosync.sh start"
        exit 1
    fi
    touch "$PAUSE_FILE"
    echo "⏸️  Git AutoSync pausado. Nenhuma sincronização ocorrerá até que você rode: ./autosync.sh resume"
}

resume() {
    if [ -f "$PAUSE_FILE" ]; then
        rm -f "$PAUSE_FILE"
        echo "▶️  Git AutoSync retomado com sucesso!"
    else
        echo "ℹ️  Git AutoSync não estava pausado."
    fi
}

logs() {
    if [ ! -f "$LOG_FILE" ]; then
        touch "$LOG_FILE"
    fi
    echo "📋 Exibindo logs em tempo real (Ctrl+C para sair)..."
    tail -f "$LOG_FILE"
}

rollback_list() {
    echo "================================================================================"
    echo "                  🛡️  Git AutoSync - Histórico de Checkpoints                  "
    echo "================================================================================"
    if [ ! -f "$CHECKPOINTS_FILE" ]; then
        echo "ℹ️  Nenhum checkpoint registrado até o momento."
        return 0
    fi

    python3 -c "
import json
try:
    with open('$CHECKPOINTS_FILE') as f:
        data = json.load(f)
        if not data:
            print('Nenhum checkpoint registrado.')
            exit(0)
        print(f'{\"TIMESTAMP\":<20} | {\"SHA\":<9} | {\"SHA ANTES\":<10} | {\"MENSAGEM\"}')
        print('-' * 80)
        for cp in reversed(data[-10:]):
            ts = cp.get('timestamp', '-')
            sha = cp.get('sha', cp.get('sha_full', ''))[:8]
            sha_b = cp.get('sha_before', cp.get('sha_before_full', ''))[:8]
            msg = cp.get('commit_message', '-')
            print(f'{ts:<20} | {sha:<9} | {sha_b:<10} | {msg}')
except Exception as e:
    print(f'Erro ao ler checkpoints: {e}')
"
    echo "================================================================================"
}

rollback_to_target() {
    local target="$1"
    local mode="$2" # --soft ou --hard
    local update_remote="$3" # yes/no/ask

    if [ -z "$mode" ]; then
        mode="--soft"
    fi

    # Validação do target no git
    if ! git rev-parse --verify "$target" >/dev/null 2>&1; then
        echo "❌ Erro: Alvo/SHA inválido: $target"
        return 1
    fi

    local target_commit
    target_commit=$(git log -1 --pretty=format:"%h - %s (%cr)" "$target")
    echo "🎯 Alvo de restauração: $target_commit"

    if [ "$mode" = "--hard" ]; then
        echo "⚠️  ATENÇÃO: Rollback HARD descartará todas as alterações após este ponto!"
        read -p "Digite 'CONFIRMAR' para prosseguir: " confirm
        if [ "$confirm" != "CONFIRMAR" ]; then
            echo "Operação cancelada."
            return 1
        fi
    fi

    local branch
    branch=$(git rev-parse --abbrev-ref HEAD)
    echo "🔄 Executando git reset $mode $target..."
    git reset "$mode" "$target"

    if [ "$mode" = "--soft" ]; then
        echo "✅ Soft rollback concluído! Seus arquivos continuam preservados no disco."
    else
        echo "✅ Hard rollback concluído! Repositório resetado para $target."
    fi

    if [ "$update_remote" = "yes" ]; then
        echo "Sincronizando reversão com o GitHub (--force-with-lease)..."
        git push --force-with-lease origin "$branch"
        echo "✅ GitHub atualizado."
    elif [ "$update_remote" != "no" ]; then
        echo ""
        read -p "Deseja também atualizar o repositório remoto no GitHub para refletir a reversão? (s/N): " remote_ans
        if [[ "$remote_ans" =~ ^[sS]$ ]]; then
            echo "Sincronizando reversão com o GitHub (--force-with-lease)..."
            git push --force-with-lease origin "$branch"
            echo "✅ GitHub atualizado com sucesso!"
        else
            echo "ℹ️  O remoto não foi modificado."
        fi
    fi
}

rollback() {
    local cmd="$1"
    local opt="$2"

    case "$cmd" in
        list)
            rollback_list
            ;;
        --last)
            local mode="--soft"
            if [ "$opt" = "--hard" ]; then
                mode="--hard"
            fi
            echo "🔄 Revertendo o último commit..."
            rollback_to_target "HEAD~1" "$mode"
            ;;
        "")
            # Modo interativo
            echo "========================================"
            echo "       🛡️  Git AutoSync - ROLLBACK      "
            echo "========================================"
            LAST_COMMIT=$(git log -1 --pretty=format:"%h - %s (%cr)")
            echo "Commit atual no topo:"
            echo "  $LAST_COMMIT"
            echo ""
            rollback_list
            echo ""
            echo "Opções de Rollback:"
            echo "  1) Soft Rollback do último commit (Desfaz commit/push, mantém arquivos locais)"
            echo "  2) Hard Rollback do último commit (Descarta alterações permanentemente)"
            echo "  3) Restaurar para um SHA específico da lista"
            echo "  4) Cancelar"
            echo ""
            read -p "Digite a opção desejada [1-4]: " menu_opt

            case "$menu_opt" in
                1)
                    rollback_to_target "HEAD~1" "--soft"
                    ;;
                2)
                    rollback_to_target "HEAD~1" "--hard"
                    ;;
                3)
                    read -p "Digite o SHA para onde deseja restaurar: " custom_sha
                    read -p "Tipo de reset? (1 = Soft [padrão], 2 = Hard): " custom_type
                    local c_mode="--soft"
                    if [ "$custom_type" = "2" ]; then
                        c_mode="--hard"
                    fi
                    rollback_to_target "$custom_sha" "$c_mode"
                    ;;
                *)
                    echo "Operação cancelada."
                    ;;
            esac
            ;;
        *)
            # Argumento é um SHA
            local mode="--soft"
            if [ "$opt" = "--hard" ]; then
                mode="--hard"
            fi
            rollback_to_target "$cmd" "$mode"
            ;;
    esac
}

case "$1" in
    start)
        start
        ;;
    stop)
        stop
        ;;
    restart)
        stop
        sleep 1
        start
        ;;
    status)
        status
        ;;
    pause)
        pause
        ;;
    resume)
        resume
        ;;
    logs)
        logs
        ;;
    rollback)
        shift
        rollback "$@"
        ;;
    *)
        echo "Uso: $0 {start|stop|restart|status|pause|resume|logs|rollback [list|--last|<sha>] [--soft|--hard]}"
        echo ""
        echo "Exemplos de Rollback:"
        echo "  $0 rollback list                # Exibe histórico de checkpoints"
        echo "  $0 rollback --last              # Desfaz o último commit (soft)"
        echo "  $0 rollback --last --hard       # Desfaz o último commit (hard)"
        echo "  $0 rollback <SHA>               # Restaura para o SHA especificado (soft)"
        echo "  $0 rollback <SHA> --hard        # Restaura para o SHA especificado (hard)"
        exit 1
        ;;
esac
