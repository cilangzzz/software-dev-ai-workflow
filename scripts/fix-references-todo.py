#!/usr/bin/env python3
"""fix-references-todo.py — 将 role skill 中所有缺失的 references/*.md 链接
   转为纯文本 + TODO 注释，保留语义但不产生 dead link"""

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
scope_dirs = {".claude", "2.0-用例", "1.0-软件开发流程角色agent模型"}

placeholder_pat = re.compile(r"[{<]|%s|%d")
link_pat = re.compile(r"\[([^\]]+)\]\(([^)]+\.md)\)")

# We need to scan every file in scope, find broken refs/{x}.md links, and rewrite
def is_in_scope(rel: str) -> bool:
    if "/_deprecated/" in rel or "/_archive/" in rel:
        return False
    return any(rel == s or rel.startswith(s + "/") for s in scope_dirs)


total_replaced = 0
files_changed = 0
for md in ROOT.rglob("*.md"):
    rel = md.relative_to(ROOT).as_posix()
    if not is_in_scope(rel):
        continue
    try:
        text = md.read_text(encoding="utf-8", errors="replace")
    except Exception:
        continue

    def fix_link(m: re.Match) -> str:
        global total_replaced
        link_text, target = m.group(1), m.group(2).split("#")[0].split("?")[0]
        if not target or target.startswith(("http://", "https://", "mailto:")):
            return m.group(0)
        if placeholder_pat.search(target):
            return m.group(0)
        if "/references/" not in target and "references/" not in target:
            return m.group(0)
        target_path = (md.parent / target).resolve()
        if target_path.exists():
            return m.group(0)
        # Broken: convert to text + TODO comment
        total_replaced += 1
        return f"{link_text} <!-- TODO: {target} 缺失 -->"

    new_text = link_pat.sub(fix_link, text)
    if new_text != text:
        md.write_text(new_text, encoding="utf-8")
        files_changed += 1
        print(f"  {rel}")

print(f"Total: {total_replaced} links in {files_changed} files")