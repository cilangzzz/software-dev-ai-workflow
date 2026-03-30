# api-designer

## 基本信息
| 属性 | 值 |
|------|------|
| 名称 | api-designer |
| 版本 | 1.0.0 |
| 部门 | 研发部 |
| 优先级 | P0 |
| 复杂度 | high |
| 预估时间 | 25-45min |

## 描述
根据数据库设计和业务需求，生成RESTful API设计文档，包括：
- 接口定义（URL、Method、参数）
- 请求体Schema（JSON格式）
- 响应体Schema（统一响应格式）
- 错误码设计
- 鉴权配置
- OpenAPI规范文件
- Postman Collection

## 触发条件

### 命令触发
```
/api-designer
```

### 事件触发
| 事件 | 条件 |
|------|------|
| db_design_completed | 数据库设计文档完成 |
| prd_approved | PRD文档审核通过 |
| contract_signed | 开发契约签署 |

### 自然语言触发
| 关键词 | 示例 |
|--------|------|
| 设计API接口 | "请为销售管理模块设计API接口" |
| 生成接口文档 | "生成客户管理的接口文档" |
| 创建REST API | "创建订单管理的REST API" |

## 输入参数

| 参数名 | 类型 | 必填 | 默认值 | 描述 |
|--------|------|------|--------|------|
| db_design_file | string | 是 | - | 数据库设计文档路径 |
| prd_file | string | 是 | - | PRD文档路径 |
| api_prefix | string | 否 | /admin-api/erp/{module} | API路径前缀 |
| auth_type | string | 否 | bearer | 鉴权类型：bearer/oauth2/api_key/none |
| pagination | object | 否 | 见默认配置 | 分页配置 |
| module_code | string | 是 | - | 模块编码（如sd、wm、pp） |

### 默认分页配置
```yaml
pagination:
  default_page_no: 1
  default_page_size: 10
  max_page_size: 100
  param_names:
    page_no: pageNo
    page_size: pageSize
```

## 输出产物

| 产物 | 路径 | 类型 | 描述 |
|------|------|------|------|
| API设计文档 | 研发/API设计/API-{module}.md | document | 完整API设计文档 |
| OpenAPI规范 | 研发/API设计/openapi/{module}.yaml | spec | OpenAPI 3.0规范文件 |
| Postman Collection | 研发/API设计/postman/{module}.postman_collection.json | collection | Postman测试集合 |

## 执行流程

### Phase 1: 实体分析（5min）
```
1. 解析数据库设计文档
   - 提取所有表结构
   - 识别实体名称和字段
   - 分析主键和外键关系

2. 识别CRUD实体
   - 需要完整CRUD的实体（客户、订单等）
   - 只需要R（查询）的实体（字典、配置等）
   - 需要特殊操作的实体（状态流转等）

3. 分析业务流程关联
   - 从PRD提取业务流程
   - 确定需要组合接口的场景
   - 识别批量操作需求
```

### Phase 2: 端点设计（10min）
```
1. 设计RESTful端点命名
   | 操作 | URL Pattern | Method | 示例 |
   |------|-------------|--------|------|
   | 列表查询 | /{resources} | GET | GET /customers |
   | 详情查询 | /{resources}/{id} | GET | GET /customers/1 |
   | 创建 | /{resources} | POST | POST /customers |
   | 更新 | /{resources}/{id} | PUT | PUT /customers/1 |
   | 删除 | /{resources}/{id} | DELETE | DELETE /customers/1 |
   | 批量删除 | /{resources}/batch | DELETE | DELETE /customers/batch |
   | 批量创建 | /{resources}/batch | POST | POST /customers/batch |

2. 定义HTTP方法语义
   - GET: 安全、幂等、可缓存
   - POST: 创建资源、非幂等
   - PUT: 更新资源、幂等
   - DELETE: 删除资源、幂等

3. 设计URL路径结构
   - 基础路径: {api_prefix}/{module}/{resource}
   - 版本路径: {api_prefix}/v1/{module}/{resource}
   - 子资源路径: {api_prefix}/{module}/{resource}/{id}/{sub-resource}
   - 限制: 嵌套不超过两层

4. 设计查询参数
   | 参数类型 | 参数名 | 描述 | 示例 |
   |----------|--------|------|------|
   | 分页 | pageNo, pageSize | 分页参数 | pageNo=1&pageSize=10 |
   | 排序 | sortField, sortOrder | 排序参数 | sortField=name&sortOrder=desc |
   | 过滤 | {field} | 字段过滤 | customerType=1 |
   | 搜索 | keyword | 关键词搜索 | keyword=张三 |
```

### Phase 3: 请求响应设计（15min）
```
1. 设计请求体Schema
   - 创建请求: 必填字段 + 可选字段
   - 更新请求: 可更新字段（排除不可更新字段）
   - 批量请求: 数组包装

2. 设计响应体Schema（统一格式）
   ```json
   {
     "code": 0,                    // 状态码，0表示成功
     "message": "success",         // 状态消息
     "data": {},                   // 业务数据
     "timestamp": 1709875200000    // 时间戳
   }
   ```

3. 设计分页响应格式
   ```json
   {
     "code": 0,
     "message": "success",
     "data": {
       "list": [],               // 数据列表
       "total": 100,             // 总记录数
       "pageNo": 1,              // 当前页码
       "pageSize": 10            // 每页数量
     },
     "timestamp": 1709875200000
   }
   ```

4. 设计错误响应格式
   ```json
   {
     "code": 40001,              // 错误码
     "message": "参数校验失败",   // 错误消息
     "data": {
       "errors": [               // 详细错误列表
         {
           "field": "customerName",
           "message": "客户名称不能为空"
         }
       ]
     },
     "timestamp": 1709875200000
   }
   ```

### Phase 4: 文档生成（10min）
```
1. 生成API设计文档
   - 文档头部信息（编号、版本、日期）
   - 接口概述（规范、响应格式、错误码）
   - 接口详情（按实体分组）
   - 公共参数说明

2. 生成OpenAPI 3.0规范
   - info: API基本信息
   - servers: 服务地址配置
   - paths: 接口路径定义
   - components: 公共组件定义
     - schemas: 数据模型
     - responses: 响应模板
     - parameters: 参数模板
     - securitySchemes: 鉴权配置

3. 生成Postman Collection
   - info: Collection信息
   - item: 接口请求列表
   - variable: 环境变量
   - auth: 鉴权配置
```

## API设计规范

### RESTful规范
| 规范项 | 说明 | 示例 |
|--------|------|------|
| 资源命名 | 使用名词复数 | /customers, /orders |
| HTTP方法语义 | 正确使用GET/POST/PUT/DELETE | POST创建，PUT更新 |
| 版本化 | URL或Header版本控制 | /v1/customers 或 X-API-Version: 1 |
| 嵌套资源 | 不超过两层 | /customers/1/orders |
| 过滤排序 | 使用查询参数 | ?status=1&sortField=name |

### 响应码规范
| 业务码 | HTTP状态码 | 描述 |
|--------|------------|------|
| 0 | 200 | 成功 |
| 40001 | 400 | 参数校验失败 |
| 40002 | 400 | 参数格式错误 |
| 40003 | 401 | 未授权/Token过期 |
| 40004 | 403 | 权限不足 |
| 40005 | 404 | 资源不存在 |
| 40006 | 409 | 资源冲突 |
| 40007 | 500 | 服务器内部错误 |
| 40008 | 503 | 服务不可用 |

### 鉴权配置
| 鉴权类型 | Header格式 | 说明 |
|----------|------------|------|
| bearer | Authorization: Bearer {token} | JWT Token |
| api_key | X-API-Key: {key} | API密钥 |
| basic | Authorization: Basic {credentials} | 基础认证 |

## 质量标准

### 必须满足
| 标准 | 描述 | 验证方式 |
|------|------|----------|
| 鉴权配置 | 所有接口必须有鉴权配置（除白名单接口） | 检查security配置 |
| 参数描述完整 | 所有参数必须有类型和描述 | 检查参数定义 |
| 统一响应格式 | 所有响应使用统一格式 | 检查响应Schema |
| 错误码分类 | 错误码必须有分类和描述 | 检查错误码定义 |
| 分页参数统一 | 使用统一分页参数名 | 检查分页参数 |
| 批量操作限制 | 批量操作接口必须有数量限制（如100条） | 检查批量接口 |

### 建议满足
| 标准 | 描述 |
|------|------|
| 接口命名清晰 | URL路径能清晰表达业务含义 |
| 参数校验完整 | 请求参数有完整的校验规则 |
| 示例数据真实 | 提供真实的请求/响应示例 |
| 版本控制合理 | API版本与业务版本对应 |

## 示例

### 输入
```yaml
db_design_file: 研发/数据库设计/DB-01-销售管理模块.md
prd_file: 产品/PRD/PRD-01-销售管理模块.md
module_code: sd
api_prefix: /admin-api/erp/sd
auth_type: bearer
```

### 输出（部分示例）

#### API设计文档
```markdown
## 1. 接口概述

### 1.1 基本信息
- **模块**: 销售管理模块(SD)
- **版本**: V1.0
- **基础路径**: /admin-api/erp/sd
- **鉴权方式**: Bearer Token

### 1.2 统一响应格式
...

## 2. 客户管理接口

### 2.1 客户列表查询
- **URL**: GET /admin-api/erp/sd/customers
- **鉴权**: Bearer Token (需登录)
- **描述**: 分页查询客户列表，支持过滤和排序

#### 请求参数
| 参数名 | 类型 | 必填 | 描述 |
|--------|------|------|------|
| pageNo | int | 否 | 页码，默认1 |
| pageSize | int | 否 | 每页数量，默认10，最大100 |
| customerName | string | 否 | 客户名称（模糊匹配） |
| customerType | int | 否 | 客户类型:1-整车厂,2-供应商,3-经销商 |
| customerLevel | int | 否 | 客户等级:1-A级,2-B级,3-C级 |
| status | int | 否 | 状态:0-禁用,1-启用 |
| sortField | string | 否 | 排序字段 |
| sortOrder | string | 否 | 排序方向:asc/desc |

#### 响应示例
```json
{
  "code": 0,
  "message": "success",
  "data": {
    "list": [
      {
        "id": 1,
        "customerCode": "C001",
        "customerName": "XX汽车制造有限公司",
        "customerType": 1,
        "customerLevel": 1,
        "creditLimit": 1000000.00,
        "creditUsed": 500000.00,
        "status": 1
      }
    ],
    "total": 100,
    "pageNo": 1,
    "pageSize": 10
  },
  "timestamp": 1709875200000
}
```

### 2.2 创建客户
- **URL**: POST /admin-api/erp/sd/customers
- **鉴权**: Bearer Token (需登录)

#### 请求体
```json
{
  "customerCode": "C001",
  "customerName": "XX汽车制造有限公司",
  "customerType": 1,
  "customerLevel": 1,
  "creditLimit": 1000000.00,
  "contactPerson": "张三",
  "contactPhone": "13800138000"
}
```
```

#### OpenAPI规范（部分）
```yaml
openapi: 3.0.0
info:
  title: 销售管理模块(SD) API
  version: 1.0.0
  description: ERP销售管理模块REST API

servers:
  - url: http://localhost:8080/admin-api/erp/sd
    description: 开发环境

security:
  - bearerAuth: []

components:
  securitySchemes:
    bearerAuth:
      type: http
      scheme: bearer

  schemas:
    Customer:
      type: object
      properties:
        id:
          type: integer
          format: int64
          description: 主键ID
        customerCode:
          type: string
          maxLength: 32
          description: 客户编码
        customerName:
          type: string
          maxLength: 200
          description: 客户名称

paths:
  /customers:
    get:
      summary: 客户列表查询
      operationId: listCustomers
      parameters:
        - name: pageNo
          in: query
          schema:
            type: integer
            default: 1
        - name: pageSize
          in: query
          schema:
            type: integer
            default: 10
      responses:
        '200':
          description: 成功
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/PageResponse'
```

## 错误处理

| 错误代码 | 错误描述 | 处理方式 |
|----------|----------|----------|
| API001 | DB设计文件不存在 | 返回错误，提示正确路径 |
| API002 | 表结构解析失败 | 分析文档格式，提供修复建议 |
| API003 | 实体命名冲突 | 检查命名规范，建议调整 |
| API004 | 接口路径冲突 | 检查URL设计，建议重构 |
| API005 | 参数定义不完整 | 补充必填参数 |

## 与其他Skill的关系

### 上游依赖
| Skill | 依赖内容 |
|------|----------|
| db-designer | 表结构作为API实体基础 |
| requirement-analyzer | 功能需求定义接口范围 |
| architect | API规范约束 |

### 下游输出
| Skill | 输出内容 |
|------|----------|
| crud-generator | API定义生成Controller代码 |
| test-case-generator | API定义生成测试用例 |
| api_test | OpenAPI规范用于接口测试 |