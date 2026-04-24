# 基础组件

本分类包含 6 个基础组件。

---

## TDButton 按钮

**功能**：常规按钮组件，支持多种样式、尺寸、主题和形状配置。

**核心属性**：
| 属性 | 类型 | 默认值 | 说明 |
|------|------|--------|------|
| text | String | - | 文本内容 |
| size | TDButtonSize | medium | 尺寸 (large/medium/small/extraSmall) |
| type | TDButtonType | fill | 类型 (fill/outline/text/ghost) |
| shape | TDButtonShape | rectangle | 形状 (rectangle/round/square/circle/filled) |
| theme | TDButtonTheme | default | 主题 (default/primary/danger/light) |
| disabled | bool | false | 禁止点击 |
| isBlock | bool | false | 是否为通栏按钮 |
| icon | IconData | - | 图标 |
| onTap | Function | - | 点击事件 |

**示例**：
```dart
// 基础用法
const TDButton(
  text: '填充按钮',
  size: TDButtonSize.large,
  type: TDButtonType.fill,
  theme: TDButtonTheme.primary,
)

// 带图标
TDButton(
  text: '带图标',
  icon: TDIcons.add,
  type: TDButtonType.fill,
)

// 描边按钮
const TDButton(
  text: '描边按钮',
  type: TDButtonType.outline,
  theme: TDButtonTheme.primary,
)

// 加载状态
TDButton(
  text: '加载中',
  iconWidget: TDLoading(size: TDLoadingSize.small),
)
```

---

## TDIcons 图标

**功能**：TDesign 图标库，提供 2113 个预定义图标常量。

**使用方法**：
```dart
// 基础用法
Icon(TDIcons.activity)
Icon(TDIcons.check_circle_filled)

// 自定义属性
Icon(
  TDIcons.search,
  size: 24,
  color: TDTheme.of(context).brandNormalColor,
)
```

**常用图标**：
| 名称 | 用途 |
|------|------|
| add, close, check | 操作 |
| search, edit, delete | 功能 |
| arrow_left, arrow_right | 导航 |
| check_circle_filled | 成功 |
| error_circle_filled | 错误 |

> 完整图标列表见 [icons-reference.md](../icons-reference.md)

---

## TDLink 链接

**功能**：链接文本组件，支持多种样式和跳转功能。

**核心属性**：
| 属性 | 类型 | 默认值 | 说明 |
|------|------|--------|------|
| label | String | 必填 | 展示的文本 |
| uri | Uri | - | 跳转的uri |
| type | TDLinkType | basic | 类型 |
| style | TDLinkStyle | defaultStyle | 风格 |
| state | TDLinkState | normal | 状态 |
| size | TDLinkSize | medium | 大小 |
| linkClick | Function | - | 点击回调 |

**示例**：
```dart
TDLink(
  label: '链接文字',
  uri: Uri.parse('https://example.com'),
  style: TDLinkStyle.primary,
)
```

---

## TDDivider 分割线

**功能**：分割线组件，支持水平和垂直方向，支持虚线和中间文本。

**核心属性**：
| 属性 | 类型 | 默认值 | 说明 |
|------|------|--------|------|
| direction | Axis | horizontal | 方向 |
| color | Color | - | 线条颜色 |
| height | double | 0.5 | 线条高度 |
| isDashed | bool | false | 是否为虚线 |
| text | String | - | 中间文本 |
| alignment | TextAlignment | center | 文字位置 |

**示例**：
```dart
// 水平分割线
const TDDivider()

// 带文字分割线
TDDivider(text: '分割线')

// 虚线分割线
const TDDivider(isDashed: true)

// 垂直分割线
const TDDivider(direction: Axis.vertical, width: 1)
```

---

## TDCell 单元格

**功能**：单元格组件，用于列表项展示，支持标题、描述、图标、箭头等。

**核心属性**：
| 属性 | 类型 | 默认值 | 说明 |
|------|------|--------|------|
| title | String | - | 标题 |
| description | String | - | 下方描述 |
| note | String | - | 同行说明文字 |
| leftIcon | IconData | - | 左侧图标 |
| arrow | bool | false | 显示右侧箭头 |
| required | bool | false | 显示必填星号 |
| onClick | Function | - | 点击事件 |

**示例**：
```dart
TDCellGroup(
  cells: [
    TDCell(
      arrow: true,
      title: '单行标题',
      onClick: (cell) => print('点击'),
    ),
    TDCell(
      arrow: true,
      title: '带描述',
      description: '描述信息',
    ),
  ],
)

// 卡片风格
const TDCellGroup(
  theme: TDCellGroupTheme.cardTheme,
  cells: [
    TDCell(arrow: true, title: '卡片风格'),
  ],
)
```

---

## TDText 文本

**功能**：文本控件，对系统 Text 进行扩展，支持主题字体配置。

**核心属性**：
| 属性 | 类型 | 默认值 | 说明 |
|------|------|--------|------|
| font | Font | - | 字体尺寸 |
| fontWeight | FontWeight | - | 字体粗细 |
| textColor | Color | - | 文本颜色 |
| isTextThrough | bool | false | 是否删除线 |
| forceVerticalCenter | bool | false | 是否强制居中 |

**示例**：
```dart
TDText(
  '文本内容',
  font: TDTheme.of(context).fontTitleLarge,
  textColor: TDTheme.of(context).textColorPrimary,
)
```

---

## 导入方式

```dart
import 'package:tdesign_flutter/tdesign_flutter.dart';
```