#!/usr/bin/env python3
"""
catalog-generator.py — 生成仓库级 Skill catalog.json

扫描所有 .skill.md / SKILL.md，输出结构化 catalog：
- .claude/skills/          → stage skills (YAML frontmatter)
- 1.0-.../agent模型/{部门}/skill/  → role skills (markdown meta)
- 0.0-通用skill/           → general skills (YAML frontmatter)

输出: catalog.json (UTF-8, indent=2)
"""

import json
import os
import re
import sys
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parent.parent
CATALOG = ROOT / "catalog.json"


def clean_name(path: Path) -> str:
    """去后缀: xx.skill.md → xx; SKILL.md → parent dir name"""
    n = path.name
    if n == "SKILL.md":
        return path.parent.name
    if n.endswith(".skill.md"):
        return n[: -len(".skill.md")]
    return path.stem

# Regions: (name, base_dir, file_pattern, kind)
REGIONS = [
    ("stage", ROOT / ".claude" / "skills", "stage-*.skill.md", "stage"),
    ("agent_model", ROOT / "1.0-软件开发流程角色agent模型", "*.skill.md", "role_skill"),
    ("general", ROOT / "0.0-通用skill", "SKILL.md", "general"),
]

DEPT_MAP = {
    "产品": "product",
    "研发": "development",
    "测试": "testing",
    "运维": "operations",
    "安全": "security",
    "数据": "data",
    "设计": "design",
    "项目管理": "project_management",
}


def parse_frontmatter(text: str) -> dict[str, Any]:
    """解析 YAML frontmatter（--- 包围）"""
    m = re.match(r"^---\n(.+?)\n---", text, re.DOTALL)
    if not m:
        return {}
    fm: dict[str, Any] = {}
    cur_key = None
    for line in m.group(1).splitlines():
        if not line.strip():
            continue
        if line.startswith("  ") and cur_key:
            # 子项，跳过复杂解析
            continue
        if ":" in line and not line.startswith(" "):
            k, v = line.split(":", 1)
            fm[k.strip()] = v.strip().strip('"').strip("'")
            cur_key = k.strip()
    return fm


def parse_markdown_meta(text: str) -> dict[str, Any]:
    """解析 1.0 Skill 的 meta 格式 (# Skill: X / - **字段**: 值)"""
    meta: dict[str, Any] = {}
    # # Skill: name
    m = re.search(r"^#\s*Skill:\s*(\S+)", text, re.MULTILINE)
    if m:
        meta["name"] = m.group(1)
    # **字段**: 值
    for k in ("名称", "版本", "部门", "分类", "描述", "ID"):
        pattern = r"\*\*\s*" + k + r"\s*\*\*:\s*(.+)"
        m2 = re.search(pattern, text)
        if m2:
            meta[k] = m2.group(1).strip()
    # 触发条件: 命令
    cm = re.search(r"\*\*/?(\w[\w-]*)\*\*", text)
    if cm and "command" not in meta:
        meta["command"] = "/" + cm.group(1)
    return meta


def collect() -> dict[str, Any]:
    catalog: dict[str, Any] = {
        "$schema": "./catalog.schema.json",
        "version": "1.0.0",
        "generated_by": "scripts/catalog-generator.py",
        "regions": {},
    }

    for region_name, base, pattern, kind in REGIONS:
        region_entry: dict[str, Any] = {"kind": kind, "skills": []}

        if not base.exists():
            catalog["regions"][region_name] = region_entry
            continue

        for path in sorted(base.rglob(pattern)):
            rel = path.relative_to(ROOT).as_posix()
            try:
                text = path.read_text(encoding="utf-8", errors="replace")
            except Exception as e:
                continue
            entry: dict[str, Any] = {"path": rel, "name": clean_name(path)}

            if path.name.endswith(".skill.md"):
                fm = parse_frontmatter(text)
                entry.update(
                    {
                        "name": fm.get("name", clean_name(path)),
                        "description": fm.get("description", ""),
                        "version": fm.get("version", ""),
                    }
                )
                # trigger.commands
                tm = re.search(r"commands:\s*\n((?:\s+-\s+.+\n)+)", text)
                if tm:
                    cmds = re.findall(r"-\s+(.+)", tm.group(1))
                    entry["commands"] = [c.strip() for c in cmds]
                # downstream role skills (新字段)
                ds_block = re.search(r"downstream:\s*\n((?:\s+-\s+.+\n(?:\s+.+\n)*)+)", text)
                if ds_block:
                    ds_items: list[dict[str, str]] = []
                    for m in re.finditer(
                        r"-\s+name:\s*\"?([^\"\n]+)\"?\s*\n\s+department:\s*\"?([^\"\n]+)\"?\s*\n\s+path:\s*\"?([^\"\n]+)\"?",
                        ds_block.group(1),
                    ):
                        ds_items.append(
                            {"name": m.group(1), "department": m.group(2), "path": m.group(3)}
                        )
                    if ds_items:
                        entry["downstream"] = ds_items
            elif path.name == "SKILL.md":
                # 0.0-通用skill — frontmatter style
                fm = parse_frontmatter(text)
                entry.update(
                    {
                        "name": fm.get("name", path.parent.name),
                        "description": fm.get("description", ""),
                        "version": fm.get("version", ""),
                    }
                )
                # 触发词
                km = re.search(r"keywords:\s*(.+)", text)
                if km:
                    entry["keywords"] = km.group(1).strip()
            else:
                # 1.0/.../*.skill.md (markdown meta style)
                meta = parse_markdown_meta(text)
                entry.update(
                    {
                        "name": meta.get("name", clean_name(path)),
                        "description": meta.get("描述", ""),
                        "version": meta.get("版本", ""),
                        "department": meta.get("部门", ""),
                        "category": meta.get("分类", ""),
                        "skill_id": meta.get("ID", clean_name(path)),
                    }
                )
                if "command" in meta:
                    entry["command"] = meta["command"]

            # derive department from path for role skills
            if kind == "role_skill":
                dept = None
                for d in DEPT_MAP:
                    if f"/{d}/skill/" in rel:
                        dept = d
                        break
                if dept:
                    entry["department_zh"] = dept
                    entry["department_id"] = DEPT_MAP[dept]

            region_entry["skills"].append(entry)

        catalog["regions"][region_name] = region_entry

    # 汇总
    catalog["summary"] = {
        "stage_skills": len(catalog["regions"]["stage"]["skills"]),
        "role_skills": len(catalog["regions"]["agent_model"]["skills"]),
        "general_skills": len(catalog["regions"]["general"]["skills"]),
        "total": sum(
            len(r["skills"]) for r in catalog["regions"].values()
        ),
    }
    return catalog


def main() -> int:
    catalog = collect()
    CATALOG.write_text(
        json.dumps(catalog, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    print(
        f"Generated {CATALOG.relative_to(ROOT)}: "
        f"{catalog['summary']['total']} skills "
        f"(stage={catalog['summary']['stage_skills']}, "
        f"role={catalog['summary']['role_skills']}, "
        f"general={catalog['summary']['general_skills']})"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())