"""Backup and overlay identity only. Preserve runtime, credentials and schedules."""
import argparse
import hashlib
import json
from pathlib import Path
import shutil
import time


def install(root, home):
    root, home = Path(root).resolve(), Path(home).expanduser().resolve()
    home.mkdir(parents=True, exist_ok=True, mode=0o700)
    marker = home / 'cso' / 'overlay.json'
    sources = {'SOUL.md': root / 'profiles/SOUL.md', 'AGENTS.md': root / 'profiles/AGENTS.md', 'skills/chief-sales-officer/SKILL.md': root / 'skills/chief-sales-officer/SKILL.md'}
    prior = json.loads(marker.read_text()) if marker.exists() else {}
    for target, source in sources.items():
        dst = home / target
        if dst.exists() and target in prior and hashlib.sha256(dst.read_bytes()).hexdigest() != prior[target]:
            raise ValueError('Owner-edited CSO file needs review: ' + target)
    backup = home / 'cso' / 'backups' / str(time.time_ns())
    for target, source in sources.items():
        dst = home / target
        if dst.exists() and dst.read_bytes() == source.read_bytes():
            continue
        if dst.exists():
            saved = backup / target
            saved.parent.mkdir(parents=True, exist_ok=True, mode=0o700)
            shutil.copy2(dst, saved)
            saved.chmod(0o600)
        dst.parent.mkdir(parents=True, exist_ok=True, mode=0o700)
        temp = dst.with_name(dst.name + '.cso-new')
        temp.write_bytes(source.read_bytes()); temp.chmod(0o600); temp.replace(dst)
    private = home / 'cso'
    private.mkdir(parents=True, exist_ok=True, mode=0o700)
    contract = private / 'integration.json'
    if not contract.exists():
        shutil.copyfile(root / 'integration.example.json', contract)
        contract.chmod(0o600)
    marker.write_text(json.dumps({k: hashlib.sha256(v.read_bytes()).hexdigest() for k, v in sources.items()}, indent=2))
    marker.chmod(0o600)
    print('CSO identity installed; old identity backed up; runtime and connections preserved.')

if __name__ == '__main__':
    p = argparse.ArgumentParser(); p.add_argument('--root', required=True); p.add_argument('--home', required=True)
    a = p.parse_args(); install(a.root, a.home)
