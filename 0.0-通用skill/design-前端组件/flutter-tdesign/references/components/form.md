# 表单组件

本分类包含 14 个表单组件。

---

## TDInput 输入框

**功能**：输入框组件，支持多种布局样式，卡片样式，清除按钮等。

**核心属性**：
| 属性 | 类型 | 默认值 | 说明 |
|------|------|--------|------|
| leftLabel | String | - | 输入框左侧文案 |
| hintText | String | - | 提示文案 |
| type | TDInputType | normal | 输入框类型 |
| size | TDInputSize | large | 输入框规格 |
| maxLength | int | 500 | 最大字数限制 |
| controller | TextEditingController | - | 文本控制器 |
| onChanged | Function | - | 输入回调 |
| needClear | bool | true | 是否需要清除按钮 |
| additionInfo | String | - | 错误提示信息 |

**示例**：
```dart
TDInput(
  leftLabel: '标签文字',
  controller: controller,
  hintText: '请输入文字',
  onChanged: (text) {},
  onClearTap: () => controller.clear(),
)

// 密码输入框
TDInput(
  leftLabel: '密码',
  hintText: '请输入密码',
  obscureText: true,
)
```

---

## TDTextarea 多行文本框

**功能**：多行文本输入组件，支持自动高度调整。

**核心属性**：
| 属性 | 类型 | 默认值 | 说明 |
|------|------|--------|------|
| label | String | - | 输入框标题 |
| hintText | String | - | 提示文案 |
| maxLength | int | - | 最大字数限制 |
| indicator | bool | false | 是否显示字数统计 |
| autosize | bool | false | 是否自动增高 |

**示例**：
```dart
TDTextarea(
  label: '备注',
  hintText: '请输入备注信息',
  maxLength: 200,
  indicator: true,
)
```

---

## TDCheckbox 复选框

**功能**：复选框组件，支持圆形/方形/勾选样式，支持卡片模式和分组。

**核心属性**：
| 属性 | 类型 | 默认值 | 说明 |
|------|------|--------|------|
| id | String | - | 标识 |
| title | String | - | 文本 |
| checked | bool | false | 选中状态 |
| enable | bool | true | 是否可用 |
| style | TDCheckboxStyle | - | 样式 |
| cardMode | bool | false | 卡片模式 |

**示例**：
```dart
TDCheckboxGroupContainer(
  selectIds: const ['1'],
  child: Column(
    children: [
      TDCheckbox(id: '1', title: '选项一'),
      TDCheckbox(id: '2', title: '选项二'),
    ],
  ),
)
```

---

## TDRadio 单选框

**功能**：单选框按钮，支持分组管理。

**核心属性**：
| 属性 | 类型 | 默认值 | 说明 |
|------|------|--------|------|
| id | String | - | 标识 |
| title | String | - | 文本 |
| radioStyle | TDRadioStyle | circle | 样式 |

**TDRadioGroup**：
| 属性 | 说明 |
|------|------|
| selectId | 选中的id |
| direction | 方向 |
| strictMode | 严格模式 |

**示例**：
```dart
TDRadioGroup(
  selectId: '1',
  direction: Axis.horizontal,
  directionalTdRadios: const [
    TDRadio(id: '1', title: '选项一'),
    TDRadio(id: '2', title: '选项二'),
  ],
)
```

---

## TDSwitch 开关

**功能**：开关组件，支持多种尺寸和样式。

**核心属性**：
| 属性 | 类型 | 默认值 | 说明 |
|------|------|--------|------|
| enable | bool | true | 是否可点击 |
| isOn | bool | false | 是否打开 |
| size | TDSwitchSize | medium | 尺寸 |
| type | TDSwitchType | fill | 类型 |
| onChanged | Function | - | 改变事件 |

**示例**：
```dart
const TDSwitch()
const TDSwitch(isOn: true, type: TDSwitchType.text)
```

---

## TDSlider 滑块

**功能**：滑动选择器，支持单选和范围选择。

**核心属性**：
| 属性 | 类型 | 默认值 | 说明 |
|------|------|--------|------|
| value | double/RangeValues | - | 默认值 |
| min | double | 0 | 最小值 |
| max | double | 100 | 最大值 |
| divisions | int | - | 分割数 |
| onChanged | Function | - | 滑动监听 |

**示例**：
```dart
TDSlider(
  value: 50,
  onChanged: (value) {},
)

// 范围滑块
TDRangeSlider(
  value: const RangeValues(10, 60),
  onChanged: (value) {},
)
```

---

## TDStepper 步进器

**功能**：步进器组件，用于数值增减操作。

**核心属性**：
| 属性 | 类型 | 默认值 | 说明 |
|------|------|--------|------|
| value | int | 0 | 值 |
| min | int | 0 | 最小值 |
| max | int | 100 | 最大值 |
| step | int | 1 | 步长 |
| theme | TDStepperTheme | normal | 风格 |
| onChange | Function | - | 数值变更回调 |

**示例**：
```dart
const TDStepper(
  theme: TDStepperTheme.filled,
  value: 1,
  min: 0,
  max: 10,
)
```

---

## TDRate 评分

**功能**：评分组件，支持半选、自定义图标和辅助文字。

**核心属性**：
| 属性 | 类型 | 默认值 | 说明 |
|------|------|--------|------|
| value | double | 0 | 评分值 |
| allowHalf | bool | false | 是否允许半选 |
| count | int | 5 | 评分数量 |
| disabled | bool | false | 是否禁用 |
| texts | List<String> | - | 评分等级辅助文字 |
| onChange | Function | - | 评分变更回调 |

**示例**：
```dart
const TDRate(value: 3)
const TDRate(value: 3.5, allowHalf: true)
```

---

## TDForm 表单

**功能**：表单组件，支持表单校验和提交。

**核心属性**：
| 属性 | 类型 | 默认值 | 说明 |
|------|------|--------|------|
| items | List<TDFormItem> | - | 表单内容 |
| rules | Map | - | 校验规则 |
| data | Map | - | 表单数据 |
| onSubmit | Function | - | 提交回调 |

**示例**：
```dart
TDForm(
  items: [
    TDFormItem(
      label: '用户名',
      name: 'username',
      child: TDInput(hintText: '请输入'),
    ),
  ],
  onSubmit: (data) {},
)
```

---

## TDUpload 上传

**功能**：上传组件，支持图片和视频上传。

**核心属性**：
| 属性 | 类型 | 默认值 | 说明 |
|------|------|--------|------|
| files | List | - | 文件列表 |
| max | int | 0 | 上传数量限制 |
| mediaType | List | - | 文件类型 |
| multiple | bool | false | 是否多选 |
| onChange | Function | - | 监听事件 |

**示例**：
```dart
TDUpload(
  max: 5,
  multiple: true,
  mediaType: [TDUploadMediaType.image],
)
```

---

## TDPicker 选择器

**功能**：多级选择器和多级联动选择器。

**静态方法**：
| 方法 | 说明 |
|------|------|
| showMultiPicker | 显示多级选择器 |
| showMultiLinkedPicker | 显示多级联动选择器 |

---

## TDDatePicker 日期选择器

**功能**：时间选择器，支持年月日时分秒配置。

**核心属性**：
| 属性 | 类型 | 默认值 | 说明 |
|------|------|--------|------|
| title | String | - | 选择器标题 |
| useYear/Month/Day | bool | true | 是否使用各时间单位 |
| onConfirm | Function | - | 确认回调 |

---

## TDCascader 级联选择器

**功能**：级联选择器组件。

**核心属性**：
| 属性 | 类型 | 默认值 | 说明 |
|------|------|--------|------|
| data | List<Map> | - | 数据源 |
| title | String | - | 选择器标题 |
| onChange | Function | - | 值变更回调 |

---

## TDSearchBar 搜索栏

**功能**：搜索栏组件，支持方形和圆角样式。

**核心属性**：
| 属性 | 类型 | 默认值 | 说明 |
|------|------|--------|------|
| placeHolder | String | - | 预设文案 |
| autoFocus | bool | false | 自动获取焦点 |
| needCancel | bool | false | 是否需要取消按钮 |
| onTextChanged | Function | - | 文字改变回调 |

**示例**：
```dart
TDSearchBar(
  placeHolder: '搜索预设文案',
  onTextChanged: (text) {},
)
```