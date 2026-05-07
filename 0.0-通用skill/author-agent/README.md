# Agent 编写专家

用于创建、编辑和验证研发 Agent 角色配置和技术 Skill 的专业工具。

## 目录结构

```
agent-authoring/
├── SKILL.md                              # 主Skill文件
├── templates/                            # 模板文件
│   ├── role-config.yaml                  # Agent角色配置模板
│   └── skill-yaml-tech.yaml              # 技术Skill模板
├── references/                           # 参考文档
│   ├── checklist.md                      # 验证检查清单
│   ├── agent-types-guide.md              # Agent类型参考指南
│   └── rules/                            # 规则文件目录
│       ├── backend-java.md               # Java后端规则参考
│       ├── backend-python.md             # Python后端规则参考
│       ├── backend-go.md                 # Go后端规则参考
│       ├── frontend-vue.md               # Vue前端规则参考
│       ├── frontend-react.md             # React前端规则参考
│       ├── frontend-qt.md                # Qt桌面规则参考
│       ├── data-dba.md                   # DBA规则参考
│       ├── ops-devops.md                 # DevOps规则参考
│       ├── test-engineer.md              # 测试工程师规则参考
│       ├── product-b2b.md                # B端产品规则参考
│       ├── design-uiux.md                # UI/UX设计规则参考
│       └── common-dev.md                 # 通用研发规则参考
└── README.md                             # 说明文档
```

## 功能概述

### 1. Agent 角色配置创建

支持创建各类研发角色配置：
- **后端开发**: Java、Python、Go、Node.js
- **前端开发**: Vue、React、Qt、Flutter
- **数据领域**: DBA、数据工程师、数据科学家
- **运维开发**: DevOps、SRE
- **测试开发**: 测试工程师、QA
- **产品设计**: B端产品、C端产品、UI/UX设计师

### 2. 技术 Skill 创建

支持创建技术实现类 Skill：
- 项目脚手架 Skill
- 功能实现 Skill
- 代码生成 Skill
- 架构设计 Skill

### 3. 按需规则加载

根据研发类型自动加载对应规则参考：
- 技术栈定义
- 项目结构规范
- 命名规范示例
- 代码风格模板

## 使用方式

### 快速创建 Agent

```
用户: 帮我创建一个Java后端开发的Agent角色配置

执行流程:
1. 识别研发类型: 后端Java
2. 加载 backend-java.md 规则参考
3. 收集角色信息（名称、能力等级等）
4. 使用 role-config.yaml 模板生成配置
5. 创建配置文件并验证
```

### 快速创建 Skill

```
用户: 帮我为Vue前端创建一个组件设计Skill

执行流程:
1. 识别研发类型: 前端Vue
2. 加载 frontend-vue.md 规则参考
3. 收集Skill需求（参数、流程、输出）
4. 使用 skill-yaml-tech.yaml 模板生成
5. 创建Skill文件并验证
```

## Agent 类型分类

### 研发类
| 类型 | 技术栈 | 核心能力 |
|------|-------|---------|
| Java后端 | Spring Boot, MyBatis Plus | API开发、业务逻辑 |
| Python后端 | FastAPI, Django | 异步API、数据处理 |
| Go后端 | Gin, Gorm | 微服务、高性能API |
| Vue前端 | Vue3, Pinia | 界面开发、状态管理 |
| React前端 | React, Redux | 界面开发、Hooks |
| Qt桌面 | Qt, C++ | 桌面应用开发 |
| DBA | MySQL, PostgreSQL | 数据库设计、优化 |

### 产品类
| 类型 | 关注点 | 核心能力 |
|------|-------|---------|
| B端产品 | 业务效率 | 需求分析、流程设计 |
| C端产品 | 用户增长 | 用户洞察、增长策略 |
| 数据产品 | 数据价值 | 指标设计、数据应用 |

### 设计类
| 类型 | 核心能力 | 产出物 |
|------|---------|---------|
| UI设计 | 界面设计、规范制定 | 设计稿、组件库 |
| UX设计 | 用户研究、交互设计 | 原型、研究报告 |

### 运维类
| 类型 | 核心能力 | 产出物 |
|------|---------|---------|
| DevOps | CI/CD、容器化 | 部署脚本、监控配置 |
| SRE | 可靠性保障 | SLO定义、故障预案 |

## 设计流程参考

### Agent 设计流程

1. **明确角色定位** - 定义角色所属部门和类别
2. **定义核心能力** - 列出核心技能和能力等级
3. **确定技术栈** - 根据角色类型确定技术栈
4. **配置 Skill 加载** - 确定需要和排除的 Skill
5. **定义工作流** - 设计典型工作流程
6. **制定规范** - 定义命名规范和代码风格

### Skill 设计流程

1. **明确 Skill 功能** - 定义 Skill 的目标和产出物
2. **定义触发条件** - 命令、关键词、事件触发
3. **设计输入参数** - 必填/可选参数及约束
4. **定义执行流程** - 阶段划分和步骤定义
5. **设计输出产物** - 产物类型和格式规范
6. **编写使用示例** - 真实可用的示例

## 能力等级定义

| 等级 | 描述 | 特征 |
|------|------|------|
| expert | 专家级 | 独立解决复杂问题，制定最佳实践 |
| advanced | 高级 | 独立完成复杂任务，处理异常情况 |
| intermediate | 中级 | 独立完成常规任务，需要指导 |
| beginner | 初级 | 完成基础任务，需要较多指导 |

## 相关文档

- [主Skill文件](SKILL.md) - 详细的使用说明
- [Agent类型参考](references/agent-types-guide.md) - 各类Agent的设计参考
- [检查清单](references/checklist.md) - Agent配置验证清单
- [角色配置模板](templates/role-config.yaml) - YAML模板
- [技术Skill模板](templates/skill-yaml-tech.yaml) - Skill YAML模板

---
**版本**: 1.0.0
**创建时间**: 2026-04-24