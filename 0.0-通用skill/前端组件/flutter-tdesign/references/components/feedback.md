# 反馈组件

本分类包含 8 个反馈组件。

---

## TDDialog 对话框

**功能**：弹窗组件，支持 Alert、Confirm、Image、Input 等类型。

**核心属性**：
| 属性 | 类型 | 默认值 | 说明 |
|------|------|--------|------|
| title | String | - | 标题内容 |
| content | String | - | 内容 |
| leftBtn/rightBtn | TDDialogButtonOptions | - | 按钮配置 |
| showCloseButton | bool | false | 显示关闭按钮 |

**示例**：
```dart
// 确认对话框
showGeneralDialog(
  context: context,
  pageBuilder: (context, animation, secondaryAnimation) {
    return TDConfirmDialog(
      title: '对话框标题',
      content: '告知当前状态、信息和解决方法',
    );
  },
);

// 输入对话框
showGeneralDialog(
  context: context,
  pageBuilder: (context, animation, secondaryAnimation) {
    return TDInputDialog(
      title: '请输入',
      hintText: '输入提示',
      textEditingController: controller,
    );
  },
);
```

---

## TDToast 轻提示

**功能**：Toast 轻提示组件，支持文本、图标、加载等样式。

**核心方法**：
| 方法 | 说明 |
|------|------|
| showText | 普通文本 Toast |
| showSuccess | 成功提示 |
| showFail | 失败提示 |
| showWarning | 警告提示 |
| showLoading | 加载提示 |
| dismissLoading | 关闭加载 |

**示例**：
```dart
TDToast.showText('提示文字', context: context);
TDToast.showSuccess('操作成功', context: context);
TDToast.showLoading(context: context);
TDToast.dismissLoading();
```

---

## TDMessage 消息通知

**功能**：消息通知组件，支持 info/success/warning/error 主题。

**核心属性**：
| 属性 | 类型 | 默认值 | 说明 |
|------|------|--------|------|
| content | String | - | 通知内容 |
| theme | MessageTheme | info | 消息主题 |
| duration | int | 3000 | 计时器 |
| closeBtn | dynamic | - | 关闭按钮 |

**示例**：
```dart
TDMessage.showMessage(
  context: context,
  content: '消息内容',
  theme: MessageTheme.success,
);
```

---

## TDActionSheet 动作面板

**功能**：动作面板组件，支持列表、宫格、分组三种样式。

**核心属性**：
| 属性 | 类型 | 默认值 | 说明 |
|------|------|--------|------|
| theme | TDActionSheetTheme | list | 主题样式 |
| items | List | - | 项目列表 |
| showCancel | bool | true | 是否显示取消按钮 |

**示例**：
```dart
TDActionSheet.showListActionSheet(
  context: context,
  items: [
    TDActionSheetItem(label: '选项一'),
    TDActionSheetItem(label: '选项二'),
  ],
);
```

---

## TDPopup 弹出层

**功能**：弹出层组件，支持底部弹出和居中弹出。

**示例**：
```dart
// 底部弹出
Navigator.of(context).push(
  TDSlidePopupRoute(
    slideTransitionFrom: SlideTransitionFrom.bottom,
    builder: (context) {
      return TDPopupBottomDisplayPanel(
        title: '标题',
        child: Container(height: 240),
      );
    },
  ),
);

// 居中弹出
Navigator.of(context).push(
  TDSlidePopupRoute(
    slideTransitionFrom: SlideTransitionFrom.center,
    builder: (context) {
      return TDPopupCenterPanel(
        child: SizedBox(width: 240, height: 240),
      );
    },
  ),
);
```

---

## TDLoading 加载

**功能**：加载组件，支持圆形、点状、菊花状三种图标样式。

**核心属性**：
| 属性 | 类型 | 默认值 | 说明 |
|------|------|--------|------|
| size | TDLoadingSize | - | 尺寸 |
| icon | TDLoadingIcon | circle | 图标类型 |
| iconColor | Color | - | 图标颜色 |
| text | String | - | 文案 |

**示例**：
```dart
const TDLoading(
  size: TDLoadingSize.medium,
  icon: TDLoadingIcon.circle,
)

// 带文字
const TDLoading(
  size: TDLoadingSize.small,
  icon: TDLoadingIcon.circle,
  text: '加载中...',
)
```

---

## TDProgress 进度条

**功能**：进度条组件，支持线性、环形、微进度、按钮进度四种类型。

**核心属性**：
| 属性 | 类型 | 默认值 | 说明 |
|------|------|--------|------|
| type | TDProgressType | linear | 进度条类型 |
| value | double | - | 进度值(0-1) |
| strokeWidth | double | - | 进度条粗细 |
| color | Color | - | 进度条颜色 |

**示例**：
```dart
TDProgress(
  type: TDProgressType.linear,
  value: 0.5,
)

TDProgress(
  type: TDProgressType.circular,
  value: 0.7,
)
```

---

## TDResult 结果页

**功能**：结果页组件，用于展示操作结果。

**核心属性**：
| 属性 | 类型 | 默认值 | 说明 |
|------|------|--------|------|
| theme | TDResultTheme | default | 主题样式 |
| title | String | - | 标题文本 |
| description | String | - | 描述文本 |

**示例**：
```dart
const TDResult(
  theme: TDResultTheme.success,
  title: '操作成功',
  description: '您的操作已完成',
)
```