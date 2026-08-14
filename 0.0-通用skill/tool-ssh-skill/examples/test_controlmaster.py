"""
ControlMaster 复用性能对比（可选回归）

说明：
- 该脚本用于直观展示“每次新连接” vs “ControlMaster 复用”差异。
- 需要你把 HOST/USER/KEY_FILE 替换成可用目标。
"""

from __future__ import annotations

import os
import subprocess
import time

# 测试配置（请替换）
HOST = "192.0.2.10"
USER = "deploy"
KEY_FILE = "./keys/example_id_ed25519"
ITERATIONS = 10


def _user_known_hosts_file_arg() -> str:
    return "UserKnownHostsFile=NUL" if os.name == "nt" else "UserKnownHostsFile=/dev/null"


def test_without_controlmaster() -> float:
    print("\n" + "=" * 60)
    print("测试1: 传统方式（每次建立新连接）")
    print("=" * 60)

    times_ms = []
    for i in range(ITERATIONS):
        cmd = [
            "ssh",
            "-i",
            KEY_FILE,
            "-o",
            "StrictHostKeyChecking=no",
            "-o",
            _user_known_hosts_file_arg(),
            f"{USER}@{HOST}",
            "echo test",
        ]

        start = time.time()
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=10)
        elapsed = (time.time() - start) * 1000
        times_ms.append(elapsed)
        print(f"  第{i + 1:2d}次: {elapsed:6.1f}ms - {result.stdout.strip()}")

    avg = sum(times_ms) / len(times_ms)
    print(f"\n  平均耗时: {avg:.1f}ms")
    return avg


def test_with_controlmaster() -> float:
    print("\n" + "=" * 60)
    print("测试2: ControlMaster方式（连接复用）")
    print("=" * 60)

    control_path = os.path.join(os.environ.get("TEMP", "/tmp"), f"ssh-test-{USER}@{HOST}")
    if os.path.exists(control_path):
        try:
            os.remove(control_path)
        except OSError:
            pass

    times_ms = []
    for i in range(ITERATIONS):
        cmd = [
            "ssh",
            "-i",
            KEY_FILE,
            "-o",
            "StrictHostKeyChecking=no",
            "-o",
            _user_known_hosts_file_arg(),
            "-o",
            "ControlMaster=auto",
            "-o",
            f"ControlPath={control_path}",
            "-o",
            "ControlPersist=10s",
            f"{USER}@{HOST}",
            "echo test",
        ]

        start = time.time()
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=10)
        elapsed = (time.time() - start) * 1000
        times_ms.append(elapsed)
        print(f"  第{i + 1:2d}次: {elapsed:6.1f}ms - {result.stdout.strip()}")

    avg = sum(times_ms) / len(times_ms)
    print(f"\n  平均耗时: {avg:.1f}ms")
    return avg


def main() -> None:
    avg1 = test_without_controlmaster()
    avg2 = test_with_controlmaster()
    if avg2 > 0:
        print(f"\n加速比（大致）：{avg1 / avg2:.1f}x")


if __name__ == "__main__":
    main()

