# Notion API 属性类型参考

本文档详细说明NotionNext博客使用的Notion API属性格式。

## 标题属性 (title)

```json
{
  "title": {
    "title": [
      {
        "type": "text",
        "text": {
          "content": "文章标题内容"
        }
      }
    ]
  }
}
```

## 选择属性 (select)

用于单选字段，如status、type、category。

```json
{
  "status": {
    "select": {
      "name": "Published"
    }
  }
}
```

### status可选值
- `Published` - 已发布，显示在列表
- `Draft` - 草稿，不显示
- `Invisible` - 隐藏，可通过URL访问

### type可选值
- `Post` - 博客文章
- `Page` - 单页面
- `Menu` - 导航菜单
- `SubMenu` - 子菜单
- `Notice` - 公告
- `Config` - 配置项

### category可选值
- `知行合一`
- `技术分享`
- `心情随笔`

## 多选属性 (multi_select)

用于标签字段。

```json
{
  "tags": {
    "multi_select": [
      { "name": "推荐" },
      { "name": "工具" },
      { "name": "开发" }
    ]
  }
}
```

### tags可选值
- `推荐` - 精选推荐
- `文字` - 纯文字内容
- `思考` - 深度思考
- `新闻` - 新闻资讯
- `工具` - 工具介绍
- `开发` - 开发相关
- `建站` - 网站建设
- `金钱` - 财务相关
- `健康` - 健康主题

## 富文本属性 (rich_text)

用于slug、summary、icon、password等字段。

```json
{
  "slug": {
    "rich_text": [
      {
        "type": "text",
        "text": {
          "content": "article-slug-name"
        }
      }
    ]
  }
}
```

## 日期属性 (date)

用于发布日期。

```json
{
  "date": {
    "date": {
      "start": "2026-04-23"
    }
  }
}
```

带时间的日期格式：
```json
{
  "date": {
    "date": {
      "start": "2026-04-23T10:00:00",
      "end": "2026-04-23T12:00:00"
    }
  }
}
```

## 带时区的日期格式

```json
{
  "date": {
    "date": {
      "start": "2026-04-23T10:00:00+08:00",
      "time_zone": null
    }
  }
}
```

## 复选框属性 (checkbox)

用于启用/禁用状态。

```json
{
  "启用": {
    "checkbox": true
  }
}
```

## 数字属性 (number)

用于数值字段。

```json
{
  "Quote Value": {
    "number": 100.00
  }
}
```

## 邮箱属性 (email)

```json
{
  "Email": {
    "email": "user@example.com"
  }
}
```

## URL属性 (url)

```json
{
  "URL": {
    "url": "https://example.com"
  }
}
```

## 电话属性 (phone_number)

```json
{
  "Phone": {
    "phone_number": "+86-138-0000-0000"
  }
}
```

## 关系属性 (relation)

用于关联其他数据库条目。

```json
{
  "Related Posts": {
    "relation": [
      { "id": "page-id-32chars" }
    ]
  }
}
```

## 完整文章属性示例

```json
{
  "title": {
    "title": [
      { "type": "text", "text": { "content": "Vue3组合式API入门指南" } }
    ]
  },
  "status": {
    "select": { "name": "Published" }
  },
  "type": {
    "select": { "name": "Post" }
  },
  "slug": {
    "rich_text": [
      { "type": "text", "text": { "content": "vue3-composition-api-guide" } }
    ]
  },
  "category": {
    "select": { "name": "技术分享" }
  },
  "tags": {
    "multi_select": [
      { "name": "开发" },
      { "name": "推荐" }
    ]
  },
  "summary": {
    "rich_text": [
      { "type": "text", "text": { "content": "本文介绍Vue3组合式API的基本概念和使用方法..." } }
    ]
  },
  "date": {
    "date": { "start": "2026-04-23" }
  },
  "icon": {
    "rich_text": [
      { "type": "text", "text": { "content": "" } }
    ]
  },
  "password": {
    "rich_text": [
      { "type": "text", "text": { "content": "" } }
    ]
  }
}
```

---
**文档版本**: 1.0.0
**最后更新**: 2026-04-23