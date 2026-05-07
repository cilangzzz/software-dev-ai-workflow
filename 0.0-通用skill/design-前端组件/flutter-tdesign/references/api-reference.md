# TDesign Flutter API 速查表

核心组件 API 快速参考，详细属性请查看对应分类文档。

---

## 常用组件核心属性

### TDButton
| 属性 | 说明 |
|------|------|
| text | 文本内容 |
| type | fill/outline/text/ghost |
| theme | primary/danger/default |
| size | large/medium/small |
| disabled | 禁止点击 |
| onTap | 点击事件 |

### TDInput
| 属性 | 说明 |
|------|------|
| leftLabel | 左侧文案 |
| hintText | 提示文案 |
| controller | 文本控制器 |
| onChanged | 输入回调 |
| maxLength | 最大字数 |
| additionInfo | 错误提示 |

### TDDialog
| 属性 | 说明 |
|------|------|
| title | 标题 |
| content | 内容 |
| leftBtn/rightBtn | 按钮配置 |

### TDToast 方法
| 方法 | 说明 |
|------|------|
| showText | 文本提示 |
| showSuccess | 成功提示 |
| showFail | 失败提示 |
| showLoading | 加载提示 |
| dismissLoading | 关闭加载 |

### TDNavBar
| 属性 | 说明 |
|------|------|
| title | 标题文案 |
| centerTitle | 居中显示 |
| useDefaultBack | 默认返回 |
| leftBarItems/rightBarItems | 操作项 |

---

## 主题 API

### TDTheme
| 方法 | 说明 |
|------|------|
| defaultData() | 默认主题 |
| of(context) | 当前主题 |

### 常用颜色属性
| 属性 | 说明 |
|------|------|
| brandNormalColor | 品牌主色 |
| textColorPrimary | 主要文字 |
| bgColorContainer | 容器背景 |
| successNormalColor | 成功色 |
| errorNormalColor | 错误色 |

---

> 详细 API 请查看各分类组件文档。