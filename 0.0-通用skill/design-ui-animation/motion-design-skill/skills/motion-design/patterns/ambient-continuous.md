# Ambient & Continuous Motion (环境与连续运动)

## 特征

环境运动是连续的、微妙的、循环的。它为界面提供生命力和深度，而不分散用户对主要内容的注意力。

**关键原则**：
- 幅度小（视觉变化的5-15%）
- 持续时间慢（2-5秒循环）
- 不打扰用户焦点
- 自动运行，不需要用户触发

---

## 呼吸效果 (Breathing)

**描述**：元素微妙地扩展和收缩，模拟呼吸。

**参数**：
| 参数 | 值 |
|------|-----|
| 缩放范围 | 100% ↔ 102-105% |
| 持续时间 | 2-4秒/周期 |
| 缓动 | sine ease-in-out |
| 用途 | 图标、徽章、指示器 |

**实现**：
```css
@keyframes breathe {
  0%, 100% { transform: scale(1); }
  50% { transform: scale(1.03); }
}

.element {
  animation: breathe 3s ease-in-out infinite;
}
```

---

## 浮动效果 (Floating)

**描述**：元素轻微上下移动，模拟漂浮。

**参数**：
| 参数 | 值 |
|------|-----|
| 位移范围 | ±5-15px |
| 持续时间 | 3-6秒/周期 |
| 缓动 | sine ease-in-out |
| 用途 | 装饰元素、插图、吉祥物 |

**实现**：
```css
@keyframes float {
  0%, 100% { transform: translateY(0); }
  50% { transform: translateY(-10px); }
}

.element {
  animation: float 4s ease-in-out infinite;
}
```

---

## 脉动效果 (Pulsing)

**描述**：元素透明度或大小周期性变化，吸引注意。

**参数**：
| 参数 | 值 |
|------|-----|
| 透明度范围 | 50% ↔ 100% 或 缩放95%↔105% |
| 持续时间 | 1.5-3秒/周期 |
| 缓动 | sine ease-in-out |
| 用途 | 通知徽章、在线指示器、状态点 |

**实现**：
```css
@keyframes pulse {
  0%, 100% { opacity: 1; transform: scale(1); }
  50% { opacity: 0.6; transform: scale(0.95); }
}

.element {
  animation: pulse 2s ease-in-out infinite;
}
```

---

## 视差效果 (Parallax)

**描述**：不同层以不同速度响应滚动或鼠标移动。

**参数**：
| 层级 | 移动速度 |
|------|----------|
| 前景 | 1.2-1.5x 滚动速度 |
| 主内容 | 1.0x（正常） |
| 背景 | 0.3-0.7x 滚动速度 |

**用例**：
- 英雄区域背景
- 产品展示页
- 滚动驱动的叙事

**注意**：
- 移动端谨慎使用（性能）
- 提供 prefers-reduced-motion 回退

---

## 光泽扫过 (Shimmer)

**描述**：光泽效果从元素上扫过，暗示活动或价值。

**参数**：
| 参数 | 值 |
|------|-----|
| 扫过时间 | 1.5-3秒 |
| 间隔 | 2-5秒（可选） |
| 方向 | 左到右（默认） |
| 用途 | 骨架屏、加载状态、高端效果 |

**实现**：
```css
@keyframes shimmer {
  0% { background-position: -200% 0; }
  100% { background-position: 200% 0; }
}

.element {
  background: linear-gradient(
    90deg,
    rgba(255,255,255,0) 0%,
    rgba(255,255,255,0.3) 50%,
    rgba(255,255,255,0) 100%
  );
  background-size: 200% 100%;
  animation: shimmer 2s ease-in-out infinite;
}
```

---

## 粒子系统 (Particles)

**描述**：小元素在区域内漂浮、旋转或流动。

**参数**：
| 参数 | 值 |
|------|-----|
| 粒子数量 | 10-50个 |
| 粒子大小 | 2-10px |
| 运动类型 | 随机漂浮、定向流动 |
| 持续时间 | 5-15秒循环 |
| 用途 | 装饰背景、庆祝效果、魔法效果 |

---

## 渐变动画 (Gradient Animation)

**描述**：背景渐变颜色或位置变化。

**参数**：
| 参数 | 值 |
|------|-----|
| 变化速度 | 3-10秒/周期 |
| 颜色变化 | 色相偏移或位置变化 |
| 用途 | 背景、英雄区域、卡片 |

**实现**：
```css
@keyframes gradient-shift {
  0%, 100% { background-position: 0% 50%; }
  50% { background-position: 100% 50%; }
}

.element {
  background: linear-gradient(270deg, #ff6b6b, #4ecdc4, #45b7d1);
  background-size: 200% 200%;
  animation: gradient-shift 5s ease infinite;
}
```

---

## 性能考虑

| 技术 | 性能影响 | 建议 |
|------|----------|------|
| transform | 低 | ✅ 优先使用 |
| opacity | 低 | ✅ 优先使用 |
| background-position | 中 | ⚠️ 适量使用 |
| filter/blur | 高 | ⚠️ 谨慎使用 |
| box-shadow动画 | 高 | ❌ 避免 |

---

## 可访问性

**必须**：提供 `prefers-reduced-motion` 回退。

```css
@media (prefers-reduced-motion: reduce) {
  .element {
    animation: none;
  }
}
```

**策略**：
- 完全停止环境动画
- 或减少到最小必要运动
- 或用静态状态替代