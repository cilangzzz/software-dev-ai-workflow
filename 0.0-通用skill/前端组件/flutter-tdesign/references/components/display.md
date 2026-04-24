# 展示组件

本分类包含 10 个展示组件。

---

## TDAvatar 头像

**功能**：头像组件，支持图标、图片、自定义文字、展示等类型。

**核心属性**：
| 属性 | 类型 | 默认值 | 说明 |
|------|------|--------|------|
| avatarUrl | String | - | 头像地址 |
| size | TDAvatarSize | medium | 头像尺寸 |
| type | TDAvatarType | normal | 头像类型 |
| shape | TDAvatarShape | circle | 头像形状 |
| text | String | - | 自定义文字 |

**示例**：
```dart
const TDAvatar(
  size: TDAvatarSize.medium,
  type: TDAvatarType.normal,
  defaultUrl: 'assets/img/avatar.png',
)

// 文字头像
const TDAvatar(
  size: TDAvatarSize.medium,
  type: TDAvatarType.customText,
  text: 'A',
)
```

---

## TDBadge 徽标

**功能**：徽标组件，支持红点、消息、气泡、方形、角标等样式。

**核心属性**：
| 属性 | 类型 | 默认值 | 说明 |
|------|------|--------|------|
| type | TDBadgeType | redPoint | 红点样式 |
| count | String | - | 红点数量 |
| maxCount | String | 99 | 最大红点数量 |
| size | TDBadgeSize | small | 红点尺寸 |

**示例**：
```dart
const TDBadge(TDBadgeType.redPoint)
TDBadge(TDBadgeType.message, count: '8')
```

---

## TDTag 标签

**功能**：展示型标签组件，支持方形、圆角、半圆、带关闭图标等样式。

**核心属性**：
| 属性 | 类型 | 默认值 | 说明 |
|------|------|--------|------|
| text | String | 必填 | 标签内容 |
| theme | TDTagTheme | - | 主题 |
| size | TDTagSize | medium | 标签大小 |
| shape | TDTagShape | square | 标签形状 |
| isOutline | bool | false | 是否为描边类型 |

**示例**：
```dart
const TDTag('标签文字')
const TDTag('标签文字', theme: TDTagTheme.primary)
TDTag('标签文字', needCloseIcon: true)
```

---

## TDImage 图片

**功能**：图片组件，支持裁剪、适应、方形、圆角、圆形等类型。

**核心属性**：
| 属性 | 类型 | 默认值 | 说明 |
|------|------|--------|------|
| imgUrl | String | - | 图片地址 |
| type | TDImageType | roundedSquare | 图片类型 |
| width/height | double | - | 自定义宽/高 |
| fit | BoxFit | - | 适配样式 |

**示例**：
```dart
TDImage(
  imgUrl: 'https://example.com/image.png',
  type: TDImageType.circle,
)
```

---

## TDImageViewer 图片预览

**功能**：图片预览工具，支持图片查看、删除、索引显示等。

**核心属性**：
| 属性 | 类型 | 默认值 | 说明 |
|------|------|--------|------|
| images | List | - | 图片列表 |
| closeBtn | bool | true | 是否显示关闭按钮 |
| showIndex | bool | true | 是否显示索引 |

**示例**：
```dart
TDImageViewer.showImageViewer(
  context: context,
  images: ['url1', 'url2'],
)
```

---

## TDEmpty 空状态

**功能**：空状态组件，用于空数据展示。

**核心属性**：
| 属性 | 类型 | 默认值 | 说明 |
|------|------|--------|------|
| type | TDEmptyType | plain | 类型 |
| icon | IconData | - | 图标 |
| emptyText | String | - | 描述文字 |
| operationText | String | - | 操作按钮文案 |

**示例**：
```dart
const TDEmpty(
  type: TDEmptyType.plain,
  emptyText: '暂无数据',
)
```

---

## TDCalendar 日历

**功能**：日历组件，支持单选、多选、区间选择。

**核心属性**：
| 属性 | 类型 | 默认值 | 说明 |
|------|------|--------|------|
| type | CalendarType | single | 选择类型 |
| minDate/maxDate | int | - | 最小/最大可选日期 |
| value | List<int> | - | 当前选择的日期 |
| onChange | Function | - | 选中值变化回调 |

**示例**：
```dart
TDCalendar(
  type: CalendarType.single,
  onChange: (value) {},
)
```

---

## TDSwiper 轮播图

**功能**：轮播图指示器样式，支持圆点、圆角矩形、数字、箭头样式。

**示例**：
```dart
TDSwiperPagination.dots(activeColor: Colors.blue)
TDSwiperPagination.fraction()
```

---

## TDCollapse 折叠面板

**功能**：折叠面板组件，支持 Block 通栏风格和 Card 卡片风格。

**核心属性**：
| 属性 | 类型 | 默认值 | 说明 |
|------|------|--------|------|
| children | List | - | 子组件 |
| style | TDCollapseStyle | block | 样式 |

**示例**：
```dart
TDCollapse(
  children: [
    TDCollapsePanel(
      headerBuilder: (context, isExpanded) => Text('标题'),
      body: Text('内容'),
    ),
  ],
)
```

---

## TDSkeleton 骨架屏

**功能**：骨架屏组件，用于加载占位。

**核心属性**：
| 属性 | 类型 | 默认值 | 说明 |
|------|------|--------|------|
| theme | TDSkeletonTheme | text | 主题 |
| animation | TDSkeletonAnimation | - | 动画效果 |

**示例**：
```dart
const TDSkeleton(theme: TDSkeletonTheme.avatarText)
```