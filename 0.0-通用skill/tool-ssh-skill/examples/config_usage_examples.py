"""
配置加载示例（文档型）

本文件用于给人/AI 提供“正确范式”，避免在不同项目中手写 `ssh/scp`。
更完整的索引请看：README.md
"""


def main() -> None:
    print(
        """
最常见用法（推荐：走 CLI 入口，稳定且不依赖 Python 导入路径）：

  # 单机（密钥认证）
  python ../scripts/ssh_execute.py ./config_single_key.json "whoami && hostname"

  # 单跳板机
  python ../scripts/ssh_execute.py ./config_jump_single_key.json "uptime"

  # 多服务器（选择某个 server）
  python ../scripts/ssh_execute.py ./config_multi_servers.json "hostname" --server dev

配置文件建议字段：
- summary（中文摘要，推荐必填）：一眼看懂用途/环境/责任人
- description（可选）：补充说明
- environment/tags/owner/team（可选）：便于团队协作与筛选
"""
    )


if __name__ == "__main__":
    main()

