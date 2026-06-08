<div align="center">

# 软件开发工作流 AI.SKILL

> 让 AI 成为软件开发流程中的智能伙伴，从需求到运维的全流程赋能

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Claude Code](https://img.shields.io/badge/Claude%20Code-Skill-blueviolet)](https://claude.ai/code)
[![AgentSkills](https://img.shields.io/badge/AgentSkills-Standard-green)](https://agentskills.io)

</div>

## 这是什么

一套 **AI 驱动的软件开发全流程框架**。它不是代码库，而是一个结构化的知识体系——定义了 AI Agent 在软件开发各角色中"该怎么干、干什么、产出什么"。你只需描述想做什么，AI 按流程自动完成从需求到运维的全链路产出。

**8 大角色 Agent，覆盖完整研发链路：**

| 角色 | 能力 | 核心产出 |
|------|------|----------|
| 📋 产品 | 需求分析、用户故事、验收标准 | PRD、Gherkin 验收、设计系统 |
| 🏗️ 研发 | 架构设计、代码生成、CRUD | ADR、数据模型、完整可运行代码 |
| 🧪 测试 | 用例生成、执行、缺陷分析 | 测试报告（功能覆盖率≥95%） |
| 🚀 运维 | 部署分析、CI/CD | 运维手册、故障处理指南 |
| 🔒 安全 | 威胁建模、安全审计 | STRIDE 威胁报告、加固方案 |
| 🎨 设计 | 设计系统、设计转代码 | 组件规范、样式代码 |
| 📊 数据 | 数据质量、血缘追踪 | 数据质量报告、血缘图 |
| 📁 项目管理 | 进度规划、风险管控 | 里程碑报告、风险登记册 |

**框架特性：**

- 🔄 **双流程支持** — 瀑布 / 敏捷全流程定义，含质量门控检查点（Gate 1-5）
- 🏭 **行业系统模型** — 内置 ERP（12 模块）、MES（10+ 模块）、语音社区等完整参考架构
- 🔧 **20+ 通用技能** — Word、Draw.io、Notion、Jira、禅道等工具集成
- 🧬 **可自扩展** — 通过 `author-agent` / `author-skill` 元技能，AI 自行创建新角色和新技能
- 📐 **质量门控** — 每阶段有可量化检查标准，不达标不放行

> **核心理念**：人类定义目标和决策，AI 负责执行和产出。

## 目录结构

```
software-dev-ai-workflow/
├── 0.0-通用skill/                     # 通用技能工具集（Jira、Draw.io、Word等）
├── 1.0-软件开发流程角色agent模型/       # 角色Agent定义（产品、研发、测试、运维等）
├── 2.0-软件开发流程/                   # 瀑布/敏捷双流程、产出物清单
├── 3.0-用例/                          # 实际用例示例
├── 4.0-系统模型/                       # 系统产出模型（ERP、MES、SaaS）
├── 5.0-基础开发系统模板/               # 基础开发框架模板
├── 6.0-基础开发项目管理模板/           # 项目管理模板
└── output/                            # 输出目录
```

## 开发流程

```
需求分析 → 方案制定 → 架构设计 → 模型设计 → 代码开发 → 测试验证 → 部署上线
  产品Agent    研发Agent    研发Agent    研发Agent   测试Agent   运维Agent
  PRD/故事     技术选型     ADR/架构     数据模型    测试报告    运维手册
```

每阶段由专属 Agent 驱动，Gate 检查点确保质量。

## 快速开始

1. 选择角色 Agent → [`1.0-软件开发流程角色agent模型/`](1.0-软件开发流程角色agent模型/)
2. 选择开发流程 → [`2.0-软件开发流程/`](2.0-软件开发流程/)（瀑布/敏捷）
3. 参考系统模型 → [`4.0-系统模型/`](4.0-系统模型/)
4. 产出物输出至 → [`output/`](output/)

## 示例项目

| 项目 | 类型 | 说明 | 链接 |
|------|------|------|------|
| **MiniAI记事本** | 前端全栈 | 零手写代码，Vue 3 + TypeScript，整合新闻/笔记/记账 | [GitHub](https://github.com/cilangzzz/Miniai-Notepad) |
| **Crosshair Pro** | 桌面应用 | FPS准心覆盖工具，WPF + .NET 8，MVVM架构，5种准心样式+自定义图片 | [GitHub](https://github.com/cilangzzz/Crosshair) |
| **MES制造执行系统** | 企业后端 | 汽车整车装配MES，覆盖工单→成品全流程 | [GitHub](https://github.com/cilangzzz/yudao-aisk-mes) |

以上项目的产品方案、研发方案、代码、测试文档均由 AI 自动生成。

## 贡献

欢迎贡献新的 Skill 或改进现有 Skill：Fork → 创建分支 → 提交 PR

## 许可证

[MIT License](LICENSE)