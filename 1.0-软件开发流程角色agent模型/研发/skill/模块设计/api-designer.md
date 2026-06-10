# Skill: api-designer

## 基本信息
- **名称**: api-designer
- **版本**: 1.0.0
- **所属部门**: 研发部
- **优先级**: P0

## 功能描述
根据模块设计文档自动生成RESTful API接口设计文档，包括接口定义、请求/响应结构、错误码定义、接口示例等。支持OpenAPI/Swagger规范输出。

## 触发条件
- 命令触发: `/api-designer`
- 自然语言触发:
  - "设计API接口"
  - "生成接口文档"
  - "创建API设计"
  - "生成OpenAPI文档"

## 输入参数
| 参数名 | 类型 | 必填 | 描述 |
|--------|------|------|------|
| module_doc | string | 是 | 模块设计文档路径或内容 |
| api_version | string | 否 | API版本号，默认v1 |
| base_path | string | 否 | API基础路径，如/api/v1 |
| output_format | string | 否 | 输出格式：markdown/openapi |

## 执行流程
1. **模块解析** - 解析模块设计文档
2. **实体识别** - 识别核心实体和操作
3. **接口设计** - 设计RESTful接口
4. **请求结构** - 定义请求参数和DTO
5. **响应结构** - 定义响应结构和VO
6. **错误码定义** - 定义错误码和错误信息
7. **示例生成** - 生成请求/响应示例
8. **文档输出** - 输出API设计文档

## RESTful设计原则

| HTTP方法 | 操作 | 示例路径 | 说明 |
|----------|------|----------|------|
| GET | 查询 | /api/orders | 获取列表 |
| GET | 查询 | /api/orders/{id} | 获取详情 |
| POST | 创建 | /api/orders | 创建资源 |
| PUT | 更新 | /api/orders/{id} | 全量更新 |
| PATCH | 更新 | /api/orders/{id} | 部分更新 |
| DELETE | 删除 | /api/orders/{id} | 删除资源 |

## 输出格式

### API设计文档（Markdown格式）
```markdown
# API接口设计文档

## 1. 接口概述

| 项目 | 内容 |
|------|------|
| 模块名称 | {模块名} |
| API版本 | v1 |
| 基硎路径 | /api/v1/{module} |
| 接口总数 | {数量} |

## 2. 通用说明

### 2.1 请求头
| Header | 必填 | 说明 |
|--------|------|------|
| Authorization | 是 | Bearer {token} |
| Content-Type | 是 | application/json |
| X-Tenant-Id | 是 | 租户ID |

### 2.2 响应结构
```json
{
  "code": 0,
  "message": "success",
  "data": {}
}
```

### 2.3 分页参数
| 参数 | 类型 | 说明 |
|------|------|------|
| pageNo | int | 页码，从1开始 |
| pageSize | int | 每页数量，默认20 |

## 3. 接口详细定义

### 3.1 {接口名称}

**接口说明**: {描述}

| 属性 | 内容 |
|------|------|
| 接口路径 | {method} {path} |
| 接口说明 | {说明} |
| 权限标识 | {permission} |

**请求参数**:
| 参数名 | 类型 | 必填 | 说明 |
|--------|------|------|------|
| {param} | {type} | 是/否 | {说明} |

**请求示例**:
```json
{
  "field": "value"
}
```

**响应结构**:
| 字段名 | 类型 | 说明 |
|--------|------|------|
| {field} | {type} | {说明} |

**响应示例**:
```json
{
  "code": 0,
  "message": "success",
  "data": {
    "id": 1
  }
}
```

## 4. 数据模型

### 4.1 请求DTO

#### {DTO名称}
| 字段名 | 类型 | 必填 | 校验 | 说明 |
|--------|------|------|------|------|
| {field} | {type} | 是 | @NotBlank | {说明} |

### 4.2 响应VO

#### {VO名称}
| 字段名 | 类型 | 说明 |
|--------|------|------|
| {field} | {type} | {说明} |

## 5. 错误码定义

| 错误码 | 错误信息 | 说明 |
|--------|----------|------|
| 0 | success | 成功 |
| {code} | {message} | {说明} |

## 6. 接口调用示例

### 6.1 curl示例
```bash
curl -X POST '{url}' \
  -H 'Authorization: Bearer {token}' \
  -H 'Content-Type: application/json' \
  -d '{body}'
```
```

## 质量标准
- RESTful规范符合度 100%
- 接口命名一致性 ≥ 95%
- 错误码覆盖度 ≥ 90%
- 请求/响应示例完整性 100%

## 使用示例

### 示例：设计工单管理API

**输入**:
```
模块：生产工单管理
实体：MesWorkOrder
操作：创建、修改、删除、查询、下发、开始、完成、关闭
```

**输出**:
```markdown
# 生产工单管理API接口设计文档

## 1. 接口概述

| 项目 | 内容 |
|------|------|
| 模块名称 | 生产工单管理 |
| API版本 | v1 |
| 基础路径 | /mes/work-order |
| 接口总数 | 9 |

## 2. 通用说明

### 2.1 请求头
| Header | 必填 | 说明 |
|--------|------|------|
| Authorization | 是 | Bearer {token} |
| Content-Type | 是 | application/json |
| X-Tenant-Id | 是 | 租户ID |

### 2.2 响应结构
```json
{
  "code": 0,
  "message": "success",
  "data": {}
}
```

### 2.3 分页参数
| 参数 | 类型 | 说明 |
|------|------|------|
| pageNo | int | 页码，从1开始 |
| pageSize | int | 每页数量，默认20 |

## 3. 接口详细定义

### 3.1 创建工单

**接口说明**: 创建新的生产工单

| 属性 | 内容 |
|------|------|
| 接口路径 | POST /mes/work-order/create |
| 接口说明 | 创建新的生产工单，状态为"待下发" |
| 权限标识 | mes:work-order:create |

**请求参数**:
| 参数名 | 类型 | 必填 | 说明 |
|--------|------|------|------|
| productId | Long | 是 | 产品ID |
| productCode | String | 是 | 产品编码 |
| productName | String | 是 | 产品名称 |
| planQty | Integer | 是 | 计划数量 |
| routingId | Long | 是 | 工艺路线ID |
| lineId | Long | 是 | 产线ID |
| planStartTime | DateTime | 是 | 计划开始时间 |
| planEndTime | DateTime | 是 | 计划结束时间 |
| priority | Integer | 否 | 优先级(1-10)，默认5 |
| remark | String | 否 | 备注 |

**请求示例**:
```json
{
  "productId": 1001,
  "productCode": "MODEL-Y-001",
  "productName": "Model Y 标准版",
  "planQty": 100,
  "routingId": 2001,
  "lineId": 3001,
  "planStartTime": "2026-03-25 08:00:00",
  "planEndTime": "2026-03-25 17:00:00",
  "priority": 5,
  "remark": "优先生产"
}
```

**响应结构**:
| 字段名 | 类型 | 说明 |
|--------|------|------|
| id | Long | 工单ID |
| orderNo | String | 工单编号 |
| status | Integer | 状态 |

**响应示例**:
```json
{
  "code": 0,
  "message": "success",
  "data": {
    "id": 10001,
    "orderNo": "WO202603240001",
    "status": 0
  }
}
```

### 3.2 更新工单

**接口说明**: 更新工单信息（仅待下发状态可修改）

| 属性 | 内容 |
|------|------|
| 接口路径 | PUT /mes/work-order/update |
| 接口说明 | 更新工单信息，仅"待下发"状态可修改 |
| 权限标识 | mes:work-order:update |

**请求参数**:
| 参数名 | 类型 | 必填 | 说明 |
|--------|------|------|------|
| id | Long | 是 | 工单ID |
| planQty | Integer | 否 | 计划数量 |
| routingId | Long | 否 | 工艺路线ID |
| lineId | Long | 否 | 产线ID |
| planStartTime | DateTime | 否 | 计划开始时间 |
| planEndTime | DateTime | 否 | 计划结束时间 |
| priority | Integer | 否 | 优先级 |
| remark | String | 否 | 备注 |

### 3.3 获取工单详情

**接口说明**: 根据ID获取工单详情

| 属性 | 内容 |
|------|------|
| 接口路径 | GET /mes/work-order/get |
| 接口说明 | 根据ID获取工单详细信息 |
| 权限标识 | mes:work-order:query |

**请求参数**:
| 参数名 | 类型 | 必填 | 说明 |
|--------|------|------|------|
| id | Long | 是 | 工单ID |

**响应结构**:
| 字段名 | 类型 | 说明 |
|--------|------|------|
| id | Long | 工单ID |
| orderNo | String | 工单编号 |
| erpOrderNo | String | ERP订单编号 |
| productId | Long | 产品ID |
| productCode | String | 产品编码 |
| productName | String | 产品名称 |
| planQty | Integer | 计划数量 |
| actualQty | Integer | 实际数量 |
| routingId | Long | 工艺路线ID |
| routingName | String | 工艺路线名称 |
| lineId | Long | 产线ID |
| lineName | String | 产线名称 |
| status | Integer | 状态 |
| statusName | String | 状态名称 |
| priority | Integer | 优先级 |
| planStartTime | DateTime | 计划开始时间 |
| planEndTime | DateTime | 计划结束时间 |
| actualStartTime | DateTime | 实际开始时间 |
| actualEndTime | DateTime | 实际结束时间 |
| remark | String | 备注 |
| creator | String | 创建人 |
| createTime | DateTime | 创建时间 |

### 3.4 分页查询工单

**接口说明**: 分页查询工单列表

| 属性 | 内容 |
|------|------|
| 接口路径 | GET /mes/work-order/page |
| 接口说明 | 分页查询工单列表，支持多条件筛选 |
| 权限标识 | mes:work-order:query |

**请求参数**:
| 参数名 | 类型 | 必填 | 说明 |
|--------|------|------|------|
| orderNo | String | 否 | 工单编号（模糊查询） |
| productId | Long | 否 | 产品ID |
| lineId | Long | 否 | 产线ID |
| status | Integer | 否 | 状态 |
| planStartTimeBegin | DateTime | 否 | 计划开始时间起 |
| planStartTimeEnd | DateTime | 否 | 计划开始时间止 |
| pageNo | Integer | 否 | 页码，默认1 |
| pageSize | Integer | 否 | 每页数量，默认20 |

**响应结构**:
| 字段名 | 类型 | 说明 |
|--------|------|------|
| total | Long | 总数 |
| list | Array | 数据列表 |

### 3.5 下发工单

**接口说明**: 下发工单到产线

| 属性 | 内容 |
|------|------|
| 接口路径 | PUT /mes/work-order/release |
| 接口说明 | 将工单下发到产线，状态变为"已下发" |
| 权限标识 | mes:work-order:release |

**请求参数**:
| 参数名 | 类型 | 必填 | 说明 |
|--------|------|------|------|
| id | Long | 是 | 工单ID |

**响应示例**:
```json
{
  "code": 0,
  "message": "下发成功",
  "data": {
    "id": 10001,
    "status": 1,
    "statusName": "已下发"
  }
}
```

### 3.6 开始生产

**接口说明**: 开始生产执行

| 属性 | 内容 |
|------|------|
| 接口路径 | PUT /mes/work-order/start |
| 接口说明 | 开始生产，状态变为"生产中" |
| 权限标识 | mes:work-order:operate |

**请求参数**:
| 参数名 | 类型 | 必填 | 说明 |
|--------|------|------|------|
| id | Long | 是 | 工单ID |

### 3.7 完成工单

**接口说明**: 完成工单

| 属性 | 内容 |
|------|------|
| 接口路径 | PUT /mes/work-order/complete |
| 接口说明 | 完成工单，状态变为"已完成" |
| 权限标识 | mes:work-order:operate |

**请求参数**:
| 参数名 | 类型 | 必填 | 说明 |
|--------|------|------|------|
| id | Long | 是 | 工单ID |
| actualQty | Integer | 是 | 实际数量 |

### 3.8 关闭工单

**接口说明**: 关闭工单

| 属性 | 内容 |
|------|------|
| 接口路径 | PUT /mes/work-order/close |
| 接口说明 | 关闭工单，状态变为"已关闭" |
| 权限标识 | mes:work-order:operate |

**请求参数**:
| 参数名 | 类型 | 必填 | 说明 |
|--------|------|------|------|
| id | Long | 是 | 工单ID |
| reason | String | 是 | 关闭原因 |

### 3.9 删除工单

**接口说明**: 删除工单（仅待下发状态可删除）

| 属性 | 内容 |
|------|------|
| 接口路径 | DELETE /mes/work-order/delete |
| 接口说明 | 删除工单，仅"待下发"状态可删除 |
| 权限标识 | mes:work-order:delete |

**请求参数**:
| 参数名 | 类型 | 必填 | 说明 |
|--------|------|------|------|
| id | Long | 是 | 工单ID |

## 4. 数据模型

### 4.1 请求DTO

#### WorkOrderCreateReqDTO
| 字段名 | 类型 | 必填 | 校验 | 说明 |
|--------|------|------|------|------|
| productId | Long | 是 | @NotNull | 产品ID |
| productCode | String | 是 | @NotBlank | 产品编码 |
| productName | String | 是 | @NotBlank | 产品名称 |
| planQty | Integer | 是 | @Min(1) | 计划数量 |
| routingId | Long | 是 | @NotNull | 工艺路线ID |
| lineId | Long | 是 | @NotNull | 产线ID |
| planStartTime | LocalDateTime | 是 | @NotNull | 计划开始时间 |
| planEndTime | LocalDateTime | 是 | @NotNull | 计划结束时间 |
| priority | Integer | 否 | @Min(1) @Max(10) | 优先级 |
| remark | String | 否 | @Length(max=500) | 备注 |

#### WorkOrderPageReqDTO
| 字段名 | 类型 | 必填 | 校验 | 说明 |
|--------|------|------|------|------|
| orderNo | String | 否 | @Length(max=64) | 工单编号 |
| productId | Long | 否 | - | 产品ID |
| lineId | Long | 否 | - | 产线ID |
| status | Integer | 否 | - | 状态 |
| planStartTimeBegin | LocalDateTime | 否 | - | 计划开始时间起 |
| planStartTimeEnd | LocalDateTime | 否 | - | 计划开始时间止 |
| pageNo | Integer | 否 | @Min(1) | 页码 |
| pageSize | Integer | 否 | @Min(1) @Max(100) | 每页数量 |

### 4.2 响应VO

#### WorkOrderRespVO
| 字段名 | 类型 | 说明 |
|--------|------|------|
| id | Long | 工单ID |
| orderNo | String | 工单编号 |
| erpOrderNo | String | ERP订单编号 |
| productId | Long | 产品ID |
| productCode | String | 产品编码 |
| productName | String | 产品名称 |
| planQty | Integer | 计划数量 |
| actualQty | Integer | 实际数量 |
| routingId | Long | 工艺路线ID |
| routingName | String | 工艺路线名称 |
| lineId | Long | 产线ID |
| lineName | String | 产线名称 |
| workshopId | Long | 车间ID |
| workshopName | String | 车间名称 |
| status | Integer | 状态 |
| statusName | String | 状态名称 |
| priority | Integer | 优先级 |
| planStartTime | LocalDateTime | 计划开始时间 |
| planEndTime | LocalDateTime | 计划结束时间 |
| actualStartTime | LocalDateTime | 实际开始时间 |
| actualEndTime | LocalDateTime | 实际结束时间 |
| remark | String | 备注 |
| creator | String | 创建人 |
| createTime | LocalDateTime | 创建时间 |

## 5. 错误码定义

| 错误码 | 错误信息 | 说明 |
|--------|----------|------|
| 0 | success | 成功 |
| 1001001 | 工单不存在 | 指定ID的工单不存在 |
| 1001002 | 工单状态不允许此操作 | 当前状态不支持该操作 |
| 1001003 | 该产线已有生产中的工单 | 产线唯一约束校验失败 |
| 1001004 | 存在未完成的作业记录 | 关闭前检查失败 |
| 1001005 | 计划数量必须大于0 | 数量校验失败 |
| 1001006 | 计划开始时间不能晚于结束时间 | 时间校验失败 |

## 6. 接口调用示例

### 6.1 创建工单
```bash
curl -X POST 'http://api.example.com/mes/work-order/create' \
  -H 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...' \
  -H 'Content-Type: application/json' \
  -H 'X-Tenant-Id: 1' \
  -d '{
    "productId": 1001,
    "productCode": "MODEL-Y-001",
    "productName": "Model Y 标准版",
    "planQty": 100,
    "routingId": 2001,
    "lineId": 3001,
    "planStartTime": "2026-03-25 08:00:00",
    "planEndTime": "2026-03-25 17:00:00"
  }'
```

### 6.2 查询工单列表
```bash
curl -X GET 'http://api.example.com/mes/work-order/page?status=0&pageNo=1&pageSize=20' \
  -H 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...' \
  -H 'X-Tenant-Id: 1'
```

### 6.3 下发工单
```bash
curl -X PUT 'http://api.example.com/mes/work-order/release' \
  -H 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...' \
  -H 'Content-Type: application/json' \
  -H 'X-Tenant-Id: 1' \
  -d '{"id": 10001}'
```
```

## 依赖工具
- Read - 读取模块设计文档
- Write - 输出API设计文档
- Grep - 搜索相关接口定义

## 注意事项
- 遵循RESTful设计规范
- 接口命名使用小写中划线格式
- 请求/响应字段命名使用驼峰格式
- 错误码要有规律，便于识别和处理
- 敏感字段不要在响应中返回
- 分页查询需要考虑性能优化