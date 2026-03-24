# API-03-库存管理模块

## 文档信息

| 项目 | 内容 |
|------|------|
| 文档名称 | 库存管理模块API设计文档 |
| 文档编号 | API-03 |
| 版本号 | V1.0 |
| 创建日期 | 2026-03-24 |
| 所属系统 | 汽车制造业ERP系统 |
| 模块名称 | 库存管理 (WM) |
| 技术栈 | Spring Boot 2.7 + MyBatis Plus |

---

## 1. API设计规范

### 1.1 基础URL

```
开发环境: http://dev.example.com/api/v1
测试环境: http://test.example.com/api/v1
生产环境: http://api.example.com/api/v1
```

### 1.2 请求规范

#### 1.2.1 请求头

| 请求头 | 类型 | 必填 | 说明 |
|--------|------|------|------|
| Authorization | String | 是 | Bearer Token认证 |
| Content-Type | String | 是 | application/json |
| tenantId | Long | 是 | 租户ID |
| Accept-Language | String | 否 | 语言，默认zh-CN |

#### 1.2.2 请求方式

| 方法 | 说明 |
|------|------|
| GET | 查询资源 |
| POST | 创建资源 |
| PUT | 更新资源（全量） |
| PATCH | 更新资源（部分） |
| DELETE | 删除资源 |

### 1.3 响应规范

#### 1.3.1 统一响应格式

```json
{
  "code": 200,
  "message": "操作成功",
  "data": {},
  "timestamp": 1648099200000
}
```

#### 1.3.2 响应码定义

| 响应码 | 说明 |
|--------|------|
| 200 | 操作成功 |
| 400 | 请求参数错误 |
| 401 | 未授权 |
| 403 | 无权限 |
| 404 | 资源不存在 |
| 409 | 资源冲突 |
| 500 | 服务器内部错误 |

#### 1.3.3 分页响应格式

```json
{
  "code": 200,
  "message": "操作成功",
  "data": {
    "records": [],
    "total": 100,
    "size": 10,
    "current": 1,
    "pages": 10
  },
  "timestamp": 1648099200000
}
```

---

## 2. 库存台账API

### 2.1 库存查询

#### 2.1.1 分页查询库存列表

**接口描述**：分页查询库存列表

**请求信息**：
- URL: `/wm/stock/page`
- Method: GET
- 权限: wm:stock:list

**请求参数**：

| 参数名 | 类型 | 必填 | 说明 |
|--------|------|------|------|
| warehouseId | Long | 否 | 仓库ID |
| warehouseCode | String | 否 | 仓库编码 |
| materialCode | String | 否 | 物料编码 |
| materialName | String | 否 | 物料名称 |
| batchNo | String | 否 | 批次号 |
| vinCode | String | 否 | VIN码 |
| status | String | 否 | 库存状态 |
| current | Integer | 否 | 当前页，默认1 |
| size | Integer | 否 | 每页大小，默认10 |

**请求示例**：
```
GET /api/v1/wm/stock/page?warehouseId=1&materialCode=M001&current=1&size=10
```

**响应示例**：
```json
{
  "code": 200,
  "message": "操作成功",
  "data": {
    "records": [
      {
        "id": 1,
        "warehouseId": 1,
        "warehouseCode": "WH01",
        "warehouseName": "原材料仓",
        "locationId": 1,
        "locationCode": "LOC001",
        "materialId": 100,
        "materialCode": "M001",
        "materialName": "发动机总成",
        "batchNo": "B20260324001",
        "quantity": 100.0000,
        "availableQty": 80.0000,
        "lockedQty": 10.0000,
        "inspectQty": 10.0000,
        "status": "NORMAL",
        "unitCode": "PCS",
        "productionDate": "2026-03-01",
        "expiryDate": "2027-03-01"
      }
    ],
    "total": 100,
    "size": 10,
    "current": 1,
    "pages": 10
  },
  "timestamp": 1648099200000
}
```

---

#### 2.1.2 查询库存详情

**接口描述**：根据ID查询库存详情

**请求信息**：
- URL: `/wm/stock/{id}`
- Method: GET
- 权限: wm:stock:query

**路径参数**：

| 参数名 | 类型 | 必填 | 说明 |
|--------|------|------|------|
| id | Long | 是 | 库存ID |

**请求示例**：
```
GET /api/v1/wm/stock/1
```

**响应示例**：
```json
{
  "code": 200,
  "message": "操作成功",
  "data": {
    "id": 1,
    "warehouseId": 1,
    "warehouseCode": "WH01",
    "warehouseName": "原材料仓",
    "zoneId": 1,
    "zoneCode": "ZA01",
    "locationId": 1,
    "locationCode": "LOC001",
    "materialId": 100,
    "materialCode": "M001",
    "materialName": "发动机总成",
    "specModel": "V6 3.0T",
    "batchNo": "B20260324001",
    "vinCode": null,
    "unitId": 1,
    "unitCode": "PCS",
    "quantity": 100.0000,
    "availableQty": 80.0000,
    "lockedQty": 10.0000,
    "inspectQty": 10.0000,
    "status": "NORMAL",
    "productionDate": "2026-03-01",
    "expiryDate": "2027-03-01",
    "lastInTime": "2026-03-24 10:00:00",
    "lastOutTime": null,
    "isVmi": 0,
    "createTime": "2026-03-24 10:00:00",
    "createBy": "admin"
  },
  "timestamp": 1648099200000
}
```

---

#### 2.1.3 查询物料库存汇总

**接口描述**：查询物料在各仓库的库存汇总

**请求信息**：
- URL: `/wm/stock/summary`
- Method: GET
- 权限: wm:stock:summary

**请求参数**：

| 参数名 | 类型 | 必填 | 说明 |
|--------|------|------|------|
| materialCode | String | 是 | 物料编码 |

**请求示例**：
```
GET /api/v1/wm/stock/summary?materialCode=M001
```

**响应示例**：
```json
{
  "code": 200,
  "message": "操作成功",
  "data": {
    "materialCode": "M001",
    "materialName": "发动机总成",
    "totalQuantity": 500.0000,
    "totalAvailableQty": 400.0000,
    "totalLockedQty": 50.0000,
    "totalInspectQty": 50.0000,
    "warehouseSummary": [
      {
        "warehouseCode": "WH01",
        "warehouseName": "原材料仓",
        "quantity": 300.0000,
        "availableQty": 250.0000
      },
      {
        "warehouseCode": "WH02",
        "warehouseName": "线边仓",
        "quantity": 200.0000,
        "availableQty": 150.0000
      }
    ]
  },
  "timestamp": 1648099200000
}
```

---

### 2.2 库存流水

#### 2.2.1 分页查询库存流水

**接口描述**：分页查询库存流水记录

**请求信息**：
- URL: `/wm/stock/log/page`
- Method: GET
- 权限: wm:stock:log

**请求参数**：

| 参数名 | 类型 | 必填 | 说明 |
|--------|------|------|------|
| warehouseId | Long | 否 | 仓库ID |
| materialCode | String | 否 | 物料编码 |
| batchNo | String | 否 | 批次号 |
| vinCode | String | 否 | VIN码 |
| transType | String | 否 | 变动类型 |
| transNo | String | 否 | 单据号 |
| startTime | String | 否 | 开始时间 |
| endTime | String | 否 | 结束时间 |
| current | Integer | 否 | 当前页 |
| size | Integer | 否 | 每页大小 |

**请求示例**：
```
GET /api/v1/wm/stock/log/page?materialCode=M001&startTime=2026-03-01&endTime=2026-03-31&current=1&size=20
```

**响应示例**：
```json
{
  "code": 200,
  "message": "操作成功",
  "data": {
    "records": [
      {
        "id": 1,
        "logNo": "SL2026032400001",
        "warehouseCode": "WH01",
        "warehouseName": "原材料仓",
        "locationCode": "LOC001",
        "materialCode": "M001",
        "materialName": "发动机总成",
        "batchNo": "B20260324001",
        "transType": "RK01",
        "transTypeName": "采购入库",
        "transNo": "RK2026032400001",
        "direction": 1,
        "quantity": 100.0000,
        "beforeQty": 0.0000,
        "afterQty": 100.0000,
        "operTime": "2026-03-24 10:00:00",
        "operUserName": "张三"
      }
    ],
    "total": 50,
    "size": 20,
    "current": 1,
    "pages": 3
  },
  "timestamp": 1648099200000
}
```

---

### 2.3 VIN库存

#### 2.3.1 分页查询VIN库存

**接口描述**：分页查询整车VIN库存

**请求信息**：
- URL: `/wm/vin-stock/page`
- Method: GET
- 权限: wm:vin:list

**请求参数**：

| 参数名 | 类型 | 必填 | 说明 |
|--------|------|------|------|
| vinCode | String | 否 | VIN码（支持模糊查询） |
| modelCode | String | 否 | 车型编码 |
| warehouseId | Long | 否 | 仓库ID |
| stockStatus | String | 否 | 库存状态 |
| salesStatus | String | 否 | 销售状态 |
| inStartTime | String | 否 | 入库开始时间 |
| inEndTime | String | 否 | 入库结束时间 |
| current | Integer | 否 | 当前页 |
| size | Integer | 否 | 每页大小 |

**请求示例**：
```
GET /api/v1/wm/vin-stock/page?salesStatus=UNSALE&current=1&size=10
```

**响应示例**：
```json
{
  "code": 200,
  "message": "操作成功",
  "data": {
    "records": [
      {
        "id": 1,
        "vinCode": "LSVAU2180N2123456",
        "modelCode": "MODEL_A",
        "modelName": "Model A 轿车",
        "configCode": "CFG001",
        "configName": "豪华版",
        "exteriorColor": "极夜黑",
        "interiorColor": "黑色",
        "engineNo": "ENG001",
        "productionDate": "2026-03-01",
        "warehouseCode": "FG01",
        "warehouseName": "成品仓",
        "locationCode": "LOC001",
        "inTime": "2026-03-05 10:00:00",
        "stockDays": 19,
        "stockStatus": "NORMAL",
        "salesStatus": "UNSALE"
      }
    ],
    "total": 200,
    "size": 10,
    "current": 1,
    "pages": 20
  },
  "timestamp": 1648099200000
}
```

---

#### 2.3.2 查询VIN详情

**接口描述**：根据VIN码查询车辆详情

**请求信息**：
- URL: `/wm/vin-stock/{vinCode}`
- Method: GET
- 权限: wm:vin:query

**路径参数**：

| 参数名 | 类型 | 必填 | 说明 |
|--------|------|------|------|
| vinCode | String | 是 | VIN码 |

**请求示例**：
```
GET /api/v1/wm/vin-stock/LSVAU2180N2123456
```

**响应示例**：
```json
{
  "code": 200,
  "message": "操作成功",
  "data": {
    "id": 1,
    "vinCode": "LSVAU2180N2123456",
    "modelId": 1,
    "modelCode": "MODEL_A",
    "modelName": "Model A 轿车",
    "configId": 1,
    "configCode": "CFG001",
    "configName": "豪华版",
    "exteriorColor": "极夜黑",
    "interiorColor": "黑色",
    "engineNo": "ENG001",
    "motorNo": null,
    "productionDate": "2026-03-01",
    "warehouseId": 1,
    "warehouseCode": "FG01",
    "warehouseName": "成品仓",
    "zoneId": 1,
    "zoneCode": "ZA01",
    "locationId": 1,
    "locationCode": "LOC001",
    "inTime": "2026-03-05 10:00:00",
    "stockDays": 19,
    "stockStatus": "NORMAL",
    "salesStatus": "UNSALE",
    "orderId": null,
    "orderNo": null,
    "customerId": null,
    "customerName": null,
    "outTime": null,
    "createTime": "2026-03-05 10:00:00",
    "createBy": "admin"
  },
  "timestamp": 1648099200000
}
```

---

#### 2.3.3 VIN预订

**接口描述**：预订车辆

**请求信息**：
- URL: `/wm/vin-stock/reserve`
- Method: POST
- 权限: wm:vin:reserve

**请求体**：

```json
{
  "vinCode": "LSVAU2180N2123456",
  "orderId": 1001,
  "orderNo": "SO2026032400001",
  "customerId": 100,
  "customerName": "张三"
}
```

**响应示例**：
```json
{
  "code": 200,
  "message": "预订成功",
  "data": {
    "vinCode": "LSVAU2180N2123456",
    "salesStatus": "RESERVED"
  },
  "timestamp": 1648099200000
}
```

---

## 3. 入库管理API

### 3.1 入库单管理

#### 3.1.1 分页查询入库单

**接口描述**：分页查询入库单列表

**请求信息**：
- URL: `/wm/inbound/page`
- Method: GET
- 权限: wm:inbound:list

**请求参数**：

| 参数名 | 类型 | 必填 | 说明 |
|--------|------|------|------|
| orderNo | String | 否 | 入库单号 |
| orderType | String | 否 | 入库类型 |
| warehouseId | Long | 否 | 仓库ID |
| sourceOrderNo | String | 否 | 来源单据号 |
| status | String | 否 | 状态 |
| startTime | String | 否 | 开始时间 |
| endTime | String | 否 | 结束时间 |
| current | Integer | 否 | 当前页 |
| size | Integer | 否 | 每页大小 |

**请求示例**：
```
GET /api/v1/wm/inbound/page?orderType=RK01&status=COMPLETED&current=1&size=10
```

**响应示例**：
```json
{
  "code": 200,
  "message": "操作成功",
  "data": {
    "records": [
      {
        "id": 1,
        "orderNo": "RK2026032400001",
        "orderType": "RK01",
        "orderTypeName": "采购入库",
        "sourceOrderType": "PO",
        "sourceOrderNo": "PO2026032000001",
        "warehouseCode": "WH01",
        "warehouseName": "原材料仓",
        "supplierCode": "SUP001",
        "supplierName": "供应商A",
        "inboundDate": "2026-03-24",
        "totalQty": 100.0000,
        "totalLine": 2,
        "status": "COMPLETED",
        "statusName": "已完成",
        "createTime": "2026-03-24 10:00:00",
        "createBy": "张三"
      }
    ],
    "total": 50,
    "size": 10,
    "current": 1,
    "pages": 5
  },
  "timestamp": 1648099200000
}
```

---

#### 3.1.2 查询入库单详情

**接口描述**：根据ID查询入库单详情

**请求信息**：
- URL: `/wm/inbound/{id}`
- Method: GET
- 权限: wm:inbound:query

**路径参数**：

| 参数名 | 类型 | 必填 | 说明 |
|--------|------|------|------|
| id | Long | 是 | 入库单ID |

**请求示例**：
```
GET /api/v1/wm/inbound/1
```

**响应示例**：
```json
{
  "code": 200,
  "message": "操作成功",
  "data": {
    "id": 1,
    "orderNo": "RK2026032400001",
    "orderType": "RK01",
    "orderTypeName": "采购入库",
    "sourceOrderType": "PO",
    "sourceOrderId": 1001,
    "sourceOrderNo": "PO2026032000001",
    "warehouseId": 1,
    "warehouseCode": "WH01",
    "warehouseName": "原材料仓",
    "supplierId": 1,
    "supplierCode": "SUP001",
    "supplierName": "供应商A",
    "inboundDate": "2026-03-24",
    "totalQty": 100.0000,
    "totalLine": 2,
    "status": "COMPLETED",
    "statusName": "已完成",
    "approveUserId": 2,
    "approveUserName": "李四",
    "approveTime": "2026-03-24 11:00:00",
    "createTime": "2026-03-24 10:00:00",
    "createBy": "张三",
    "remark": null,
    "lines": [
      {
        "id": 1,
        "orderId": 1,
        "orderNo": "RK2026032400001",
        "lineNo": 1,
        "materialId": 100,
        "materialCode": "M001",
        "materialName": "发动机总成",
        "specModel": "V6 3.0T",
        "unitCode": "PCS",
        "sourceQty": 50.0000,
        "receivedQty": 50.0000,
        "thisQty": 50.0000,
        "batchNo": "B20260324001",
        "productionDate": "2026-03-01",
        "expiryDate": "2027-03-01",
        "locationCode": "LOC001",
        "inspectStatus": "QUALIFIED",
        "barcode": "WM-M001-20260324-00001"
      }
    ]
  },
  "timestamp": 1648099200000
}
```

---

#### 3.1.3 创建入库单

**接口描述**：创建入库单

**请求信息**：
- URL: `/wm/inbound`
- Method: POST
- 权限: wm:inbound:create

**请求体**：

```json
{
  "orderType": "RK01",
  "sourceOrderType": "PO",
  "sourceOrderId": 1001,
  "sourceOrderNo": "PO2026032000001",
  "warehouseId": 1,
  "warehouseCode": "WH01",
  "supplierId": 1,
  "supplierCode": "SUP001",
  "inboundDate": "2026-03-24",
  "remark": "正常入库",
  "lines": [
    {
      "materialId": 100,
      "materialCode": "M001",
      "materialName": "发动机总成",
      "specModel": "V6 3.0T",
      "unitCode": "PCS",
      "sourceQty": 50.0000,
      "thisQty": 50.0000,
      "batchNo": "B20260324001",
      "productionDate": "2026-03-01",
      "expiryDate": "2027-03-01",
      "locationCode": "LOC001"
    }
  ]
}
```

**响应示例**：
```json
{
  "code": 200,
  "message": "创建成功",
  "data": {
    "id": 1,
    "orderNo": "RK2026032400001"
  },
  "timestamp": 1648099200000
}
```

---

#### 3.1.4 更新入库单

**接口描述**：更新入库单信息

**请求信息**：
- URL: `/wm/inbound/{id}`
- Method: PUT
- 权限: wm:inbound:update

**路径参数**：

| 参数名 | 类型 | 必填 | 说明 |
|--------|------|------|------|
| id | Long | 是 | 入库单ID |

**请求体**：

```json
{
  "warehouseId": 1,
  "warehouseCode": "WH01",
  "inboundDate": "2026-03-24",
  "remark": "修改备注",
  "lines": [
    {
      "id": 1,
      "thisQty": 45.0000,
      "batchNo": "B20260324001",
      "locationCode": "LOC001"
    }
  ]
}
```

**响应示例**：
```json
{
  "code": 200,
  "message": "更新成功",
  "data": null,
  "timestamp": 1648099200000
}
```

---

#### 3.1.5 删除入库单

**接口描述**：删除入库单（仅草稿状态可删除）

**请求信息**：
- URL: `/wm/inbound/{id}`
- Method: DELETE
- 权限: wm:inbound:delete

**路径参数**：

| 参数名 | 类型 | 必填 | 说明 |
|--------|------|------|------|
| id | Long | 是 | 入库单ID |

**响应示例**：
```json
{
  "code": 200,
  "message": "删除成功",
  "data": null,
  "timestamp": 1648099200000
}
```

---

#### 3.1.6 提交审核

**接口描述**：提交入库单审核

**请求信息**：
- URL: `/wm/inbound/{id}/submit`
- Method: POST
- 权限: wm:inbound:submit

**路径参数**：

| 参数名 | 类型 | 必填 | 说明 |
|--------|------|------|------|
| id | Long | 是 | 入库单ID |

**响应示例**：
```json
{
  "code": 200,
  "message": "提交成功",
  "data": null,
  "timestamp": 1648099200000
}
```

---

#### 3.1.7 审核入库单

**接口描述**：审核入库单

**请求信息**：
- URL: `/wm/inbound/{id}/approve`
- Method: POST
- 权限: wm:inbound:approve

**路径参数**：

| 参数名 | 类型 | 必填 | 说明 |
|--------|------|------|------|
| id | Long | 是 | 入库单ID |

**请求体**：

```json
{
  "approved": true,
  "remark": "审核通过"
}
```

**响应示例**：
```json
{
  "code": 200,
  "message": "审核成功",
  "data": null,
  "timestamp": 1648099200000
}
```

---

#### 3.1.8 确认入库

**接口描述**：确认入库，更新库存

**请求信息**：
- URL: `/wm/inbound/{id}/confirm`
- Method: POST
- 权限: wm:inbound:confirm

**路径参数**：

| 参数名 | 类型 | 必填 | 说明 |
|--------|------|------|------|
| id | Long | 是 | 入库单ID |

**响应示例**：
```json
{
  "code": 200,
  "message": "入库成功",
  "data": {
    "orderNo": "RK2026032400001",
    "stockUpdated": true
  },
  "timestamp": 1648099200000
}
```

---

### 3.2 采购入库

#### 3.2.1 根据采购订单创建入库单

**接口描述**：根据采购订单创建入库单

**请求信息**：
- URL: `/wm/inbound/create-from-po`
- Method: POST
- 权限: wm:inbound:create

**请求体**：

```json
{
  "poOrderId": 1001,
  "poOrderNo": "PO2026032000001",
  "warehouseId": 1,
  "warehouseCode": "WH01",
  "lines": [
    {
      "poLineId": 1,
      "materialId": 100,
      "materialCode": "M001",
      "thisQty": 50.0000,
      "batchNo": "B20260324001",
      "locationCode": "LOC001"
    }
  ]
}
```

**响应示例**：
```json
{
  "code": 200,
  "message": "创建成功",
  "data": {
    "id": 1,
    "orderNo": "RK2026032400001"
  },
  "timestamp": 1648099200000
}
```

---

### 3.3 生产入库

#### 3.3.1 根据生产工单创建入库单

**接口描述**：根据生产工单创建入库单

**请求信息**：
- URL: `/wm/inbound/create-from-wo`
- Method: POST
- 权限: wm:inbound:create

**请求体**：

```json
{
  "woOrderId": 2001,
  "woOrderNo": "WO2026032000001",
  "warehouseId": 1,
  "warehouseCode": "FG01",
  "lines": [
    {
      "woLineId": 1,
      "materialId": 200,
      "materialCode": "FG001",
      "thisQty": 10.0000,
      "vinCodes": ["LSVAU2180N2123456", "LSVAU2180N2123457"]
    }
  ]
}
```

**响应示例**：
```json
{
  "code": 200,
  "message": "创建成功",
  "data": {
    "id": 1,
    "orderNo": "RK2026032400001"
  },
  "timestamp": 1648099200000
}
```

---

## 4. 出库管理API

### 4.1 出库单管理

#### 4.1.1 分页查询出库单

**接口描述**：分页查询出库单列表

**请求信息**：
- URL: `/wm/outbound/page`
- Method: GET
- 权限: wm:outbound:list

**请求参数**：

| 参数名 | 类型 | 必填 | 说明 |
|--------|------|------|------|
| orderNo | String | 否 | 出库单号 |
| orderType | String | 否 | 出库类型 |
| warehouseId | Long | 否 | 仓库ID |
| sourceOrderNo | String | 否 | 来源单据号 |
| status | String | 否 | 状态 |
| startTime | String | 否 | 开始时间 |
| endTime | String | 否 | 结束时间 |
| current | Integer | 否 | 当前页 |
| size | Integer | 否 | 每页大小 |

**请求示例**：
```
GET /api/v1/wm/outbound/page?orderType=CK02&current=1&size=10
```

**响应示例**：
```json
{
  "code": 200,
  "message": "操作成功",
  "data": {
    "records": [
      {
        "id": 1,
        "orderNo": "CK2026032400001",
        "orderType": "CK02",
        "orderTypeName": "销售出库",
        "sourceOrderType": "SO",
        "sourceOrderNo": "SO2026032000001",
        "warehouseCode": "FG01",
        "warehouseName": "成品仓",
        "customerCode": "C001",
        "customerName": "客户A",
        "outboundDate": "2026-03-24",
        "totalQty": 10.0000,
        "totalLine": 1,
        "pickingStatus": "COMPLETED",
        "status": "COMPLETED",
        "statusName": "已完成",
        "createTime": "2026-03-24 10:00:00",
        "createBy": "张三"
      }
    ],
    "total": 30,
    "size": 10,
    "current": 1,
    "pages": 3
  },
  "timestamp": 1648099200000
}
```

---

#### 4.1.2 查询出库单详情

**接口描述**：根据ID查询出库单详情

**请求信息**：
- URL: `/wm/outbound/{id}`
- Method: GET
- 权限: wm:outbound:query

**路径参数**：

| 参数名 | 类型 | 必填 | 说明 |
|--------|------|------|------|
| id | Long | 是 | 出库单ID |

**请求示例**：
```
GET /api/v1/wm/outbound/1
```

**响应示例**：
```json
{
  "code": 200,
  "message": "操作成功",
  "data": {
    "id": 1,
    "orderNo": "CK2026032400001",
    "orderType": "CK02",
    "orderTypeName": "销售出库",
    "sourceOrderType": "SO",
    "sourceOrderId": 3001,
    "sourceOrderNo": "SO2026032000001",
    "warehouseId": 1,
    "warehouseCode": "FG01",
    "warehouseName": "成品仓",
    "customerId": 1,
    "customerCode": "C001",
    "customerName": "客户A",
    "outboundDate": "2026-03-24",
    "totalQty": 10.0000,
    "totalLine": 1,
    "pickingStatus": "COMPLETED",
    "status": "COMPLETED",
    "statusName": "已完成",
    "logisticsNo": "SF1234567890",
    "createTime": "2026-03-24 10:00:00",
    "createBy": "张三",
    "remark": null,
    "lines": [
      {
        "id": 1,
        "orderId": 1,
        "orderNo": "CK2026032400001",
        "lineNo": 1,
        "materialId": 200,
        "materialCode": "FG001",
        "materialName": "整车Model A",
        "specModel": "豪华版",
        "unitCode": "PCS",
        "sourceQty": 10.0000,
        "outboundQty": 10.0000,
        "thisQty": 10.0000,
        "pickedQty": 10.0000,
        "batchNo": null,
        "locationCode": "LOC001",
        "pickingStrategy": "FIFO",
        "vinCodes": ["LSVAU2180N2123456", "LSVAU2180N2123457"]
      }
    ]
  },
  "timestamp": 1648099200000
}
```

---

#### 4.1.3 创建出库单

**接口描述**：创建出库单

**请求信息**：
- URL: `/wm/outbound`
- Method: POST
- 权限: wm:outbound:create

**请求体**：

```json
{
  "orderType": "CK02",
  "sourceOrderType": "SO",
  "sourceOrderId": 3001,
  "sourceOrderNo": "SO2026032000001",
  "warehouseId": 1,
  "warehouseCode": "FG01",
  "customerId": 1,
  "customerCode": "C001",
  "outboundDate": "2026-03-24",
  "remark": "正常出库",
  "lines": [
    {
      "materialId": 200,
      "materialCode": "FG001",
      "materialName": "整车Model A",
      "unitCode": "PCS",
      "sourceQty": 10.0000,
      "thisQty": 10.0000,
      "pickingStrategy": "FIFO",
      "vinCodes": ["LSVAU2180N2123456"]
    }
  ]
}
```

**响应示例**：
```json
{
  "code": 200,
  "message": "创建成功",
  "data": {
    "id": 1,
    "orderNo": "CK2026032400001"
  },
  "timestamp": 1648099200000
}
```

---

#### 4.1.4 确认出库

**接口描述**：确认出库，扣减库存

**请求信息**：
- URL: `/wm/outbound/{id}/confirm`
- Method: POST
- 权限: wm:outbound:confirm

**路径参数**：

| 参数名 | 类型 | 必填 | 说明 |
|--------|------|------|------|
| id | Long | 是 | 出库单ID |

**响应示例**：
```json
{
  "code": 200,
  "message": "出库成功",
  "data": {
    "orderNo": "CK2026032400001",
    "stockUpdated": true
  },
  "timestamp": 1648099200000
}
```

---

### 4.2 领料出库

#### 4.2.1 创建领料申请

**接口描述**：创建生产领料申请

**请求信息**：
- URL: `/wm/outbound/material-requisition`
- Method: POST
- 权限: wm:outbound:create

**请求体**：

```json
{
  "woOrderId": 2001,
  "woOrderNo": "WO2026032000001",
  "warehouseId": 1,
  "warehouseCode": "WH01",
  "requisitionType": "NORMAL",
  "remark": "正常领料",
  "lines": [
    {
      "materialId": 100,
      "materialCode": "M001",
      "materialName": "发动机总成",
      "unitCode": "PCS",
      "requestQty": 10.0000,
      "purpose": "生产领用"
    }
  ]
}
```

**响应示例**：
```json
{
  "code": 200,
  "message": "创建成功",
  "data": {
    "id": 1,
    "orderNo": "CK2026032400001"
  },
  "timestamp": 1648099200000
}
```

---

### 4.3 拣货管理

#### 4.3.1 生成拣货任务

**接口描述**：根据出库单生成拣货任务

**请求信息**：
- URL: `/wm/outbound/{id}/generate-picking`
- Method: POST
- 权限: wm:outbound:picking

**路径参数**：

| 参数名 | 类型 | 必填 | 说明 |
|--------|------|------|------|
| id | Long | 是 | 出库单ID |

**响应示例**：
```json
{
  "code": 200,
  "message": "生成成功",
  "data": {
    "pickingTasks": [
      {
        "taskId": 1,
        "materialCode": "M001",
        "materialName": "发动机总成",
        "locationCode": "LOC001",
        "pickQty": 10.0000,
        "batchNo": "B20260324001"
      }
    ]
  },
  "timestamp": 1648099200000
}
```

---

#### 4.3.2 确认拣货

**接口描述**：确认拣货完成

**请求信息**：
- URL: `/wm/outbound/picking/confirm`
- Method: POST
- 权限: wm:outbound:picking

**请求体**：

```json
{
  "orderId": 1,
  "lines": [
    {
      "lineId": 1,
      "pickedQty": 10.0000,
      "batchNo": "B20260324001",
      "locationCode": "LOC001"
    }
  ]
}
```

**响应示例**：
```json
{
  "code": 200,
  "message": "拣货确认成功",
  "data": null,
  "timestamp": 1648099200000
}
```

---

## 5. 库位管理API

### 5.1 仓库管理

#### 5.1.1 分页查询仓库

**接口描述**：分页查询仓库列表

**请求信息**：
- URL: `/wm/warehouse/page`
- Method: GET
- 权限: wm:warehouse:list

**请求参数**：

| 参数名 | 类型 | 必填 | 说明 |
|--------|------|------|------|
| warehouseCode | String | 否 | 仓库编码 |
| warehouseName | String | 否 | 仓库名称 |
| warehouseType | String | 否 | 仓库类型 |
| status | Integer | 否 | 状态 |
| current | Integer | 否 | 当前页 |
| size | Integer | 否 | 每页大小 |

**响应示例**：
```json
{
  "code": 200,
  "message": "操作成功",
  "data": {
    "records": [
      {
        "id": 1,
        "warehouseCode": "WH01",
        "warehouseName": "原材料仓",
        "warehouseType": "RAW",
        "warehouseTypeName": "原材料仓",
        "orgId": 1,
        "orgName": "总部",
        "address": "北京市朝阳区",
        "managerId": 1,
        "managerName": "张三",
        "phone": "13800138000",
        "isVmi": 0,
        "allowNegative": 0,
        "status": 1,
        "createTime": "2026-01-01 10:00:00"
      }
    ],
    "total": 10,
    "size": 10,
    "current": 1,
    "pages": 1
  },
  "timestamp": 1648099200000
}
```

---

#### 5.1.2 创建仓库

**接口描述**：创建仓库

**请求信息**：
- URL: `/wm/warehouse`
- Method: POST
- 权限: wm:warehouse:create

**请求体**：

```json
{
  "warehouseCode": "WH01",
  "warehouseName": "原材料仓",
  "warehouseType": "RAW",
  "orgId": 1,
  "address": "北京市朝阳区",
  "managerId": 1,
  "managerName": "张三",
  "phone": "13800138000",
  "isVmi": 0,
  "allowNegative": 0,
  "remark": "主要存储原材料"
}
```

**响应示例**：
```json
{
  "code": 200,
  "message": "创建成功",
  "data": {
    "id": 1,
    "warehouseCode": "WH01"
  },
  "timestamp": 1648099200000
}
```

---

### 5.2 库位管理

#### 5.2.1 分页查询库位

**接口描述**：分页查询库位列表

**请求信息**：
- URL: `/wm/location/page`
- Method: GET
- 权限: wm:location:list

**请求参数**：

| 参数名 | 类型 | 必填 | 说明 |
|--------|------|------|------|
| warehouseId | Long | 否 | 仓库ID |
| zoneId | Long | 否 | 库区ID |
| locationCode | String | 否 | 库位编码 |
| status | Integer | 否 | 状态 |
| current | Integer | 否 | 当前页 |
| size | Integer | 否 | 每页大小 |

**响应示例**：
```json
{
  "code": 200,
  "message": "操作成功",
  "data": {
    "records": [
      {
        "id": 1,
        "locationCode": "LOC001",
        "locationName": "A-01-01-01",
        "zoneId": 1,
        "zoneCode": "ZA01",
        "zoneName": "A区",
        "warehouseId": 1,
        "warehouseCode": "WH01",
        "warehouseName": "原材料仓",
        "locationType": "HIGH_RACK",
        "rowNo": 1,
        "columnNo": 1,
        "layerNo": 1,
        "capacity": 100.0000,
        "usedCapacity": 50.0000,
        "status": 1,
        "statusName": "启用"
      }
    ],
    "total": 100,
    "size": 10,
    "current": 1,
    "pages": 10
  },
  "timestamp": 1648099200000
}
```

---

#### 5.2.2 推荐库位

**接口描述**：根据物料信息推荐合适的库位

**请求信息**：
- URL: `/wm/location/recommend`
- Method: POST
- 权限: wm:location:recommend

**请求体**：

```json
{
  "warehouseId": 1,
  "materialId": 100,
  "materialCode": "M001",
  "quantity": 50.0000,
  "batchNo": "B20260324001"
}
```

**响应示例**：
```json
{
  "code": 200,
  "message": "操作成功",
  "data": {
    "recommendedLocations": [
      {
        "locationId": 1,
        "locationCode": "LOC001",
        "availableCapacity": 80.0000,
        "priority": 1,
        "reason": "同物料已存放"
      },
      {
        "locationId": 2,
        "locationCode": "LOC002",
        "availableCapacity": 100.0000,
        "priority": 2,
        "reason": "空库位"
      }
    ]
  },
  "timestamp": 1648099200000
}
```

---

## 6. 库存预警API

### 6.1 预警规则

#### 6.1.1 分页查询预警规则

**接口描述**：分页查询预警规则列表

**请求信息**：
- URL: `/wm/alert-rule/page`
- Method: GET
- 权限: wm:alert:list

**请求参数**：

| 参数名 | 类型 | 必填 | 说明 |
|--------|------|------|------|
| ruleCode | String | 否 | 规则编码 |
| ruleName | String | 否 | 规则名称 |
| alertType | String | 否 | 预警类型 |
| status | Integer | 否 | 状态 |
| current | Integer | 否 | 当前页 |
| size | Integer | 否 | 每页大小 |

**响应示例**：
```json
{
  "code": 200,
  "message": "操作成功",
  "data": {
    "records": [
      {
        "id": 1,
        "ruleCode": "AR001",
        "ruleName": "安全库存预警",
        "alertType": "SAFETY_STOCK",
        "alertTypeName": "安全库存",
        "materialScope": "ALL",
        "warehouseScope": "ALL",
        "thresholdValue": 10.0000,
        "alertLevel": "URGENT",
        "alertLevelName": "紧急",
        "notifyType": "MESSAGE,EMAIL",
        "status": 1,
        "createTime": "2026-01-01 10:00:00"
      }
    ],
    "total": 10,
    "size": 10,
    "current": 1,
    "pages": 1
  },
  "timestamp": 1648099200000
}
```

---

#### 6.1.2 创建预警规则

**接口描述**：创建预警规则

**请求信息**：
- URL: `/wm/alert-rule`
- Method: POST
- 权限: wm:alert:create

**请求体**：

```json
{
  "ruleCode": "AR001",
  "ruleName": "安全库存预警",
  "alertType": "SAFETY_STOCK",
  "materialScope": "ALL",
  "warehouseScope": "ALL",
  "thresholdValue": 10.0000,
  "alertLevel": "URGENT",
  "notifyType": "MESSAGE,EMAIL",
  "notifyUsers": "1,2,3"
}
```

**响应示例**：
```json
{
  "code": 200,
  "message": "创建成功",
  "data": {
    "id": 1,
    "ruleCode": "AR001"
  },
  "timestamp": 1648099200000
}
```

---

### 6.2 预警消息

#### 6.2.1 分页查询预警消息

**接口描述**：分页查询预警消息列表

**请求信息**：
- URL: `/wm/alert-message/page`
- Method: GET
- 权限: wm:alert:list

**请求参数**：

| 参数名 | 类型 | 必填 | 说明 |
|--------|------|------|------|
| alertType | String | 否 | 预警类型 |
| alertLevel | String | 否 | 预警级别 |
| status | String | 否 | 处理状态 |
| startTime | String | 否 | 开始时间 |
| endTime | String | 否 | 结束时间 |
| current | Integer | 否 | 当前页 |
| size | Integer | 否 | 每页大小 |

**响应示例**：
```json
{
  "code": 200,
  "message": "操作成功",
  "data": {
    "records": [
      {
        "id": 1,
        "messageNo": "AM2026032400001",
        "ruleCode": "AR001",
        "ruleName": "安全库存预警",
        "alertType": "SAFETY_STOCK",
        "alertTypeName": "安全库存",
        "alertLevel": "URGENT",
        "alertLevelName": "紧急",
        "warehouseCode": "WH01",
        "warehouseName": "原材料仓",
        "materialCode": "M001",
        "materialName": "发动机总成",
        "currentValue": 5.0000,
        "thresholdValue": 10.0000,
        "generateTime": "2026-03-24 10:00:00",
        "status": "PENDING",
        "statusName": "待处理"
      }
    ],
    "total": 20,
    "size": 10,
    "current": 1,
    "pages": 2
  },
  "timestamp": 1648099200000
}
```

---

#### 6.2.2 处理预警消息

**接口描述**：处理预警消息

**请求信息**：
- URL: `/wm/alert-message/{id}/handle`
- Method: POST
- 权限: wm:alert:handle

**路径参数**：

| 参数名 | 类型 | 必填 | 说明 |
|--------|------|------|------|
| id | Long | 是 | 预警消息ID |

**请求体**：

```json
{
  "handleRemark": "已安排采购补货"
}
```

**响应示例**：
```json
{
  "code": 200,
  "message": "处理成功",
  "data": null,
  "timestamp": 1648099200000
}
```

---

## 7. 条码管理API

### 7.1 条码生成

#### 7.1.1 生成条码

**接口描述**：生成物料条码

**请求信息**：
- URL: `/wm/barcode/generate`
- Method: POST
- 权限: wm:barcode:generate

**请求体**：

```json
{
  "ruleCode": "BR001",
  "materialId": 100,
  "materialCode": "M001",
  "batchNo": "B20260324001",
  "quantity": 1.0000,
  "generateCount": 10
}
```

**响应示例**：
```json
{
  "code": 200,
  "message": "生成成功",
  "data": {
    "barcodes": [
      {
        "id": 1,
        "barcode": "WM-M001-B20260324001-000001",
        "materialCode": "M001",
        "batchNo": "B20260324001",
        "quantity": 1.0000
      }
    ],
    "totalCount": 10
  },
  "timestamp": 1648099200000
}
```

---

#### 7.1.2 解析条码

**接口描述**：解析条码获取物料信息

**请求信息**：
- URL: `/wm/barcode/parse`
- Method: POST
- 权限: wm:barcode:query

**请求体**：

```json
{
  "barcode": "WM-M001-B20260324001-000001"
}
```

**响应示例**：
```json
{
  "code": 200,
  "message": "解析成功",
  "data": {
    "barcode": "WM-M001-B20260324001-000001",
    "materialId": 100,
    "materialCode": "M001",
    "materialName": "发动机总成",
    "batchNo": "B20260324001",
    "quantity": 1.0000,
    "status": "ACTIVE"
  },
  "timestamp": 1648099200000
}
```

---

### 7.2 条码打印

#### 7.2.1 获取打印数据

**接口描述**：获取条码打印数据

**请求信息**：
- URL: `/wm/barcode/print-data`
- Method: POST
- 权限: wm:barcode:print

**请求体**：

```json
{
  "barcodeIds": [1, 2, 3],
  "templateCode": "TPL001"
}
```

**响应示例**：
```json
{
  "code": 200,
  "message": "操作成功",
  "data": {
    "templateCode": "TPL001",
    "labels": [
      {
        "barcode": "WM-M001-B20260324001-000001",
        "materialCode": "M001",
        "materialName": "发动机总成",
        "batchNo": "B20260324001",
        "quantity": 1.0000,
        "productionDate": "2026-03-01",
        "expiryDate": "2027-03-01"
      }
    ]
  },
  "timestamp": 1648099200000
}
```

---

## 8. PDA接口API

### 8.1 入库扫描

#### 8.1.1 PDA入库扫描

**接口描述**：PDA扫描入库

**请求信息**：
- URL: `/pda/inbound/scan`
- Method: POST
- 权限: pda:inbound:scan

**请求体**：

```json
{
  "orderNo": "RK2026032400001",
  "barcode": "WM-M001-B20260324001-000001",
  "locationCode": "LOC001",
  "quantity": 1.0000
}
```

**响应示例**：
```json
{
  "code": 200,
  "message": "扫描成功",
  "data": {
    "materialCode": "M001",
    "materialName": "发动机总成",
    "scannedQty": 1.0000,
    "totalScannedQty": 5.0000,
    "remainingQty": 45.0000
  },
  "timestamp": 1648099200000
}
```

---

### 8.2 出库扫描

#### 8.2.1 PDA出库扫描

**接口描述**：PDA扫描出库

**请求信息**：
- URL: `/pda/outbound/scan`
- Method: POST
- 权限: pda:outbound:scan

**请求体**：

```json
{
  "orderNo": "CK2026032400001",
  "barcode": "WM-M001-B20260324001-000001",
  "quantity": 1.0000
}
```

**响应示例**：
```json
{
  "code": 200,
  "message": "扫描成功",
  "data": {
    "materialCode": "M001",
    "materialName": "发动机总成",
    "scannedQty": 1.0000,
    "totalScannedQty": 5.0000,
    "remainingQty": 5.0000
  },
  "timestamp": 1648099200000
}
```

---

### 8.3 库存查询

#### 8.3.1 PDA库存查询

**接口描述**：PDA扫描查询库存

**请求信息**：
- URL: `/pda/stock/query`
- Method: POST
- 权限: pda:stock:query

**请求体**：

```json
{
  "barcode": "WM-M001-B20260324001-000001"
}
```

**响应示例**：
```json
{
  "code": 200,
  "message": "查询成功",
  "data": {
    "materialCode": "M001",
    "materialName": "发动机总成",
    "batchNo": "B20260324001",
    "stockList": [
      {
        "warehouseCode": "WH01",
        "warehouseName": "原材料仓",
        "locationCode": "LOC001",
        "quantity": 50.0000,
        "availableQty": 40.0000
      }
    ]
  },
  "timestamp": 1648099200000
}
```

---

## 9. 错误码定义

| 错误码 | 说明 |
|--------|------|
| 10001 | 仓库不存在 |
| 10002 | 仓库编码已存在 |
| 10003 | 库位不存在 |
| 10004 | 库位容量不足 |
| 10005 | 库存不足 |
| 10006 | 库存已锁定 |
| 10007 | 入库单不存在 |
| 10008 | 入库单状态不允许操作 |
| 10009 | 入库数量超过订单数量 |
| 10010 | 出库单不存在 |
| 10011 | 出库单状态不允许操作 |
| 10012 | VIN码不存在 |
| 10013 | VIN码已存在 |
| 10014 | VIN码状态不允许操作 |
| 10015 | 条码不存在 |
| 10016 | 条码已使用 |
| 10017 | 批次号不存在 |

---

## 附录

### 附录A：API清单

| 模块 | 接口数量 | 说明 |
|------|----------|------|
| 库存台账 | 8 | 库存查询、流水、VIN库存 |
| 入库管理 | 12 | 入库单CRUD、采购入库、生产入库 |
| 出库管理 | 10 | 出库单CRUD、领料、拣货 |
| 库位管理 | 6 | 仓库、库区、库位管理 |
| 库存预警 | 6 | 预警规则、预警消息 |
| 条码管理 | 4 | 条码生成、解析、打印 |
| PDA接口 | 6 | 入库、出库、查询扫描 |
| **合计** | **52** | - |

### 附录B：版本历史

| 版本 | 日期 | 修改内容 | 修改人 |
|------|------|----------|--------|
| V1.0 | 2026-03-24 | 初始版本 | - |

---

**文档审批**

| 角色 | 姓名 | 审批日期 | 签名 |
|------|------|----------|------|
| 架构师 | | | |
| 后端负责人 | | | |
| 前端负责人 | | | |