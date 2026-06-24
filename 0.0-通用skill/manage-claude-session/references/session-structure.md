# 会话数据结构说明

## 概述

Claude Code 使用 JSONL (JSON Lines) 格式存储会话数据，每行一个独立的 JSON 对象。

## 文件位置

| 文件类型 | 路径 | 说明 |
|----------|------|------|
| 历史记录 | `~/.claude/history.jsonl` | 所有会话的简要记录 |
| 项目会话 | `~/.claude/projects/{hash}/*.jsonl` | 项目级别的详细会话 |
| 会话状态 | `~/.claude/sessions/*.json` | 当前活跃会话状态 |

## 数据格式

### 1. history.jsonl 格式

每行记录一次用户输入：

```json
{
  "display": "用户输入的文本内容",
  "pastedContents": {
    "1": {
      "id": 1,
      "type": "text",
      "contentHash": "abc123..."
    }
  },
  "timestamp": 1774194778215,
  "project": "C:\\Users\\admin\\Desktop",
  "sessionId": "c0074208-b947-442b-bb41-4144e647218e"
}
```

**字段说明**：

| 字段 | 类型 | 说明 |
|------|------|------|
| display | string | 用户输入的显示文本 |
| pastedContents | object | 粘贴的内容（如果有） |
| timestamp | number | 毫秒级时间戳 |
| project | string | 项目路径 |
| sessionId | string | 会话唯一标识符 |

### 2. 详细会话 .jsonl 格式

#### 用户消息

```json
{
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "da71b03d-cd0a-48f3-b9af-2f3162f0e58b",
  "type": "user",
  "message": {
    "role": "user",
    "content": [
      {
        "type": "text",
        "text": "用户消息内容"
      }
    ]
  },
  "uuid": "f93a0155-52f3-4fe0-9ff1-860ec6496ab8",
  "timestamp": "2026-06-15T15:23:53.399Z",
  "permissionMode": "auto",
  "promptSource": "sdk",
  "userType": "external",
  "entrypoint": "claude-vscode",
  "cwd": "f:\\sandbox\\workflow",
  "sessionId": "0f0d10f6-dc95-4c10-81d6-f1ba2d7bb264",
  "version": "2.1.168",
  "gitBranch": "main"
}
```

#### AI 回复

```json
{
  "parentUuid": "f93a0155-52f3-4fe0-9ff1-860ec6496ab8",
  "type": "assistant",
  "message": {
    "role": "assistant",
    "content": [
      {
        "type": "text",
        "text": "AI回复内容..."
      }
    ]
  },
  "uuid": "abc123...",
  "timestamp": "2026-06-15T15:23:55.123Z",
  "sessionId": "0f0d10f6-dc95-4c10-81d6-f1ba2d7bb264"
}
```

#### 工具调用

```json
{
  "parentUuid": "previous-uuid",
  "type": "tool_use",
  "message": {
    "role": "assistant",
    "content": [
      {
        "type": "tool_use",
        "id": "toolu_abc123",
        "name": "Read",
        "input": {
          "file_path": "f:\\sandbox\\workflow\\README.md"
        }
      }
    ]
  },
  "uuid": "tool-uuid...",
  "sessionId": "0f0d10f6-dc95-4c10-81d6-f1ba2d7bb264"
}
```

#### 工具结果

```json
{
  "parentUuid": "tool-uuid",
  "type": "tool_result",
  "toolResultId": "toolu_abc123",
  "content": "文件内容...",
  "uuid": "result-uuid...",
  "sessionId": "0f0d10f6-dc95-4c10-81d6-f1ba2d7bb264"
}
```

### 3. 会话状态 .json 格式

```json
{
  "sessionId": "c0074208-b947-442b-bb41-4144e647218e",
  "projectId": "f--sandbox-workflow",
  "createdAt": "2026-06-15T15:23:53.368Z",
  "lastActiveAt": "2026-06-15T16:30:00.000Z",
  "messageCount": 42
}
```

## 消息类型汇总

| type 值 | 说明 |
|---------|------|
| user | 用户消息 |
| assistant | AI 回复 |
| tool_use | 工具调用请求 |
| tool_result | 工具执行结果 |
| attachment | 附加信息（如技能列表） |
| queue-operation | 队列操作 |
| file-history-snapshot | 文件历史快照 |

## 解析注意事项

1. **逐行解析**: JSONL 文件必须逐行读取，每行是独立 JSON
2. **大文件处理**: 使用流式读取，避免一次性加载整个文件
3. **时间格式**:
   - history.jsonl 使用毫秒时间戳
   - 详细会话使用 ISO 8601 格式
4. **路径转义**: Windows 路径使用双反斜杠 `\\`
5. **UUID 关联**: 使用 uuid 和 parentUuid 构建消息树

## 时间戳转换

```javascript
// 毫秒时间戳转日期
const date = new Date(1774194778215);
// 输出: 2026-03-23T00:12:58.215Z

// ISO 字符串转日期
const date2 = new Date("2026-06-15T15:23:53.399Z");
```

---
**版本**: 1.0.0
**最后更新**: 2026-06-24
