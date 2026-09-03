#!/usr/bin/env python3
"""
patch-stage-downstream.py — 给 .claude/skills/stage-*.skill.md 添加 downstream 字段

解析每个 stage 文件:
- 提取 ## 核心技能 / ## 相关技能 段下的所有 `[name](../1.0-.../.../name.skill.md)` 链接
- 解析出 (role_skill_name, dept, path)
- 插入到 frontmatter 的 downstream: 字段下（YAML 列表）

idempotent: 已存在 downstream 字段则跳过
"""

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
STAGE_DIR = ROOT / ".claude" / "skills"

DEPT_KEYS = ["产品", "研发", "测试", "运维", "安全", "数据", "设计", "项目管理"]


def extract_downstream(text: str) -> list[dict]:
    """在 markdown body 中找指向 1.0-.../skill/ 的链接"""
    results: list[dict] = []
    seen: set[str] = set()
    # 匹配 [name](../1.0-软件开发流程角色agent模型/<部门>/skill/<path>.skill.md)
    pattern = re.compile(
        r"\[([^\]]+)\]\(\.\./1\.0-软件开发流程角色agent模型/([^/]+)/skill/([^)]+\.skill\.md)\)"
    )
    for m in pattern.finditer(text):
        name, dept, path = m.group(1), m.group(2), m.group(3)
        full = f"{dept}/skill/{path}"
        if full in seen:
            continue
        seen.add(full)
        results.append({"name": name, "department": dept, "path": full})
    return results


def patch_file(path: Path) -> int:
    text = path.read_text(encoding="utf-8")
    if re.search(r"^downstream:\s*$", text, re.MULTILINE):
        return 0  # already patched

    items = extract_downstream(text)
    if not items:
        return 0

    # 找到 frontmatter 结束行 "---"
    fm_match = re.match(r"^---\n(.+?)\n---\n", text, re.DOTALL)
    if not fm_match:
        return 0
    fm_body = fm_match.group(1)
    rest = text[fm_match.end():]

    # 追加 downstream 字段
    lines = ["downstream:"]
    for it in items:
        lines.append(f'  - name: "{it["name"]}"')
        lines.append(f'    department: "{it["department"]}"')
        lines.append(f'    path: "{it["path"]}"')

    new_fm = fm_body + "\n" + "\n".join(lines)
    new_text = f"---\n{new_fm}\n---\n{rest}"
    path.write_text(new_text, encoding="utf-8")
    return len(items)


def main():
    total = 0
    for p in sorted(STAGE_DIR.glob("stage-*.skill.md")):
        n = patch_file(p)
        if n:
            print(f"  {p.name}: +{n} downstream links")
            total += n
    print(f"Total: {total} downstream links added")


if __name__ == "__main__":
    main()
