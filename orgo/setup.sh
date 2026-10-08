#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
command -v hermes >/dev/null || { echo 'Install Hermes on the target computer first.' >&2; exit 1; }
python3 "$ROOT/orgo/install.py" --root "$ROOT" --home "${HERMES_HOME:-$HOME/.hermes}"
"$ROOT/orgo/verify.sh"
