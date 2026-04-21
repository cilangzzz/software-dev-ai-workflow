# Swagger UI HTML 文档生成规则

## 概述

生成自包含的 Swagger UI HTML 文件，将 OpenAPI 规范嵌入 HTML 中，可直接在浏览器中打开查看交互式 API 文档。

## 文件结构

```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
  <meta charset="UTF-8">
  <title>{项目名称} 接口文档</title>
  <style>
    /* SwaggerUI CSS bundle - 内联 */
  </style>
</head>
<body>
  <div id="swagger-ui"></div>
  <script>
    /* SwaggerUI JS bundle - 内联 */

    window.onload = function() {
      window.ui = SwaggerUIBundle({
        spec: { /* OpenAPI 3.x 规范对象，直接嵌入 */ },
        dom_id: '#swagger-ui',
        deepLinking: true,
        presets: [
          SwaggerUIBundle.presets.apis,
          SwaggerUIStandalonePreset
        ],
        layout: "StandaloneLayout",
        docExpansion: "list",
        filter: true,
        showExtensions: true,
        showCommonExtensions: true,
        tagsSorter: "alpha",
        operationsSorter: "alpha"
      });
    };
  </script>
</body>
</html>
```

## 生成步骤

1. **获取 OpenAPI 规范**：使用前面步骤生成的 OpenAPI JSON 对象
2. **获取 SwaggerUI 资源**：
   - 方案A（推荐）：使用 CDN 链接引入 SwaggerUI CSS/JS
   - 方案B：将 SwaggerUI 的 CSS/JS 内联到 HTML 中（实现完全离线）
3. **嵌入 spec**：将 OpenAPI JSON 对象直接作为 `spec` 参数传入
4. **配置选项**：设置布局、排序、展开等显示选项

## 方案A：CDN引入（文件更小）

```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
  <meta charset="UTF-8">
  <title>{项目名称} 接口文档</title>
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/swagger-ui-dist@5/swagger-ui.css">
</head>
<body>
  <div id="swagger-ui"></div>
  <script src="https://cdn.jsdelivr.net/npm/swagger-ui-dist@5/swagger-ui-bundle.js"></script>
  <script src="https://cdn.jsdelivr.net/npm/swagger-ui-dist@5/swagger-ui-standalone-preset.js"></script>
  <script>
    window.onload = function() {
      const spec = __OPENAPI_SPEC_PLACEHOLDER__;
      window.ui = SwaggerUIBundle({
        spec: spec,
        dom_id: '#swagger-ui',
        deepLinking: true,
        presets: [
          SwaggerUIBundle.presets.apis,
          SwaggerUIStandalonePreset
        ],
        layout: "StandaloneLayout"
      });
    };
  </script>
</body>
</html>
```

将 `__OPENAPI_SPEC_PLACEHOLDER__` 替换为实际的 OpenAPI JSON 字符串。

## 方案B：完全内联（离线可用）

需要获取 SwaggerUI 的 CSS 和 JS 文件内容，直接内联到 `<style>` 和 `<script>` 标签中。
文件较大（约 1.7MB），但无需网络连接即可使用。

## 配置选项说明

| 选项 | 值 | 说明 |
|------|------|------|
| layout | "StandaloneLayout" | 独立布局，不含顶部导航栏 |
| docExpansion | "list" / "full" / "none" | 接口展开方式 |
| filter | true | 启用搜索过滤 |
| showExtensions | true | 显示 OpenAPI 扩展字段 |
| showCommonExtensions | true | 显示通用扩展字段 |
| tagsSorter | "alpha" | 标签按字母排序 |
| operationsSorter | "alpha" | 接口按字母排序 |

## 注意事项

- HTML 标题固定为 `{项目名称} 接口文档`
- 内嵌的 OpenAPI spec 版本通常使用 3.0.1 以获得更好的 SwaggerUI 兼容性
- 生成的 HTML 文件应可在 Chrome/Firefox/Edge 等主流浏览器中直接打开
