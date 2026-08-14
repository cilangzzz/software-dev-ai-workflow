"""
SSH Skill - 系统级SSH连接管理工具

基于系统OpenSSH的SSH客户端，提供稳定可靠的SSH连接能力。

核心特性:
- ControlMaster 连接复用（10-100x性能提升）
- ProxyJump 跳板机支持（支持多级）
- 项目级配置管理
- 流式输出和交互式会话
- 批量并发操作

快速开始:
    from ssh_skill import SSHConfigLoader

    # 加载配置
    client = SSHConfigLoader.from_file(".ssh_config/prod.json")

    # 执行命令
    result = client.execute("whoami && hostname")
    print(result.stdout)

    # 批量操作
    from ssh_skill import SSHCluster
    cluster = SSHCluster.from_directory(".ssh_config/cluster/")
    results = cluster.execute_all("uptime", parallel=True)
"""

from .client import SSHClient, SSHResult
from .config import SSHConfigLoader, ServerConfig
from .cluster import SSHCluster, SSHBatchOperations
from .utils import (
    check_ssh_available,
    get_ssh_version,
    validate_key_file
)

__version__ = "0.1.0"

__all__ = [
    # 核心类
    "SSHClient",
    "SSHResult",
    "SSHConfigLoader",
    "ServerConfig",
    "SSHCluster",
    "SSHBatchOperations",

    # 工具函数
    "check_ssh_available",
    "get_ssh_version",
    "validate_key_file",
]
