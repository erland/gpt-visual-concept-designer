#!/usr/bin/env python3
from pathlib import Path
import re
import yaml

ROOT=Path(__file__).resolve().parents[1]

def main() -> int:
    errors=[]
    status=yaml.safe_load((ROOT/"migration-status-1.5.yaml").read_text(encoding="utf-8"))
    project=yaml.safe_load((ROOT/"gpt-project.yaml").read_text(encoding="utf-8"))
    registry=yaml.safe_load((ROOT/"runtime-distribution-registry.yaml").read_text(encoding="utf-8"))
    canonical=(ROOT/project["instructions"]["canonical"]).read_bytes()
    legacy=(ROOT/project["instructions"]["legacy_source"]).read_bytes()
    version=(ROOT/"VERSION").read_text(encoding="utf-8").strip()
    manifest=(ROOT/"knowledge/knowledge-manifest.yaml").read_text(encoding="utf-8")
    knowledge=re.findall(r"^\s*file:\s*(.+?)\s*$",manifest,flags=re.M)
    readme=(ROOT/"README.md").read_text(encoding="utf-8")

    p=status.get("progress",{})
    if p.get("last_completed_step")!=7:
        errors.append("migration last_completed_step must be 7")
    if p.get("completed_steps")!=list(range(1,8)):
        errors.append("migration completed_steps must be exactly 1..7")
    if status.get("final_readiness",{}).get("migration_steps_complete")!=7:
        errors.append("final readiness must declare 7/7")
    if canonical!=legacy:
        errors.append("canonical and legacy instructions diverged")
    if version!="1.0.0":
        errors.append(f"VERSION changed: {version!r}")
    if len(knowledge)!=20:
        errors.append(f"expected 20 Knowledge files, found {len(knowledge)}")
    for name in knowledge:
        if not (ROOT/"knowledge"/name).is_file():
            errors.append(f"missing Knowledge file: {name}")
    if registry.get("active_targets")!=["chat","custom-gpt"]:
        errors.append(f"unexpected active targets: {registry.get('active_targets')}")
    for name in ("claude","opencode","openai_plugin"):
        if name not in registry.get("inactive_targets",{}):
            errors.append(f"missing inactive runtime decision: {name}")
    if "7/7 komplett" not in readme:
        errors.append("README does not state completed GPT Builder 1.5 migration")

    critical=[
        b"Anropa sedan alltid **Image generation**",
        b"Designspecifikationen \xc3\xa4r sanningsk\xc3\xa4llan",
        b"L\xc3\xa5s endast efter anv\xc3\xa4ndarens bekr\xc3\xa4ftelse.",
    ]
    for marker in critical:
        if marker not in canonical:
            errors.append(f"canonical behavior marker missing: {marker!r}")

    if errors:
        print("GPT BUILDER 1.5 MIGRATION: FAIL")
        for e in errors: print("-",e)
        return 1
    print("GPT BUILDER 1.5 MIGRATION: PASS")
    print("7/7 complete; VERSION 1.0.0; 20/20 Knowledge; active runtimes: chat, custom-gpt")
    return 0

if __name__=="__main__":
    raise SystemExit(main())
