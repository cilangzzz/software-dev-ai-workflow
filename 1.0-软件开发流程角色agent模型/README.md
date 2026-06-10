# 软件开发流程角色Agent模型

## 概述

本目录包含完整的软件开发流程角色Agent模型定义，用于AI辅助软件开发全生命周期。每个Agent角色都有明确的职责、技能(Skill)和产出物定义。

## 目录结构

```
1.0-软件开发流程角色agent模型/
├── 产出物映射表.md              # 阶段-部门产出物映射关系
├── 产品/                        # 产品部Agent
│   ├── 产出物清单.md            # 产品部产出物清单
│   ├── role-config.yaml         # 角色配置
│   ├── references/              # 参考模板
│   │   ├── prd-template.md      # PRD模板
│   │   ├── srs-template.md      # SRS模板
│   │   └── ...
│   └── skill/                   # 产品部技能
│       ├── requirement-analyzer.md
│       ├── user-story-generator.md
│       ├── acceptance-criteria-writer.md
│       ├── user-manual-writer.md
│       └── 业务模块/             # 细分业务技能
│           └── business-rule-analyzer.md
├── 研发/                        # 研发部Agent
│   ├── 产出物清单.md
│   ├── skill-collaboration.yaml # Agent协作配置
│   ├── tech-selector.yaml       # 技术选型配置
│   ├── backend/                 # 后端开发技能
│   │   └── java/
│   │       ├── architect.md
│   │       ├── implement.md
│   │       └── scaffold.md
│   ├── frontend/                # 前端开发技能
│   ├── common/                  # 通用技能
│   │   ├── 代码评审/
│   │   ├── 架构设计/
│   │   ├── 需求变更/
│   │   └── 需求评审/
│   └── skill/                   # 研发部技能
│       ├── 模块设计/             # 细分业务技能
│       │   ├── module-designer.md
│       │   ├── api-designer.md
│       │   └── state-machine-designer.md
│       └── 数据模型/             # 细分业务技能
│           └── data-model-designer.md
├── 测试/                        # 测试部Agent
│   ├── 产出物清单.md
│   └── skill/
│       ├── test-case-generator.md
│       ├── test-executor.md
│       └── bug-analyzer.md
├── 运维/                        # 运维部Agent
│   ├── 产出物清单.md
│   └── skill/
│       ├── ci-cd-pipeline.md
│       └── deployment-analyzer.md
├── 安全/                        # 安全部Agent
│   ├── 产出物清单.md
│   └── skill/
│       ├── security-scan.md
│       ├── security-code-review.md
│       └── security-threat-model.md
├── 数据/                        # 数据部Agent
│   ├── 产出物清单.md
│   └── skill/
│       ├── data-lineage-trace.md
│       └── data-quality-check.md
└── 项目管理/                    # 项目管理Agent
    └── skill/
        └── ...
```

## Agent角色总览

| 部门 | Agent角色 | Skill数量 | 核心职责 | 负责阶段 |
|------|----------|-----------|----------|----------|
| 产品部 | requirement-analyzer, user-story-generator | 5 | 需求分析、用户故事、验收标准 | 需求阶段 |
| 研发部 | architect, implement, code-review | 11 | 架构设计、代码实现、代码审查 | 设计阶段、开发阶段 |
| 测试部 | test-case-generator, test-executor | 3 | 测试用例、测试执行、Bug分析 | 测试阶段 |
| 运维部 | ci-cd-pipeline, deployment-analyzer | 2 | CI/CD配置、部署分析 | 部署阶段、运维阶段 |
| 安全部 | security-scan, security-code-review | 3 | 安全扫描、代码安全审查 | 安全阶段 |
| 数据部 | data-lineage, data-quality-check | 2 | 数据血缘追踪、数据质量检查 | 数据阶段 |

## Skill索引

### 产品部Skill

| Skill名称 | 功能描述 | 触发命令 |
|-----------|----------|----------|
| requirement-analyzer | 解析需求描述，生成结构化PRD框架 | `/requirement-analyzer` |
| user-story-generator | 生成符合INVEST原则的用户故事 | `/user-story-generator` |
| acceptance-criteria-writer | 编写Gherkin格式的验收标准 | `/acceptance-criteria-writer` |
| user-manual-writer | 生成用户手册和快速入门指南 | `/user-manual-writer` |
| business-rule-analyzer | 提取和分析业务规则 | `/business-rule-analyzer` |

### 研发部Skill

| Skill名称 | 功能描述 | 触发命令 |
|-----------|----------|----------|
| architect | 系统架构设计，生成架构图 | `/architect` |
| implement | 功能代码实现 | `/implement` |
| scaffold | 项目脚手架生成 | `/scaffold` |
| module-designer | 功能模块详细设计 | `/module-designer` |
| api-designer | RESTful API接口设计 | `/api-designer` |
| state-machine-designer | 状态机设计 | `/state-machine-designer` |
| data-model-designer | 数据模型设计 | `/data-model-designer` |
| code-review | 代码审查 | `/code-review` |

### 测试部Skill

| Skill名称 | 功能描述 | 触发命令 |
|-----------|----------|----------|
| test-case-generator | 根据需求生成测试用例 | `/test-case-generator` |
| test-executor | 执行测试并记录结果 | `/test-executor` |
| bug-analyzer | 分析Bug原因并提供修复建议 | `/bug-analyzer` |

### 运维部Skill

| Skill名称 | 功能描述 | 触发命令 |
|-----------|----------|----------|
| ci-cd-pipeline | CI/CD流水线配置 | `/ci-cd-pipeline` |
| deployment-analyzer | 部署分析和配置 | `/deployment-analyzer` |

### 安全部Skill

| Skill名称 | 功能描述 | 触发命令 |
|-----------|----------|----------|
| security-scan | 安全漏洞扫描 | `/security-scan` |
| security-code-review | 代码安全审查 | `/security-code-review` |
| security-threat-model | 威胁建模分析 | `/security-threat-model` |

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
```

### 3. 工作流串联

多个Agent可以串联完成复杂任务：

```
需求分析 → 用户故事生成 → 架构设计 → 模块设计 → API设计 → 测试用例生成
```

### 4. 产出物模板

所有产出物都有标准化模板，位于各部门的 `references/` 目录：

- 产品部模板：`产品/references/`
- PRD模板：`产品/references/prd-template.md`
- SRS模板：`产品/references/srs-template.md`

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

## 相关文档

- [产出物映射表](产出物映射表.md)
- [产品部产出物清单](产品/产出物清单.md)
- [研发部产出物清单](研发/产出物清单.md)
- [测试部产出物清单](测试/产出物清单.md)
- [运维部产出物清单](运维/产出物清单.md)