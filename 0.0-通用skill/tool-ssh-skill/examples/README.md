# examples（回归用例集）

本目录用于保存 **ssh-skill 的可运行示例与配置模板**，作为运维场景的“回归用例集”：

- 给人看：快速复制改造，减少手工写 `ssh/scp` 的概率
- 给 AI 看：提供明确范式，减少跑偏、减少反复试错

## 重要安全约定

- 本目录所有 `*.json` 都是**示例模板**：只使用占位符或保留网段 IP（如 `192.0.2.x`、`198.51.100.x`、`203.0.113.x`），禁止写入真实服务器信息/密钥/密码。
- 密码字段只允许占位符（例如 `__REPLACE_ME__`），不要提交真实密码。

## 配置示例（JSON）

- `config_template.json`：通用模板（包含 `summary` 字段示例）
- `config_single_key.json`：单机 + 密钥认证 + ControlMaster（推荐默认）
- `config_key_with_passphrase.json`：单机 + 密钥认证（带私钥密码）
- `config_single_password.json`：单机 + 密码认证（走 Paramiko 客户端连接池）
- `config_jump_single_key.json`：单跳板机 + 密钥认证
- `config_jump_double.json`：双跳板机 + 密钥认证
- `config_jump_simple.json`：简化跳板机写法（`jump_hosts` 仅写字符串）
- `config_jump_password.json`：跳板机 + 密码认证（全链路密码示例）
- `config_multi_servers.json`：多服务器配置（`servers` 字典）
- `config_env_development.json`：环境示例（开发）
- `config_env_production.json`：环境示例（生产）
- `config_temporary_access.json`：临时访问（含 `expires_at` 示例）

## 示例脚本（Python）

这些脚本主要用于演示如何用 `scripts/lib/` 的 API 进行连接、并发与交互：

- `basic_usage.py`：最小用法
- `concurrency_examples.py`：并发/批量
- `jumphost_usage_examples.py`：跳板机场景
- `interactive_session_examples.py`：交互式会话范式
- `config_usage_examples.py`：如何加载配置文件
- `test_controlmaster.py`：ControlMaster 复用行为演示

## 静态冒烟测试（推荐）

用于确保示例 JSON 长期保持可用（结构正确、元数据齐全），不需要真实连服务器：

```powershell
pwsh -NoProfile -ExecutionPolicy Bypass -File .\\run_smoke_tests.ps1
```

如只想做结构校验、不强制元数据：

```powershell
pwsh -NoProfile -ExecutionPolicy Bypass -File .\\run_smoke_tests.ps1 -StrictMetadata:$false
```
