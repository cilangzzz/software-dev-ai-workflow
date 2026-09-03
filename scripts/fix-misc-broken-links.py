#!/usr/bin/env python3
"""fix-misc-broken-links.py — 综合性修复 misc 类失效链接
策略:
1. ./XX-XXX.md in ERP/MES/VCP 01-需求分析 → ../02-模块设计/XX-XXX.md
2. ../1.0-... in 2.0-用例/项目管理样例/02-开发库 → ../../1.0-...
3. ../accessibility/SKILL.md 等 in 测试/skill/ → TODO
4. skill/process/X.skill.md in 1.0/研发/agent/ → TODO
5. 产出物映射表.md 等 with wrong relative depth → TODO
6. ../01-项目启动阶段/... in 2.0/开发流程样例/记录/ → TODO
7. 其余 misc → TODO
"""

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

# Pattern catalogue: (file_path_substring, regex, replacement_or_callable)
RULES = [
    # 1. ERP/MES/VCP 01-需求分析 → 02-模块设计 sibling
    {
        "name": "system-model-modules",
        "match_files": lambda p: "/系统模型样例/" in str(p) and "/01-需求分析/" in str(p),
        "regex": r"\[([^\]]+)\]\((\./[0-9]+-[^/)]+\.md)\)",
        "repl": lambda m, f: f"[{m.group(1)}](../02-模块设计/{m.group(2).split('/')[-1]})",
    },
    # 2. 项目管理样例/02-开发库 → ../../1.0-...
    {
        "name": "pm-2xx-relpath",
        "match_files": lambda p: "/项目管理样例/" in str(p) and "/02-开发库/" in str(p),
        "regex": r"\]\(\.\./1\.0-软件开发流程角色agent模型/",
        "repl_str": "](../../1.0-软件开发流程角色agent模型/",
    },
    # 3. 跨阶段流程文档 → ../01-XX → TODO
    {
        "name": "cross-stage-flow",
        "match_files": lambda p: "/开发流程样例/记录/" in str(p) and "跨阶段" in p.name,
        "regex": r"\[([^\]]+)\]\((\.\./[0-9]+-[^)]+\.md)\)",
        "repl": lambda m, f: f"{m.group(1)} <!-- TODO: {m.group(2)} 路径待修复 -->",
    },
    # 4. ERP 系统整体架构设计 (deeper path)
    {
        "name": "erp-arch",
        "match_files": lambda p: "/系统模型样例/" in str(p) and "ERP" in p.name,
        "regex": r"\[([^\]]+)\]\((\./[^\)]+?\.md)\)",
        "repl": lambda m, f: (
            f"[{m.group(1)}](../02-模块设计/{m.group(2).split('/')[-1]})"
            if (f.parent / "../02-模块设计" / m.group(2).split("/")[-1]).resolve().exists()
            else f"{m.group(1)} <!-- TODO: {m.group(2)} 待补 -->"
        ),
    },
]

# Generic TODO-convert for unrecognized
GENERIC_TODO = lambda m: f"{m.group(1)} <!-- TODO: {m.group(2)} 链接待修复 -->"

scope_dirs = {".claude", "2.0-用例", "1.0-软件开发流程角色agent模型"}

total_rules = 0
total_todo = 0
files_changed = 0

for md in ROOT.rglob("*.md"):
    rel = md.relative_to(ROOT).as_posix()
    if not any(rel == s or rel.startswith(s + "/") for s in scope_dirs):
        continue
    if "/_deprecated/" in rel or "/_archive/" in rel:
        continue
    try:
        text = md.read_text(encoding="utf-8", errors="replace")
    except Exception:
        continue

    new_text = text
    file_changes = 0

    # Apply specific rules first
    for rule in RULES:
        if not rule["match_files"](md):
            continue
        if "repl" in rule:
            def make_repl(repl_fn, ref_text):
                def r(m):
                    return repl_fn(m, ref_text)
                return r
            new_text = re.sub(rule["regex"], make_repl(rule["repl"], md), new_text)
        elif "repl_str" in rule:
            new_text = re.sub(rule["regex"], rule["repl_str"], new_text)

    # Generic TODO conversion for remaining broken links
    def generic_fix(m):
        global total_todo
        link_text = m.group(1)
        target = m.group(2).split("#")[0].split("?")[0]
        if not target or target.startswith(("http://", "https://", "mailto:")):
            return m.group(0)
        if re.search(r"[{<]|%s|%d", target):
            return m.group(0)
        target_path = (md.parent / target).resolve()
        if target_path.exists():
            return m.group(0)
        total_todo += 1
        return f"{link_text} <!-- TODO: {target} 链接待修复 -->"

    new_text = re.sub(r"\[([^\]]+)\]\(([^)]+\.md)\)", generic_fix, new_text)

    if new_text != text:
        md.write_text(new_text, encoding="utf-8")
        files_changed += 1

print(f"Files modified: {files_changed}")
print(f"Generic TODO marks: {total_todo}")