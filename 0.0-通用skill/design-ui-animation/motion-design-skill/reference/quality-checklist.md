# 质量检查清单

## 关键规则

- [ ] 空间运动不用线性缓动
- [ ] 重要状态不只透明度变化
- [ ] 距离不超过屏幕1/3无中间关键帧

## 高优先级

- [ ] 持续时间匹配元素类型
- [ ] 入场ease-out，退场ease-in
- [ ] 有主要+次要运动层

## 性能

- [ ] 只用transform和opacity
- [ ] 避免动画width、height、margin、top、left
- [ ] 同时运动 ≤ 1/3元素

## 可访问性

```css
@media (prefers-reduced-motion: reduce) {
  * {
    animation-duration: 0.01ms !important;
    transition-duration: 0.01ms !important;
  }
}
```

## 个性一致

| 个性 | 检查项 |
|------|--------|
| Playful | 有过冲、短时机 |
| Premium | 无过冲、长时机 |
| Corporate | 最小过冲、中等时机 |
| Energetic | 大过冲、最短时机 |

## 视觉质量

- [ ] 运动平滑无卡顿
- [ ] 缓动感觉自然
- [ ] 主角元素突出
- [ ] 状态变化清晰传达