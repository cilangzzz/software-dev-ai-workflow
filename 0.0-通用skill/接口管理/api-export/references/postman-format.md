# Postman Collection v2.1 格式规范

## 顶层结构

```json
{
  "info": {
    "name": "项目名称",
    "description": "",
    "schema": "https://schema.getpostman.com/json/collection/v2.1.0/collection.json"
  },
  "item": [ ... ],
  "variable": [],
  "event": [],
  "auth": {}
}
```

## item 数组（文件夹和请求）

### 文件夹

```json
{
  "name": "文件夹名（如：登录 Copy）",
  "description": "",
  "item": [ ... ],    // 子文件夹或请求
  "event": [
    {
      "listen": "prerequest",
      "script": { "exec": [], "type": "text/javascript", "packages": {} }
    },
    {
      "listen": "test",
      "script": { "exec": [], "type": "text/javascript", "packages": {} }
    }
  ],
  "auth": {}
}
```

### 请求

```json
{
  "name": "接口名称",
  "description": "",
  "event": [],
  "auth": {},
  "request": {
    "auth": {},
    "method": "POST",
    "body": {
      "mode": "raw",
      "raw": "{\"key\":\"value\"}",
      "options": {
        "raw": {
          "language": "json"
        }
      }
    },
    "header": [],
    "url": {
      "raw": "http://localhost:8080/api/path",
      "path": ["api", "path"],
      "host": ["localhost"],
      "protocol": "http",
      "port": "8080",
      "query": [],
      "variable": []
    }
  },
  "response": [ ... ],
  "protocolProfileBehavior": {
    "strictSSL": false,
    "followRedirects": true
  }
}
```

### URL解析规则

```json
{
  "url": {
    "raw": "{protocol}://{host}:{port}/{path.join('/')}",
    "path": ["segment1", "segment2", ...],
    "host": ["hostname"],
    "protocol": "http/https",
    "port": "端口号",
    "query": [
      {
        "key": "参数名",
        "value": "参数值",
        "description": "",
        "disabled": false
      }
    ],
    "variable": [
      {
        "key": "路径变量名",
        "value": "变量值",
        "description": ""
      }
    ]
  }
}
```

使用 `{{baseUrl}}` 变量时：
```json
{
  "url": {
    "raw": "{{baseUrl}}/api/path",
    "host": ["{{baseUrl}}"],
    "path": ["api", "path"]
  }
}
```

## saved responses（保存的响应示例）

```json
{
  "response": [
    {
      "name": "响应名称（如：管理员）",
      "originalRequest": {
        "method": "POST",
        "header": [],
        "url": { ... },
        "body": {
          "mode": "raw",
          "raw": "{\"key\":\"value\"}",
          "options": { "raw": { "language": "json" } }
        }
      },
      "cookie": [],
      "status": "OK",
      "code": 200,
      "_postman_previewlanguage": "json",
      "header": [
        { "key": "Content-Type", "value": "application/json;charset=UTF-8" }
      ],
      "body": "{\"code\":0,\"data\":{...},\"msg\":\"\"}"
    }
  ]
}
```

## 脚本（pre-request / test）

### 自动登录脚本模板

```javascript
function sendLoginRequest() {
  const baseUrl = pm.request.getBaseUrl();
  const username = pm.environment.get("LOGIN_USERNAME");
  const password = pm.environment.get("LOGIN_PASSWORD");

  const loginRequest = {
    url: baseUrl + "/admin-api/system/auth/login",
    method: "POST",
    header: {
      "Content-Type": "application/json",
    },
    body: {
      mode: 'raw',
      raw: JSON.stringify({"username": username, "password": password, "rememberMe": true}),
    }
  };

  pm.sendRequest(loginRequest, function(err, res) {
    if (err) {
      console.log(err);
    } else {
      const jsonData = res.json();
      pm.environment.set("ACCESS_TOKEN", jsonData.data.accessToken);
      pm.environment.set("ACCESS_TOKEN_EXPIRES", jsonData.data.accessTokenExpires);
    }
  });
}

const accessToken = pm.environment.get("ACCESS_TOKEN");
const accessTokenExpires = pm.environment.get("ACCESS_TOKEN_EXPIRES");
sendLoginRequest();
```

## variable（集合变量）

```json
{
  "variable": [
    {
      "key": "baseUrl",
      "value": "http://localhost:8080",
      "type": "string"
    }
  ]
}
```

## 与 OpenAPI 的映射关系

| OpenAPI | Postman |
|---------|---------|
| paths[path][method] | item[].request |
| parameters (in: header) | request.header[] |
| parameters (in: query) | request.url.query[] |
| parameters (in: path) | request.url.variable[] |
| requestBody.content["application/json"].example | request.body.raw |
| responses.200.content["application/json"] | response[].body |
| servers[0].url | url.raw 或 variable baseUrl |
| tags[0] | item 文件夹名 |
