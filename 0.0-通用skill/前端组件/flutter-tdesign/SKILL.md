---
name: flutter-tdesign
description: TDesign Flutter 组件库开发专家 - 基于腾讯 TDesign 设计体系的 Flutter UI 组件库，支持50+预制组件、主题定制、深色模式、国际化。触发场景：(1) Flutter UI 开发 (2) TDesign 组件使用 (3) 主题定制需求 (4) 移动端/Web 应用开发
---

# Skill: flutter-tdesign

## 基本信息

| 属性 | 值 |
|------|-----|
| **名称** | TDesign Flutter 组件库 |
| **版本** | 0.2.7 |
| **技术栈** | Flutter 3.16+, Dart 3.2.6+ |
| **组件数量** | 50+ |
| **图标数量** | 2113 |

## 功能描述

基于腾讯 TDesign 设计体系的 Flutter UI 组件库，提供 50+ 预制组件、主题定制、深色模式、国际化支持。

## 触发条件

### 命令触发
- `/tdesign`

### 自然语言触发
- "使用 TDesign Flutter" / "Flutter UI 组件"
- "TDButton/TDDialog/TDToast..."
- "TDesign 主题配置"

## 输入参数

| 参数 | 类型 | 默认值 | 说明 |
|------|------|--------|------|
| component | string | - | 组件名称 |
| category | string | - | 组件分类(basic/form/navigation/feedback/display/operation) |

## 参考文档（按需加载）

### 组件文档
- [组件索引](references/components/index.md) - 快速查找组件
- 按分类加载：
  - [基础组件](references/components/basic.md) - Button, Icon, Link, Divider, Cell, Text
  - [表单组件](references/components/form.md) - Input, Checkbox, Radio, Switch, Slider...
  - [导航组件](references/components/navigation.md) - NavBar, TabBar, SideBar...
  - [反馈组件](references/components/feedback.md) - Dialog, Toast, Message, ActionSheet...
  - [展示组件](references/components/display.md) - Avatar, Badge, Tag, Image...
  - [操作组件](references/components/operation.md) - DropdownMenu, SwipeCell, BackTop...
  - [其他组件](references/components/other.md) - NoticeBar, Steps, Table...

### 配置文档
- [主题指南](references/theme-guide.md) - 颜色、字体、圆角、阴影配置
- [开发规范](references/rules/flutter-tdesign.md) - 最佳实践

### 快速参考
- [图标速查](references/icons-reference.md) - 常用图标列表
- [API速查](references/api-reference.md) - 核心 API 索引

## 快速示例

### 按钮组件
```dart
const TDButton(
  text: '按钮',
  type: TDButtonType.fill,
  theme: TDButtonTheme.primary,
)
```

### Toast 提示
```dart
TDToast.showSuccess('成功', context: context);
TDToast.showLoading(context: context);
```

### 主题配置
```dart
TDTheme(
  data: TDTheme.defaultData(),
  child: MaterialApp(...),
)
```

## 导入方式

```dart
import 'package:tdesign_flutter/tdesign_flutter.dart';
```