# 系统架构设计专家

## 基本信息

- **ID**: architect-v2
- **名称**: 系统架构设计专家
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

### artifacts


- **name**: 架构设计文档
- **files**: - 架构设计文档-{system_name}.md
- **format**: markdown
- **description**: 完整的架构设计文档
- **required**: True

- **name**: C4架构图
- **files**: - 架构图/System-Context.drawio
- 架构图/Container.drawio
- 架构图/Component.drawio
- **format**: drawio
- **description**: C4模型分层架构图
- **required**: True

- **name**: ADR决策记录
- **files**: - ADR/ADR-{number}-{title}.md
- **format**: markdown
- **description**: 架构决策记录
- **required**: True

- **name**: 技术栈清单
- **files**: - 技术选型-{system_name}.md
- **format**: markdown
- **description**: 技术栈选型清单
- **required**: True

- **name**: 风险评估矩阵
- **files**: - 风险评估-{system_name}.xlsx
- **format**: excel
- **description**: 架构风险识别和缓解措施
- **required**: False

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
| 可维护性 | {goal} | {metric} | {priority} |
| 安全性 | {goal} | {metric} | {priority} |

### 1.3 架构原则
- **原则1**: {原则名称} - {原则描述}
- **原则2**: {原则名称} - {原则描述}

---

## 2. 约束条件
### 2.1 技术约束
| 约束类型 | 约束描述 | 影响范围 | 满足方案 |
| 现有系统 | {constraint} | {scope} | {solution} |
| 技术栈 | {constraint} | {scope} | {solution} |

### 2.2 业务约束
| 约束类型 | 约束描述 | 影响范围 |
| 时间约束 | {constraint} | {scope} |
| 成本约束 | {constraint} | {scope} |

### 2.3 组织约束
| 约束类型 | 约束描述 | 影响范围 |
| 团队规模 | {constraint} | {scope} |
| 技术能力 | {constraint} | {scope} |

---

## 3. 架构风格选择
### 3.1 评估矩阵
| 架构风格 | 可扩展性 | 可维护性 | 性能 | 成本 | 综合 | 推荐 |
| 微服务 | ★★★★ | ★★★ | ★★★★ | ★★ | {score} | ✓/✗ |
| 单体 | ★★ | ★★★★ | ★★★★ | ★★★★ | {score} | ✓/✗ |
| 模块化单体 | ★★★ | ★★★★ | ★★★★ | ★★★ | {score} | ✓/✗ |

### 3.2 选择理由
{选择的架构风格及其理由}

---

## 4. C4架构设计
### 4.1 Level 1: System Context (系统上下文)
**描述**: {系统与外部世界的交互}

![System Context Diagram](架构图/System-Context.drawio)

| 外部实体 | 类型 | 交互方式 | 说明 |
| {entity} | 用户/系统 | {interaction} | {note} |

### 4.2 Level 2: Container (容器)
**描述**: {系统内部的高层结构}

![Container Diagram](架构图/Container.drawio)

| 容器名称 | 类型 | 技术栈 | 职责 | 通信方式 |
| {container} | 应用/数据库 | {tech} | {role} | {comm} |

### 4.3 Level 3: Component (组件)
**描述**: {容器内部的组件结构}

![Component Diagram](架构图/Component.drawio)

| 组件名称 | 所属容器 | 职责 | 接口 | 依赖 |
| {component} | {container} | {role} | {api} | {deps} |

### 4.4 Level 4: Code (代码结构) - 可选
{关键模块的代码结构设计}

---

## 5. 技术选型
### 5.1 技术栈清单
| 层级 | 技术选择 | 版本 | 选择理由 | ADR编号 |
| 前端 | {tech} | {version} | {reason} | ADR-001 |
| 后端 | {tech} | {version} | {reason} | ADR-002 |
| 数据库 | {tech} | {version} | {reason} | ADR-003 |
| 缓存 | {tech} | {version} | {reason} | ADR-004 |
| 消息队列 | {tech} | {version} | {reason} | ADR-005 |
| 容器化 | {tech} | {version} | {reason} | ADR-006 |

### 5.2 技术雷达评估
| 技术 | 状态 | 成熟度 | 团队熟悉度 | 建议 |
| {tech} | 采用/试验/评估/暂缓 | {level} | {level} | {advice} |

---

## 6. 质量属性设计
### 6.1 性能设计
| 性能指标 | 目标值 | 设计方案 | 验证方法 |
| 响应时间 | < {n}ms | {solution} | {method} |
| 吞吐量 | ≥ {n} TPS | {solution} | {method} |
| 并发用户 | ≥ {n} | {solution} | {method} |

### 6.2 可扩展性设计
- **水平扩展**: {扩展方案}
- **垂直扩展**: {扩展方案}
- **弹性伸缩**: {伸缩方案}

### 6.3 安全设计
| 安全领域 | 安全措施 | 实现方式 |
| 认证 | {measure} | {implementation} |
| 授权 | {measure} | {implementation} |
| 数据安全 | {measure} | {implementation} |
| API安全 | {measure} | {implementation} |

### 6.4 可观测性设计
- **日志**: {日志方案}
- **监控**: {监控方案}
- **追踪**: {追踪方案}
- **告警**: {告警方案}

---

## 7. 数据架构
### 7.1 数据模型
{数据模型设计概述}

### 7.2 数据流转
{数据流转图和说明}

### 7.3 数据存储策略
| 数据类型 | 存储方案 | 访问模式 | 备份策略 |
| {type} | {solution} | {pattern} | {backup} |

---

## 8. 部署架构
### 8.1 部署拓扑
{部署拓扑图和说明}

### 8.2 环境规划
| 环境 | 用途 | 配置 | 部署策略 |
| 开发 | {purpose} | {config} | {strategy} |
| 测试 | {purpose} | {config} | {strategy} |
| 生产 | {purpose} | {config} | {strategy} |

---

## 9. 风险评估
| 风险编号 | 风险描述 | 影响程度 | 发生概率 | 缓解措施 | 负责人 |
| R-001 | {risk} | 高/中/低 | 高/中/低 | {mitigation} | {owner} |

---

## 10. 实施计划
### 10.1 里程碑
| 里程碑 | 目标 | 时间 | 交付物 |
| {milestone} | {goal} | {date} | {deliverables} |

### 10.2 资源需求
| 资源类型 | 数量 | 说明 |
| 人员 | {count} | {note} |
| 设备 | {count} | {note} |
| 预算 | {amount} | {note} |

---

## 附录
### A. ADR索引
| ADR编号 | 标题 | 状态 |
| ADR-001 | {title} | 已接受 |

### B. 参考资料
- {参考文档链接}

### C. 术语表
| 术语 | 定义 |
| {term} | {definition} |

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

### 问题陈述
{清晰陈述需要解决的问题}

### 约束条件
- 约束1: {约束描述}
- 约束2: {约束描述}

---

## 决策
{描述所做的决策及其理由}

### 决策内容
{具体的决策内容}

### 决策理由
1. 理由1: {理由描述}
2. 理由2: {理由描述}

---

## 考虑的方案

### 方案1: {方案名称}
- **描述**: {方案描述}
- **优点**: {优点列表}
- **缺点**: {缺点列表}
- **评分**: {评分}

### 方案2: {方案名称}
- **描述**: {方案描述}
- **优点**: {优点列表}
- **缺点**: {缺点列表}
- **评分**: {评分}

### 方案对比
| 维度 | 方案1 | 方案2 | 方案3 |
| 性能 | {score} | {score} | {score} |
| 成本 | {score} | {score} | {score} |
| 复杂度 | {score} | {score} | {score} |

---

## 后果
### 正面影响
- {正面影响描述}

### 负面影响
- {负面影响描述}

### 风险
- {风险描述}

---

## 实施计划
| 步骤 | 描述 | 时间 | 负责人 |
| 1 | {desc} | {time} | {owner} |

---

## 相关ADR
- 上游决策: ADR-{number}
- 下游影响: ADR-{number}

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


- **path**: 研发/references/架构设计/adr.md
- **description**: ADR编写指南

- **path**: 研发/references/架构设计/c4-guide.md
- **description**: C4模型使用指南

- **path**: 研发/tech-selector.yaml
- **description**: 技术选型配置

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

- **skill**: implement
- **relationship**: 提供架构指导
- **condition**: 开发阶段

## 使用示例


- **name**: 电商订单系统架构设计
- **input_summary**: PRD: 订单系统需支持高并发、分布式事务、实时状态更新
- **output_summary**: 
```
## 架构风格
选择: 微服务架构
理由: 业务复杂度高、需要独立扩展、团队规模支持

## ADR-001: 选择微服务架构
状态: 已接受
理由:
- 订单、支付、库存需要独立扩展
- 团队有微服务经验
- 预期并发量需要分布式部署

## C4架构图
Level 1 Context:
- 用户 -> 订单系统
- 支付系统 -> 订单系统
- 库存系统 -> 订单系统

Level 2 Container:
- 订单服务 (Spring Boot)
- 订单数据库 (MySQL)
- 订单缓存 (Redis)
- 消息队列 (RocketMQ)
- API网关 (Spring Cloud Gateway)

Level 3 Component:
订单服务内部:
- OrderController
- OrderService
- OrderRepository
- PaymentClient
- InventoryClient
- MessagePublisher

## 技术栈
| 层级 | 技术 | 版本 | ADR |
| 后端 | Spring Boot | 3.2 | ADR-002 |
| 数据库 | MySQL | 8.0 | ADR-003 |
| 缓存 | Redis | 7.0 | ADR-004 |
| 消息队列 | RocketMQ | 5.0 | ADR-005 |

## 风险评估
| 风险 | 影响 | 缓解措施 |
| 分布式事务复杂性 | 高 | 使用Seata框架 |
| 服务调用延迟 | 中 | Redis缓存热点数据 |

```


## 注意事项

- 架构设计需技术评审通过后方可实施
- ADR是架构演进的关键，必须持续维护
- C4模型第四层(Code)仅在复杂核心模块需要
- 技术选型需考虑团队熟悉度和运维成本
- 架构设计需与需求变更同步更新
- 风险评估需定期更新

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
- **changes**: 基于C4模型、TOGAF、ADR最佳实践重构