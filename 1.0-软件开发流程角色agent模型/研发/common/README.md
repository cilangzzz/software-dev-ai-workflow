# Common 通用 Skill 目录

本目录包含研发流程中通用的 Skill 定义和配置文件，按功能领域细分为子目录。

## 目录结构

```
common/
├── 需求评审/          # 需求评审相关 Skill
│   ├── README.md
│   ├── requirement-review.md
│   └── role-config.yaml
├── 需求变更/          # 需求变更管理 Skill
│   ├── README.md
│   ├── requirement-change.md
│   └── role-config.yaml
├── 架构设计/          # 架构决策记录 Skill
│   ├── README.md
│   ├── adr.md
│   └── role-config.yaml
└── code-review.md     # 代码评审 Skill（保留在根目录）
```

## 子目录说明

### 需求评审
| 项目 | 说明 |
|------|------|
| Skill 名称 | requirement-review |
| 触发命令 | `/requirement-review` |
| 功能 | 辅助需求评审，分析需求完整性、识别设计冲突、评估变更影响 |
| 优先级 | P0 |

### 需求变更
| 项目 | 说明 |
|------|------|
| Skill 名称 | requirement-change |
| 触发命令 | `/requirement-change` |
| 功能 | 管理需求变更全流程，分析变更影响并生成追溯记录 |
| 优先级 | P0 |

### 架构设计
| 项目 | 说明 |
|------|------|
| Skill 名称 | adr |
| 触发命令 | `/adr` |
| 功能 | 创建和管理架构决策记录（ADR），建立可追溯的技术决策知识库 |
| 优先级 | P0 |

### 代码评审
| 项目 | 说明 |
|------|------|
| Skill 名称 | code-review |
| 触发命令 | `/code-review` |
| 功能 | 对代码变更进行自动化审查，检测潜在问题并提供改进建议 |
| 优先级 | P0 |
| 位置 | 保留在 common 根目录 |

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