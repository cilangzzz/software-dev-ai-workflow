---
schema_version: 1.0
module_id: ERP-SD-01
module_name: 销售管理模块
system_type: ERP
status: draft
created_at: 2026-03-30
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
  # 默认路径（当环境变量未设置时使用）
  default_path: "H:/Documents/yudao-skill-pro"
---

# 需求规格

## 1. 模块概述
销售管理模块(Sales and Distribution, SD)是ERP系统的核心模块之一，负责管理客户信息、销售订单、定价策略、发货流程等业务。支持多租户SaaS模式，适用于汽车制造行业的经销商网络管理。

## 2. 功能需求清单
| 需求ID | 功能名称 | 描述 | 优先级 |
|--------|----------|------|--------|
| FN001 | 客户档案管理 | 客户信息的新增、修改、删除、查询 | P0 |
| FN002 | 客户等级管理 | A/B/C级客户分类，差异化服务 | P0 |
| FN003 | 信用额度管理 | 客户信用额度设置和使用控制 | P0 |
| FN004 | 销售订单管理 | 订单创建、修改、审批、关闭 | P0 |
| FN005 | 订单价格计算 | 支持价目表、折扣、促销组合 | P0 |
| FN006 | 发货管理 | 发货单创建、拣货、出库 | P1 |
| FN007 | 销售退货 | 退货申请、审批、入库 | P1 |
| FN008 | 销售统计 | 销售额、销量、毛利统计报表 | P1 |
| FN009 | 客户对账 | 应收账款查询、对账单生成 | P1 |
| FN010 | 多级经销商管理 | 4S店、二级经销商网络管理 | P2 |

## 3. 非功能需求
- **性能要求**: 列表查询响应时间 < 2s，并发用户数 >= 100
- **安全要求**: 客户敏感信息加密存储，操作日志审计
- **可用性要求**: 99.9%可用性，故障恢复时间 < 30min

## 4. 验收标准引用
参考：产品/AcceptanceCriteria/AC-01-销售管理模块.md

## 5. 依赖关系
### 上游模块
- 系统管理模块(SYS): 用户、权限、组织架构
- 基础数据模块(MD): 物料主数据、客商主数据

### 下游模块
- 库存管理模块(WM): 发货扣减库存
- 应收管理模块(FI-AR): 生成应收账款
- 生产计划模块(PP): 销售预测驱动生产

## 6. 数据约束

> **重要**：数据约束以 yudao-skill-pro 基础架构规范为准。
> 详细规范见 references 中指定的 db-designer.yaml 和 entity-designer.yaml。

### 6.1 必需字段（详见 db-designer.yaml）
- `id` - BIGINT, 主键
- `tenant_id` - BIGINT, 租户编号（位于 id 之后）
- `creator` - VARCHAR(64), 创建者
- `create_time` - DATETIME, 创建时间
- `updater` - VARCHAR(64), 更新者
- `update_time` - DATETIME, 更新时间
- `deleted` - BIT(1), 逻辑删除

### 6.2 索引规范（详见 db-designer.yaml）
- 所有索引必须包含 `tenant_id` 作为第一列
- 唯一索引必须包含 `deleted` 字段

### 6.3 实体继承（详见 entity-designer.yaml）
- 多租户业务表：继承 `TenantBaseDO`

### 6.4 业务特定约束
- VIN码预分配：订单创建时可预分配车辆VIN码（17位，符合ISO3779标准）