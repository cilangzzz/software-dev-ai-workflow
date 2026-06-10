<div align="center">

# 软件开发工作流 AI.SKILL

> *"让AI成为软件开发流程中的智能伙伴，从需求到运维的全流程赋能！*

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Claude Code](https://img.shields.io/badge/Claude%20Code-Skill-blueviolet)](https://claude.ai/code)
[![AgentSkills](https://img.shields.io/badge/AgentSkills-Standard-green)](https://agentskills.io)

<br>

**一套 AI 驱动的软件开发工作流框架**，将软件工程从需求到运维的每个环节都交给 AI Agent 协作完成。

<br>

[目录结构](#目录结构) · [适用人群](#适用人群) · [能做什么](#能做什么) · [快速开始](#快速开始)

</div>

---

## 目录结构

```
software-dev-ai-workflow/
├── 0.0-通用skill/                    # 通用技能工具集（Jira、Draw.io、Word等）
├── 1.0-软件开发流程角色agent模型/      # 角色Agent模型定义（产品、研发、测试等）
├── 2.0-用例/                         # 用例示例库
│   ├── agent用例/                    # Agent使用示例（按部门分类）
│   ├── 开发流程样例/                  # 瀑布/敏捷开发流程模板
│   ├── 系统模型样例/                  # ERP、MES、VCP等系统模型
│   └── 项目管理样例/                  # 项目管理模板
├── 3.0-基础开发系统模板/              # 基础开发框架模板
├── output/                           # 输出目录
└── README.md
```

---

## 适用人群

| 角色 | 使用场景 |
|------|----------|
| **产品经理** | 快速生成PRD、用户故事、验收标准，降低文档编写成本 |
| **架构师** | 自动输出技术选型报告、架构设计文档、ADR决策记录 |
| **开发工程师** | 基于设计方案生成代码框架、API实现、数据模型 |
| **测试工程师** | 自动生成测试用例、测试报告、验收测试脚本 |
| **运维工程师** | 生成部署文档、运维手册、监控配置方案 |
| **项目经理** | 获取完整项目文档体系、进度跟踪模板 |
| **创业者/独立开发者** | 从想法到可运行代码的快速验证 |

---

## 能做什么

### 📝 产品阶段
- PRD产品需求文档
- 用户故事（User Story）
- 验收标准（Gherkin格式）
- 业务流程图

### 🏗️ 设计阶段
- 技术选型报告
- 架构设计文档
- ADR架构决策记录
- 数据库设计
- API接口设计

### 💻 开发阶段
- 项目代码框架
- 数据模型实现
- 业务逻辑代码
- 单元测试代码

### 🧪 测试阶段
- 功能测试用例
- 性能测试方案
- 安全测试清单

### 🚀 运维阶段
- 部署手册
- 运维手册
- 故障处理指南
- 监控告警配置

---

## 快速开始

### 使用步骤

```
1. 选择角色Agent → 从 1.0-软件开发流程角色agent模型/ 选择
2. 参考用例 → 查看 2.0-用例/ 中的示例
3. 输入需求 → 描述你想做什么
4. 获取产出 → AI自动生成文档或代码
```

### 典型工作流程

```
需求描述 → 产品Agent → PRD文档
    ↓
PRD文档 → 研发Agent → 架构设计 + 数据模型
    ↓
设计方案 → 研发Agent → 项目代码
    ↓
功能规格 → 测试Agent → 测试用例
    ↓
测试通过 → 运维Agent → 部署文档
```

### 示例用法

**需求分析**：
```
输入: "开发一个汽车整车装配MES系统"
输出: PRD、用户故事、验收标准、业务流程图
```

**架构设计**：
```
输入: PRD文档
输出: 系统架构设计、数据库设计、API设计文档
```

**代码生成**：
```
输入: 架构设计 + 数据模型
输出: 可运行的项目代码框架
```

---

## 已产出案例

| 项目 | 类型 | 说明 |
|------|------|------|
| [Miniai-Notepad](https://github.com/cilangzzz/Miniai-Notepad) | 前端应用 | 个人记事本，Vue3 + TypeScript，AI零手写生成 |
| [yudao-aisk-mes](https://github.com/cilangzzz/yudao-aisk-mes) | 企业系统 | 汽车装配MES，Spring Boot + Vue3，完整文档体系 |

---

## 贡献指南

欢迎贡献新的Skill或改进现有Skill：

1. Fork 本仓库
2. 创建特性分支
3. 提交 Pull Request

## 许可证

MIT License


<div align="center">

**让AI赋能软件开发全流程！**

</div>