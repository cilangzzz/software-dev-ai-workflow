# 其他组件

本分类包含 10 个其他组件。

---

## TDNoticeBar 公告栏

**功能**：公告栏组件，支持跑马灯效果。

**核心属性**：
| 属性 | 类型 | 默认值 | 说明 |
|------|------|--------|------|
| content | String | - | 文本内容 |
| marquee | bool | false | 跑马灯效果 |
| theme | TDNoticeBarTheme | info | 主题 |

**示例**：
```dart
TDNoticeBar(
  content: '公告内容',
  marquee: true,
)
```

---

## TDPopover 气泡弹出框

**功能**：气泡弹出框组件。

**核心属性**：
| 属性 | 类型 | 默认值 | 说明 |
|------|------|--------|------|
| content | String | - | 显示内容 |
| placement | TDPopoverPlacement | - | 浮层出现位置 |

**示例**：
```dart
TDPopover.showPopover(
  context: context,
  content: '气泡内容',
)
```

---

## TDSteps 步骤条

**功能**：步骤条组件。

**核心属性**：
| 属性 | 类型 | 默认值 | 说明 |
|------|------|--------|------|
| activeIndex | int | 0 | 当前激活的索引 |
| direction | TDStepsDirection | horizontal | 方向 |
| steps | List | - | 步骤条数据 |

**示例**：
```dart
TDSteps(
  activeIndex: 1,
  steps: [
    TDStepsItemData(title: '步骤一'),
    TDStepsItemData(title: '步骤二'),
  ],
)
```

---

## TDTable 表格

**功能**：表格组件。

**核心属性**：
| 属性 | 类型 | 默认值 | 说明 |
|------|------|--------|------|
| columns | List<TDTableCol> | - | 列配置 |
| data | List | - | 数据源 |
| bordered | bool | false | 是否显示边框 |

**示例**：
```dart
TDTable(
  columns: [
    TDTableCol(title: '列一'),
  ],
  data: [{'列一': '数据'}],
)
```

---

## TDTreeSelect 树形选择

**功能**：树形选择组件。

**核心属性**：
| 属性 | 类型 | 默认值 | 说明 |
|------|------|--------|------|
| options | List | - | 展示的选项列表 |
| multiple | bool | false | 支持多选 |
| onChange | Function | - | 选中值发生变化 |

**示例**：
```dart
TDTreeSelect(
  options: treeOptions,
  onChange: (value) {},
)
```

---

## TDTimeCounter 计时器

**功能**：计时器组件，支持倒计时和正计时。

**核心属性**：
| 属性 | 类型 | 默认值 | 说明 |
|------|------|--------|------|
| time | int | - | 计时时长（毫秒） |
| direction | TDTimeCounterDirection | down | 计时方向 |
| format | String | HH:mm:ss | 时间格式 |
| onFinish | Function | - | 计时结束回调 |

**示例**：
```dart
TDTimeCounter(
  time: 60000, // 60秒
  direction: TDTimeCounterDirection.down,
  onFinish: () {
    print('计时结束');
  },
)
```

---

## TDTheme 主题控件

**功能**：主题管理组件。

**核心方法**：
| 方法 | 说明 |
|------|------|
| defaultData() | 获取默认主题数据 |
| of(context) | 获取当前主题数据 |
| needMultiTheme(bool) | 开启多套主题功能 |

**示例**：
```dart
TDTheme(
  data: TDTheme.defaultData(),
  child: MaterialApp(...),
)

// 获取主题
final theme = TDTheme.of(context);
Color primary = theme.brandNormalColor;
```

> 详细主题配置见 [theme-guide.md](../theme-guide.md)

---

## TDPageTransformer 页面变换器

**功能**：页面变换器组件。

**核心属性**：
| 属性 | 类型 | 默认值 | 说明 |
|------|------|--------|------|
| margin | double | - | 左右间隔 |
| scale | double | - | 缩放比例 |
| fade | double | - | 淡化比例 |

---

## TDFontLoader 字体加载器

**功能**：自定义字体加载组件。

---

## TDMap 自定义Map

**功能**：支持引用的主题Map类型。