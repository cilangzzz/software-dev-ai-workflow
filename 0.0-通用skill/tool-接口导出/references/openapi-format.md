# OpenAPI 3.1.0 格式规范

## 顶层结构

```json
{
  "openapi": "3.1.0",
  "info": { ... },
  "tags": [],
  "paths": { ... },
  "webhooks": {},
  "components": {
    "schemas": {},
    "responses": {},
    "securitySchemes": {}
  },
  "servers": [],
  "security": []
}
```

## info 对象

| 字段 | 类型 | 必填 | 来源 |
|------|------|------|------|
| title | string | 是 | 项目名称 / 模块名 |
| description | string | 否 | 项目描述，从README或模块注释提取 |
| version | string | 是 | 项目版本号，从pom.xml/package.json提取 |
| contact.url | string | 否 | 项目主页或Dashboard地址 |
| contact.email | string | 否 | 联系邮箱 |
| license.name | string | 否 | 开源协议名称 |
| license.url | string | 否 | 开源协议链接 |

## servers 数组

```json
{
  "servers": [
    {
      "url": "{base_url}",
      "description": "默认服务"
    }
  ]
}
```

## paths 定义

### 路径规则
- key 为接口路径，如 `/admin-api/system/auth/login`
- 值为 HTTP 方法对象（get/post/put/delete/patch）

### 路径拼接
```
完整路径 = api_prefix + controller_mapping + method_mapping
```

### 单个接口结构

```json
{
  "/path": {
    "post": {
      "summary": "接口名称（从Swagger注解或方法名提取）",
      "deprecated": false,
      "description": "接口描述",
      "tags": ["模块名"],
      "parameters": [ ... ],
      "requestBody": { ... },
      "responses": { ... },
      "security": []
    }
  }
}
```

### parameters 数组

每个参数对象：

| 字段 | 类型 | 说明 |
|------|------|------|
| name | string | 参数名 |
| in | string | 位置: header/query/path/cookie |
| description | string | 参数描述 |
| example | string | 示例值 |
| schema.type | string | JSON Schema类型 |
| schema.default | string | 默认值 |

映射规则：
- `@RequestParam` → `in: "query"` 或 `in: "path"`（含路径变量时）
- `@RequestHeader` → `in: "header"`
- `@PathVariable` → `in: "path"`
- `@CookieValue` → `in: "cookie"`

### requestBody

```json
{
  "requestBody": {
    "content": {
      "application/json": {
        "schema": {
          "type": "object",
          "properties": {}
        },
        "example": { }
      }
    }
  }
}
```

- `@RequestBody` JSON参数 → `content: application/json`
- 表单参数 → `content: application/x-www-form-urlencoded`

### responses

```json
{
  "responses": {
    "200": {
      "description": "",
      "content": {
        "application/json": {
          "schema": {
            "type": "object",
            "properties": {
              "code": { "type": "integer" },
              "data": { "type": "object", "properties": { ... } },
              "msg": { "type": "string" }
            },
            "required": ["code", "data", "msg"]
          }
        }
      },
      "headers": {}
    }
  }
}
```

## components/schemas 定义

用于 `$ref` 引用，避免循环引用和重复定义。

```json
{
  "components": {
    "schemas": {
      "UserDTO": {
        "type": "object",
        "properties": {
          "id": { "type": "integer" },
          "name": { "type": "string" }
        },
        "required": ["id", "name"]
      }
    }
  }
}
```

## 类型映射（Java → JSON Schema）

| Java类型 | JSON Schema type | format |
|----------|-----------------|--------|
| String | string | - |
| Integer/int | integer | int32 |
| Long/long | integer | int64 |
| Float/float | number | float |
| Double/double | number | double |
| Boolean/boolean | boolean | - |
| BigDecimal | number | - |
| Date/LocalDateTime | string | date-time |
| LocalDate | string | date |
| UUID | string | uuid |
| byte[] | string | byte |
| List\<T\> | array | items: T |
| Set\<T\> | array | uniqueItems: true, items: T |
| Map\<K,V\> | object | additionalProperties: V |
| Enum | string | enum: [values] |

## 安全配置

```json
{
  "components": {
    "securitySchemes": {
      "BearerAuth": {
        "type": "http",
        "scheme": "bearer",
        "bearerFormat": "JWT"
      }
    }
  },
  "security": [
    { "BearerAuth": [] }
  ]
}
```
