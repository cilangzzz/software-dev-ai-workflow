---
name: aliyun-qwen-image
description: 阿里云百炼Qwen-Image文生图API调用助手 - 用于通过阿里云百炼平台调用Qwen-Image系列模型生成高质量图像。支持同步和异步调用方式、提示词智能改写、多分辨率输出、反向提示词等高级功能。触发场景：(1) 用户需要生成图像 (2) 用户提到文生图、AI绘画 (3) 用户询问阿里云百炼图像生成 (4) 需要批量生成图片 (5) 需要定制化图像生成参数
---

# 阿里云百炼 Qwen-Image 文生图 Skill

## 基本信息

- **名称**: aliyun-qwen-image
- **版本**: 1.0.0
- **分类**: AI服务调用
- **优先级**: P1
- **创建日期**: 2026-05-11
- **更新日期**: 2026-05-11

## 功能描述

通过阿里云百炼平台调用Qwen-Image系列文生图模型，生成高质量图像。支持同步和异步两种调用方式，提供提示词智能改写、多分辨率输出、反向提示词过滤等高级功能。

## 触发条件

- **命令触发**: `/qwen-image`
- **关键词触发**:
  - "文生图"
  - "AI绘画"
  - "生成图片"
  - "图像生成"
  - "阿里云图像"
  - "百炼生图"
  - "qwen image"
  - "wanx"

## 支持的模型

### 图像生成模型 (IG)

| 模型名称 | 调用方式 | 特点 | 价格 | 推荐场景 |
|---------|---------|------|------|---------|
| `qwen-image-max` | 同步 | 最高质量版本 | - | 最高质量需求 |
| `qwen-image-2.0-pro` | 同步 | 满血版，最强文字渲染和真实质感 | 0.5元/张 | 高质量单图生成 (推荐) |
| `qwen-image-2.0` | 同步 | 加速版，效果与性能平衡 | 0.2元/张 | 快速图像生成 |
| `qwen-image-plus` | 异步 | Plus版本 | - | 批量生成 |
| `qwen-image` | 异步 | 基础版本 | - | 快速异步生成 |

### 图像编辑模型

| 模型名称 | 用途 |
|---------|------|
| `qwen-image-edit-plus` | 图像编辑 (Plus版本) |
| `qwen-image-edit` | 图像编辑 (基础版本) |

### 视频生成模型 (VG)

| 模型名称 | 特点 | 价格 |
|---------|------|------|
| `wan2.7-i2v` | 图生视频，演绎能力升级 | 1元/秒(1080P) |
| `wan2.7-t2v` | 文生视频 | - |
| `wan2.7-r2v` | 参考生视频，支持5个混合参考 | 1元/秒(1080P) |

> 详细模型列表见 [references/models.md](references/models.md)

## 输入参数

### 必选参数

| 参数名 | 类型 | 描述 | 示例值 |
|-------|------|------|-------|
| prompt | string | 正向提示词，描述期望的图像内容，支持中英文，不超过800字符 | "一只坐着的橘黄色的猫，表情愉悦，活泼可爱" |
| model | string | 模型名称 | qwen-image-2.0-pro |

### 可选参数

| 参数名 | 类型 | 默认值 | 描述 |
|-------|------|--------|------|
| negative_prompt | string | "" | 反向提示词，描述不希望出现的内容，不超过500字符 |
| size | string | 2048*2048 | 输出图像分辨率，格式为宽*高 |
| watermark | boolean | false | 是否添加"Qwen-Image"水印 |
| prompt_extend | boolean | true | 是否开启提示词智能改写 |
| seed | integer | 随机 | 随机数种子，范围[0,2147483647] |
| n | integer | 1 | 生成图像数量，当前固定为1 |

### 推荐分辨率

#### qwen-image-2.0系列 (512*512 ~ 2048*2048)

| 分辨率 | 宽高比 | 用途 |
|-------|-------|------|
| 2688*1536 | 16:9 | 横屏壁纸、视频封面 |
| 1536*2688 | 9:16 | 手机壁纸、短视频封面 |
| 2048*2048 | 1:1 | 社交媒体头像、商品图 |
| 2368*1728 | 4:3 | 传统显示器、PPT |
| 1728*2368 | 3:4 | 竖版展示 |

#### qwen-image-max/plus系列

| 分辨率 | 宽高比 |
|-------|-------|
| 1664*928 | 16:9 (默认) |
| 1472*1104 | 4:3 |
| 1328*1328 | 1:1 |
| 1104*1472 | 3:4 |
| 928*1664 | 9:16 |

## 执行流程

### 方式一：同步调用（qwen-image-2.0系列）

1. **准备参数** - 设置model、prompt、size等参数
2. **发送请求** - 调用同步API接口
3. **获取结果** - 直接返回生成的图像URL
4. **下载保存** - 图像URL有效期24小时，需及时保存

### 方式二：异步调用（qwen-image-plus/image系列）

1. **创建任务** - 发送请求获取task_id
2. **轮询查询** - 使用task_id查询任务状态
3. **等待完成** - 状态从PENDING→RUNNING→SUCCEEDED
4. **获取结果** - 任务成功后获取图像URL
5. **下载保存** - 及时保存图像

## API接口详情

### 同步接口

**请求地址**:
```
POST https://dashscope.aliyuncs.com/api/v1/services/aigc/multimodal-generation/generation
```

**请求头**:
```
Content-Type: application/json
Authorization: Bearer $DASHSCOPE_API_KEY
```

**请求体示例**:
```json
{
    "model": "qwen-image-2.0-pro",
    "input": {
        "messages": [
            {
                "role": "user",
                "content": [
                    {"text": "一只坐着的橘黄色的猫，表情愉悦，活泼可爱"}
                ]
            }
        ]
    },
    "parameters": {
        "negative_prompt": "低分辨率，低画质，肢体畸形，手指畸形",
        "prompt_extend": true,
        "watermark": false,
        "size": "2048*2048"
    }
}
```

### 异步接口

**创建任务地址**:
```
POST https://dashscope.aliyuncs.com/api/v1/services/aigc/text2image/image-synthesis
```

**请求头**:
```
Content-Type: application/json
Authorization: Bearer $DASHSCOPE_API_KEY
X-DashScope-Async: enable
```

**查询任务地址**:
```
GET https://dashscope.aliyuncs.com/api/v1/tasks/{task_id}
```

## 响应格式

### 成功响应

```json
{
    "output": {
        "choices": [
            {
                "finish_reason": "stop",
                "message": {
                    "role": "assistant",
                    "content": [
                        {"image": "https://dashscope-result.xxx.aliyuncs.com/xxx.png?Expires=xxx"}
                    ]
                }
            }
        ]
    },
    "usage": {
        "height": 2048,
        "image_count": 1,
        "width": 2048
    },
    "request_id": "d0250a3d-b07f-49e1-bdc8-xxx"
}
```

### 异步任务响应

```json
{
    "output": {
        "task_id": "0385dc79-5ff8-4d82-bcb6-xxx",
        "task_status": "PENDING"
    },
    "request_id": "4909100c-7b5a-9f92-xxx"
}
```

## 使用示例

### 示例1：基础图像生成

**输入**:
```
生成一张橘猫的图片，表情愉悦，可爱风格
```

**执行**:
```python
import dashscope
from dashscope import MultiModalConversation

response = MultiModalConversation.call(
    model="qwen-image-2.0-pro",
    messages=[{
        "role": "user",
        "content": [{"text": "一只坐着的橘黄色的猫，表情愉悦，活泼可爱，逼真准确"}]
    }],
    size="2048*2048"
)
```

**输出摘要**: 返回2048*2048分辨率PNG图像URL

### 示例2：高清壁纸生成

**输入**:
```
生成一张16:9的风景壁纸，冬日北京街景，中式建筑风格
```

**执行**:
```bash
curl --location 'https://dashscope.aliyuncs.com/api/v1/services/aigc/multimodal-generation/generation' \
--header 'Authorization: Bearer $DASHSCOPE_API_KEY' \
--data '{
    "model": "qwen-image-2.0-pro",
    "input": {
        "messages": [{"role": "user", "content": [{"text": "冬日北京的都市街景，中式建筑"}]}]
    },
    "parameters": {"size": "2688*1536"}
}'
```

### 示例3：异步批量生成

**输入**:
```
异步生成多张产品宣传图，需要高分辨率
```

**执行**:
1. 创建异步任务获取task_id
2. 轮询查询任务状态（建议间隔10秒）
3. 获取生成结果

## 质量标准

- **图像质量**: PNG格式，支持最高2048*2048分辨率
- **响应时效**: 同步接口秒级响应，异步接口需轮询等待
- **链接有效期**: 生成图像URL有效期24小时
- **提示词长度**: 正向不超过800字符，反向不超过500字符

## 依赖工具

- **DashScope SDK** - Python/Java官方SDK
- **curl** - HTTP命令行工具
- **Postman** - API调试工具

## 注意事项

1. **API Key配置**: 需配置环境变量`DASHSCOPE_API_KEY`或直接传入
2. **地域选择**: 北京和新加坡地域API Key不同，注意区分
3. **图像保存**: URL有效期24小时，务必及时下载保存
4. **异步轮询**: 建议间隔10秒查询，避免频繁请求
5. **RPS限制**: 异步查询接口默认RPS为20
6. **费用计量**: 按图像分辨率和数量计费，注意控制成本

## 错误处理

| 错误码 | 说明 | 解决方案 |
|-------|------|---------|
| InvalidApiKey | API Key无效 | 检查API Key配置 |
| InvalidParameter | 参数错误 | 检查参数格式和取值范围 |
| ModelNotFound | 模型不存在 | 使用支持的模型名称 |

## 快速参考

### 常用命令

| 命令 | 说明 |
|-----|------|
| `/qwen-image` | 快速生成图像 |
| `/qwen-image --async` | 异步生成图像 |
| `/qwen-image --size=2048*2048` | 指定分辨率 |

### 常用特性

| 特性 | 说明 |
|-----|------|
| prompt_extend | 提示词智能改写，优化生成效果 |
| negative_prompt | 反向提示词，排除不希望的内容 |
| seed | 固定种子值，保持生成结果相对稳定 |

## 相关文档

- [阿里云百炼文生图API官方文档](https://help.aliyun.com/zh/model-studio/qwen-image-api)
- [文生图Prompt指南](https://help.aliyun.com/zh/model-studio/text-to-image-prompt)
- [获取API Key](https://help.aliyun.com/zh/model-studio/get-api-key)
- [错误码参考](https://help.aliyun.com/zh/model-studio/error-code)

---
**技能版本**: 1.0.0
**最后更新**: 2026-05-11
**创建者**: AI Assistant