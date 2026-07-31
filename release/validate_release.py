from pathlib import Path
import sys, yaml
root = Path(__file__).resolve().parents[1]
errors=[]
version=(root/'VERSION').read_text().strip()
if version!='1.3.0': errors.append(f'Unexpected VERSION: {version}')
instructions=(root/'gpt/gpt-instructions.md').read_text(encoding='utf-8')
if len(instructions)>8000: errors.append(f'Instructions too long: {len(instructions)}')
manifest=yaml.safe_load((root/'knowledge/knowledge-manifest.yaml').read_text(encoding='utf-8'))
if str(manifest.get('library_version'))!='1.3.0': errors.append('Manifest version mismatch')
docs=manifest.get('documents',[])
if len(docs)!=20: errors.append(f'Expected 20 knowledge documents, got {len(docs)}')
for d in docs:
    if d.get('status')!='complete': errors.append(f"Incomplete knowledge: {d.get('file')}")
    if not (root/'knowledge'/d.get('file','')).exists(): errors.append(f"Missing knowledge: {d.get('file')}")
cases=list((root/'tests/cases').glob('T*.md'))
if len(cases)!=25: errors.append(f'Expected 25 test cases, got {len(cases)}')
for ex in ['guided-character','sketch-vehicle','environment-world']:
    if not (root/'examples'/ex/'README.md').exists(): errors.append(f'Missing example {ex}')
for req in ['README.md','INSTALLATION.md','USAGE.md','CHANGELOG.md','RELEASE-NOTES.md','release/PREFLIGHT-REPORT.md','workflow/project-bundle-workflow.md','schemas/project-manifest.schema.yaml','schemas/image-manifest.schema.yaml','workflow/project-manifest-guide.md','workflow/internal-prompt-engine.md','templates/image-generation-brief.yaml']:
    if not (root/req).exists(): errors.append(f'Missing {req}')
if errors:
    print('FAIL')
    for e in errors: print('-',e)
    sys.exit(1)
print(f'OK: version={version}, instructions={len(instructions)} chars, knowledge={len(docs)}, tests={len(cases)}, examples=3')
