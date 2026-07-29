# 属性选择

## 性能对比

| 属性 | 性能 | 推荐 |
|------|------|------|
| transform | ⭐⭐⭐ | ✅ 优先 |
| opacity | ⭐⭐⭐ | ✅ 优先 |
| color | ⭐⭐ | ✅ 可用 |
| background-color | ⭐⭐ | ✅ 可用 |
| box-shadow | ⭐ | ⚠️ 谨慎 |
| width/height | ❌ | ❌ 避免 |
| margin/padding | ❌ | ❌ 避免 |
| top/left/right/bottom | ❌ | ❌ 避免 |

---

## 效果到属性映射

| 效果 | 主要属性 | 次要属性 |
|------|----------|----------|
| 入场/退场 | translate | opacity, scale |
| 强调 | scale | rotation（微妙） |
| 状态变化 | opacity, color | scale |
| 加载 | rotation | scale |
| 成功 | scale | color |
| 错误 | translate（抖动） | color |
| 悬停 | scale, translate | color, shadow |

---

## Transform属性

### translate
```css
/* ✅ 推荐 */
transform: translateX(100px);
transform: translateY(50px);

/* ❌ 避免 */
left: 100px;
top: 50px;
```

### scale
```css
transform: scale(1.1);      /* 均匀 */
transform: scale(1.1, 0.9); /* 挤压 */
```

### rotation
```css
transform: rotate(45deg);
transform: rotateX(45deg);  /* 3D */
```

---

## Opacity

配合visibility使用：

```css
.fade-out {
  opacity: 0;
  visibility: hidden;
}

.fade-in {
  opacity: 1;
  visibility: visible;
}
```

---

## 禁止使用

| 属性 | 问题 | 替代 |
|------|------|------|
| width/height | 重排 | scale |
| margin/padding | 重排 | translate |
| top/left | 重排 | translate |
| border-width | 重排 | scale或clip-path |