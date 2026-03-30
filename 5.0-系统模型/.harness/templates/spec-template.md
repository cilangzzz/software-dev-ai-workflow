---
schema_version: 1.0
module_id: {MODULE_ID}
module_name: {MODULE_NAME}
system_type: {ERP/MES}
status: draft
created_at: {DATE}
---

# 需求规格

## 1. 模块概述
{模块描述}

## 2. 功能需求清单
| 需求ID | 功能名称 | 描述 | 优先级 |
|--------|----------|------|--------|
| FN001 | | | P0 |
| FN002 | | | P1 |

## 3. 非功能需求
- **性能要求**: 响应时间 < 2s，并发用户数 >= 100
- **安全要求**: 敏感数据加密存储，操作日志审计
- **可用性要求**: 99.9%可用性，故障恢复时间 < 30min

## 4. 验收标准引用
参考：产品/AcceptanceCriteria/AC-{module}.md

## 5. 依赖关系
### 上游模块
- {上游模块列表}

### 下游模块
- {下游模块列表}

## 6. 数据约束
- 多租户支持：所有业务表包含 tenant_id
- 审计字段：created_by, created_time, updated_by, updated_time
- 逻辑删除：deleted 字段 (0-未删除, 1-已删除)