---
schema_version: 1.0
module_id: ERP-SD-01
contract_date: 2026-03-30
estimated_effort: 40h
quality_threshold: 7.0
iteration_limit: 3
# 动态引用基础架构规范（以 yudao-skill-pro 为准）
# 基础路径通过环境变量 YUDAO_SKILL_PRO_PATH 或用户输入指定
references:
  design:
    - "${YUDAO_SKILL_PRO_PATH}/skills/design/db-designer.yaml"
    - "${YUDAO_SKILL_PRO_PATH}/skills/design/entity-designer.yaml"
    - "${YUDAO_SKILL_PRO_PATH}/skills/design/api-designer.yaml"
    - "${YUDAO_SKILL_PRO_PATH}/skills/design/crud-designer.yaml"
  module_guide:
    - "${YUDAO_SKILL_PRO_PATH}/skills/modules/erp/skill-erp.yaml"
  default_path: "H:/Documents/yudao-skill-pro"
---

# 开发契约

## 1. 交付物清单
| 序号 | 交付物 | 路径 | 状态 | 负责Skill |
|------|--------|------|------|-----------|
| 1 | PRD文档 | 产品/PRD/PRD-01-销售管理模块.md | pending | requirement-analyzer |
| 2 | UserStory | 产品/UserStory/UserStory-01-销售管理模块.md | pending | user-story-generator |
| 3 | 验收标准 | 产品/AcceptanceCriteria/AC-01-销售管理模块.md | pending | acceptance-criteria-writer |
| 4 | 系统架构 | 研发/系统架构设计.md | pending | architect |
| 5 | 数据库设计 | 研发/数据库设计/DB-01-销售管理模块.md | pending | db-designer |
| 6 | API设计 | 研发/API设计/API-01-销售管理模块.md | pending | api-designer |
| 7 | 详细设计 | 研发/详细设计/Detail-01-销售管理模块.md | pending | implement |
| 8 | 实体类 | 代码/backend/src/main/java/**/entity/*.java | pending | entity-generator |
| 9 | CRUD代码 | 代码/backend/src/main/java/**/{controller,service,mapper}/ | pending | crud-generator |
| 10 | 测试代码 | 代码/tests/ | pending | test-case-generator |

## 2. 质量门控
| 门控项 | 标准 | 检查方式 | 阶段 |
|--------|------|----------|------|
| PRD完整性 | 包含功能概述、用户角色、功能清单、业务流程 | doc_validator | plan |
| UserStory覆盖率 | >= 80%功能覆盖 | doc_validator | plan |
| 架构评审通过 | 架构图、技术选型、模块划分完整 | architecture_review | contract |
| SQL语法正确 | DDL语句语法验证通过 | db_migrate.validate | build |
| API规范验证 | 符合OpenAPI 3.0标准 | api_test.validate_spec | build |
| 单元测试覆盖率 | >= 80% | test_executor | evaluate |
| 集成测试通过 | 所有接口测试通过 | api_test.run_test | evaluate |

## 3. 技术约束

> **重要**：以下技术约束以 yudao-skill-pro 基础架构规范为准。
> 启动工作流前必须先读取 references 中指定的规范文件，确保生成的代码符合项目标准。

### 3.1 核心规范文件（必须先读取）
| 规范文件 | 约束内容 |
|----------|----------|
| db-designer.yaml | 数据库表设计、必需字段、索引规范、命名规范 |
| entity-designer.yaml | 实体类继承体系、注解规范、类型映射 |
| api-designer.yaml | URL命名、HTTP方法、权限标识、响应格式 |
| crud-designer.yaml | CRUD代码生成规范 |
| skill-erp.yaml | ERP模块业务逻辑、领域模型、代码模式 |

### 3.2 关键约束摘要（详细规范见上述文件）

#### 数据库设计约束
- 必需字段：`id`, `tenant_id`, `creator`, `create_time`, `updater`, `update_time`, `deleted`
- `deleted` 类型：`BIT(1)`（非 TINYINT）
- 索引规范：所有索引必须包含 `tenant_id` 作为第一列

#### 实体类约束
- 多租户业务表：继承 `TenantBaseDO`
- 单租户业务表：继承 `BaseDO`
- 注解：`@TableName(autoResultMap = true)`, `@EqualsAndHashCode(callSuper = true)`

#### API 设计约束
- URL格式：`/{模块}/{功能}/{操作}`（操作式 URL，非标准 RESTful）
- 权限标识：`{模块}:{功能}:{操作}`
- 响应格式：`CommonResult<T>`

### 3.3 技术栈
- 后端框架: Spring Boot 2.7 + MyBatis Plus 3.5
- 数据库: MySQL 8.x
- 缓存: Redis 6.x
- 消息队列: RabbitMQ 3.x
- 工作流: Flowable 6.8.x
- 前端: Vue3 + Element Plus
- 移动端: UniApp

## 4. 时间约束
| 阶段 | 预计时长 | 开始时间 | 截止时间 |
|------|----------|----------|----------|
| plan | 2h | - | - |
| contract | 1h | - | - |
| build | 4h | - | - |
| evaluate | 2h | - | - |
| iterate | 2h/轮 | - | - |

## 5. 风险识别
| 风险ID | 风险描述 | 影响程度 | 应对措施 |
|--------|----------|----------|----------|
| R001 | 多租户数据隔离不彻底 | 高 | 所有查询强制添加tenant_id条件 |
| R002 | 信用额度并发超卖 | 中 | 使用Redis分布式锁 |
| R003 | 订单价格计算复杂 | 中 | 独立定价引擎模块 |