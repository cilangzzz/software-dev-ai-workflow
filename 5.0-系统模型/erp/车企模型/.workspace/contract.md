---
schema_version: 1.0
module_id: ERP-SD-01
contract_date: 2026-03-30
estimated_effort: 40h
quality_threshold: 7.0
iteration_limit: 3
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
### 技术栈
- 后端框架: Spring Boot 2.7 + MyBatis Plus 3.5
- 数据库: MySQL 8.x
- 缓存: Redis 6.x
- 消息队列: RabbitMQ 3.x
- 工作流: Flowable 6.8.x
- 前端: Vue3 + Element Plus
- 移动端: UniApp

### 架构约束
- 多租户: 共享数据库，tenant_id逻辑隔离
- 认证: JWT Token (Bearer)
- API风格: RESTful
- 响应格式: 统一JSON格式 {code, message, data, timestamp}

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