# Markdown 文档生成规则

## 生成工具风格

参考 `@tarslib/widdershins v4.0.30` 的输出风格，从 OpenAPI 规范生成 Markdown。

## YAML Front Matter

```yaml
---
title: "{项目名称} API 文档"
language_tabs:
  - shell: Shell
  - http: HTTP
  - javascript: JavaScript
  - java: Java
  - python: Python
toc_footers: []
includes: []
search: true
highlight_theme: darkula
---
```

`language_tabs` 的值由输入参数 `lang_tabs` 决定。

## 文档结构

### 1. API 标题

```markdown
# {项目名称}

> {项目描述}

Base URLs:

* <a href="{base_url}">{base_url}</a>

认证方式: {auth_type_description}
```

### 2. 接口文档（每个接口一个章节）

```markdown
## {接口名称}

<a id="opId{operationId}"></a>

### 请求

`{METHOD} {path}`

{接口描述}

#### 请求头

| 参数名 | 类型 | 必填 | 描述 |
|--------|------|------|------|
| Authorization | string | 是 | Bearer Token |
| Content-Type | string | 是 | application/json |

#### 路径参数

| 参数名 | 类型 | 必填 | 描述 |
|--------|------|------|------|
| id | integer | 是 | 资源ID |

#### 查询参数

| 参数名 | 类型 | 必填 | 描述 |
|--------|------|------|------|
| page | integer | 否 | 页码 |

#### 请求体 (application/json)

```json
{
  "username": "admin",
  "password": "admin123"
}
```

| 参数名 | 类型 | 必填 | 描述 |
|--------|------|------|------|
| username | string | 是 | 用户名 |
| password | string | 是 | 密码 |

### 响应

#### 200 成功

```json
{
  "code": 0,
  "data": {
    "userId": 1,
    "accessToken": "xxx"
  },
  "msg": ""
}
```

| 参数名 | 类型 | 描述 |
|--------|------|------|
| code | integer | 状态码 |
| data | object | 响应数据 |
| data.userId | integer | 用户ID |
| data.accessToken | string | 访问令牌 |
| msg | string | 提示信息 |

---

```

### 3. 状态码参考

```markdown
## 状态码参考

| 状态码 | 描述 |
|--------|------|
| 200 | 成功 |
| 400 | 请求参数错误 |
| 401 | 未授权 |
| 403 | 禁止访问 |
| 404 | 资源不存在 |
| 500 | 服务器内部错误 |
```

## 嵌套对象的表格展示

对于嵌套的响应对象，使用 `父字段.子字段` 的方式展开展示：

```
| 参数名 | 类型 | 描述 |
|--------|------|------|
| data | object | 响应数据 |
| data.userId | integer | 用户ID |
| data.accessToken | string | 访问令牌 |
| data.refreshToken | string | 刷新令牌 |
| data.expiresTime | integer | 过期时间 |
```

## 多语言代码示例

为每个接口生成多种语言的请求示例：

### Shell (curl)

```shell
curl -X POST {base_url}{path} \
  -H "Authorization: Bearer {token}" \
  -H "Content-Type: application/json" \
  -d '{"username":"admin","password":"admin123"}'
```

### HTTP

```http
POST {path} HTTP/1.1
Host: {host}
Authorization: Bearer {token}
Content-Type: application/json

{"username":"admin","password":"admin123"}
```

### JavaScript

```javascript
fetch("{base_url}{path}", {
  method: "POST",
  headers: {
    "Authorization": "Bearer {token}",
    "Content-Type": "application/json"
  },
  body: JSON.stringify({"username":"admin","password":"admin123"})
})
.then(response => response.json())
.then(data => console.log(data));
```

### Java

```java
HttpClient client = HttpClient.newHttpClient();
String json = "{\"username\":\"admin\",\"password\":\"admin123\"}";
HttpRequest request = HttpRequest.newBuilder()
    .uri(URI.create("{base_url}{path}"))
    .header("Authorization", "Bearer {token}")
    .header("Content-Type", "application/json")
    .POST(HttpRequest.BodyPublishers.ofString(json))
    .build();
HttpResponse<String> response = client.send(request, HttpResponse.BodyHandlers.ofString());
System.out.println(response.body());
```

### Python

```python
import requests

response = requests.post(
    "{base_url}{path}",
    headers={
        "Authorization": "Bearer {token}",
        "Content-Type": "application/json"
    },
    json={"username": "admin", "password": "admin123"}
)
print(response.json())
```
