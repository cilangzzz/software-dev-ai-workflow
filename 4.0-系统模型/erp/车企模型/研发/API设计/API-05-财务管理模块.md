# 财务管理模块(FI/CO) API设计文档

**文档版本**: V1.0
**创建日期**: 2026-03-24
**文档编号**: API-05
**关联PRD**: PRD-05-财务管理模块
**技术栈**: Spring Boot 2.7 + MyBatis Plus

---

## 1. 文档概述

### 1.1 文档目的
本文档详细描述财务管理模块的RESTful API接口设计，包括接口路径、请求参数、响应格式、错误码等。

### 1.2 API设计原则
- **RESTful风格**: 使用标准HTTP方法和资源路径
- **版本控制**: URL中包含版本号/api/v1
- **统一响应**: 使用统一的响应格式
- **错误处理**: 使用标准HTTP状态码和错误信息
- **安全认证**: 所有接口需要Token认证
- **多租户**: 通过Token获取租户信息

### 1.3 通用请求头
```
Authorization: Bearer {token}
Content-Type: application/json
X-Tenant-Id: {tenantId}
```

### 1.4 统一响应格式

**成功响应**:
```json
{
  "code": 200,
  "message": "操作成功",
  "data": {},
  "timestamp": 1711267200000
}
```

**失败响应**:
```json
{
  "code": 400,
  "message": "参数错误",
  "data": null,
  "timestamp": 1711267200000
}
```

**分页响应**:
```json
{
  "code": 200,
  "message": "操作成功",
  "data": {
    "list": [],
    "total": 100,
    "pageNum": 1,
    "pageSize": 10,
    "pages": 10
  },
  "timestamp": 1711267200000
}
```

---

## 2. 总账模块API

### 2.1 会计科目管理

#### 2.1.1 查询科目列表

**接口说明**: 分页查询会计科目列表

**请求信息**:
- **URL**: `/api/v1/fi/accounts`
- **Method**: `GET`
- **权限**: `fi:account:list`

**请求参数**:
| 参数名 | 类型 | 必填 | 说明 |
|--------|------|------|------|
| accountCode | String | N | 科目编码 |
| accountName | String | N | 科目名称 |
| accountType | Integer | N | 科目类型 |
| is_enabled | Integer | N | 是否启用 |
| pageNum | Integer | N | 页码，默认1 |
| pageSize | Integer | N | 每页条数，默认10 |

**响应示例**:
```json
{
  "code": 200,
  "message": "操作成功",
  "data": {
    "list": [
      {
        "id": 1,
        "accountCode": "1001",
        "accountName": "库存现金",
        "accountType": 1,
        "accountTypeName": "资产类",
        "balanceDirection": 1,
        "isLeaf": 1,
        "isEnabled": 1,
        "auxCustomer": 0,
        "auxSupplier": 0,
        "createTime": "2024-03-01 10:00:00"
      }
    ],
    "total": 100,
    "pageNum": 1,
    "pageSize": 10,
    "pages": 10
  }
}
```

---

#### 2.1.2 查询科目树

**接口说明**: 查询会计科目树形结构

**请求信息**:
- **URL**: `/api/v1/fi/accounts/tree`
- **Method**: `GET`
- **权限**: `fi:account:list`

**请求参数**:
| 参数名 | 类型 | 必填 | 说明 |
|--------|------|------|------|
| is_enabled | Integer | N | 是否启用 |

**响应示例**:
```json
{
  "code": 200,
  "message": "操作成功",
  "data": [
    {
      "id": 1,
      "accountCode": "1001",
      "accountName": "库存现金",
      "accountType": 1,
      "children": [
        {
          "id": 2,
          "accountCode": "100101",
          "accountName": "库存现金-人民币"
        }
      ]
    }
  ]
}
```

---

#### 2.1.3 新增科目

**接口说明**: 新增会计科目

**请求信息**:
- **URL**: `/api/v1/fi/accounts`
- **Method**: `POST`
- **权限**: `fi:account:add`

**请求体**:
```json
{
  "accountCode": "1001",
  "accountName": "库存现金",
  "parentId": null,
  "accountType": 1,
  "balanceDirection": 1,
  "auxCustomer": 0,
  "auxSupplier": 0,
  "auxDepartment": 0,
  "auxProject": 0,
  "remark": ""
}
```

**响应示例**:
```json
{
  "code": 200,
  "message": "新增成功",
  "data": {
    "id": 1
  }
}
```

---

#### 2.1.4 修改科目

**接口说明**: 修改会计科目

**请求信息**:
- **URL**: `/api/v1/fi/accounts/{id}`
- **Method**: `PUT`
- **权限**: `fi:account:edit`

**路径参数**:
| 参数名 | 类型 | 必填 | 说明 |
|--------|------|------|------|
| id | Long | Y | 科目ID |

**请求体**:
```json
{
  "accountName": "现金",
  "auxCustomer": 1,
  "remark": "修改备注"
}
```

**响应示例**:
```json
{
  "code": 200,
  "message": "修改成功"
}
```

---

#### 2.1.5 删除科目

**接口说明**: 删除会计科目

**请求信息**:
- **URL**: `/api/v1/fi/accounts/{id}`
- **Method**: `DELETE`
- **权限**: `fi:account:delete`

**路径参数**:
| 参数名 | 类型 | 必填 | 说明 |
|--------|------|------|------|
| id | Long | Y | 科目ID |

**响应示例**:
```json
{
  "code": 200,
  "message": "删除成功"
}
```

---

#### 2.1.6 启用/停用科目

**接口说明**: 启用或停用会计科目

**请求信息**:
- **URL**: `/api/v1/fi/accounts/{id}/status`
- **Method**: `PUT`
- **权限**: `fi:account:edit`

**请求体**:
```json
{
  "isEnabled": 0
}
```

**响应示例**:
```json
{
  "code": 200,
  "message": "操作成功"
}
```

---

### 2.2 凭证管理

#### 2.2.1 查询凭证列表

**接口说明**: 分页查询凭证列表

**请求信息**:
- **URL**: `/api/v1/fi/vouchers`
- **Method**: `GET`
- **权限**: `fi:voucher:list`

**请求参数**:
| 参数名 | 类型 | 必填 | 说明 |
|--------|------|------|------|
| voucherWord | String | N | 凭证字 |
| voucherNo | String | N | 凭证号 |
| voucherDateStart | String | N | 凭证日期起 |
| voucherDateEnd | String | N | 凭证日期止 |
| fiscalYear | Integer | N | 会计年度 |
| periodNum | Integer | N | 期间号 |
| accountCode | String | N | 科目编码 |
| status | Integer | N | 状态 |
| pageNum | Integer | N | 页码 |
| pageSize | Integer | N | 每页条数 |

**响应示例**:
```json
{
  "code": 200,
  "message": "操作成功",
  "data": {
    "list": [
      {
        "id": 1,
        "voucherWord": "记",
        "voucherNo": 1,
        "voucherDate": "2024-03-01",
        "fiscalYear": 2024,
        "periodNum": 3,
        "debitAmount": 10000.00,
        "creditAmount": 10000.00,
        "entryCount": 2,
        "status": 0,
        "statusName": "制单",
        "makeByName": "张三",
        "makeTime": "2024-03-01 10:00:00"
      }
    ],
    "total": 100
  }
}
```

---

#### 2.2.2 查询凭证明细

**接口说明**: 查询凭证详细信息

**请求信息**:
- **URL**: `/api/v1/fi/vouchers/{id}`
- **Method**: `GET`
- **权限**: `fi:voucher:query`

**响应示例**:
```json
{
  "code": 200,
  "message": "操作成功",
  "data": {
    "id": 1,
    "voucherWord": "记",
    "voucherNo": 1,
    "voucherDate": "2024-03-01",
    "fiscalYear": 2024,
    "periodNum": 3,
    "debitAmount": 10000.00,
    "creditAmount": 10000.00,
    "status": 0,
    "makeByName": "张三",
    "makeTime": "2024-03-01 10:00:00",
    "entries": [
      {
        "entryNo": 1,
        "accountCode": "1001",
        "accountName": "库存现金",
        "summary": "提现",
        "debitAmount": 10000.00,
        "creditAmount": 0.00,
        "auxCustomerId": null,
        "auxCustomerName": null
      },
      {
        "entryNo": 2,
        "accountCode": "1002",
        "accountName": "银行存款",
        "summary": "提现",
        "debitAmount": 0.00,
        "creditAmount": 10000.00
      }
    ]
  }
}
```

---

#### 2.2.3 新增凭证

**接口说明**: 新增记账凭证

**请求信息**:
- **URL**: `/api/v1/fi/vouchers`
- **Method**: `POST`
- **权限**: `fi:voucher:add`

**请求体**:
```json
{
  "voucherWord": "记",
  "voucherDate": "2024-03-01",
  "entries": [
    {
      "accountCode": "1001",
      "summary": "提现",
      "debitAmount": 10000.00,
      "creditAmount": 0.00,
      "auxCustomerId": null
    },
    {
      "accountCode": "1002",
      "summary": "提现",
      "debitAmount": 0.00,
      "creditAmount": 10000.00
    }
  ],
  "remark": ""
}
```

**响应示例**:
```json
{
  "code": 200,
  "message": "新增成功",
  "data": {
    "id": 1,
    "voucherNo": 1
  }
}
```

---

#### 2.2.4 修改凭证

**接口说明**: 修改记账凭证

**请求信息**:
- **URL**: `/api/v1/fi/vouchers/{id}`
- **Method**: `PUT`
- **权限**: `fi:voucher:edit`

**请求体**:
```json
{
  "voucherDate": "2024-03-01",
  "entries": [
    {
      "accountCode": "1001",
      "summary": "提现",
      "debitAmount": 10000.00,
      "creditAmount": 0.00
    },
    {
      "accountCode": "1002",
      "summary": "提现",
      "debitAmount": 0.00,
      "creditAmount": 10000.00
    }
  ]
}
```

**响应示例**:
```json
{
  "code": 200,
  "message": "修改成功"
}
```

---

#### 2.2.5 删除凭证

**接口说明**: 删除记账凭证

**请求信息**:
- **URL**: `/api/v1/fi/vouchers/{id}`
- **Method**: `DELETE`
- **权限**: `fi:voucher:delete`

**响应示例**:
```json
{
  "code": 200,
  "message": "删除成功"
}
```

---

#### 2.2.6 审核凭证

**接口说明**: 审核记账凭证

**请求信息**:
- **URL**: `/api/v1/fi/vouchers/{id}/audit`
- **Method**: `POST`
- **权限**: `fi:voucher:audit`

**请求体**:
```json
{
  "auditResult": 1,
  "auditRemark": ""
}
```

**响应示例**:
```json
{
  "code": 200,
  "message": "审核成功"
}
```

---

#### 2.2.7 批量审核凭证

**接口说明**: 批量审核记账凭证

**请求信息**:
- **URL**: `/api/v1/fi/vouchers/batch-audit`
- **Method**: `POST`
- **权限**: `fi:voucher:audit`

**请求体**:
```json
{
  "ids": [1, 2, 3],
  "auditResult": 1
}
```

**响应示例**:
```json
{
  "code": 200,
  "message": "审核成功"
}
```

---

#### 2.2.8 记账凭证

**接口说明**: 对凭证进行记账操作

**请求信息**:
- **URL**: `/api/v1/fi/vouchers/{id}/post`
- **Method**: `POST`
- **权限**: `fi:voucher:post`

**响应示例**:
```json
{
  "code": 200,
  "message": "记账成功"
}
```

---

#### 2.2.9 批量记账凭证

**接口说明**: 批量记账凭证

**请求信息**:
- **URL**: `/api/v1/fi/vouchers/batch-post`
- **Method**: `POST`
- **权限**: `fi:voucher:post`

**请求体**:
```json
{
  "ids": [1, 2, 3]
}
```

**响应示例**:
```json
{
  "code": 200,
  "message": "记账成功"
}
```

---

#### 2.2.10 红冲凭证

**接口说明**: 对已记账凭证进行红冲

**请求信息**:
- **URL**: `/api/v1/fi/vouchers/{id}/red`
- **Method**: `POST`
- **权限**: `fi:voucher:red`

**请求体**:
```json
{
  "redAmount": null,
  "remark": "红冲原因"
}
```

**响应示例**:
```json
{
  "code": 200,
  "message": "红冲成功",
  "data": {
    "id": 2,
    "voucherNo": 2
  }
}
```

---

### 2.3 账簿查询

#### 2.3.1 查询总分类账

**接口说明**: 查询总分类账

**请求信息**:
- **URL**: `/api/v1/fi/ledgers/general`
- **Method**: `GET`
- **权限**: `fi:ledger:query`

**请求参数**:
| 参数名 | 类型 | 必填 | 说明 |
|--------|------|------|------|
| fiscalYear | Integer | Y | 会计年度 |
| periodNumStart | Integer | N | 起始期间 |
| periodNumEnd | Integer | N | 结束期间 |
| accountCodeStart | String | N | 起始科目 |
| accountCodeEnd | String | N | 结束科目 |
| accountLevel | Integer | N | 科目级次 |

**响应示例**:
```json
{
  "code": 200,
  "message": "操作成功",
  "data": [
    {
      "accountCode": "1001",
      "accountName": "库存现金",
      "beginDebit": 10000.00,
      "beginCredit": 0.00,
      "currentDebit": 5000.00,
      "currentCredit": 3000.00,
      "endDebit": 12000.00,
      "endCredit": 0.00
    }
  ]
}
```

---

#### 2.3.2 查询明细分类账

**接口说明**: 查询明细分类账

**请求信息**:
- **URL**: `/api/v1/fi/ledgers/detail`
- **Method**: `GET`
- **权限**: `fi:ledger:query`

**请求参数**:
| 参数名 | 类型 | 必填 | 说明 |
|--------|------|------|------|
| accountCode | String | Y | 科目编码 |
| fiscalYear | Integer | Y | 会计年度 |
| periodNum | Integer | Y | 期间号 |
| auxCustomerId | Long | N | 客户ID |
| auxSupplierId | Long | N | 供应商ID |
| auxDepartmentId | Long | N | 部门ID |

**响应示例**:
```json
{
  "code": 200,
  "message": "操作成功",
  "data": [
    {
      "voucherDate": "2024-03-01",
      "voucherWord": "记",
      "voucherNo": 1,
      "voucherId": 1,
      "summary": "提现",
      "debitAmount": 10000.00,
      "creditAmount": 0.00,
      "balance": 10000.00
    }
  ]
}
```

---

#### 2.3.3 查询科目余额表

**接口说明**: 查询科目余额表

**请求信息**:
- **URL**: `/api/v1/fi/balances`
- **Method**: `GET`
- **权限**: `fi:balance:query`

**请求参数**:
| 参数名 | 类型 | 必填 | 说明 |
|--------|------|------|------|
| fiscalYear | Integer | Y | 会计年度 |
| periodNum | Integer | Y | 期间号 |
| accountCodeStart | String | N | 起始科目 |
| accountCodeEnd | String | N | 结束科目 |
| accountLevel | Integer | N | 科目级次 |
| showLeaf | Integer | N | 只显示末级 |

**响应示例**:
```json
{
  "code": 200,
  "message": "操作成功",
  "data": {
    "list": [
      {
        "accountCode": "1001",
        "accountName": "库存现金",
        "accountLevel": 1,
        "beginDebit": 10000.00,
        "beginCredit": 0.00,
        "currentDebit": 5000.00,
        "currentCredit": 3000.00,
        "yearDebit": 50000.00,
        "yearCredit": 30000.00,
        "endDebit": 12000.00,
        "endCredit": 0.00
      }
    ],
    "totalDebit": 50000.00,
    "totalCredit": 30000.00,
    "isBalanced": true
  }
}
```

---

### 2.4 期末处理

#### 2.4.1 查询期末结账状态

**接口说明**: 查询期末结账状态

**请求信息**:
- **URL**: `/api/v1/fi/periods/close-status`
- **Method**: `GET`
- **权限**: `fi:period:query`

**请求参数**:
| 参数名 | 类型 | 必填 | 说明 |
|--------|------|------|------|
| fiscalYear | Integer | Y | 会计年度 |
| periodNum | Integer | Y | 期间号 |

**响应示例**:
```json
{
  "code": 200,
  "message": "操作成功",
  "data": {
    "periodId": 1,
    "status": 1,
    "statusName": "已开放",
    "checkItems": [
      {
        "itemCode": "voucher_posted",
        "itemName": "凭证已记账",
        "isChecked": true,
        "isPassed": true
      },
      {
        "itemCode": "trial_balance",
        "itemName": "试算平衡",
        "isChecked": true,
        "isPassed": true
      }
    ],
    "canClose": true
  }
}
```

---

#### 2.4.2 损益结转

**接口说明**: 执行损益结转

**请求信息**:
- **URL**: `/api/v1/fi/periods/profit-transfer`
- **Method**: `POST`
- **权限**: `fi:period:close`

**请求体**:
```json
{
  "fiscalYear": 2024,
  "periodNum": 3
}
```

**响应示例**:
```json
{
  "code": 200,
  "message": "结转成功",
  "data": {
    "voucherId": 100,
    "voucherNo": 50,
    "profitAmount": 100000.00
  }
}
```

---

#### 2.4.3 期末结账

**接口说明**: 执行期末结账

**请求信息**:
- **URL**: `/api/v1/fi/periods/close`
- **Method**: `POST`
- **权限**: `fi:period:close`

**请求体**:
```json
{
  "fiscalYear": 2024,
  "periodNum": 3
}
```

**响应示例**:
```json
{
  "code": 200,
  "message": "结账成功"
}
```

---

## 3. 应收模块API

### 3.1 客户管理

#### 3.1.1 查询客户列表

**接口说明**: 分页查询客户列表

**请求信息**:
- **URL**: `/api/v1/ar/customers`
- **Method**: `GET`
- **权限**: `ar:customer:list`

**请求参数**:
| 参数名 | 类型 | 必填 | 说明 |
|--------|------|------|------|
| customerCode | String | N | 客户编码 |
| customerName | String | N | 客户名称 |
| customerType | Integer | N | 客户类型 |
| is_enabled | Integer | N | 是否启用 |
| pageNum | Integer | N | 页码 |
| pageSize | Integer | N | 每页条数 |

**响应示例**:
```json
{
  "code": 200,
  "message": "操作成功",
  "data": {
    "list": [
      {
        "id": 1,
        "customerCode": "C001",
        "customerName": "XX经销商",
        "customerType": 1,
        "customerTypeName": "经销商",
        "creditAmount": 1000000.00,
        "creditDays": 30,
        "contactPerson": "张三",
        "contactPhone": "13800138000",
        "isEnabled": 1
      }
    ],
    "total": 100
  }
}
```

---

#### 3.1.2 新增客户

**接口说明**: 新增客户

**请求信息**:
- **URL**: `/api/v1/ar/customers`
- **Method**: `POST`
- **权限**: `ar:customer:add`

**请求体**:
```json
{
  "customerCode": "C001",
  "customerName": "XX经销商",
  "customerType": 1,
  "taxNo": "91110000000000000X",
  "address": "北京市朝阳区",
  "contactPerson": "张三",
  "contactPhone": "13800138000",
  "creditAmount": 1000000.00,
  "creditDays": 30,
  "remark": ""
}
```

**响应示例**:
```json
{
  "code": 200,
  "message": "新增成功",
  "data": {
    "id": 1
  }
}
```

---

### 3.2 应收发票管理

#### 3.2.1 查询应收发票列表

**接口说明**: 分页查询应收发票列表

**请求信息**:
- **URL**: `/api/v1/ar/invoices`
- **Method**: `GET`
- **权限**: `ar:invoice:list`

**请求参数**:
| 参数名 | 类型 | 必填 | 说明 |
|--------|------|------|------|
| invoiceNo | String | N | 发票号 |
| customerId | Long | N | 客户ID |
| invoiceDateStart | String | N | 发票日期起 |
| invoiceDateEnd | String | N | 发票日期止 |
| status | Integer | N | 状态 |
| pageNum | Integer | N | 页码 |
| pageSize | Integer | N | 每页条数 |

**响应示例**:
```json
{
  "code": 200,
  "message": "操作成功",
  "data": {
    "list": [
      {
        "id": 1,
        "invoiceNo": "INV001",
        "invoiceType": 1,
        "customerId": 1,
        "customerCode": "C001",
        "customerName": "XX经销商",
        "invoiceDate": "2024-03-01",
        "amount": 10000.00,
        "taxAmount": 1300.00,
        "totalAmount": 11300.00,
        "writtenOffAmount": 0.00,
        "remainAmount": 11300.00,
        "status": 0,
        "statusName": "待审核"
      }
    ],
    "total": 100
  }
}
```

---

#### 3.2.2 新增应收发票

**接口说明**: 新增应收发票

**请求信息**:
- **URL**: `/api/v1/ar/invoices`
- **Method**: `POST`
- **权限**: `ar:invoice:add`

**请求体**:
```json
{
  "invoiceNo": "INV001",
  "customerId": 1,
  "invoiceDate": "2024-03-01",
  "taxRate": 13.00,
  "amount": 10000.00,
  "taxAmount": 1300.00,
  "totalAmount": 11300.00,
  "sourceType": "SALE_ORDER",
  "sourceId": 1,
  "remark": ""
}
```

**响应示例**:
```json
{
  "code": 200,
  "message": "新增成功",
  "data": {
    "id": 1
  }
}
```

---

### 3.3 收款管理

#### 3.3.1 查询收款单列表

**接口说明**: 分页查询收款单列表

**请求信息**:
- **URL**: `/api/v1/ar/receipts`
- **Method**: `GET`
- **权限**: `ar:receipt:list`

**请求参数**:
| 参数名 | 类型 | 必填 | 说明 |
|--------|------|------|------|
| receiptNo | String | N | 收款单号 |
| customerId | Long | N | 客户ID |
| receiptDateStart | String | N | 收款日期起 |
| receiptDateEnd | String | N | 收款日期止 |
| status | Integer | N | 状态 |
| pageNum | Integer | N | 页码 |
| pageSize | Integer | N | 每页条数 |

**响应示例**:
```json
{
  "code": 200,
  "message": "操作成功",
  "data": {
    "list": [
      {
        "id": 1,
        "receiptNo": "REC001",
        "customerId": 1,
        "customerCode": "C001",
        "customerName": "XX经销商",
        "receiptDate": "2024-03-01",
        "receiptType": 1,
        "paymentMethod": 2,
        "amount": 10000.00,
        "writtenOffAmount": 10000.00,
        "remainAmount": 0.00,
        "status": 1,
        "statusName": "已审核"
      }
    ],
    "total": 100
  }
}
```

---

#### 3.3.2 新增收款单

**接口说明**: 新增收款单

**请求信息**:
- **URL**: `/api/v1/ar/receipts`
- **Method**: `POST`
- **权限**: `ar:receipt:add`

**请求体**:
```json
{
  "customerId": 1,
  "receiptDate": "2024-03-01",
  "receiptType": 1,
  "paymentMethod": 2,
  "bankAccountId": 1,
  "amount": 10000.00,
  "remark": ""
}
```

**响应示例**:
```json
{
  "code": 200,
  "message": "新增成功",
  "data": {
    "id": 1,
    "receiptNo": "REC001"
  }
}
```

---

#### 3.3.3 核销应收账款

**接口说明**: 核销收款与应收发票

**请求信息**:
- **URL**: `/api/v1/ar/write-offs`
- **Method**: `POST`
- **权限**: `ar:writeoff:add`

**请求体**:
```json
{
  "customerId": 1,
  "writeOffDate": "2024-03-01",
  "items": [
    {
      "receiptId": 1,
      "invoiceId": 1,
      "writeOffAmount": 10000.00
    }
  ],
  "remark": ""
}
```

**响应示例**:
```json
{
  "code": 200,
  "message": "核销成功",
  "data": {
    "writeOffNo": "WO001"
  }
}
```

---

### 3.4 账龄分析

#### 3.4.1 查询应收账龄

**接口说明**: 查询应收账款账龄分析

**请求信息**:
- **URL**: `/api/v1/ar/aging`
- **Method**: `GET`
- **权限**: `ar:aging:query`

**请求参数**:
| 参数名 | 类型 | 必填 | 说明 |
|--------|------|------|------|
| asOfDate | String | Y | 截止日期 |
| customerId | Long | N | 客户ID |
| customerType | Integer | N | 客户类型 |

**响应示例**:
```json
{
  "code": 200,
  "message": "操作成功",
  "data": {
    "summary": {
      "totalAmount": 500000.00,
      "range0_30": 200000.00,
      "range31_60": 150000.00,
      "range61_90": 100000.00,
      "range91_180": 50000.00
    },
    "details": [
      {
        "customerId": 1,
        "customerCode": "C001",
        "customerName": "XX经销商",
        "totalAmount": 100000.00,
        "range0_30": 50000.00,
        "range31_60": 30000.00,
        "range61_90": 20000.00,
        "range91_180": 0.00
      }
    ]
  }
}
```

---

## 4. 应付模块API

### 4.1 供应商管理

#### 4.1.1 查询供应商列表

**接口说明**: 分页查询供应商列表

**请求信息**:
- **URL**: `/api/v1/ap/suppliers`
- **Method**: `GET`
- **权限**: `ap:supplier:list`

**请求参数**:
| 参数名 | 类型 | 必填 | 说明 |
|--------|------|------|------|
| supplierCode | String | N | 供应商编码 |
| supplierName | String | N | 供应商名称 |
| supplierType | Integer | N | 供应商类型 |
| is_enabled | Integer | N | 是否启用 |
| pageNum | Integer | N | 页码 |
| pageSize | Integer | N | 每页条数 |

**响应示例**:
```json
{
  "code": 200,
  "message": "操作成功",
  "data": {
    "list": [
      {
        "id": 1,
        "supplierCode": "S001",
        "supplierName": "XX零部件公司",
        "supplierType": 1,
        "supplierTypeName": "零部件供应商",
        "paymentDays": 30,
        "contactPerson": "李四",
        "contactPhone": "13900139000",
        "isEnabled": 1
      }
    ],
    "total": 100
  }
}
```

---

### 4.2 采购发票管理

#### 4.2.1 查询采购发票列表

**接口说明**: 分页查询采购发票列表

**请求信息**:
- **URL**: `/api/v1/ap/invoices`
- **Method**: `GET`
- **权限**: `ap:invoice:list`

**请求参数**:
| 参数名 | 类型 | 必填 | 说明 |
|--------|------|------|------|
| invoiceNo | String | N | 发票号 |
| supplierId | Long | N | 供应商ID |
| invoiceDateStart | String | N | 发票日期起 |
| invoiceDateEnd | String | N | 发票日期止 |
| status | Integer | N | 状态 |
| pageNum | Integer | N | 页码 |
| pageSize | Integer | N | 每页条数 |

**响应示例**:
```json
{
  "code": 200,
  "message": "操作成功",
  "data": {
    "list": [
      {
        "id": 1,
        "invoiceNo": "INV001",
        "invoiceType": 1,
        "supplierId": 1,
        "supplierCode": "S001",
        "supplierName": "XX零部件公司",
        "invoiceDate": "2024-03-01",
        "amount": 50000.00,
        "taxAmount": 6500.00,
        "totalAmount": 56500.00,
        "writtenOffAmount": 0.00,
        "remainAmount": 56500.00,
        "status": 0,
        "statusName": "待审核"
      }
    ],
    "total": 100
  }
}
```

---

### 4.3 付款管理

#### 4.3.1 查询付款申请列表

**接口说明**: 分页查询付款申请列表

**请求信息**:
- **URL**: `/api/v1/ap/payment-applies`
- **Method**: `GET`
- **权限**: `ap:payment:list`

**请求参数**:
| 参数名 | 类型 | 必填 | 说明 |
|--------|------|------|------|
| applyNo | String | N | 申请单号 |
| supplierId | Long | N | 供应商ID |
| applyDateStart | String | N | 申请日期起 |
| applyDateEnd | String | N | 申请日期止 |
| status | Integer | N | 状态 |
| pageNum | Integer | N | 页码 |
| pageSize | Integer | N | 每页条数 |

**响应示例**:
```json
{
  "code": 200,
  "message": "操作成功",
  "data": {
    "list": [
      {
        "id": 1,
        "applyNo": "PAY001",
        "supplierId": 1,
        "supplierCode": "S001",
        "supplierName": "XX零部件公司",
        "applyDate": "2024-03-01",
        "paymentType": 1,
        "paymentMethod": 2,
        "applyAmount": 50000.00,
        "paidAmount": 0.00,
        "status": 0,
        "statusName": "待审批"
      }
    ],
    "total": 100
  }
}
```

---

#### 4.3.2 新增付款申请

**接口说明**: 新增付款申请

**请求信息**:
- **URL**: `/api/v1/ap/payment-applies`
- **Method**: `POST`
- **权限**: `ap:payment:add`

**请求体**:
```json
{
  "supplierId": 1,
  "applyDate": "2024-03-01",
  "paymentType": 1,
  "paymentMethod": 2,
  "bankAccountId": 1,
  "applyAmount": 50000.00,
  "invoiceIds": [1, 2],
  "remark": ""
}
```

**响应示例**:
```json
{
  "code": 200,
  "message": "新增成功",
  "data": {
    "id": 1,
    "applyNo": "PAY001"
  }
}
```

---

### 4.4 经销商返利

#### 4.4.1 查询经销商返利列表

**接口说明**: 分页查询经销商返利列表

**请求信息**:
- **URL**: `/api/v1/ap/dealer-rebates`
- **Method**: `GET`
- **权限**: `ap:rebate:list`

**请求参数**:
| 参数名 | 类型 | 必填 | 说明 |
|--------|------|------|------|
| rebateNo | String | N | 返利单号 |
| customerId | Long | N | 经销商ID |
| fiscalYear | Integer | N | 会计年度 |
| periodNum | Integer | N | 期间号 |
| rebateType | Integer | N | 返利类型 |
| status | Integer | N | 状态 |
| pageNum | Integer | N | 页码 |
| pageSize | Integer | N | 每页条数 |

**响应示例**:
```json
{
  "code": 200,
  "message": "操作成功",
  "data": {
    "list": [
      {
        "id": 1,
        "rebateNo": "RB001",
        "customerId": 1,
        "customerCode": "C001",
        "customerName": "XX经销商",
        "fiscalYear": 2024,
        "periodNum": 3,
        "rebateType": 1,
        "rebateTypeName": "销量返利",
        "salesQuantity": 100,
        "rebateRate": 2.00,
        "rebateAmount": 50000.00,
        "paidAmount": 0.00,
        "status": 0,
        "statusName": "待确认"
      }
    ],
    "total": 100
  }
}
```

---

#### 4.4.2 计算经销商返利

**接口说明**: 计算经销商返利

**请求信息**:
- **URL**: `/api/v1/ap/dealer-rebates/calculate`
- **Method**: `POST`
- **权限**: `ap:rebate:calc`

**请求体**:
```json
{
  "fiscalYear": 2024,
  "periodNum": 3,
  "customerIds": [1, 2, 3]
}
```

**响应示例**:
```json
{
  "code": 200,
  "message": "计算成功",
  "data": {
    "totalRebateAmount": 150000.00,
    "details": [
      {
        "customerId": 1,
        "customerName": "XX经销商",
        "salesQuantity": 100,
        "rebateAmount": 50000.00
      }
    ]
  }
}
```

---

## 5. 固定资产模块API

### 5.1 资产卡片管理

#### 5.1.1 查询资产卡片列表

**接口说明**: 分页查询资产卡片列表

**请求信息**:
- **URL**: `/api/v1/fa/assets`
- **Method**: `GET`
- **权限**: `fa:asset:list`

**请求参数**:
| 参数名 | 类型 | 必填 | 说明 |
|--------|------|------|------|
| assetCode | String | N | 资产编码 |
| assetName | String | N | 资产名称 |
| categoryId | Long | N | 分类ID |
| useStatus | Integer | N | 使用状态 |
| assetStatus | Integer | N | 资产状态 |
| pageNum | Integer | N | 页码 |
| pageSize | Integer | N | 每页条数 |

**响应示例**:
```json
{
  "code": 200,
  "message": "操作成功",
  "data": {
    "list": [
      {
        "id": 1,
        "assetCode": "FA001",
        "assetName": "生产设备A",
        "categoryId": 1,
        "categoryName": "机器设备",
        "originalValue": 1000000.00,
        "accumDepreciation": 100000.00,
        "netValue": 900000.00,
        "useDepartmentName": "生产车间",
        "useStatus": 1,
        "useStatusName": "在用",
        "assetStatus": 1,
        "assetStatusName": "正常"
      }
    ],
    "total": 100
  }
}
```

---

#### 5.1.2 新增资产卡片

**接口说明**: 新增资产卡片

**请求信息**:
- **URL**: `/api/v1/fa/assets`
- **Method**: `POST`
- **权限**: `fa:asset:add`

**请求体**:
```json
{
  "assetName": "生产设备A",
  "categoryId": 1,
  "specification": "XX-100",
  "unit": "台",
  "originalValue": 1000000.00,
  "deprMethod": 1,
  "useYears": 10,
  "startDate": "2024-03-01",
  "useDepartmentId": 1,
  "location": "生产车间",
  "remark": ""
}
```

**响应示例**:
```json
{
  "code": 200,
  "message": "新增成功",
  "data": {
    "id": 1,
    "assetCode": "FA001"
  }
}
```

---

### 5.2 折旧管理

#### 5.2.1 查询折旧列表

**接口说明**: 分页查询折旧记录

**请求信息**:
- **URL**: `/api/v1/fa/depreciations`
- **Method**: `GET`
- **权限**: `fa:depr:list`

**请求参数**:
| 参数名 | 类型 | 必填 | 说明 |
|--------|------|------|------|
| fiscalYear | Integer | Y | 会计年度 |
| periodNum | Integer | Y | 期间号 |
| assetCode | String | N | 资产编码 |
| categoryId | Long | N | 分类ID |
| pageNum | Integer | N | 页码 |
| pageSize | Integer | N | 每页条数 |

**响应示例**:
```json
{
  "code": 200,
  "message": "操作成功",
  "data": {
    "list": [
      {
        "id": 1,
        "assetCode": "FA001",
        "assetName": "生产设备A",
        "categoryName": "机器设备",
        "originalValue": 1000000.00,
        "accumDeprBegin": 100000.00,
        "monthDepreciation": 7916.67,
        "accumDeprEnd": 107916.67,
        "netValue": 892083.33
      }
    ],
    "total": 100
  }
}
```

---

#### 5.2.2 执行折旧计提

**接口说明**: 执行折旧计提

**请求信息**:
- **URL**: `/api/v1/fa/depreciations/execute`
- **Method**: `POST`
- **权限**: `fa:depr:execute`

**请求体**:
```json
{
  "fiscalYear": 2024,
  "periodNum": 3
}
```

**响应示例**:
```json
{
  "code": 200,
  "message": "计提成功",
  "data": {
    "totalDepreciation": 150000.00,
    "assetCount": 50,
    "voucherId": 100
  }
}
```

---

### 5.3 资产变动

#### 5.3.1 资产调拨

**接口说明**: 资产调拨

**请求信息**:
- **URL**: `/api/v1/fa/asset-changes/transfer`
- **Method**: `POST`
- **权限**: `fa:asset:change`

**请求体**:
```json
{
  "assetId": 1,
  "changeDate": "2024-03-01",
  "oldDepartmentId": 1,
  "newDepartmentId": 2,
  "remark": "部门调整"
}
```

**响应示例**:
```json
{
  "code": 200,
  "message": "调拨成功",
  "data": {
    "changeNo": "AC001"
  }
}
```

---

### 5.4 资产处置

#### 5.4.1 资产报废

**接口说明**: 资产报废

**请求信息**:
- **URL**: `/api/v1/fa/assets/{id}/scrap`
- **Method**: `POST`
- **权限**: `fa:asset:dispose`

**请求体**:
```json
{
  "scrapDate": "2024-03-01",
  "scrapReason": "设备老化",
  "remark": ""
}
```

**响应示例**:
```json
{
  "code": 200,
  "message": "报废成功"
}
```

---

## 6. 资金管理模块API

### 6.1 银行账户管理

#### 6.1.1 查询银行账户列表

**接口说明**: 查询银行账户列表

**请求信息**:
- **URL**: `/api/v1/tr/bank-accounts`
- **Method**: `GET`
- **权限**: `tr:account:list`

**响应示例**:
```json
{
  "code": 200,
  "message": "操作成功",
  "data": [
    {
      "id": 1,
      "accountNo": "6222000000000000",
      "accountName": "基本户",
      "bankName": "中国银行",
      "accountType": 1,
      "currencyCode": "CNY",
      "balance": 1000000.00,
      "status": 1,
      "statusName": "正常"
    }
  ]
}
```

---

### 6.2 资金计划

#### 6.2.1 查询资金计划列表

**接口说明**: 分页查询资金计划列表

**请求信息**:
- **URL**: `/api/v1/tr/fund-plans`
- **Method**: `GET`
- **权限**: `tr:plan:list`

**响应示例**:
```json
{
  "code": 200,
  "message": "操作成功",
  "data": {
    "list": [
      {
        "id": 1,
        "planNo": "FP202403",
        "planName": "2024年3月资金计划",
        "planType": 1,
        "startDate": "2024-03-01",
        "endDate": "2024-03-31",
        "incomePlan": 5000000.00,
        "expensePlan": 4000000.00,
        "incomeActual": 4800000.00,
        "expenseActual": 4200000.00,
        "status": 2,
        "statusName": "执行中"
      }
    ],
    "total": 100
  }
}
```

---

### 6.3 票据管理

#### 6.3.1 查询票据列表

**接口说明**: 分页查询票据列表

**请求信息**:
- **URL**: `/api/v1/tr/bills`
- **Method**: `GET`
- **权限**: `tr:bill:list`

**响应示例**:
```json
{
  "code": 200,
  "message": "操作成功",
  "data": {
    "list": [
      {
        "id": 1,
        "billNo": "12345678",
        "billType": 1,
        "billTypeName": "银行承兑汇票",
        "billStatus": 1,
        "billStatusName": "持有",
        "issueDate": "2024-03-01",
        "dueDate": "2024-09-01",
        "issuer": "XX公司",
        "amount": 100000.00
      }
    ],
    "total": 100
  }
}
```

---

## 7. 财务报表模块API

### 7.1 标准财务报表

#### 7.1.1 生成资产负债表

**接口说明**: 生成资产负债表

**请求信息**:
- **URL**: `/api/v1/fr/reports/balance-sheet`
- **Method**: `GET`
- **权限**: `fr:report:query`

**请求参数**:
| 参数名 | 类型 | 必填 | 说明 |
|--------|------|------|------|
| fiscalYear | Integer | Y | 会计年度 |
| periodNum | Integer | Y | 期间号 |
| compareType | String | N | 对比类型(year/month) |

**响应示例**:
```json
{
  "code": 200,
  "message": "操作成功",
  "data": {
    "reportDate": "2024-03-31",
    "currency": "CNY",
    "unit": "元",
    "assets": [
      {
        "item": "流动资产",
        "amount": 5000000.00,
        "compareAmount": 4500000.00,
        "items": [
          {
            "item": "货币资金",
            "amount": 1000000.00,
            "compareAmount": 800000.00
          }
        ]
      }
    ],
    "liabilities": [],
    "equities": [],
    "totalAssets": 10000000.00,
    "totalLiabilitiesAndEquities": 10000000.00,
    "isBalanced": true
  }
}
```

---

#### 7.1.2 生成利润表

**接口说明**: 生成利润表

**请求信息**:
- **URL**: `/api/v1/fr/reports/income-statement`
- **Method**: `GET`
- **权限**: `fr:report:query`

**请求参数**:
| 参数名 | 类型 | 必填 | 说明 |
|--------|------|------|------|
| fiscalYear | Integer | Y | 会计年度 |
| periodNum | Integer | Y | 期间号 |
| compareType | String | N | 对比类型 |

**响应示例**:
```json
{
  "code": 200,
  "message": "操作成功",
  "data": {
    "reportPeriod": "2024年1-3月",
    "currency": "CNY",
    "unit": "元",
    "items": [
      {
        "item": "营业收入",
        "currentAmount": 5000000.00,
        "yearAmount": 15000000.00,
        "compareAmount": 4500000.00
      },
      {
        "item": "营业成本",
        "currentAmount": 3000000.00,
        "yearAmount": 9000000.00,
        "compareAmount": 2800000.00
      },
      {
        "item": "营业利润",
        "currentAmount": 1500000.00,
        "yearAmount": 4500000.00,
        "compareAmount": 1300000.00
      },
      {
        "item": "净利润",
        "currentAmount": 1125000.00,
        "yearAmount": 3375000.00,
        "compareAmount": 975000.00
      }
    ]
  }
}
```

---

### 7.2 成本分析报表

#### 7.2.1 整车成本分析

**接口说明**: 查询整车成本分析

**请求信息**:
- **URL**: `/api/v1/fr/reports/vehicle-cost`
- **Method**: `GET`
- **权限**: `fr:report:query`

**请求参数**:
| 参数名 | 类型 | 必填 | 说明 |
|--------|------|------|------|
| fiscalYear | Integer | Y | 会计年度 |
| periodNum | Integer | Y | 期间号 |
| vehicleModelId | Long | N | 车型ID |

**响应示例**:
```json
{
  "code": 200,
  "message": "操作成功",
  "data": {
    "vehicleModel": "车型A",
    "period": "2024年3月",
    "quantity": 100,
    "costItems": [
      {
        "item": "直接材料",
        "amount": 50000.00,
        "unitCost": 500.00,
        "percent": 60.00
      },
      {
        "item": "直接人工",
        "amount": 10000.00,
        "unitCost": 100.00,
        "percent": 12.00
      },
      {
        "item": "制造费用",
        "amount": 15000.00,
        "unitCost": 150.00,
        "percent": 18.00
      },
      {
        "item": "模具分摊",
        "amount": 5000.00,
        "unitCost": 50.00,
        "percent": 6.00
      },
      {
        "item": "研发分摊",
        "amount": 3000.00,
        "unitCost": 30.00,
        "percent": 4.00
      }
    ],
    "totalCost": 83000.00,
    "unitCost": 830.00
  }
}
```

---

## 8. 错误码定义

### 8.1 通用错误码

| 错误码 | 说明 |
|--------|------|
| 200 | 操作成功 |
| 400 | 参数错误 |
| 401 | 未授权 |
| 403 | 无权限 |
| 404 | 资源不存在 |
| 500 | 服务器内部错误 |

### 8.2 业务错误码

| 错误码 | 说明 |
|--------|------|
| 10001 | 科目编码已存在 |
| 10002 | 科目已使用，不可删除 |
| 10003 | 科目已使用，不可修改属性 |
| 10004 | 存在下级科目，不可删除 |
| 10101 | 借贷不平衡 |
| 10102 | 凭证日期不在开放期间 |
| 10103 | 凭证已审核，不可修改 |
| 10104 | 凭证已记账，不可修改 |
| 10105 | 制单人不可审核自己的凭证 |
| 10106 | 凭证号已存在 |
| 10201 | 期间已结账 |
| 10202 | 存在未记账凭证 |
| 10203 | 试算不平衡 |
| 10204 | 损益未结转 |
| 20001 | 客户编码已存在 |
| 20002 | 客户信用额度超限 |
| 20003 | 发票号已存在 |
| 20004 | 发票已核销，不可删除 |
| 30001 | 供应商编码已存在 |
| 30002 | 三单匹配不通过 |
| 40001 | 资产编码已存在 |
| 40002 | 资产已折旧，不可删除 |
| 40003 | 本期已计提折旧 |

---

## 9. 附录

### 9.1 修订历史
| 版本 | 日期 | 修订人 | 修订内容 |
|------|------|--------|----------|
| V1.0 | 2026-03-24 | 研发团队 | 初始版本 |

---

**文档结束**