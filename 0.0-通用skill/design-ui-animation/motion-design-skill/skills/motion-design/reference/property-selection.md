# Property Selection (属性选择)

## 属性概览

| 属性 | 性能 | 用途 | 单位 |
|------|------|------|------|
| transform | ⭐⭐⭐ 最佳 | 移动、缩放、旋转 | px, deg, 无单位 |
| opacity | ⭐⭐⭐ 最佳 | 淡入淡出 | 0-1 |
| color | ⭐⭐ 良好 | 颜色过渡 | hex, rgb, hsl |
| background-color | ⭐⭐ 良好 | 背景色变化 | hex, rgb, hsl |
| box-shadow | ⭐ 一般 | 阴影变化 | px, color |
| width/height | ❌ 避免 | 尺寸变化 | px, % |
| margin/padding | ❌ 避免 | 间距变化 | px, % |
| top/left/right/bottom | ❌ 避免 | 定位变化 | px, % |

---

## 效果目标到属性映射

| 效果目标 | 主要属性 | 次要属性 | 避免使用 |
|----------|----------|----------|----------|
| 入场/退场 | translate | opacity, scale | width, height |
| 强调/注意 | scale | rotation（微妙） | - |
| 状态变化 | opacity, color | scale（按压反馈） | - |
| 方向/流动 | translate | rotation（跟随路径） | top, left |
| 深度/3D感 | scale + shadow | translate（视差） | z-index动画 |
| 加载/进度 | rotation | scale, opacity | - |
| 成功 | scale（弹出） | color, rotation | - |
| 错误/警告 | translate（抖动） | color, rotation | - |
| 悬停 | scale, translate | color, shadow | - |
| 焦点 | scale, shadow | color | - |

---

## Transform属性详解

### translate（位移）

**推荐使用**：优于 top/left/right/bottom

```css
/* ✅ 推荐 */
transform: translateX(100px);
transform: translateY(50px);
transform: translate(100px, 50px);

/* ❌ 避免 */
left: 100px;
top: 50px;
```

**GSAP别名**：`x`, `y`, `xPercent`, `yPercent`

### scale（缩放）

**用途**：强调、按压反馈、入场效果

```css
transform: scale(1.1);      /* 均匀缩放 */
transform: scaleX(1.2);     /* 水平缩放 */
transform: scaleY(0.9);     /* 垂直缩放 */
transform: scale(1.1, 0.9); /* 挤压效果 */
```

**挤压与拉伸**：`scale(1.1, 0.9)` 创建挤压效果

### rotation（旋转）

**用途**：图标旋转、强调、趣味效果

```css
transform: rotate(45deg);   /* 2D旋转 */
transform: rotateX(45deg);  /* 3D X轴旋转 */
transform: rotateY(45deg);  /* 3D Y轴旋转 */
```

**方向后缀**（GSAP）：
- `_short`：最短路径
- `_cw`：顺时针
- `_ccw`：逆时针

---

## Opacity属性

### 最佳实践

```css
/* ✅ 推荐：配合visibility */
.fade-out {
  opacity: 0;
  visibility: hidden;
}

.fade-in {
  opacity: 1;
  visibility: visible;
}
```

### autoAlpha（GSAP）

GSAP的`autoAlpha`自动处理visibility：

```javascript
gsap.to(".element", { autoAlpha: 0 }); // opacity: 0 + visibility: hidden
gsap.to(".element", { autoAlpha: 1 }); // opacity: 1 + visibility: visible
```

---

## 组合属性策略

### 简洁阈值

| 属性数量 | 效果 |
|----------|------|
| 1个 | 直接、明确 |
| 2个 | 精致、专业 |
| 3个 | 可能过于复杂 |
| 4个+ | 通常过度 |

### 常见组合

| 组合 | 用途 |
|------|------|
| translate + opacity | 入场/退场 |
| scale + opacity | 弹入/弹出 |
| scale + rotation | 强调、趣味 |
| translate + scale + opacity | 复杂入场 |
| scale + shadow | 悬停卡片 |

---

## 颜色属性

### 推荐格式

```css
/* ✅ 推荐：HSL（更易动画） */
color: hsl(200, 100%, 50%);

/* ✅ 可用：RGB */
color: rgb(0, 128, 255);

/* ⚠️ 避免：hex（动画计算复杂） */
color: #007FFF;
```

### 颜色过渡时机

| 变化类型 | 推荐时机 |
|----------|----------|
| 色调变化 | 200-300ms |
| 亮度变化 | 150-250ms |
| 完全换色 | 200-400ms |

---

## Shadow属性

### 性能考虑

阴影动画性能开销较大，谨慎使用。

**优化策略**：
- 使用`filter: drop-shadow()`（仅对有形状的内容）
- 使用预定义的阴影类切换
- 使用opacity而非阴影值动画

### 悬停阴影

```css
/* 方案1：直接动画（性能开销大） */
.card:hover {
  box-shadow: 0 10px 30px rgba(0,0,0,0.2);
}

/* 方案2：伪元素（性能更好） */
.card::after {
  content: '';
  position: absolute;
  box-shadow: 0 10px 30px rgba(0,0,0,0.2);
  opacity: 0;
  transition: opacity 0.3s;
}

.card:hover::after {
  opacity: 1;
}
```

---

## 属性选择决策树

```
需要移动元素？
├── 是 → 使用 transform: translate
│   └── 需要弧线？ → 添加中间关键帧或使用motion path
└── 否
    ├── 需要缩放？ → 使用 transform: scale
    ├── 需要旋转？ → 使用 transform: rotate
    ├── 需要淡入淡出？ → 使用 opacity (+ visibility)
    ├── 需要换色？ → 使用 color / background-color
    └── 需要阴影变化？ → 使用伪元素或阴影opacity
```

---

## 禁止使用的属性

| 属性 | 问题 | 替代方案 |
|------|------|----------|
| width/height | 触发重排 | transform: scale |
| margin/padding | 触发重排 | transform: translate |
| top/left/right/bottom | 触发重排 | transform: translate |
| border-width | 触发重排 | transform: scale 或 clip-path |
| font-size | 触发重排 | transform: scale |