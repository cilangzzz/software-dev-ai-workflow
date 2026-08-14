# SSH Skill

> 为 Claude Code 打造的企业级 SSH 管理工具，让远程服务器操作像本地一样简单高效

[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Version](https://img.shields.io/badge/version-3.3.1-green.svg)](SKILL.md)

## 📖 简介

本 Skill 由 [badseal/ssh-skill](https://github.com/badseal/ssh-skill) v3.3.1 移植而来，是 Claude Code 进行 SSH 远程操作的统一入口。集成在通用工具集中，为软件开发工作流提供强大的远程服务器管理能力。

## 🚀 核心特性

| 特性 | 说明 |
|------|------|
| 🚀 **守护进程长连接** | 首次连接后自动启动守护进程，命令响应从 ~0.45s 降至 ~0.12s（**3.75x** 性能提升） |
| 🔄 **自动连接复用** | 多个 Claude Code 实例可共享同一守护进程 |
| 📦 **SFTP 高级传输** | 支持断点续传、进度显示、目录递归上传/下载 |
| 🌐 **服务器间直接传输** | 数据直接在服务器间传输，无需本地中转 |
| 🔌 **SSH 隧道** | 支持本地端口转发，访问远程内网服务（数据库、Web 服务等） |
| 🎯 **跳板机支持** | 通过 ProxyJump 自动处理多级跳板机 |
| ⚡ **批量并发操作** | 支持对多台服务器并发执行命令 |
| 🛡️ **自动错误恢复** | SSH 连接断开自动重连（最多 3 次） |

## 📂 目录结构

```
tool-ssh-skill/
├── SKILL.md                          # Claude Code Skill 主文档（必读）
├── _meta.json                        # Skill 元数据
├── README.md                         # 本文件
├── .gitignore
├── scripts/                          # 核心脚本目录
│   ├── ssh_execute.py               # 远程命令执行
│   ├── ssh_upload.py                # 文件上传
│   ├── ssh_download.py              # 文件下载
│   ├── ssh_server_transfer.py       # 服务器间传输
│   ├── ssh_cluster.py               # 批量操作
│   ├── ssh_config_manager_v3.py     # 配置管理
│   ├── ssh_tunnel.py                # SSH 隧道
│   ├── ssh_daemon.py                # 守护进程管理
│   ├── ssh_key_manager.py           # 密钥管理
│   ├── deploy_pubkey.py             # 公钥部署
│   └── lib/                          # 公共库
└── examples/                         # 配置和使用示例
    ├── README.md
    ├── basic_usage.py
    ├── config_*.json                # 各种配置模板
    ├── jumphost_usage_examples.py
    ├── test_controlmaster.py
    └── ...
```

## 📦 依赖

```bash
pip install paramiko
```

## 🔧 安装步骤

1. **安装依赖**：`pip install paramiko`
2. **放置 Skill**：将 `tool-ssh-skill` 目录放到 `.claude/skills/` 下（已包含在仓库中）
3. **配置 SSH**：在 `~/.ssh/config` 中添加服务器配置（参考 [examples/](examples/) 中的 config_*.json 模板）
4. **开始使用**：通过快捷命令或自然语言触发

## 🎯 快速开始

### 执行远程命令

```bash
python ~/.claude/skills/ssh-skill/scripts/ssh_execute.py prod-web-01 "systemctl status nginx"
```

### 上传文件

```bash
MSYS_NO_PATHCONV=1 python ~/.claude/skills/ssh-skill/scripts/ssh_upload.py prod-web-01 ./app.tar.gz /tmp/
```

### 下载文件

```bash
MSYS_NO_PATHCONV=1 python ~/.claude/skills/ssh-skill/scripts/ssh_download.py prod-web-01 /var/log/app.log ./app.log
```

### 服务器间传输

```bash
MSYS_NO_PATHCONV=1 python ~/.claude/skills/ssh-skill/scripts/ssh_server_transfer.py source-server /data/backup.tar.gz target-server /backup/
```

### 批量操作

```bash
python ~/.claude/skills/ssh-skill/scripts/ssh_cluster.py "uptime" --parallel
```

## ⚡ 快捷命令（Claude Code 中）

| 命令 | 功能 |
|------|------|
| `/ssh-skill list` | 列出所有已配置的服务器 |
| `/ssh-skill find <关键词>` | 查找匹配的服务器 |
| `/ssh-skill transfer <源> <源路径> <目标> <目标路径>` | 服务器间文件传输 |
| `/ssh-skill tunnel <别名> <端口>` | 启动 SSH 隧道 |
| `/ssh-skill help` | 显示帮助信息 |

## 🔑 自然语言触发示例

在 Claude Code 中，自然语言描述会触发此 Skill：

```
"在 prod-web-01 上执行 systemctl status nginx"
"上传 ./app.tar.gz 到 prod-web-01 的 /tmp 目录"
"从 old-server 迁移数据到 new-server"
"建立到 prod-db-01 的 MySQL 隧道"
"在所有生产环境服务器上执行 df -h"
```

## 📈 性能对比

| 模式 | 单次命令 | 连续 10 条 | 连续 30 条 |
|------|----------|-----------|-----------|
| 直连 | ~0.45s | ~4.5s | ~13.5s |
| **守护进程** | **~0.12s** | **~1.2s** | **~3.6s** |

## 📚 详细文档

- [SKILL.md](SKILL.md) - Claude Code Skill 完整使用文档
- [examples/README.md](examples/README.md) - 配置与使用示例
- [_meta.json](_meta.json) - 元数据

## ⚠️ 强制规则

- 所有 SSH 操作必须通过本 Skill 的 Python 脚本
- **禁止**直接写 `ssh` 或 `scp` 命令（首次配置公钥除外）
- 路径必须使用正斜杠 `/`
- 不要用 `cd` 切换到脚本目录，直接用完整路径调用
- 使用别名（alias）标识服务器
- 对同一服务器的多个只读查询，优先合并为一次调用

## 📄 许可证

MIT License - 详见 [LICENSE](https://github.com/badseal/ssh-skill/blob/main/LICENSE)

## 👨‍💻 原作者

- Michael Zhang - [@badseal](https://github.com/badseal)

---

**集成到 software-dev-ai-workflow 通用工具集** | 2026-08-14