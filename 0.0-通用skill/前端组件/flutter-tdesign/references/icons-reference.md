# TDesign Flutter 图标速查

常用图标快速参考，完整列表 2113 个。

---

## 常用图标

### 操作图标
```dart
Icon(TDIcons.add)           // 添加
Icon(TDIcons.close)         // 关闭
Icon(TDIcons.check)         // 勾选
Icon(TDIcons.edit)          // 编辑
Icon(TDIcons.delete)        // 删除
Icon(TDIcons.search)        // 搜索
Icon(TDIcons.refresh)       // 刷新
Icon(TDIcons.copy)          // 复制
```

### 状态图标
```dart
Icon(TDIcons.check_circle_filled)   // 成功
Icon(TDIcons.error_circle_filled)   // 错误
Icon(TDIcons.info_circle_filled)    // 信息
Icon(TDIcons.loading)               // 加载
```

### 导航图标
```dart
Icon(TDIcons.arrow_left)    // 左箭头
Icon(TDIcons.arrow_right)   // 右箭头
Icon(TDIcons.chevron_down)  // 下折叠
Icon(TDIcons.chevron_up)    // 上折叠
Icon(TDIcons.home_filled)   // 首页
Icon(TDIcons.backtop)       // 返回顶部
```

### 常用场景图标
```dart
Icon(TDIcons.user)          // 用户
Icon(TDIcons.message)       // 消息
Icon(TDIcons.notification)  // 通知
Icon(TDIcons.setting)       // 设置
Icon(TDIcons.time)          // 时间
Icon(TDIcons.calendar)      // 日历
Icon(TDIcons.location)      // 定位
Icon(TDIcons.call)          // 电话
Icon(TDIcons.mail)          // 邮件
Icon(TDIcons.image)         // 图片
Icon(TDIcons.file)          // 文件
Icon(TDIcons.folder)        // 文件夹
Icon(TDIcons.play)          // 播放
Icon(TDIcons.pause)         // 暂停
Icon(TDIcons.heart)         // 喜欢
Icon(TDIcons.star)          // 收藏
Icon(TDIcons.share)         // 分享
Icon(TDIcons.cart)          // 购物车
```

---

## 命名规则

| 后缀 | 说明 |
|------|------|
| `_filled` | 填充版本 |
| `_circle` | 圆形容器 |
| `_rectangle` | 矩形容器 |

---

## 使用方法

```dart
Icon(TDIcons.icon_name, size: 24, color: Colors.blue)
```