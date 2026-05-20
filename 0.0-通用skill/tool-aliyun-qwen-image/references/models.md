# 阿里云百炼图像与视频生成模型列表

## 图像生成模型 (IG)

### Qwen-Image 系列 - 推荐

| 模型ID | 名称 | 特点 | 价格 |
|-------|------|------|------|
| `qwen-image-max` | Qwen-Image-Max | 最高质量版本 | - |
| `qwen-image-2.0-pro` | Qwen-Image-2.0-Pro | 满血版，最强文字渲染和真实质感 | 0.5元/张 |
| `qwen-image-2.0` | Qwen-Image-2.0 | 加速版，效果与性能平衡 | 0.2元/张 |
| `qwen-image-2.0-pro-2026-04-22` | Qwen-Image-2.0-Pro快照 | 4月22日版本，画面质感升级 | - |
| `qwen-image-2.0-pro-2026-03-03` | Qwen-Image-2.0-Pro快照 | 3月3日版本 | - |
| `qwen-image-2.0-2026-03-03` | Qwen-Image-2.0快照 | 3月3日版本 | - |
| `qwen-image-plus` | Qwen-Image-Plus | Plus版本 | - |
| `qwen-image-plus-2026-01-09` | Qwen-Image-Plus快照 | 1月9日版本 | - |
| `qwen-image` | Qwen-Image | 基础版本 | - |

### Qwen-Image-Edit 系列 - 图像编辑

| 模型ID | 名称 | 特点 | 用途 |
|-------|------|------|------|
| `qwen-image-edit-plus` | Qwen-Image-Edit-Plus | Plus编辑版本 | 图像编辑 |
| `qwen-image-edit-plus-2025-12-15` | Qwen-Image-Edit-Plus快照 | 12月15日版本 | 图像编辑 |
| `qwen-image-edit` | Qwen-Image-Edit | 基础编辑版本 | 图像编辑 |

### 其他图像模型

| 模型ID | 名称 | 提供方 | 特点 |
|-------|------|--------|------|
| `qwen-mt-image` | Qwen-MT-Image | qwen-domain-model | 多模态图像 |
| `z-image-turbo` | Z-Image-Turbo | qwen-domain-model | 快速生成 |

---

## 视频生成模型 (VG)

### Wan 万相系列 - 推荐

| 模型ID | 名称 | 特点 | 价格 |
|-------|------|------|------|
| `wan2.7-r2v` | 万相2.7-参考生视频 | 稳定角色/道具/场景参考，支持5个混合参考 | 1元/秒(1080P) |
| `wan2.7-i2v` | 万相2.7-图生视频 | 演绎能力全面升级，情感细腻 | 1元/秒(1080P) |
| `wan2.7-t2v` | 万相2.7-文生视频 | 文生视频 | - |
| `wan2.7-videoedit` | 万相2.7-视频编辑 | 视频编辑 | - |
| `wan2.6-i2v` | Wan2.6-I2V | 图生视频 | - |
| `wan2.6-i2v-flash` | Wan2.6-I2V-Flash | 快速图生视频 | - |
| `wan2.6-t2v` | Wan2.6-T2V | 文生视频 | - |
| `wan2.5-i2v-preview` | Wan2.5-I2V-Preview | 预览版本 | - |
| `wan2.5-t2v-preview` | Wan2.5-T2V-Preview | 预览版本 | - |
| `wan2.2-i2v-plus` | Wan2.2-I2V-Plus | Plus版本 | - |

### HappyHorse 系列

| 模型ID | 名称 | 特点 |
|-------|------|------|
| `happyhorse-1.0-t2v` | HappyHorse-1.0-T2V | 文生视频 |
| `happyhorse-1.0-i2v` | HappyHorse-1.0-I2V | 图生视频 |
| `happyhorse-1.0-r2v` | HappyHorse-1.0-R2V | 参考生视频 |
| `happyhorse-1.0-video-edit` | HappyHorse-1.0-Video-Edit | 视频编辑 |

---

## 推荐使用

### 图像生成场景

| 场景 | 推荐模型 | 分辨率 |
|------|---------|--------|
| 高质量单图 | `qwen-image-2.0-pro` | 2048*2048 |
| 快速生成 | `qwen-image-2.0` | 2048*2048 |
| 最高质量 | `qwen-image-max` | - |
| 图像编辑 | `qwen-image-edit-plus` | - |

### 视频生成场景

| 场景 | 推荐模型 | 价格 |
|------|---------|------|
| 高质量视频 | `wan2.7-i2v` | 1元/秒(1080P) |
| 快速生成 | `wan2.6-i2v-flash` | - |
| 参考生视频 | `wan2.7-r2v` | 1元/秒(1080P) |

---

## 调用方式对比

| 模型系列 | 同步接口 | 异步接口 |
|---------|---------|---------|
| qwen-image-2.0系列 | ✓ 支持 | ✗ 不支持 |
| qwen-image-plus/image | ✗ 不支持 | ✓ 支持 |
| wan系列 | ✗ 不支持 | ✓ 支持 |

---

## 分辨率规格

### Qwen-Image-2.0系列 (512*512 ~ 2048*2048)

```
推荐分辨率:
- 2688*1536 (16:9) - 横屏壁纸
- 1536*2688 (9:16) - 手机壁纸
- 2048*2048 (1:1)  - 社交媒体 (默认)
- 2368*1728 (4:3)  - 传统显示器
- 1728*2368 (3:4)  - 竖版
```

### Qwen-Image-Plus/Max系列 (固定选项)

```
可选分辨率:
- 1664*928   (16:9) - 默认
- 1472*1104  (4:3)
- 1328*1328  (1:1)
- 1104*1472  (3:4)
- 928*1664   (9:16)
```

### Wan视频系列

```
视频分辨率:
- 720P  - 0.6元/秒
- 1080P - 1.0元/秒
```

---

## API接口地址

| 类型 | 接口地址 |
|------|---------|
| 图像同步 | `https://dashscope.aliyuncs.com/api/v1/services/aigc/multimodal-generation/generation` |
| 图像异步 | `https://dashscope.aliyuncs.com/api/v1/services/aigc/text2image/image-synthesis` |
| 视频异步 | `https://dashscope.aliyuncs.com/api/v1/services/aigc/text2video/video-synthesis` |
| 任务查询 | `https://dashscope.aliyuncs.com/api/v1/tasks/{task_id}` |

---

**文档更新**: 2026-05-11
**数据来源**: 阿里云百炼API模型列表