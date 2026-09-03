#!/usr/bin/env python3
"""fix-dept-phase-paths.py — 修复 1.0/.../<dept>/产出物清单.md 中 ../流程/... 错误路径
   应指向 ../../2.0-用例/开发流程样例/01-瀑布开发流程/<stage>/产出物清单.md"""

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DEPT_BASE = ROOT / "1.0-软件开发流程角色agent模型"

STAGE_MAP = {
    "需求阶段": "01-需求阶段",
    "设计阶段": "02-设计阶段",
    "开发阶段": "03-开发阶段",
    "测试阶段": "04-测试阶段",
    "部署阶段": "05-部署阶段",
    "运维阶段": "06-运维阶段",
    "安全阶段": "08-安全阶段",
    "数据阶段": "09-数据阶段",
}

total = 0
for p in sorted(DEPT_BASE.glob("*/产出物清单.md")):
    text = p.read_text(encoding="utf-8")
    new_text = text
    n = 0
    for stage_zh, stage_dir in STAGE_MAP.items():
        bad = f"../流程/阶段产出物清单-{stage_zh}.md"
        good = f"../../2.0-用例/开发流程样例/01-瀑布开发流程/{stage_dir}/产出物清单.md"
        if bad in new_text:
            new_text = new_text.replace(bad, good)
            n += 1
    if n:
        p.write_text(new_text, encoding="utf-8")
        print(f"  {p.parent.name}: +{n}")
        total += n
print(f"Total: {total}")