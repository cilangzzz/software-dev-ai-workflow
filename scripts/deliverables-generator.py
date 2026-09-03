#!/usr/bin/env python3
"""
deliverables-generator.py — 产出物清单单一事实源生成器

从以下两类来源汇总产出物：
- 2.0-用例/开发流程样例/{01-瀑布,02-敏捷}/<阶段>/产出物清单.md
- 1.0-软件开发流程角色agent模型/<部门>/产出物清单.md

按表头列名识别字段（避免硬编码列序，兼容各表不同 schema）

输出:
  docs/deliverables/by-stage.md       按阶段汇总
  docs/deliverables/by-department.md  按部门汇总
"""

from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT_DIR = ROOT / "docs" / "deliverables"

STAGES_WATERFALL = [
    "01-需求阶段", "02-设计阶段", "03-开发阶段", "04-测试阶段",
    "05-部署阶段", "06-运维阶段", "07-项目收尾阶段", "08-安全阶段",
    "09-数据阶段", "10-项目管理阶段",
]
STAGES_AGILE = [
    "01-项目启动", "02-迭代规划", "03-迭代执行", "04-迭代评审",
    "05-迭代回顾", "06-发布交付", "07-敏捷运维",
]

DEPT_LIST = ["产品", "测试", "运维", "安全", "数据", "设计", "研发", "项目管理"]

PHASE_BASE = ROOT / "2.0-用例" / "开发流程样例"
DEPT_BASE = ROOT / "1.0-软件开发流程角色agent模型"

# 关键列名识别（允许变体）
COL_CN = {"中文名称", "中文名", "产出物", "名称"}
COL_EN = {"英文名称", "英文名", "English Name"}
COL_TYPE = {"类型", "类别"}
COL_PRIO = {"优先级", "优先", "Priority"}
COL_DESC = {"说明", "描述", "质量标准", "简介", "内容", "质量要求"}
COL_SKILL = {"相关Skill", "Skill", "关联Skill"}
COL_FILE = {"文件格式", "文件"}


def is_separator_row(cells: list[str]) -> bool:
    return all(set(c) <= set("-: ") for c in cells)


def extract_section_tables(text: str, header_marker: str) -> list[tuple[list[str], list[list[str]]]]:
    """在指定 ## 段下抽取所有 markdown 表; 返回 [(header, rows), ...]
    离开段边界(下一个 ## )停止。rows 不含 header 和分隔行。"""
    lines = text.splitlines()
    in_section = False
    cur_header: list[str] = []
    cur_rows: list[list[str]] = []
    out: list[tuple[list[str], list[list[str]]]] = []

    def flush():
        nonlocal cur_header, cur_rows
        if cur_header and cur_rows:
            out.append((cur_header, cur_rows))
        cur_header = []
        cur_rows = []

    for line in lines:
        s = line.strip()
        if not in_section:
            if s.startswith("## ") and header_marker in s:
                in_section = True
            continue
        if s.startswith("## "):
            break
        if not s.startswith("|"):
            continue
        cells = [c.strip() for c in s.strip("|").split("|")]
        if is_separator_row(cells):
            continue
        # 判断是否是新表头: 第一个 cell 含"序号"或"中文"
        is_header_like = any(k in cells[0] for k in ("序号", "中文", "产出物")) and len(cells) >= 4
        if is_header_like and cur_header:
            flush()
        if is_header_like and not cur_header:
            cur_header = cells
        else:
            if cur_header:
                cur_rows.append(cells)
    flush()
    return out


def load_phase(mode: str, phase: str) -> list[tuple[str, dict]]:
    p = PHASE_BASE / mode / phase / "产出物清单.md"
    if not p.exists():
        return []
    tables = extract_section_tables(p.read_text(encoding="utf-8"), "产出物列表")
    out: list[tuple[str, dict]] = []
    for header, rows in tables:
        for r in rows:
            entry = map_row(header, r)
            if entry:
                out.append((phase, entry))
    return out


def load_dept(d: str) -> list[tuple[str, str, dict]]:
    p = DEPT_BASE / d / "产出物清单.md"
    if not p.exists():
        return []
    text = p.read_text(encoding="utf-8")
    tables = extract_section_tables(text, "产出物列表")
    # 提取最近 ### 标题作为 sub_section 名
    # 简单做法: 用 phase 段中的"阶段名"近似
    out: list[tuple[str, str, dict]] = []
    cur_sub = ""
    for line in text.splitlines():
        s = line.strip()
        if s.startswith("### "):
            cur_sub = s[4:].strip()
    for header, rows in tables:
        for r in rows:
            entry = map_row(header, r)
            if entry:
                out.append((d, cur_sub, entry))
    return out


def map_row(header: list[str], row: list[str]) -> dict | None:
    """按 header 列名映射字段。精确优先，子串回退用 startswith/endswith 防误匹。"""
    n = min(len(header), len(row))
    entry: dict[str, str] = {}

    def match_exact(h: str, exact: set[str]) -> bool:
        return h in exact

    def match_prefix(h: str, prefix_set: set[str]) -> bool:
        for p in prefix_set:
            if h.startswith(p):
                return True
        return False

    def match_suffix(h: str, suffix_set: set[str]) -> bool:
        for s in suffix_set:
            if h.endswith(s):
                return True
        return False

    for i in range(n):
        h = header[i]
        v = row[i]
        # 中文名称 / 英文名称 都含 "名称"，必须先用 startswith 区分
        if match_prefix(h, {"中文"}):
            entry["cn"] = v
        elif match_prefix(h, {"英文", "English"}):
            entry["en"] = v
        elif match_exact(h, COL_TYPE) or match_suffix(h, {"类型", "类别"}):
            entry["type"] = v
        elif match_exact(h, COL_PRIO) or match_suffix(h, {"优先级", "优先"}):
            entry["prio"] = v
        elif match_exact(h, COL_SKILL) or match_suffix(h, {"Skill"}):
            entry["skill"] = v
        elif match_exact(h, COL_FILE) or match_suffix(h, {"文件格式", "文件"}):
            entry["file"] = v
        elif match_exact(h, COL_DESC) or match_suffix(h, {"说明", "描述", "标准", "简介", "内容"}):
            entry["desc"] = v
    if not entry.get("cn"):
        return None
    return entry


def gen_by_stage() -> str:
    md: list[str] = [
        "# 按阶段产出物清单（汇总）\n",
        "> 自动生成自 `2.0-用例/开发流程样例/*/产出物清单.md`。",
        "> 修改源文件后运行 `python scripts/deliverables-generator.py` 重新生成。\n",
    ]

    md.append("## 瀑布流程\n")
    md.append("| 阶段 | 中文名称 | 英文名称 | 类型 | 优先级 | 说明 |")
    md.append("|------|---------|---------|------|--------|------|")
    waterfall_count = 0
    for stage in STAGES_WATERFALL:
        items = load_phase("01-瀑布开发流程", stage)
        if not items:
            continue
        for _, e in items:
            md.append(
                f"| {stage} | {e.get('cn','')} | {e.get('en','')} | "
                f"{e.get('type','')} | {e.get('prio','')} | {e.get('desc','')} |"
            )
            waterfall_count += 1
    md.append("")
    md.append(f"_瀑布流程共计 {waterfall_count} 项产出物_\n")

    md.append("## 敏捷流程\n")
    md.append("| 阶段 | 中文名称 | 英文名称 | 类型 | 优先级 | 说明 |")
    md.append("|------|---------|---------|------|--------|------|")
    agile_count = 0
    for stage in STAGES_AGILE:
        items = load_phase("02-敏捷开发流程", stage)
        if not items:
            continue
        for _, e in items:
            md.append(
                f"| {stage} | {e.get('cn','')} | {e.get('en','')} | "
                f"{e.get('type','')} | {e.get('prio','')} | {e.get('desc','')} |"
            )
            agile_count += 1
    md.append("")
    md.append(f"_敏捷流程共计 {agile_count} 项产出物_\n")

    return "\n".join(md)


def gen_by_department() -> str:
    md: list[str] = [
        "# 按部门产出物清单（汇总）\n",
        "> 自动生成自 `1.0-软件开发流程角色agent模型/*/产出物清单.md`。",
        "> 修改源文件后运行 `python scripts/deliverables-generator.py` 重新生成。\n",
    ]

    md.append("| 部门 | 子段 | 中文名称 | 英文名称 | 类型 | 优先级 | 相关Skill | 说明 |")
    md.append("|------|------|---------|---------|------|--------|----------|------|")
    dept_count = 0
    for d in DEPT_LIST:
        items = load_dept(d)
        if not items:
            continue
        for _, sub, e in items:
            md.append(
                f"| {d} | {sub} | {e.get('cn','')} | {e.get('en','')} | "
                f"{e.get('type','')} | {e.get('prio','')} | {e.get('skill','')} | "
                f"{e.get('desc','')} |"
            )
            dept_count += 1
    md.append("")
    md.append(f"_各部门共计 {dept_count} 项产出物_\n")

    return "\n".join(md)


def main():
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    (OUT_DIR / "by-stage.md").write_text(gen_by_stage(), encoding="utf-8")
    (OUT_DIR / "by-department.md").write_text(gen_by_department(), encoding="utf-8")
    print("Generated:")
    print(" -", (OUT_DIR / "by-stage.md").relative_to(ROOT))
    print(" -", (OUT_DIR / "by-department.md").relative_to(ROOT))


if __name__ == "__main__":
    main()
