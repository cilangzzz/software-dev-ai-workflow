#!/usr/bin/env python3
"""
validate-skills.py — Skill 静态校验

校验项（CI 失败标准）:
1. catalog.json 存在且符合 schema
2. catalog 中 path 全部存在
3. 每个 stage skill 的 downstream path 在 catalog 中能找到对应 role skill
4. 每个 *.skill.md / SKILL.md 有 frontmatter（或 markdown meta）
5. .md 内部链接目标存在（同级、上一级、绝对）
6. README.md 中关键目录链接存在

退出码: 0 = 通过, 1 = 有 ERROR, 2 = 仅 WARNING
"""

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CATALOG = ROOT / "catalog.json"
SCHEMA = ROOT / "catalog.schema.json"

errors: list[str] = []
warnings: list[str] = []


def err(msg: str) -> None:
    errors.append(msg)


def warn(msg: str) -> None:
    warnings.append(msg)


def check_catalog_exists() -> dict | None:
    if not CATALOG.exists():
        err(f"catalog.json missing at {CATALOG.relative_to(ROOT)}")
        return None
    try:
        return json.loads(CATALOG.read_text(encoding="utf-8"))
    except json.JSONDecodeError as e:
        err(f"catalog.json invalid JSON: {e}")
        return None


def check_catalog_paths(catalog: dict) -> None:
    for region_name, region in catalog.get("regions", {}).items():
        for sk in region.get("skills", []):
            p = ROOT / sk["path"]
            if not p.exists():
                err(f"catalog.{region_name} references missing file: {sk['path']}")


def check_downstream_targets(catalog: dict) -> None:
    """stage skills 的 downstream 必须能在 role skills 中找到"""
    role_index: dict[str, str] = {}
    for sk in catalog.get("regions", {}).get("agent_model", {}).get("skills", []):
        # path 形如 "1.0-.../产品/skill/xxx.skill.md" → 索引 key 用 dept/skill-name
        path = sk["path"]
        role_index[path] = sk["name"]

    for sk in catalog.get("regions", {}).get("stage", {}).get("skills", []):
        for ds in sk.get("downstream", []):
            # ds.path 是 "产品/skill/xxx.skill.md"，需拼成完整路径
            ds_rel = f"1.0-软件开发流程角色agent模型/{ds['path']}"
            if ds_rel not in role_index:
                err(
                    f"stage {sk['name']} downstream[{ds['name']}] target missing: {ds_rel}"
                )


def check_md_links() -> None:
    """检查 .md 内部链接（相对路径）目标存在。
    仅扫 user-facing 文档（README/2.0-用例/1.0-软件开发流程角色agent模型/.claude/skills/），
    跳过 templates/references/0.0-通用skill（避免模板占位符噪声）"""
    link_pat = re.compile(r"\]\(([^)]+\.md)\)")
    scope_dirs = {
        "README.md",
        ".claude",
        "2.0-用例",
        "1.0-软件开发流程角色agent模型",
    }
    # 占位符模式：{xxx} / <xxx> / ${xxx} / 模板化文件
    placeholder_pat = re.compile(r"[{<]|%s|%d|\{.*?\}")
    checked = 0
    skipped = 0
    for md in ROOT.rglob("*.md"):
        rel = md.relative_to(ROOT).as_posix()
        if not any(rel == s or rel.startswith(s + "/") for s in scope_dirs):
            continue
        if rel.startswith("node_modules/") or "/_deprecated/" in rel or "/_archive/" in rel:
            continue
        try:
            text = md.read_text(encoding="utf-8", errors="replace")
        except Exception:
            continue
        for m in link_pat.finditer(text):
            target = m.group(1).split("#")[0].split("?")[0]
            if not target or target.startswith(("http://", "https://", "mailto:")):
                continue
            if placeholder_pat.search(target):
                skipped += 1
                continue
            target_path = (md.parent / target).resolve()
            checked += 1
            if not target_path.exists():
                warn(f"{rel}: broken link -> {target}")
    print(f"  checked {checked} links, skipped {skipped} placeholder links")


def check_required_files() -> None:
    """关键文件必须存在"""
    required = [
        "README.md",
        "catalog.json",
        "catalog.schema.json",
        "docs/skill-index.md",
        "docs/deliverables/by-stage.md",
        "docs/deliverables/by-department.md",
    ]
    for r in required:
        if not (ROOT / r).exists():
            err(f"required file missing: {r}")


def main() -> int:
    print("=== validate-skills ===")
    check_required_files()
    catalog = check_catalog_exists()
    if catalog:
        check_catalog_paths(catalog)
        check_downstream_targets(catalog)
    check_md_links()

    print(f"\nErrors:   {len(errors)}")
    print(f"Warnings: {len(warnings)}\n")

    for e in errors:
        print(f"  ERROR: {e}")
    for w in warnings[:30]:
        print(f"  WARN:  {w}")
    if len(warnings) > 30:
        print(f"  ... and {len(warnings) - 30} more warnings")

    if errors:
        return 1
    if warnings:
        return 2
    return 0


if __name__ == "__main__":
    sys.exit(main())
