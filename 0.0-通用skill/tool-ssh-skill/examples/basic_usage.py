"""
SSH Skill 基本用法（可运行）

说明：
- 这是一个“回归用例”脚本：用本目录的示例配置调用 ssh-skill 的 CLI 入口。
- 运行前请先把示例配置中的占位符替换为你的真实信息（不要提交到仓库）。

用法：
  python basic_usage.py [config_json] [command]

示例：
  python basic_usage.py ./config_single_key.json "whoami && hostname"
"""

from __future__ import annotations

import os
import subprocess
import sys
from pathlib import Path


def main() -> int:
    examples_dir = Path(__file__).resolve().parent
    skill_root = examples_dir.parent
    script = skill_root / "scripts" / "ssh_execute.py"

    config_path = Path(sys.argv[1]).resolve() if len(sys.argv) >= 2 else (examples_dir / "config_single_key.json")
    command = sys.argv[2] if len(sys.argv) >= 3 else "whoami && hostname"

    if not script.exists():
        raise FileNotFoundError(f"未找到脚本入口：{script}")
    if not config_path.exists():
        raise FileNotFoundError(f"未找到配置文件：{config_path}")

    env = os.environ.copy()
    env.setdefault("MSYS_NO_PATHCONV", "1")

    proc = subprocess.run(
        [sys.executable, str(script), str(config_path), command],
        text=True,
        env=env,
    )
    return proc.returncode


if __name__ == "__main__":
    raise SystemExit(main())

