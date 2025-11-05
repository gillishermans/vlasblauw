#!/usr/bin/env python3
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PROJECTS = ROOT / "projects"
IMAGE_EXTS = {'.jpg', '.jpeg', '.png', '.webp', '.gif', '.svg'}

out = []
if PROJECTS.exists():
    for sub in sorted([p for p in PROJECTS.iterdir() if p.is_dir()]):
        imgs = [f for f in sorted(sub.iterdir()) if f.suffix.lower() in IMAGE_EXTS]
        if imgs:
            out.append({
                "folder": sub.name,
                "image": f"projects/{sub.name}/{imgs[0].name}",
                "images": [f"projects/{sub.name}/{i.name}" for i in imgs],
                "title": sub.name,
                "href": f"projects/{sub.name}/"
            })

with open(ROOT / "projects.json", "w", encoding="utf8") as fh:
    json.dump(out, fh, ensure_ascii=False, indent=2)

print(f"Written {len(out)} entries to projects.json")