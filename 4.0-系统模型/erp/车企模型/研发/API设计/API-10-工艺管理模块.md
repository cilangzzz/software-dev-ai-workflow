# API-10 工艺管理模块API设计 (ENG)

## 文档信息

| 项目 | 内容 |
|------|------|
| 文档版本 | V1.0 |
| 创建日期 | 2026-03-24 |
| 模块名称 | 工艺管理 (Engineering Management) |
| 模块代码 | ENG |
| 技术栈 | Spring Boot 2.7 + MyBatis Plus |
| 接口规范 | RESTful API |

---

## 1. API设计原则

### 1.1 RESTful规范

| 规范项 | 说明 |
|--------|------|
| URL设计 | 使用名词复数形式，如 `/api/v1/products` |
| HTTP方法 | GET(查询)、POST(创建)、PUT(更新)、DELETE(删除) |
| 状态码 | 200(成功)、201(创建成功)、400(参数错误)、401(未授权)、403(禁止访问)、404(未找到)、500(服务器错误) |
| 版本控制 | URL中包含版本号 `/api/v1/` |
| 响应格式 | 统一JSON格式响应 |

### 1.2 统一响应格式

**成功响应:**

```json
{
  "code": 200,
  "message": "操作成功",
  "data": {},
  "timestamp": 1648123456789
}
```

**失败响应:**

```json
{
  "code": 400,
  "message": "参数错误",
  "data": null,
  "timestamp": 1648123456789
}
```

**分页响应:**

```json
{
  "code": 200,
  "message": "操作成功",
  "data": {
    "list": [],
    "total": 100,
    "pageNum": 1,
    "pageSize": 20,
    "pages": 5
  },
  "timestamp": 1648123456789
}
```

### 1.3 认证方式

- 认证方式: JWT Token
- 请求头: `Authorization: Bearer {token}`
- 租户标识: `X-Tenant-Id: {tenantId}`

---

## 2. 产品管理API

### 2.1 产品主数据API

#### 2.1.1 查询产品列表

**接口信息:**

| 项目 | 内容 |
|------|------|
| 接口路径 | GET /api/v1/eng/products |
| 接口描述 | 分页查询产品列表 |
| 权限标识 | eng:product:list |

**请求参数:**

| 参数名 | 类型 | 必填 | 说明 |
|--------|------|------|------|
| productCode | String | 否 | 产品编码(模糊查询) |
| productName | String | 否 | 产品名称(模糊查询) |
| categoryId | Long | 否 | 产品分类ID |
| productType | Integer | 否 | 产品类型 |
| status | Integer | 否 | 产品状态 |
| approveStatus | Integer | 否 | 审批状态 |
| pageNum | Integer | 否 | 页码，默认1 |
| pageSize | Integer | 否 | 每页数量，默认20 |
| orderBy | String | 否 | 排序字段 |
| orderDirection | String | 否 | 排序方向(ASC/DESC) |

**响应示例:**

```json
{
  "code": 200,
  "message": "操作成功",
  "data": {
    "list": [
      {
        "id": 1,
        "productCode": "PROD-2024-001",
        "productName": "车型A-标准版",
        "productNameEn": "Model A-Standard",
        "categoryId": 10,
        "categoryName": "整车",
        "model": "A-STD-2024",
        "barcode": "6901234567890",
        "unitId": 1,
        "unitName": "辆",
        "productType": 1,
        "productTypeName": "自制件",
        "status": 3,
        "statusName": "量产",
        "safetyStock": 100.0000,
        "minOrderQty": 10.0000,
        "approveStatus": 2,
        "approveStatusName": "已审",
        "effectiveDate": "2024-01-01",
        "expiryDate": null,
        "createTime": "2024-01-15 10:30:00",
        "createByName": "张三"
      }
    ],
    "total": 100,
    "pageNum": 1,
    "pageSize": 20,
    "pages": 5
  }
}
```

#### 2.1.2 查询产品详情

**接口信息:**

| 项目 | 内容 |
|------|------|
| 接口路径 | GET /api/v1/eng/products/{id} |
| 接口描述 | 根据ID查询产品详情 |
| 权限标识 | eng:product:query |

**路径参数:**

| 参数名 | 类型 | 必填 | 说明 |
|--------|------|------|------|
| id | Long | 是 | 产品ID |

**响应示例:**

```json
{
  "code": 200,
  "message": "操作成功",
  "data": {
    "id": 1,
    "productCode": "PROD-2024-001",
    "productName": "车型A-标准版",
    "productNameEn": "Model A-Standard",
    "categoryId": 10,
    "categoryName": "整车",
    "categoryPath": "汽车/乘用车/轿车/车型A",
    "model": "A-STD-2024",
    "barcode": "6901234567890",
    "unitId": 1,
    "unitName": "辆",
    "productType": 1,
    "productTypeName": "自制件",
    "status": 3,
    "statusName": "量产",
    "safetyStock": 100.0000,
    "minOrderQty": 10.0000,
    "approveStatus": 2,
    "approveStatusName": "已审",
    "effectiveDate": "2024-01-01",
    "expiryDate": null,
    "remark": "车型A标准版配置",
    "attributes": [
      {
        "attrName": "颜色",
        "attrValue": "珍珠白",
        "attrType": 1
      },
      {
        "attrName": "排量",
        "attrValue": "1.5T",
        "attrType": 1
      }
    ],
    "createTime": "2024-01-15 10:30:00",
    "createByName": "张三",
    "updateTime": "2024-02-20 14:20:00",
    "updateByName": "李四"
  }
}
```

#### 2.1.3 创建产品

**接口信息:**

| 项目 | 内容 |
|------|------|
| 接口路径 | POST /api/v1/eng/products |
| 接口描述 | 创建新产品 |
| 权限标识 | eng:product:create |

**请求体:**

```json
{
  "productCode": "PROD-2024-002",
  "productName": "车型A-豪华版",
  "productNameEn": "Model A-Luxury",
  "categoryId": 10,
  "model": "A-LUX-2024",
  "barcode": "6901234567891",
  "unitId": 1,
  "productType": 1,
  "status": 1,
  "safetyStock": 50.0000,
  "minOrderQty": 5.0000,
  "effectiveDate": "2024-04-01",
  "remark": "车型A豪华版配置",
  "attributes": [
    {
      "attrName": "颜色",
      "attrValue": "星空黑",
      "attrType": 1
    },
    {
      "attrName": "排量",
      "attrValue": "2.0T",
      "attrType": 1
    }
  ]
}
```

**响应示例:**

```json
{
  "code": 200,
  "message": "产品创建成功",
  "data": {
    "id": 2,
    "productCode": "PROD-2024-002"
  }
}
```

#### 2.1.4 更新产品

**接口信息:**

| 项目 | 内容 |
|------|------|
| 接口路径 | PUT /api/v1/eng/products/{id} |
| 接口描述 | 更新产品信息 |
| 权限标识 | eng:product:update |

**路径参数:**

| 参数名 | 类型 | 必填 | 说明 |
|--------|------|------|------|
| id | Long | 是 | 产品ID |

**请求体:**

```json
{
  "productName": "车型A-豪华版(改)",
  "productNameEn": "Model A-Luxury(Updated)",
  "categoryId": 10,
  "model": "A-LUX-2024-V2",
  "safetyStock": 80.0000,
  "minOrderQty": 8.0000,
  "remark": "车型A豪华版配置-更新",
  "attributes": [
    {
      "attrName": "颜色",
      "attrValue": "极光蓝",
      "attrType": 1
    }
  ]
}
```

**响应示例:**

```json
{
  "code": 200,
  "message": "产品更新成功",
  "data": null
}
```

#### 2.1.5 删除产品

**接口信息:**

| 项目 | 内容 |
|------|------|
| 接口路径 | DELETE /api/v1/eng/products/{id} |
| 接口描述 | 删除产品(逻辑删除) |
| 权限标识 | eng:product:delete |

**路径参数:**

| 参数名 | 类型 | 必填 | 说明 |
|--------|------|------|------|
| id | Long | 是 | 产品ID |

**响应示例:**

```json
{
  "code": 200,
  "message": "产品删除成功",
  "data": null
}
```

#### 2.1.6 提交产品审批

**接口信息:**

| 项目 | 内容 |
|------|------|
| 接口路径 | POST /api/v1/eng/products/{id}/submit |
| 接口描述 | 提交产品审批 |
| 权限标识 | eng:product:submit |

**响应示例:**

```json
{
  "code": 200,
  "message": "产品已提交审批",
  "data": null
}
```

#### 2.1.7 审批产品

**接口信息:**

| 项目 | 内容 |
|------|------|
| 接口路径 | POST /api/v1/eng/products/{id}/approve |
| 接口描述 | 审批产品 |
| 权限标识 | eng:product:approve |

**请求体:**

```json
{
  "approveResult": 1,
  "approveOpinion": "产品信息审核通过，可以发布使用"
}
```

**响应示例:**

```json
{
  "code": 200,
  "message": "审批成功",
  "data": null
}
```

#### 2.1.8 批量导入产品

**接口信息:**

| 项目 | 内容 |
|------|------|
| 接口路径 | POST /api/v1/eng/products/import |
| 接口描述 | 批量导入产品数据 |
| 权限标识 | eng:product:import |
| Content-Type | multipart/form-data |

**请求参数:**

| 参数名 | 类型 | 必填 | 说明 |
|--------|------|------|------|
| file | File | 是 | Excel文件(.xlsx) |

**响应示例:**

```json
{
  "code": 200,
  "message": "导入完成",
  "data": {
    "successCount": 95,
    "failCount": 5,
    "errorList": [
      {
        "row": 10,
        "productCode": "PROD-001",
        "errorMsg": "产品编码已存在"
      }
    ]
  }
}
```

#### 2.1.9 导出产品

**接口信息:**

| 项目 | 内容 |
|------|------|
| 接口路径 | GET /api/v1/eng/products/export |
| 接口描述 | 导出产品数据 |
| 权限标识 | eng:product:export |

**请求参数:**

| 参数名 | 类型 | 必填 | 说明 |
|--------|------|------|------|
| productCode | String | 否 | 产品编码 |
| productName | String | 否 | 产品名称 |
| categoryId | Long | 否 | 产品分类ID |
| status | Integer | 否 | 产品状态 |

**响应:** Excel文件下载

---

### 2.2 产品分类API

#### 2.2.1 查询分类树

**接口信息:**

| 项目 | 内容 |
|------|------|
| 接口路径 | GET /api/v1/eng/product-categories/tree |
| 接口描述 | 查询产品分类树 |
| 权限标识 | eng:category:list |

**响应示例:**

```json
{
  "code": 200,
  "message": "操作成功",
  "data": [
    {
      "id": 1,
      "categoryCode": "AUTO",
      "categoryName": "汽车",
      "parentId": null,
      "level": 1,
      "sortOrder": 1,
      "status": 1,
      "children": [
        {
          "id": 2,
          "categoryCode": "PASSENGER",
          "categoryName": "乘用车",
          "parentId": 1,
          "level": 2,
          "sortOrder": 1,
          "status": 1,
          "children": []
        }
      ]
    }
  ]
}
```

#### 2.2.2 创建分类

**接口信息:**

| 项目 | 内容 |
|------|------|
| 接口路径 | POST /api/v1/eng/product-categories |
| 接口描述 | 创建产品分类 |
| 权限标识 | eng:category:create |

**请求体:**

```json
{
  "categoryCode": "SEDAN",
  "categoryName": "轿车",
  "parentId": 2,
  "sortOrder": 1,
  "status": 1,
  "remark": "轿车产品分类"
}
```

**响应示例:**

```json
{
  "code": 200,
  "message": "分类创建成功",
  "data": {
    "id": 10,
    "categoryCode": "SEDAN"
  }
}
```

---

## 3. BOM管理API

### 3.1 BOM主数据API

#### 3.1.1 查询BOM列表

**接口信息:**

| 项目 | 内容 |
|------|------|
| 接口路径 | GET /api/v1/eng/boms |
| 接口描述 | 分页查询BOM列表 |
| 权限标识 | eng:bom:list |

**请求参数:**

| 参数名 | 类型 | 必填 | 说明 |
|--------|------|------|------|
| bomCode | String | 否 | BOM编码 |
| productId | Long | 否 | 产品ID |
| productCode | String | 否 | 产品编码 |
| productName | String | 否 | 产品名称 |
| bomType | Integer | 否 | BOM类型 |
| version | String | 否 | 版本号 |
| approveStatus | Integer | 否 | 审批状态 |
| pageNum | Integer | 否 | 页码 |
| pageSize | Integer | 否 | 每页数量 |

**响应示例:**

```json
{
  "code": 200,
  "message": "操作成功",
  "data": {
    "list": [
      {
        "id": 1,
        "bomCode": "BOM-2024-001",
        "productId": 1,
        "productCode": "PROD-2024-001",
        "productName": "车型A-标准版",
        "version": "V1.0",
        "bomType": 1,
        "bomTypeName": "标准BOM",
        "effectiveDate": "2024-01-01",
        "expiryDate": null,
        "approveStatus": 2,
        "approveStatusName": "已审",
        "syncStatus": 1,
        "syncStatusName": "已同步",
        "syncTime": "2024-01-15 11:00:00",
        "createTime": "2024-01-15 10:30:00",
        "createByName": "张三"
      }
    ],
    "total": 50,
    "pageNum": 1,
    "pageSize": 20,
    "pages": 3
  }
}
```

#### 3.1.2 查询BOM详情

**接口信息:**

| 项目 | 内容 |
|------|------|
| 接口路径 | GET /api/v1/eng/boms/{id} |
| 接口描述 | 查询BOM详情(含明细) |
| 权限标识 | eng:bom:query |

**响应示例:**

```json
{
  "code": 200,
  "message": "操作成功",
  "data": {
    "id": 1,
    "bomCode": "BOM-2024-001",
    "productId": 1,
    "productCode": "PROD-2024-001",
    "productName": "车型A-标准版",
    "version": "V1.0",
    "bomType": 1,
    "bomTypeName": "标准BOM",
    "effectiveDate": "2024-01-01",
    "expiryDate": null,
    "approveStatus": 2,
    "remark": "车型A标准版BOM",
    "items": [
      {
        "id": 1,
        "seqNo": 10,
        "materialId": 101,
        "materialCode": "MAT-ENGINE-001",
        "materialName": "发动机总成",
        "quantity": 1.000000,
        "lossRate": 0.00,
        "operationId": null,
        "altGroup": null,
        "priority": 1,
        "isFixed": 0,
        "validFlag": 1,
        "effectiveDate": null,
        "expiryDate": null
      },
      {
        "id": 2,
        "seqNo": 20,
        "materialId": 102,
        "materialCode": "MAT-TRANS-001",
        "materialName": "变速箱总成",
        "quantity": 1.000000,
        "lossRate": 0.00,
        "operationId": null,
        "altGroup": null,
        "priority": 1,
        "isFixed": 0,
        "validFlag": 1,
        "effectiveDate": null,
        "expiryDate": null
      }
    ],
    "createTime": "2024-01-15 10:30:00",
    "createByName": "张三"
  }
}
```

#### 3.1.3 创建BOM

**接口信息:**

| 项目 | 内容 |
|------|------|
| 接口路径 | POST /api/v1/eng/boms |
| 接口描述 | 创建BOM |
| 权限标识 | eng:bom:create |

**请求体:**

```json
{
  "productId": 1,
  "version": "V1.0",
  "bomType": 1,
  "effectiveDate": "2024-04-01",
  "remark": "新版本BOM",
  "items": [
    {
      "seqNo": 10,
      "materialId": 101,
      "quantity": 1.000000,
      "lossRate": 0.00,
      "isFixed": 0,
      "validFlag": 1
    },
    {
      "seqNo": 20,
      "materialId": 102,
      "quantity": 1.000000,
      "lossRate": 0.00,
      "isFixed": 0,
      "validFlag": 1
    }
  ]
}
```

**响应示例:**

```json
{
  "code": 200,
  "message": "BOM创建成功",
  "data": {
    "id": 2,
    "bomCode": "BOM-2024-002"
  }
}
```

#### 3.1.4 更新BOM

**接口信息:**

| 项目 | 内容 |
|------|------|
| 接口路径 | PUT /api/v1/eng/boms/{id} |
| 接口描述 | 更新BOM信息 |
| 权限标识 | eng:bom:update |

**请求体:**

```json
{
  "effectiveDate": "2024-05-01",
  "remark": "更新后的BOM",
  "items": [
    {
      "id": 1,
      "seqNo": 10,
      "materialId": 101,
      "quantity": 1.000000,
      "lossRate": 1.00,
      "isFixed": 0,
      "validFlag": 1
    }
  ]
}
```

**响应示例:**

```json
{
  "code": 200,
  "message": "BOM更新成功",
  "data": null
}
```

#### 3.1.5 删除BOM

**接口信息:**

| 项目 | 内容 |
|------|------|
| 接口路径 | DELETE /api/v1/eng/boms/{id} |
| 接口描述 | 删除BOM |
| 权限标识 | eng:bom:delete |

**响应示例:**

```json
{
  "code": 200,
  "message": "BOM删除成功",
  "data": null
}
```

#### 3.1.6 BOM展开查询

**接口信息:**

| 项目 | 内容 |
|------|------|
| 接口路径 | GET /api/v1/eng/boms/{id}/expand |
| 接口描述 | BOM展开查询 |
| 权限标识 | eng:bom:query |

**请求参数:**

| 参数名 | 类型 | 必填 | 说明 |
|--------|------|------|------|
| expandType | String | 是 | 展开类型: single(单级)/multi(多级)/end(末级) |

**响应示例:**

```json
{
  "code": 200,
  "message": "操作成功",
  "data": {
    "expandType": "multi",
    "totalMaterials": 15,
    "totalQuantity": 25.500000,
    "tree": [
      {
        "level": 1,
        "materialId": 101,
        "materialCode": "MAT-ENGINE-001",
        "materialName": "发动机总成",
        "quantity": 1.000000,
        "accumQty": 1.000000,
        "children": [
          {
            "level": 2,
            "materialId": 201,
            "materialCode": "MAT-ENG-BLOCK",
            "materialName": "发动机缸体",
            "quantity": 1.000000,
            "accumQty": 1.000000,
            "children": []
          }
        ]
      }
    ]
  }
}
```

#### 3.1.7 BOM反查

**接口信息:**

| 项目 | 内容 |
|------|------|
| 接口路径 | GET /api/v1/eng/boms/where-used |
| 接口描述 | 查询物料被使用的BOM |
| 权限标识 | eng:bom:query |

**请求参数:**

| 参数名 | 类型 | 必填 | 说明 |
|--------|------|------|------|
| materialId | Long | 是 | 物料ID |
| level | String | 否 | 查询层级: single(单级)/multi(多级) |

**响应示例:**

```json
{
  "code": 200,
  "message": "操作成功",
  "data": {
    "materialId": 101,
    "materialCode": "MAT-ENGINE-001",
    "materialName": "发动机总成",
    "usedIn": [
      {
        "bomId": 1,
        "bomCode": "BOM-2024-001",
        "productName": "车型A-标准版",
        "quantity": 1.000000,
        "level": 1
      },
      {
        "bomId": 3,
        "bomCode": "BOM-2024-003",
        "productName": "车型B-豪华版",
        "quantity": 1.000000,
        "level": 1
      }
    ]
  }
}
```

#### 3.1.8 BOM版本对比

**接口信息:**

| 项目 | 内容 |
|------|------|
| 接口路径 | GET /api/v1/eng/boms/compare |
| 接口描述 | 对比两个BOM版本 |
| 权限标识 | eng:bom:query |

**请求参数:**

| 参数名 | 类型 | 必填 | 说明 |
|--------|------|------|------|
| bomId1 | Long | 是 | BOM版本1 ID |
| bomId2 | Long | 是 | BOM版本2 ID |

**响应示例:**

```json
{
  "code": 200,
  "message": "操作成功",
  "data": {
    "bom1": {
      "id": 1,
      "version": "V1.0"
    },
    "bom2": {
      "id": 2,
      "version": "V2.0"
    },
    "differences": [
      {
        "type": "MODIFIED",
        "materialCode": "MAT-TRANS-001",
        "materialName": "变速箱总成",
        "bom1Qty": 1.000000,
        "bom2Qty": 1.000000,
        "bom1LossRate": 0.00,
        "bom2LossRate": 2.00
      },
      {
        "type": "ADDED",
        "materialCode": "MAT-NEW-001",
        "materialName": "新增零件",
        "bom1Qty": null,
        "bom2Qty": 2.000000
      },
      {
        "type": "DELETED",
        "materialCode": "MAT-OLD-001",
        "materialName": "删除零件",
        "bom1Qty": 1.000000,
        "bom2Qty": null
      }
    ]
  }
}
```

#### 3.1.9 BOM审批

**接口信息:**

| 项目 | 内容 |
|------|------|
| 接口路径 | POST /api/v1/eng/boms/{id}/approve |
| 接口描述 | 审批BOM |
| 权限标识 | eng:bom:approve |

**请求体:**

```json
{
  "approveResult": 1,
  "approveOpinion": "BOM结构正确，审批通过"
}
```

**响应示例:**

```json
{
  "code": 200,
  "message": "审批成功",
  "data": null
}
```

---

### 3.2 替代物料API

#### 3.2.1 查询替代物料

**接口信息:**

| 项目 | 内容 |
|------|------|
| 接口路径 | GET /api/v1/eng/bom-items/{id}/alternatives |
| 接口描述 | 查询BOM明细的替代物料 |
| 权限标识 | eng:bom:query |

**响应示例:**

```json
{
  "code": 200,
  "message": "操作成功",
  "data": [
    {
      "id": 1,
      "mainMaterialId": 101,
      "mainMaterialCode": "MAT-ENGINE-001",
      "altMaterialId": 102,
      "altMaterialCode": "MAT-ENGINE-002",
      "altMaterialName": "发动机总成(替代)",
      "altRatio": 100.00,
      "priority": 1,
      "condition": "库存不足时启用",
      "status": 1
    }
  ]
}
```

#### 3.2.2 添加替代物料

**接口信息:**

| 项目 | 内容 |
|------|------|
| 接口路径 | POST /api/v1/eng/bom-items/{id}/alternatives |
| 接口描述 | 添加替代物料 |
| 权限标识 | eng:bom:update |

**请求体:**

```json
{
  "altMaterialId": 102,
  "altRatio": 100.00,
  "priority": 2,
  "condition": "主物料缺货时使用"
}
```

**响应示例:**

```json
{
  "code": 200,
  "message": "替代物料添加成功",
  "data": {
    "id": 2
  }
}
```

---

## 4. 工艺路线API

### 4.1 工序API

#### 4.1.1 查询工序列表

**接口信息:**

| 项目 | 内容 |
|------|------|
| 接口路径 | GET /api/v1/eng/operations |
| 接口描述 | 分页查询工序列表 |
| 权限标识 | eng:operation:list |

**请求参数:**

| 参数名 | 类型 | 必填 | 说明 |
|--------|------|------|------|
| operationCode | String | 否 | 工序编码 |
| operationName | String | 否 | 工序名称 |
| operationType | Integer | 否 | 工序类型 |
| workCenterId | Long | 否 | 工作中心ID |
| status | Integer | 否 | 状态 |
| pageNum | Integer | 否 | 页码 |
| pageSize | Integer | 否 | 每页数量 |

**响应示例:**

```json
{
  "code": 200,
  "message": "操作成功",
  "data": {
    "list": [
      {
        "id": 1,
        "operationCode": "OP-001",
        "operationName": "底盘装配",
        "operationType": 2,
        "operationTypeName": "装配",
        "workCenterId": 10,
        "workCenterName": "装配线1",
        "stdTime": 120.00,
        "setupTime": 15.00,
        "waitTime": 5.00,
        "status": 1,
        "statusName": "启用",
        "createTime": "2024-01-15 10:30:00"
      }
    ],
    "total": 50,
    "pageNum": 1,
    "pageSize": 20,
    "pages": 3
  }
}
```

#### 4.1.2 创建工序

**接口信息:**

| 项目 | 内容 |
|------|------|
| 接口路径 | POST /api/v1/eng/operations |
| 接口描述 | 创建工序 |
| 权限标识 | eng:operation:create |

**请求体:**

```json
{
  "operationCode": "OP-002",
  "operationName": "车身焊接",
  "operationType": 1,
  "workCenterId": 20,
  "stdTime": 90.00,
  "setupTime": 20.00,
  "waitTime": 10.00,
  "skillRequirement": "中级焊工证",
  "status": 1,
  "remark": "车身点焊工序",
  "resources": [
    {
      "resourceType": 1,
      "resourceId": 101,
      "quantity": 2,
      "isRequired": 1
    },
    {
      "resourceType": 3,
      "resourceId": 201,
      "quantity": 1,
      "isRequired": 1
    }
  ]
}
```

**响应示例:**

```json
{
  "code": 200,
  "message": "工序创建成功",
  "data": {
    "id": 2
  }
}
```

#### 4.1.3 配置工序资源

**接口信息:**

| 项目 | 内容 |
|------|------|
| 接口路径 | POST /api/v1/eng/operations/{id}/resources |
| 接口描述 | 配置工序所需资源 |
| 权限标识 | eng:operation:update |

**请求体:**

```json
{
  "resources": [
    {
      "resourceType": 1,
      "resourceId": 101,
      "quantity": 2,
      "isRequired": 1
    }
  ]
}
```

**响应示例:**

```json
{
  "code": 200,
  "message": "资源配置成功",
  "data": null
}
```

---

### 4.2 工艺路线API

#### 4.2.1 查询工艺路线列表

**接口信息:**

| 项目 | 内容 |
|------|------|
| 接口路径 | GET /api/v1/eng/routes |
| 接口描述 | 分页查询工艺路线列表 |
| 权限标识 | eng:route:list |

**请求参数:**

| 参数名 | 类型 | 必填 | 说明 |
|--------|------|------|------|
| routeCode | String | 否 | 路线编码 |
| routeName | String | 否 | 路线名称 |
| productId | Long | 否 | 产品ID |
| version | String | 否 | 版本号 |
| approveStatus | Integer | 否 | 审批状态 |
| pageNum | Integer | 否 | 页码 |
| pageSize | Integer | 否 | 每页数量 |

**响应示例:**

```json
{
  "code": 200,
  "message": "操作成功",
  "data": {
    "list": [
      {
        "id": 1,
        "routeCode": "RT-2024-001",
        "routeName": "车型A装配工艺",
        "productId": 1,
        "productCode": "PROD-2024-001",
        "productName": "车型A-标准版",
        "version": "V1.0",
        "isDefault": 1,
        "effectiveDate": "2024-01-01",
        "approveStatus": 2,
        "approveStatusName": "已审",
        "syncStatus": 1,
        "syncStatusName": "已同步",
        "createTime": "2024-01-15 10:30:00"
      }
    ],
    "total": 30,
    "pageNum": 1,
    "pageSize": 20,
    "pages": 2
  }
}
```

#### 4.2.2 查询工艺路线详情

**接口信息:**

| 项目 | 内容 |
|------|------|
| 接口路径 | GET /api/v1/eng/routes/{id} |
| 接口描述 | 查询工艺路线详情 |
| 权限标识 | eng:route:query |

**响应示例:**

```json
{
  "code": 200,
  "message": "操作成功",
  "data": {
    "id": 1,
    "routeCode": "RT-2024-001",
    "routeName": "车型A装配工艺",
    "productId": 1,
    "productCode": "PROD-2024-001",
    "productName": "车型A-标准版",
    "version": "V1.0",
    "isDefault": 1,
    "effectiveDate": "2024-01-01",
    "expiryDate": null,
    "approveStatus": 2,
    "remark": "车型A标准装配工艺",
    "totalStdTime": 480.00,
    "totalSetupTime": 45.00,
    "items": [
      {
        "id": 1,
        "seqNo": 10,
        "operationId": 1,
        "operationCode": "OP-001",
        "operationName": "底盘装配",
        "workCenterId": 10,
        "workCenterName": "装配线1",
        "stdTime": 120.00,
        "setupTime": 15.00,
        "preOperationId": null,
        "nextOperationId": 2,
        "isParallel": 0,
        "isKeyProcess": 1,
        "isReportPoint": 1,
        "isInspect": 1
      },
      {
        "id": 2,
        "seqNo": 20,
        "operationId": 2,
        "operationCode": "OP-002",
        "operationName": "车身装配",
        "workCenterId": 10,
        "workCenterName": "装配线1",
        "stdTime": 180.00,
        "setupTime": 15.00,
        "preOperationId": 1,
        "nextOperationId": 3,
        "isParallel": 0,
        "isKeyProcess": 1,
        "isReportPoint": 1,
        "isInspect": 1
      }
    ],
    "createTime": "2024-01-15 10:30:00",
    "createByName": "张三"
  }
}
```

#### 4.2.3 创建工艺路线

**接口信息:**

| 项目 | 内容 |
|------|------|
| 接口路径 | POST /api/v1/eng/routes |
| 接口描述 | 创建工艺路线 |
| 权限标识 | eng:route:create |

**请求体:**

```json
{
  "routeName": "车型A装配工艺V2",
  "productId": 1,
  "version": "V2.0",
  "isDefault": 0,
  "effectiveDate": "2024-04-01",
  "remark": "优化后的装配工艺",
  "items": [
    {
      "seqNo": 10,
      "operationId": 1,
      "workCenterId": 10,
      "stdTime": 120.00,
      "setupTime": 15.00,
      "isParallel": 0,
      "isKeyProcess": 1,
      "isReportPoint": 1,
      "isInspect": 1
    },
    {
      "seqNo": 20,
      "operationId": 2,
      "workCenterId": 10,
      "stdTime": 180.00,
      "setupTime": 15.00,
      "isParallel": 0,
      "isKeyProcess": 1,
      "isReportPoint": 1,
      "isInspect": 1
    }
  ]
}
```

**响应示例:**

```json
{
  "code": 200,
  "message": "工艺路线创建成功",
  "data": {
    "id": 2,
    "routeCode": "RT-2024-002"
  }
}
```

#### 4.2.4 更新工艺路线

**接口信息:**

| 项目 | 内容 |
|------|------|
| 接口路径 | PUT /api/v1/eng/routes/{id} |
| 接口描述 | 更新工艺路线 |
| 权限标识 | eng:route:update |

**请求体:**

```json
{
  "routeName": "车型A装配工艺(修改)",
  "effectiveDate": "2024-05-01",
  "remark": "再次优化",
  "items": [
    {
      "id": 1,
      "seqNo": 10,
      "operationId": 1,
      "workCenterId": 10,
      "stdTime": 100.00,
      "setupTime": 10.00,
      "isKeyProcess": 1,
      "isReportPoint": 1,
      "isInspect": 1
    }
  ]
}
```

**响应示例:**

```json
{
  "code": 200,
  "message": "工艺路线更新成功",
  "data": null
}
```

#### 4.2.5 删除工艺路线

**接口信息:**

| 项目 | 内容 |
|------|------|
| 接口路径 | DELETE /api/v1/eng/routes/{id} |
| 接口描述 | 删除工艺路线 |
| 权限标识 | eng:route:delete |

**响应示例:**

```json
{
  "code": 200,
  "message": "工艺路线删除成功",
  "data": null
}
```

#### 4.2.6 工艺路线审批

**接口信息:**

| 项目 | 内容 |
|------|------|
| 接口路径 | POST /api/v1/eng/routes/{id}/approve |
| 接口描述 | 审批工艺路线 |
| 权限标识 | eng:route:approve |

**请求体:**

```json
{
  "approveResult": 1,
  "approveOpinion": "工艺路线正确，审批通过"
}
```

**响应示例:**

```json
{
  "code": 200,
  "message": "审批成功",
  "data": null
}
```

#### 4.2.7 复制工艺路线

**接口信息:**

| 项目 | 内容 |
|------|------|
| 接口路径 | POST /api/v1/eng/routes/{id}/copy |
| 接口描述 | 复制工艺路线 |
| 权限标识 | eng:route:create |

**请求体:**

```json
{
  "routeName": "车型B装配工艺",
  "productId": 2
}
```

**响应示例:**

```json
{
  "code": 200,
  "message": "复制成功",
  "data": {
    "id": 3,
    "routeCode": "RT-2024-003"
  }
}
```

---

## 5. 工程变更API

### 5.1 ECR API

#### 5.1.1 查询ECR列表

**接口信息:**

| 项目 | 内容 |
|------|------|
| 接口路径 | GET /api/v1/eng/ecrs |
| 接口描述 | 分页查询ECR列表 |
| 权限标识 | eng:ecr:list |

**请求参数:**

| 参数名 | 类型 | 必填 | 说明 |
|--------|------|------|------|
| ecrCode | String | 否 | ECR编码 |
| ecrName | String | 否 | ECR名称 |
| changeType | Integer | 否 | 变更类型 |
| urgency | Integer | 否 | 紧急程度 |
| status | Integer | 否 | 状态 |
| applicantId | Long | 否 | 申请人ID |
| pageNum | Integer | 否 | 页码 |
| pageSize | Integer | 否 | 每页数量 |

**响应示例:**

```json
{
  "code": 200,
  "message": "操作成功",
  "data": {
    "list": [
      {
        "id": 1,
        "ecrCode": "ECR-20240315-001",
        "ecrName": "发动机支架设计变更",
        "changeType": 1,
        "changeTypeName": "产品设计",
        "changeReason": "提高强度",
        "urgency": 2,
        "urgencyName": "紧急",
        "applicantId": 100,
        "applicantName": "张三",
        "applyDate": "2024-03-15",
        "status": 2,
        "statusName": "待审",
        "createTime": "2024-03-15 10:30:00"
      }
    ],
    "total": 20,
    "pageNum": 1,
    "pageSize": 20,
    "pages": 1
  }
}
```

#### 5.1.2 查询ECR详情

**接口信息:**

| 项目 | 内容 |
|------|------|
| 接口路径 | GET /api/v1/eng/ecrs/{id} |
| 接口描述 | 查询ECR详情 |
| 权限标识 | eng:ecr:query |

**响应示例:**

```json
{
  "code": 200,
  "message": "操作成功",
  "data": {
    "id": 1,
    "ecrCode": "ECR-20240315-001",
    "ecrName": "发动机支架设计变更",
    "changeType": 1,
    "changeTypeName": "产品设计",
    "changeReason": "原支架强度不足，需要增加厚度",
    "changeContent": "将发动机支架厚度从3mm增加到5mm，同时优化结构设计...",
    "impactScope": "涉及产品:车型A、车型B",
    "urgency": 2,
    "urgencyName": "紧急",
    "applicantId": 100,
    "applicantName": "张三",
    "applyDate": "2024-03-15",
    "status": 2,
    "statusName": "待审",
    "remark": "请尽快处理",
    "relations": [
      {
        "objectType": 1,
        "objectId": 1,
        "objectCode": "PROD-2024-001",
        "objectName": "车型A-标准版"
      }
    ],
    "impacts": [
      {
        "impactType": 2,
        "objectId": 1,
        "objectCode": "BOM-2024-001",
        "objectName": "车型A BOM",
        "impactDesc": "需更换支架物料"
      }
    ],
    "createTime": "2024-03-15 10:30:00",
    "createByName": "张三"
  }
}
```

#### 5.1.3 创建ECR

**接口信息:**

| 项目 | 内容 |
|------|------|
| 接口路径 | POST /api/v1/eng/ecrs |
| 接口描述 | 创建工程变更请求 |
| 权限标识 | eng:ecr:create |

**请求体:**

```json
{
  "ecrName": "座椅固定螺栓变更",
  "changeType": 2,
  "changeReason": "供应商停产，需更换替代件",
  "changeContent": "将座椅固定螺栓从A供应商更换为B供应商同等规格产品",
  "impactScope": "涉及所有车型",
  "urgency": 3,
  "remark": "急需处理",
  "relations": [
    {
      "objectType": 1,
      "objectId": 1,
      "objectCode": "PROD-2024-001",
      "objectName": "车型A-标准版"
    },
    {
      "objectType": 2,
      "objectId": 1,
      "objectCode": "BOM-2024-001",
      "objectName": "车型A BOM"
    }
  ]
}
```

**响应示例:**

```json
{
  "code": 200,
  "message": "ECR创建成功",
  "data": {
    "id": 2,
    "ecrCode": "ECR-20240315-002"
  }
}
```

#### 5.1.4 提交ECR审批

**接口信息:**

| 项目 | 内容 |
|------|------|
| 接口路径 | POST /api/v1/eng/ecrs/{id}/submit |
| 接口描述 | 提交ECR审批 |
| 权限标识 | eng:ecr:submit |

**响应示例:**

```json
{
  "code": 200,
  "message": "ECR已提交审批",
  "data": null
}
```

#### 5.1.5 ECR影响分析

**接口信息:**

| 项目 | 内容 |
|------|------|
| 接口路径 | GET /api/v1/eng/ecrs/{id}/impact-analysis |
| 接口描述 | 分析ECR影响范围 |
| 权限标识 | eng:ecr:query |

**响应示例:**

```json
{
  "code": 200,
  "message": "操作成功",
  "data": {
    "ecrId": 1,
    "analysisTime": "2024-03-15 11:00:00",
    "impacts": {
      "products": [
        {
          "id": 1,
          "code": "PROD-2024-001",
          "name": "车型A-标准版"
        }
      ],
      "boms": [
        {
          "id": 1,
          "code": "BOM-2024-001",
          "name": "车型A BOM",
          "version": "V1.0"
        }
      ],
      "routes": [
        {
          "id": 1,
          "code": "RT-2024-001",
          "name": "车型A装配工艺"
        }
      ],
      "orders": [
        {
          "id": 1001,
          "code": "PO-2024-001",
          "type": "生产订单",
          "status": "生产中"
        }
      ],
      "inventory": [
        {
          "materialId": 101,
          "materialCode": "MAT-001",
          "materialName": "发动机支架",
          "quantity": 50.0000
        }
      ]
    },
    "reportUrl": "/api/v1/eng/ecrs/1/impact-report"
  }
}
```

#### 5.1.6 审批ECR

**接口信息:**

| 项目 | 内容 |
|------|------|
| 接口路径 | POST /api/v1/eng/ecrs/{id}/approve |
| 接口描述 | 审批ECR |
| 权限标识 | eng:ecr:approve |

**请求体:**

```json
{
  "approveResult": 1,
  "approveOpinion": "变更合理，批准执行"
}
```

**响应示例:**

```json
{
  "code": 200,
  "message": "审批成功",
  "data": null
}
```

---

### 5.2 ECO API

#### 5.2.1 查询ECO列表

**接口信息:**

| 项目 | 内容 |
|------|------|
| 接口路径 | GET /api/v1/eng/ecos |
| 接口描述 | 分页查询ECO列表 |
| 权限标识 | eng:eco:list |

**请求参数:**

| 参数名 | 类型 | 必填 | 说明 |
|--------|------|------|------|
| ecoCode | String | 否 | ECO编码 |
| ecrId | Long | 否 | 关联ECR ID |
| status | Integer | 否 | 状态 |
| ownerId | Long | 否 | 责任人ID |
| pageNum | Integer | 否 | 页码 |
| pageSize | Integer | 否 | 每页数量 |

**响应示例:**

```json
{
  "code": 200,
  "message": "操作成功",
  "data": {
    "list": [
      {
        "id": 1,
        "ecoCode": "ECO-20240316-001",
        "ecoName": "发动机支架变更执行",
        "ecrId": 1,
        "ecrCode": "ECR-20240315-001",
        "planCompleteDate": "2024-03-20",
        "actualCompleteDate": null,
        "ownerId": 101,
        "ownerName": "李四",
        "status": 2,
        "statusName": "执行中",
        "syncStatus": 0,
        "syncStatusName": "未同步",
        "createTime": "2024-03-16 09:00:00"
      }
    ],
    "total": 10,
    "pageNum": 1,
    "pageSize": 20,
    "pages": 1
  }
}
```

#### 5.2.2 创建ECO

**接口信息:**

| 项目 | 内容 |
|------|------|
| 接口路径 | POST /api/v1/eng/ecos |
| 接口描述 | 创建工程变更指令 |
| 权限标识 | eng:eco:create |

**请求体:**

```json
{
  "ecoName": "座椅螺栓变更执行",
  "ecrId": 2,
  "executionPlan": "1. 更新BOM物料\n2. 通知采购部门\n3. 更新工艺路线\n4. 同步到MES",
  "planCompleteDate": "2024-03-25",
  "ownerId": 101,
  "remark": "优先处理"
}
```

**响应示例:**

```json
{
  "code": 200,
  "message": "ECO创建成功",
  "data": {
    "id": 2,
    "ecoCode": "ECO-20240316-002"
  }
}
```

#### 5.2.3 执行ECO

**接口信息:**

| 项目 | 内容 |
|------|------|
| 接口路径 | POST /api/v1/eng/ecos/{id}/execute |
| 接口描述 | 执行ECO变更操作 |
| 权限标识 | eng:eco:execute |

**请求体:**

```json
{
  "actionType": 1,
  "actionDesc": "更新BOM物料",
  "targetId": 1,
  "changes": {
    "materialId": 102,
    "quantity": 4.000000
  }
}
```

**响应示例:**

```json
{
  "code": 200,
  "message": "执行成功",
  "data": null
}
```

#### 5.2.4 查询ECO进度

**接口信息:**

| 项目 | 内容 |
|------|------|
| 接口路径 | GET /api/v1/eng/ecos/{id}/progress |
| 接口描述 | 查询ECO执行进度 |
| 权限标识 | eng:eco:query |

**响应示例:**

```json
{
  "code": 200,
  "message": "操作成功",
  "data": {
    "ecoId": 1,
    "status": 2,
    "statusName": "执行中",
    "progress": 60,
    "planCompleteDate": "2024-03-20",
    "remainingDays": 2,
    "executions": [
      {
        "seqNo": 1,
        "actionType": 1,
        "actionDesc": "更新BOM物料",
        "status": 1,
        "executeTime": "2024-03-16 10:00:00",
        "executorName": "李四"
      },
      {
        "seqNo": 2,
        "actionType": 3,
        "actionDesc": "通知相关部门",
        "status": 1,
        "executeTime": "2024-03-16 11:00:00",
        "executorName": "李四"
      },
      {
        "seqNo": 3,
        "actionType": 2,
        "actionDesc": "更新工艺路线",
        "status": 2,
        "executeTime": null,
        "executorName": null
      }
    ]
  }
}
```

#### 5.2.5 关闭ECO

**接口信息:**

| 项目 | 内容 |
|------|------|
| 接口路径 | POST /api/v1/eng/ecos/{id}/close |
| 接口描述 | 关闭ECO |
| 权限标识 | eng:eco:close |

**响应示例:**

```json
{
  "code": 200,
  "message": "ECO已关闭，变更已同步到MES",
  "data": {
    "syncStatus": 1,
    "syncTime": "2024-03-20 16:00:00"
  }
}
```

---

## 6. MES集成API

### 6.1 数据同步API

#### 6.1.1 同步BOM到MES

**接口信息:**

| 项目 | 内容 |
|------|------|
| 接口路径 | POST /api/v1/eng/sync/bom/{id} |
| 接口描述 | 手动同步BOM到MES |
| 权限标识 | eng:sync:bom |

**响应示例:**

```json
{
  "code": 200,
  "message": "同步成功",
  "data": {
    "bomId": 1,
    "bomCode": "BOM-2024-001",
    "syncStatus": 1,
    "syncTime": "2024-03-20 16:00:00"
  }
}
```

#### 6.1.2 同步工艺路线到MES

**接口信息:**

| 项目 | 内容 |
|------|------|
| 接口路径 | POST /api/v1/eng/sync/route/{id} |
| 接口描述 | 手动同步工艺路线到MES |
| 权限标识 | eng:sync:route |

**响应示例:**

```json
{
  "code": 200,
  "message": "同步成功",
  "data": {
    "routeId": 1,
    "routeCode": "RT-2024-001",
    "syncStatus": 1,
    "syncTime": "2024-03-20 16:00:00"
  }
}
```

#### 6.1.3 查询同步日志

**接口信息:**

| 项目 | 内容 |
|------|------|
| 接口路径 | GET /api/v1/eng/sync/logs |
| 接口描述 | 查询MES同步日志 |
| 权限标识 | eng:sync:log |

**请求参数:**

| 参数名 | 类型 | 必填 | 说明 |
|--------|------|------|------|
| syncType | Integer | 否 | 同步类型 |
| syncStatus | Integer | 否 | 同步状态 |
| startTime | String | 否 | 开始时间 |
| endTime | String | 否 | 结束时间 |
| pageNum | Integer | 否 | 页码 |
| pageSize | Integer | 否 | 每页数量 |

**响应示例:**

```json
{
  "code": 200,
  "message": "操作成功",
  "data": {
    "list": [
      {
        "id": 1,
        "syncType": 2,
        "syncTypeName": "BOM",
        "businessId": 1,
        "businessCode": "BOM-2024-001",
        "syncDirection": 1,
        "syncDirectionName": "ERP到MES",
        "syncStatus": 1,
        "syncStatusName": "成功",
        "syncTime": "2024-03-20 16:00:00"
      }
    ],
    "total": 50,
    "pageNum": 1,
    "pageSize": 20,
    "pages": 3
  }
}
```

---

## 7. 公共API

### 7.1 下拉选项API

#### 7.1.1 获取产品类型选项

**接口信息:**

| 项目 | 内容 |
|------|------|
| 接口路径 | GET /api/v1/eng/options/product-types |
| 接口描述 | 获取产品类型下拉选项 |
| 权限标识 | 无 |

**响应示例:**

```json
{
  "code": 200,
  "message": "操作成功",
  "data": [
    { "value": 1, "label": "自制件" },
    { "value": 2, "label": "外购件" },
    { "value": 3, "label": "外协件" },
    { "value": 4, "label": "虚拟件" }
  ]
}
```

#### 7.1.2 获取工序类型选项

**接口信息:**

| 项目 | 内容 |
|------|------|
| 接口路径 | GET /api/v1/eng/options/operation-types |
| 接口描述 | 获取工序类型下拉选项 |
| 权限标识 | 无 |

**响应示例:**

```json
{
  "code": 200,
  "message": "操作成功",
  "data": [
    { "value": 1, "label": "加工" },
    { "value": 2, "label": "装配" },
    { "value": 3, "label": "检验" },
    { "value": 4, "label": "包装" },
    { "value": 5, "label": "运输" }
  ]
}
```

---

## 8. API汇总

### 8.1 接口统计

| 模块 | 接口数量 |
|------|----------|
| 产品管理 | 11 |
| BOM管理 | 13 |
| 工序管理 | 3 |
| 工艺路线 | 7 |
| ECR管理 | 6 |
| ECO管理 | 5 |
| MES集成 | 3 |
| 公共接口 | 2 |
| **合计** | **50** |

### 8.2 接口清单

| 序号 | 接口路径 | 方法 | 说明 |
|------|----------|------|------|
| 1 | /api/v1/eng/products | GET | 查询产品列表 |
| 2 | /api/v1/eng/products/{id} | GET | 查询产品详情 |
| 3 | /api/v1/eng/products | POST | 创建产品 |
| 4 | /api/v1/eng/products/{id} | PUT | 更新产品 |
| 5 | /api/v1/eng/products/{id} | DELETE | 删除产品 |
| 6 | /api/v1/eng/products/{id}/submit | POST | 提交产品审批 |
| 7 | /api/v1/eng/products/{id}/approve | POST | 审批产品 |
| 8 | /api/v1/eng/products/import | POST | 批量导入产品 |
| 9 | /api/v1/eng/products/export | GET | 导出产品 |
| 10 | /api/v1/eng/product-categories/tree | GET | 查询分类树 |
| 11 | /api/v1/eng/product-categories | POST | 创建分类 |
| 12 | /api/v1/eng/boms | GET | 查询BOM列表 |
| 13 | /api/v1/eng/boms/{id} | GET | 查询BOM详情 |
| 14 | /api/v1/eng/boms | POST | 创建BOM |
| 15 | /api/v1/eng/boms/{id} | PUT | 更新BOM |
| 16 | /api/v1/eng/boms/{id} | DELETE | 删除BOM |
| 17 | /api/v1/eng/boms/{id}/expand | GET | BOM展开查询 |
| 18 | /api/v1/eng/boms/where-used | GET | BOM反查 |
| 19 | /api/v1/eng/boms/compare | GET | BOM版本对比 |
| 20 | /api/v1/eng/boms/{id}/approve | POST | 审批BOM |
| 21 | /api/v1/eng/bom-items/{id}/alternatives | GET | 查询替代物料 |
| 22 | /api/v1/eng/bom-items/{id}/alternatives | POST | 添加替代物料 |
| 23 | /api/v1/eng/operations | GET | 查询工序列表 |
| 24 | /api/v1/eng/operations | POST | 创建工序 |
| 25 | /api/v1/eng/operations/{id}/resources | POST | 配置工序资源 |
| 26 | /api/v1/eng/routes | GET | 查询工艺路线列表 |
| 27 | /api/v1/eng/routes/{id} | GET | 查询工艺路线详情 |
| 28 | /api/v1/eng/routes | POST | 创建工艺路线 |
| 29 | /api/v1/eng/routes/{id} | PUT | 更新工艺路线 |
| 30 | /api/v1/eng/routes/{id} | DELETE | 删除工艺路线 |
| 31 | /api/v1/eng/routes/{id}/approve | POST | 审批工艺路线 |
| 32 | /api/v1/eng/routes/{id}/copy | POST | 复制工艺路线 |
| 33 | /api/v1/eng/ecrs | GET | 查询ECR列表 |
| 34 | /api/v1/eng/ecrs/{id} | GET | 查询ECR详情 |
| 35 | /api/v1/eng/ecrs | POST | 创建ECR |
| 36 | /api/v1/eng/ecrs/{id}/submit | POST | 提交ECR审批 |
| 37 | /api/v1/eng/ecrs/{id}/impact-analysis | GET | ECR影响分析 |
| 38 | /api/v1/eng/ecrs/{id}/approve | POST | 审批ECR |
| 39 | /api/v1/eng/ecos | GET | 查询ECO列表 |
| 40 | /api/v1/eng/ecos | POST | 创建ECO |
| 41 | /api/v1/eng/ecos/{id}/execute | POST | 执行ECO |
| 42 | /api/v1/eng/ecos/{id}/progress | GET | 查询ECO进度 |
| 43 | /api/v1/eng/ecos/{id}/close | POST | 关闭ECO |
| 44 | /api/v1/eng/sync/bom/{id} | POST | 同步BOM到MES |
| 45 | /api/v1/eng/sync/route/{id} | POST | 同步工艺路线到MES |
| 46 | /api/v1/eng/sync/logs | GET | 查询同步日志 |
| 47 | /api/v1/eng/options/product-types | GET | 获取产品类型选项 |
| 48 | /api/v1/eng/options/operation-types | GET | 获取工序类型选项 |

---

## 9. 错误码定义

| 错误码 | 错误信息 | 说明 |
|--------|----------|------|
| 200 | 操作成功 | 成功 |
| 400 | 参数错误 | 请求参数不正确 |
| 401 | 未授权 | 未登录或Token过期 |
| 403 | 禁止访问 | 无权限访问 |
| 404 | 资源未找到 | 请求的资源不存在 |
| 500 | 服务器内部错误 | 系统异常 |
| 10001 | 产品编码已存在 | 产品编码重复 |
| 10002 | 产品被引用无法删除 | 产品被BOM等引用 |
| 20001 | BOM编码已存在 | BOM编码重复 |
| 20002 | 存在循环引用 | BOM存在循环引用 |
| 20003 | 用量必须大于0 | BOM用量校验失败 |
| 30001 | 工序编码已存在 | 工序编码重复 |
| 40001 | ECR不存在 | ECR不存在 |
| 40002 | ECR状态不允许操作 | ECR状态校验失败 |
| 50001 | MES同步失败 | MES接口调用失败 |

---

## 10. 版本历史

| 版本 | 日期 | 修改人 | 修改内容 |
|------|------|--------|----------|
| V1.0 | 2026-03-24 | 研发组 | 初始版本 |

---

*文档结束*