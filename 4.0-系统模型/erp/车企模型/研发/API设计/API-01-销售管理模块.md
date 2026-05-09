# 销售管理模块(SD) API设计文档

## 文档信息

| 项目 | 内容 |
|------|------|
| 文档编号 | API-01 |
| 模块名称 | 销售管理(Sales and Distribution) |
| 版本 | V1.0 |
| 创建日期 | 2026-03-24 |
| 接口前缀 | /admin-api/erp/sale |
| 技术栈 | Spring Boot 2.7 + MyBatis Plus |

---

## 1. 接口概述

### 1.1 接口规范

- **协议**: HTTPS
- **数据格式**: JSON
- **字符编码**: UTF-8
- **接口前缀**: /admin-api/erp/sale
- **认证方式**: Bearer Token (JWT)

### 1.2 通用响应格式

```json
{
  "code": 0,
  "msg": "success",
  "data": {},
  "timestamp": 1711267200000
}
```

### 1.3 通用错误码

| 错误码 | 说明 |
|--------|------|
| 0 | 成功 |
| 400 | 请求参数错误 |
| 401 | 未授权/Token失效 |
| 403 | 无权限访问 |
| 404 | 资源不存在 |
| 500 | 服务器内部错误 |
| 10001 | 业务异常 |
| 10002 | 数据校验失败 |
| 10003 | 数据已存在 |
| 10004 | 数据不存在 |
| 10005 | 状态不允许操作 |

---

## 2. 客户管理接口

### 2.1 客户列表查询

**接口地址**: GET /customer/page

**接口描述**: 分页查询客户列表

**请求参数**:

| 参数名 | 类型 | 必填 | 说明 |
|--------|------|------|------|
| pageNo | Integer | 否 | 页码，默认1 |
| pageSize | Integer | 否 | 每页条数，默认20 |
| customerCode | String | 否 | 客户编码 |
| customerName | String | 否 | 客户名称(模糊查询) |
| customerType | Integer | 否 | 客户类型 |
| customerLevel | Integer | 否 | 客户等级 |
| status | Integer | 否 | 状态 |

**响应示例**:

```json
{
  "code": 0,
  "msg": "success",
  "data": {
    "total": 100,
    "list": [
      {
        "id": 1,
        "customerCode": "CU202603240001",
        "customerName": "张三",
        "customerType": 1,
        "customerTypeName": "个人客户",
        "customerLevel": 1,
        "customerLevelName": "A级",
        "mobile": "138****8000",
        "province": "北京市",
        "city": "朝阳区",
        "creditLimit": 500000.00,
        "creditUsed": 200000.00,
        "status": 1,
        "createdTime": "2026-03-24 10:00:00"
      }
    ]
  }
}
```

---

### 2.2 客户详情查询

**接口地址**: GET /customer/{id}

**接口描述**: 根据ID查询客户详情

**路径参数**:

| 参数名 | 类型 | 必填 | 说明 |
|--------|------|------|------|
| id | Long | 是 | 客户ID |

**响应示例**:

```json
{
  "code": 0,
  "msg": "success",
  "data": {
    "id": 1,
    "customerCode": "CU202603240001",
    "customerName": "张三",
    "customerType": 1,
    "customerTypeName": "个人客户",
    "customerLevel": 1,
    "customerLevelName": "A级",
    "gender": 1,
    "age": 35,
    "mobile": "13800138000",
    "email": "zhangsan@example.com",
    "idCard": "110***********1234",
    "province": "北京市",
    "city": "朝阳区",
    "address": "北京市朝阳区XX路XX号",
    "intentionModel": "Model A",
    "budgetRange": "20-30万",
    "infoSource": "官网",
    "salesRepId": 100,
    "salesRepName": "李四",
    "creditLimit": 500000.00,
    "creditUsed": 200000.00,
    "creditAvailable": 300000.00,
    "status": 1,
    "tags": ["高意向", "价格敏感"],
    "remark": "重要客户",
    "createdBy": "李四",
    "createdTime": "2026-03-24 10:00:00",
    "updatedBy": "李四",
    "updatedTime": "2026-03-24 11:00:00"
  }
}
```

---

### 2.3 创建客户

**接口地址**: POST /customer

**接口描述**: 创建新客户

**请求体**:

```json
{
  "customerType": 1,
  "customerName": "张三",
  "gender": 1,
  "age": 35,
  "mobile": "13800138000",
  "email": "zhangsan@example.com",
  "idCard": "110101199001011234",
  "province": "北京市",
  "city": "朝阳区",
  "address": "北京市朝阳区XX路XX号",
  "intentionModel": "Model A",
  "budgetRange": "20-30万",
  "infoSource": "官网",
  "remark": "重要客户"
}
```

**响应示例**:

```json
{
  "code": 0,
  "msg": "success",
  "data": {
    "id": 1,
    "customerCode": "CU202603240001"
  }
}
```

---

### 2.4 更新客户

**接口地址**: PUT /customer/{id}

**接口描述**: 更新客户信息

**路径参数**:

| 参数名 | 类型 | 必填 | 说明 |
|--------|------|------|------|
| id | Long | 是 | 客户ID |

**请求体**:

```json
{
  "customerName": "张三",
  "gender": 1,
  "age": 36,
  "email": "zhangsan_new@example.com",
  "province": "北京市",
  "city": "海淀区",
  "address": "北京市海淀区XX路XX号",
  "remark": "已更新备注"
}
```

**响应示例**:

```json
{
  "code": 0,
  "msg": "success",
  "data": null
}
```

---

### 2.5 删除客户

**接口地址**: DELETE /customer/{id}

**接口描述**: 删除客户(逻辑删除)

**路径参数**:

| 参数名 | 类型 | 必填 | 说明 |
|--------|------|------|------|
| id | Long | 是 | 客户ID |

**响应示例**:

```json
{
  "code": 0,
  "msg": "success",
  "data": null
}
```

---

### 2.6 客户信用额度设置

**接口地址**: POST /customer/{id}/credit

**接口描述**: 设置客户信用额度

**请求体**:

```json
{
  "creditLimit": 1000000.00,
  "validPeriod": 12,
  "reason": "长期合作客户"
}
```

**响应示例**:

```json
{
  "code": 0,
  "msg": "success",
  "data": {
    "approvalId": 1001,
    "approvalStatus": "pending"
  }
}
```

---

### 2.7 客户标签管理

**接口地址**: POST /customer/{id}/tags

**接口描述**: 更新客户标签

**请求体**:

```json
{
  "tags": ["高意向", "价格敏感", "需试驾"]
}
```

**响应示例**:

```json
{
  "code": 0,
  "msg": "success",
  "data": null
}
```

---

### 2.8 客户联系记录查询

**接口地址**: GET /customer/{id}/contacts

**接口描述**: 查询客户联系记录

**响应示例**:

```json
{
  "code": 0,
  "msg": "success",
  "data": [
    {
      "id": 1,
      "contactType": 1,
      "contactTypeName": "电话",
      "contactContent": "客户对Model A感兴趣，计划下周到店试驾",
      "nextFollowDate": "2026-03-30",
      "attachments": [],
      "createdBy": "李四",
      "createdTime": "2026-03-24 10:00:00"
    }
  ]
}
```

---

## 3. 经销商管理接口

### 3.1 经销商列表查询

**接口地址**: GET /dealer/page

**接口描述**: 分页查询经销商列表

**请求参数**:

| 参数名 | 类型 | 必填 | 说明 |
|--------|------|------|------|
| pageNo | Integer | 否 | 页码，默认1 |
| pageSize | Integer | 否 | 每页条数，默认20 |
| dealerCode | String | 否 | 经销商编码 |
| dealerName | String | 否 | 经销商名称(模糊查询) |
| dealerLevel | Integer | 否 | 经销商等级 |
| province | String | 否 | 省份 |
| status | Integer | 否 | 状态 |

**响应示例**:

```json
{
  "code": 0,
  "msg": "success",
  "data": {
    "total": 50,
    "list": [
      {
        "id": 1,
        "dealerCode": "BJ0001",
        "dealerName": "XX汽车4S店",
        "dealerLevel": 1,
        "dealerLevelName": "一级",
        "province": "北京市",
        "city": "朝阳区",
        "contactPerson": "李四",
        "contactPhone": "010-12345678",
        "creditLimit": 5000000.00,
        "creditUsed": 3000000.00,
        "yearlySales": 50000000.00,
        "targetCompletion": 112.5,
        "status": 1,
        "createdTime": "2026-01-01 00:00:00"
      }
    ]
  }
}
```

---

### 3.2 经销商详情查询

**接口地址**: GET /dealer/{id}

**接口描述**: 根据ID查询经销商详情

**响应示例**:

```json
{
  "code": 0,
  "msg": "success",
  "data": {
    "id": 1,
    "dealerCode": "BJ0001",
    "dealerName": "XX汽车4S店",
    "dealerShortName": "XX4S",
    "dealerLevel": 1,
    "dealerLevelName": "一级",
    "province": "北京市",
    "city": "朝阳区",
    "address": "北京市朝阳区XX路XX号",
    "contactPerson": "李四",
    "contactPhone": "010-12345678",
    "contactEmail": "dealer@example.com",
    "businessLicense": "91110000XXXXXXXXXX",
    "authorizedDate": "2020-01-01",
    "authorizedArea": "北京市朝阳区",
    "creditLimit": 5000000.00,
    "creditUsed": 3000000.00,
    "rebatePolicy": "标准返利",
    "yearlyTarget": 40000000.00,
    "yearlySales": 50000000.00,
    "targetCompletion": 125.0,
    "satisfactionScore": 92.5,
    "status": 1,
    "attachments": [
      {
        "type": "营业执照",
        "name": "license.jpg",
        "url": "/files/license.jpg"
      }
    ],
    "createdTime": "2026-01-01 00:00:00"
  }
}
```

---

### 3.3 创建经销商

**接口地址**: POST /dealer

**接口描述**: 创建新经销商

**请求体**:

```json
{
  "dealerName": "XX汽车4S店",
  "dealerShortName": "XX4S",
  "province": "北京市",
  "city": "朝阳区",
  "address": "北京市朝阳区XX路XX号",
  "contactPerson": "李四",
  "contactPhone": "010-12345678",
  "contactEmail": "dealer@example.com",
  "businessLicense": "91110000XXXXXXXXXX",
  "authorizedArea": "北京市朝阳区",
  "rebatePolicyId": 1,
  "yearlyTarget": 40000000.00,
  "creditLimit": 5000000.00,
  "attachments": [
    {
      "type": "营业执照",
      "name": "license.jpg",
      "url": "/files/license.jpg"
    }
  ]
}
```

**响应示例**:

```json
{
  "code": 0,
  "msg": "success",
  "data": {
    "id": 1,
    "dealerCode": "BJ0001"
  }
}
```

---

### 3.4 经销商等级评定

**接口地址**: POST /dealer/{id}/evaluate

**接口描述**: 执行经销商等级评定

**响应示例**:

```json
{
  "code": 0,
  "msg": "success",
  "data": {
    "evaluationId": 1001,
    "oldLevel": 2,
    "newLevel": 1,
    "scores": {
      "salesScore": 95,
      "serviceScore": 90,
      "satisfactionScore": 92,
      "totalScore": 92.3
    }
  }
}
```

---

## 4. 销售订单接口

### 4.1 订单列表查询

**接口地址**: GET /order/page

**接口描述**: 分页查询销售订单列表

**请求参数**:

| 参数名 | 类型 | 必填 | 说明 |
|--------|------|------|------|
| pageNo | Integer | 否 | 页码，默认1 |
| pageSize | Integer | 否 | 每页条数，默认20 |
| orderNo | String | 否 | 订单编号 |
| customerId | Long | 否 | 客户ID |
| orderStatus | Integer | 否 | 订单状态 |
| orderType | Integer | 否 | 订单类型 |
| startDate | String | 否 | 开始日期 |
| endDate | String | 否 | 结束日期 |
| salesRepId | Long | 否 | 销售代表ID |

**响应示例**:

```json
{
  "code": 0,
  "msg": "success",
  "data": {
    "total": 200,
    "list": [
      {
        "id": 1,
        "orderNo": "SO202603240001",
        "orderType": 1,
        "orderTypeName": "标准订单",
        "customerId": 100,
        "customerName": "张三",
        "customerType": 1,
        "modelCode": "MODEL-A",
        "modelName": "Model A",
        "orderQty": 1,
        "totalAmount": 260000.00,
        "discountRate": 5.0,
        "discountAmount": 13000.00,
        "finalAmount": 247000.00,
        "orderStatus": 30,
        "orderStatusName": "待交付",
        "vinCode": "LSVAM4187E2183456",
        "salesRepName": "李四",
        "orderDate": "2026-03-24",
        "promiseDate": "2026-04-15",
        "createdTime": "2026-03-24 10:00:00"
      }
    ]
  }
}
```

---

### 4.2 订单详情查询

**接口地址**: GET /order/{id}

**接口描述**: 根据ID查询订单详情

**响应示例**:

```json
{
  "code": 0,
  "msg": "success",
  "data": {
    "id": 1,
    "orderNo": "SO202603240001",
    "orderType": 1,
    "orderTypeName": "标准订单",
    "orderSource": 1,
    "orderSourceName": "手工录入",
    "customerId": 100,
    "customerCode": "CU202603240001",
    "customerName": "张三",
    "customerType": 1,
    "customerTypeName": "个人客户",
    "salesRepId": 50,
    "salesRepName": "李四",
    "orderDate": "2026-03-24",
    "promiseDate": "2026-04-15",
    "deliveryMethod": 1,
    "deliveryMethodName": "到店自提",
    "deliveryAddress": "北京市朝阳区XX路XX号",
    "paymentMethod": 1,
    "paymentMethodName": "全款",
    "orderStatus": 30,
    "orderStatusName": "待交付",
    "vinCode": "LSVAM4187E2183456",
    "vinStatus": 2,
    "vinStatusName": "已绑定",
    "items": [
      {
        "id": 1,
        "lineNo": 10,
        "productId": 1000,
        "productCode": "MODEL-A",
        "productName": "Model A",
        "modelCode": "MODEL-A-001",
        "modelName": "Model A 舒适版",
        "colorExt": "星空黑",
        "colorInt": "黑色",
        "wheel": "19寸运动轮毂",
        "orderQty": 1,
        "basePrice": 250000.00,
        "optionPrice": 10000.00,
        "unitPrice": 260000.00,
        "discountRate": 5.0,
        "discountAmount": 13000.00,
        "lineAmount": 247000.00
      }
    ],
    "priceSummary": {
      "basePrice": 250000.00,
      "optionPrice": 10000.00,
      "totalPrice": 260000.00,
      "discountAmount": 13000.00,
      "finalAmount": 247000.00
    },
    "statusHistory": [
      {
        "status": 10,
        "statusName": "待确认",
        "operateTime": "2026-03-24 10:00:00",
        "operator": "李四"
      },
      {
        "status": 30,
        "statusName": "待交付",
        "operateTime": "2026-03-25 14:00:00",
        "operator": "系统"
      }
    ],
    "remark": "客户要求加装踏板",
    "createdBy": "李四",
    "createdTime": "2026-03-24 10:00:00",
    "updatedTime": "2026-03-25 14:00:00"
  }
}
```

---

### 4.3 创建订单

**接口地址**: POST /order

**接口描述**: 创建销售订单

**请求体**:

```json
{
  "orderType": 1,
  "customerId": 100,
  "salesRepId": 50,
  "promiseDate": "2026-04-15",
  "deliveryMethod": 1,
  "deliveryAddress": "北京市朝阳区XX路XX号",
  "paymentMethod": 1,
  "items": [
    {
      "productId": 1000,
      "productCode": "MODEL-A",
      "productName": "Model A",
      "modelCode": "MODEL-A-001",
      "colorExt": "星空黑",
      "colorInt": "黑色",
      "wheel": "19寸运动轮毂",
      "orderQty": 1,
      "discountRate": 5.0,
      "discountReason": "大客户优惠"
    }
  ],
  "remark": "客户要求加装踏板"
}
```

**响应示例**:

```json
{
  "code": 0,
  "msg": "success",
  "data": {
    "id": 1,
    "orderNo": "SO202603240001",
    "orderStatus": 10
  }
}
```

---

### 4.4 更新订单

**接口地址**: PUT /order/{id}

**接口描述**: 更新订单信息(仅草稿状态)

**请求体**:

```json
{
  "promiseDate": "2026-04-20",
  "deliveryMethod": 2,
  "deliveryAddress": "北京市海淀区XX路XX号",
  "remark": "更新交付地址"
}
```

**响应示例**:

```json
{
  "code": 0,
  "msg": "success",
  "data": null
}
```

---

### 4.5 提交订单审批

**接口地址**: POST /order/{id}/submit

**接口描述**: 提交订单进行审批

**响应示例**:

```json
{
  "code": 0,
  "msg": "success",
  "data": {
    "approvalId": 1001,
    "needApproval": true,
    "approvalType": "discount"
  }
}
```

---

### 4.6 订单审批

**接口地址**: POST /order/{id}/approve

**接口描述**: 审批订单

**请求体**:

```json
{
  "approved": true,
  "remark": "审批通过"
}
```

**响应示例**:

```json
{
  "code": 0,
  "msg": "success",
  "data": {
    "orderStatus": 30
  }
}
```

---

### 4.7 订单取消

**接口地址**: POST /order/{id}/cancel

**接口描述**: 取消订单

**请求体**:

```json
{
  "cancelReason": "客户放弃购买",
  "cancelType": 1
}
```

**响应示例**:

```json
{
  "code": 0,
  "msg": "success",
  "data": {
    "approvalId": 1002,
    "needApproval": true
  }
}
```

---

### 4.8 VIN码预分配

**接口地址**: POST /order/{id}/vin-allocate

**接口描述**: 为订单预分配VIN码

**响应示例**:

```json
{
  "code": 0,
  "msg": "success",
  "data": {
    "vinCode": "LSVAM4187E2183456",
    "vinStatus": 1,
    "preoccupyExpireDate": "2026-04-24"
  }
}
```

---

### 4.9 VIN码绑定确认

**接口地址**: POST /order/{id}/vin-bind

**接口描述**: 确认VIN码绑定

**请求体**:

```json
{
  "vinCode": "LSVAM4187E2183456",
  "confirmed": true
}
```

**响应示例**:

```json
{
  "code": 0,
  "msg": "success",
  "data": {
    "vinStatus": 2,
    "orderStatus": 50
  }
}
```

---

### 4.10 VIN码查询

**接口地址**: GET /vin/{vinCode}

**接口描述**: 通过VIN码查询车辆及订单信息

**路径参数**:

| 参数名 | 类型 | 必填 | 说明 |
|--------|------|------|------|
| vinCode | String | 是 | VIN码 |

**响应示例**:

```json
{
  "code": 0,
  "msg": "success",
  "data": {
    "vinCode": "LSVAM4187E2183456",
    "modelCode": "MODEL-A",
    "modelName": "Model A",
    "colorExt": "星空黑",
    "colorInt": "黑色",
    "productionDate": "2026-03-15",
    "productionFactory": "北京工厂",
    "vinStatus": 2,
    "vinStatusName": "已绑定",
    "orderInfo": {
      "orderNo": "SO202603240001",
      "customerName": "张三",
      "salesRepName": "李四",
      "orderDate": "2026-03-24",
      "deliveryDate": "2026-03-25"
    },
    "inventoryInfo": {
      "warehouseName": "北京中心库",
      "storageLocation": "A-01-01",
      "inboundDate": "2026-03-16"
    }
  }
}
```

---

## 5. 订单配置接口

### 5.1 车型列表查询

**接口地址**: GET /model/list

**接口描述**: 查询车型列表

**请求参数**:

| 参数名 | 类型 | 必填 | 说明 |
|--------|------|------|------|
| brandCode | String | 否 | 品牌代码 |
| seriesCode | String | 否 | 车系代码 |
| status | Integer | 否 | 状态 |

**响应示例**:

```json
{
  "code": 0,
  "msg": "success",
  "data": [
    {
      "id": 1000,
      "modelCode": "MODEL-A",
      "modelName": "Model A",
      "brandCode": "BRAND-01",
      "brandName": "XX品牌",
      "seriesCode": "SERIES-01",
      "seriesName": "XX车系",
      "basePrice": 250000.00,
      "status": 1
    }
  ]
}
```

---

### 5.2 车型配置项查询

**接口地址**: GET /model/{modelId}/options

**接口描述**: 查询车型可选配置项

**响应示例**:

```json
{
  "code": 0,
  "msg": "success",
  "data": {
    "modelId": 1000,
    "modelCode": "MODEL-A",
    "modelName": "Model A",
    "basePrice": 250000.00,
    "optionGroups": [
      {
        "groupCode": "COLOR_EXT",
        "groupName": "外观颜色",
        "options": [
          {
            "optionCode": "CLR-BK-01",
            "optionName": "星空黑",
            "optionPrice": 0,
            "imageUrl": "/images/color/bk.jpg",
            "isDefault": true
          },
          {
            "optionCode": "CLR-WH-01",
            "optionName": "珍珠白",
            "optionPrice": 2000,
            "imageUrl": "/images/color/wh.jpg",
            "isDefault": false
          }
        ]
      },
      {
        "groupCode": "COLOR_INT",
        "groupName": "内饰颜色",
        "options": [
          {
            "optionCode": "INT-BK-01",
            "optionName": "黑色",
            "optionPrice": 0,
            "imageUrl": "/images/interior/bk.jpg",
            "isDefault": true
          }
        ]
      },
      {
        "groupCode": "WHEEL",
        "groupName": "轮毂",
        "options": [
          {
            "optionCode": "WHL-18-01",
            "optionName": "18寸标准轮毂",
            "optionPrice": 0,
            "imageUrl": "/images/wheel/18.jpg",
            "isDefault": true
          },
          {
            "optionCode": "WHL-19-01",
            "optionName": "19寸运动轮毂",
            "optionPrice": 10000,
            "imageUrl": "/images/wheel/19.jpg",
            "isDefault": false
          }
        ]
      }
    ],
    "rules": [
      {
        "ruleType": "mutex",
        "optionA": "WHL-19-01",
        "optionB": "WHL-18-01",
        "description": "轮毂只能选择一种"
      }
    ]
  }
}
```

---

### 5.3 配置价格计算

**接口地址**: POST /model/calculate-price

**接口描述**: 计算配置后价格

**请求体**:

```json
{
  "modelId": 1000,
  "options": [
    {
      "groupCode": "COLOR_EXT",
      "optionCode": "CLR-BK-01"
    },
    {
      "groupCode": "COLOR_INT",
      "optionCode": "INT-BK-01"
    },
    {
      "groupCode": "WHEEL",
      "optionCode": "WHL-19-01"
    }
  ]
}
```

**响应示例**:

```json
{
  "code": 0,
  "msg": "success",
  "data": {
    "modelId": 1000,
    "basePrice": 250000.00,
    "optionPrice": 10000.00,
    "totalPrice": 260000.00,
    "priceDetail": [
      {
        "item": "车型基础价",
        "amount": 250000.00
      },
      {
        "item": "外观颜色-星空黑",
        "amount": 0.00
      },
      {
        "item": "内饰颜色-黑色",
        "amount": 0.00
      },
      {
        "item": "轮毂-19寸运动轮毂",
        "amount": 10000.00
      }
    ],
    "valid": true,
    "conflicts": []
  }
}
```

---

### 5.4 配置有效性校验

**接口地址**: POST /model/validate-options

**接口描述**: 校验配置组合有效性

**请求体**:

```json
{
  "modelId": 1000,
  "options": [
    {
      "groupCode": "WHEEL",
      "optionCode": "WHL-19-01"
    },
    {
      "groupCode": "WHEEL",
      "optionCode": "WHL-18-01"
    }
  ]
}
```

**响应示例**:

```json
{
  "code": 0,
  "msg": "success",
  "data": {
    "valid": false,
    "conflicts": [
      {
        "optionA": "WHL-19-01",
        "optionB": "WHL-18-01",
        "message": "轮毂只能选择一种，当前配置与已选配置冲突"
      }
    ]
  }
}
```

---

### 5.5 保存配置方案

**接口地址**: POST /config-scheme

**接口描述**: 保存配置方案

**请求体**:

```json
{
  "schemeName": "张三专属配置",
  "modelId": 1000,
  "customerId": 100,
  "options": [
    {
      "groupCode": "COLOR_EXT",
      "optionCode": "CLR-BK-01",
      "optionName": "星空黑"
    },
    {
      "groupCode": "COLOR_INT",
      "optionCode": "INT-BK-01",
      "optionName": "黑色"
    },
    {
      "groupCode": "WHEEL",
      "optionCode": "WHL-19-01",
      "optionName": "19寸运动轮毂"
    }
  ],
  "totalPrice": 260000.00,
  "remark": "客户偏好配置"
}
```

**响应示例**:

```json
{
  "code": 0,
  "msg": "success",
  "data": {
    "id": 1,
    "schemeCode": "CFG202603240001",
    "expireDate": "2026-06-24"
  }
}
```

---

## 6. 交付管理接口

### 6.1 交付计划列表

**接口地址**: GET /delivery-plan/page

**接口描述**: 分页查询交付计划列表

**请求参数**:

| 参数名 | 类型 | 必填 | 说明 |
|--------|------|------|------|
| pageNo | Integer | 否 | 页码 |
| pageSize | Integer | 否 | 每页条数 |
| planNo | String | 否 | 计划编号 |
| orderNo | String | 否 | 订单编号 |
| planStatus | Integer | 否 | 计划状态 |
| startDate | String | 否 | 开始日期 |
| endDate | String | 否 | 结束日期 |

**响应示例**:

```json
{
  "code": 0,
  "msg": "success",
  "data": {
    "total": 50,
    "list": [
      {
        "id": 1,
        "planNo": "DP202603240001",
        "orderId": 1,
        "orderNo": "SO202603240001",
        "customerName": "张三",
        "vinCode": "LSVAM4187E2183456",
        "modelName": "Model A",
        "planDate": "2026-04-01",
        "deliveryMethod": 1,
        "deliveryMethodName": "送车上门",
        "deliveryAddress": "北京市朝阳区XX路XX号",
        "planStatus": 10,
        "planStatusName": "待确认",
        "pdiStatus": 1,
        "pdiStatusName": "通过",
        "createdTime": "2026-03-24 10:00:00"
      }
    ]
  }
}
```

---

### 6.2 创建交付计划

**接口地址**: POST /delivery-plan

**接口描述**: 创建交付计划

**请求体**:

```json
{
  "orderId": 1,
  "planDate": "2026-04-01",
  "deliveryMethod": 1,
  "deliveryAddress": "北京市朝阳区XX路XX号",
  "receiverName": "张三",
  "receiverPhone": "13800138000",
  "remark": "客户指定上午交付"
}
```

**响应示例**:

```json
{
  "code": 0,
  "msg": "success",
  "data": {
    "id": 1,
    "planNo": "DP202603240001"
  }
}
```

---

### 6.3 调整交付计划

**接口地址**: PUT /delivery-plan/{id}

**接口描述**: 调整交付计划

**请求体**:

```json
{
  "planDate": "2026-04-10",
  "adjustReason": "客户临时有事"
}
```

**响应示例**:

```json
{
  "code": 0,
  "msg": "success",
  "data": {
    "needApproval": true,
    "approvalId": 1001
  }
}
```

---

### 6.4 PDI检查标准查询

**接口地址**: GET /pdi-standard/list

**接口描述**: 查询PDI检查标准项目

**响应示例**:

```json
{
  "code": 0,
  "msg": "success",
  "data": [
    {
      "category": "外观检查",
      "items": [
        {
          "itemCode": "PDI-001",
          "itemName": "车漆检查",
          "checkMethod": "目测",
          "standard": "漆面光洁，无划痕、无色差",
          "isRequired": true
        },
        {
          "itemCode": "PDI-002",
          "itemName": "玻璃检查",
          "checkMethod": "目测",
          "standard": "玻璃完好，无裂纹、划痕",
          "isRequired": true
        }
      ]
    },
    {
      "category": "内饰检查",
      "items": [
        {
          "itemCode": "PDI-010",
          "itemName": "座椅检查",
          "checkMethod": "目测/手动",
          "standard": "座椅完好，调节功能正常",
          "isRequired": true
        }
      ]
    }
  ]
}
```

---

### 6.5 提交PDI检查结果

**接口地址**: POST /pdi-check

**接口描述**: 提交PDI检查结果

**请求体**:

```json
{
  "vinCode": "LSVAM4187E2183456",
  "deliveryPlanId": 1,
  "checkResults": [
    {
      "itemCode": "PDI-001",
      "itemName": "车漆检查",
      "result": 1,
      "remark": ""
    },
    {
      "itemCode": "PDI-002",
      "itemName": "玻璃检查",
      "result": 1,
      "remark": ""
    },
    {
      "itemCode": "PDI-010",
      "itemName": "座椅检查",
      "result": 2,
      "remark": "主驾驶座椅有划痕",
      "photos": ["/files/pdi/001.jpg"]
    }
  ]
}
```

**响应示例**:

```json
{
  "code": 0,
  "msg": "success",
  "data": {
    "pdiId": 1,
    "pdiStatus": 2,
    "pdiStatusName": "不合格",
    "failedItems": [
      {
        "itemCode": "PDI-010",
        "itemName": "座椅检查",
        "remark": "主驾驶座椅有划痕"
      }
    ]
  }
}
```

---

### 6.6 车辆出库

**接口地址**: POST /outbound

**接口描述**: 车辆出库确认

**请求体**:

```json
{
  "vinCode": "LSVAM4187E2183456",
  "deliveryPlanId": 1,
  "confirmed": true
}
```

**响应示例**:

```json
{
  "code": 0,
  "msg": "success",
  "data": {
    "outboundNo": "OB202603240001",
    "outboundTime": "2026-04-01 09:00:00"
  }
}
```

---

### 6.7 交付确认

**接口地址**: POST /delivery-confirm

**接口描述**: 交付签收确认

**请求体**:

```json
{
  "deliveryPlanId": 1,
  "vinCode": "LSVAM4187E2183456",
  "signatureImage": "/files/sign/001.png",
  "photos": [
    "/files/delivery/001.jpg",
    "/files/delivery/002.jpg"
  ],
  "documents": [
    {
      "type": "合格证",
      "status": "齐全"
    },
    {
      "type": "说明书",
      "status": "齐全"
    },
    {
      "type": "钥匙",
      "quantity": 2,
      "status": "齐全"
    }
  ],
  "remark": ""
}
```

**响应示例**:

```json
{
  "code": 0,
  "msg": "success",
  "data": {
    "deliveryNo": "DV202603240001",
    "deliveryTime": "2026-04-01 10:30:00",
    "orderStatus": 70
  }
}
```

---

### 6.8 交付异常上报

**接口地址**: POST /delivery-exception

**接口描述**: 上报交付异常

**请求体**:

```json
{
  "deliveryPlanId": 1,
  "exceptionType": 2,
  "exceptionReason": "车辆外观有划痕",
  "photos": [
    "/files/exception/001.jpg"
  ]
}
```

**响应示例**:

```json
{
  "code": 0,
  "msg": "success",
  "data": {
    "exceptionId": 1,
    "orderStatus": 85
  }
}
```

---

## 7. 销售分析接口

### 7.1 销售日报

**接口地址**: GET /analysis/daily-report

**接口描述**: 查询销售日报

**请求参数**:

| 参数名 | 类型 | 必填 | 说明 |
|--------|------|------|------|
| date | String | 否 | 日期，默认当天 |

**响应示例**:

```json
{
  "code": 0,
  "msg": "success",
  "data": {
    "reportDate": "2026-03-24",
    "orderCount": 25,
    "orderAmount": 6250000.00,
    "deliveryCount": 20,
    "deliveryAmount": 5000000.00,
    "lastYearOrderCount": 20,
    "lastYearOrderAmount": 5000000.00,
    "orderYoy": 25.0,
    "orderAmountYoy": 25.0,
    "lastMonthOrderCount": 22,
    "orderMom": 13.6,
    "modelSales": [
      {
        "modelName": "Model A",
        "orderCount": 15,
        "orderAmount": 3750000.00,
        "percentage": 60.0
      },
      {
        "modelName": "Model B",
        "orderCount": 10,
        "orderAmount": 2500000.00,
        "percentage": 40.0
      }
    ],
    "regionSales": [
      {
        "region": "北京市",
        "orderCount": 10,
        "orderAmount": 2500000.00
      }
    ]
  }
}
```

---

### 7.2 销售月报

**接口地址**: GET /analysis/monthly-report

**接口描述**: 查询销售月报

**请求参数**:

| 参数名 | 类型 | 必填 | 说明 |
|--------|------|------|------|
| year | Integer | 否 | 年份，默认当前年 |
| month | Integer | 否 | 月份，默认当前月 |

**响应示例**:

```json
{
  "code": 0,
  "msg": "success",
  "data": {
    "reportMonth": "2026-03",
    "orderCount": 500,
    "orderAmount": 125000000.00,
    "deliveryCount": 450,
    "deliveryAmount": 112500000.00,
    "targetAmount": 100000000.00,
    "targetCompletion": 112.5,
    "lastYearOrderCount": 400,
    "lastYearOrderAmount": 100000000.00,
    "orderYoy": 25.0,
    "orderAmountYoy": 25.0,
    "lastMonthOrderCount": 480,
    "orderMom": 4.2,
    "dailyTrend": [
      {
        "date": "2026-03-01",
        "orderCount": 15,
        "orderAmount": 375000.00
      }
    ],
    "modelRanking": [
      {
        "rank": 1,
        "modelName": "Model A",
        "orderCount": 200,
        "orderAmount": 50000000.00,
        "percentage": 40.0
      }
    ],
    "regionRanking": [
      {
        "rank": 1,
        "region": "北京市",
        "orderCount": 100,
        "orderAmount": 25000000.00
      }
    ]
  }
}
```

---

### 7.3 经销商业绩报表

**接口地址**: GET /analysis/dealer-performance

**接口描述**: 查询经销商业绩排名

**请求参数**:

| 参数名 | 类型 | 必填 | 说明 |
|--------|------|------|------|
| year | Integer | 否 | 年份 |
| month | Integer | 否 | 月份 |
| dealerId | Long | 否 | 经销商ID |

**响应示例**:

```json
{
  "code": 0,
  "msg": "success",
  "data": {
    "total": 50,
    "list": [
      {
        "rank": 1,
        "dealerId": 1,
        "dealerCode": "BJ0001",
        "dealerName": "XX汽车4S店",
        "dealerLevel": 1,
        "orderCount": 50,
        "deliveryCount": 45,
        "salesAmount": 11250000.00,
        "targetAmount": 10000000.00,
        "targetCompletion": 112.5,
        "yoyGrowth": 15.0,
        "satisfactionScore": 92.5
      }
    ]
  }
}
```

---

### 7.4 销售概览看板

**接口地址**: GET /analysis/dashboard

**接口描述**: 查询销售概览看板数据

**响应示例**:

```json
{
  "code": 0,
  "msg": "success",
  "data": {
    "todayOverview": {
      "orderCount": 25,
      "orderCountMom": 5.0,
      "deliveryCount": 20,
      "deliveryCountMom": 3.0,
      "monthSales": 50000000.00,
      "monthTarget": 60000000.00,
      "targetCompletion": 83.3
    },
    "pendingOrders": {
      "toConfirm": 10,
      "toApprove": 5,
      "inProduction": 50,
      "toDeliver": 30
    },
    "weeklyTrend": [
      {
        "date": "2026-03-18",
        "orderCount": 20,
        "deliveryCount": 18
      },
      {
        "date": "2026-03-19",
        "orderCount": 22,
        "deliveryCount": 20
      }
    ],
    "monthlyTrend": [
      {
        "month": "2026-01",
        "salesAmount": 45000000.00
      },
      {
        "month": "2026-02",
        "salesAmount": 48000000.00
      },
      {
        "month": "2026-03",
        "salesAmount": 50000000.00
      }
    ],
    "alerts": [
      {
        "type": "overdue",
        "message": "5个订单即将超期",
        "count": 5
      },
      {
        "type": "credit",
        "message": "3个客户信用额度即将用尽",
        "count": 3
      }
    ]
  }
}
```

---

### 7.5 订单状态看板

**接口地址**: GET /analysis/order-status-dashboard

**接口描述**: 查询订单状态分布

**响应示例**:

```json
{
  "code": 0,
  "msg": "success",
  "data": {
    "statusDistribution": [
      {
        "status": 10,
        "statusName": "待确认",
        "count": 10,
        "percentage": 5.0
      },
      {
        "status": 20,
        "statusName": "已确认",
        "count": 15,
        "percentage": 7.5
      },
      {
        "status": 30,
        "statusName": "生产中",
        "count": 50,
        "percentage": 25.0
      },
      {
        "status": 50,
        "statusName": "待交付",
        "count": 30,
        "percentage": 15.0
      },
      {
        "status": 60,
        "statusName": "交付中",
        "count": 20,
        "percentage": 10.0
      },
      {
        "status": 70,
        "statusName": "已完成",
        "count": 70,
        "percentage": 35.0
      },
      {
        "status": 85,
        "statusName": "异常处理中",
        "count": 5,
        "percentage": 2.5
      }
    ],
    "exceptionOrders": [
      {
        "orderNo": "SO202603240001",
        "exceptionType": "延期",
        "days": 3,
        "customerName": "张三"
      }
    ],
    "overdueOrders": [
      {
        "orderNo": "SO202603200001",
        "promiseDate": "2026-03-20",
        "overdueDays": 4,
        "customerName": "李四"
      }
    ]
  }
}
```

---

### 7.6 库存预警分析

**接口地址**: GET /analysis/inventory-alert

**接口描述**: 查询库存预警信息

**响应示例**:

```json
{
  "code": 0,
  "msg": "success",
  "data": [
    {
      "alertType": "low_stock",
      "alertTypeName": "库存不足",
      "modelCode": "MODEL-A",
      "modelName": "Model A",
      "currentStock": 5,
      "safetyStock": 10,
      "alertLevel": "warning"
    },
    {
      "alertType": "slow_moving",
      "alertTypeName": "滞销预警",
      "vinCode": "LSVAM4187E2183456",
      "modelCode": "MODEL-B",
      "modelName": "Model B",
      "stockDays": 120,
      "threshold": 90,
      "alertLevel": "danger"
    }
  ]
}
```

---

## 8. 错误码定义

### 8.1 客户管理错误码

| 错误码 | 说明 |
|--------|------|
| 20001 | 客户不存在 |
| 20002 | 客户已存在 |
| 20003 | 客户手机号已存在 |
| 20004 | 客户状态不允许操作 |
| 20005 | 客户信用额度不足 |

### 8.2 订单管理错误码

| 错误码 | 说明 |
|--------|------|
| 21001 | 订单不存在 |
| 21002 | 订单已存在 |
| 21003 | 订单状态不允许操作 |
| 21004 | 订单已审批 |
| 21005 | 订单已取消 |
| 21006 | 订单折扣超出权限 |
| 21007 | 订单信用额度不足 |
| 21008 | VIN码不存在 |
| 21009 | VIN码已被占用 |
| 21010 | VIN码格式不正确 |

### 8.3 配置管理错误码

| 错误码 | 说明 |
|--------|------|
| 22001 | 车型不存在 |
| 22002 | 配置项不存在 |
| 22003 | 配置组合冲突 |
| 22004 | 配置规则违反 |

### 8.4 交付管理错误码

| 错误码 | 说明 |
|--------|------|
| 23001 | 交付计划不存在 |
| 23002 | PDI检查未通过 |
| 23003 | 车辆未入库 |
| 23004 | 车辆已出库 |
| 23005 | 单据不齐全 |

---

## 9. 接口版本历史

| 版本 | 日期 | 修改内容 |
|------|------|----------|
| V1.0 | 2026-03-24 | 初始版本 |

---

**文档修订历史**

| 版本 | 修订日期 | 修订人 | 修订内容 |
|------|----------|--------|----------|
| V1.0 | 2026-03-24 | 系统生成 | 初始版本 |