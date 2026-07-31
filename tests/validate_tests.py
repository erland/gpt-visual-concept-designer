from pathlib import Path
import sys
import yaml
root=Path(__file__).resolve().parents[1]
manifest=yaml.safe_load((root/'tests/test-manifest.yaml').read_text(encoding='utf-8'))
tests=manifest.get('tests', [])
ids=[t.get('id') for t in tests]
files=[t.get('file') for t in tests]
errors=[]
if len(ids)!=27: errors.append(f'Expected 27 test IDs, got {len(ids)}')
if len(set(ids))!=len(ids): errors.append('Duplicate test IDs')
for rel in files:
    if not rel or not (root/'tests'/rel).exists(): errors.append(f'Missing {rel}')
for required in ['assessment-rubric.md','pass-fail-criteria.md','test-run-template.md','README.md']:
    if not (root/'tests'/required).exists(): errors.append(f'Missing tests/{required}')
if errors:
    print('\n'.join(errors)); sys.exit(1)
print(f'OK: {len(ids)} tests, {len(files)} case files, required support files present.')
