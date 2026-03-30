# Harness 工具配置说明

本目录包含 Harness 工作流扩展工具的配置定义。

## 可用工具

### db_migrate

数据库迁移管理工具，用于：
- 根据 DB 设计文档生成 Flyway/Liquibase 迁移脚本
- 验证 SQL 语法和表关系
- 执行数据库迁移和回滚

**使用示例**:
```bash
# 生成迁移脚本
harness tool db_migrate --action generate --db_design_file 研发/数据库设计/DB-01-销售管理模块.md

# 验证 SQL
harness tool db_migrate --action validate --db_design_file 研发/数据库设计/DB-01-销售管理模块.md
```

### api_test

API 接口测试工具，用于：
- 根据 API 设计文档生成 Postman Collection
- 执行接口自动化测试
- 验证 OpenAPI 规范完整性

**使用示例**:
```bash
# 生成 Postman Collection
harness tool api_test --action generate_collection --api_design_file 研发/API设计/API-01-销售管理模块.md

# 执行测试
harness tool api_test --action run_test --base_url http://localhost:8080

# 验证 OpenAPI 规范
harness tool api_test --action validate_spec --openapi_spec 研发/API设计/openapi/sd.yaml
```

## 工具配置结构

每个工具配置文件包含以下部分：

| 配置项 | 描述 |
|--------|------|
| schema | OpenAI Function Calling Schema 定义 |
| execution_flow | 执行流程步骤定义 |
| output_format | 输出格式定义 |
| error_handling | 错误处理配置 |

## 扩展新工具

要添加新工具，请：

1. 创建 `{tool_name}.yaml` 配置文件
2. 定义 OpenAI Function Calling Schema
3. 定义执行流程
4. 定义输出格式和错误处理
5. 在 Profile 配置中引用新工具