# Common 通用 Skill 目录

本目录包含研发流程中通用的 Skill 定义和配置文件，按功能领域细分为子目录。

## ⚠️ Skill 加载机制

| Skill | 加载方式 | 说明 |
|-------|----------|------|
| 需求评审 | 命令触发 | 显式调用 `/requirement-review` |
| 需求变更 | 命令触发 | 显式调用 `/requirement-change` |
| 架构设计 | 命令触发 | 显式调用 `/adr` |
| **代码评审** | **条件触发** | Git/PR事件或文件变更自动加载 |

**代码评审 Skill 采用按需加载机制**，只有在满足特定条件时才会自动加载：
- Git 事件：`pre_commit`, `pre_push` 自动触发
- PR 事件：PR 创建/更新时自动触发
- 文件变更：代码文件（`.java`, `.py`, `.js`, `.ts`, `.vue`, `.go`）变更触发
- 可通过 `[skip-review]` 标记跳过审查

详见 [代码评审/role-config.yaml](代码评审/role-config.yaml) 的触发条件配置。

## 目录结构

```
common/
├── README.md                    # 目录总览和协作关系图
├── 需求评审/
│   ├── README.md                # 子目录索引
│   ├── requirement-review.md    # 需求评审 Skill 定义
│   └── role-config.yaml         # 角色配置和参数说明
├── 需求变更/
│   ├── README.md                # 子目录索引
│   ├── requirement-change.md    # 需求变更 Skill 定义
│   └── role-config.yaml         # 角色配置和参数说明
├── 架构设计/
│   ├── README.md                # 子目录索引
│   ├── adr.md                   # ADR Skill 定义
│   └── role-config.yaml         # 角色配置和参数说明
├── 代码评审/                     # ⚠️ 按需加载 Skill
│   ├── README.md                # 子目录索引（含触发条件说明）
│   ├── code-review.md           # 代码评审 Skill 定义
│   └── role-config.yaml         # 角色配置 + 触发条件定义
```

## 子目录说明

### 需求评审
| 项目 | 说明 |
|------|------|
| Skill 名称 | requirement-review |
| 触发命令 | `/requirement-review` |
| 加载方式 | 命令触发（显式调用） |
| 功能 | 辅助需求评审，分析需求完整性、识别设计冲突、评估变更影响 |
| 优先级 | P0 |

### 需求变更
| 项目 | 说明 |
|------|------|
| Skill 名称 | requirement-change |
| 触发命令 | `/requirement-change` |
| 加载方式 | 命令触发（显式调用） |
| 功能 | 管理需求变更全流程，分析变更影响并生成追溯记录 |
| 优先级 | P0 |

### 架构设计
| 项目 | 说明 |
|------|------|
| Skill 名称 | adr |
| 触发命令 | `/adr` |
| 加载方式 | 命令触发（显式调用） |
| 功能 | 创建和管理架构决策记录（ADR），建立可追溯的技术决策知识库 |
| 优先级 | P0 |

### 代码评审（按需加载）
| 项目 | 说明 |
|------|------|
| Skill 名称 | code-review |
| 触发命令 | `/code-review` |
| 加载方式 | **条件触发**（Git事件/PR事件/文件变更） |
| 自动触发条件 | `pre_commit`, `pre_push`, `pr_create`, `pr_update`, 代码文件变更 |
| 跳过标记 | `[skip-review]` |
| 功能 | 对代码变更进行自动化审查，检测潜在问题并提供改进建议 |
| 优先级 | P0 |

## Skill 协作关系

### 流程顺序
```
需求评审 → 架构设计 → 开发 → 需求变更 → 代码评审
```

### 协作关系图
```
┌─────────────┐     ┌─────────────┐
│ 需求评审    │────→│ 架构设计    │
│ requirement │     │ adr         │
│ -review     │     │             │
└─────────────┘     └──────┬──────┘
                          │
                          ▼
┌─────────────┐     ┌─────────────┐
│ 需求变更    │←────│ 开发实施    │
│ requirement │     │ backend/    │
│ -change     │     │ frontend    │
└─────────────┘     └──────┬──────┘
                          │
                          ▼
                   ┌─────────────┐
                   │ 代码评审    │
                   │ code-review │
                   └─────────────┘
```

## 快速参考

| 场景 | 使用 Skill | 命令 |
|------|-----------|------|
| 收到新需求文档 | 需求评审 | `/requirement-review` |
| 记录技术决策 | 架构设计 | `/adr` |
| 处理需求变更 | 需求变更 | `/requirement-change` |
| 审查代码质量 | 代码评审 | `/code-review` |