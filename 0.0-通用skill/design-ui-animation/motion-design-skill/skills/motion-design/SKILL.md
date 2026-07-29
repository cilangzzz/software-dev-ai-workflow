---
name: motion-design
description: >
  UI动效设计原则与最佳实践。提供时机、缓动、编排和迪士尼动画原则的UI适配。
  适用于创建动画、过渡、微交互、加载状态、页面转场、滚动触发效果或任何动效工作。
  与CSS、Framer Motion、GSAP、Lottie、Spring或任何动画系统兼容。
license: MIT
metadata:
  author: LottieFiles (adapted)
  version: "1.0.0"
---

# Motion Design Skill (UI动效设计)

## 何时使用此技能

适用于以下场景：
- 创建UI动画（按钮、卡片、模态框、页面转场）
- 设计微交互和反馈动画
- 构建加载、成功或错误状态
- 动画化插图或装饰元素
- 规划滚动触发或基于进度的动画
- 建立品牌动效识别
- 编排多元素序列

**决策树：**
1. 是否服务于功能目的（反馈、引导）？→ 使用响应性时机规则
2. 是否表达品牌个性？→ 参考动效人格原型
3. 是否讲述故事或引导注意力？→ 运用迪士尼原则 + 编排
4. 是否是复杂的多元素场景？→ 应用1/3规则 + 交错模式

---

## 快速参考：8步检查清单

创建任何动画前：

1. **情感目标？** — 喜悦、平静、紧迫、优雅
2. **动效人格？** — Playful（趣味）、Premium（高端）、Corporate（企业）、Energetic（活力）
3. **主要属性？** — 位置、缩放、旋转、透明度
4. **持续时间？** — 参见下方的持续时间表
5. **缓动曲线？** — 入场=减速，退场=加速
6. **主角元素？** — 应用分阶段原则
7. **次要+环境层？** — 增加丰富度
8. **1/3规则？** — 动效距离、同时运动元素数量

---

## 三大支柱（核心原则）

每个动画必须满足三个支柱才能进行技术决策：

| 支柱 | 问题 | 驱动因素 |
|------|------|----------|
| **情感意图** | 观众应该感受到什么？ | 缓动、时机、幅度 |
| **视觉叙事** | 微故事是什么？ | 铺垫 → 动作 → 结局 |
| **动效工艺** | 如何让它可信？ | 物理、次要运动、路径 |

**三个动效层**（扁平动画 = 缺失层次）：
- **主要层**：观众跟随的主要动作
- **次要层**：支撑丰富度（阴影、图标位移）
- **环境层**：背景生命力（渐变、微妙脉动）

> 深入了解：[director/core-philosophy.md](director/core-philosophy.md)

---

## 动效人格

每个项目选择一个原型。保持一致应用。

| 原型 | 持续时间 | 缓动 | 过冲 | 关键词 |
|------|----------|------|------|--------|
| **Playful（趣味）** | 150-300ms | ease-out-back | 10-20% | 有趣、异想天开、弹跳、可爱 |
| **Premium（高端）** | 350-600ms | cubic-bezier(0.4,0,0.2,1) | 0% | 优雅、极简、奢华、精致 |
| **Corporate（企业）** | 200-400ms | cubic-bezier(0.2,0,0,1) | 0-3% | 干净、专业、商务、仪表板 |
| **Energetic（活力）** | 100-250ms | ease-out-expo | 15-30% | 动态、充满活力、大胆、刺激 |

**默认值**：UI用Corporate，插图用Playful。

**品牌动效识别** — 定义三个常量：
1. **标志性缓动**：一个曲线用于80%的动画
2. **持续时间调色板**：3个持续时间（快速/标准/慢速）
3. **入场模式**：一个一致的入场风格

> 深入了解：[director/motion-personality.md](director/motion-personality.md)

---

## 属性选择

| 效果目标 | 主要属性 | 次要属性 |
|----------|----------|----------|
| 入场/退场 | position | opacity, scale |
| 强调/注意 | scale | rotation（微妙）, opacity pulse |
| 状态变化 | opacity, color | scale（按压反馈） |
| 方向/流动 | position | rotation（跟随路径） |
| 深度/3D感 | scale + shadow | position（视差） |
| 加载/进度 | rotation（旋转器） | scale, opacity pulse |
| 成功 | scale（弹出） | color, rotation（对勾绘制） |
| 错误/警告 | position（抖动） | color, rotation（摇晃） |

**简洁阈值**：使用最少的属性。一个=直接。两个=精致。三个+=可能过于繁杂。

> 深入了解：[reference/property-selection.md](reference/property-selection.md)

---

## 持续时间表

| 元素类型 | 持续时间 | 理由 |
|----------|----------|------|
| 工具提示/微反馈 | 80-120ms | 必须感觉即时 |
| 按钮按压/切换 | 120-180ms | 响应式反馈 |
| 图标过渡 | 150-250ms | 清晰的状态变化 |
| 卡片入场/退场 | 200-350ms | 空间感知 |
| 模态框/对话框 | 300-400ms | 焦点转移 |
| 页面转场 | 400-600ms | 上下文切换 |
| 戏剧性揭示 | 600-1200ms | 戏剧性铺垫 |

**距离影响持续时间**：100px = 基准。200px = 1.3倍。400px = 1.6倍。

**入场 > 退场**：入场比退场长30-50%。用户关心出现的内容。

**交互反馈**：
- 悬停：<100ms
- 按下：<150ms
- 释放/稳定：200-300ms
- 错误抖动：300-400ms（2-3次振荡）

> 深入了解：[reference/timing-easing-tables.md](reference/timing-easing-tables.md)

---

## 缓动选择

**方向规则**：
- **入场** → 减速（快开始，轻着陆）：ease-out系列
- **退场** → 加速（轻开始，快离开）：ease-in系列
- **屏幕上** → 两端平滑：ease-in-out系列
- **循环环境** → 无缝：基于sine的ease-in-out

**行业标准**：

| 标准 | Cubic Bezier | 用途 |
|------|-------------|------|
| Material Design 3 | (0.2, 0, 0, 1) | 默认屏幕上 |
| MD3 强调 | (0.05, 0.7, 0.1, 1) | 入场、注意 |
| MD3 加速 | (0.3, 0, 1, 1) | 退场、消失 |
| Apple HIG | (0.25, 0.1, 0.25, 1) | iOS标准 |
| Snappy UI | (0.2, 0, 0, 1) | 快速、果断 |
| Gentle float | (0.4, 0, 0.2, 1) | 环境、背景 |
| Bounce settle | (0.175, 0.885, 0.32, 1.275) | 过冲、趣味 |

**基于材质的缓动**：

| 材质 | 持续时间倍数 | 过冲 |
|------|-------------|------|
| 刚性（金属、石头） | 1.2x | 0% |
| 弹性（橡胶、凝胶） | 0.8x | 15-25% |
| 流体（水、颜料） | 1.5x | 5% |
| 纸张（卡片、纸张） | 1.0x | 3-5% |
| 气体（烟雾、雾） | 2.0x | 0% |
| 玻璃（易碎） | 0.9x | 0% |

> 深入了解：[reference/timing-easing-tables.md](reference/timing-easing-tables.md)

---

## 常见模式

### 按钮按压（Playful）
1. **预备**：缩放到0.97（50ms，ease-out）
2. **挤压**：缩放到[1.04, 0.96]（100ms，ease-in）
3. **跟随通过**：过冲到1.02，稳定到1.0（spring，200ms）
4. **次要**：阴影收缩，图标下移2px
5. **总计**：约150ms按压 + 200ms稳定

### 卡片入场（Premium）
1. **开始**：目标位置下方20px，透明度0
2. **路径**：轻微曲线（中点X偏移10px）
3. **缓动**：ease-out-cubic减速
4. **跟随通过**：阴影在卡片后50ms到达
5. **次要**：内容在卡片落地后100ms淡入
6. **分阶段**：其他卡片变暗至80%

### 成功状态（Playful）
1. **主要**：缩放弹出带ease-out-back
2. **次要**：对勾绘制
3. **环境**：微妙粒子爆发
4. **颜色**：绿色填充
5. **总计**：300-400ms

### 错误抖动（Corporate）
1. **主要**：位置振荡2-3次，水平方向±10-15px
2. **缓动**：ease-in-out实现尖锐停止
3. **颜色**：红色调
4. **总计**：300-400ms
5. **无过冲**：错误感觉坚定

> 更多模式：[patterns/entrance-exit.md](patterns/entrance-exit.md) | [patterns/state-feedback.md](patterns/state-feedback.md)

---

## 编排要点

**协调入场**：
- 主角先行 — 主要元素最先或最突出入场
- 空间一致性 — 所有元素从相同方向入场
- 反向运动 — 主角向右移动 → 环境以20-30%速度向左移动

**1/3规则（距离）**：没有动画在没有关键帧变化的情况下超过屏幕的1/3。

**1/3规则（元素）**：有3+元素时，同时运动的元素不超过1/3。

**交错预算**：

| 模式 | 延迟 | 总预算 | 用例 |
|------|------|--------|------|
| 微级联 | 20-40ms | <200ms | 列表项、网格单元格 |
| 标准 | 50-100ms | <400ms | 卡片、面板、导航 |
| 戏剧性 | 100-200ms | <600ms | 主角区块 |
| 波浪 | 30-60ms | <500ms | 数据可视化 |

**关键**：总交错时间必须保持在500ms以下。

> 深入了解：[director/choreography.md](director/choreography.md)

---

## 情感到动效映射

| 情感 | 特征 | 路径 | 缓动 | 持续时间 |
|------|------|------|------|----------|
| 喜悦 | 弹跳、弧线 | 曲线、向上 | ease-out-back | 200-400ms |
| 平静 | 平滑、流动 | 轻柔曲线 | sine ease-in-out | 500-1000ms |
| 紧迫 | 尖锐、快速 | 直线 | ease-out | 100-200ms |
| 悲伤 | 缓慢、向下 | 下垂曲线 | cubic ease-in-out | 600-1200ms |
| 惊讶 | 突然、扩展 | 径向向外 | ease-out-expo | 150-300ms |
| 优雅 | 缓慢、控制 | 长弧线 | (0.4,0,0.2,1) | 400-700ms |
| 趣味 | 弹跳、不规则 | 弧线、波浪 | ease-out-back | 200-350ms |

**路径即语言**：角度=紧张。曲线=友好。螺旋=异想天开。对角线=有目的。垂直=增长/重量。水平=进步。

> 深入了解：[director/emotion-mapping.md](director/emotion-mapping.md)

---

## 重量分类

| 重量 | 示例 | 持续时间 | 过冲 | 缓动 |
|------|------|----------|------|------|
| 重 | 模态框、覆盖层 | 300-500ms | 0% | 轻柔、高阻尼 |
| 中 | 卡片、面板 | 200-350ms | 3-5% | 适中 |
| 轻 | 工具提示、徽章、图标 | 80-200ms | 5-15% | 响应式 |

---

## 质量规则

### 关键 — 绝不违反
1. **绝不对空间运动使用线性** — 总是使用缓动曲线（线性仅用于旋转器、进度条）
2. **绝不对重要状态变化仅使用透明度** — 结合位置或缩放
3. **绝不超过1/3屏幕** 而没有中间关键帧
4. **总是三个动效层** — 主要 + 次要 + 环境

### 高优先级 — 强烈遵循
1. 根据元素类型匹配持续时间（见表格）
2. 使用方向缓动（ease-out入场，ease-in退场）
3. 应用迪士尼原则（特别是预备、跟随通过）
4. 在场景中保持一致的个性

> 完整检查清单：[reference/quality-checklist.md](reference/quality-checklist.md)

---

## 故障排除快速参考

| 问题 | 可能原因 | 修复 |
|------|----------|------|
| 看起来机械 | 线性缓动或无弧线 | 添加缓动曲线 + 弧线路径 |
| 感觉太慢 | 持续时间对于元素类型太长 | 检查持续时间表，使用ease-out |
| 感觉廉价/扁平 | 缺少次要 + 环境层 | 添加阴影运动 + 背景生命力 |
| 太分散注意力 | 太多元素在运动 | 应用1/3规则，减少幅度 |
| 没有个性 | 到处使用通用缓动 | 一致应用个性原型 |

> 深入了解：[reference/troubleshooting.md](reference/troubleshooting.md)

---

## 文件参考

**哲学**（director/）：
- [core-philosophy.md](director/core-philosophy.md) — 三大支柱深入
- [disney-principles.md](director/disney-principles.md) — 12原则，UI适配
- [motion-personality.md](director/motion-personality.md) — 4原型 + 品牌识别
- [emotion-mapping.md](director/emotion-mapping.md) — 情感 → 动效映射
- [choreography.md](director/choreography.md) — 多元素协调

**参考**（reference/）：
- [timing-easing-tables.md](reference/timing-easing-tables.md) — 持续时间 + 缓动查找
- [property-selection.md](reference/property-selection.md) — 属性通信指南
- [troubleshooting.md](reference/troubleshooting.md) — 动画问题 + 修复
- [quality-checklist.md](reference/quality-checklist.md) — 评估标准

**模式**（patterns/）：
- [entrance-exit.md](patterns/entrance-exit.md) — 入场/退场配方
- [state-feedback.md](patterns/state-feedback.md) — 成功、错误、加载、悬停
- [ambient-continuous.md](patterns/ambient-continuous.md) — 循环、呼吸、视差
- [multi-element.md](patterns/multi-element.md) — 交错 + 编排配方
