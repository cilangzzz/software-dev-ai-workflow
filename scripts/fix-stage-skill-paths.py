#!/usr/bin/env python3
"""fix-stage-skill-paths.py — 修复 .claude/skills/stage-*.skill.md 中 ../1.0-... 路径
   文件实际位于 .claude/skills/ 下两级，正确路径应为 ../../1.0-..."""

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
STAGE_DIR = ROOT / ".claude" / "skills"

total = 0
for p in sorted(STAGE_DIR.glob("stage-*.skill.md")):
    text = p.read_text(encoding="utf-8")
    # 只在 markdown 链接 ([...](...)) 内修
    new_text, n = re.subn(
        r"\]\(\.\./1\.0-软件开发流程角色agent模型/",
        r"](../../1.0-软件开发流程角色agent模型/",
        text,
    )
    if n:
        p.write_text(new_text, encoding="utf-8")
        print(f"  {p.name}: +{n}")
        total += n
print(f"Total: {total}")