#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
python3 - "$ROOT" "${HERMES_HOME:-$HOME/.hermes}" <<'PY'
import json,sys,pathlib,hashlib
root,home=map(pathlib.Path,sys.argv[1:])
marker=json.loads((home/'cso/overlay.json').read_text())
for target,expected in marker.items():
 assert hashlib.sha256((home/target).read_bytes()).hexdigest()==expected, target+' checksum mismatch'
assert 'Chief Sales Officer' in (home/'SOUL.md').read_text()
json.loads((home/'cso/integration.json').read_text())
json.loads((root/'orgo/deployment.json').read_text())
print('CSO overlay verification passed. External integration status is separate.')
PY
