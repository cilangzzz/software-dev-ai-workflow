# 操作组件

本分类包含 6 个操作组件。

---

## TDDropdownMenu 下拉菜单

**功能**：下拉菜单组件，支持向下、向上、自动方向展开。

**核心属性**：
| 属性 | 类型 | 默认值 | 说明 |
|------|------|--------|------|
| items | List | - | 下拉菜单列表 |
| direction | TDDropdownMenuDirection | auto | 菜单展开方向 |
| showOverlay | bool | true | 是否显示遮罩层 |

**示例**：
```dart
TDDropdownMenu(
  items: [
    TDDropdownItem(
      label: '选项一',
      options: [
        TDDropdownItemOption(label: '子选项一', value: '1'),
      ],
    ),
  ],
)
```

---

## TDSwipeCell 滑动单元格

**功能**：滑动单元格组件，支持左右滑动展示操作按钮。

**核心属性**：
| 属性 | 类型 | 默认值 | 说明 |
|------|------|--------|------|
| cell | Widget | 必填 | 单元格组件 |
| left/right | TDSwipeCellPanel | - | 左侧/右侧滑动操作项 |
| disabled | bool | false | 是否禁用滑动 |

**示例**：
```dart
TDSwipeCell(
  right: TDSwipeCellPanel(
    children: [
      TDSwipeCellAction(label: '删除', backgroundColor: Colors.red),
    ],
  ),
  cell: TDCell(title: '左滑删除'),
)
```

---

## TDBackTop 返回顶部

**功能**：返回顶部按钮组件。

**核心属性**：
| 属性 | 类型 | 默认值 | 说明 |
|------|------|--------|------|
| controller | ScrollController | - | 页面滚动控制器 |
| theme | TDBackTopTheme | light | 主题 |
| style | TDBackTopStyle | circle | 样式 |

**示例**：
```dart
TDBackTop(
  controller: scrollController,
  onClick: () {
    scrollController.animateTo(0, duration: Duration(milliseconds: 300), curve: Curves.ease);
  },
)
```

---

## TDFab 悬浮按钮

**功能**：悬浮按钮组件，支持圆形和矩形形状。

**核心属性**：
| 属性 | 类型 | 默认值 | 说明 |
|------|------|--------|------|
| theme | TDFabTheme | default | 主题 |
| shape | TDFabShape | circle | 形状 |
| size | TDFabSize | large | 大小 |
| icon | Icon | - | 图标 |

**示例**：
```dart
TDFab(
  icon: Icon(TDIcons.add),
  onClick: () {},
)
```

---

## TDRefreshHeader 下拉刷新

**功能**：下拉刷新头部，结合 EasyRefresh 实现。

**核心属性**：
| 属性 | 类型 | 默认值 | 说明 |
|------|------|--------|------|
| extent | double | 48 | Header容器高度 |
| loadingIcon | TDLoadingIcon | circle | loading样式 |

---

## TDSlidePopupRoute 滑动弹出路由

**功能**：滑动弹出路由组件。

**核心属性**：
| 属性 | 类型 | 默认值 | 说明 |
|------|------|--------|------|
| slideTransitionFrom | SlideTransitionFrom | bottom | 从哪个方向滑出 |
| builder | WidgetBuilder | 必填 | 控件构建器 |
| isDismissible | bool | true | 点击蒙层能否关闭 |

**示例**：
```dart
Navigator.of(context).push(
  TDSlidePopupRoute(
    slideTransitionFrom: SlideTransitionFrom.bottom,
    builder: (context) => Container(height: 200),
  ),
)
```