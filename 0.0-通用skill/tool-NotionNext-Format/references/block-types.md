# Notion Block 类型参考

本文档详细说明Notion正文Block的格式和使用方法。

## Block类型列表

| Block类型 | Notion API类型 | CLI参数 | 用途 |
|-----------|----------------|---------|------|
| 段落 | paragraph | paragraph | 普通文本段落 |
| 一级标题 | heading_1 | h1 | 大标题 |
| 二级标题 | heading_2 | h2 | 章节标题 |
| 三级标题 | heading_3 | h3 | 小标题 |
| 无序列表 | bulleted_list_item | bullet | 列表要点 |
| 有序列表 | numbered_list_item | numbered | 步骤列表 |
| 待办事项 | to_do | todo | 任务清单 |
| 引用块 | quote | quote | 引用内容 |
| 代码块 | code | code | 代码片段 |
| 分割线 | divider | divider | 章节分隔 |
| 提示框 | callout | callout | 重要提示 |
| 图片 | image | image | 图片展示 |

## CLI命令格式

### 基本格式

```bash
node notion-cli.js append-body PAGE_ID --text "内容" --type BLOCK_TYPE
```

### 段落 (paragraph)

```bash
node notion-cli.js append-body PAGE_ID --text "这是一段普通文字内容。" --type paragraph

# 或默认不指定type
node notion-cli.js append-body PAGE_ID --text "这是一段普通文字内容。"
```

### 标题

```bash
# 一级标题
node notion-cli.js append-body PAGE_ID --text "文章标题" --type h1

# 二级标题（章节）
node notion-cli.js append-body PAGE_ID --text "第一章 简介" --type h2

# 三级标题（小节）
node notion-cli.js append-body PAGE_ID --text "1.1 什么是Vue" --type h3
```

### 列表

```bash
# 无序列表
node notion-cli.js append-body PAGE_ID --text "更好的性能" --type bullet
node notion-cli.js append-body PAGE_ID --text "更小的体积" --type bullet
node notion-cli.js append-body PAGE_ID --text "更好的TypeScript支持" --type bullet

# 有序列表（步骤）
node notion-cli.js append-body PAGE_ID --text "安装依赖" --type numbered
node notion-cli.js append-body PAGE_ID --text "配置环境" --type numbered
node notion-cli.js append-body PAGE_ID --text "运行项目" --type numbered
```

### 待办事项

```bash
# 未完成的待办
node notion-cli.js append-body PAGE_ID --text "完成文档编写" --type todo

# 待办默认为未勾选状态
```

### 引用块

```bash
node notion-cli.js append-body PAGE_ID --text "这是一段重要的引用内容，需要特别关注。" --type quote
```

### 代码块

```bash
# JavaScript代码
node notion-cli.js append-body PAGE_ID --text "const app = createApp(App);" --type code --lang javascript

# Python代码
node notion-cli.js append-body PAGE_ID --text "print('Hello World')" --type code --lang python

# Shell命令
node notion-cli.js append-body PAGE_ID --text "npm install vue" --type code --lang shell

# JSON格式
node notion-cli.js append-body PAGE_ID --text '{"name": "vue"}' --type code --lang json
```

**支持的语言**:
- javascript / js
- python / py
- java
- go
- rust
- typescript / ts
- shell / bash
- sql
- html
- css
- json
- yaml
- markdown
- plain text (默认)

### 分割线

```bash
node notion-cli.js append-body PAGE_ID --type divider
```

### 提示框 (callout)

```bash
node notion-cli.js append-body PAGE_ID --text "这是一个重要提示！" --type callout
```

## Raw JSON Block格式

对于复杂布局，可直接使用Notion API的JSON格式：

```bash
node notion-cli.js append-body PAGE_ID --blocks '[
  {
    "object": "block",
    "type": "heading_2",
    "heading_2": {
      "rich_text": [
        { "type": "text", "text": { "content": "章节标题" } }
      ]
    }
  },
  {
    "object": "block",
    "type": "paragraph",
    "paragraph": {
      "rich_text": [
        { "type": "text", "text": { "content": "段落内容..." } }
      ]
    }
  },
  {
    "object": "block",
    "type": "bulleted_list_item",
    "bulleted_list_item": {
      "rich_text": [
        { "type": "text", "text": { "content": "列表项" } }
      ]
    }
  }
]'
```

## 文章内容组织建议

### 推荐的文章结构

```
h1: 文章标题（可选，通常使用数据库title）
---
h2: 引言/概述
paragraph: 简要介绍文章主题
---
h2: 正文章节1
h3: 小节标题
paragraph: 内容描述
bullet: 要点列表
---
h2: 正文章节2
code: 代码示例
---
h2: 总结
paragraph: 总结内容
quote: 引用/名言
divider: 分隔线
```

### 创建文章示例

```bash
# 添加引言
node notion-cli.js append-body PAGE_ID --text "引言" --type h2
node notion-cli.js append-body PAGE_ID --text "本文将介绍Vue3组合式API的核心概念..."

# 添加正文
node notion-cli.js append-body PAGE_ID --text "什么是组合式API" --type h2
node notion-cli.js append-body PAGE_ID --text "组合式API是Vue3引入的新特性..." --type paragraph
node notion-cli.js append-body PAGE_ID --text "更好的代码组织" --type bullet
node notion-cli.js append-body PAGE_ID --text "更灵活的逻辑复用" --type bullet

# 添加代码示例
node notion-cli.js append-body PAGE_ID --text "基本使用" --type h2
node notion-cli.js append-body PAGE_ID --text "import { ref } from 'vue'" --type code --lang javascript

# 添加总结
node notion-cli.js append-body PAGE_ID --text "总结" --type h2
node notion-cli.js append-body PAGE_ID --text "组合式API为Vue开发带来了新的可能性..." --type paragraph
```

---
**文档版本**: 1.0.0
**最后更新**: 2026-04-23