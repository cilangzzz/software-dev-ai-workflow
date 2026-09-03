#!/usr/bin/env python3
"""fix-erp-mes-paths.py — 修复 ERP/MES/VCP 需求总览中的 ./产品/PRD/PRD-XX-XXX.md 错误路径
   应指向 ../02-模块设计/NN-XXX.md"""

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

# Files we know are broken: ERP/MES/VCP 00-XXX需求总览
broken_files = []
for p in ROOT.rglob("*.md"):
    s = str(p).replace("\\", "/")
    if "系统模型样例" in s and p.name.startswith("00-") and "需求总览" in p.name:
        broken_files.append(p)

total = 0
files_changed = 0
for p in broken_files:
    text = p.read_text(encoding="utf-8")
    module_dir = p.parent.parent / "02-模块设计"
    if not module_dir.exists():
        continue
    module_files = {f.name: f for f in module_dir.iterdir() if f.suffix == ".md"}

    file_changes = 0

    def repl(m: re.Match) -> str:
        link_text = m.group(1)
        target = m.group(2)
        # ERP: PRD-NN-{module}.md → ../02-模块设计/{NN}-{module}.md
        mm = re.search(r"PRD-(\d+)-(.+)\.md$", target)
        if mm:
            name = mm.group(2)
            candidates = [f for fname, f in module_files.items() if fname.endswith(f"{name}.md")]
            if not candidates:
                return f"{link_text} <!-- TODO: {target} 模块文档待补 -->"
            return f"[{link_text}](../02-模块设计/{candidates[0].name})"
        # MES: PRD-{name}.md (无编号) → 找 02-模块设计/ 下任何含 {name} 的文件
        mm = re.search(r"PRD-(.+)\.md$", target)
        if mm:
            name = mm.group(1)
            candidates = [f for fname, f in module_files.items() if name in fname]
            if not candidates:
                return f"{link_text} <!-- TODO: {target} 模块文档待补 -->"
            return f"[{link_text}](../02-模块设计/{candidates[0].name})"
        # VCP: ./产品/PRD/ (目录)
        if target.endswith("/PRD/") or target.endswith("/PRD"):
            return f"{link_text} <!-- TODO: {target} 目录文档待补 -->"
        return f"{link_text} <!-- TODO: {target} 链接待修复 -->"

    # 匹配所有 ./产品/PRD-*.md 或 ./产品/PRD/* 形式
    new_text = re.sub(
        r"\[([^\]]+)\]\((\./产品/(?:PRD/)?PRD[^)]*(?:\.md|/))\)",
        repl,
        text,
    )
    if new_text != text:
        n = len(re.findall(r"\./产品/PRD/PRD-\d+", text))
        p.write_text(new_text, encoding="utf-8")
        files_changed += 1
        print(f"  {p.relative_to(ROOT)}: {n}")
        total += n
print(f"Total: {total} in {files_changed} files")