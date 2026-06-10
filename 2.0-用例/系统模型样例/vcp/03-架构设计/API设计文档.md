# VCP语音社区系统 - API设计文档

## 文档信息

| 属性 | 值 |
|------|-----|
| **文档名称** | API设计文档 |
| **版本** | 1.0 |
| **创建日期** | 2026-06-10 |
| **API风格** | RESTful |

---

## 1. API概述

VCP系统采用RESTful API风格设计，所有API返回JSON格式数据。WebSocket用于实时消息推送和语音信令。

### 1.1 基础信息

| 属性 | 值 |
|------|-----|
| **API Base URL** | `https://api.vcp.example.com/v1` |
| **WebSocket URL** | `wss://ws.vcp.example.com` |
| **认证方式** | JWT Token（Header: Authorization: Bearer {token}） |
| **数据格式** | JSON |
| **编码** | UTF-8 |

### 1.2 响应格式

**成功响应：**
```json
{
  "code": 0,
  "message": "success",
  "data": { ... }
}
```

**错误响应：**
```json
{
  "code": 10001,
  "message": "用户名已存在",
  "data": null
}
```

### 1.3 错误码定义

| 错误码范围 | 说明 |
|------------|------|
| 0 | 成功 |
| 10001-10999 | 用户相关错误 |
| 20001-20999 | 服务器相关错误 |
| 30001-30999 | 频道相关错误 |
| 40001-40999 | 消息相关错误 |
| 50001-50999 | 语音相关错误 |
| 60001-60999 | 权限相关错误 |
| 70001-70999 | 系统错误 |

---

## 2. 用户模块API

### 2.1 认证接口

#### POST /api/auth/register
用户注册

**请求参数：**
```json
{
  "username": "string",      // 用户名（必填）
  "phone": "string",         // 手机号（可选）
  "email": "string",         // 邮箱（可选）
  "password": "string",      // 密码（必填）
  "verify_code": "string"    // 验证码（必填）
}
```

**响应：**
```json
{
  "code": 0,
  "data": {
    "user": {
      "id": 1,
      "username": "testuser",
      "avatar": "https://..."
    },
    "token": "eyJhbGciOiJIUzI1NiIs..."
  }
}
```

#### POST /api/auth/login
用户登录

**请求参数：**
```json
{
  "account": "string",       // 用户名/手机号/邮箱（必填）
  "password": "string"       // 密码（必填）
}
```

**响应：**
```json
{
  "code": 0,
  "data": {
    "user": {
      "id": 1,
      "username": "testuser",
      "nickname": "测试用户",
      "avatar": "https://..."
    },
    "token": "eyJhbGciOiJIUzI1NiIs...",
    "expires_at": "2026-06-17T00:00:00Z"
  }
}
```

#### POST /api/auth/logout
用户登出

**响应：**
```json
{
  "code": 0,
  "message": "登出成功"
}
```

#### POST /api/auth/refresh
刷新Token

**响应：**
```json
{
  "code": 0,
  "data": {
    "token": "eyJhbGciOiJIUzI1NiIs...",
    "expires_at": "2026-06-17T00:00:00Z"
  }
}
```

### 2.2 用户资料接口

#### GET /api/user/profile
获取个人资料

**响应：**
```json
{
  "code": 0,
  "data": {
    "id": 1,
    "username": "testuser",
    "nickname": "测试用户",
    "avatar": "https://...",
    "bio": "个性签名",
    "online_status": 1,
    "created_at": "2026-06-10T00:00:00Z"
  }
}
```

#### PUT /api/user/profile
更新个人资料

**请求参数：**
```json
{
  "nickname": "string",      // 昵称（可选）
  "bio": "string"            // 个性签名（可选）
}
```

#### POST /api/user/avatar
上传头像

**请求参数：**
- Content-Type: multipart/form-data
- file: 图片文件（必填）

**响应：**
```json
{
  "code": 0,
  "data": {
    "avatar_url": "https://..."
  }
}
```

#### PUT /api/user/status
设置在线状态

**请求参数：**
```json
{
  "status": 1                // 1-在线 2-离开 3-DND 4-隐身
}
```

### 2.3 好友接口

#### GET /api/friend/list
获取好友列表

**请求参数：**
- status: 按状态筛选（可选）

**响应：**
```json
{
  "code": 0,
  "data": {
    "friends": [
      {
        "id": 2,
        "username": "friend1",
        "nickname": "好友1",
        "avatar": "https://...",
        "online_status": 1
      }
    ]
  }
}
```

#### GET /api/friend/search
搜索用户

**请求参数：**
- keyword: 搜索关键词（必填）

#### POST /api/friend/request
发送好友请求

**请求参数：**
```json
{
  "user_id": 123             // 目标用户ID（必填）
}
```

#### POST /api/friend/accept
接受好友请求

**请求参数：**
```json
{
  "request_id": 456          // 请求ID（必填）
}
```

#### POST /api/friend/reject
拒绝好友请求

**请求参数：**
```json
{
  "request_id": 456          // 请求ID（必填）
}
```

#### DELETE /api/friend/{userId}
删除好友

---

## 3. 服务器模块API

### 3.1 服务器管理接口

#### POST /api/server/create
创建服务器

**请求参数：**
```json
{
  "name": "string",          // 服务器名称（必填）
  "icon": "string",          // 服务器图标URL（可选）
  "description": "string",   // 服务器描述（可选）
  "region": "string"         // 区域（必填）
}
```

#### GET /api/server/list
获取我的服务器列表

**响应：**
```json
{
  "code": 0,
  "data": {
    "servers": [
      {
        "id": 1,
        "name": "测试服务器",
        "icon": "https://...",
        "member_count": 100,
        "owner_id": 1
      }
    ]
  }
}
```

#### GET /api/server/{id}
获取服务器详情

#### PUT /api/server/{id}
更新服务器设置

#### DELETE /api/server/{id}
删除服务器

### 3.2 成员管理接口

#### GET /api/server/{id}/members
获取成员列表

**请求参数：**
- page: 页码
- limit: 每页数量
- role_id: 按角色筛选（可选）

#### POST /api/server/{id}/members/{userId}/kick
踢出成员

**请求参数：**
```json
{
  "reason": "string",        // 踢出原因（可选）
  "ban_duration": 0          // 封禁时长（0=不封禁，-1=永久）
}
```

#### POST /api/server/{id}/members/{userId}/ban
封禁成员

**请求参数：**
```json
{
  "reason": "string",        // 封禁原因（可选）
  "duration": 7              // 封禁天数（-1=永久）
}
```

#### GET /api/server/{id}/bans
获取封禁列表

#### POST /api/server/{id}/bans/{userId}/revoke
解除封禁

### 3.3 邀请接口

#### POST /api/server/{id}/invite/create
创建邀请链接

**请求参数：**
```json
{
  "max_uses": 100,           // 最大使用次数（可选，null=无限）
  "expires_in": 7            // 有效天数（可选，null=永久）
}
```

**响应：**
```json
{
  "code": 0,
  "data": {
    "code": "abc123",
    "invite_url": "https://vcp.example.com/invite/abc123",
    "expires_at": "2026-06-17T00:00:00Z"
  }
}
```

#### GET /api/server/{id}/invite/list
获取邀请列表

#### DELETE /api/server/{id}/invite/{code}
删除邀请链接

#### POST /api/server/join/{code}
通过邀请加入服务器

### 3.4 角色接口

#### GET /api/server/{id}/roles
获取角色列表

#### POST /api/server/{id}/roles
创建角色

**请求参数：**
```json
{
  "name": "string",          // 角色名称（必填）
  "color": "#FF0000",        // 角色颜色（可选）
  "permissions": 12345       // 权限位（必填）
}
```

#### PUT /api/server/{id}/roles/{roleId}
编辑角色

#### DELETE /api/server/{id}/roles/{roleId}
删除角色

#### PUT /api/server/{id}/members/{userId}/roles
分配角色给成员

**请求参数：**
```json
{
  "role_ids": [1, 2, 3]      // 角色ID列表（必填）
}
```

---

## 4. 频道模块API

### 4.1 分类接口

#### GET /api/server/{id}/categories
获取频道分类列表

#### POST /api/server/{id}/categories
创建分类

#### PUT /api/server/{id}/categories/{catId}
编辑分类

#### DELETE /api/server/{id}/categories/{catId}
删除分类

#### PUT /api/server/{id}/categories/reorder
重新排序分类

**请求参数：**
```json
{
  "order": [1, 2, 3]         // 分类ID列表，按新顺序排列
}
```

### 4.2 频道接口

#### GET /api/server/{id}/channels
获取频道列表

#### POST /api/server/{id}/channels
创建频道

**请求参数：**
```json
{
  "name": "string",          // 频道名称（必填）
  "type": 1,                 // 类型：1-文字 2-语音（必填）
  "category_id": 1,          // 分类ID（可选）
  "topic": "string",         // 频道主题（可选）
  "slow_mode": 0             // 慢速模式间隔（可选）
}
```

#### GET /api/server/{id}/channels/{chId}
获取频道详情

#### PUT /api/server/{id}/channels/{chId}
编辑频道

#### DELETE /api/server/{id}/channels/{chId}
删除频道

#### PUT /api/server/{id}/channels/reorder
重新排序频道

### 4.3 频道权限接口

#### GET /api/channel/{chId}/permissions
获取频道权限

#### PUT /api/channel/{chId}/permissions
设置频道权限

**请求参数：**
```json
{
  "role_id": 1,              // 角色ID（与user_id二选一）
  "user_id": null,           // 用户ID（与role_id二选一）
  "allow": 12345,            // 允许的权限位
  "deny": 0                  // 拒绝的权限位
}
```

---

## 5. 消息模块API

### 5.1 消息接口

#### GET /api/channel/{chId}/messages
获取频道消息列表

**请求参数：**
- before: 获取此ID之前的消息（可选）
- after: 获取此ID之后的消息（可选）
- limit: 数量（默认50）

**响应：**
```json
{
  "code": 0,
  "data": {
    "messages": [
      {
        "id": 1,
        "author": {
          "id": 1,
          "username": "testuser",
          "avatar": "https://..."
        },
        "content": "消息内容",
        "type": 1,
        "attachments": [],
        "reactions": [],
        "created_at": "2026-06-10T10:00:00Z",
        "is_edited": false
      }
    ]
  }
}
```

#### POST /api/channel/{chId}/messages
发送消息

**请求参数：**
```json
{
  "content": "string",       // 消息内容（必填）
  "attachments": [           // 附件列表（可选）
    {
      "file_id": "temp_123"
    }
  ],
  "reply_to": 123            // 引用消息ID（可选）
}
```

#### GET /api/channel/{chId}/messages/search
搜索消息

**请求参数：**
- keyword: 关键词（必填）
- author_id: 发送者ID（可选）
- before: 时间范围（可选）
- after: 时间范围（可选）

#### GET /api/channel/{chId}/messages/{msgId}
获取特定消息

#### PUT /api/channel/{chId}/messages/{msgId}
编辑消息

#### DELETE /api/channel/{chId}/messages/{msgId}
删除消息

### 5.2 消息反应接口

#### POST /api/message/{msgId}/reaction
添加反应

**请求参数：**
```json
{
  "emoji": "👍"              // Emoji（必填）
}
```

#### DELETE /api/message/{msgId}/reaction
移除反应

**请求参数：**
- emoji: Emoji标识

---

## 6. 语音模块API

### 6.1 语音房间接口

#### POST /api/voice/room/{channelId}/join
加入语音房间

**响应：**
```json
{
  "code": 0,
  "data": {
    "room_id": 1,
    "sfu_url": "wss://sfu.vcp.example.com",
    "token": "voice_token_..."
  }
}
```

#### POST /api/voice/room/{channelId}/leave
离开语音房间

#### GET /api/voice/room/{channelId}/members
获取房间成员

#### POST /api/voice/room/{channelId}/mute
自我静音

#### POST /api/voice/room/{channelId}/unmute
取消自我静音

#### POST /api/voice/room/{channelId}/deafen
自我闭麦

#### POST /api/voice/room/{channelId}/undeafen
取消自我闭麦

#### POST /api/voice/room/{channelId}/server-mute/{userId}
管理员静音某人

#### POST /api/voice/room/{channelId}/server-unmute/{userId}
管理员取消静音

#### PUT /api/voice/quality
设置语音质量参数

**请求参数：**
```json
{
  "sample_rate": 48000,      // 采样率
  "noise_suppression": 2     // 降噪等级
}
```

---

## 7. 通知模块API

### 7.1 通知接口

#### GET /api/notification/list
获取通知列表

**请求参数：**
- page: 页码
- limit: 每页数量
- unread_only: 仅未读（可选）

#### POST /api/notification/{id}/read
标记单条已读

#### POST /api/notification/read-all
全部标记已读

#### GET /api/notification/unread-count
获取未读数

**响应：**
```json
{
  "code": 0,
  "data": {
    "count": 5
  }
}
```

### 7.2 通知偏好接口

#### GET /api/notification/settings
获取通知偏好

#### PUT /api/notification/settings
更新通知偏好

**请求参数：**
```json
{
  "notification_level": 1,   // 1-所有 2-仅@ 3-静音
  "desktop_push": true,
  "sound": true
}
```

#### PUT /api/server/{id}/notification-setting
设置服务器通知级别

#### PUT /api/channel/{chId}/notification-setting
设置频道通知级别

---

## 8. 管理审核模块API

### 8.1 举报接口

#### POST /api/report
提交举报

**请求参数：**
```json
{
  "server_id": 1,
  "target_type": 2,          // 1-用户 2-消息
  "target_id": 123,
  "reason_type": "SPAM",     // SPAM/HARASSMENT/INAPPROPRIATE/OTHER
  "description": "string"
}
```

#### GET /api/server/{id}/reports
获取举报列表

#### POST /api/report/{id}/handle
处理举报

**请求参数：**
```json
{
  "action": "delete",        // delete/warn/ban/ignore
  "result": "处理说明"
}
```

### 8.2 审核日志接口

#### GET /api/server/{id}/moderation-logs
获取操作日志

### 8.3 内容过滤接口

#### GET /api/server/{id}/word-filter
获取敏感词列表

#### PUT /api/server/{id}/word-filter
更新敏感词列表

---

## 9. 系统设置模块API

### 9.1 音频设置接口

#### GET /api/settings/audio
获取音频设置

#### PUT /api/settings/audio
更新音频设置

#### GET /api/settings/audio/devices
获取音频设备列表

#### POST /api/settings/audio/test
测试音频设备

### 9.2 快捷键设置接口

#### GET /api/settings/shortcuts
获取快捷键设置

#### PUT /api/settings/shortcuts
更新快捷键设置

### 9.3 主题设置接口

#### GET /api/settings/theme
获取主题设置

#### PUT /api/settings/theme
更新主题设置

### 9.4 隐私设置接口

#### GET /api/settings/privacy
获取隐私设置

#### PUT /api/settings/privacy
更新隐私设置

### 9.5 设置导入导出接口

#### GET /api/settings/export
导出设置（JSON）

#### POST /api/settings/import
导入设置

---

## 10. WebSocket事件

### 10.1 连接认证

```
连接URL: wss://ws.vcp.example.com?token={jwt_token}
```

### 10.2 消息事件

| 事件 | 方向 | 说明 |
|------|------|------|
| message:create | Server → Client | 新消息 |
| message:update | Server → Client | 消息编辑 |
| message:delete | Server → Client | 消息删除 |
| message:reaction:add | Server → Client | 添加反应 |
| message:reaction:remove | Server → Client | 移除反应 |

### 10.3 输入指示事件

| 事件 | 方向 | 说明 |
|------|------|------|
| typing:start | Client → Server | 开始输入 |
| typing:stop | Client → Server | 停止输入 |
| typing:indicator | Server → Client | 输入中指示 |

### 10.4 语音事件

| 事件 | 方向 | 说明 |
|------|------|------|
| voice:join | Client → Server | 用户加入房间 |
| voice:leave | Client → Server | 用户离开房间 |
| voice:offer | Client ↔ Server | WebRTC SDP Offer |
| voice:answer | Client ↔ Server | WebRTC SDP Answer |
| voice:ice-candidate | Client ↔ Server | ICE候选交换 |
| voice:mute | Client → Server | 静音状态变更 |
| voice:speaking | Server → Client | 发言状态通知 |

### 10.5 状态事件

| 事件 | 方向 | 说明 |
|------|------|------|
| user:status | Server → Client | 用户状态变更 |
| server:member:join | Server → Client | 成员加入服务器 |
| server:member:leave | Server → Client | 成员离开服务器 |
| voice:member:join | Server → Client | 用户加入语音 |
| voice:member:leave | Server → Client | 用户离开语音 |

---

## 附录

### A. API文档工具

- Swagger UI: `https://api.vcp.example.com/swagger`
- OpenAPI Spec: `代码/backend/api/openapi.yaml`

### B. 参考文档

- [系统架构设计](./系统架构设计.md)
- [数据库设计](./数据库设计文档.md)
- [需求总览](../01-需求分析/00-VCP系统需求总览.md)