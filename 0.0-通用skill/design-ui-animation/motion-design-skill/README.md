# Motion Design Skill (UI动效设计)

通用UI动效设计原则与最佳实践，适用于AI辅助动画设计。

## 概述

本技能提供了动效设计的核心原则、时机缓动参考、常见模式和故障排除指南。基于迪士尼12原则的UI适配，结合Material Design和Apple HIG的动效规范。

## 文件结构

```
motion-design-skill/
├── README.md                          # 本文件
└── skills/
    └── motion-design/
        ├── SKILL.md                    # 主技能文件（核心参考）
        ├── director/                   # 设计哲学与理论
        │   ├── core-philosophy.md      # 三大支柱深入
        │   ├── disney-principles.md    # 迪士尼12原则UI适配
        │   ├── motion-personality.md   # 4大原型与品牌识别
        │   ├── emotion-mapping.md      # 情感→动效映射
        │   └── choreography.md         # 多元素编排
        ├── patterns/                   # 实用模式
        │   ├── entrance-exit.md        # 入场/退场配方
        │   ├── state-feedback.md       # 状态反馈模式
        │   ├── ambient-continuous.md   # 环境与连续运动
        │   └── multi-element.md        # 多元素编排模式
        └── reference/                  # 参考表
            ├── timing-easing-tables.md # 时机与缓动表
            ├── property-selection.md   # 属性选择指南
            ├── quality-checklist.md    # 质量检查清单
            └── troubleshooting.md      # 故障排除
```

## 快速开始

### 8步检查清单

创建任何动画前，完成以下检查：

1. **情感目标？** — 喜悦、平静、紧迫、优雅
2. **动效人格？** — Playful、Premium、Corporate、Energetic
3. **主要属性？** — 位置、缩放、旋转、透明度
4. **持续时间？** — 根据元素类型查表
5. **缓动曲线？** — 入场=减速，退场=加速
6. **主角元素？** — 应用分阶段原则
7. **次要+环境层？** — 增加丰富度
8. **1/3规则？** — 动效距离、同时运动元素数量

### 动效人格选择

| 原型 | 适合场景 | 持续时间 | 缓动 | 过冲 |
|------|----------|----------|------|------|
| **Playful** | 儿童、游戏、社交 | 150-300ms | ease-out-back | 10-20% |
| **Premium** | 奢侈、金融、高端 | 350-600ms | (0.4,0,0.2,1) | 0% |
| **Corporate** | B2B、仪表板、企业 | 200-400ms | (0.2,0,0,1) | 0-3% |
| **Energetic** | 运动、音乐、年轻 | 100-250ms | ease-out-expo | 15-30% |

## 核心原则

### 三大支柱

1. **情感意图**：观众应该感受到什么？→ 驱动缓动、时机、幅度
2. **视觉叙事**：微故事是什么？→ 驱动分阶段、层次
3. **动效工艺**：如何可信？→ 驱动物理、次要运动

### 三个运动层

- **主要层**：观众跟随的主要动作
- **次要层**：阴影、图标、子元素反应
- **环境层**：背景渐变、装饰微动

### 1/3规则

- **距离**：运动不超过屏幕1/3无中间关键帧
- **元素**：同时运动元素不超过总数的1/3

## 与GSAP Skill配合使用

本动效设计skill与`gsap-skills`配合使用：

1. **motion-design-skill**：提供设计原则、时机参考、模式配方
2. **gsap-skills**：提供具体实现方法、API使用、代码示例

**使用流程**：
1. 使用motion-design-skill确定设计方向
2. 使用gsap-skills实现具体动画代码

## 来源

本技能基于以下资源改编：

- [LottieFiles/motion-design-skill](https://github.com/LottieFiles/motion-design-skill) — 通用动效设计原则
- Material Design Motion Guidelines
- Apple Human Interface Guidelines - Motion
- 迪士尼12动画原则

## 许可证

MIT