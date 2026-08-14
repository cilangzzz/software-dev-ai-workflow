"""
跳板机场景示例（文档型）

目标：把“直连/单跳/双跳/简化跳板”四类典型拓扑固定成模板，减少跑偏与试错。
"""


def main() -> None:
    print(
        """
单跳板机（推荐：使用 config_jump_single_key.json）：

  python ../scripts/ssh_execute.py ./config_jump_single_key.json "whoami && hostname"

双跳板机（推荐：使用 config_jump_double.json）：

  python ../scripts/ssh_execute.py ./config_jump_double.json "whoami && hostname"

简化写法（jump_hosts 只写字符串主机名）：

  python ../scripts/ssh_execute.py ./config_jump_simple.json "uptime"

注意：
- 示例配置全部是占位符/保留网段 IP，请按你的真实环境替换后使用。
- 遇到需要一次性初始化的步骤（例如写入 authorized_keys）可以临时用系统 ssh，但后续日常操作必须回到本 skill。
"""
    )


if __name__ == "__main__":
    main()

