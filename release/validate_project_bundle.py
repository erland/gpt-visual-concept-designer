from pathlib import Path
import sys
import yaml
root = Path(sys.argv[1]) if len(sys.argv) > 1 else Path('.')
required = ['README.md', 'project.yaml', 'CHANGELOG.md', 'manifests/concepts.yaml', 'manifests/images.yaml']
errors = [f'missing: {rel}' for rel in required if not (root / rel).exists()]
manifest = root / 'manifests/images.yaml'
if manifest.exists():
    data = yaml.safe_load(manifest.read_text(encoding='utf-8')) or {}
    ids = set()
    for item in data.get('images', []):
        image_id = item.get('id')
        if image_id in ids: errors.append(f'duplicate image id: {image_id}')
        ids.add(image_id)
        file_path = root / item.get('file', '')
        if not file_path.exists() and item.get('status') != 'missing': errors.append(f"missing image file: {item.get('file')}")
        roles = item.get('roles', [])
        if item.get('status') == 'deprecated' and any(str(role).startswith('authoritative_') for role in roles):
            errors.append(f'deprecated authoritative image: {image_id}')
if errors:
    print('\n'.join(errors))
    raise SystemExit(1)
print('Project bundle valid')
