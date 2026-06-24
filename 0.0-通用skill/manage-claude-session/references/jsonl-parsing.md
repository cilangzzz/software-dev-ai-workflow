# JSONL 解析规范

## 概述

JSONL (JSON Lines) 是一种文本格式，每行包含一个有效的 JSON 对象。Claude Code 使用此格式存储会话数据。

## 解析方法

### 基本解析流程

```javascript
// 伪代码示例
function parseJSONL(content) {
  const lines = content.split('\n');
  const results = [];

  for (const line of lines) {
    if (line.trim() === '') continue;

    try {
      const obj = JSON.parse(line);
      results.push(obj);
    } catch (e) {
      console.error('解析错误:', e);
    }
  }

  return results;
}
```

### 流式解析（推荐用于大文件）

```javascript
const fs = require('fs');
const readline = require('readline');

async function parseJSONLStream(filePath) {
  const fileStream = fs.createReadStream(filePath);
  const rl = readline.createInterface({
    input: fileStream,
    crlfDelay: Infinity
  });

  const results = [];

  for await (const line of rl) {
    if (line.trim() === '') continue;

    try {
      const obj = JSON.parse(line);
      results.push(obj);
    } catch (e) {
      console.error('行解析错误:', e);
    }
  }

  return results;
}
```

## 消息树构建

会话中的消息通过 `uuid` 和 `parentUuid` 构建树状结构：

```javascript
function buildMessageTree(messages) {
  const nodeMap = new Map();

  // 创建节点映射
  for (const msg of messages) {
    if (msg.uuid) {
      nodeMap.set(msg.uuid, { ...msg, children: [] });
    }
  }

  // 构建父子关系
  let root = null;
  for (const msg of messages) {
    const node = nodeMap.get(msg.uuid);
    if (msg.parentUuid && nodeMap.has(msg.parentUuid)) {
      nodeMap.get(msg.parentUuid).children.push(node);
    } else {
      root = node;
    }
  }

  return root;
}
```

## 会话内容提取

### 提取用户消息

```javascript
function extractUserMessages(messages) {
  return messages
    .filter(m => m.type === 'user')
    .map(m => ({
      timestamp: m.timestamp,
      content: m.message?.content?.[0]?.text || m.display,
      uuid: m.uuid
    }));
}
```

### 提取工具调用

```javascript
function extractToolCalls(messages) {
  return messages
    .filter(m => m.type === 'tool_use')
    .map(m => ({
      timestamp: m.timestamp,
      toolName: m.message?.content?.[0]?.name,
      toolInput: m.message?.content?.[0]?.input,
      uuid: m.uuid
    }));
}
```

### 提取完整对话

```javascript
function extractConversation(messages) {
  const conversation = [];
  const sorted = messages.sort((a, b) =>
    new Date(a.timestamp) - new Date(b.timestamp)
  );

  for (const msg of sorted) {
    if (msg.type === 'user') {
      conversation.push({
        role: 'user',
        content: msg.message?.content?.[0]?.text,
        timestamp: msg.timestamp
      });
    } else if (msg.type === 'assistant') {
      conversation.push({
        role: 'assistant',
        content: msg.message?.content?.[0]?.text,
        timestamp: msg.timestamp
      });
    }
  }

  return conversation;
}
```

## 搜索实现

### 全文搜索

```javascript
function searchInSession(messages, keyword) {
  const results = [];

  for (let i = 0; i < messages.length; i++) {
    const line = JSON.stringify(messages[i]);
    if (line.includes(keyword)) {
      results.push({
        lineIndex: i,
        message: messages[i],
        context: getContext(line, keyword, 50)
      });
    }
  }

  return results;
}

function getContext(text, keyword, contextLength) {
  const index = text.indexOf(keyword);
  const start = Math.max(0, index - contextLength);
  const end = Math.min(text.length, index + keyword.length + contextLength);

  return {
    before: text.slice(start, index),
    match: keyword,
    after: text.slice(index + keyword.length, end)
  };
}
```

## 常见问题处理

### 1. 空行处理

```javascript
// 跳过空行
if (line.trim() === '') continue;
```

### 2. 编码问题

```javascript
// 确保使用 UTF-8 编码
const content = fs.readFileSync(filePath, 'utf-8');
```

### 3. 特殊字符转义

```javascript
// JSON 已处理转义，直接解析即可
const obj = JSON.parse(line);
```

### 4. 时间戳处理

```javascript
// history.jsonl 使用的毫秒时间戳
function convertTimestamp(ts) {
  if (typeof ts === 'number') {
    return new Date(ts);
  }
  return new Date(ts);
}
```

## 性能优化

### 分批处理

```javascript
async function processInBatches(messages, batchSize, processor) {
  const results = [];

  for (let i = 0; i < messages.length; i += batchSize) {
    const batch = messages.slice(i, i + batchSize);
    const batchResults = await processor(batch);
    results.push(...batchResults);
  }

  return results;
}
```

### 内存优化

```javascript
// 使用生成器避免一次性加载
function* messageGenerator(messages) {
  for (const msg of messages) {
    yield msg;
  }
}
```

---
**版本**: 1.0.0
**最后更新**: 2026-06-24
