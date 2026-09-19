#!/usr/bin/env python3
"""Zabalí každý skill ze složky skills/ do zips/<name>.zip (složka skillu v kořeni zipu).
Spuštění z kořene repozitáře: python scripts/build_zips.py
"""
import zipfile
from pathlib import Path

root = Path(__file__).resolve().parent.parent
skills = root / "skills"
zips = root / "zips"
zips.mkdir(exist_ok=True)
for skill in sorted(p for p in skills.iterdir() if p.is_dir()):
    if not (skill / "SKILL.md").exists():
        continue
    out = zips / f"{skill.name}.zip"
    with zipfile.ZipFile(out, "w", zipfile.ZIP_DEFLATED) as z:
        for f in sorted(skill.rglob("*")):
            if f.is_file() and "__pycache__" not in f.parts:
                z.write(f, f.relative_to(skills).as_posix())
    print(f"{out.name}: {out.stat().st_size // 1024} kB")
