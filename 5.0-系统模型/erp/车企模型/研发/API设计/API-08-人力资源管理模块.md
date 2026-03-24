# API-08 人力资源管理模块API设计文档

## 文档信息

| 项目 | 内容 |
|------|------|
| 文档编号 | API-08 |
| 文档名称 | 人力资源管理模块API设计文档 |
| 版本号 | V1.0 |
| 创建日期 | 2026-03-24 |
| 所属系统 | 汽车制造业ERP系统 |
| 技术栈 | Spring Boot 2.7 + MyBatis Plus |
| 关联PRD | PRD-08-人力资源管理模块 |

---

## 1. API设计规范

### 1.1 RESTful API规范

- 使用HTTP标准方法：GET(查询)、POST(创建)、PUT(更新)、DELETE(删除)
- URL使用小写字母和连字符
- 资源命名使用复数形式
- 版本号放在URL中：/api/v1/

### 1.2 请求响应格式

#### 统一响应格式

```json
{
  "code": 200,
  "message": "操作成功",
  "data": {},
  "timestamp": 1708329600000
}
```

#### 分页响应格式

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
  "timestamp": 1708329600000
}
```

### 1.3 错误码定义

| 错误码 | 说明 |
|--------|------|
| 200 | 操作成功 |
| 400 | 请求参数错误 |
| 401 | 未授权 |
| 403 | 无权限 |
| 404 | 资源不存在 |
| 500 | 服务器内部错误 |
| 10001 | 数据已存在 |
| 10002 | 数据不存在 |
| 10003 | 状态不允许操作 |

### 1.4 请求头

| 参数名 | 类型 | 必填 | 说明 |
|--------|------|------|------|
| Authorization | String | 是 | Bearer {token} |
| Content-Type | String | 是 | application/json |
| tenantId | Long | 是 | 租户ID |

---

## 2. 组织管理API

### 2.1 组织架构管理

#### 2.1.1 获取组织架构树

**接口说明**: 获取完整组织架构树形结构

**请求URL**: `GET /api/v1/hr/org/departments/tree`

**请求参数**:

| 参数名 | 类型 | 必填 | 说明 |
|--------|------|------|------|
| deptType | String | 否 | 组织类型过滤 |

**响应示例**:

```json
{
  "code": 200,
  "message": "操作成功",
  "data": [
    {
      "id": 1,
      "deptCode": "HQ",
      "deptName": "总部",
      "deptType": "company",
      "parentId": 0,
      "managerName": "张总",
      "employeeCount": 500,
      "children": [
        {
          "id": 2,
          "deptCode": "PROD",
          "deptName": "生产部",
          "deptType": "department",
          "parentId": 1,
          "managerName": "李经理",
          "employeeCount": 200,
          "children": []
        }
      ]
    }
  ]
}
```

#### 2.1.2 创建组织单元

**接口说明**: 创建新的组织单元

**请求URL**: `POST /api/v1/hr/org/departments`

**请求体**:

```json
{
  "deptCode": "PROD001",
  "deptName": "总装车间",
  "deptType": "department",
  "parentId": 1,
  "managerId": 100,
  "costCenter": "CC001",
  "remark": "备注信息"
}
```

**响应示例**:

```json
{
  "code": 200,
  "message": "组织创建成功",
  "data": {
    "id": 3,
    "deptCode": "PROD001",
    "deptName": "总装车间"
  }
}
```

#### 2.1.3 更新组织单元

**接口说明**: 更新组织单元信息

**请求URL**: `PUT /api/v1/hr/org/departments/{id}`

**请求体**:

```json
{
  "deptName": "总装一车间",
  "managerId": 101,
  "remark": "更新备注"
}
```

#### 2.1.4 删除组织单元

**接口说明**: 删除组织单元（需无下级和人员）

**请求URL**: `DELETE /api/v1/hr/org/departments/{id}`

**响应示例**:

```json
{
  "code": 200,
  "message": "组织删除成功"
}
```

#### 2.1.5 获取组织单元详情

**接口说明**: 获取组织单元详细信息

**请求URL**: `GET /api/v1/hr/org/departments/{id}`

**响应示例**:

```json
{
  "code": 200,
  "message": "操作成功",
  "data": {
    "id": 1,
    "deptCode": "PROD001",
    "deptName": "总装车间",
    "deptType": "department",
    "parentId": 1,
    "parentName": "生产部",
    "managerId": 100,
    "managerName": "张三",
    "costCenter": "CC001",
    "employeeCount": 50,
    "status": 1,
    "createdTime": "2024-01-01 10:00:00"
  }
}
```

### 2.2 岗位管理

#### 2.2.1 获取岗位列表

**接口说明**: 分页查询岗位列表

**请求URL**: `GET /api/v1/hr/org/positions`

**请求参数**:

| 参数名 | 类型 | 必填 | 说明 |
|--------|------|------|------|
| deptId | Long | 否 | 部门ID |
| positionName | String | 否 | 岗位名称 |
| status | Integer | 否 | 状态 |
| page | Integer | 否 | 页码，默认1 |
| size | Integer | 否 | 每页条数，默认10 |

**响应示例**:

```json
{
  "code": 200,
  "message": "操作成功",
  "data": {
    "records": [
      {
        "id": 1,
        "positionCode": "POS001",
        "positionName": "装配工",
        "deptId": 1,
        "deptName": "总装车间",
        "positionType": "operation",
        "positionLevel": "P3",
        "headcount": 50,
        "currentCount": 45,
        "vacancyCount": 5,
        "status": 1
      }
    ],
    "total": 100,
    "size": 10,
    "current": 1,
    "pages": 10
  }
}
```

#### 2.2.2 创建岗位

**接口说明**: 创建新岗位

**请求URL**: `POST /api/v1/hr/org/positions`

**请求体**:

```json
{
  "positionCode": "POS001",
  "positionName": "装配工",
  "deptId": 1,
  "positionType": "operation",
  "positionLevel": "P3",
  "headcount": 50,
  "jobDescription": "负责汽车装配工作",
  "qualification": "高中以上学历"
}
```

#### 2.2.3 更新岗位

**接口说明**: 更新岗位信息

**请求URL**: `PUT /api/v1/hr/org/positions/{id}`

#### 2.2.4 删除岗位

**接口说明**: 删除岗位

**请求URL**: `DELETE /api/v1/hr/org/positions/{id}`

---

## 3. 员工档案管理API

### 3.1 员工信息管理

#### 3.1.1 获取员工列表

**接口说明**: 分页查询员工列表

**请求URL**: `GET /api/v1/hr/emp/employees`

**请求参数**:

| 参数名 | 类型 | 必填 | 说明 |
|--------|------|------|------|
| employeeNo | String | 否 | 员工工号 |
| employeeName | String | 否 | 员工姓名(模糊) |
| deptId | Long | 否 | 部门ID |
| employeeStatus | String | 否 | 员工状态 |
| page | Integer | 否 | 页码 |
| size | Integer | 否 | 每页条数 |

**响应示例**:

```json
{
  "code": 200,
  "message": "操作成功",
  "data": {
    "records": [
      {
        "id": 1,
        "employeeNo": "EMP001",
        "employeeName": "张三",
        "gender": "M",
        "mobile": "138****8000",
        "deptId": 1,
        "deptName": "生产部",
        "positionName": "装配工",
        "employeeStatus": "REGULAR",
        "hireDate": "2024-01-01"
      }
    ],
    "total": 500,
    "size": 10,
    "current": 1,
    "pages": 50
  }
}
```

#### 3.1.2 获取员工详情

**接口说明**: 获取员工完整档案信息

**请求URL**: `GET /api/v1/hr/emp/employees/{id}`

**响应示例**:

```json
{
  "code": 200,
  "message": "操作成功",
  "data": {
    "id": 1,
    "employeeNo": "EMP001",
    "employeeName": "张三",
    "gender": "M",
    "birthday": "1990-01-15",
    "idType": "ID_CARD",
    "idNumber": "1101**********0011",
    "email": "zhangsan@example.com",
    "mobile": "13800138000",
    "address": "北京市朝阳区",
    "emergencyContact": "李四",
    "emergencyPhone": "13900139000",
    "photoUrl": "http://xxx/photo.jpg",
    "deptId": 1,
    "deptName": "生产部",
    "positionId": 1,
    "positionName": "装配工",
    "positionLevel": "P3",
    "employeeType": "FULL_TIME",
    "employeeStatus": "REGULAR",
    "hireDate": "2024-01-01",
    "regularDate": "2024-04-01",
    "workYears": 2.5,
    "bankName": "中国银行",
    "bankAccount": "6216**********1234",
    "educations": [
      {
        "schoolName": "北京理工大学",
        "major": "机械工程",
        "education": "BACHELOR",
        "startDate": "2008-09-01",
        "endDate": "2012-06-30"
      }
    ],
    "workExperiences": [
      {
        "companyName": "某汽车公司",
        "position": "装配工",
        "startDate": "2012-07-01",
        "endDate": "2023-12-31"
      }
    ]
  }
}
```

#### 3.1.3 创建员工档案

**接口说明**: 新建员工档案

**请求URL**: `POST /api/v1/hr/emp/employees`

**请求体**:

```json
{
  "employeeNo": "EMP001",
  "employeeName": "张三",
  "gender": "M",
  "birthday": "1990-01-15",
  "idType": "ID_CARD",
  "idNumber": "110101199001150011",
  "email": "zhangsan@example.com",
  "mobile": "13800138000",
  "address": "北京市朝阳区",
  "emergencyContact": "李四",
  "emergencyPhone": "13900139000",
  "deptId": 1,
  "positionId": 1,
  "employeeType": "FULL_TIME",
  "hireDate": "2024-01-01",
  "bankName": "中国银行",
  "bankAccount": "6216000000001234"
}
```

#### 3.1.4 更新员工档案

**接口说明**: 更新员工档案信息

**请求URL**: `PUT /api/v1/hr/emp/employees/{id}`

#### 3.1.5 获取员工教育经历

**接口说明**: 获取员工教育经历列表

**请求URL**: `GET /api/v1/hr/emp/employees/{employeeId}/educations`

#### 3.1.6 添加教育经历

**接口说明**: 添加员工教育经历

**请求URL**: `POST /api/v1/hr/emp/employees/{employeeId}/educations`

**请求体**:

```json
{
  "schoolName": "北京理工大学",
  "major": "机械工程",
  "education": "BACHELOR",
  "degree": "BACHELOR",
  "startDate": "2008-09-01",
  "endDate": "2012-06-30",
  "certificateNo": "CERT001",
  "isHighest": 1
}
```

### 3.2 入职管理

#### 3.2.1 创建入职申请

**接口说明**: 发起员工入职申请

**请求URL**: `POST /api/v1/hr/emp/entry/apply`

**请求体**:

```json
{
  "candidateName": "张三",
  "mobile": "13800138000",
  "email": "zhangsan@example.com",
  "deptId": 1,
  "positionId": 1,
  "hireDate": "2024-06-01",
  "salary": 8000,
  "probationMonths": 3,
  "attachments": [
    {
      "type": "ID_CARD",
      "url": "http://xxx/idcard.jpg"
    },
    {
      "type": "DIPLOMA",
      "url": "http://xxx/diploma.jpg"
    }
  ]
}
```

#### 3.2.2 审批入职申请

**接口说明**: 审批入职申请

**请求URL**: `POST /api/v1/hr/emp/entry/{id}/approve`

**请求体**:

```json
{
  "approved": true,
  "remark": "同意入职"
}
```

### 3.3 离职管理

#### 3.3.1 提交离职申请

**接口说明**: 员工提交离职申请

**请求URL**: `POST /api/v1/hr/emp/leave/apply`

**请求体**:

```json
{
  "leaveType": "PERSONAL",
  "leaveReason": "个人发展",
  "expectedLeaveDate": "2024-07-31",
  "remark": "感谢公司培养"
}
```

#### 3.3.2 审批离职申请

**接口说明**: 审批离职申请

**请求URL**: `POST /api/v1/hr/emp/leave/{id}/approve`

### 3.4 异动管理

#### 3.4.1 发起调动申请

**接口说明**: 发起员工调动申请

**请求URL**: `POST /api/v1/hr/emp/transfer/apply`

**请求体**:

```json
{
  "employeeId": 1,
  "changeType": "TRANSFER",
  "afterDeptId": 2,
  "afterPositionId": 3,
  "afterLevel": "P4",
  "effectDate": "2024-07-01",
  "changeReason": "业务需要"
}
```

#### 3.4.2 获取异动记录

**接口说明**: 获取员工异动记录列表

**请求URL**: `GET /api/v1/hr/emp/employees/{employeeId}/changes`

---

## 4. 考勤管理API

### 4.1 排班管理

#### 4.1.1 获取班次列表

**接口说明**: 获取所有班次定义

**请求URL**: `GET /api/v1/hr/att/shifts`

**响应示例**:

```json
{
  "code": 200,
  "message": "操作成功",
  "data": [
    {
      "id": 1,
      "shiftCode": "DAY",
      "shiftName": "白班",
      "onTime": "08:00",
      "offTime": "17:00",
      "lateMinutes": 10,
      "earlyMinutes": 10,
      "workHours": 8.0
    }
  ]
}
```

#### 4.1.2 创建排班计划

**接口说明**: 批量创建排班计划

**请求URL**: `POST /api/v1/hr/att/schedules`

**请求体**:

```json
{
  "employeeIds": [1, 2, 3],
  "startDate": "2024-06-01",
  "endDate": "2024-06-30",
  "shiftId": 1,
  "remark": "6月份排班"
}
```

#### 4.1.3 获取排班日历

**接口说明**: 获取员工排班日历

**请求URL**: `GET /api/v1/hr/att/schedules/calendar`

**请求参数**:

| 参数名 | 类型 | 必填 | 说明 |
|--------|------|------|------|
| employeeId | Long | 是 | 员工ID |
| startDate | Date | 是 | 开始日期 |
| endDate | Date | 是 | 结束日期 |

**响应示例**:

```json
{
  "code": 200,
  "message": "操作成功",
  "data": [
    {
      "date": "2024-06-01",
      "shiftId": 1,
      "shiftName": "白班",
      "onTime": "08:00",
      "offTime": "17:00"
    }
  ]
}
```

### 4.2 考勤打卡

#### 4.2.1 上班打卡

**接口说明**: 员工上班打卡

**请求URL**: `POST /api/v1/hr/att/clock-in`

**请求体**:

```json
{
  "clockTime": "2024-06-01 08:00:00",
  "clockType": "ON",
  "deviceId": "DEVICE001",
  "location": "北京市朝阳区xxx",
  "longitude": 116.4074,
  "latitude": 39.9042,
  "photoUrl": "http://xxx/photo.jpg"
}
```

**响应示例**:

```json
{
  "code": 200,
  "message": "打卡成功",
  "data": {
    "clockTime": "2024-06-01 08:00:00",
    "clockStatus": "NORMAL",
    "shiftName": "白班",
    "onTime": "08:00"
  }
}
```

#### 4.2.2 下班打卡

**接口说明**: 员工下班打卡

**请求URL**: `POST /api/v1/hr/att/clock-out`

#### 4.2.3 获取今日考勤状态

**接口说明**: 获取员工今日考勤状态

**请求URL**: `GET /api/v1/hr/att/today-status`

**响应示例**:

```json
{
  "code": 200,
  "message": "操作成功",
  "data": {
    "date": "2024-06-01",
    "shiftName": "白班",
    "onTime": "08:00",
    "offTime": "17:00",
    "onClockTime": "07:55",
    "onClockStatus": "NORMAL",
    "offClockTime": null,
    "offClockStatus": null,
    "workHours": 0
  }
}
```

### 4.3 请假管理

#### 4.3.1 获取假期类型列表

**接口说明**: 获取所有假期类型

**请求URL**: `GET /api/v1/hr/att/leave-types`

#### 4.3.2 获取假期余额

**接口说明**: 获取员工假期余额

**请求URL**: `GET /api/v1/hr/att/leave-balance`

**请求参数**:

| 参数名 | 类型 | 必填 | 说明 |
|--------|------|------|------|
| employeeId | Long | 是 | 员工ID |
| year | Integer | 是 | 年度 |

**响应示例**:

```json
{
  "code": 200,
  "message": "操作成功",
  "data": [
    {
      "leaveTypeId": 1,
      "leaveTypeName": "年假",
      "totalDays": 10.0,
      "usedDays": 3.0,
      "remainingDays": 7.0,
      "expireDate": "2024-12-31"
    }
  ]
}
```

#### 4.3.3 提交请假申请

**接口说明**: 提交请假申请

**请求URL**: `POST /api/v1/hr/att/leave/apply`

**请求体**:

```json
{
  "leaveTypeId": 1,
  "startDate": "2024-06-10",
  "endDate": "2024-06-11",
  "startTime": "09:00",
  "endTime": "18:00",
  "leaveDays": 2.0,
  "leaveReason": "家中有事",
  "attachmentUrl": "http://xxx/proof.jpg"
}
```

#### 4.3.4 审批请假申请

**接口说明**: 审批请假申请

**请求URL**: `POST /api/v1/hr/att/leave/{id}/approve`

**请求体**:

```json
{
  "approved": true,
  "remark": "同意请假"
}
```

### 4.4 加班管理

#### 4.4.1 提交加班申请

**接口说明**: 提交加班申请

**请求URL**: `POST /api/v1/hr/att/overtime/apply`

**请求体**:

```json
{
  "overtimeDate": "2024-06-15",
  "startTime": "18:00",
  "endTime": "21:00",
  "overtimeHours": 3.0,
  "compensateType": "PAY",
  "overtimeReason": "项目紧急"
}
```

#### 4.4.2 审批加班申请

**接口说明**: 审批加班申请

**请求URL**: `POST /api/v1/hr/att/overtime/{id}/approve`

### 4.5 考勤统计

#### 4.5.1 获取考勤日报

**接口说明**: 获取部门考勤日报

**请求URL**: `GET /api/v1/hr/att/daily-report`

**请求参数**:

| 参数名 | 类型 | 必填 | 说明 |
|--------|------|------|------|
| date | Date | 是 | 日期 |
| deptId | Long | 否 | 部门ID |

**响应示例**:

```json
{
  "code": 200,
  "message": "操作成功",
  "data": {
    "date": "2024-06-01",
    "totalEmployee": 100,
    "actualEmployee": 95,
    "lateEmployee": 3,
    "earlyEmployee": 2,
    "absentEmployee": 1,
    "leaveEmployee": 5,
    "businessEmployee": 2,
    "details": []
  }
}
```

#### 4.5.2 获取考勤月报

**接口说明**: 获取部门考勤月报

**请求URL**: `GET /api/v1/hr/att/monthly-report`

**请求参数**:

| 参数名 | 类型 | 必填 | 说明 |
|--------|------|------|------|
| month | String | 是 | 月份(yyyy-MM) |
| deptId | Long | 否 | 部门ID |

---

## 5. 薪资管理API

### 5.1 薪资体系

#### 5.1.1 获取薪资等级列表

**接口说明**: 获取薪资等级列表

**请求URL**: `GET /api/v1/hr/sal/grades`

#### 5.1.2 创建薪资等级

**接口说明**: 创建薪资等级

**请求URL**: `POST /api/v1/hr/sal/grades`

**请求体**:

```json
{
  "gradeCode": "G01",
  "gradeName": "P1级",
  "positionLevel": "P1",
  "minSalary": 5000,
  "midSalary": 6500,
  "maxSalary": 8000
}
```

#### 5.1.3 获取薪资项目列表

**接口说明**: 获取薪资项目列表

**请求URL**: `GET /api/v1/hr/sal/items`

### 5.2 员工定薪

#### 5.2.1 获取员工薪资档案

**接口说明**: 获取员工薪资档案信息

**请求URL**: `GET /api/v1/hr/sal/employee-salary/{employeeId}`

**响应示例**:

```json
{
  "code": 200,
  "message": "操作成功",
  "data": {
    "employeeId": 1,
    "employeeName": "张三",
    "gradeId": 1,
    "gradeName": "P3级",
    "baseSalary": 6000,
    "positionSalary": 2000,
    "performanceSalary": 1000,
    "totalSalary": 9000,
    "effectDate": "2024-01-01",
    "items": [
      {
        "itemCode": "BASE",
        "itemName": "基本工资",
        "amount": 6000
      }
    ]
  }
}
```

#### 5.2.2 员工定薪

**接口说明**: 为员工定薪

**请求URL**: `POST /api/v1/hr/sal/employee-salary`

**请求体**:

```json
{
  "employeeId": 1,
  "gradeId": 1,
  "baseSalary": 6000,
  "positionSalary": 2000,
  "performanceSalary": 1000,
  "effectDate": "2024-01-01",
  "items": [
    {
      "itemCode": "ALLOWANCE",
      "itemName": "交通补贴",
      "amount": 500
    }
  ]
}
```

#### 5.2.3 调薪申请

**接口说明**: 发起调薪申请

**请求URL**: `POST /api/v1/hr/sal/salary-adjust/apply`

**请求体**:

```json
{
  "employeeId": 1,
  "adjustReason": "年度调薪",
  "afterBaseSalary": 7000,
  "afterPositionSalary": 2500,
  "effectDate": "2024-07-01"
}
```

### 5.3 薪资核算

#### 5.3.1 执行薪资核算

**接口说明**: 执行月度薪资核算

**请求URL**: `POST /api/v1/hr/sal/payroll/calculate`

**请求体**:

```json
{
  "payrollMonth": "2024-06",
  "deptIds": [1, 2, 3],
  "employeeIds": null
}
```

**响应示例**:

```json
{
  "code": 200,
  "message": "薪资核算完成",
  "data": {
    "payrollMonth": "2024-06",
    "totalEmployee": 500,
    "successCount": 498,
    "failCount": 2,
    "failList": [
      {
        "employeeId": 100,
        "employeeName": "张三",
        "reason": "考勤数据异常"
      }
    ]
  }
}
```

#### 5.3.2 获取薪资核算列表

**接口说明**: 获取薪资核算列表

**请求URL**: `GET /api/v1/hr/sal/payroll`

**请求参数**:

| 参数名 | 类型 | 必填 | 说明 |
|--------|------|------|------|
| payrollMonth | String | 是 | 核算月份 |
| deptId | Long | 否 | 部门ID |
| employeeName | String | 否 | 员工姓名 |
| status | String | 否 | 状态 |

#### 5.3.3 获取工资单详情

**接口说明**: 获取员工工资单详情

**请求URL**: `GET /api/v1/hr/sal/payroll/{id}`

**响应示例**:

```json
{
  "code": 200,
  "message": "操作成功",
  "data": {
    "id": 1,
    "payrollNo": "PAY202406001",
    "payrollMonth": "2024-06",
    "employeeNo": "EMP001",
    "employeeName": "张三",
    "deptName": "生产部",
    "positionName": "装配工",
    "baseSalary": 6000,
    "positionSalary": 2000,
    "performanceSalary": 1000,
    "overtimePay": 300,
    "allowance": 500,
    "grossSalary": 9800,
    "absenceDeduct": 0,
    "socialDeduct": 840,
    "housingFundDeduct": 800,
    "taxDeduct": 87,
    "netSalary": 8073,
    "workDays": 21,
    "actualWorkDays": 21,
    "overtimeHours": 8,
    "items": []
  }
}
```

#### 5.3.4 审核工资单

**接口说明**: 审核工资单

**请求URL**: `POST /api/v1/hr/sal/payroll/{id}/confirm`

### 5.4 薪资发放

#### 5.4.1 获取工资条

**接口说明**: 员工获取工资条

**请求URL**: `GET /api/v1/hr/sal/payslip`

**请求参数**:

| 参数名 | 类型 | 必填 | 说明 |
|--------|------|------|------|
| payrollMonth | String | 是 | 月份 |

**响应示例**:

```json
{
  "code": 200,
  "message": "操作成功",
  "data": {
    "payrollMonth": "2024-06",
    "employeeName": "张三",
    "deptName": "生产部",
    "grossSalary": 9800,
    "totalDeduct": 1727,
    "netSalary": 8073,
    "payTime": "2024-07-10",
    "status": "PAID",
    "items": [
      {
        "itemType": "INCOME",
        "itemName": "基本工资",
        "amount": 6000
      },
      {
        "itemType": "DEDUCT",
        "itemName": "社保扣款",
        "amount": 840
      }
    ]
  }
}
```

#### 5.4.2 工资条签收

**接口说明**: 员工签收工资条

**请求URL**: `POST /api/v1/hr/sal/payslip/{id}/sign`

### 5.5 社保公积金

#### 5.5.1 获取社保方案列表

**接口说明**: 获取社保方案列表

**请求URL**: `GET /api/v1/hr/sal/social-schemes`

#### 5.5.2 获取员工社保信息

**接口说明**: 获取员工社保信息

**请求URL**: `GET /api/v1/hr/sal/employee-social/{employeeId}`

---

## 6. 绩效管理API

### 6.1 绩效方案

#### 6.1.1 获取绩效方案列表

**接口说明**: 获取绩效方案列表

**请求URL**: `GET /api/v1/hr/per/schemes`

#### 6.1.2 创建绩效方案

**接口说明**: 创建绩效方案

**请求URL**: `POST /api/v1/hr/per/schemes`

**请求体**:

```json
{
  "schemeCode": "PER2024",
  "schemeName": "2024年度绩效考核",
  "periodType": "YEARLY",
  "startDate": "2024-01-01",
  "endDate": "2024-12-31",
  "isForceDistribution": 1,
  "sRate": 10,
  "aRate": 20,
  "bRate": 50,
  "cRate": 15,
  "dRate": 5,
  "description": "年度绩效考核方案"
}
```

#### 6.1.3 获取KPI指标库

**接口说明**: 获取KPI指标库列表

**请求URL**: `GET /api/v1/hr/per/kpi-library`

### 6.2 绩效考核

#### 6.2.1 发起考核任务

**接口说明**: 发起绩效考核任务

**请求URL**: `POST /api/v1/hr/per/tasks`

**请求体**:

```json
{
  "taskCode": "TASK202406",
  "taskName": "2024年6月绩效考核",
  "schemeId": 1,
  "period": "2024-06",
  "startDate": "2024-06-25",
  "endDate": "2024-06-30",
  "deadline": "2024-07-05",
  "employeeIds": [1, 2, 3]
}
```

#### 6.2.2 获取待考核列表

**接口说明**: 获取待考核员工列表

**请求URL**: `GET /api/v1/hr/per/tasks/{taskId}/pending`

#### 6.2.3 员工自评

**接口说明**: 员工提交自评

**请求URL**: `POST /api/v1/hr/per/records/{id}/self-evaluate`

**请求体**:

```json
{
  "selfScore": 90,
  "selfComment": "完成了所有工作目标",
  "indicators": [
    {
      "kpiId": 1,
      "kpiName": "产量完成率",
      "targetValue": 100,
      "actualValue": 105,
      "score": 95,
      "comment": "超额完成"
    }
  ]
}
```

#### 6.2.4 上级评价

**接口说明**: 上级提交评价

**请求URL**: `POST /api/v1/hr/per/records/{id}/assess`

**请求体**:

```json
{
  "assessorScore": 88,
  "assessorComment": "工作表现优秀",
  "indicators": [
    {
      "kpiId": 1,
      "score": 90,
      "comment": "达成目标"
    }
  ]
}
```

### 6.3 绩效结果

#### 6.3.1 获取绩效结果

**接口说明**: 获取员工绩效结果

**请求URL**: `GET /api/v1/hr/per/records/{id}`

**响应示例**:

```json
{
  "code": 200,
  "message": "操作成功",
  "data": {
    "id": 1,
    "taskId": 1,
    "taskName": "2024年6月绩效考核",
    "employeeId": 1,
    "employeeName": "张三",
    "deptName": "生产部",
    "selfScore": 90,
    "assessorScore": 88,
    "finalScore": 88.5,
    "grade": "A",
    "status": "CONFIRMED",
    "indicators": []
  }
}
```

#### 6.3.2 确认绩效结果

**接口说明**: 员工确认绩效结果

**请求URL**: `POST /api/v1/hr/per/records/{id}/confirm`

#### 6.3.3 获取绩效报表

**接口说明**: 获取绩效统计报表

**请求URL**: `GET /api/v1/hr/per/reports/summary`

**请求参数**:

| 参数名 | 类型 | 必填 | 说明 |
|--------|------|------|------|
| taskId | Long | 是 | 任务ID |
| deptId | Long | 否 | 部门ID |

---

## 7. 培训管理API

### 7.1 培训课程

#### 7.1.1 获取课程列表

**接口说明**: 获取培训课程列表

**请求URL**: `GET /api/v1/hr/trn/courses`

**请求参数**:

| 参数名 | 类型 | 必填 | 说明 |
|--------|------|------|------|
| courseCategory | String | 否 | 课程分类 |
| courseName | String | 否 | 课程名称 |
| status | Integer | 否 | 状态 |

#### 7.1.2 创建课程

**接口说明**: 创建培训课程

**请求URL**: `POST /api/v1/hr/trn/courses`

**请求体**:

```json
{
  "courseCode": "CRS001",
  "courseName": "安全生产培训",
  "courseCategory": "SAFETY",
  "courseType": "OFFLINE",
  "description": "车间安全生产培训",
  "duration": 4.0,
  "credit": 4.0,
  "objectives": "掌握安全生产知识"
}
```

#### 7.1.3 获取讲师列表

**接口说明**: 获取培训讲师列表

**请求URL**: `GET /api/v1/hr/trn/instructors`

### 7.2 培训班

#### 7.2.1 获取培训班列表

**接口说明**: 获取培训班列表

**请求URL**: `GET /api/v1/hr/trn/classes`

#### 7.2.2 创建培训班

**接口说明**: 创建培训班

**请求URL**: `POST /api/v1/hr/trn/classes`

**请求体**:

```json
{
  "classCode": "CLS202406001",
  "className": "新员工入职培训",
  "courseId": 1,
  "instructorId": 1,
  "startDate": "2024-06-15",
  "endDate": "2024-06-15",
  "startTime": "09:00",
  "endTime": "17:00",
  "location": "培训室A",
  "capacity": 50,
  "employeeIds": [1, 2, 3]
}
```

#### 7.2.3 培训签到

**接口说明**: 培训签到

**请求URL**: `POST /api/v1/hr/trn/classes/{classId}/check-in`

**请求体**:

```json
{
  "employeeId": 1,
  "checkTime": "2024-06-15 08:55:00"
}
```

#### 7.2.4 提交培训评估

**接口说明**: 提交培训评估

**请求URL**: `POST /api/v1/hr/trn/records/{id}/evaluate`

**请求体**:

```json
{
  "evaluationScore": 4.5,
  "evaluationComment": "培训内容丰富，讲师讲解清晰"
}
```

### 7.3 在线学习

#### 7.3.1 获取在线课程列表

**接口说明**: 获取可学习的在线课程

**请求URL**: `GET /api/v1/hr/trn/online-courses`

#### 7.3.2 开始学习

**接口说明**: 开始在线学习

**请求URL**: `POST /api/v1/hr/trn/online-learning/start`

**请求体**:

```json
{
  "courseId": 1
}
```

#### 7.3.3 更新学习进度

**接口说明**: 更新学习进度

**请求URL**: `PUT /api/v1/hr/trn/online-learning/{id}/progress`

**请求体**:

```json
{
  "progress": 50.5,
  "learnDuration": 1800
}
```

#### 7.3.4 完成学习

**接口说明**: 完成课程学习

**请求URL**: `POST /api/v1/hr/trn/online-learning/{id}/complete`

### 7.4 培训记录

#### 7.4.1 获取员工培训记录

**接口说明**: 获取员工培训记录列表

**请求URL**: `GET /api/v1/hr/trn/records/employee/{employeeId}`

**响应示例**:

```json
{
  "code": 200,
  "message": "操作成功",
  "data": {
    "records": [
      {
        "id": 1,
        "className": "新员工入职培训",
        "courseName": "安全生产培训",
        "startDate": "2024-06-15",
        "attendanceHours": 8,
        "examScore": 85,
        "isPass": 1,
        "certificateNo": "CERT001"
      }
    ],
    "totalHours": 40,
    "totalCredit": 40
  }
}
```

---

## 8. 公共接口API

### 8.1 数据字典

#### 8.1.1 获取字典列表

**接口说明**: 获取数据字典

**请求URL**: `GET /api/v1/hr/common/dictionaries/{dictType}`

**响应示例**:

```json
{
  "code": 200,
  "message": "操作成功",
  "data": [
    {
      "value": "M",
      "label": "男"
    },
    {
      "value": "F",
      "label": "女"
    }
  ]
}
```

### 8.2 文件上传

#### 8.2.1 上传文件

**接口说明**: 上传文件(图片、文档等)

**请求URL**: `POST /api/v1/hr/common/upload`

**请求体**: multipart/form-data

**响应示例**:

```json
{
  "code": 200,
  "message": "上传成功",
  "data": {
    "fileId": "FILE001",
    "fileName": "photo.jpg",
    "fileUrl": "http://xxx/photo.jpg",
    "fileSize": 102400
  }
}
```

### 8.3 导入导出

#### 8.3.1 导出员工数据

**接口说明**: 导出员工数据Excel

**请求URL**: `GET /api/v1/hr/emp/employees/export`

**请求参数**:

| 参数名 | 类型 | 必填 | 说明 |
|--------|------|------|------|
| deptId | Long | 否 | 部门ID |
| employeeStatus | String | 否 | 员工状态 |

**响应**: Excel文件流

#### 8.3.2 导入员工数据

**接口说明**: 导入员工数据Excel

**请求URL**: `POST /api/v1/hr/emp/employees/import`

**请求体**: multipart/form-data

---

## 9. 接口安全

### 9.1 接口鉴权

所有接口需要在请求头携带Token:

```
Authorization: Bearer {access_token}
```

### 9.2 敏感接口

以下接口需要额外权限验证：

| 接口 | 权限要求 |
|------|----------|
| 员工薪资查询 | HR薪资权限 |
| 薪资核算 | HR薪资核算权限 |
| 绩效评价 | 绩效考核权限 |

### 9.3 数据权限

- 多租户隔离：所有查询自动添加tenant_id条件
- 部门权限：普通用户只能查看本部门数据
- 个人权限：员工只能查看自己的敏感数据

---

## 10. 接口调用示例

### 10.1 创建员工完整流程

```bash
# 1. 创建员工档案
curl -X POST 'http://localhost:8080/api/v1/hr/emp/employees' \
  -H 'Authorization: Bearer {token}' \
  -H 'Content-Type: application/json' \
  -H 'tenantId: 1' \
  -d '{
    "employeeName": "张三",
    "gender": "M",
    "mobile": "13800138000",
    "deptId": 1,
    "positionId": 1
  }'

# 2. 添加教育经历
curl -X POST 'http://localhost:8080/api/v1/hr/emp/employees/1/educations' \
  -H 'Authorization: Bearer {token}' \
  -H 'Content-Type: application/json' \
  -d '{
    "schoolName": "北京理工大学",
    "major": "机械工程",
    "education": "BACHELOR"
  }'

# 3. 员工定薪
curl -X POST 'http://localhost:8080/api/v1/hr/sal/employee-salary' \
  -H 'Authorization: Bearer {token}' \
  -H 'Content-Type: application/json' \
  -d '{
    "employeeId": 1,
    "baseSalary": 6000,
    "positionSalary": 2000
  }'
```

### 10.2 请假申请流程

```bash
# 1. 查询假期余额
curl -X GET 'http://localhost:8080/api/v1/hr/att/leave-balance?employeeId=1&year=2024' \
  -H 'Authorization: Bearer {token}'

# 2. 提交请假申请
curl -X POST 'http://localhost:8080/api/v1/hr/att/leave/apply' \
  -H 'Authorization: Bearer {token}' \
  -H 'Content-Type: application/json' \
  -d '{
    "leaveTypeId": 1,
    "startDate": "2024-06-10",
    "endDate": "2024-06-11",
    "leaveDays": 2,
    "leaveReason": "家中有事"
  }'

# 3. 审批请假
curl -X POST 'http://localhost:8080/api/v1/hr/att/leave/1/approve' \
  -H 'Authorization: Bearer {token}' \
  -H 'Content-Type: application/json' \
  -d '{
    "approved": true,
    "remark": "同意"
  }'
```

---

**文档审批**

| 角色 | 姓名 | 日期 | 签名 |
|------|------|------|------|
| 架构师 | | | |
| 技术负责人 | | | |
| 前端负责人 | | | |