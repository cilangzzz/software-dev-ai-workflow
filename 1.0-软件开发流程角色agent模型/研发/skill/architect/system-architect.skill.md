# 系统架构设计

## 基本信息

- **ID**: system-architect
- **名称**: 系统架构设计
- **版本**: 2.0.0
- **分类**: design
- **部门**: 研发部
- **描述**: 专业系统架构设计工具，采用C4模型分层架构、TOGAF方法论，输出完整的架构设计文档和ADR决策记录。支持微服务、单体、混合架构类型。


## 触发条件


### commands

- /architect
- /架构设计
- /system-architect

### keywords

- 架构设计
- 系统架构
- 技术架构
- 设计架构
- 架构方案

### patterns

- 帮我设计.*架构
- 系统.*架构方案
- 技术架构.*设计

## 输入参数


### parameters


- **name**: prd_document
- **type**: string
- **required**: True
- **description**: PRD文档路径或内容
- **validation**: - **min_length**: 50
- **examples**: - 产品/产出物/订单系统/需求阶段/PRD-订单模块.md

- **name**: tech_constraints
- **type**: object
- **required**: False
- **default**: 
- **description**: 技术约束条件
- **properties**: - **existing_stack**: 现有技术栈（需兼容的系统）
- **compliance**: 合规要求（如数据安全、审计）
- **budget**: 预算限制
- **team_skills**: 团队技术能力

- **name**: architecture_type
- **type**: string
- **required**: False
- **default**: auto
- **enum**: - auto
- microservice
- monolithic
- hybrid
- modular-monolith
- **description**: 架构类型选择

- **name**: diagram_format
- **type**: string
- **required**: False
- **default**: c4
- **enum**: - c4
- uml
- drawio
- mermaid
- **description**: 架构图输出格式

## 工作流程

- **description**: C4模型分层架构设计流程，确保架构可追溯、可演进

### phases


- **name**: 需求理解
- **description**: 理解业务需求和约束条件
- **duration**: 10-15分钟
- **steps**: 
- **step**: PRD解析
- **action**: 提取功能需求、性能需求、约束条件
- **output**: 需求摘要

- **step**: 约束分析
- **action**: 分析技术、业务、组织约束
- **output**: 约束清单

- **step**: 架构目标定义
- **action**: 定义架构目标和质量属性
- **reference**: ISO 25010质量模型

- **name**: 架构决策
- **description**: 做出关键架构决策并记录
- **duration**: 20-40分钟
- **steps**: 
- **step**: 架构风格选择
- **action**: 评估并选择架构风格
- **method**: 架构风格评估矩阵
- **criteria**: 可扩展性、可维护性、性能、成本

- **step**: 技术选型
- **action**: 选择技术栈和框架
- **method**: 技术雷达评估
- **reference**: tech-selector.yaml
- **output**: 技术栈清单

- **step**: ADR编写
- **action**: 编写架构决策记录
- **template**: adr-template
- **output**: ADR文档集

- **step**: 风险评估
- **action**: 识别架构风险和缓解措施
- **output**: 风险评估矩阵

- **name**: 架构设计
- **description**: 使用C4模型进行分层设计
- **duration**: 30-60分钟
- **steps**: 
- **step**: Context层设计
- **action**: 设计系统上下文图（Level 1）
- **description**: 展示系统与外部世界的交互
- **output**: System Context Diagram

- **step**: Container层设计
- **action**: 设计容器图（Level 2）
- **description**: 展示应用容器（服务、数据库等）
- **output**: Container Diagram

- **step**: Component层设计
- **action**: 设计组件图（Level 3）
- **description**: 展示容器内部的组件结构
- **output**: Component Diagram

- **step**: Code层设计（可选）
- **action**: 设计代码结构图（Level 4）
- **description**: 展示关键代码结构
- **condition**: 复杂核心模块需要

- **name**: 架构验证
- **description**: 验证架构满足需求
- **duration**: 15-20分钟
- **steps**: 
- **step**: 质量属性验证
- **action**: 验证架构满足性能、安全等质量属性
- **checklist**: 质量属性检查清单

- **step**: 约束满足验证
- **action**: 验证架构满足技术约束
- **output**: 约束满足矩阵

- **step**: 成本估算
- **action**: 估算架构实施成本
- **output**: 成本估算报告

## 输出产物

- **base_path**: 研发/产出物/{project_name}/设计阶段/

### required


- **name**: 架构设计文档
- **files**: - 架构设计文档-{system_name}.md
- **format**: markdown
- **description**: 完整的架构设计文档
- **quality_check**: C4模型Level 1-3完整

- **name**: C4架构图
- **files**: - 架构图/System-Context.drawio
- 架构图/Container.drawio
- 架构图/Component.drawio
- **format**: drawio
- **description**: C4模型分层架构图
- **quality_check**: Context/Container/Component完整

- **name**: ADR决策记录
- **files**: - ADR/ADR-{number}-{title}.md
- **format**: markdown
- **description**: 架构决策记录
- **quality_check**: 关键决策100%覆盖

- **name**: 技术栈清单
- **files**: - 技术选型-{system_name}.md
- **format**: markdown
- **description**: 技术栈选型清单
- **quality_check**: 每项技术有选择理由

### conditional


- **name**: 风险评估矩阵
- **files**: - 风险评估-{system_name}.xlsx
- **format**: excel
- **description**: 架构风险识别和缓解措施
- **condition**: 大型项目或高风险项目
- **condition_detail**: 项目周期>3个月 或 团队>5人 或 涉及敏感数据

- **name**: C4 Level 4代码图
- **files**: - 架构图/Code-Structure.drawio
- **format**: drawio
- **description**: 核心模块代码结构图
- **condition**: 核心复杂模块
- **condition_detail**: 核心业务逻辑复杂度>阈值

- **name**: 成本估算报告
- **files**: - 成本估算-{system_name}.md
- **format**: markdown
- **description**: 架构实施成本估算
- **condition**: 大型项目
- **condition_detail**: 需要预算审批的项目

## templates

- **architecture_doc_template**: 
```
# 系统架构设计文档

## 文档信息
| 系统名称 | {system_name} |
| 文档编号 | ARCH-{number} |
| 版本 | v1.0 |
| 创建日期 | {date} |
| 架构师 | {architect} |
| 状态 | 草稿/评审中/已批准 |

---

## 1. 架构概述
### 1.1 系统定位
{系统在整体业务中的定位}

### 1.2 架构目标
| 目标类型 | 目标描述 | 衡量指标 | 优先级 |
| 功能性 | {goal} | {metric} | {priority} |
| 性能 | {goal} | {metric} | {priority} |
| 可扩展性 | {goal} | {metric} | {priority} |

---

## 2. C4架构设计
### 2.1 Level 1: System Context
![System Context Diagram](架构图/System-Context.drawio)

### 2.2 Level 2: Container
![Container Diagram](架构图/Container.drawio)

### 2.3 Level 3: Component
![Component Diagram](架构图/Component.drawio)

---

## 3. 技术选型
| 层级 | 技术选择 | 版本 | 选择理由 | ADR编号 |
| 前端 | {tech} | {version} | {reason} | ADR-001 |
| 后端 | {tech} | {version} | {reason} | ADR-002 |

```

- **adr_template**: 
```
# ADR-{编号}: {决策标题}

## 元信息
| 状态 | {提议/已接受/已废弃/已替代} |
| 创建日期 | {date} |
| 决策者 | {decider} |
| 影响范围 | {scope} |

---

## 背景
{描述导致此决策的背景和问题}

## 决策
{描述所做的决策及其理由}

## 考虑的方案
### 方案1: {方案名称}
- **优点**: {优点列表}
- **缺点**: {缺点列表}

## 后果
- 正面影响: {正面影响}
- 负面影响: {负面影响}

```


## 检查清单


### before_design


- **item**: PRD已评审通过
- **check**: 确认PRD状态为已批准

- **item**: 约束条件已明确
- **check**: 检查tech_constraints参数

- **item**: 现有系统架构已了解
- **check**: 读取现有架构文档（如有）

### during_design


- **item**: 架构风格已评估
- **check**: 完成架构风格评估矩阵

- **item**: ADR已编写
- **check**: 每个关键决策都有ADR记录

- **item**: C4模型四层完整
- **check**: Context/Container/Component图完整

- **item**: 技术选型有理由
- **check**: 每项技术都有选择理由

### after_design


- **item**: 质量属性满足需求
- **check**: 质量属性验证矩阵

- **item**: 约束条件已满足
- **check**: 约束满足矩阵

- **item**: 风险评估完整
- **check**: 风险识别和缓解措施

- **item**: 文档结构完整
- **check**: 检查所有章节已填写

- **item**: 架构评审通过
- **check**: 技术评审会议

## 质量标准


- **standard**: ADR覆盖率
- **requirement**: 关键决策100%有ADR
- **check**: 统计关键决策数 vs ADR数

- **standard**: C4模型完整性
- **requirement**: Level 1-3 100%完整
- **check**: 检查Context/Container/Component图

- **standard**: 质量属性验证
- **requirement**: 所有质量属性有验证方案
- **check**: 质量属性验证矩阵

- **standard**: 技术选型合理性
- **requirement**: 技术雷达评估通过
- **check**: 每项技术有评估记录

## 协作关系


### upstream


- **skill**: requirement-analyzer
- **relationship**: 提供PRD文档
- **condition**: 需求分析完成后

### downstream


- **skill**: module-designer
- **relationship**: 提供架构设计
- **condition**: 架构设计完成后

- **skill**: api-designer
- **relationship**: 提供组件结构
- **condition**: Container层设计后

- **skill**: scaffold
- **relationship**: 提供项目结构
- **condition**: 架构设计完成后

- **skill**: code-implement
- **relationship**: 提供架构指导
- **condition**: 开发阶段

## 参考文档


### methodology


- **name**: C4模型
- **description**: Context-Container-Component-Code分层架构模型
- **url**: https://c4model.com/

- **name**: TOGAF
- **description**: 企业架构框架

- **name**: ADR
- **description**: 架构决策记录
- **url**: https://adr.github.io/

- **name**: ISO 25010
- **description**: 软件产品质量模型

### primary


- **path**: 研发/common/架构设计/adr.md
- **description**: ADR编写指南

- **path**: 研发/tech-selector.yaml
- **description**: 技术选型配置

## metadata

- **created_at**: 2026-06-11
- **updated_at**: 2026-06-11
- **author**: Claude Agent

### version_history


- **version**: 1.0.0
- **date**: 2026-03-20
- **changes**: 初始版本

- **version**: 2.0.0
- **date**: 2026-06-11
- **changes**: 重构为Skill技能定义格式，增加条件产出物