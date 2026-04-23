# CONFIG-TABLE 配置项说明

本文档详细说明NotionNext CONFIG-TABLE数据库的配置项。

## 配置表结构

| 属性名 | 类型 | 说明 |
|--------|------|------|
| 配置名 | title | 配置项名称（唯一标识） |
| 配置值 | rich_text | 配置值内容 |
| 启用 | checkbox | 是否启用此配置 |
| 备注 | rich_text | 配置说明 |
| 创建日期 | created_time | 自动记录 |

## 配置优先级

```
Notion CONFIG-TABLE > 环境变量 > blog.config.js
```

Notion配置表的优先级最高，可覆盖其他配置源。

## 核心配置项

### 网站基础配置

| 配置名 | 配置值示例 | 启用 | 说明 |
|--------|-----------|------|------|
| THEME | heo | ✅ | 网站主题，可选: hexo/matery/heo等 |
| LANG | en-US | ✅ | 网站默认语言，zh-CN/en-US等 |
| TITLE | tangly1024 | ❌ | 网站标题（读取数据库标题，无需配置） |
| DESCRIPTION | tangly1024 | ❌ | 网站描述（读取数据库描述，无需配置） |
| AUTHOR | cilangzzz | ❌ | 网站作者名称 |
| SINCE | 2023 | ❌ | 网站创建年份 |
| KEYWORDS | notion,blog,博客 | ❌ | SEO关键词，逗号分隔 |
| BLOG_FAVICON | https://xxx.ico | ❌ | 网站favicon图标URL |

### URL配置

| 配置名 | 配置值示例 | 启用 | 说明 |
|--------|-----------|------|------|
| LINK | https://your-site.com | ✅ | 网站URL，必填 |
| POST_URL_PREFIX | %category% | ❌ | 文章URL前缀模式 |
| POST_URL_PREFIX_MAPPING_CATEGORY | JSON映射 | ✅ | 分类路径映射 |

### 分类路径映射示例

```json
{
  "知行合一": "learning",
  "技术分享": "technology",
  "心情随笔": "essay"
}
```

效果：
- 原URL: `/知行合一/article-slug`
- 映射后: `/learning/article-slug`

### 菜单配置

| 配置名 | 配置值示例 | 启用 | 说明 |
|--------|-----------|------|------|
| CUSTOM_MENU | true | ✅ | 启用二级菜单 |
| CUSTOM_RIGHT_CLICK_CONTEXT_MENU | false | ✅ | 自定义右键菜单 |

### 显示配置

| 配置名 | 配置值示例 | 启用 | 说明 |
|--------|-----------|------|------|
| HOME_BANNER_IMAGE | https://xxx.jpg | ❌ | 首页封面大图 |
| PREVIEW_TAG_COUNT | 5 | ❌ | 馄览显示标签数 |
| PREVIEW_CATEGORY_COUNT | 2 | ❌ | 馄览显示分类数 |
| THEME_SWITCH | true | ❌ | 显示主题切换按钮 |
| CAN_COPY | true | ❌ | 允许复制文字 |

### 功能配置

| 配置名 | 配置值示例 | 启用 | 说明 |
|--------|-----------|------|------|
| POST_SHARE_BAR_ENABLE | true | ❌ | 文章分享功能 |
| WIDGET_PET | false | ❌ | 宠物挂件显示 |

### 联系方式配置

| 配置名 | 配置值示例 | 启用 | 说明 |
|--------|-----------|------|------|
| CONTACT_EMAIL | xxx@xxx.com | ❌ | 联系邮箱 |
| CONTACT_WHATSAPP | https://wa.me/xxx | ❌ | WhatsApp链接 |
| CONTACT_TELEGRAM | https://t.me/xxx | ❌ | Telegram链接 |

### 自定义样式配置

| 配置名 | 配置值示例 | 启用 | 说明 |
|--------|-----------|------|------|
| GLOBAL_CSS | CSS样式代码 | ❌ | 全站自定义CSS |
| GLOBAL_JS | JS代码 | ✅ | 全站自定义JS |
| FONT_URL | CSS字体链接数组 | ❌ | 字体加载URL |
| FONT_STYLE | font-serif font-light | ❌ | 字体样式 |

### GLOBAL_CSS示例

```css
#wrapper {
  background-image: url(https://xxx.jpg);
  background-position: center;
  background-repeat: no-repeat;
  background-size: 100% 100%;
}

[id^="theme-"] {
  font-family: LXGW WenKai;
}
```

### GLOBAL_JS示例

```javascript
console.log('网站加载完成');
// 自定义统计代码
// 自定义交互逻辑
```

### FONT_URL示例

```json
[
  "https://npm.elemecdn.com/lxgw-wenkai-webfont@1.6.0/style.css",
  "https://fonts.googleapis.com/css?family=Bitter&display=swap",
  "https://fonts.googleapis.com/css2?family=Noto+Sans+SC:wght@300&display=swap"
]
```

### 高级配置

| 配置名 | 配置值示例 | 启用 | 说明 |
|--------|-----------|------|------|
| INLINE_CONFIG | JSON对象 | ❌ | 批量导入JSON配置 |
| SIMPLE_LOGO_DESCRIPTION | 自定义文字 | ✅ | Logo描述文字 |
| GREETING_WORDS | 欢迎语列表 | ❌ | 打字效果欢迎语 |

### INLINE_CONFIG示例

```json
{
  "TEST": "测试值",
  "CUSTOM_KEY": "自定义配置"
}
```

### GREETING_WORDS示例

```
Hi，我是一个程序员, Hi，我是一个打工人, Hi，我是一个干饭人, 欢迎来到我的博客🎉
```

## 配置项添加方法

### 通过Notion CLI添加配置

```bash
node notion-cli.js add-entry CONFIG_DB_ID \
  --title "配置名称" \
  --properties '{...JSON格式属性...}'
```

### 示例：添加主题配置

```bash
node notion-cli.js add-entry CONFIG_DB_ID \
  --title "THEME" \
  --properties '{
    "配置值": { "rich_text": [{ "text": { "content": "heo" } }] },
    "启用": { "checkbox": true },
    "备注": { "rich_text": [{ "text": { "content": "网站主题选择" } }] }
  }'
```

## 注意事项

1. **优先级**: Notion配置优先级最高，谨慎覆盖
2. **JSON格式**: 配置值中JSON需使用英文双引号
3. **启用状态**: checkbox=true才会生效
4. **性能**: 建议基础配置在blog.config.js中设置
5. **动态更新**: Notion配置实时生效，无需重新部署

---
**文档版本**: 1.0.0
**最后更新**: 2026-04-23