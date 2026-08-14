"""
交互式会话提示（文档型）

运维中常见的交互问题：
- `sudo` 需要输入密码
- `apt/yum` 需要确认
- 远端脚本提示 `Enter password:` / `Press any key`

建议：
- 优先把命令改成“非交互式”（例如 `DEBIAN_FRONTEND=noninteractive`、`-y`、`sudo -n` 等）
- 若必须交互，建议把交互步骤拆成“明确的多步命令”并逐步验证输出

本 skill 的核心目标是：把连接与复用封装起来，避免回退到手写 `ssh`。
"""


def main() -> None:
    print(
        """
示例：把 apt 安装变为非交互式（需要你按真实系统调整）：

  python ../scripts/ssh_execute.py ./config_single_key.json "sudo -n true && echo ok || echo 'sudo 需要免密或交互'"
  python ../scripts/ssh_execute.py ./config_single_key.json "sudo -n DEBIAN_FRONTEND=noninteractive apt-get update -y"
  python ../scripts/ssh_execute.py ./config_single_key.json "sudo -n DEBIAN_FRONTEND=noninteractive apt-get install -y nginx"
"""
    )


if __name__ == "__main__":
    main()

