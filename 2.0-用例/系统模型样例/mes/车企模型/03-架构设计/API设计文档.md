# 汽车整车装配MES系统 - API设计文档

**文档版本：** v1.0
**创建日期：** 2026-03-24
**作者：** MES架构组

---

## 一、API概述

### 1.1 接口规范

| 规范项 | 说明 |
|--------|------|
| 协议 | HTTPS |
| 风格 | RESTful |
| 数据格式 | JSON |
| 字符编码 | UTF-8 |
| 接口前缀 | /admin-api/mes |

### 1.2 请求规范

**请求头：**

| 参数名 | 类型 | 必填 | 说明 |
|--------|------|------|------|
| Authorization | String | 是 | Bearer {token} |
| tenant-id | Long | 是 | 租户ID |
| Content-Type | String | 是 | application/json |

### 1.3 响应规范

**标准响应结构：**

```json
{
  "code": 0,
  "msg": "success",
  "data": {}
}
```

**错误响应结构：**

```json
{
  "code": 1001,
  "msg": "工单不存在",
  "data": null
}
```

### 1.4 错误码定义

| 错误码 | 说明 |
|--------|------|
| 0 | 成功 |
| 1001 | 资源不存在 |
| 1002 | 参数错误 |
| 1003 | 状态不正确 |
| 1004 | 重复操作 |
| 2001 | 权限不足 |
| 2002 | Token失效 |
| 3001 | 业务规则校验失败 |

---

## 二、工单管理API

### 2.1 创建工单

**接口：** POST /admin-api/mes/work-order/create

**请求参数：**

```json
{
  "productCode": "MODEL-Y-001",
  "productName": "Model Y",
  "planQty": 100,
  "routingId": 1,
  "planStartTime": "2026-03-24 08:00:00",
  "planEndTime": "2026-03-24 17:00:00",
  "lineId": 1,
  "priority": 5,
  "remark": "备注"
}
```

**响应示例：**

```json
{
  "code": 0,
  "msg": "success",
  "data": 1
}
```

### 2.2 更新工单

**接口：** PUT /admin-api/mes/work-order/update

**请求参数：**

```json
{
  "id": 1,
  "planQty": 120,
  "planStartTime": "2026-03-24 09:00:00",
  "planEndTime": "2026-03-24 18:00:00",
  "priority": 8
}
```

### 2.3 获取工单详情

**接口：** GET /admin-api/mes/work-order/get?id=1

**响应示例：**

```json
{
  "code": 0,
  "msg": "success",
  "data": {
    "id": 1,
    "orderNo": "WO202603240001",
    "productCode": "MODEL-Y-001",
    "productName": "Model Y",
    "planQty": 100,
    "actualQty": 58,
    "routingId": 1,
    "routingName": "Model Y总装路线",
    "status": 2,
    "statusName": "生产中",
    "priority": 5,
    "planStartTime": "2026-03-24 08:00:00",
    "planEndTime": "2026-03-24 17:00:00",
    "lineId": 1,
    "lineName": "总装一线"
  }
}
```

### 2.4 工单列表查询

**接口：** GET /admin-api/mes/work-order/page

**请求参数：**

| 参数名 | 类型 | 必填 | 说明 |
|--------|------|------|------|
| pageNo | Integer | 否 | 页码，默认1 |
| pageSize | Integer | 否 | 每页数量，默认10 |
| orderNo | String | 否 | 工单编号 |
| status | Integer | 否 | 状态 |
| lineId | Long | 否 | 产线ID |
| startTime | String | 否 | 计划开始时间起 |
| endTime | String | 否 | 计划开始时间止 |

### 2.5 工单操作接口

| 接口 | 方法 | 路径 | 说明 |
|------|------|------|------|
| 下发工单 | PUT | /work-order/release?id=1 | 下发工单到产线 |
| 开始生产 | PUT | /work-order/start?id=1 | 开始执行工单 |
| 完成工单 | PUT | /work-order/complete?id=1 | 完成工单 |
| 关闭工单 | PUT | /work-order/close?id=1 | 关闭工单 |

---

## 三、工艺路线API

### 3.1 创建工艺路线

**接口：** POST /admin-api/mes/routing/create

**请求参数：**

```json
{
  "routingCode": "RT-001",
  "routingName": "Model Y总装路线",
  "productCode": "MODEL-Y-001",
  "productName": "Model Y",
  "version": "V1.0",
  "description": "Model Y整车装配工艺路线",
  "operations": [
    {
      "operationCode": "OP010",
      "operationName": "发动机装配",
      "sequence": 10,
      "workstationId": 1,
      "standardTime": 15.0,
      "keyOperation": true,
      "qualityCheck": true
    },
    {
      "operationCode": "OP020",
      "operationName": "变速箱装配",
      "sequence": 20,
      "workstationId": 2,
      "standardTime": 12.0,
      "keyOperation": false,
      "qualityCheck": false
    }
  ]
}
```

### 3.2 工艺路线API列表

| 接口 | 方法 | 路径 | 说明 |
|------|------|------|------|
| 创建路线 | POST | /routing/create | 创建工艺路线 |
| 更新路线 | PUT | /routing/update | 更新工艺路线 |
| 删除路线 | DELETE | /routing/delete?id=1 | 删除工艺路线 |
| 获取路线 | GET | /routing/get?id=1 | 获取路线详情 |
| 路线列表 | GET | /routing/page | 分页查询路线 |
| 生效路线 | PUT | /routing/activate?id=1 | 生效工艺路线 |
| 失效路线 | PUT | /routing/deactivate?id=1 | 失效工艺路线 |
| 复制路线 | POST | /routing/copy?id=1 | 复制工艺路线 |

### 3.3 工序管理API

| 接口 | 方法 | 路径 | 说明 |
|------|------|------|------|
| 添加工序 | POST | /operation/create | 添加工序到路线 |
| 更新工序 | PUT | /operation/update | 更新工序信息 |
| 删除工序 | DELETE | /operation/delete?id=1 | 删除工序 |
| 调整顺序 | PUT | /operation/sort | 调整工序顺序 |

---

## 四、工作站API

### 4.1 工作站API列表

| 接口 | 方法 | 路径 | 说明 |
|------|------|------|------|
| 创建工作站 | POST | /workstation/create | 创建工作站 |
| 更新工作站 | PUT | /workstation/update | 更新工作站 |
| 删除工作站 | DELETE | /workstation/delete?id=1 | 删除工作站 |
| 获取工作站 | GET | /workstation/get?id=1 | 获取工作站详情 |
| 工作站列表 | GET | /workstation/page | 分页查询 |
| 按产线查询 | GET | /workstation/list-by-line?lineId=1 | 按产线查询 |
| 启用工作站 | PUT | /workstation/enable?id=1 | 启用工作站 |
| 停用工作站 | PUT | /workstation/disable?id=1 | 停用工作站 |
| 绑定设备 | PUT | /workstation/bind-equipment | 绑定设备到工作站 |

---

## 五、装配作业API

### 5.1 扫码解析（核心接口）

**接口：** POST /admin-api/mes/operation/scan

**请求参数：**

```json
{
  "scanCode": "LSVAU2180N2123456",
  "workstationId": 1001,
  "operatorId": 100
}
```

**响应示例：**

```json
{
  "code": 0,
  "msg": "success",
  "data": {
    "scanType": "VIN",
    "vin": "LSVAU2180N2123456",
    "workOrderNo": "WO202603240001",
    "productName": "Model Y",
    "currentOperation": {
      "operationId": 2001,
      "operationCode": "OP010",
      "operationName": "发动机装配",
      "sequence": 10,
      "keyOperation": true,
      "keyParts": [
        {"partCode": "ENG001", "partName": "发动机总成", "required": true},
        {"partCode": "ECU001", "partName": "发动机ECU", "required": true}
      ]
    },
    "workstation": {
      "workstationId": 1001,
      "workstationCode": "A01",
      "workstationName": "发动机装配工位"
    },
    "instruction": "1. 检查发动机支架\n2. 安装发动机螺栓\n3. 扭矩: 120±5 N·m",
    "boundParts": [
      {"partCode": "ENG001", "partSn": "ENG-20260324001"}
    ]
  }
}
```

### 5.2 开始作业

**接口：** POST /admin-api/mes/operation/start

**请求参数：**

```json
{
  "vin": "LSVAU2180N2123456",
  "workOrderId": 1,
  "operationId": 2001,
  "workstationId": 1001,
  "operatorId": 100
}
```

### 5.3 完成作业

**接口：** PUT /admin-api/mes/operation/complete

**请求参数：**

```json
{
  "id": 1,
  "result": 0,
  "remark": "作业正常完成"
}
```

### 5.4 绑定关键件

**接口：** POST /admin-api/mes/operation/bind-part

**请求参数：**

```json
{
  "vin": "LSVAU2180N2123456",
  "workOrderId": 1,
  "partCode": "ENG001",
  "partName": "发动机总成",
  "partSn": "ENG-20260324001",
  "supplierCode": "SUP001",
  "workstationId": 1001,
  "operatorId": 100
}
```

### 5.5 作业记录查询

**接口：** GET /admin-api/mes/operation/record/page

**请求参数：**

| 参数名 | 类型 | 必填 | 说明 |
|--------|------|------|------|
| pageNo | Integer | 否 | 页码 |
| pageSize | Integer | 否 | 每页数量 |
| vin | String | 否 | VIN码 |
| workOrderNo | String | 否 | 工单编号 |
| operatorId | Long | 否 | 操作员ID |
| startTime | String | 否 | 开始时间起 |
| endTime | String | 否 | 开始时间止 |

### 5.6 车辆进度查询

**接口：** GET /admin-api/mes/operation/progress?vin=LSVAU2180N2123456

**响应示例：**

```json
{
  "code": 0,
  "data": {
    "vin": "LSVAU2180N2123456",
    "workOrderNo": "WO202603240001",
    "productName": "Model Y",
    "totalOperations": 20,
    "completedOperations": 8,
    "progress": 40.0,
    "operations": [
      {
        "operationCode": "OP010",
        "operationName": "发动机装配",
        "sequence": 10,
        "status": 1,
        "statusName": "已完成",
        "operatorName": "张三",
        "endTime": "2026-03-24 09:00:00"
      },
      {
        "operationCode": "OP020",
        "operationName": "变速箱装配",
        "sequence": 20,
        "status": 0,
        "statusName": "进行中",
        "operatorName": "李四"
      }
    ]
  }
}
```

---

## 六、物料管理API

### 6.1 物料管理API列表

| 接口 | 方法 | 路径 | 说明 |
|------|------|------|------|
| 库存查询 | GET | /stock/page | 分页查询线边库存 |
| 按工位查询 | GET | /stock/list-by-workstation?workstationId=1 | 按工位查询库存 |
| 库存预警列表 | GET | /stock/warning-list | 查询缺料预警列表 |
| 物料消耗 | POST | /stock/consume | 记录物料消耗 |
| 物料入库 | POST | /stock/in | 线边物料入库 |
| 配送申请 | POST | /stock/delivery-apply | 申请物料配送 |
| 盘点录入 | POST | /stock/inventory | 录入盘点结果 |

### 6.2 物料消耗

**接口：** POST /admin-api/mes/stock/consume

**请求参数：**

```json
{
  "vin": "LSVAU2180N2123456",
  "workOrderId": 1,
  "materialCode": "MAT001",
  "materialName": "螺栓M12",
  "qty": 4,
  "unit": "个",
  "workstationId": 1001,
  "operatorId": 100
}
```

---

## 七、质量管理API

### 7.1 质量管理API列表

| 接口 | 方法 | 路径 | 说明 |
|------|------|------|------|
| 创建检验记录 | POST | /quality/create | 创建检验记录 |
| 检验记录列表 | GET | /quality/page | 分页查询检验记录 |
| 不合格登记 | POST | /defect/create | 登记不合格问题 |
| 不合格处理 | PUT | /defect/handle | 处理不合格问题 |
| 不合格验证 | PUT | /defect/verify | 验证处理结果 |
| 不合格列表 | GET | /defect/page | 分页查询不合格记录 |

---

## 八、生产追溯API

### 8.1 VIN追溯查询（核心接口）

**接口：** GET /admin-api/mes/trace/vin?vin=LSVAU2180N2123456

**响应示例：**

```json
{
  "code": 0,
  "data": {
    "vin": "LSVAU2180N2123456",
    "vehicleInfo": {
      "productCode": "MODEL-Y-001",
      "productName": "Model Y",
      "color": "珍珠白",
      "config": "长续航版",
      "produceDate": "2026-03-24"
    },
    "workOrderInfo": {
      "orderNo": "WO202603240001",
      "planQty": 100,
      "actualQty": 58,
      "lineName": "总装一线"
    },
    "operationRecords": [
      {
        "operationCode": "OP010",
        "operationName": "发动机装配",
        "workstationName": "A01",
        "operatorName": "张三",
        "startTime": "2026-03-24 08:30:00",
        "endTime": "2026-03-24 08:45:00",
        "result": "合格"
      }
    ],
    "keyParts": [
      {
        "partCode": "ENG001",
        "partName": "发动机总成",
        "partSn": "ENG-20260324001",
        "supplierName": "XX发动机厂",
        "bindTime": "2026-03-24 08:35:00"
      }
    ],
    "qualityRecords": [
      {
        "checkType": "过程检",
        "checkItemName": "扭矩检验",
        "result": "合格",
        "inspectorName": "李四",
        "checkTime": "2026-03-24 08:45:00"
      }
    ],
    "deviceData": [
      {
        "deviceCode": "TQ-GUN-001",
        "deviceName": "扭矩枪1号",
        "torqueValue": 122.5,
        "torqueResult": "合格",
        "collectTime": "2026-03-24 08:43:00"
      }
    ]
  }
}
```

### 8.2 关键件反向追溯

**接口：** GET /admin-api/mes/trace/part?partSn=ENG-20260324001

**响应示例：**

```json
{
  "code": 0,
  "data": {
    "partCode": "ENG001",
    "partName": "发动机总成",
    "partSn": "ENG-20260324001",
    "supplierCode": "SUP001",
    "supplierName": "XX发动机厂",
    "bindVin": "LSVAU2180N2123456",
    "bindTime": "2026-03-24 08:35:00",
    "bindWorkstation": "A01",
    "bindOperator": "张三"
  }
}
```

---

## 九、设备集成API

### 9.1 扭矩数据接收

**接口：** POST /admin-api/mes/device/torque

**请求参数：**

```json
{
  "deviceCode": "TQ-GUN-001",
  "vin": "LSVAU2180N2123456",
  "torqueValue": 122.5,
  "angleValue": 180,
  "result": "OK",
  "timestamp": "2026-03-24T08:43:00"
}
```

### 9.2 设备状态上报

**接口：** POST /admin-api/mes/device/status

**请求参数：**

```json
{
  "deviceCode": "PLC-001",
  "deviceName": "主线PLC",
  "status": 1,
  "statusText": "运行",
  "ioSignals": [
    {"signalCode": "IO001", "signalName": "工位到位", "value": 1}
  ],
  "timestamp": "2026-03-24T08:43:00"
}
```

---

## 十、移动端API

### 10.1 移动端API前缀

移动端接口前缀：`/app-api/mes`

### 10.2 移动端API列表

| 接口 | 方法 | 路径 | 说明 |
|------|------|------|------|
| 用户登录 | POST | /auth/login | 用户登录认证 |
| 扫码解析 | POST | /operation/scan | 扫码解析并返回作业信息 |
| 开始作业 | POST | /operation/start | 开始工序作业 |
| 完成作业 | PUT | /operation/complete | 完成工序作业 |
| 绑定关键件 | POST | /operation/bind-part | 扫描绑定关键零部件 |
| 工单列表 | GET | /work-order/list | 查询工单列表 |
| 作业记录 | GET | /operation/records | 查询个人作业记录 |
| 异常上报 | POST | /exception/report | 上报作业异常 |

### 10.3 移动端登录

**接口：** POST /app-api/mes/auth/login

**请求参数：**

```json
{
  "username": "worker001",
  "password": "123456"
}
```

**响应示例：**

```json
{
  "code": 0,
  "data": {
    "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
    "userId": 100,
    "userName": "张三",
    "workstations": [
      {"id": 1001, "code": "A01", "name": "发动机装配工位"}
    ]
  }
}
```

---

## 十一、生产看板API

### 11.1 看板API列表

| 接口 | 方法 | 路径 | 说明 |
|------|------|------|------|
| 产线状态数据 | GET | /dashboard/line-status?lineId=1 | 获取产线实时状态数据 |
| 产量数据 | GET | /dashboard/production?lineId=1 | 获取产量统计数据 |
| OEE数据 | GET | /dashboard/oee?lineId=1 | 获取OEE数据 |
| 异常报警列表 | GET | /dashboard/alerts?lineId=1 | 获取异常报警列表 |
| 工位状态列表 | GET | /dashboard/workstation-status?lineId=1 | 获取工位状态列表 |

### 11.2 产线状态数据

**接口：** GET /admin-api/mes/dashboard/line-status?lineId=1

**响应示例：**

```json
{
  "code": 0,
  "data": {
    "lineId": 1,
    "lineName": "总装一线",
    "workOrderNo": "WO202603240001",
    "productName": "Model Y",
    "planQty": 100,
    "actualQty": 58,
    "progress": 58.0,
    "passRate": 98.3,
    "status": "生产中",
    "startTime": "2026-03-24 08:00:00",
    "planEndTime": "2026-03-24 17:00:00",
    "workstations": [
      {"code": "A01", "name": "发动机装配", "status": "正常"},
      {"code": "A02", "name": "变速箱装配", "status": "正常"},
      {"code": "A06", "name": "底盘合装", "status": "故障"}
    ],
    "alerts": [
      {"time": "10:23", "workstation": "A06", "type": "设备故障", "desc": "扭矩枪通讯异常", "status": "处理中"}
    ]
  }
}
```

---

## 十二、接口调用示例

### 12.1 完整作业流程示例

```bash
# 1. 扫码识别
curl -X POST "https://api.example.com/admin-api/mes/operation/scan" \
  -H "Authorization: Bearer {token}" \
  -H "tenant-id: 1" \
  -H "Content-Type: application/json" \
  -d '{"scanCode":"LSVAU2180N2123456","workstationId":1001,"operatorId":100}'

# 2. 绑定关键件
curl -X POST "https://api.example.com/admin-api/mes/operation/bind-part" \
  -H "Authorization: Bearer {token}" \
  -H "tenant-id: 1" \
  -H "Content-Type: application/json" \
  -d '{"vin":"LSVAU2180N2123456","workOrderId":1,"partCode":"ENG001","partName":"发动机总成","partSn":"ENG-20260324001","workstationId":1001,"operatorId":100}'

# 3. 完成作业
curl -X PUT "https://api.example.com/admin-api/mes/operation/complete" \
  -H "Authorization: Bearer {token}" \
  -H "tenant-id: 1" \
  -H "Content-Type: application/json" \
  -d '{"id":1,"result":0}'
```