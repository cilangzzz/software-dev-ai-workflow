# TDesign Flutter 主题配置指南

本文档提供 TDesign Flutter 主题系统的完整配置方法，包括颜色、字体、圆角、阴影等属性配置。

---

## 一、主题系统概述

TDesign Flutter 的主题系统基于 `TDTheme` 和 `TDThemeData` 实现，支持：

- **颜色配置**：品牌色、功能色、文字色、背景色
- **字体配置**：字体尺寸、行高、字体家族
- **圆角配置**：多种圆角尺寸
- **阴影配置**：基础、中层、上层投影
- **间距配置**：常用 Margin 值
- **深色模式**：内置深色主题
- **自定义扩展**：TDExtraThemeData

---

## 二、主题使用方式

### 2.1 使用默认主题

```dart
void main() {
  runApp(
    TDTheme(
      data: TDTheme.defaultData(),
      child: MaterialApp(
        home: HomePage(),
      ),
    ),
  );
}
```

### 2.2 获取主题数据

```dart
// 在 build 方法中获取
final theme = TDTheme.of(context);

// 无 context 时获取默认主题
final theme = TDTheme.defaultData();

// 可空获取
final theme = TDTheme.ofNullable(context);
```

### 2.3 多套主题支持

```dart
// 开启多套主题功能
TDTheme.needMultiTheme(true);

// 切换主题
TDTheme(
  data: customThemeData,
  child: MaterialApp(...),
)
```

---

## 三、颜色配置

### 3.1 品牌色组

| 属性名 | 默认值 | 用途 |
|--------|--------|------|
| brandColor1 | #F2F3FF | 品牌浅色 |
| brandColor2 | #D9E1FF | 品牌浅色 |
| brandColor3 | #B5C7FF | 品牌浅色 |
| brandColor4 | #8EABFF | 品牌浅色 |
| brandColor5 | #618DFF | 品牌浅色 |
| brandColor6 | #366EF4 | 品牌悬停色 |
| brandColor7 | #0052D9 | 品牌主色 |
| brandColor8 | #003CAB | 品牌点击色 |
| brandColor9 | #002A7C | 品牌深色 |
| brandColor10 | #001A57 | 品牌深色 |

**常用品牌色**：
| 属性名 | 默认值 | 用途 |
|--------|--------|------|
| brandLightColor | #F2F3FF | 品牌浅色 |
| brandFocusColor | #D9E1FF | 品牌焦点色 |
| brandDisabledColor | #B5C7FF | 品牌禁用色 |
| brandHoverColor | #366EF4 | 品牌悬停色 |
| brandNormalColor | #0052D9 | 品牌主色 |
| brandClickColor | #003CAB | 品牌点击色 |

### 3.2 功能色组

**错误色**：
| 属性名 | 默认值 | 用途 |
|--------|--------|------|
| errorColor1 | #FFF0ED | 错误浅色 |
| errorColor6 | #D54941 | 错误主色 |
| errorNormalColor | #D54941 | 错误主色 |
| errorHoverColor | #F6685D | 错误悬停色 |

**警告色**：
| 属性名 | 默认值 | 用途 |
|--------|--------|------|
| warningColor1 | #FFF1E9 | 警告浅色 |
| warningNormalColor | #E37318 | 警告主色 |
| warningHoverColor | #FA9550 | 警告悬停色 |

**成功色**：
| 属性名 | 默认值 | 用途 |
|--------|--------|------|
| successColor1 | #E3F9E9 | 成功浅色 |
| successNormalColor | #2BA471 | 成功主色 |
| successHoverColor | #56C08D | 成功悬停色 |

### 3.3 文字色组

| 属性名 | 默认值 | 用途 |
|--------|--------|------|
| fontGyColor1 | #E6000000 (90%) | 主要文字 |
| fontGyColor2 | #99000000 (60%) | 次要文字 |
| fontGyColor3 | #66000000 (40%) | 占位文字 |
| fontGyColor4 | #42000000 (26%) | 禁用文字 |
| fontWhColor1 | #FFFFFFFF | 白色文字 |
| fontWhColor2 | #8CFFFFFF | 白色次要文字 |

**组件文字色**：
| 属性名 | 默认值 | 用途 |
|--------|--------|------|
| textColorPrimary | fontGyColor1 | 主要文字 |
| textColorSecondary | fontGyColor2 | 次要文字 |
| textColorPlaceholder | fontGyColor3 | 占位文字 |
| textDisabledColor | fontGyColor4 | 禁用文字 |
| textColorAnti | fontWhColor1 | 反色文字 |
| textColorBrand | brandNormalColor | 品牌文字 |
| textColorLink | brandNormalColor | 链接文字 |

### 3.4 背景色组

| 属性名 | 默认值 | 用途 |
|--------|--------|------|
| bgColorPage | grayColor2 | 页面背景 |
| bgColorContainer | whiteColor1 | 容器背景 |
| bgColorContainerHover | grayColor1 | 容器悬停背景 |
| bgColorContainerActive | grayColor3 | 容器激活背景 |
| bgColorSecondaryContainer | grayColor1 | 次级容器背景 |

### 3.5 中性色组

| 属性名 | 默认值 | 用途 |
|--------|--------|------|
| grayColor1 | #F3F3F3 | 最浅灰 |
| grayColor2 | #EEEEEE | 浅灰 |
| grayColor3 | #E7E7E7 | 浅灰 |
| grayColor4 | #DCDCDC | 灰色 |
| grayColor5 | #C5C5C5 | 灰色 |
| ... | ... | ... |
| grayColor14 | #181818 | 最深灰 |

---

## 四、字体配置

### 4.1 字体尺寸

| 属性名 | 字号 | 行高 | 用途 |
|--------|------|------|------|
| fontDisplayLarge | 64 | 72 | 大展示标题 |
| fontDisplayMedium | 48 | 56 | 中展示标题 |
| fontHeadlineLarge | 36 | 44 | 大标题 |
| fontHeadlineMedium | 28 | 36 | 中标题 |
| fontHeadlineSmall | 24 | 32 | 小标题 |
| fontTitleExtraLarge | 20 | 28 | 特大标题 |
| fontTitleLarge | 18 | 26 | 大标题 |
| fontTitleMedium | 16 | 24 | 中标题 |
| fontTitleSmall | 14 | 22 | 小标题 |
| fontBodyExtraLarge | 18 | 26 | 特大正文 |
| fontBodyLarge | 16 | 24 | 大正文 |
| fontBodyMedium | 14 | 22 | 中正文 |
| fontBodySmall | 12 | 20 | 小正文 |
| fontBodyExtraSmall | 10 | 16 | 特小正文 |

### 4.2 标记字体

| 属性名 | 字号 | 行高 | 用途 |
|--------|------|------|------|
| fontMarkLarge | 16 | 24 | 大标记 |
| fontMarkMedium | 14 | 22 | 中标记 |
| fontMarkSmall | 12 | 20 | 小标记 |
| fontMarkExtraSmall | 10 | 16 | 特小标记 |

### 4.3 链接字体

| 属性名 | 字号 | 行高 | 用途 |
|--------|------|------|------|
| fontLinkLarge | 16 | 24 | 大链接 |
| fontLinkMedium | 14 | 22 | 中链接 |
| fontLinkSmall | 12 | 20 | 小链接 |

### 4.4 字体使用

```dart
// 获取字体配置
final theme = TDTheme.of(context);
Font? titleFont = theme.fontTitleLarge;

// 在 TDText 中使用
TDText(
  '标题文字',
  font: theme.fontTitleLarge,
  fontWeight: FontWeight.w600,
)

// 获取字体属性
double fontSize = theme.fontTitleLarge?.fontSize ?? 16;
double lineHeight = theme.fontTitleLarge?.lineHeight ?? 24;
```

---

## 五、圆角配置

| 属性名 | 默认值 | 用途 |
|--------|--------|------|
| radiusSmall | 3 | 小圆角 |
| radiusDefault | 6 | 默认圆角 |
| radiusLarge | 9 | 大圆角 |
| radiusExtraLarge | 12 | 特大圆角 |
| radiusRound | 9999 | 胶囊型 |
| radiusCircle | 9999 | 圆形 |

**使用示例**：
```dart
final theme = TDTheme.of(context);
double radius = theme.radiusDefault;

Container(
  borderRadius: BorderRadius.circular(radius),
)
```

---

## 六、阴影配置

| 属性名 | 用途 |
|--------|------|
| shadowsBase | 基础投影 |
| shadowsMiddle | 中层投影 |
| shadowsTop | 上层投影 |

**使用示例**：
```dart
final theme = TDTheme.of(context);
List<BoxShadow>? shadows = theme.shadowsBase;

Container(
  decoration: BoxDecoration(
    boxShadow: shadows,
  ),
)
```

---

## 七、间距配置

| 属性名 | 默认值 | 用途 |
|--------|--------|------|
| spacer4 | 4 | 4px间距 |
| spacer8 | 8 | 8px间距 |
| spacer12 | 12 | 12px间距 |
| spacer16 | 16 | 16px间距 |
| spacer24 | 24 | 24px间距 |
| spacer32 | 32 | 32px间距 |
| spacer40 | 40 | 40px间距 |
| spacer48 | 48 | 48px间距 |
| spacer64 | 64 | 64px间距 |
| spacer96 | 96 | 96px间距 |
| spacer160 | 160 | 160px间距 |

---

## 八、自定义主题

### 8.1 JSON 配置方式

```dart
const themeJson = '''
{
  "custom": {
    "color": {
      "brandNormalColor": "#0052D9",
      "brandHoverColor": "#366EF4",
      "brandClickColor": "#003CAB",
      "successNormalColor": "#2BA471",
      "warningNormalColor": "#E37318",
      "errorNormalColor": "#D54941"
    },
    "font": {
      "fontTitleLarge": {
        "fontSize": 18,
        "lineHeight": 26
      },
      "fontBodyMedium": {
        "fontSize": 14,
        "lineHeight": 22
      }
    },
    "radius": {
      "radiusDefault": 6,
      "radiusLarge": 9
    },
    "shadow": {
      "shadowsBase": [
        {
          "color": "#0000001a",
          "blurRadius": 10,
          "spreadRadius": 0,
          "offset": { "x": 0, "y": 2 }
        }
      ]
    },
    "margin": {
      "spacer16": 16,
      "spacer24": 24
    }
  },
  "customDark": {
    "color": {
      "brandNormalColor": "#618DFF",
      "bgColorPage": "#181818",
      "bgColorContainer": "#242424"
    }
  }
}
''';

TDTheme(
  data: TDThemeData.fromJson('custom', themeJson)!,
  child: MaterialApp(...),
)
```

### 8.2 代码配置方式

```dart
final customTheme = TDTheme.defaultData().copyWithTDThemeData(
  'custom',
  colorMap: {
    'brandNormalColor': Color(0xFF0052D9),
    'brandHoverColor': Color(0xFF366EF4),
  },
  fontMap: {
    'fontTitleLarge': Font(fontSize: 18, lineHeight: 26),
  },
  radiusMap: {
    'radiusDefault': 6.0,
  },
);

TDTheme(
  data: customTheme,
  child: MaterialApp(...),
)
```

---

## 九、深色模式

### 9.1 内置深色主题

```dart
// 默认主题已包含深色模式配置
final theme = TDTheme.defaultData();

// 获取深色主题
TDThemeData? darkTheme = theme.dark;

// 系统主题适配
ThemeData systemDarkTheme = theme.systemThemeDataDark!;
```

### 9.2 配置深色主题

```dart
const themeJson = '''
{
  "custom": {
    "color": { "brandNormalColor": "#0052D9" }
  },
  "customDark": {
    "color": {
      "brandNormalColor": "#618DFF",
      "bgColorPage": "#181818",
      "bgColorContainer": "#242424",
      "textColorPrimary": "#E6000000"
    }
  }
}
''';

TDTheme(
  data: TDThemeData.fromJson('custom', themeJson)!,
  child: MaterialApp(
    theme: TDTheme.defaultData().systemThemeDataLight,
    darkTheme: TDTheme.defaultData().systemThemeDataDark,
    themeMode: ThemeMode.system,
    home: HomePage(),
  ),
)
```

---

## 十、主题扩展

### 10.1 自定义扩展主题

```dart
class MyExtraThemeData extends TDExtraThemeData {
  Color? customColor;
  double? customSpacing;

  @override
  void parse(String name, Map<String, dynamic> curThemeMap) {
    customColor = TDThemeData.toColor(curThemeMap['customColor']);
    customSpacing = curThemeMap['customSpacing']?.toDouble();
  }
}

// 使用扩展主题
final extraData = MyExtraThemeData();
TDTheme(
  data: TDThemeData.fromJson('custom', themeJson, extraThemeData: extraData)!,
  child: MaterialApp(...),
)

// 获取扩展数据
final extra = TDTheme.of(context).ofExtra<MyExtraThemeData>();
Color? myColor = extra?.customColor;
```

---

## 十一、资源代理

### 11.1 自定义资源加载

```dart
TDTheme.setResourceBuilder(
  (context) {
    // 根据条件返回不同的资源代理
    return DefaultTDResourceDelegate();
  },
  needAlwaysBuild: false,
);
```

---

## 十二、主题属性快速参考

### 颜色属性使用

```dart
final theme = TDTheme.of(context);

// 品牌色
Color primary = theme.brandNormalColor;
Color hover = theme.brandHoverColor;
Color disabled = theme.brandDisabledColor;

// 功能色
Color success = theme.successNormalColor;
Color warning = theme.warningNormalColor;
Color error = theme.errorNormalColor;

// 文字色
Color textPrimary = theme.textColorPrimary;
Color textSecondary = theme.textColorSecondary;
Color textPlaceholder = theme.textColorPlaceholder;

// 背景色
Color bgPage = theme.bgColorPage;
Color bgContainer = theme.bgColorContainer;
```

### 字体属性使用

```dart
// 使用 TDText
TDText(
  '标题',
  font: theme.fontTitleLarge,
  textColor: theme.textColorPrimary,
)

// 直接使用字号
TextStyle(
  fontSize: theme.fontTitleLarge?.fontSize,
  height: theme.fontTitleLarge?.lineHeight?.toDouble() / theme.fontTitleLarge?.fontSize,
)
```

---

## 十三、最佳实践

1. **全局包裹**：应用顶层使用 TDTheme 包裹
2. **统一获取**：统一使用 `TDTheme.of(context)` 获取
3. **深色适配**：配置完整的深色主题数据
4. **避免硬编码**：使用主题属性替代硬编码颜色值
5. **性能优化**：避免频繁切换主题，使用 const 构造函数