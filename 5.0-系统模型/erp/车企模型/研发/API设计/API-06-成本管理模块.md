# API-06 成本管理模块API设计 (CO)

## 文档信息

| 项目 | 内容 |
|------|------|
| 文档编号 | API-06 |
| 模块名称 | 成本管理 (Controlling) |
| 版本号 | V1.0 |
| 编制日期 | 2026-03-24 |
| 编制人 | 研发架构团队 |
| 技术栈 | Spring Boot 2.7 + MyBatis Plus |
| 状态 | 待评审 |

---

## 1. API设计概述

### 1.1 设计原则

- RESTful API设计风格
- 统一的请求响应格式
- 完善的错误处理机制
- API版本控制
- 接口权限控制

### 1.2 API命名规范

| 类型 | 规范 | 示例 |
|-----|------|------|
| URL路径 | 小写，单词用连字符分隔 | /api/v1/cost-elements |
| 查询参数 | 小驼峰命名 | costCenterId |
| 请求体字段 | 小驼峰命名 | elementCode |
| 响应体字段 | 小驼峰命名 | elementName |

### 1.3 通用响应格式

```json
{
  "code": 200,
  "message": "success",
  "data": {},
  "timestamp": 1711267200000
}
```

### 1.4 分页响应格式

```json
{
  "code": 200,
  "message": "success",
  "data": {
    "records": [],
    "total": 100,
    "size": 10,
    "current": 1,
    "pages": 10
  },
  "timestamp": 1711267200000
}
```

### 1.5 错误码定义

| 错误码 | 说明 |
|-------|------|
| 200 | 成功 |
| 400 | 请求参数错误 |
| 401 | 未授权 |
| 403 | 无权限 |
| 404 | 资源不存在 |
| 409 | 资源冲突 |
| 500 | 服务器内部错误 |
| 10001 | 成本要素编码已存在 |
| 10002 | 成本中心编码已存在 |
| 10003 | 成本核算期间已存在 |
| 10004 | 标准成本版本已存在 |

---

## 2. 成本要素管理API

### 2.1 查询成本要素列表

**接口说明**: 分页查询成本要素列表

**请求URL**: `GET /api/v1/cost-elements`

**请求参数**:

| 参数名 | 类型 | 必填 | 说明 |
|-------|------|------|------|
| elementCode | String | N | 成本要素编码 |
| elementName | String | N | 成本要素名称(模糊查询) |
| elementCategory | String | N | 成本要素类别 |
| status | Integer | N | 状态 |
| pageNum | Integer | N | 页码，默认1 |
| pageSize | Integer | N | 每页条数，默认10 |

**请求示例**:
```
GET /api/v1/cost-elements?elementName=材料&elementCategory=01&pageNum=1&pageSize=10
```

**响应示例**:
```json
{
  "code": 200,
  "message": "success",
  "data": {
    "records": [
      {
        "id": 1,
        "elementCode": "CE001",
        "elementName": "原材料成本",
        "elementCategory": "01",
        "elementCategoryName": "材料成本",
        "elementType": "01",
        "elementTypeName": "直接成本",
        "costBehavior": "01",
        "costBehaviorName": "变动成本",
        "controllable": 1,
        "glAccountCode": "5001",
        "glAccountName": "生产成本-直接材料",
        "status": 1,
        "createTime": "2026-03-24 10:00:00"
      }
    ],
    "total": 50,
    "size": 10,
    "current": 1,
    "pages": 5
  },
  "timestamp": 1711267200000
}
```

---

### 2.2 查询成本要素详情

**接口说明**: 根据ID查询成本要素详情

**请求URL**: `GET /api/v1/cost-elements/{id}`

**路径参数**:

| 参数名 | 类型 | 必填 | 说明 |
|-------|------|------|------|
| id | Long | Y | 成本要素ID |

**响应示例**:
```json
{
  "code": 200,
  "message": "success",
  "data": {
    "id": 1,
    "elementCode": "CE001",
    "elementName": "原材料成本",
    "elementCategory": "01",
    "elementCategoryName": "材料成本",
    "elementType": "01",
    "elementTypeName": "直接成本",
    "costBehavior": "01",
    "costBehaviorName": "变动成本",
    "controllable": 1,
    "glAccountId": 101,
    "glAccountCode": "5001",
    "glAccountName": "生产成本-直接材料",
    "parentId": 0,
    "levelNo": 1,
    "isLeaf": 1,
    "sortNo": 1,
    "status": 1,
    "createTime": "2026-03-24 10:00:00",
    "updateTime": "2026-03-24 10:00:00",
    "remark": ""
  },
  "timestamp": 1711267200000
}
```

---

### 2.3 创建成本要素

**接口说明**: 创建新的成本要素

**请求URL**: `POST /api/v1/cost-elements`

**请求体**:
```json
{
  "elementCode": "CE010",
  "elementName": "外购件成本",
  "elementCategory": "01",
  "elementType": "01",
  "costBehavior": "01",
  "controllable": 1,
  "glAccountId": 102,
  "glAccountCode": "5002",
  "parentId": 1,
  "sortNo": 10,
  "remark": "外购零部件成本"
}
```

**响应示例**:
```json
{
  "code": 200,
  "message": "创建成功",
  "data": {
    "id": 10
  },
  "timestamp": 1711267200000
}
```

---

### 2.4 更新成本要素

**接口说明**: 更新成本要素信息

**请求URL**: `PUT /api/v1/cost-elements/{id}`

**路径参数**:

| 参数名 | 类型 | 必填 | 说明 |
|-------|------|------|------|
| id | Long | Y | 成本要素ID |

**请求体**:
```json
{
  "elementName": "外购件成本-更新",
  "controllable": 0,
  "remark": "更新备注"
}
```

**响应示例**:
```json
{
  "code": 200,
  "message": "更新成功",
  "timestamp": 1711267200000
}
```

---

### 2.5 删除成本要素

**接口说明**: 删除成本要素(逻辑删除)

**请求URL**: `DELETE /api/v1/cost-elements/{id}`

**路径参数**:

| 参数名 | 类型 | 必填 | 说明 |
|-------|------|------|------|
| id | Long | Y | 成本要素ID |

**响应示例**:
```json
{
  "code": 200,
  "message": "删除成功",
  "timestamp": 1711267200000
}
```

---

### 2.6 启用/停用成本要素

**接口说明**: 启用或停用成本要素

**请求URL**: `PUT /api/v1/cost-elements/{id}/status`

**路径参数**:

| 参数名 | 类型 | 必填 | 说明 |
|-------|------|------|------|
| id | Long | Y | 成本要素ID |

**请求体**:
```json
{
  "status": 0
}
```

**响应示例**:
```json
{
  "code": 200,
  "message": "操作成功",
  "timestamp": 1711267200000
}
```

---

### 2.7 查询成本要素树

**接口说明**: 查询成本要素树形结构

**请求URL**: `GET /api/v1/cost-elements/tree`

**请求参数**:

| 参数名 | 类型 | 必填 | 说明 |
|-------|------|------|------|
| elementCategory | String | N | 成本要素类别 |

**响应示例**:
```json
{
  "code": 200,
  "message": "success",
  "data": [
    {
      "id": 1,
      "elementCode": "CE001",
      "elementName": "材料成本",
      "parentId": 0,
      "levelNo": 1,
      "children": [
        {
          "id": 2,
          "elementCode": "CE001-01",
          "elementName": "原材料成本",
          "parentId": 1,
          "levelNo": 2,
          "children": []
        }
      ]
    }
  ],
  "timestamp": 1711267200000
}
```

---

## 3. 成本中心管理API

### 3.1 查询成本中心列表

**接口说明**: 分页查询成本中心列表

**请求URL**: `GET /api/v1/cost-centers`

**请求参数**:

| 参数名 | 类型 | 必填 | 说明 |
|-------|------|------|------|
| centerCode | String | N | 成本中心编码 |
| centerName | String | N | 成本中心名称(模糊查询) |
| centerType | String | N | 成本中心类型 |
| departmentId | Long | N | 部门ID |
| status | Integer | N | 状态 |
| pageNum | Integer | N | 页码 |
| pageSize | Integer | N | 每页条数 |

**响应示例**:
```json
{
  "code": 200,
  "message": "success",
  "data": {
    "records": [
      {
        "id": 1,
        "centerCode": "CC001",
        "centerName": "冲压车间",
        "centerType": "01",
        "centerTypeName": "生产成本中心",
        "departmentId": 101,
        "departmentName": "冲压部",
        "managerId": 1001,
        "managerName": "张三",
        "workshopId": 1,
        "workshopName": "冲压车间",
        "status": 1,
        "createTime": "2026-03-24 10:00:00"
      }
    ],
    "total": 30,
    "size": 10,
    "current": 1,
    "pages": 3
  },
  "timestamp": 1711267200000
}
```

---

### 3.2 创建成本中心

**接口说明**: 创建新的成本中心

**请求URL**: `POST /api/v1/cost-centers`

**请求体**:
```json
{
  "centerCode": "CC010",
  "centerName": "总装车间",
  "centerType": "01",
  "departmentId": 105,
  "departmentCode": "DEPT005",
  "managerId": 1005,
  "workshopId": 5,
  "capacity": 10000,
  "capacityUnit": "台/月",
  "sortNo": 10,
  "remark": "总装车间成本中心"
}
```

**响应示例**:
```json
{
  "code": 200,
  "message": "创建成功",
  "data": {
    "id": 10
  },
  "timestamp": 1711267200000
}
```

---

### 3.3 查询成本中心树

**接口说明**: 查询成本中心树形结构

**请求URL**: `GET /api/v1/cost-centers/tree`

**响应示例**:
```json
{
  "code": 200,
  "message": "success",
  "data": [
    {
      "id": 1,
      "centerCode": "CC001",
      "centerName": "生产部",
      "centerType": "01",
      "parentId": 0,
      "levelNo": 1,
      "children": [
        {
          "id": 2,
          "centerCode": "CC001-01",
          "centerName": "冲压车间",
          "parentId": 1,
          "levelNo": 2,
          "children": []
        }
      ]
    }
  ],
  "timestamp": 1711267200000
}
```

---

### 3.4 查询成本中心成本汇总

**接口说明**: 查询成本中心的成本汇总信息

**请求URL**: `GET /api/v1/cost-centers/{id}/cost-summary`

**请求参数**:

| 参数名 | 类型 | 必填 | 说明 |
|-------|------|------|------|
| id | Long | Y | 成本中心ID |
| periodYear | Integer | Y | 会计年度 |
| periodMonth | Integer | Y | 会计期间 |

**响应示例**:
```json
{
  "code": 200,
  "message": "success",
  "data": {
    "costCenterId": 1,
    "costCenterName": "冲压车间",
    "periodYear": 2026,
    "periodMonth": 3,
    "totalMaterialCost": 1000000.00,
    "totalLaborCost": 200000.00,
    "totalOverheadCost": 150000.00,
    "totalCost": 1350000.00,
    "costByElement": [
      {
        "elementId": 1,
        "elementCode": "CE001",
        "elementName": "原材料成本",
        "amount": 1000000.00,
        "ratio": 74.07
      }
    ]
  },
  "timestamp": 1711267200000
}
```

---

## 4. 成本归集API

### 4.1 查询成本归集列表

**接口说明**: 分页查询成本归集记录

**请求URL**: `GET /api/v1/cost-collections`

**请求参数**:

| 参数名 | 类型 | 必填 | 说明 |
|-------|------|------|------|
| collectionNo | String | N | 归集单号 |
| collectionType | String | N | 归集类型 |
| periodYear | Integer | N | 会计年度 |
| periodMonth | Integer | N | 会计期间 |
| costCenterId | Long | N | 成本中心ID |
| status | String | N | 状态 |
| pageNum | Integer | N | 页码 |
| pageSize | Integer | N | 每页条数 |

**响应示例**:
```json
{
  "code": 200,
  "message": "success",
  "data": {
    "records": [
      {
        "id": 1,
        "collectionNo": "CC2026030001",
        "collectionType": "01",
        "collectionTypeName": "材料成本",
        "periodYear": 2026,
        "periodMonth": 3,
        "costCenterId": 1,
        "costCenterCode": "CC001",
        "costCenterName": "冲压车间",
        "totalAmount": 1000000.00,
        "currency": "CNY",
        "status": "20",
        "statusName": "已审核",
        "collectionDate": "2026-03-31",
        "createTime": "2026-03-31 10:00:00"
      }
    ],
    "total": 50,
    "size": 10,
    "current": 1,
    "pages": 5
  },
  "timestamp": 1711267200000
}
```

---

### 4.2 执行材料成本归集

**接口说明**: 执行材料成本自动归集

**请求URL**: `POST /api/v1/cost-collections/material`

**请求体**:
```json
{
  "periodYear": 2026,
  "periodMonth": 3,
  "costCenterIds": [1, 2, 3],
  "autoCreate": true
}
```

**响应示例**:
```json
{
  "code": 200,
  "message": "材料成本归集成功",
  "data": {
    "collectionId": 100,
    "collectionNo": "CC2026030001",
    "totalRecords": 150,
    "totalAmount": 5000000.00
  },
  "timestamp": 1711267200000
}
```

---

### 4.3 执行人工成本归集

**接口说明**: 执行人工成本自动归集

**请求URL**: `POST /api/v1/cost-collections/labor`

**请求体**:
```json
{
  "periodYear": 2026,
  "periodMonth": 3,
  "costCenterIds": [1, 2, 3]
}
```

**响应示例**:
```json
{
  "code": 200,
  "message": "人工成本归集成功",
  "data": {
    "collectionId": 101,
    "collectionNo": "CC2026030002",
    "totalRecords": 50,
    "totalAmount": 1000000.00
  },
  "timestamp": 1711267200000
}
```

---

### 4.4 查询成本归集明细

**接口说明**: 查询成本归集明细列表

**请求URL**: `GET /api/v1/cost-collections/{id}/details`

**响应示例**:
```json
{
  "code": 200,
  "message": "success",
  "data": {
    "records": [
      {
        "id": 1,
        "collectionId": 1,
        "lineNo": 1,
        "elementId": 1,
        "elementCode": "CE001",
        "elementName": "原材料成本",
        "materialId": 100,
        "materialCode": "MAT001",
        "materialName": "钢板Q235",
        "quantity": 1000.0000,
        "unit": "KG",
        "unitPrice": 5.0000,
        "amount": 5000.00,
        "sourceType": "01",
        "sourceNo": "MO2026030001"
      }
    ],
    "total": 150,
    "size": 10,
    "current": 1,
    "pages": 15
  },
  "timestamp": 1711267200000
}
```

---

## 5. 成本分配API

### 5.1 查询分配规则列表

**接口说明**: 查询成本分配规则列表

**请求URL**: `GET /api/v1/cost-allocation-rules`

**请求参数**:

| 参数名 | 类型 | 必填 | 说明 |
|-------|------|------|------|
| ruleCode | String | N | 规则编码 |
| ruleName | String | N | 规则名称 |
| ruleType | String | N | 规则类型 |
| status | Integer | N | 状态 |
| pageNum | Integer | N | 页码 |
| pageSize | Integer | N | 每页条数 |

**响应示例**:
```json
{
  "code": 200,
  "message": "success",
  "data": {
    "records": [
      {
        "id": 1,
        "ruleCode": "AR001",
        "ruleName": "动力车间成本分配",
        "ruleType": "01",
        "ruleTypeName": "辅助生产分配",
        "sourceCenterId": 10,
        "sourceCenterCode": "CC010",
        "sourceCenterName": "动力车间",
        "allocationBase": "01",
        "allocationBaseName": "产量",
        "allocationMethod": "01",
        "status": 1,
        "effectiveDate": "2026-01-01"
      }
    ],
    "total": 20,
    "size": 10,
    "current": 1,
    "pages": 2
  },
  "timestamp": 1711267200000
}
```

---

### 5.2 创建分配规则

**接口说明**: 创建成本分配规则

**请求URL**: `POST /api/v1/cost-allocation-rules`

**请求体**:
```json
{
  "ruleCode": "AR010",
  "ruleName": "维修车间成本分配",
  "ruleType": "01",
  "sourceCenterId": 12,
  "sourceElementId": 5,
  "allocationBase": "03",
  "allocationMethod": "01",
  "allocationOrder": 2,
  "effectiveDate": "2026-01-01",
  "details": [
    {
      "targetCenterId": 1,
      "targetElementId": 3,
      "allocationRatio": 30.0000
    },
    {
      "targetCenterId": 2,
      "targetElementId": 3,
      "allocationRatio": 40.0000
    },
    {
      "targetCenterId": 3,
      "targetElementId": 3,
      "allocationRatio": 30.0000
    }
  ]
}
```

**响应示例**:
```json
{
  "code": 200,
  "message": "创建成功",
  "data": {
    "id": 10
  },
  "timestamp": 1711267200000
}
```

---

### 5.3 执行成本分配

**接口说明**: 执行成本分配

**请求URL**: `POST /api/v1/cost-allocations/execute`

**请求体**:
```json
{
  "periodYear": 2026,
  "periodMonth": 3,
  "ruleIds": [1, 2, 3],
  "allocationOrder": "auto"
}
```

**响应示例**:
```json
{
  "code": 200,
  "message": "成本分配执行成功",
  "data": {
    "allocationNo": "CA2026030001",
    "totalAllocated": 500000.00,
    "details": [
      {
        "ruleId": 1,
        "ruleName": "动力车间成本分配",
        "sourceAmount": 200000.00,
        "allocatedAmount": 200000.00
      }
    ]
  },
  "timestamp": 1711267200000
}
```

---

## 6. 标准成本API

### 6.1 查询标准成本列表

**接口说明**: 分页查询标准成本列表

**请求URL**: `GET /api/v1/standard-costs`

**请求参数**:

| 参数名 | 类型 | 必填 | 说明 |
|-------|------|------|------|
| materialCode | String | N | 物料编码 |
| materialName | String | N | 物料名称 |
| status | String | N | 状态 |
| effectiveDateStart | String | N | 生效日期开始 |
| effectiveDateEnd | String | N | 生效日期结束 |
| pageNum | Integer | N | 页码 |
| pageSize | Integer | N | 每页条数 |

**响应示例**:
```json
{
  "code": 200,
  "message": "success",
  "data": {
    "records": [
      {
        "id": 1,
        "materialId": 100,
        "materialCode": "CAR001",
        "materialName": "轿车A型",
        "versionNo": "V1.0",
        "standardPrice": 80000.0000,
        "materialCost": 50000.00,
        "laborCost": 10000.00,
        "overheadCost": 15000.00,
        "totalCost": 75000.00,
        "effectiveDate": "2026-01-01",
        "status": "30",
        "statusName": "已生效"
      }
    ],
    "total": 100,
    "size": 10,
    "current": 1,
    "pages": 10
  },
  "timestamp": 1711267200000
}
```

---

### 6.2 创建标准成本

**接口说明**: 创建物料标准成本

**请求URL**: `POST /api/v1/standard-costs`

**请求体**:
```json
{
  "materialId": 100,
  "materialCode": "CAR001",
  "versionNo": "V2.0",
  "standardPrice": 85000.0000,
  "materialCost": 52000.00,
  "laborCost": 11000.00,
  "overheadCost": 16000.00,
  "effectiveDate": "2026-04-01",
  "remark": "2026年4月标准成本"
}
```

**响应示例**:
```json
{
  "code": 200,
  "message": "创建成功",
  "data": {
    "id": 10
  },
  "timestamp": 1711267200000
}
```

---

### 6.3 BOM成本滚算

**接口说明**: 执行BOM成本滚算

**请求URL**: `POST /api/v1/standard-costs/bom-rollup`

**请求体**:
```json
{
  "materialId": 100,
  "materialCode": "CAR001",
  "versionNo": "V2.0",
  "includeLabor": true,
  "includeOverhead": true,
  "bomVersion": "V1.0",
  "routingVersion": "V1.0"
}
```

**响应示例**:
```json
{
  "code": 200,
  "message": "BOM成本滚算成功",
  "data": {
    "materialId": 100,
    "materialCode": "CAR001",
    "totalCost": 75000.00,
    "materialCost": 50000.00,
    "laborCost": 10000.00,
    "overheadCost": 15000.00,
    "details": [
      {
        "lineNo": 1,
        "costType": "01",
        "costTypeName": "材料成本",
        "materialId": 200,
        "materialCode": "ENG001",
        "materialName": "发动机总成",
        "quantity": 1.0000,
        "unit": "台",
        "unitPrice": 20000.0000,
        "amount": 20000.00,
        "bomLevel": 1
      }
    ]
  },
  "timestamp": 1711267200000
}
```

---

### 6.4 标准成本审批

**接口说明**: 审批标准成本

**请求URL**: `POST /api/v1/standard-costs/{id}/approve`

**路径参数**:

| 参数名 | 类型 | 必填 | 说明 |
|-------|------|------|------|
| id | Long | Y | 标准成本ID |

**请求体**:
```json
{
  "approveResult": "pass",
  "approveOpinion": "审核通过"
}
```

**响应示例**:
```json
{
  "code": 200,
  "message": "审批成功",
  "timestamp": 1711267200000
}
```

---

### 6.5 查询标准工资率列表

**接口说明**: 查询标准工资率列表

**请求URL**: `GET /api/v1/standard-labor-rates`

**响应示例**:
```json
{
  "code": 200,
  "message": "success",
  "data": {
    "records": [
      {
        "id": 1,
        "rateCode": "LR001",
        "rateName": "焊工标准工资率",
        "workType": "焊接",
        "skillLevel": "高级",
        "costCenterId": 2,
        "standardRate": 80.0000,
        "effectiveDate": "2026-01-01",
        "status": 1
      }
    ],
    "total": 20,
    "size": 10,
    "current": 1,
    "pages": 2
  },
  "timestamp": 1711267200000
}
```

---

## 7. 成本核算API

### 7.1 创建成本核算单

**接口说明**: 创建成本核算单

**请求URL**: `POST /api/v1/cost-calculations`

**请求体**:
```json
{
  "calcType": "01",
  "periodYear": 2026,
  "periodMonth": 3,
  "calcDate": "2026-03-31",
  "remark": "2026年3月成本核算"
}
```

**响应示例**:
```json
{
  "code": 200,
  "message": "创建成功",
  "data": {
    "id": 100,
    "calcNo": "CA2026030001"
  },
  "timestamp": 1711267200000
}
```

---

### 7.2 执行成本核算

**接口说明**: 执行成本核算计算

**请求URL**: `POST /api/v1/cost-calculations/{id}/execute`

**路径参数**:

| 参数名 | 类型 | 必填 | 说明 |
|-------|------|------|------|
| id | Long | Y | 核算单ID |

**请求体**:
```json
{
  "calcSteps": ["collection", "allocation", "wip", "finish"],
  "autoApprove": false
}
```

**响应示例**:
```json
{
  "code": 200,
  "message": "成本核算执行成功",
  "data": {
    "calcNo": "CA2026030001",
    "status": "30",
    "totalMaterialCost": 5000000.00,
    "totalLaborCost": 1000000.00,
    "totalOverheadCost": 800000.00,
    "totalCost": 6800000.00,
    "wipCost": 500000.00,
    "finishCost": 6300000.00,
    "executeTime": "2026-03-31 15:00:00"
  },
  "timestamp": 1711267200000
}
```

---

### 7.3 查询成本核算结果

**接口说明**: 查询成本核算明细结果

**请求URL**: `GET /api/v1/cost-calculations/{id}/details`

**请求参数**:

| 参数名 | 类型 | 必填 | 说明 |
|-------|------|------|------|
| id | Long | Y | 核算单ID |
| materialCode | String | N | 物料编码 |
| costCenterId | Long | N | 成本中心ID |

**响应示例**:
```json
{
  "code": 200,
  "message": "success",
  "data": {
    "records": [
      {
        "id": 1,
        "calcId": 100,
        "lineNo": 1,
        "materialId": 100,
        "materialCode": "CAR001",
        "materialName": "轿车A型",
        "workOrderId": 1001,
        "workOrderNo": "MO2026030001",
        "costCenterId": 1,
        "finishQty": 100.0000,
        "wipQty": 10.0000,
        "equivalentQty": 105.0000,
        "materialCost": 50000.00,
        "laborCost": 10000.00,
        "overheadCost": 15000.00,
        "totalCost": 75000.00,
        "unitCost": 714.2857,
        "standardCost": 700.0000,
        "costVariance": 14.2857
      }
    ],
    "total": 50,
    "size": 10,
    "current": 1,
    "pages": 5
  },
  "timestamp": 1711267200000
}
```

---

### 7.4 成本核算审核

**接口说明**: 审核成本核算单

**请求URL**: `POST /api/v1/cost-calculations/{id}/approve`

**请求体**:
```json
{
  "approveResult": "pass",
  "approveOpinion": "核算数据准确，审核通过"
}
```

**响应示例**:
```json
{
  "code": 200,
  "message": "审核成功",
  "timestamp": 1711267200000
}
```

---

### 7.5 成本结转

**接口说明**: 执行成本结转

**请求URL**: `POST /api/v1/cost-calculations/{id}/transfer`

**请求体**:
```json
{
  "generateVoucher": true,
  "voucherDate": "2026-03-31"
}
```

**响应示例**:
```json
{
  "code": 200,
  "message": "成本结转成功",
  "data": {
    "voucherId": 10001,
    "voucherNo": "V2026030001",
    "transferAmount": 6300000.00
  },
  "timestamp": 1711267200000
}
```

---

## 8. 成本差异分析API

### 8.1 查询成本差异列表

**接口说明**: 查询成本差异分析列表

**请求URL**: `GET /api/v1/cost-variances`

**请求参数**:

| 参数名 | 类型 | 必填 | 说明 |
|-------|------|------|------|
| periodYear | Integer | Y | 会计年度 |
| periodMonth | Integer | Y | 会计期间 |
| materialCode | String | N | 物料编码 |
| varianceType | String | N | 差异类型 |
| costCenterId | Long | N | 成本中心ID |
| pageNum | Integer | N | 页码 |
| pageSize | Integer | N | 每页条数 |

**响应示例**:
```json
{
  "code": 200,
  "message": "success",
  "data": {
    "records": [
      {
        "id": 1,
        "periodYear": 2026,
        "periodMonth": 3,
        "materialId": 100,
        "materialCode": "CAR001",
        "materialName": "轿车A型",
        "varianceType": "01",
        "varianceTypeName": "材料价格差异",
        "standardAmount": 50000.00,
        "actualAmount": 52000.00,
        "varianceAmount": 2000.00,
        "varianceRate": 4.0000,
        "varianceReason": "原材料价格上涨",
        "status": "20"
      }
    ],
    "total": 30,
    "size": 10,
    "current": 1,
    "pages": 3
  },
  "timestamp": 1711267200000
}
```

---

### 8.2 成本差异汇总分析

**接口说明**: 成本差异汇总分析

**请求URL**: `GET /api/v1/cost-variances/summary`

**请求参数**:

| 参数名 | 类型 | 必填 | 说明 |
|-------|------|------|------|
| periodYear | Integer | Y | 会计年度 |
| periodMonth | Integer | Y | 会计期间 |
| groupBy | String | N | 分组维度(material/costCenter/type) |

**响应示例**:
```json
{
  "code": 200,
  "message": "success",
  "data": {
    "periodYear": 2026,
    "periodMonth": 3,
    "totalStandardAmount": 10000000.00,
    "totalActualAmount": 10200000.00,
    "totalVarianceAmount": 200000.00,
    "totalVarianceRate": 2.0000,
    "varianceByType": [
      {
        "varianceType": "01",
        "varianceTypeName": "材料价格差异",
        "varianceAmount": 100000.00,
        "varianceRate": 1.0000
      },
      {
        "varianceType": "02",
        "varianceTypeName": "材料数量差异",
        "varianceAmount": 50000.00,
        "varianceRate": 0.5000
      }
    ]
  },
  "timestamp": 1711267200000
}
```

---

## 9. 成本分析API

### 9.1 成本结构分析

**接口说明**: 成本结构分析

**请求URL**: `GET /api/v1/cost-analysis/structure`

**请求参数**:

| 参数名 | 类型 | 必填 | 说明 |
|-------|------|------|------|
| periodYear | Integer | Y | 会计年度 |
| periodMonth | Integer | Y | 会计期间 |
| analysisType | String | Y | 分析类型(element/center/product/behavior) |

**响应示例**:
```json
{
  "code": 200,
  "message": "success",
  "data": {
    "analysisType": "element",
    "periodYear": 2026,
    "periodMonth": 3,
    "totalCost": 6800000.00,
    "structure": [
      {
        "categoryCode": "01",
        "categoryName": "材料成本",
        "amount": 5000000.00,
        "ratio": 73.53
      },
      {
        "categoryCode": "02",
        "categoryName": "人工成本",
        "amount": 1000000.00,
        "ratio": 14.71
      },
      {
        "categoryCode": "03",
        "categoryName": "制造费用",
        "amount": 800000.00,
        "ratio": 11.76
      }
    ]
  },
  "timestamp": 1711267200000
}
```

---

### 9.2 成本趋势分析

**接口说明**: 成本趋势分析

**请求URL**: `GET /api/v1/cost-analysis/trend`

**请求参数**:

| 参数名 | 类型 | 必填 | 说明 |
|-------|------|------|------|
| startPeriodYear | Integer | Y | 开始年度 |
| startPeriodMonth | Integer | Y | 开始期间 |
| endPeriodYear | Integer | Y | 结束年度 |
| endPeriodMonth | Integer | Y | 结束期间 |
| dimension | String | N | 维度(total/material/labor/overhead) |

**响应示例**:
```json
{
  "code": 200,
  "message": "success",
  "data": {
    "dimension": "total",
    "trendData": [
      {
        "periodYear": 2026,
        "periodMonth": 1,
        "totalCost": 6500000.00,
        "materialCost": 4800000.00,
        "laborCost": 950000.00,
        "overheadCost": 750000.00
      },
      {
        "periodYear": 2026,
        "periodMonth": 2,
        "totalCost": 6700000.00,
        "materialCost": 4900000.00,
        "laborCost": 980000.00,
        "overheadCost": 820000.00
      }
    ]
  },
  "timestamp": 1711267200000
}
```

---

### 9.3 变动固定成本分析

**接口说明**: 变动固定成本分析

**请求URL**: `GET /api/v1/cost-analysis/behavior`

**请求参数**:

| 参数名 | 类型 | 必填 | 说明 |
|-------|------|------|------|
| periodYear | Integer | Y | 会计年度 |
| periodMonth | Integer | Y | 会计期间 |

**响应示例**:
```json
{
  "code": 200,
  "message": "success",
  "data": {
    "periodYear": 2026,
    "periodMonth": 3,
    "totalCost": 6800000.00,
    "variableCost": 5500000.00,
    "variableRatio": 80.88,
    "fixedCost": 1300000.00,
    "fixedRatio": 19.12,
    "breakEvenPoint": {
      "quantity": 500,
      "amount": 5000000.00
    },
    "safetyMargin": {
      "quantity": 200,
      "amount": 2000000.00,
      "ratio": 28.57
    }
  },
  "timestamp": 1711267200000
}
```

---

### 9.4 车间成本对比分析

**接口说明**: 车间成本对比分析

**请求URL**: `GET /api/v1/cost-analysis/workshop-compare`

**请求参数**:

| 参数名 | 类型 | 必填 | 说明 |
|-------|------|------|------|
| periodYear | Integer | Y | 会计年度 |
| periodMonth | Integer | Y | 会计期间 |
| costCenterIds | String | N | 成本中心ID列表(逗号分隔) |

**响应示例**:
```json
{
  "code": 200,
  "message": "success",
  "data": {
    "periodYear": 2026,
    "periodMonth": 3,
    "comparison": [
      {
        "costCenterId": 1,
        "costCenterCode": "CC001",
        "costCenterName": "冲压车间",
        "totalCost": 1500000.00,
        "unitCost": 150.00,
        "costByElement": {
          "material": 1200000.00,
          "labor": 150000.00,
          "overhead": 150000.00
        }
      },
      {
        "costCenterId": 2,
        "costCenterCode": "CC002",
        "costCenterName": "焊装车间",
        "totalCost": 1200000.00,
        "unitCost": 120.00,
        "costByElement": {
          "material": 800000.00,
          "labor": 200000.00,
          "overhead": 200000.00
        }
      }
    ]
  },
  "timestamp": 1711267200000
}
```

---

## 10. 利润分析API

### 10.1 边际贡献分析

**接口说明**: 边际贡献分析

**请求URL**: `GET /api/v1/profit-analysis/contribution-margin`

**请求参数**:

| 参数名 | 类型 | 必填 | 说明 |
|-------|------|------|------|
| periodYear | Integer | Y | 会计年度 |
| periodMonth | Integer | Y | 会计期间 |
| dimension | String | N | 维度(product/customer/vehicle) |

**响应示例**:
```json
{
  "code": 200,
  "message": "success",
  "data": {
    "periodYear": 2026,
    "periodMonth": 3,
    "totalRevenue": 10000000.00,
    "totalVariableCost": 5500000.00,
    "totalContributionMargin": 4500000.00,
    "contributionMarginRate": 45.00,
    "details": [
      {
        "materialId": 100,
        "materialCode": "CAR001",
        "materialName": "轿车A型",
        "revenue": 5000000.00,
        "variableCost": 2500000.00,
        "contributionMargin": 2500000.00,
        "contributionMarginRate": 50.00
      }
    ]
  },
  "timestamp": 1711267200000
}
```

---

### 10.2 产品利润分析

**接口说明**: 产品利润分析

**请求URL**: `GET /api/v1/profit-analysis/product-profit`

**请求参数**:

| 参数名 | 类型 | 必填 | 说明 |
|-------|------|------|------|
| periodYear | Integer | Y | 会计年度 |
| periodMonth | Integer | Y | 会计期间 |
| materialCode | String | N | 物料编码 |

**响应示例**:
```json
{
  "code": 200,
  "message": "success",
  "data": {
    "periodYear": 2026,
    "periodMonth": 3,
    "products": [
      {
        "materialId": 100,
        "materialCode": "CAR001",
        "materialName": "轿车A型",
        "salesQty": 100,
        "revenue": 8000000.00,
        "costOfSales": 6300000.00,
        "grossProfit": 1700000.00,
        "grossProfitRate": 21.25,
        "operatingProfit": 1200000.00,
        "operatingProfitRate": 15.00
      }
    ]
  },
  "timestamp": 1711267200000
}
```

---

### 10.3 盈利能力分析

**接口说明**: 企业盈利能力分析

**请求URL**: `GET /api/v1/profit-analysis/profitability`

**请求参数**:

| 参数名 | 类型 | 必填 | 说明 |
|-------|------|------|------|
| periodYear | Integer | Y | 会计年度 |
| periodMonth | Integer | Y | 会计期间 |

**响应示例**:
```json
{
  "code": 200,
  "message": "success",
  "data": {
    "periodYear": 2026,
    "periodMonth": 3,
    "revenue": 10000000.00,
    "costOfSales": 6800000.00,
    "grossProfit": 3200000.00,
    "grossProfitRate": 32.00,
    "operatingProfit": 2000000.00,
    "operatingProfitRate": 20.00,
    "netProfit": 1500000.00,
    "netProfitRate": 15.00,
    "roe": 18.00,
    "roa": 12.00
  },
  "timestamp": 1711267200000
}
```

---

## 11. 系统集成API

### 11.1 从财务系统获取制造费用

**接口说明**: 从财务系统获取制造费用数据

**请求URL**: `POST /api/v1/integration/fi/fetch-overhead`

**请求体**:
```json
{
  "periodYear": 2026,
  "periodMonth": 3,
  "costCenterIds": [1, 2, 3]
}
```

**响应示例**:
```json
{
  "code": 200,
  "message": "获取成功",
  "data": {
    "totalRecords": 50,
    "totalAmount": 800000.00,
    "fetchTime": "2026-03-31 10:00:00"
  },
  "timestamp": 1711267200000
}
```

---

### 11.2 向财务系统传递凭证

**接口说明**: 向财务系统传递成本凭证

**请求URL**: `POST /api/v1/integration/fi/send-voucher`

**请求体**:
```json
{
  "calcId": 100,
  "voucherDate": "2026-03-31",
  "voucherType": "cost_transfer"
}
```

**响应示例**:
```json
{
  "code": 200,
  "message": "传递成功",
  "data": {
    "voucherId": 10001,
    "voucherNo": "V2026030001",
    "fiVoucherId": "FI2026030001"
  },
  "timestamp": 1711267200000
}
```

---

### 11.3 从生产系统获取工单数据

**接口说明**: 从生产系统获取工单数据

**请求URL**: `POST /api/v1/integration/pm/fetch-workorders`

**请求体**:
```json
{
  "periodYear": 2026,
  "periodMonth": 3,
  "costCenterIds": [1, 2, 3]
}
```

**响应示例**:
```json
{
  "code": 200,
  "message": "获取成功",
  "data": {
    "totalOrders": 100,
    "totalFinishQty": 500,
    "totalWipQty": 50
  },
  "timestamp": 1711267200000
}
```

---

## 12. API权限控制

### 12.1 权限码定义

| 权限码 | 说明 |
|-------|------|
| co:costElement:list | 查询成本要素列表 |
| co:costElement:add | 新增成本要素 |
| co:costElement:edit | 编辑成本要素 |
| co:costElement:delete | 删除成本要素 |
| co:costCenter:list | 查询成本中心列表 |
| co:costCenter:add | 新增成本中心 |
| co:costCenter:edit | 编辑成本中心 |
| co:costCenter:delete | 删除成本中心 |
| co:costCollection:list | 查询成本归集列表 |
| co:costCollection:execute | 执行成本归集 |
| co:costAllocation:list | 查询成本分配列表 |
| co:costAllocation:execute | 执行成本分配 |
| co:standardCost:list | 查询标准成本列表 |
| co:standardCost:add | 新增标准成本 |
| co:standardCost:approve | 审批标准成本 |
| co:costCalculation:list | 查询成本核算列表 |
| co:costCalculation:execute | 执行成本核算 |
| co:costCalculation:approve | 审核成本核算 |
| co:costAnalysis:view | 查看成本分析 |
| co:profitAnalysis:view | 查看利润分析 |

---

## 13. 接口调用示例

### 13.1 成本核算完整流程示例

```bash
# 1. 创建成本核算单
curl -X POST "http://localhost:8080/api/v1/cost-calculations" \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer {token}" \
  -d '{
    "calcType": "01",
    "periodYear": 2026,
    "periodMonth": 3
  }'

# 2. 执行材料成本归集
curl -X POST "http://localhost:8080/api/v1/cost-collections/material" \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer {token}" \
  -d '{
    "periodYear": 2026,
    "periodMonth": 3
  }'

# 3. 执行成本分配
curl -X POST "http://localhost:8080/api/v1/cost-allocations/execute" \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer {token}" \
  -d '{
    "periodYear": 2026,
    "periodMonth": 3
  }'

# 4. 执行成本核算
curl -X POST "http://localhost:8080/api/v1/cost-calculations/{id}/execute" \
  -H "Authorization: Bearer {token}"

# 5. 审核成本核算
curl -X POST "http://localhost:8080/api/v1/cost-calculations/{id}/approve" \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer {token}" \
  -d '{
    "approveResult": "pass"
  }'

# 6. 成本结转
curl -X POST "http://localhost:8080/api/v1/cost-calculations/{id}/transfer" \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer {token}" \
  -d '{
    "generateVoucher": true
  }'
```

---

**文档修订历史**

| 版本 | 日期 | 修订人 | 修订内容 |
|-----|------|-------|---------|
| V1.0 | 2026-03-24 | 研发架构团队 | 初始版本 |