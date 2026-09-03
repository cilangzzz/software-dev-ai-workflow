#!/usr/bin/env python3
"""
skill-index-generator.py — 从 catalog.json 生成 docs/skill-index.md

输出四象限视图:
1. 按阶段（stage skills）
2. 按部门（role skills）
3. 按通用能力（general skills）
4. 阶段→角色 调用关系图（基于 downstream）
"""

import json
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CATALOG = ROOT / "catalog.json"
OUT = ROOT / "docs" / "skill-index.md"


def gen() -> str:
    c = json.loads(CATALOG.read_text(encoding="utf-8"))
    s = c["summary"]
    md: list[str] = [
        "# Skill 总目录（自动生成）\n",
        f"> 来源: `catalog.json`（{c.get('version', '?')}），生成器: `scripts/catalog-generator.py` + `scripts/skill-index-generator.py`",
        f"> 共 {s['total']} 个 Skill（阶段 {s['stage_skills']} + 角色 {s['role_skills']} + 通用 {s['general_skills']}）\n",
    ]

    md.append("## 1. 按阶段（8 阶段端到端编排）\n")
    md.append("| 阶段 | 命令 | 描述 | 调用角色 |")
    md.append("|------|------|------|----------|")
    for sk in c["regions"]["stage"]["skills"]:
        cmd = (sk.get("commands") or ["-"])[0]
        ds = sk.get("downstream") or []
        ds_disp = ", ".join(f"`{d['name']}` ({d['department']})" for d in ds) or "-"
        md.append(f"| [{sk['name']}]({sk['path']}) | `{cmd}` | {sk.get('description','')} | {ds_disp} |")
    md.append("")

    md.append("## 2. 按部门（角色 Agent 技能）\n")
    by_dept: dict[str, list[dict]] = defaultdict(list)
    for sk in c["regions"]["agent_model"]["skills"]:
        dept = sk.get("department_zh") or sk.get("department", "未分类")
        by_dept[dept].append(sk)
    dept_order = ["产品", "研发", "测试", "运维", "安全", "数据", "设计", "项目管理"]
    for d in dept_order:
        items = by_dept.get(d, [])
        if not items:
            continue
        md.append(f"### {d}（{len(items)} 个 Skill）\n")
        md.append("| Skill | 分类 | 描述 |")
        md.append("|-------|------|------|")
        for sk in sorted(items, key=lambda x: x["name"]):
            cat = sk.get("category", "") or "-"
            md.append(f"| [{sk['name']}]({sk['path']}) | {cat} | {sk.get('description','')[:80]} |")
        md.append("")

    md.append("## 3. 按通用能力（0.0-通用skill）\n")
    md.append("| Skill | 触发词 | 描述 |")
    md.append("|-------|--------|------|")
    for sk in c["regions"]["general"]["skills"]:
        kw = sk.get("keywords", "-")
        md.append(f"| [{sk['name']}]({sk['path']}) | {kw} | {sk.get('description','')[:80]} |")
    md.append("")

    md.append("## 4. 阶段→角色 调用关系\n")
    md.append("```")
    md.append("需求分析(stage-01) ─┬─ 产品/requirement-analyzer")
    md.append("                    ├─ 产品/user-story-generator")
    md.append("                    └─ 产品/acceptance-criteria-writer")
    md.append("...")
    md.append("```\n")
    md.append("完整数据见 [`catalog.json`](../catalog.json) 各 stage skill 的 `downstream` 字段。\n")

    return "\n".join(md)


def main():
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(gen(), encoding="utf-8")
    print("Generated:", OUT.relative_to(ROOT))


if __name__ == "__main__":
    main()
