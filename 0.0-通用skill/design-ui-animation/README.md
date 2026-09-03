# UI动效设计技能包

本目录包含两个互补的动效设计技能，帮助实现高质量的网页UI动效。

## 技能概述

| 技能 | 用途 | 内容 |
|------|------|------|
| **motion-design-skill** | 设计理念 | 动效原则、时机缓动参考、常见模式 |
| **gsap-skills** | 实现方法 | GSAP API用法、代码示例、最佳实践 |

## 使用流程

```
需求 → motion-design-skill（设计决策）→ gsap-skills（代码实现）
```

### 步骤1：设计决策（阅读 motion-design-skill）

在实现动效前，先阅读 [motion-design-skill/skills/motion-design/SKILL.md](motion-design-skill/skills/motion-design/SKILL.md)，确定：

1. **情感目标** — 喜悦、平静、紧迫、优雅？
2. **动效人格** — Playful、Premium、Corporate、Energetic？
3. **时机参数** — 持续时间、缓动曲线、交错延迟
4. **运动属性** — 使用哪些CSS属性（优先transform和opacity）

**快速参考**：
- [时机缓动表](motion-design-skill/skills/motion-design/reference/timing-easing-tables.md) — 查找正确的持续时间
- [入场退场模式](motion-design-skill/skills/motion-design/patterns/entrance-exit.md) — 常见动画配方
- [状态反馈模式](motion-design-skill/skills/motion-design/patterns/state-feedback.md) — 按钮、加载、成功、错误

### 步骤2：代码实现（查阅 gsap-skills）

确定设计参数后，查阅 [gsap-skills](gsap-skills/skills/) 实现具体代码：

| 需求 | 查阅文档 |
|------|----------|
| 基础动画 | [gsap-core](gsap-skills/skills/gsap-core/SKILL.md) — `gsap.to()`, `from()`, 缓动 |
| 序列动画 | [gsap-timeline](gsap-skills/skills/gsap-timeline/SKILL.md) — 时间线编排 |
| 滚动动画 | [gsap-scrolltrigger](gsap-skills/skills/gsap-scrolltrigger/SKILL.md) — 滚动触发 |
| React项目 | [gsap-react](gsap-skills/skills/gsap-react/SKILL.md) — React集成 |
| 性能优化 | [gsap-performance](gsap-skills/skills/gsap-performance/SKILL.md) — 最佳实践 |

## 示例工作流

### 示例：卡片入场动画

**1. 设计决策（motion-design-skill）**
- 情感：优雅、专业
- 人格：Corporate
- 时机：250-350ms，ease-out
- 属性：translate + opacity

**2. 代码实现（gsap-skills）**
```javascript
gsap.from(".card", {
  y: 30,
  opacity: 0,
  duration: 0.3,
  ease: "power2.out",
  stagger: 0.05
});
```

### 示例：按钮按压反馈

**1. 设计决策（motion-design-skill）**
- 人格：Corporate
- 按压：scale 0.97，60ms
- 释放：scale 1.0，100ms

**2. 代码实现（gsap-skills）**
```javascript
// 按下
gsap.to(".btn", { scale: 0.97, duration: 0.06, ease: "out" });
// 释放
gsap.to(".btn", { scale: 1, duration: 0.1, ease: "out" });
```

### 示例：成功状态动画

**1. 设计决策（motion-design-skill）**
- 效果：弹跳、对勾绘制
- 时机：200ms + 150ms（延迟100ms）
- 缓动：ease-out-back

**2. 代码实现（gsap-skills）**
```javascript
const tl = gsap.timeline();
tl.to(".container", { scale: 1, duration: 0.2, ease: "back.out(1.7)" })
  .to(".checkmark", { strokeDashoffset: 0, duration: 0.15 }, "+=0.1");
```

## 核心原则速查

### motion-design-skill 关键规则

| 规则 | 说明 |
|------|------|
| 入场 > 退场 | 入场比退场长30-50% |
| 入场ease-out | 快开始，轻着陆 |
| 退场ease-in | 轻开始，快离开 |
| 1/3规则 | 距离不超过屏幕1/3，同时运动不超过元素总数1/3 |
| 只用transform/opacity | 避免动画布局属性 |

### gsap-skills 常用API

| API | 用途 |
|-----|------|
| `gsap.to()` | 动画到目标值 |
| `gsap.from()` | 从目标值动画 |
| `gsap.timeline()` | 创建时间线序列 |
| `stagger` | 交错动画 |
| `ScrollTrigger` | 滚动触发 |

## 文件结构

```
design-ui-animation/
├── README.md                    # 本说明文件
├── motion-design-skill/         # 设计理念
│   └── skills/motion-design/
│       ├── SKILL.md             # 主文件（必读）
│       ├── director/            # 设计哲学
│       ├── patterns/            # 常见模式
│       └── reference/           # 参考表
└── gsap-skills/                 # 实现方法
    ├── examples/                # 代码示例
    └── skills/
        ├── gsap-core/           # 核心API
        ├── gsap-timeline/       # 时间线
        ├── gsap-scrolltrigger/  # 滚动触发
        ├── gsap-react/          # React集成
        ├── gsap-plugins/        # 插件
        ├── gsap-utils/          # 工具函数
        └── gsap-performance/    # 性能优化
```

## 快速开始

1. **新手**：先读 motion-design-skill/SKILL.md [⚠️ link broken, ref needed] 了解设计理念
2. **实现**：查阅 [gsap-core/SKILL.md](gsap-skills/skills/gsap-core/SKILL.md) 学习基础API
3. **进阶**：使用 [gsap-timeline](gsap-skills/skills/gsap-timeline/SKILL.md) 编排复杂动画
4. **示例**：参考 [examples/](gsap-skills/examples/) 目录下的代码