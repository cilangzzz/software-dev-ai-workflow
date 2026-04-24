# TDesign Flutter 组件索引

本索引提供所有组件的快速查找，详细信息请查看对应分类文件。

---

## 组件分类索引

| 分类 | 文件路径 | 组件数 |
|------|----------|--------|
| 基础组件 | [components/basic.md](components/basic.md) | 6 |
| 表单组件 | [components/form.md](components/form.md) | 14 |
| 导航组件 | [components/navigation.md](components/navigation.md) | 7 |
| 反馈组件 | [components/feedback.md](components/feedback.md) | 8 |
| 展示组件 | [components/display.md](components/display.md) | 10 |
| 操作组件 | [components/operation.md](components/operation.md) | 6 |
| 其他组件 | [components/other.md](components/other.md) | 10 |

---

## 组件快速索引表

### 基础组件

| 组件 | 类名 | 功能 |
|------|------|------|
| 按钮 | TDButton | 按钮组件，支持多种样式、尺寸、主题 |
| 图标 | TDIcons | 图标库，2113个预定义图标 |
| 链接 | TDLink | 链接文本组件 |
| 分割线 | TDDivider | 分割线，支持水平/垂直、虚线 |
| 单元格 | TDCell | 列表项展示组件 |
| 文本 | TDText | 扩展文本组件，支持主题字体 |

### 表单组件

| 组件 | 类名 | 功能 |
|------|------|------|
| 输入框 | TDInput | 输入框，支持多种布局样式 |
| 多行文本框 | TDTextarea | 多行文本输入 |
| 复选框 | TDCheckbox | 复选框，支持分组 |
| 单选框 | TDRadio | 单选框，支持分组 |
| 开关 | TDSwitch | 开关组件 |
| 滑块 | TDSlider | 滑动选择器，支持范围选择 |
| 步进器 | TDStepper | 数值增减操作 |
| 评分 | TDRate | 评分组件，支持半选 |
| 表单 | TDForm | 表单组件，支持校验 |
| 上传 | TDUpload | 文件上传组件 |
| 选择器 | TDPicker | 多级选择器 |
| 日期选择器 | TDDatePicker | 日期时间选择 |
| 级联选择器 | TDCascader | 级联选择 |
| 搜索栏 | TDSearchBar | 搜索栏组件 |

### 导航组件

| 组件 | 类名 | 功能 |
|------|------|------|
| 导航栏 | TDNavBar | 页面顶部导航栏 |
| 标签栏 | TDTabBar | 标签页切换 |
| 底部标签栏 | TDBottomTabBar | 底部导航 |
| 侧边导航 | TDSideBar | 侧边栏导航 |
| 索引 | TDIndexes | 快速定位列表 |
| 抽屉 | TDDrawer | 抽屉弹出 |
| 页脚 | TDFooter | 页面底部 |

### 反馈组件

| 组件 | 类名 | 功能 |
|------|------|------|
| 对话框 | TDDialog | 弹窗，支持多种类型 |
| 轻提示 | TDToast | Toast提示 |
| 消息通知 | TDMessage | 消息通知栏 |
| 动作面板 | TDActionSheet | 底部弹出选项 |
| 弹出层 | TDPopup | 弹出层面板 |
| 加载 | TDLoading | 加载指示器 |
| 进度条 | TDProgress | 进度展示 |
| 结果页 | TDResult | 操作结果展示 |

### 展示组件

| 组件 | 类名 | 功能 |
|------|------|------|
| 头像 | TDAvatar | 头像展示 |
| 徽标 | TDBadge | 徽标/红点 |
| 标签 | TDTag | 展示标签 |
| 图片 | TDImage | 图片组件 |
| 图片预览 | TDImageViewer | 图片预览工具 |
| 空状态 | TDEmpty | 空数据展示 |
| 日历 | TDCalendar | 日历选择 |
| 轮播图 | TDSwiper | 轮播指示器 |
| 折叠面板 | TDCollapse | 折叠面板 |
| 骨架屏 | TDSkeleton | 加载占位 |

### 操作组件

| 组件 | 类名 | 功能 |
|------|------|------|
| 下拉菜单 | TDDropdownMenu | 下拉筛选 |
| 滑动单元格 | TDSwipeCell | 左滑操作 |
| 返回顶部 | TDBackTop | 返回顶部按钮 |
| 悬浮按钮 | TDFab | 悬浮操作按钮 |
| 下拉刷新 | TDRefreshHeader | 刷新头部 |

### 其他组件

| 组件 | 类名 | 功能 |
|------|------|------|
| 公告栏 | TDNoticeBar | 公告滚动 |
| 气泡弹出框 | TDPopover | 气泡提示 |
| 步骤条 | TDSteps | 步骤展示 |
| 表格 | TDTable | 数据表格 |
| 树形选择 | TDTreeSelect | 树形结构选择 |
| 计时器 | TDTimeCounter | 倒计时/正计时 |
| 主题 | TDTheme | 主题管理 |
| 弹出路由 | TDSlidePopupRoute | 滑动弹出路由 |

---

## 按场景查找

### 表单场景
- 输入：TDInput, TDTextarea, TDSearchBar
- 选择：TDCheckbox, TDRadio, TDSwitch, TDPicker, TDDatePicker, TDCascader, TDTreeSelect
- 数值：TDSlider, TDStepper, TDRate
- 校验：TDForm
- 上传：TDUpload

### 列表场景
- 展示：TDCell, TDTable
- 操作：TDSwipeCell, TDDropdownMenu
- 定位：TDIndexes, TDBackTop
- 刷新：TDRefreshHeader

### 反馈场景
- 提示：TDToast, TDMessage
- 弹窗：TDDialog, TDPopup, TDActionSheet, TDDrawer
- 加载：TDLoading, TDSkeleton
- 结果：TDResult, TDProgress

### 导航场景
- 顶部：TDNavBar
- 底部：TDBottomTabBar
- 侧边：TDSideBar
- 标签页：TDTabBar

---

## 总计：50+ 组件

详细API请查看 [api-reference.md](api-reference.md)