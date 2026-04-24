# TDesign Flutter 开发规范

本文档提供使用 TDesign Flutter 组件库的开发规范和最佳实践。

---

## 一、基础规范

### 1.1 导入方式

```dart
// 推荐导入方式
import 'package:tdesign_flutter/tdesign_flutter.dart';
```

### 1.2 版本要求

| 依赖 | 最低版本 |
|------|---------|
| Flutter | 3.16.0 |
| Dart | 3.2.6 |

### 1.3 pubspec.yaml 配置

```yaml
dependencies:
  tdesign_flutter: ^0.2.7
```

---

## 二、主题规范

### 2.1 应用顶层包裹

**必须**在应用顶层使用 TDTheme 包裹：

```dart
void main() {
  runApp(
    TDTheme(
      data: TDTheme.defaultData(),
      child: MaterialApp(
        title: 'App',
        home: HomePage(),
      ),
    ),
  );
}
```

### 2.2 主题获取规范

**推荐**使用 `TDTheme.of(context)` 获取主题：

```dart
// 推荐
final theme = TDTheme.of(context);
Color primary = theme.brandNormalColor;

// 不推荐（硬编码）
Color primary = Color(0xFF0052D9);
```

### 2.3 避免硬编码颜色

**必须**使用主题颜色替代硬编码：

```dart
// 推荐
TDButton(
  text: '按钮',
  theme: TDButtonTheme.primary,
)

// 推荐（自定义颜色使用主题）
Container(
  color: TDTheme.of(context).bgColorContainer,
)

// 不推荐
Container(
  color: Colors.white,
)
```

---

## 三、组件命名规范

### 3.1 组件前缀

所有 TDesign 组件以 `TD` 前缀命名：

- `TDButton`
- `TDInput`
- `TDDialog`
- `TDToast`

### 3.2 类型/样式命名

| 后缀 | 用途 |
|------|------|
| Type | 类型枚举 |
| Size | 尺寸枚举 |
| Style | 样式枚举 |
| Theme | 主题枚举 |
| Shape | 形状枚举 |

---

## 四、组件使用规范

### 4.1 const 构造函数

**推荐**使用 const 构造函数提升性能：

```dart
// 推荐
const TDButton(
  text: '按钮',
  type: TDButtonType.fill,
)

// 不推荐（动态属性不可用const）
TDButton(
  text: dynamicText,
  onTap: () {},
)
```

### 4.2 组件尺寸规范

| 尺寸 | 使用场景 |
|------|----------|
| large | 主要按钮、重要操作 |
| medium | 默认尺寸、常规组件 |
| small | 辅助按钮、紧凑布局 |
| extraSmall | 极小场景 |

### 4.3 按钮规范

```dart
// 主操作按钮
TDButton(
  text: '确定',
  type: TDButtonType.fill,
  theme: TDButtonTheme.primary,
  size: TDButtonSize.large,
)

// 次操作按钮
TDButton(
  text: '取消',
  type: TDButtonType.outline,
  theme: TDButtonTheme.defaultTheme,
)

// 危险操作按钮
TDButton(
  text: '删除',
  type: TDButtonType.fill,
  theme: TDButtonTheme.danger,
)
```

---

## 五、表单规范

### 5.1 输入框规范

```dart
TDInput(
  leftLabel: '标签',
  hintText: '请输入',
  controller: TextEditingController(),
  onChanged: (text) {
    // 处理输入
  },
  additionInfo: errorText, // 错误提示
)
```

### 5.2 表单校验规范

```dart
TDForm(
  items: [
    TDFormItem(
      label: '用户名',
      name: 'username',
      requiredMark: true,
      child: TDInput(hintText: '请输入用户名'),
    ),
  ],
  rules: {
    'username': TDFormValidation(
      required: true,
      message: '用户名不能为空',
    ),
  },
  onSubmit: (data) {
    // 提交处理
  },
)
```

---

## 六、反馈规范

### 6.1 Toast 使用规范

```dart
// 成功提示
TDToast.showSuccess('操作成功', context: context);

// 失败提示
TDToast.showFail('操作失败', context: context);

// 加载提示（需手动关闭）
TDToast.showLoading(context: context);
// 操作完成后
TDToast.dismissLoading();
```

### 6.2 Dialog 使用规范

```dart
showGeneralDialog(
  context: context,
  pageBuilder: (context, animation, secondaryAnimation) {
    return TDConfirmDialog(
      title: '确认操作',
      content: '是否继续？',
    );
  },
);
```

---

## 七、导航规范

### 7.1 导航栏规范

```dart
TDNavBar(
  title: '页面标题',
  centerTitle: true,
  useDefaultBack: true,
  rightBarItems: [
    TDNavBarItem(
      icon: Icon(TDIcons.setting),
      action: () {
        // 右侧操作
      },
    ),
  ],
)
```

### 7.2 底部标签栏规范

```dart
TDBottomTabBar(
  basicType: TDBottomTabBarBasicType.iconText,
  navigationTabs: [
    TDBottomTabBarTabConfig(
      selectedIcon: Icon(TDIcons.home_filled),
      unselectedIcon: Icon(TDIcons.home),
      text: '首页',
    ),
    TDBottomTabBarTabConfig(
      selectedIcon: Icon(TDIcons.user_filled),
      unselectedIcon: Icon(TDIcons.user),
      text: '我的',
    ),
  ],
  currentIndex: 0,
)
```

---

## 八、图标规范

### 8.1 图标使用

```dart
// 推荐
Icon(TDIcons.search)
Icon(TDIcons.check_circle_filled, size: 24)

// 不推荐（使用其他图标库）
Icon(Icons.search)
```

### 8.2 图标颜色

```dart
// 推荐（使用主题颜色）
Icon(
  TDIcons.search,
  color: TDTheme.of(context).brandNormalColor,
)

// 不推荐
Icon(TDIcons.search, color: Colors.blue)
```

---

## 九、性能规范

### 9.1 避免不必要的重建

```dart
// 推荐
class MyWidget extends StatelessWidget {
  const MyWidget({Key? key}) : super(key: key);
  
  @override
  Widget build(BuildContext context) {
    return const TDButton(text: '按钮');
  }
}

// 不推荐
class MyWidget extends StatefulWidget {
  @override
  Widget build(BuildContext context) {
    return TDButton(text: '按钮'); // 无状态但使用StatefulWidget
  }
}
```

### 9.2 列表优化

```dart
ListView.builder(
  itemBuilder: (context, index) {
    return const TDCell(title: '标题'); // 使用const
  },
  itemCount: 100,
)
```

---

## 十、深色模式规范

### 10.1 配置深色主题

```dart
MaterialApp(
  theme: TDTheme.defaultData().systemThemeDataLight,
  darkTheme: TDTheme.defaultData().systemThemeDataDark,
  themeMode: ThemeMode.system,
)
```

### 10.2 主题适配

```dart
// 使用主题颜色，自动适配深色模式
Container(
  color: TDTheme.of(context).bgColorContainer,
  child: TDText(
    '文字',
    textColor: TDTheme.of(context).textColorPrimary,
  ),
)
```

---

## 十一、响应式规范

### 11.1 屏幕适配

```dart
TDNavBar(
  screenAdaptation: true, // 开启屏幕适配
)
```

### 11.2 安全区域

```dart
TDBottomTabBar(
  useSafeArea: true, // 使用安全区域
)
```

---

## 十二、国际化规范

### 12.1 多语言支持

```dart
TDButton(
  text: localizations.buttonText,
)
```

---

## 十三、错误处理规范

### 13.1 输入校验

```dart
TDInput(
  additionInfo: errorMessage,
  additionInfoColor: TDTheme.of(context).errorNormalColor,
)
```

### 13.2 异常处理

```dart
try {
  await someOperation();
  TDToast.showSuccess('成功', context: context);
} catch (e) {
  TDToast.showFail('失败: $e', context: context);
}
```

---

## 十四、代码组织规范

### 14.1 组件封装

```dart
// 推荐：封装通用组件
class MyButton extends StatelessWidget {
  final String text;
  final VoidCallback? onTap;
  
  const MyButton({
    Key? key,
    required this.text,
    this.onTap,
  }) : super(key: key);
  
  @override
  Widget build(BuildContext context) {
    return TDButton(
      text: text,
      type: TDButtonType.fill,
      theme: TDButtonTheme.primary,
      onTap: onTap,
    );
  }
}
```

### 14.2 常量定义

```dart
// 推荐：集中定义常量
class AppConstants {
  static const String appName = 'MyApp';
  static const double defaultPadding = 16.0;
}
```

---

## 十五、测试规范

### 15.1 Widget 测试

```dart
testWidgets('TDButton test', (WidgetTester tester) async {
  await tester.pumpWidget(
    TDTheme(
      data: TDTheme.defaultData(),
      child: MaterialApp(
        home: const TDButton(text: '测试按钮'),
      ),
    ),
  );
  
  expect(find.text('测试按钮'), findsOneWidget);
});
```

---

## 十六、注意事项清单

| 规范项 | 级别 | 说明 |
|--------|------|------|
| 顶层包裹 TDTheme | 必须 | 应用顶层必须使用 TDTheme |
| 使用主题颜色 | 必须 | 禁止硬编码颜色值 |
| 使用 const 构造函数 | 推荐 | 提升性能 |
| 统一图标库 | 必须 | 使用 TDIcons |
| 深色模式适配 | 推荐 | 配置深色主题 |
| 输入校验提示 | 必须 | 显示错误信息 |
| 加载提示关闭 | 必须 | 手动关闭 Loading Toast |
| 安全区域处理 | 推荐 | 使用 useSafeArea |

---

## 十七、常见问题

### Q1: 组件颜色不正确？
A: 确保应用顶层使用 TDTheme 包裹。

### Q2: 主题切换后颜色不更新？
A: 使用 `TDTheme.of(context)` 获取主题，确保在 build 方法中获取。

### Q3: 图标显示异常？
A: 确保 TDIcons 字体文件正确加载。

### Q4: 深色模式不生效？
A: 配置 MaterialApp 的 darkTheme 和 themeMode。

---

## 十八、最佳实践总结

1. **主题一致性**：统一使用 TDTheme，避免硬编码
2. **性能优化**：合理使用 const 和 StatelessWidget
3. **用户体验**：合理使用 Toast、Dialog、Loading
4. **响应式设计**：使用屏幕适配和安全区域
5. **代码规范**：遵循 Flutter 和 TDesign 命名规范