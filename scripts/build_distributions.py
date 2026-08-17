#!/usr/bin/env python3
from pathlib import Path
import argparse, hashlib, json, os, re, shutil, zipfile

ROOT = Path(__file__).resolve().parents[1]
DIST = ROOT / "dist"

def semver(v):
    if not re.fullmatch(r"\d+\.\d+\.\d+(?:[+-][0-9A-Za-z.-]+)?", v):
        raise SystemExit(f"Ogiltig version: {v}")
    return v

def manifest_knowledge_files():
    text=(ROOT/"knowledge/knowledge-manifest.yaml").read_text(encoding="utf-8")
    files=re.findall(r"^\s*file:\s*(.+?)\s*$", text, flags=re.M)
    if len(files) != 20:
        raise SystemExit(f"Knowledge-manifestet innehåller {len(files)} filer, väntat 20.")
    for f in files:
        if not (ROOT/"knowledge"/f).is_file():
            raise SystemExit(f"Saknad Knowledge-fil: {f}")
    return files

def sha256(p):
    h=hashlib.sha256()
    with open(p,"rb") as f:
        for b in iter(lambda:f.read(1024*1024), b""):
            h.update(b)
    return h.hexdigest()

def copy_file(src, dst):
    dst.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(src,dst)

def copy_tree(src,dst):
    if not src.exists(): return
    for p in src.rglob("*"):
        if p.is_file():
            copy_file(p, dst/p.relative_to(src))

def zip_dir(src,out):
    out.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(out,"w",zipfile.ZIP_DEFLATED) as z:
        for p in sorted(src.rglob("*")):
            if p.is_file():
                info=zipfile.ZipInfo(str(p.relative_to(src)).replace(os.sep,"/"))
                info.date_time=(2020,1,1,0,0,0)
                info.compress_type=zipfile.ZIP_DEFLATED
                info.external_attr=0o644 << 16
                z.writestr(info,p.read_bytes())

def build(version):
    version=semver(version)
    kfiles=manifest_knowledge_files()
    shutil.rmtree(DIST, ignore_errors=True)
    DIST.mkdir()

    stage=ROOT/".build-distributions"
    shutil.rmtree(stage, ignore_errors=True)
    custom=stage/"custom"
    chat=stage/"chat"
    custom.mkdir(parents=True); chat.mkdir(parents=True)

    # Custom GPT distribution: current install/config + exact knowledge and optional templates.
    for rel in [
        "README.md","INSTALLATION.md","USAGE.md",
        "gpt/gpt-instructions.md","gpt/gpt-name-and-description.md",
        "gpt/welcome-message.md","gpt/capabilities-and-settings.md",
        "gpt/conversation-starters.md","knowledge/knowledge-manifest.yaml",
    ]:
        if (ROOT/rel).exists():
            copy_file(ROOT/rel, custom/rel)
    for f in kfiles:
        copy_file(ROOT/"knowledge"/f, custom/"knowledge"/f)
    copy_tree(ROOT/"templates", custom/"templates")
    (custom/"VERSION").write_text(version+"\n", encoding="utf-8")

    # Portable chat
    copy_file(ROOT/"portable/START-HERE.md", chat/"START-HERE.md")
    copy_file(ROOT/"gpt/gpt-instructions.md", chat/"assistant/instructions.md")
    copy_file(ROOT/"gpt/conversation-starters.md", chat/"assistant/conversation-starters.md")
    copy_file(ROOT/"gpt/gpt-name-and-description.md", chat/"assistant/name-and-description.md")
    copy_file(ROOT/"gpt/capabilities-and-settings.md", chat/"assistant/capabilities-and-settings.md")
    for f in kfiles:
        copy_file(ROOT/"knowledge"/f, chat/"knowledge"/f)
    copy_file(ROOT/"knowledge/knowledge-manifest.yaml", chat/"knowledge/knowledge-manifest.yaml")
    copy_tree(ROOT/"templates", chat/"templates")
    # Non-primary supporting material useful for long projects / QA
    for d in ["schemas","examples","workflow","models"]:
        copy_tree(ROOT/d, chat/"supporting"/d)
    (chat/"VERSION").write_text(version+"\n", encoding="utf-8")

    files={}
    for p in sorted(chat.rglob("*")):
        if p.is_file() and p.name!="MANIFEST.json":
            files[str(p.relative_to(chat)).replace(os.sep,"/")]=sha256(p)
    (chat/"MANIFEST.json").write_text(json.dumps({
        "package":"visual-concept-designer",
        "format":"portable-chat-assistant",
        "version":version,
        "entrypoint":"START-HERE.md",
        "instructions":"assistant/instructions.md",
        "knowledge_count":20,
        "files":files
    },ensure_ascii=False,indent=2)+"\n",encoding="utf-8")

    zip_dir(custom, DIST/f"visual-concept-designer-custom-gpt-v{version}.zip")
    zip_dir(chat, DIST/f"visual-concept-designer-chat-v{version}.zip")
    shutil.rmtree(stage, ignore_errors=True)

if __name__=="__main__":
    ap=argparse.ArgumentParser()
    ap.add_argument("--version")
    args=ap.parse_args()
    version=args.version or (ROOT/"VERSION").read_text().strip()
    build(version)
