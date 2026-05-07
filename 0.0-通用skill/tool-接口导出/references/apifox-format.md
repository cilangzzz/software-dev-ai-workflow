# Apifox 项目导出格式规范

## 顶层结构

```json
{
  "apifoxProject": "1.0.0",
  "$schema": {
    "app": "apifox",
    "type": "project",
    "version": "1.2.0"
  },
  "info": { ... },
  "projectSetting": { ... },
  "apiCollection": [ ... ],
  "socketCollection": [],
  "docCollection": [],
  "schemaCollection": [],
  "commonParameters": { ... },
  "projectTestCaseCategories": [ ... ],
  "projectTestCaseTags": [ ... ],
  "moduleSettings": [ ... ],
  "globalVariables": [ ... ]
}
```

## info 对象

```json
{
  "info": {
    "name": "项目名称",
    "description": "",
    "mockRule": {
      "rules": [],
      "enableSystemRule": true
    }
  }
}
```

## projectSetting

```json
{
  "projectSetting": {
    "id": "项目ID（可随机生成数字字符串）",
    "auth": {},
    "securityScheme": {},
    "gateway": [],
    "language": "zh-CN",
    "apiStatuses": ["released"],
    "mockSettings": {},
    "advancedSettings": {
      "enableJsonc": false,
      "enableBigint": false,
      "responseValidate": true,
      "enableTestScenarioSetting": false,
      "enableYAPICompatScript": false,
      "isDefaultUrlEncoding": 2,
      "publishedDocUrlRules": {
        "defaultRule": "RESOURCE_KEY_ONLY",
        "resourceKeyStandard": "NEW"
      },
      "folderShareExpandModeSettings": {
        "expandId": [],
        "mode": "AUTO"
      }
    },
    "servers": [
      {
        "id": "default",
        "name": "默认服务",
        "moduleId": "模块ID数字"
      }
    ],
    "cloudMock": {
      "security": "free",
      "enable": false,
      "tokenKey": "apifoxToken"
    }
  }
}
```

## apiCollection 结构

### 文件夹层级

```json
{
  "apiCollection": [
    {
      "name": "根目录",
      "id": "数字ID",
      "auth": {},
      "securityScheme": {},
      "parentId": 0,
      "serverId": "",
      "description": "",
      "identityPattern": {
        "httpApi": {
          "type": "methodAndPath",
          "bodyType": "",
          "fields": []
        }
      },
      "shareSettings": {},
      "visibility": "SHARED",
      "moduleId": "模块ID",
      "preProcessors": [
        { "id": "inheritProcessors", "type": "inheritProcessors", "data": {} }
      ],
      "postProcessors": [
        { "id": "inheritProcessors", "type": "inheritProcessors", "data": {} }
      ],
      "inheritPostProcessors": {},
      "inheritPreProcessors": {},
      "items": [
        {
          "name": "模块文件夹名（如：登录 Copy）",
          "id": "数字ID",
          "auth": {},
          "securityScheme": {},
          "parentId": 0,
          "serverId": "",
          "description": "",
          "identityPattern": {
            "httpApi": {
              "type": "inherit",
              "bodyType": "",
              "fields": []
            }
          },
          "shareSettings": {},
          "visibility": "INHERITED",
          "moduleId": "模块ID",
          "preProcessors": [ ... ],
          "postProcessors": [ ... ],
          "inheritPostProcessors": {},
          "inheritPreProcessors": {},
          "items": [ ... ]  // 子文件夹或API项
        }
      ]
    }
  ]
}
```

### API 项（单个接口）

```json
{
  "name": "接口名称",
  "api": {
    "id": "字符串ID",
    "method": "post/get/put/delete/patch",
    "path": "完整URL路径",
    "parameters": {},
    "auth": {},
    "securityScheme": {},
    "commonParameters": {
      "query": [],
      "body": [],
      "cookie": [],
      "header": [
        { "name": "Authorization" }
      ]
    },
    "responses": [
      {
        "id": "字符串ID",
        "code": 200,
        "name": "成功",
        "headers": [],
        "jsonSchema": {
          "type": "object",
          "properties": { ... },
          "required": [ ... ]
        },
        "description": "",
        "contentType": "json",
        "mediaType": ""
      }
    ],
    "responseExamples": [],
    "requestBody": {
      "type": "application/json",
      "parameters": [],
      "jsonSchema": {
        "type": "object",
        "properties": { ... }
      },
      "mediaType": "",
      "examples": [
        {
          "value": "{\"key\":\"value\"}",
          "mediaType": "application/json",
          "description": ""
        }
      ],
      "oasExtensions": ""
    },
    "description": "接口描述",
    "tags": [],
    "status": "developing",
    "serverId": "",
    "operationId": "",
    "sourceUrl": "",
    "ordering": 0,
    "cases": [ ... ],
    "mocks": [],
    "customApiFields": "{}",
    "advancedSettings": {
      "disabledSystemHeaders": {}
    },
    "mockScript": {},
    "codeSamples": [],
    "commonResponseStatus": {},
    "responseChildren": [],
    "visibility": "INHERITED",
    "moduleId": "模块ID",
    "oasExtensions": "",
    "type": "http",
    "preProcessors": [],
    "postProcessors": [],
    "inheritPostProcessors": {},
    "inheritPreProcessors": {}
  }
}
```

### 测试用例（cases）

每个API可包含多个测试用例：

```json
{
  "id": "数字ID",
  "type": "DEBUG_CASE",
  "path": null,
  "name": "用例名称（如：管理员、广州市公安局）",
  "responseId": "关联的response ID",
  "parameters": {},
  "commonParameters": {
    "query": [],
    "body": [],
    "header": [
      { "name": "Authorization" }
    ],
    "cookie": []
  },
  "requestBody": {
    "parameters": [],
    "data": "{\"username\":\"admin\",\"password\":\"admin123\"}",
    "type": "application/json"
  },
  "auth": {},
  "securityScheme": {},
  "advancedSettings": {
    "disabledSystemHeaders": {},
    "isDefaultUrlEncoding": 2,
    "disableUrlEncoding": false
  },
  "visibility": "INHERITED",
  "moduleId": "模块ID",
  "categoryId": 0,
  "tagIds": [],
  "apiTestDataList": [],
  "preProcessors": [],
  "postProcessors": [],
  "inheritPostProcessors": {},
  "inheritPreProcessors": {}
}
```

## commonParameters（全局公共参数）

```json
{
  "commonParameters": {
    "id": "数字ID",
    "parameters": {
      "header": [
        {
          "name": "Authorization",
          "defaultEnable": true,
          "type": "string",
          "id": "字符串ID",
          "defaultValue": "{{ACCESS_TOKEN}}",
          "schema": {
            "type": "string",
            "default": "{{ACCESS_TOKEN}}"
          }
        }
      ]
    },
    "projectId": "项目ID",
    "creatorId": "数字ID",
    "editorId": "数字ID"
  }
}
```

## projectTestCaseCategories（测试用例分类）

预定义的5个分类：

```json
[
  { "id": "数字ID", "name": "正向", "description": null },
  { "id": "数字ID", "name": "负向", "description": null },
  { "id": "数字ID", "name": "边界值", "description": null },
  { "id": "数字ID", "name": "安全性", "description": null },
  { "id": "数字ID", "name": "其他", "description": null }
]
```

## projectTestCaseTags（测试用例标签）

28个标准标签，分组如下：

| 分组 | 标签名 | 描述 |
|------|--------|------|
| 正向 | 仅传必要字段 | 仅发送必填字段 |
| 正向 | 语义合法 | 业务逻辑有意义的值 |
| 正向 | 覆盖枚举组合 | 正交设计覆盖枚举 |
| 正向 | 其他正向 | 符合规范的有效输入 |
| 负向 | 缺失必填字段 | 省略必填字段 |
| 负向 | 无效值 | 类型正确但逻辑无效 |
| 负向 | 类型错误 | 数据类型不正确 |
| 负向 | 格式错误 | 格式不正确 |
| 负向 | 语义非法 | 语法正确但逻辑不可能 |
| 负向 | 其他负向 | 无效或意外输入 |
| 边界值 | Null | JSON null |
| 边界值 | 零值 | 数字0 |
| 边界值 | 空值 | 空字符串 |
| 边界值 | 极大值 | 最大边界值 |
| 边界值 | 极小值 | 最小边界值 |
| 边界值 | 超出最大边界值 | 超过允许的最大值 |
| 边界值 | 超出最小边界值 | 超过允许的最小值 |
| 边界值 | 字符串过长 | 超出最大长度 |
| 边界值 | 字符串过短 | 低于最小长度 |
| 安全性 | 对象级别授权缺失 | 未授权访问对象 |
| 安全性 | 访问控制 | 角色权限限制 |
| 安全性 | 认证失败 | 认证绕过 |
| 安全性 | SQL注入 | 恶意SQL代码 |
| 安全性 | XSS注入 | 跨站脚本 |
| 安全性 | 模糊输入 | 随机生成的payload |
| 安全性 | 命令行注入 | shell命令注入 |
| 安全性 | JSON注入 | 恶意JSON结构 |
| 安全性 | NoSQL注入 | NoSQL恶意查询 |
| 其他 | 其他 | 未归属标签 |

## moduleSettings（模块设置）

```json
[
  {
    "id": "模块ID",
    "name": "模块名称",
    "description": "模块描述",
    "moduleVariables": [
      {
        "name": "baseUrl",
        "value": "http://host:port/prefix",
        "description": "",
        "isBindInitial": true,
        "initialValue": "http://host:port/prefix",
        "isSync": true
      },
      {
        "name": "token",
        "value": "",
        "description": "",
        "isBindInitial": true,
        "initialValue": "",
        "isSync": true
      }
    ],
    "openApiInfo": {
      "title": "项目标题",
      "contact": { "url": "", "email": "" },
      "license": { "name": "MIT", "url": "" },
      "version": "1.0.0"
    }
  }
]
```

## ID生成规则

- 项目ID、模块ID、文件夹ID：随机数字字符串（如 "7061765"、"6082048"）
- API ID：随机数字字符串（如 "368736812"）
- Response ID：随机数字字符串（如 "800814553"）
- Case ID：随机数字（如 313747505）
- Parameter ID：随机字母数字字符串（如 "An9zy6HHT6"）
- 脚本ID：随机字母数字字符串（如 "VSeEJZwfeFhakVQJj7Oh0"）
- 标签ID、分类ID：连续递增数字
