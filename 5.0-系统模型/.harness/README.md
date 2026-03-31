# Harness 工作流集成

将 Harness_Engineering 多 Agent 自主开发架构融入到系统模型开发中。

## 目录结构

```
.harness/
├── config/
│   ├── profiles/              # 场景配置
│   │   ├── erp-module-builder.yaml
│   │   └── mes-module-builder.yaml
│   └── tools/                 # 工具配置
│       ├── db_migrate.yaml
│       ├── api_test.yaml
│       └── README.md
├── engine/                    # 工作流引擎
│   ├── __init__.py
│   ├── main.py               # 主入口
│   ├── workflow_engine.py    # 工作流引擎
│   ├── phase_executor.py     # 阶段执行器
│   ├── context_manager.py    # 上下文管理
│   └── quality_gate.py       # 质量门控
├── runtime/                   # 运行时状态
└── templates/                 # 文档模板
    ├── spec-template.md
    ├── contract-template.md
    ├── progress-template.md
    └── feedback-template.md
```

## 快速开始

### 1. 运行工作流

```bash
# 进入引擎目录
cd .harness/engine

# 运行ERP模块开发工作流
python main.py run --workspace "../../erp/车企模型/.workspace" --profile erp-module-builder

# 运行MES模块开发工作流
python main.py run --workspace "../../mes/车企模型/.workspace" --profile mes-module-builder
```

### 2. 执行质量门控检查

```bash
# 执行所有质量门控检查
python main.py check --workspace "../../erp/车企模型"

# 执行单个门控检查
python main.py check --workspace "../../erp/车企模型" --gate prd_completeness
```

### 3. 查看可用Profile

```bash
python main.py list-profiles
```

## 工作流阶段

| 阶段 | 描述 | 输入 | 输出 |
|------|------|------|------|
| **Plan** | 需求分析与规划 | spec.md | PRD, UserStory, AcceptanceCriteria |
| **Contract** | 开发契约制定 | PRD | contract.md, 系统架构设计 |
| **Build** | 代码与文档生成 | contract.md, PRD | DB设计, API设计, 实体类, CRUD代码 |
| **Evaluate** | 测试与验证 | 代码, API设计 | 测试用例, feedback.md |
| **Iterate** | 迭代优化 | feedback.md | 更新代码, 更新文档 |

## Profile 配置

### erp-module-builder

适用于 ERP 系统模块开发，包含：
- 完整的 Plan -> Contract -> Build -> Evaluate -> Iterate 流程
- 多租户架构支持
- 质量门控检查

### mes-module-builder

适用于 MES 系统模块开发，扩展了：
- 设备集成（PLC通讯、扭矩枪、扫描枪）
- 追溯特性（VIN追踪、批次追踪）
- 实时数据采集

## 状态文件

| 文件 | 描述 |
|------|------|
| `spec.md` | 需求规格输入 |
| `contract.md` | 开发契约（交付物清单、质量门控） |
| `progress.md` | 进度跟踪（阶段状态、Token使用） |
| `feedback.md` | 反馈记录（问题、修复措施） |

## 质量门控

| 门控 | 描述 | 阶段 |
|------|------|------|
| `prd_completeness` | PRD完整性检查 | Plan |
| `user_story_coverage` | UserStory覆盖率 | Plan |
| `architecture_review` | 架构设计评审 | Contract |
| `sql_syntax_check` | SQL语法验证 | Build |
| `api_spec_validation` | API规范验证 | Build |
| `unit_test_coverage` | 单元测试覆盖率 | Evaluate |
| `integration_test_pass` | 集成测试通过 | Evaluate |
| `code_quality` | 代码质量评分 | Evaluate |

## Skill 扩展

新增的 Skill 位于 `1.0-软件开发流程角色agent模型/研发/skill/`:

| Skill | 描述 |
|-------|------|
| `db-designer` | 根据PRD生成数据库设计文档 |
| `api-designer` | 根据DB设计生成API设计文档 |
| `entity-generator` | 生成JPA/MyBatis实体类 |
| `crud-generator` | 生成CRUD代码脚手架 |

## 技术栈

- **后端**: Spring Boot 2.7 + MyBatis Plus 3.5
- **数据库**: MySQL 8.x
- **缓存**: Redis 6.x
- **消息队列**: RabbitMQ 3.x
- **工作流**: Flowable 6.8.x
- **前端**: Vue3 + Element Plus
- **移动端**: UniApp

## 参考文档

- [Harness_Engineering 原项目](../../../../basePlatform/Harness_Engineering/)
- [ERP系统需求总览](../erp/车企模型/00-ERP系统需求总览.md)
- [MES系统需求总览](../mes/车企模型/00-MES系统需求总览.md)