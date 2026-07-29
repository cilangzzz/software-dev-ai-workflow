---
name: motion-design
description: >
  UI动效设计原则与最佳实践。提供时机、缓动、编排原则。
  适用于创建UI动画、过渡、微交互、加载状态、页面转场。
  与CSS、Framer Motion、GSAP、Lottie、Spring或任何动画系统兼容。
license: MIT
metadata:
  author: LottieFiles (adapted)
  version: "1.0.0"
---

# Motion Design Skill (UI动效设计)

## 何时使用

适用于：
- UI动画（按钮、卡片、模态框、页面转场）
- 微交互和反馈动画
- 加载、成功、错误状态
- 滚动触发动画
- 多元素序列编排

---

## 快速参考：8步检查清单

创建任何动画前：

1. **情感目标？** — 喜悦、平静、紧迫、优雅
2. **动效人格？** — Playful、Premium、Corporate、Energetic
3. **主要属性？** — 位置、缩放、透明度
4. **持续时间？** — 参见下方时间表
5. **缓动曲线？** — 入场=减速(ease-out)，退场=加速(ease-in)
6. **主角元素？** — 突出显示
7. **次要层？** — 阴影、子元素反应
8. **1/3规则？** — 距离不超过屏幕1/3，同时运动元素不超过总数1/3

---

## 动效人格（4选1）

| 原型 | 持续时间 | 缓动 | 过冲 | 适合场景 |
|------|----------|------|------|----------|
| **Playful** | 150-300ms | ease-out-back | 10-20% | 社交、创意工具 |
| **Premium** | 350-600ms | (0.4,0,0.2,1) | 0% | 奢侈、金融、高端 |
| **Corporate** | 200-400ms | (0.2,0,0,1) | 0-3% | B2B、仪表板 |
| **Energetic** | 100-250ms | ease-out-expo | 15-30% | 运动、娱乐 |

**默认**：UI用Corporate

---

## 持续时间表

| 元素类型 | 持续时间 |
|----------|----------|
| 工具提示 | 80-120ms |
| 按钮按压 | 120-180ms |
| 图标过渡 | 150-250ms |
| 卡片入场 | 200-350ms |
| 模态框 | 300-400ms |
| 页面转场 | 400-600ms |

**入场 > 退场**：入场比退场长30-50%

---

## 缓动选择

| 方向 | 缓动 | 原因 |
|------|------|------|
| 入场 | ease-out | 快开始，轻着陆 |
| 退场 | ease-in | 轻开始，快离开 |
| 屏幕上 | ease-in-out | 两端平滑 |
| 循环 | sine ease-in-out | 无缝 |

**行业标准缓动**：

| 名称 | Cubic Bezier | 用途 |
|------|-------------|------|
| Material Design 3 | (0.2, 0, 0, 1) | 默认 |
| MD3 强调 | (0.05, 0.7, 0.1, 1) | 入场 |
| Apple HIG | (0.25, 0.1, 0.25, 1) | iOS |
| Bounce settle | (0.175, 0.885, 0.32, 1.275) | 弹跳 |

---

## 属性选择

| 效果 | 主要属性 | 次要属性 |
|------|----------|----------|
| 入场/退场 | translate | opacity, scale |
| 强调 | scale | rotation（微妙） |
| 状态变化 | opacity, color | scale |
| 加载 | rotation | scale |
| 成功 | scale（弹出） | color |
| 错误 | translate（抖动） | color |

**只使用 transform 和 opacity** — 避免动画 width、height、margin、top、left

---

## 常见模式

### 按钮按压（Corporate）
```
按压：scale 0.97（60ms）
释放：scale 1.0（100ms）
总计：160ms
```

### 卡片入场（Premium）
```
从下方20px + opacity 0
平滑上滑 + 淡入（300ms, ease-out）
阴影后跟50ms
内容在落地后100ms淡入
```

### 成功状态
```
scale弹出带ease-out-back（200ms）
对勾绘制（150ms，50ms延迟）
颜色变绿（200ms）
总计：400ms
```

### 错误抖动
```
水平振荡 ±10-15px（300ms）
2-3次循环，ease-in-out
红色边框
无过冲
```

---

## 编排要点

**1/3规则**：
- 距离：运动不超过屏幕1/3无中间关键帧
- 元素：同时运动不超过总数1/3

**交错预算**：

| 模式 | 延迟 | 总预算 |
|------|------|--------|
| 微级联 | 20-40ms | <200ms |
| 标准 | 50-100ms | <400ms |
| 戏剧性 | 100-200ms | <600ms |

**关键**：总交错时间必须 <500ms

---

## 质量规则

### 绝不违反
1. 空间运动不用线性缓动
2. 重要状态不只透明度变化
3. 距离不超过屏幕1/3无中间关键帧

### 强烈遵循
1. 持续时间匹配元素类型
2. 入场ease-out，退场ease-in
3. 有主要+次要运动层

---

## 详细参考

- [timing-easing-tables.md](reference/timing-easing-tables.md) — 完整时机与缓动表
- [property-selection.md](reference/property-selection.md) — 属性选择指南
- [quality-checklist.md](reference/quality-checklist.md) — 质量检查清单
- [troubleshooting.md](reference/troubleshooting.md) — 故障排除

- [entrance-exit.md](patterns/entrance-exit.md) — 入场/退场模式
- [state-feedback.md](patterns/state-feedback.md) — 状态反馈模式
- [multi-element.md](patterns/multi-element.md) — 多元素编排

- [disney-principles.md](director/disney-principles.md) — 迪士尼原则UI适配
- [choreography.md](director/choreography.md) — 编排原则