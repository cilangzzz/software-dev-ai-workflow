# 导航组件

本分类包含 7 个导航组件。

---

## TDNavBar 导航栏

**功能**：导航栏组件，支持标题居中、返回按钮、左右操作项。

**核心属性**：
| 属性 | 类型 | 默认值 | 说明 |
|------|------|--------|------|
| title | String | - | 标题文案 |
| titleWidget | Widget | - | 标题控件 |
| centerTitle | bool | true | 标题是否居中 |
| backgroundColor | Color | - | 背景颜色 |
| useDefaultBack | bool | true | 使用默认返回 |
| leftBarItems | List | - | 左边操作项 |
| rightBarItems | List | - | 右边操作项 |

**示例**：
```dart
const TDNavBar(
  height: 48,
  title: '标题文字',
  useDefaultBack: true,
)

// 带右侧操作
TDNavBar(
  title: '标题',
  rightBarItems: [
    TDNavBarItem(icon: Icon(TDIcons.setting)),
  ],
)
```

---

## TDTabBar 标签栏

**功能**：标签栏组件，支持等宽、滚动、胶囊样式。

**核心属性**：
| 属性 | 类型 | 默认值 | 说明 |
|------|------|--------|------|
| tabs | List<TDTab> | - | tab数组 |
| controller | TabController | - | tab控制器 |
| showIndicator | bool | false | 是否展示引导控件 |
| outlineType | TDTabBarOutlineType | filled | 选项卡样式 |
| onTap | Function | - | 点击事件 |

**示例**：
```dart
TDTabBar(
  tabs: const [
    TDTab(text: '选项1'),
    TDTab(text: '选项2'),
  ],
  controller: TabController(length: 2, vsync: this),
  showIndicator: true,
)

// 胶囊样式
TDTabBar(
  tabs: const [TDTab(text: '选项1'), TDTab(text: '选项2')],
  outlineType: TDTabBarOutlineType.capsule,
)
```

---

## TDBottomTabBar 底部标签栏

**功能**：底部标签栏，支持纯文本、图标+文本、纯图标、展开面板等样式。

**核心属性**：
| 属性 | 类型 | 默认值 | 说明 |
|------|------|--------|------|
| basicType | TDBottomTabBarBasicType | - | 基本样式 |
| navigationTabs | List | - | tabs配置 |
| currentIndex | int | - | 选中的index |
| outlineType | TDBottomTabBarOutlineType | filled | 标签栏样式 |

**示例**：
```dart
TDBottomTabBar(
  basicType: TDBottomTabBarBasicType.iconText,
  navigationTabs: [
    TDBottomTabBarTabConfig(
      selectedIcon: Icon(TDIcons.home_filled),
      unselectedIcon: Icon(TDIcons.home),
      text: '首页',
    ),
  ],
  currentIndex: 0,
)
```

---

## TDSideBar 侧边导航

**功能**：侧边导航栏组件，支持选中状态和滚动定位。

**核心属性**：
| 属性 | 类型 | 默认值 | 说明 |
|------|------|--------|------|
| value | int | - | 选项值 |
| children | List | - | 单项列表 |
| style | TDSideBarStyle | normal | 样式 |
| onChanged | Function | - | 选中值变化回调 |

**示例**：
```dart
TDSideBar(
  value: 0,
  children: [
    TDSideBarItem(title: '选项一'),
    TDSideBarItem(title: '选项二'),
  ],
  onChanged: (value) {},
)
```

---

## TDIndexes 索引

**功能**：索引组件，用于快速定位列表内容。

**核心属性**：
| 属性 | 类型 | 默认值 | 说明 |
|------|------|--------|------|
| indexList | List<String> | A-Z | 索引字符列表 |
| sticky | bool | true | 锚点是否吸顶 |
| capsuleTheme | bool | false | 是否为胶囊式样式 |
| onChange | Function | - | 索引变更回调 |

**示例**：
```dart
TDIndexes(
  indexList: ['A', 'B', 'C'],
  onChange: (index) {},
)
```

---

## TDDrawer 抽屉

**功能**：抽屉组件，支持左右方向弹出。

**核心属性**：
| 属性 | 类型 | 默认值 | 说明 |
|------|------|--------|------|
| placement | TDDrawerPlacement | right | 抽屉方向 |
| title | String | - | 抽屉标题 |
| items | List | - | 抽屉里的列表项 |
| width | double | 280 | 宽度 |
| showOverlay | bool | true | 是否显示遮罩层 |

**示例**：
```dart
TDDrawer(
  placement: TDDrawerPlacement.left,
  title: '抽屉标题',
  items: [
    TDDrawerItem(title: '选项一'),
    TDDrawerItem(title: '选项二'),
  ],
)
```

---

## TDFooter 页脚

**功能**：页脚组件，支持文字、链接、品牌样式。

**核心属性**：
| 属性 | 类型 | 默认值 | 说明 |
|------|------|--------|------|
| type | TDFooterType | text | 样式 |
| text | String | - | 文字 |
| links | List | - | 链接列表 |
| logo | String | - | 品牌图片 |

**示例**：
```dart
const TDFooter(
  type: TDFooterType.text,
  text: 'Copyright © 2024',
)
```