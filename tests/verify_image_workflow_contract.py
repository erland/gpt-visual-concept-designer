#!/usr/bin/env python3
"""Static acceptance checks for image workflow; NOT a live model/host E2E test."""
from pathlib import Path
import hashlib, json, sys, zipfile
root=Path(__file__).resolve().parents[1]
core=(root/'canonical/core.md').read_bytes()
skill=(root/'canonical/skills/visual-concept-design/behavior.md').read_bytes()
legacy=(root/'assistant/instructions.md').read_bytes()
checks={
 'source instruction exact parity': core+skill == legacy,
 'image generation invoked explicitly': 'Anropa sedan alltid **Image generation**' in skill.decode(),
 'no synthetic image fallback': 'Skapa ingen SVG-placeholder' in skill.decode(),
 'uploaded sketch preservation': 'Vid uppladdad skiss: analysera och fastställ bevarandeprinciper först.' in skill.decode(),
 'design reference is specification': 'Bildprompten härleds och är aldrig primär källa.' in skill.decode(),
 'locks require user confirmation': 'Lås endast efter användarens bekräftelse.' in skill.decode(),
 'image generation error path': 'försök exakt en gång till' in skill.decode(),
 'handoff limits documented': 'Lova inte färdiga sprites' in skill.decode(),
 'project versioned export': 'Senaste godkända zip är källan.' in skill.decode(),
 'five runtime targets configured': all(x in (root/'gpt-project.yaml').read_text() for x in ['chat_zip:', 'plugin:', 'claude:', 'claude_skills:', 'opencode:']),
}
report={'scope':'static source contract only; no model calls or image generation executed','checks':checks,'passed':sum(checks.values()),'total':len(checks),'source_sha256':hashlib.sha256(legacy).hexdigest()}
print(json.dumps(report,indent=2,ensure_ascii=False))
sys.exit(0 if all(checks.values()) else 1)
