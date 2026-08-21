# 软件开发流程角色Agent模型

## 概述

本目录包含完整的软件开发流程角色Agent模型定义，用于AI辅助软件开发全生命周期。采用 **Agent角色** 和 **Skill技能** 分离的结构设计：

- **Agent角色**：定义"谁来做"，包含职责、权限、协作关系
- **Skill技能**：定义"怎么做"，包含输入输出、工作流程、模板

> 详细设计说明见：[目录结构设计说明.md](目录结构设计说明.md)

## 目录结构

```
1.0-软件开发流程角色agent模型/
├── 目录结构设计说明.md      # Agent/Skill分离结构设计文档
├── 产出物映射表.md          # 阶段-部门产出物映射关系
│
├── 产品/                    # 产品部
│   ├── agent/               # Agent角色定义
│   │   ├── product-manager.agent.yaml
│   │   ├── b2b-product-manager.agent.yaml
│   │   └── ...
│   ├── skill/               # Skill技能定义
│   │   ├── requirement-analyzer.skill.yaml
│   │   ├── user-story-generator.skill.yaml
│   │   └── ...
│   ├── references/          # 参考模板
│   └── 产出物清单.md        # 产出物清单（含条件说明）
│
├── 研发/                    # 研发部
│   ├── agent/               # Agent角色定义
│   │   ├── architect.agent.yaml
│   │   ├── backend-developer.agent.yaml
│   │   └── ...
│   ├── skill/               # Skill技能定义
│   │   ├── architect/       # 架构设计技能组
│   │   │   ├── system-architect.skill.yaml
│   │   │   ├── adr-writer.skill.yaml
│   │   │   └── tech-selector.skill.yaml
│   │   ├── implement/       # 代码实现技能组
│   │   ├── design/          # 详细设计技能组
│   │   └── process/         # 流程管理技能组
│   ├── tech-selector.yaml   # 技术选型配置
│   ├── skill-collaboration.yaml
│   └── 产出物清单.md
│
├── 测试/                    # 测试部
│   ├── agent/
│   ├── skill/
│   └── 产出物清单.md
│
├── 运维/                    # 运维部
├── 安全/                    # 安全部
├── 数据/                    # 数据部
└── 项目管理/                # 项目管理
```

## Agent角色总览

| 部门 | Agent角色 | Skill数量 | 核心职责 | 负责阶段 |
|------|----------|-----------|----------|----------|
| 产品部 | product-manager, b2b-product-manager, b2c-product-manager, requirement-researcher | 6 | 需求采集、需求分析、用户故事、验收标准 | 需求阶段 |
| 研发部 | architect, backend-developer, frontend-developer, tech-lead | 12 | 架构设计、代码实现、代码审查 | 设计阶段、开发阶段 |
| 测试部 | test-engineer, qa-lead, automation-engineer | 3 | 测试用例、测试执行、Bug分析 | 测试阶段 |
| 运维部 | devops-engineer, sre-engineer | 2 | CI/CD配置、部署分析 | 部署阶段、运维阶段 |
| 安全部 | security-engineer | 3 | 安全扫描、代码安全审查 | 安全阶段 |
| 数据部 | data-engineer | 2 | 数据血缘追踪、数据质量检查 | 数据阶段 |

## 核心概念

### Agent角色 vs Skill技能

| 概念 | 定义 | 文件后缀 | 说明 |
|------|------|----------|------|
| **Agent角色** | 承担特定职责的智能实体 | `.role.md` / `.agent.md` | 定义职责、权限、协作关系 |
| **Skill技能** | 可被调用的具体能力 | `.skill.md` | 定义输入输出、工作流程、模板 |

> 注：本目录实际文件后缀为 `.md`（无 `.yaml`）。

### 关系模型

```
Agent（架构师） ──调用──> Skill（系统架构设计）
    │
    ├── 可调用多个Skill
    └── Skill可被多个Agent共享
```

## Skill索引

### 产品部Skill

| Skill名称 | 功能描述 | 触发命令 | 文件路径 |
|-----------|----------|----------|----------|
| requirement-analyzer | 解析需求描述，生成结构化PRD框架 | `/requirement-analyzer` | [产品/skill/requirement-analyzer.skill.md](产品/skill/requirement-analyzer.skill.md) |
| user-story-generator | 生成符合INVEST原则的用户故事 | `/user-story-generator` | [产品/skill/user-story-generator.skill.md](产品/skill/user-story-generator.skill.md) |
| acceptance-criteria-writer | 编写Gherkin格式的验收标准 | `/acceptance-criteria-writer` | [产品/skill/acceptance-criteria-writer.skill.md](产品/skill/acceptance-criteria-writer.skill.md) |
| user-manual-writer | 生成用户手册和快速入门指南 | `/user-manual-writer` | [产品/skill/user-manual-writer.skill.md](产品/skill/user-manual-writer.skill.md) |
| business-rule-analyzer | 提取和分析业务规则 | `/business-rule-analyzer` | [产品/skill/business-rule-analyzer.skill.md](产品/skill/business-rule-analyzer.skill.md) |
| requirement-researcher | 从Web搜索行业需求文档，提炼功能需求点 | `/requirement-researcher` | [产品/skill/requirement-researcher.skill.md](产品/skill/requirement-researcher.skill.md) |

### 研发部Skill

| Skill名称 | 功能描述 | 触发命令 | 文件路径 |
|-----------|----------|----------|----------|
| architect | 系统架构设计，生成架构图 | `/architect` | [研发/skill/architect/system-architect.skill.md](研发/skill/architect/system-architect.skill.md) |
| implement | 功能代码实现 | `/implement` | [研发/skill/implement/](研发/skill/implement/) |
| scaffold | 项目脚手架生成 | `/scaffold` | [研发/skill/implement/](研发/skill/implement/) |
| module-designer | 功能模块详细设计 | `/module-designer` | [研发/skill/design/module-designer.skill.md](研发/skill/design/module-designer.skill.md) |
| api-designer | RESTful API接口设计 | `/api-designer` | [研发/skill/design/api-designer.skill.md](研发/skill/design/api-designer.skill.md) |
| state-machine-designer | 状态机设计 | `/state-machine-designer` | [研发/skill/design/state-machine-designer.skill.md](研发/skill/design/state-machine-designer.skill.md) |
| data-model-designer | 数据模型设计 | `/data-model-designer` | [研发/skill/design/data-model-designer.skill.md](研发/skill/design/data-model-designer.skill.md) |
| code-review | 代码审查 | `/code-review` | [研发/skill/process/code-review.skill.md](研发/skill/process/code-review.skill.md) |

### 测试部Skill

| Skill名称 | 功能描述 | 触发命令 | 文件路径 |
|-----------|----------|----------|----------|
| test-case-generator | 根据需求生成测试用例 | `/test-case-generator` | [测试/skill/test-case-generator.skill.md](测试/skill/test-case-generator.skill.md) |
| test-executor | 执行测试并记录结果 | `/test-executor` | [测试/skill/test-executor.skill.md](测试/skill/test-executor.skill.md) |
| bug-analyzer | 分析Bug原因并提供修复建议 | `/bug-analyzer` | [测试/skill/bug-analyzer.skill.md](测试/skill/bug-analyzer.skill.md) |

### 运维部Skill

| Skill名称 | 功能描述 | 触发命令 | 文件路径 |
|-----------|----------|----------|----------|
| ci-pipeline-assistant | CI/CD流水线配置 | `/ci-pipeline-assistant` | [运维/skill/ci-pipeline-assistant.skill.md](运维/skill/ci-pipeline-assistant.skill.md) |
| deploy-analyzer | 部署分析和配置 | `/deploy-analyzer` | [运维/skill/deploy-analyzer.skill.md](运维/skill/deploy-analyzer.skill.md) |

### 安全部Skill

| Skill名称 | 功能描述 | 触发命令 | 文件路径 |
|-----------|----------|----------|----------|
| security-scan | 安全漏洞扫描 | `/security-scan` | [安全/skill/security-scan.skill.md](安全/skill/security-scan.skill.md) |
| security-code-review | 代码安全审查 | `/security-code-review` | [安全/skill/security-code-review.skill.md](安全/skill/security-code-review.skill.md) |
| security-review | 安全审查流程 | `/security-review` | [安全/skill/security-review.skill.md](安全/skill/security-review.skill.md) |
| security-threat-model | 威胁建模分析 | `/security-threat-model` | [安全/skill/security-threat-model.skill.md](安全/skill/security-threat-model.skill.md) |

## 使用指南

### 1. 快速开始

使用Agent模型的最简单方式是通过自然语言触发：

```
"帮我分析这个需求：需要一个汽车整车装配MES系统"
```

AI将自动识别意图并调用 `requirement-analyzer` skill。

### 2. 命令触发

也可以直接使用斜杠命令：

```
/requirement-analyzer
/architect
```

### 3. 工作流串联

多个Agent可以串联完成复杂任务：

```
需求采集 → 需求分析 → 用户故事生成 → 架构设计 → 模块设计 → API设计 → 测试用例生成
```

### 4. 产出物模板

所有产出物都有标准化模板，位于各部门的 `references/` 目录：

- 产品部模板：`产品/references/`
- PRD模板：`产品/references/prd-template.md`
- SRS模板：`产品/references/srs-template.md`

### 5. 条件化产出物

产出物分为三类，根据项目情况按需产出：

| 类型 | 说明 | 示例 |
|------|------|------|
| **必需产出物** | 所有项目必须产出 | 架构设计文档、ADR |
| **条件产出物** | 特定场景必须产出 | 风险评估矩阵（大型项目） |
| **可选产出物** | 按需产出 | 性能预测报告 |

详细说明见各部门的 `产出物清单.md`。

## Agent协作配置

Agent之间的协作关系通过 `skill-collaboration.yaml` 配置：

```yaml
workflows:
  - name: requirement-to-design
    sequence:
      - agent: requirement-analyzer
        phase: 需求分析
        outputs:
          - PRD文档
      - agent: architect
        phase: 架构设计
        inputs:
          - PRD文档
        outputs:
          - 系统架构设计
```

## 产出物映射

各阶段产出物与负责部门的映射关系见 [产出物映射表.md](产出物映射表.md)。

| 阶段 | 主要负责部门 | 产出物数量 |
|------|-------------|-----------|
| 需求阶段 | 产品部 | 10 |
| 设计阶段 | 研发部 | 13 |
| 开发阶段 | 研发部 | 8 |
| 测试阶段 | 测试部 | 9 |
| 部署阶段 | 运维部 | 7 |
| 运维阶段 | 运维部 | 6 |

## 质量标准

每个Skill都定义了明确的质量标准：

| 阶段 | 检查项 | 通过标准 |
|------|--------|----------|
| 需求就绪 | PRD完整性、用户故事覆盖度 | 100%需求覆盖 |
| 设计就绪 | 架构设计评审通过、数据库设计完整 | 技术评审通过 |
| 开发就绪 | 代码审查通过、单元测试覆盖率 | 覆盖率≥80% |
| 测试就绪 | 测试用例执行完成、无P0/P1 Bug | Bug修复率100% |

## 更新记录

| 日期 | 更新内容 | 更新人 |
|------|----------|--------|
| 2026-03-24 | 初始化Agent模型 | AI Agent |
| 2026-06-10 | 新增细分业务Skill：module-designer, api-designer, state-machine-designer, data-model-designer, business-rule-analyzer | Claude Agent |
| 2026-06-11 | 重构目录结构：分离Agent角色和Skill技能，增加条件化产出物 | Claude Agent |
| 2026-06-15 | 新增需求研究员(requirement-researcher)角色和需求采集技能，支持从Web采集行业需求文档 | Claude Agent |

## 相关文档

- [目录结构设计说明](目录结构设计说明.md) - Agent/Skill分离结构详解
- [产出物映射表](产出物映射表.md)
- [产品部产出物清单](产品/产出物清单.md)
- [研发部产出物清单](研发/产出物清单.md)
- [测试部产出物清单](测试/产出物清单.md)
- [运维部产出物清单](运维/产出物清单.md)