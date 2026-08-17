#!/usr/bin/env python3
from pathlib import Path
import argparse, hashlib, json, re, zipfile

ROOT=Path(__file__).resolve().parents[1]
DIST=ROOT/"dist"

def sha_bytes(b): return hashlib.sha256(b).hexdigest()

def knowledge_files():
    text=(ROOT/"knowledge/knowledge-manifest.yaml").read_text(encoding="utf-8")
    fs=re.findall(r"^\s*file:\s*(.+?)\s*$",text,flags=re.M)
    if len(fs)!=20: raise SystemExit(f"Väntat 20 Knowledge-filer, fick {len(fs)}")
    return fs

def read(z,n):
    try:return z.read(n)
    except KeyError: raise SystemExit(f"Saknad fil i zip: {n}")

def main(version):
    custom=DIST/f"visual-concept-designer-custom-gpt-v{version}.zip"
    chat=DIST/f"visual-concept-designer-chat-v{version}.zip"
    for p in [custom,chat]:
        if not p.is_file(): raise SystemExit(f"Saknad distribution: {p.name}")
        with zipfile.ZipFile(p) as z:
            bad=z.testzip()
            if bad: raise SystemExit(f"Korrupt zip {p.name}: {bad}")

    kfs=knowledge_files()
    with zipfile.ZipFile(custom) as z:
        if read(z,"gpt/gpt-instructions.md") != (ROOT/"gpt/gpt-instructions.md").read_bytes():
            raise SystemExit("Custom GPT-instruktionen avviker från källan")
        if read(z,"gpt/conversation-starters.md") != (ROOT/"gpt/conversation-starters.md").read_bytes():
            raise SystemExit("Custom GPT starters avviker")
        for f in kfs:
            if read(z,f"knowledge/{f}") != (ROOT/"knowledge"/f).read_bytes():
                raise SystemExit(f"Custom Knowledge avviker: {f}")
        if read(z,"VERSION").decode().strip()!=version:
            raise SystemExit("Fel VERSION i custom-paket")

    with zipfile.ZipFile(chat) as z:
        if read(z,"assistant/instructions.md") != (ROOT/"gpt/gpt-instructions.md").read_bytes():
            raise SystemExit("Portable instruktion avviker")
        if read(z,"assistant/conversation-starters.md") != (ROOT/"gpt/conversation-starters.md").read_bytes():
            raise SystemExit("Portable starters avviker")
        for f in kfs:
            if read(z,f"knowledge/{f}") != (ROOT/"knowledge"/f).read_bytes():
                raise SystemExit(f"Portable Knowledge avviker: {f}")
        if read(z,"VERSION").decode().strip()!=version:
            raise SystemExit("Fel VERSION i portable-paket")
        m=json.loads(read(z,"MANIFEST.json"))
        if m["version"]!=version or m["knowledge_count"]!=20:
            raise SystemExit("Fel portable manifestversion/knowledge_count")
        for name, expected in m["files"].items():
            if sha_bytes(read(z,name))!=expected:
                raise SystemExit(f"Hashfel i portable manifest: {name}")
    print(f"OK: båda distributionerna för v{version} är validerade.")

if __name__=="__main__":
    ap=argparse.ArgumentParser()
    ap.add_argument("--version")
    a=ap.parse_args()
    v=a.version or (ROOT/"VERSION").read_text().strip()
    main(v)
