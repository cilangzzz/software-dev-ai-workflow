# 按阶段产出物清单（汇总）

> 自动生成自 `2.0-用例/开发流程样例/*/产出物清单.md`。
> 修改源文件后运行 `python scripts/deliverables-generator.py` 重新生成。

## 瀑布流程

| 阶段 | 中文名称 | 英文名称 | 类型 | 优先级 | 说明 |
|------|---------|---------|------|--------|------|
| 01-需求阶段 | 产品需求文档 | PRD (Product Requirement Document) | 文档 | P0 | 详细描述产品功能、用户场景、业务规则 |
| 01-需求阶段 | 用户故事 | User Story | 文档 | P0 | 从用户视角描述需求，格式：作为...我希望...以便... |
| 01-需求阶段 | 验收标准 | Acceptance Criteria | 文档 | P0 | 定义需求完成的验收条件 |
| 01-需求阶段 | 用例图 | Use Case Diagram | 图表 | P1 | 描述系统与用户的交互场景 |
| 01-需求阶段 | 用户旅程图 | User Journey Map | 图表 | P1 | 描述用户在系统中的操作路径 |
| 01-需求阶段 | 业务流程图 | Business Process Diagram | 图表 | P1 | 描述业务操作流程 |
| 01-需求阶段 | 思维导图 | Mind Map | 图表 | P2 | 需求拆解和关系梳理 |
| 01-需求阶段 | 需求追溯矩阵 | RTM (Requirement Traceability Matrix) | 矩阵 | P1 | 需求与测试用例的映射关系 |
| 01-需求阶段 | 竞品分析报告 | Competitive Analysis Report | 报告 | P2 | 竞品功能对比分析 |
| 01-需求阶段 | 市场调研报告 | Market Research Report | 报告 | P2 | 市场现状和机会分析 |
| 02-设计阶段 | 系统架构图 | System Architecture Diagram | 图表 | P0 | 系统整体架构和组件关系 |
| 02-设计阶段 | 技术选型报告 | Technology Selection Report | 文档 | P0 | 技术栈选择及理由 |
| 02-设计阶段 | 架构决策记录 | ADR (Architecture Decision Record) | 文档 | P0 | 重要架构决策的背景和理由 |
| 02-设计阶段 | 实体关系图 | ER Diagram | 图表 | P0 | 数据库实体关系设计 |
| 02-设计阶段 | 数据流图 | Data Flow Diagram | 图表 | P1 | 数据在系统中的流转过程 |
| 02-设计阶段 | 数据库设计文档 | Database Design Document | 文档 | P0 | 表结构、索引、字段说明 |
| 02-设计阶段 | API设计文档 | API Design Document | 文档 | P0 | 接口定义、请求响应格式 |
| 02-设计阶段 | 模块划分文档 | Module Division Document | 文档 | P1 | 系统模块划分及职责 |
| 02-设计阶段 | 接口设计文档 | Interface Design Document | 文档 | P1 | 模块间接口定义 |
| 02-设计阶段 | 线框图 | Wireframe | 图表 | P1 | 页面布局草图 |
| 02-设计阶段 | 原型图 | Prototype | 图表 | P0 | 可交互的产品原型 |
| 02-设计阶段 | UI设计规范 | UI Design Specification | 文档 | P1 | 视觉设计标准和组件库 |
| 02-设计阶段 | 设计系统文档 | Design System Document | 文档 | P2 | 设计语言、组件规范 |
| 03-开发阶段 | 详细设计文档 | Detailed Design Document | 文档 | P1 | 模块内部实现设计 |
| 03-开发阶段 | 开发计划 | Development Plan | 计划 | P0 | 开发任务分解和时间安排 |
| 03-开发阶段 | 编码规范 | Coding Standards | 文档 | P0 | 代码风格和质量标准 |
| 03-开发阶段 | 版本控制策略 | Version Control Strategy | 文档 | P1 | 分支管理、提交规范 |
| 03-开发阶段 | 代码审查清单 | Code Review Checklist | 清单 | P0 | 代码审查要点 |
| 03-开发阶段 | 技术债务清单 | Technical Debt List | 清单 | P2 | 待优化项和改进计划 |
| 03-开发阶段 | 第三方集成文档 | Third-party Integration Document | 文档 | P1 | 外部服务对接说明 |
| 03-开发阶段 | 环境配置文档 | Environment Configuration Document | 文档 | P0 | 开发、测试、生产环境配置 |
| 04-测试阶段 | 测试计划 | Test Plan | 计划 | P0 | 测试范围、策略、资源安排 |
| 04-测试阶段 | 测试用例 | Test Case | 清单 | P0 | 详细测试步骤和预期结果 |
| 04-测试阶段 | 测试执行报告 | Test Execution Report | 报告 | P0 | 测试结果统计和分析 |
| 04-测试阶段 | 缺陷报告 | Bug Report | 报告 | P0 | 问题记录和状态跟踪 |
| 04-测试阶段 | 测试覆盖率报告 | Test Coverage Report | 报告 | P1 | 代码覆盖率统计 |
| 04-测试阶段 | 性能测试报告 | Performance Test Report | 报告 | P1 | 性能指标和瓶颈分析 |
| 04-测试阶段 | 安全测试报告 | Security Test Report | 报告 | P1 | 安全漏洞和风险评估 |
| 04-测试阶段 | 用户验收测试报告 | UAT Report | 报告 | P0 | 用户验收结果 |
| 04-测试阶段 | 自动化测试脚本 | Automation Test Script | 代码 | P2 | 自动化测试代码 |
| 05-部署阶段 | 部署计划 | Deployment Plan | 计划 | P0 | 部署步骤和回滚方案 |
| 05-部署阶段 | CI/CD流水线配置 | CI/CD Pipeline Configuration | 配置 | P0 | 持续集成/部署配置 |
| 05-部署阶段 | 发布说明 | Release Notes | 文档 | P0 | 版本更新内容 |
| 05-部署阶段 | 运维手册 | Operations Manual | 文档 | P0 | 系统运维操作指南 |
| 05-部署阶段 | 监控告警配置 | Monitoring & Alert Configuration | 配置 | P1 | 系统监控指标和告警规则 |
| 05-部署阶段 | 容灾方案 | Disaster Recovery Plan | 计划 | P1 | 灾备和恢复策略 |
| 05-部署阶段 | 数据迁移方案 | Data Migration Plan | 计划 | P2 | 数据迁移步骤和验证 |
| 06-运维阶段 | 运维手册 | Operations Manual | 文档 | P0 | 日常运维操作指南 |
| 06-运维阶段 | 故障处理手册 | Incident Response Guide | 文档 | P0 | 故障排查和处理流程 |
| 06-运维阶段 | SLA文档 | SLA Document | 文档 | P1 | 服务等级协议 |
| 06-运维阶段 | 监控报表 | Monitoring Dashboard | 图表 | P1 | 系统运行状态可视化 |
| 06-运维阶段 | 容量规划报告 | Capacity Planning Report | 报告 | P2 | 资源需求和扩展计划 |
| 06-运维阶段 | 成本分析报告 | Cost Analysis Report | 报告 | P2 | 云资源成本统计 |
| 08-安全阶段 | 威胁模型 | Threat Model | 文档 | P0 | 安全威胁分析 |
| 08-安全阶段 | 安全审计报告 | Security Audit Report | 报告 | P0 | 安全检查结果 |
| 08-安全阶段 | 漏洞扫描报告 | Vulnerability Scan Report | 报告 | P0 | 安全漏洞清单 |
| 08-安全阶段 | 渗透测试报告 | Penetration Test Report | 报告 | P1 | 渗透测试发现 |
| 08-安全阶段 | 安全合规报告 | Compliance Report | 报告 | P1 | 合规性检查结果 |
| 09-数据阶段 | 数据字典 | Data Dictionary | 文档 | P0 | 数据元素定义 |
| 09-数据阶段 | 数据质量报告 | Data Quality Report | 报告 | P0 | 数据质量检查结果 |
| 09-数据阶段 | 数据血缘图 | Data Lineage Diagram | 图表 | P1 | 数据来源和流向 |
| 09-数据阶段 | ETL设计文档 | ETL Design Document | 文档 | P1 | 数据处理流程设计 |
| 10-项目管理阶段 | 项目计划 | Project Plan | 计划 | P0 | 项目整体规划和里程碑 |
| 10-项目管理阶段 | 工作分解结构 | WBS (Work Breakdown Structure) | 清单 | P0 | 任务层级分解 |
| 10-项目管理阶段 | 甘特图 | Gantt Chart | 图表 | P1 | 项目进度时间线 |
| 10-项目管理阶段 | 里程碑计划 | Milestone Plan | 计划 | P0 | 关键节点和交付物 |
| 10-项目管理阶段 | 风险管理计划 | Risk Management Plan | 计划 | P1 | 风险识别和应对策略 |
| 10-项目管理阶段 | 项目状态报告 | Project Status Report | 报告 | P0 | 周期性项目进度汇报 |
| 10-项目管理阶段 | 会议纪要 | Meeting Minutes | 文档 | P1 | 会议决议和待办事项 |
| 10-项目管理阶段 | 变更请求 | Change Request | 文档 | P1 | 需求变更申请和审批 |
| 10-项目管理阶段 | 决策记录 | Decision Log | 清单 | P2 | 重要决策的记录 |

_瀑布流程共计 71 项产出物_

## 敏捷流程

| 阶段 | 中文名称 | 英文名称 | 类型 | 优先级 | 说明 |
|------|---------|---------|------|--------|------|
| 01-项目启动 | 项目愿景文档 | Project Vision Document | 文档 | P0 | 描述项目目标、范围、成功标准的战略文档 |
| 01-项目启动 | Product Backlog | Product Backlog | 文档 | P0 | 按优先级排序的产品待办事项列表 |
| 01-项目启动 | 敏捷团队章程 | Agile Team Charter | 文档 | P0 | 定义团队角色、职责、工作方式的协议 |
| 01-项目启动 | Definition of Done | Definition of Done (DoD) | 文档 | P0 | 明确用户故事"完成"标准的检查清单 |
| 01-项目启动 | 工作协议 | Working Agreement | 文档 | P1 | 团队共同遵守的工作规则和约定 |
| 01-项目启动 | 技术栈决策 | Tech Stack Decision | 文档 | P1 | 技术选型和架构决策记录 |
| 01-项目启动 | 环境配置清单 | Environment Setup Checklist | 文档 | P1 | 开发、测试、生产环境配置要求 |
| 01-项目启动 | 风险登记表 | Risk Register | 文档 | P2 | 项目风险识别和应对策略 |
| 02-迭代规划 | Sprint Backlog | Sprint Backlog | 文档 | P0 | 当前迭代要完成的用户故事集合 |
| 02-迭代规划 | 迭代目标 | Sprint Goal | 文档 | P0 | 当前迭代要达成的核心目标 |
| 02-迭代规划 | 用户故事（细化） | Refined User Stories | 文档 | P0 | 符合INVEST原则的细化用户故事 |
| 02-迭代规划 | Story Point估算 | Story Point Estimation | 文档 | P0 | 用户故事复杂度估算结果 |
| 02-迭代规划 | 验收标准 | Acceptance Criteria | 文档 | P0 | 用户故事完成的验收条件 |
| 02-迭代规划 | 任务拆分 | Task Breakdown | 文档 | P1 | 用户故事拆分为具体任务 |
| 02-迭代规划 | 迭代计划 | Sprint Plan | 文档 | P1 | 迭代执行的详细计划 |
| 02-迭代规划 | 风险识别 | Sprint Risk Identification | 文档 | P2 | 当前迭代风险识别 |
| 03-迭代执行 | 任务看板 | Task Board | 可视化工具 | P0 | 任务状态跟踪看板 |
| 03-迭代执行 | 燃尽图 | Burndown Chart | 图表 | P0 | 迭代进度可视化 |
| 03-迭代执行 | 开发代码 | Development Code | 代码 | P0 | 功能实现代码 |
| 03-迭代执行 | 单元测试 | Unit Tests | 代码 | P0 | 单元测试代码 |
| 03-迭代执行 | 代码审查记录 | Code Review Records | 记录 | P1 | 审查意见和修改记录 |
| 03-迭代执行 | 每日站会纪要 | Daily Standup Minutes | 文档 | P2 | 站会要点记录 |
| 04-迭代评审 | 演示成果记录 | Demo Results | 文档 | P0 | 演示的功能清单和截图 |
| 04-迭代评审 | 迭代评审报告 | Sprint Review Report | 报告 | P0 | 评审结果总结 |
| 04-迭代评审 | 客户反馈记录 | Customer Feedback Log | 文档 | P0 | 收集的客户意见 |
| 04-迭代评审 | 验收确认记录 | Acceptance Confirmation | 文档 | P0 | 故事验收签字确认 |
| 05-迭代回顾 | 回顾报告 | Retrospective Report | 文档 | P0 | 迭代回顾会议记录和结论 |
| 05-迭代回顾 | 改进项列表 | Improvement Backlog | 文档 | P0 | 待改进项登记清单 |
| 05-迭代回顾 | Action Items | Action Items | 任务 | P0 | 具体改进措施和责任人 |
| 05-迭代回顾 | 团队满意度记录 | Team Happiness Record | 文档 | P1 | 团队情绪和满意度追踪 |
| 05-迭代回顾 | 度量数据报告 | Metrics Report | 文档 | P1 | 迭代度量数据汇总 |
| 05-迭代回顾 | 改进效果评估 | Improvement Evaluation | 文档 | P2 | 上迭代改进项效果评估 |
| 06-发布交付 | 发布包 | Release Package | 包 | P0 | 可部署的发布包 |
| 06-发布交付 | 发布说明 | Release Notes | 文档 | P0 | 版本变更说明 |
| 06-发布交付 | CI/CD流水线配置 | CI/CD Pipeline Config | 配置 | P0 | 自动化部署配置 |
| 06-发布交付 | 发布验收报告 | Release Acceptance Report | 报告 | P0 | 发布验证结果 |
| 06-发布交付 | 发布计划 | Release Plan | 文档 | P1 | 发布时间和内容 |
| 07-敏捷运维 | 监控告警配置 | Monitoring Alert Config | 配置 | P0 | 监控和告警规则 |
| 07-敏捷运维 | 快速响应记录 | Rapid Response Record | 文档 | P0 | 事件处理记录 |
| 07-敏捷运维 | DevOps实践记录 | DevOps Practice Log | 文档 | P1 | DevOps改进记录 |
| 07-敏捷运维 | 运维报告 | Operations Report | 报告 | P1 | 定期运维总结 |

_敏捷流程共计 41 项产出物_
