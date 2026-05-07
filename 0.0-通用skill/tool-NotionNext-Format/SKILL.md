---
name: notion-next-format
description: NotionNext博客格式专家 - 用于创建、编辑、修改和验证NotionNext博客系统内容。支持文章(Post)的创建、查询、更新、删除；页面(Page)、菜单(Menu)、公告(Notice)等多种内容类型的格式规范。Agent bypass模式下自动执行无需确认。触发场景：(1) 创建NotionNext博客文章 (2) 查询/搜索已有文章 (3) 修改/更新文章属性或内容 (4) 配置导航菜单 (5) 设置网站配置 (6) 格式化已有内容 (7) 批量导入文章
---

# NotionNext 博客格式专家

你是一个专业的NotionNext博客格式专家，擅长创建、编辑和验证符合NotionNext规范的Notion数据库内容。

## Step 0：任务识别

| 用户表述 / 关键词 | 执行 |
| --- | --- |
| 创建博客文章、写文章、发布文章 | 创建Post流程 |
| 查询文章、搜索文章、查找文章 | 查询/搜索流程 |
| 修改文章、更新文章、编辑文章 | 修改Post流程 |
| 追加内容、添加内容、补充内容 | append-body流程 |
| 创建菜单、添加导航、配置菜单 | 创建Menu流程 |
| 创建页面、添加单页、关于页面 | 创建Page流程 |
| 发布公告、添加公告 | 创建Notice流程 |
| 网站配置、CONFIG设置 | 配置Config流程 |
| 格式化文章、修正格式、验证格式 | 格式验证流程 |
| 批量导入、导入文章 | 批量创建流程 |
| 自动处理、直接执行、不要问我 | Bypass模式执行 |

## Step 1：NotionNext数据库结构

### 核心数据库属性

| 属性名 | 类型 | 必填 | 说明 |
|--------|------|------|------|
| `title` | Title | 是 | 文章标题，显示在列表和详情页 |
| `status` | Select | 是 | 发布状态：Published/Invisible/Draft |
| `type` | Select | 是 | 内容类型：Post/Page/Menu/SubMenu/Notice/Config |
| `slug` | Rich Text | 推荐 | URL路径标识，如 `my-first-post` |
| `date` | Date | 推荐 | 发布日期，用于排序和归档 |
| `category` | Select | 可选 | 分类：知行合一/技术分享/心情随笔 |
| `tags` | Multi Select | 可选 | 标签列表，用于筛选 |
| `summary` | Rich Text | 推荐 | 文章摘要，用于列表预览和SEO |
| `icon` | Rich Text | 可选 | FontAwesome图标，如 `fas fa-home` |
| `password` | Rich Text | 可选 | 文章密码，加密访问 |

### 类型详解

#### 1. Post (博客文章)

核心内容类型，显示在博客列表中。

```yaml
type: Post
必须属性:
  - title: 文章标题
  - status: Published (发布) / Draft (草稿) / Invisible (隐藏)
  - slug: URL路径 (如: my-article)
推荐属性:
  - category: 分类选择
  - tags: 标签数组
  - summary: 摘要描述
  - date: 发布日期
可选属性:
  - password: 加密访问密码
```

**分类选项**:
- `知行合一` - 学习心得、实践感悟
- `技术分享` - 技术教程、开发经验
- `心情随笔` - 生活记录、随笔感想

**标签选项**:
- `推荐` - 精选推荐内容
- `文字` - 纯文字内容
- `思考` - 深度思考类
- `新闻` - 新闻资讯
- `工具` - 工具介绍
- `开发` - 开发相关
- `建站` - 网站建设
- `金钱` - 财务相关
- `健康` - 健康主题

#### 2. Page (单页面)

独立页面，不显示在博客列表，可通过URL直接访问。

```yaml
type: Page
必须属性:
  - title: 页面标题
  - status: Published / Invisible
  - slug: URL路径 (如: about, links)
特点:
  - 不出现在文章列表
  - 导航菜单可链接
  - 适合: 关于、友链、自定义页面
```

#### 3. Menu (导航菜单)

顶部导航栏菜单项。

```yaml
type: Menu
必须属性:
  - title: 菜单显示名称
  - status: Published
  - slug: 跳转路径
推荐属性:
  - icon: FontAwesome图标
特点:
  - slug可以是内部路径或外部链接
  - slug=#时作为子菜单容器
  - 子菜单紧跟在父菜单下方
```

**slug跳转类型**:
- `/` - 首页
- `/search` - 搜索页
- `/category` - 分类页
- `/tag` - 标签页
- `/archive` - 归档页
- `links` - 单页面
- `https://...` - 外部链接
- `#` - 子菜单容器(不跳转)

**图标格式**:
- FontAwesome格式: `fas fa-home`, `fab fa-github`, `fas fa-search`

#### 4. SubMenu (子菜单)

二级菜单，挂载在上一条Menu下方。

```yaml
type: SubMenu
必须属性:
  - title: 子菜单名称
  - status: Published
  - slug: 跳转路径
特点:
  - 必须紧跟在父Menu下方
  - 父Menu的slug需为#
  - 显示在父菜单的下拉列表
```

#### 5. Notice (公告)

全站公告，显示在页面顶部。

```yaml
type: Notice
必须属性:
  - title: 公告标题
  - status: Published
  - slug: # (通常固定)
特点:
  - 显示为网站顶部公告栏
  - 支持Markdown内容
  - 可多条公告叠加显示
```

#### 6. Config (配置)

网站配置项，优先级最高。

```yaml
type: Config
必须属性:
  - title: 配置名称
  - status: Published
特点:
  - 可直接在Notion配置网站参数
  - 优先级高于环境变量和blog.config.js
  - 支持JSON格式配置值
```

## Step 2：内容创建流程

### 2.1 创建博客文章

```yaml
workflow:
  phases:
    - name: "信息收集"
      steps:
        - step: "确认文章标题"
          action: "获取title"
        - step: "确认分类和标签"
          action: "选择category和tags"
        - step: "确认摘要"
          action: "编写summary"
        - step: "确认slug"
          action: "生成URL路径"
    
    - name: "格式构建"
      steps:
        - step: "构建属性JSON"
          action: "按Notion API格式构建properties"
        - step: "验证必填字段"
          action: "检查title/status/type"
    
    - name: "内容提交"
      steps:
        - step: "调用Notion API"
          action: "使用Notion skill添加entry"
        - step: "添加正文内容"
          action: "append-body添加文章内容"
```

### 属性JSON模板

```json
{
  "title": { "title": [{ "text": { "content": "文章标题" } }] },
  "status": { "select": { "name": "Published" } },
  "type": { "select": { "name": "Post" } },
  "slug": { "rich_text": [{ "text": { "content": "article-slug" } }] },
  "category": { "select": { "name": "技术分享" } },
  "tags": { "multi_select": [{ "name": "工具" }, { "name": "推荐" }] },
  "summary": { "rich_text": [{ "text": { "content": "文章摘要内容..." } }] },
  "date": { "date": { "start": "2026-04-23" } },
  "icon": { "rich_text": [{ "text": { "content": "" } }] },
  "password": { "rich_text": [{ "text": { "content": "" } }] }
}
```

### 2.2 创建导航菜单

```yaml
workflow:
  phases:
    - name: "菜单设计"
      steps:
        - step: "确认菜单层级"
          action: "是否需要子菜单"
        - step: "确认跳转目标"
          action: "内部路径或外部链接"
    
    - name: "菜单创建"
      steps:
        - step: "创建父菜单"
          action: "type=Menu, slug=#"
        - step: "创建子菜单"
          action: "type=SubMenu, 紧跟父菜单"
```

### 菜单属性JSON模板

```json
// 父菜单 (容器)
{
  "title": { "title": [{ "text": { "content": "建站教程" } }] },
  "status": { "select": { "name": "Published" } },
  "type": { "select": { "name": "Menu" } },
  "slug": { "rich_text": [{ "text": { "content": "#" } }] },
  "icon": { "rich_text": [{ "text": { "content": "fas fa-folder" } }] },
  "summary": { "rich_text": [{ "text": { "content": "菜单slug留空或填#即可，用于下面的子菜单" } }] }
}

// 子菜单
{
  "title": { "title": [{ "text": { "content": "NotionNext介绍" } }] },
  "status": { "select": { "name": "Published" } },
  "type": { "select": { "name": "SubMenu" } },
  "slug": { "rich_text": [{ "text": { "content": "https://tangly1024.com" } }] },
  "summary": { "rich_text": [{ "text": { "content": "SubMenu是子菜单，挂在上一个Menu中" } }] }
}
```

### 2.3 创建加密文章

```json
{
  "title": { "title": [{ "text": { "content": "加密文章标题" } }] },
  "status": { "select": { "name": "Published" } },
  "type": { "select": { "name": "Post" } },
  "slug": { "rich_text": [{ "text": { "content": "locked-article" } }] },
  "password": { "rich_text": [{ "text": { "content": "123456" } }] },
  "summary": { "rich_text": [{ "text": { "content": "本文需要输入密码才可访问，密码: 123456" } }] }
}
```

## Step 3：正文内容格式

### 正文Block类型

| Block类型 | Notion类型 | 用途 |
|-----------|------------|------|
| paragraph | paragraph | 普通段落 |
| h1/h2/h3 | heading_1/2/3 | 标题 |
| bullet | bulleted_list_item | 无序列表 |
| numbered | numbered_list_item | 有序列表 |
| todo | to_do | 待办事项 |
| quote | quote | 引用块 |
| code | code | 代码块 |
| divider | divider | 分割线 |
| callout | callout | 提示框 |
| image | image | 图片 |

### 正文添加命令

```bash
# 添加标题
node notion-cli.js append-body PAGE_ID --text "章节标题" --type h2

# 添加段落
node notion-cli.js append-body PAGE_ID --text "正文内容..."

# 添加列表
node notion-cli.js append-body PAGE_ID --text "列表项内容" --type bullet

# 添加代码块
node notion-cli.js append-body PAGE_ID --text "const x = 1;" --type code --lang javascript

# 添加引用
node notion-cli.js append-body PAGE_ID --text "引用内容" --type quote
```

## Step 4：URL路径规范

### slug命名规范

```yaml
slug_rules:
  format:
    - "使用英文小写"
    - "使用连字符分隔单词"
    - "避免特殊字符"
    - "建议长度: 3-50字符"
  
  examples:
    good:
      - "my-first-post"
      - "vue3-tutorial"
      - "how-to-build-blog"
    bad:
      - "我的第一篇文章"  # 中文不推荐
      - "MyFirstPost"    # 大写不推荐
      - "my_first_post" # 下划线不推荐
```

### URL路径映射

通过CONFIG-TABLE配置分类路径映射：

```json
{
  "知行合一": "learning",
  "技术分享": "technology",
  "心情随笔": "essay"
}
```

效果：
- 使用前: `xx.com/知行合一/slug`
- 使用后: `xx.com/learning/slug`

## Step 5：CONFIG-TABLE配置表

### 常用配置项

| 配置名 | 配置值 | 说明 |
|--------|--------|------|
| THEME | heo | 网站主题 |
| LANG | en-US | 默认语言 |
| AUTHOR | cilangzzz | 网站作者 |
| SINCE | 2023 | 网站发布年份 |
| CUSTOM_MENU | true | 启用二级菜单 |
| POST_URL_PREFIX | %category% | URL路径前缀 |
| GLOBAL_JS | console.log('test'); | 自定义JS代码 |
| GLOBAL_CSS | ... | 自定义CSS样式 |

## Step 6：质量检查清单

### 文章发布检查

```yaml
checklist:
  before_publish:
    - item: "标题已填写"
      check: "title不为空"
    - item: "status已设置"
      check: "status为Published/Draft/Invisible"
    - item: "type已设置"
      check: "type为正确类型"
    - item: "slug已设置"
      check: "slug为英文小写连字符格式"
    - item: "summary已填写"
      check: "summary有内容且不超过200字"
    - item: "分类和标签已设置"
      check: "category和tags有选择"
  
  after_publish:
    - item: "URL可访问"
      check: "访问/slug路径验证"
    - item: "内容显示正确"
      check: "正文Block正确渲染"
    - item: "列表显示正常"
      check: "文章出现在对应分类列表"
```

### 菜单配置检查

```yaml
checklist:
  menu_setup:
    - item: "菜单顺序正确"
      check: "SubMenu紧跟父Menu"
    - item: "slug路径有效"
      check: "内部路径或有效URL"
    - item: "图标格式正确"
      check: "FontAwesome格式如fas fa-home"
```

## Step 7：使用示例

### 示例1：创建技术文章

**输入**:
```
创建一篇关于Vue3组合式API的文章
标题: Vue3组合式API入门指南
分类: 技术分享
标签: 开发, 推荐
摘要: 本文介绍Vue3组合式API的基本概念和使用方法...
```

**输出属性JSON**:
```json
{
  "title": { "title": [{ "text": { "content": "Vue3组合式API入门指南" } }] },
  "status": { "select": { "name": "Published" } },
  "type": { "select": { "name": "Post" } },
  "slug": { "rich_text": [{ "text": { "content": "vue3-composition-api-guide" } }] },
  "category": { "select": { "name": "技术分享" } },
  "tags": { "multi_select": [{ "name": "开发" }, { "name": "推荐" }] },
  "summary": { "rich_text": [{ "text": { "content": "本文介绍Vue3组合式API的基本概念和使用方法..." } }] },
  "date": { "date": { "start": "2026-04-23" } }
}
```

### 示例2：创建导航菜单结构

**输入**:
```
创建一个"资源"菜单，包含两个子菜单：
- GitHub仓库
- 官方文档
```

**输出**:
```json
// 父菜单
{
  "title": { "title": [{ "text": { "content": "资源" } }] },
  "status": { "select": { "name": "Published" } },
  "type": { "select": { "name": "Menu" } },
  "slug": { "rich_text": [{ "text": { "content": "#" } }] },
  "icon": { "rich_text": [{ "text": { "content": "fas fa-link" } }] }
}

// 子菜单1
{
  "title": { "title": [{ "text": { "content": "GitHub仓库" } }] },
  "status": { "select": { "name": "Published" } },
  "type": { "select": { "name": "SubMenu" } },
  "slug": { "rich_text": [{ "text": { "content": "https://github.com/user/repo" } }] }
}

// 子菜单2
{
  "title": { "title": [{ "text": { "content": "官方文档" } }] },
  "status": { "select": { "name": "Published" } },
  "type": { "select": { "name": "SubMenu" } },
  "slug": { "rich_text": [{ "text": { "content": "https://docs.example.com" } }] }
}
```

### 示例3：添加文章正文

**输入**:
```
为刚创建的文章添加以下内容：
- 介绍标题
- 什么是组合式API
- 代码示例
```

**执行命令**:
```bash
# 添加二级标题
node notion-cli.js append-body PAGE_ID --text "什么是组合式API" --type h2

# 添加段落介绍
node notion-cli.js append-body PAGE_ID --text "组合式API是Vue3引入的新特性..."

# 添加代码示例
node notion-cli.js append-body PAGE_ID --text "import { ref, computed } from 'vue'" --type code --lang javascript

# 添加列表要点
node notion-cli.js append-body PAGE_ID --text "更好的逻辑组织" --type bullet
node notion-cli.js append-body PAGE_ID --text "更好的TypeScript支持" --type bullet
```

## 工具集成

### 与Notion Skill协作

```yaml
collaboration:
  upstream:
    - skill: notion
      relationship: upstream
      condition: "需要调用Notion API"
      usage: "使用notion-cli.js执行数据库操作"
  
  commands:
    - command: "add-entry"
      usage: "创建新文章/页面/菜单"
    - command: "update-page"
      usage: "更新文章属性"
    - command: "append-body"
      usage: "添加正文内容"
    - command: "query-database"
      usage: "查询现有内容"
```

### 执行示例

```bash
# 设置环境变量
NOTION_TOKEN="ntn_xxx..."

# 创建文章
node notion-cli.js add-entry DATABASE_ID \
  --title "文章标题" \
  --properties '{...属性JSON...}'

# 添加正文
node notion-cli.js append-body PAGE_ID \
  --text "内容" --type paragraph
```

## Step 8：文章修改与编辑能力

### 8.1 更新文章属性

使用 `update-page` 命令修改已有文章的属性：

```bash
# 更新文章状态为草稿
node notion-cli.js update-page PAGE_ID --properties '{"status":{"select":{"name":"Draft"}}}'

# 更新分类和标签
node notion-cli.js update-page PAGE_ID --properties '{"category":{"select":{"name":"技术分享"}},"tags":{"multi_select":[{"name":"开发"},{"name":"推荐"}]}}'

# 更新摘要
node notion-cli.js update-page PAGE_ID --properties '{"summary":{"rich_text":[{"text":{"content":"新的摘要内容"}}]}}'
```

### 8.2 查询已有文章

使用 `query-database` 命令检索数据库中的文章：

```bash
# 查询所有文章
node notion-cli.js query-database DATABASE_ID

# 查询特定状态的文章
node notion-cli.js query-database DATABASE_ID --filter '{"property":"status","select":{"equals":"Published"}}'

# 查询特定分类的文章
node notion-cli.js query-database DATABASE_ID --filter '{"property":"category","select":{"equals":"技术分享"}}'

# 查询包含特定标签的文章
node notion-cli.js query-database DATABASE_ID --filter '{"property":"tags","multi_select":{"contains":"推荐"}}'
```

### 8.3 获取文章详情

使用 `get-page` 命令获取文章完整内容和属性：

```bash
# 通过页面ID获取
node notion-cli.js get-page PAGE_ID

# 通过Notion ID获取（需要数据库ID）
node notion-cli.js get-page '#3' DATABASE_ID
```

### 8.4 添加正文内容

使用 `append-body` 命令向已有文章追加内容：

```bash
# 添加段落
node notion-cli.js append-body PAGE_ID --text "新的段落内容"

# 添加标题
node notion-cli.js append-body PAGE_ID --text "新章节" --type h2

# 添加列表
node notion-cli.js append-body PAGE_ID --text "列表项" --type bullet

# 添加代码块
node notion-cli.js append-body PAGE_ID --text "console.log('hello')" --type code --lang javascript

# 批量添加多个Block
node notion-cli.js append-body PAGE_ID --blocks '[{"type":"heading_2","heading_2":{"rich_text":[{"text":{"content":"标题"}}]}},{"type":"paragraph","paragraph":{"rich_text":[{"text":{"content":"段落"}}]}}]'
```

### 8.5 搜索文章

使用 `search` 命令在Notion工作区搜索：

```bash
# 搜索标题包含关键词的文章
node notion-cli.js search "关键词"

# 搜索特定数据库
node notion-cli.js search "技术"
```

## Step 9：Agent工作模式与Bypass

### 9.1 Agent Bypass模式说明

在Agent bypass模式下，Agent可以直接执行操作而无需用户确认：

**触发条件**：
- 用户明确表示"自动处理"、"直接执行"、"不要问我"
- 已有明确的操作指令和历史记录
- bypass权限已配置

**Bypass模式下的行为**：
- 直接调用Notion API推送内容
- 自动检索已有文章进行更新
- 批量操作不需要逐条确认

### 9.2 常见Agent操作模式

| 用户表述 | 执行模式 | 操作 |
|---------|---------|------|
| "创建文章"、"写文章" | 正常/创建 | 创建Post流程 |
| "修改文章"、"更新文章" | 正常/修改 | 查询→更新流程 |
| "自动处理"、"直接执行" | Bypass | 无确认直接执行 |
| "批量推送" | Bypass | 批量创建流程 |

### 9.3 检索已有文章流程

在修改文章前，Agent会自动：

```yaml
workflow:
  phases:
    - name: "文章检索"
      steps:
        - step: "搜索目标文章"
          action: "使用search或query-database检索"
        - step: "获取文章详情"
          action: "使用get-page获取当前内容"
        - step: "对比修改内容"
          action: "确认需要更新的字段"
    
    - name: "执行修改"
      steps:
        - step: "更新属性"
          action: "使用update-page修改属性"
        - step: "追加内容"
          action: "使用append-body添加正文"
```

## Step 10：Token配置与400错误排查

### 10.1 Token格式说明

Notion Integration Token格式：

```
ntn_xxxxxxxxxxxxxxxxxxxxxxxx (新格式，OpenAPI token)
secret_xxxxxxxxxxxxxxxxxxxxx (旧格式，Internal Integration token)
```

**获取方式**：
1. 访问 notion.so/my-integrations
2. 创建新Integration或复制已有Integration的token
3. 确保Integration已与目标数据库/页面共享

### 10.2 400错误原因分析

| 错误代码 | 原因 | 解决方案 |
|---------|------|---------|
| `400 Bad Request` | Token格式错误 | 检查token是否完整复制 |
| `400 Bad Request` | JSON格式错误 | 检查properties JSON语法 |
| `400 Bad Request` | 属性名错误 | 使用数据库实际属性名(title而非Name) |
| `unauthorized` | Token无效/未共享 | 确保Integration已共享到数据库 |
| `validation_error` | 属性类型不匹配 | 检查select/rich_text等类型 |
| `object_not_found` | ID不存在/未共享 | 确认ID正确且已共享 |

### 10.3 Token配置位置

Token可配置在以下位置（按优先级排序）：

```yaml
env_locations:
  1. 环境变量:
     - HTTPS_PROXY=http://127.0.0.1:7897
     - NOTION_TOKEN=ntn_xxx
  
  2. 当前目录.env:
     - ./0.0-通用skill/Notion/.env
  
  3. NotionNext-Format目录.env:
     - ./0.0-通用skill/NotionNext-Format/.env
  
  4. 用户目录.env:
     - ~/.claude/.env
     - ~/.openclaw/.env
```

### 10.4 .env文件格式

```bash
# .env文件示例
NOTION_TOKEN=ntn_306888051713xxxxxxxxxxxxxxxxxxx
HTTPS_PROXY=http://127.0.0.1:7897
HTTP_PROXY=http://127.0.0.1:7897
```

**注意**：
- Token不要加引号
- 代理地址根据实际代理软件配置
- Windows常用代理端口：7897(Clash)、1080(SSR)

### 10.5 连接测试

```bash
# 测试Token是否有效
cd 0.0-通用skill/Notion
HTTPS_PROXY=http://127.0.0.1:7897 node notion-cli.js test

# 预期输出
Connected to Notion!
Found X accessible pages/databases:
```

### 10.6 属性名对照表

| 数据库显示名 | API属性名 | 类型 |
|-------------|----------|------|
| 标题 | `title` | title |
| Name | `title` | title |
| 状态 | `status` | select |
| 类型 | `type` | select |
| 分类 | `category` | select |
| 标签 | `tags` | multi_select |
| 摘要 | `summary` | rich_text |
| slug | `slug` | rich_text |

**常见错误**：使用 `Name` 而非 `title` 导致400错误

## Step 11：完整操作示例

### 11.1 创建完整文章

```bash
# 1. 创建文章
node notion-cli.js add-entry DATABASE_ID --properties '{"title":{"title":[{"text":{"content":"文章标题"}}]},"status":{"select":{"name":"Published"}},"type":{"select":{"name":"Post"}},"slug":{"rich_text":[{"text":{"content":"article-slug"}}]},"category":{"select":{"name":"技术分享"}},"tags":{"multi_select":[{"name":"开发"}]},"summary":{"rich_text":[{"text":{"content":"摘要内容"}}]},"date":{"date":{"start":"2026-04-29"}}}'

# 2. 返回的PAGE_ID用于添加正文
# 假设返回: {"id":"xxx-xxx-xxx"}

# 3. 添加正文内容
node notion-cli.js append-body "xxx-xxx-xxx" --blocks '[{"type":"heading_2","heading_2":{"rich_text":[{"text":{"content":"章节标题"}}]}},{"type":"paragraph","paragraph":{"rich_text":[{"text":{"content":"正文内容"}}]}}]'
```

### 11.2 修改已有文章

```bash
# 1. 搜索文章
node notion-cli.js search "文章标题"

# 2. 获取详情确认PAGE_ID
node notion-cli.js get-page PAGE_ID

# 3. 更新属性
node notion-cli.js update-page PAGE_ID --properties '{"status":{"select":{"name":"Draft"}}}'

# 4. 追加内容
node notion-cli.js append-body PAGE_ID --text "新增内容" --type paragraph
```

## 注意事项

- **slug唯一性**: 同一数据库内slug不应重复
- **菜单顺序**: SubMenu必须紧跟父Menu，顺序决定显示
- **密码文章**: password字段设置后访问需输入密码
- **草稿状态**: Draft状态的文章不会显示在列表
- **外链菜单**: slug为完整URL时跳转外部网站
- **图标格式**: 使用FontAwesome格式，如 `fas fa-home`
- **中文slug**: 不推荐使用中文slug，URL编码可能出问题
- **摘要长度**: 建议控制在100-200字符
- **正文Block**: 支持多种类型，按需选择

## 网络连接问题与代理配置

### 常见错误

调用 Notion API 时可能遇到以下网络错误：

| 错误信息 | 原因 | 解决方案 |
|---------|------|---------|
| `ECONNRESET` | TCP连接被中断 | 使用代理或等待重试 |
| `ETIMEDOUT` | 连接超时 | 检查网络或使用代理 |
| `SSL/TLS handshake failed` | SSL握手失败 | 配置正确的代理 |
| `schannel: failed to receive handshake` | Windows代理SSL问题 | 使用global-agent |

### 错误原因分析

1. **网络不稳定**: 国内直连Notion API可能不稳定
2. **代理问题**: 
   - 代理软件过载或重启
   - SSL/TLS握手失败
   - 代理与Notion的HTTPS连接被拦截
3. **Notion API限制**:
   - 频率限制: 3 requests/second
   - 短时间大量请求可能被阻断
   - Cloudflare安全规则触发
4. **Node.js限制**:
   - node-fetch默认无重试机制
   - 连接中断直接抛异常

### 方案一：使用 global-agent 代理

**安装依赖**:
```bash
cd NotionNext-Format
npm install global-agent @notionhq/client
```

**代理脚本示例**:
```javascript
// 设置全局代理
process.env.GLOBAL_AGENT_HTTP_PROXY = 'http://127.0.0.1:7897';
const { createGlobalProxyAgent } = require('global-agent');
createGlobalProxyAgent();

const { Client } = require('@notionhq/client');
const notion = new Client({ auth: 'ntn_xxx...' });

// 现在可以正常调用API
async function test() {
  const result = await notion.search({ query: '', page_size: 10 });
  console.log(result.results.length);
}
test();
```

**一键执行**:
```bash
cd NotionNext-Format
node -e "
process.env.GLOBAL_AGENT_HTTP_PROXY='http://127.0.0.1:7897';
require('global-agent').createGlobalProxyAgent();
const {Client}=require('@notionhq/client');
const n=new Client({auth:'ntn_xxx'});
n.search({query:'',page_size:5}).then(r=>console.log('连接成功:',r.results.length,'条')).catch(e=>console.log('错误:',e.message));
"
```

### 方案二：curl 测试代理连接

**测试代理是否能连通Notion**:
```bash
curl -x http://127.0.0.1:7897 -I https://api.notion.com/v1/search \
  -H "Authorization: Bearer ntn_xxx" \
  -H "Notion-Version: 2022-06-28"
```

**通过代理查询数据库**:
```bash
TOKEN="ntn_xxx"; DB="数据库ID";
curl -x http://127.0.0.1:7897 -X POST "https://api.notion.com/v1/databases/$DB/query" \
  -H "Authorization: Bearer $TOKEN" \
  -H "Notion-Version: 2022-06-28" \
  -H "Content-Type: application/json" \
  --data '{"page_size":10}'
```

### 方案三：请求频率控制

**批量添加内容时添加间隔**:
```javascript
async function addBlocksBatch(blocks) {
  const batchSize = 10;  // Notion API限制每次最多添加块数
  
  for (let i = 0; i < blocks.length; i += batchSize) {
    const batch = blocks.slice(i, i + batchSize);
    
    try {
      await notion.blocks.children.append({
        block_id: PAGE_ID,
        children: batch
      });
      console.log(`✅ 第 ${i+1}-${i+batch.length} 个块添加成功`);
    } catch (e) {
      console.log(`❌ 错误: ${e.message}`);
    }
    
    // 等待避免频率限制
    await new Promise(r => setTimeout(r, 300));
  }
}
```

### 方案四：环境变量配置代理

**Windows CMD**:
```cmd
set HTTPS_PROXY=http://127.0.0.1:7897
set NOTION_TOKEN=ntn_xxx
node notion-cli.js test
```

**Windows PowerShell**:
```powershell
$env:HTTPS_PROXY="http://127.0.0.1:7897"
$env:NOTION_TOKEN="ntn_xxx"
node notion-cli.js test
```

**Linux/Mac**:
```bash
export HTTPS_PROXY=http://127.0.0.1:7897
export NOTION_TOKEN=ntn_xxx
node notion-cli.js test
```

### 排错流程

1. **测试代理连通性**: `curl -x http://127.0.0.1:7897 https://api.notion.com`
2. **测试Notion API**: 使用curl带Authorization头测试
3. **检查代理软件**: 确认代理软件正常运行
4. **等待重试**: 遇到ECONNRESET等待1-2分钟再试
5. **使用global-agent**: 最稳定的代理方案

## 相关文档

- [NotionNext官方文档](https://docs.tangly1024.com)
- [属性类型参考](references/property-types.md) - Notion API属性格式
- [Block类型参考](references/block-types.md) - 正文Block格式
- [配置项说明](references/config-options.md) - CONFIG-TABLE完整配置

---
**技能版本**: 1.0.0
**最后更新**: 2026-04-23
**创建者**: AI Assistant