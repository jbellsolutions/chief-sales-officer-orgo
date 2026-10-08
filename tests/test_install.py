import importlib.util,json,tempfile,unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
spec=importlib.util.spec_from_file_location('install',ROOT/'orgo/install.py');m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
class Tests(unittest.TestCase):
 def test_backup_idempotence_and_owner_edits(self):
  with tempfile.TemporaryDirectory() as d:
   h=Path(d);(h/'SOUL.md').write_text('old content identity');(h/'.env').write_text('PRIVATE=preserve')
   m.install(ROOT,h);self.assertEqual(next((h/'cso/backups').glob('*/SOUL.md')).read_text(),'old content identity')
   m.install(ROOT,h);self.assertEqual((h/'.env').read_text(),'PRIVATE=preserve')
   (h/'SOUL.md').write_text('owner edit')
   with self.assertRaises(ValueError):m.install(ROOT,h)
 def test_disabled_contract_and_target(self):
  self.assertFalse(json.loads((ROOT/'integration.example.json').read_text())['enabled'])
  self.assertEqual(json.loads((ROOT/'orgo/deployment.json').read_text())['computer_id'],'afdb8c8d-345a-4d52-ad45-e0f60e7ca9ea')
