# 阿里云百炼 Qwen-Image 文生图 API 参考手册

## API 接口概览

### 同步接口（qwen-image-2.0系列）

| 属性 | 值 |
|-----|-----|
| 接口地址 | POST https://dashscope.aliyuncs.com/api/v1/services/aigc/multimodal-generation/generation |
| 新加坡地址 | POST https://dashscope-intl.aliyuncs.com/api/v1/services/aigc/multimodal-generation/generation |
| 认证方式 | Bearer Token (DASHSCOPE_API_KEY) |
| Content-Type | application/json |

### 异步接口（qwen-image-plus/image/max系列）

| 属性 | 值 |
|-----|-----|
| 创建任务地址 | POST https://dashscope.aliyuncs.com/api/v1/services/aigc/text2image/image-synthesis |
| 查询任务地址 | GET https://dashscope.aliyuncs.com/api/v1/tasks/{task_id} |
| 必需请求头 | X-DashScope-Async: enable |

---

## 模型规格

### qwen-image-2.0-pro

| 属性 | 说明 |
|-----|-----|
| 调用方式 | 同步 |
| 最高分辨率 | 2048*2048 |
| 最低分辨率 | 512*512 |
| 输出格式 | PNG |
| 特点 | 高质量、高分辨率、快速响应 |
| 推荐用途 | 高质量单图生成、商业用途 |

### qwen-image-2.0

| 属性 | 说明 |
|-----|-----|
| 调用方式 | 同步 |
| 最高分辨率 | 2048*2048 |
| 特点 | 基础版本 |
| 推荐用途 | 快速图像生成、测试调试 |

### qwen-image-max

| 属性 | 说明 |
|-----|-----|
| 调用方式 | 异步 |
| 默认分辨率 | 1664*928 (16:9) |
| 特点 | 高质量、适合批量 |
| 推荐用途 | 批量生成、高质量需求 |

### qwen-image-plus

| 属性 | 说明 |
|-----|-----|
| 调用方式 | 异步 |
| 默认分辨率 | 1664*928 (16:9) |
| 特点 | 平衡性价比 |
| 推荐用途 | 一般用途 |

---

## 请求参数详解

### 同步接口请求体

```json
{
  "model": "qwen-image-2.0-pro",
  "input": {
    "messages": [
      {
        "role": "user",
        "content": [
          {
            "text": "提示词内容"
          }
        ]
      }
    ]
  },
  "parameters": {
    "negative_prompt": "反向提示词",
    "prompt_extend": true,
    "watermark": false,
    "size": "2048*2048",
    "seed": 12345
  }
}
```

### 异步接口请求体

```json
{
  "model": "qwen-image-plus",
  "input": {
    "prompt": "提示词内容",
    "negative_prompt": "反向提示词"
  },
  "parameters": {
    "size": "1664*928",
    "n": 1,
    "prompt_extend": true,
    "watermark": false,
    "seed": 12345
  }
}
```

---

## 参数规范

### prompt（正向提示词）

| 属性 | 值 |
|-----|-----|
| 类型 | string |
| 必选 | 是 |
| 最大长度 | 800字符（同步接口） |
| 语言支持 | 中英文 |
| 内容要求 | 描述期望的图像元素和视觉特点 |

**示例**:
```
一只坐着的橘黄色的猫，表情愉悦，活泼可爱，逼真准确。
冬日北京的都市街景，青灰瓦顶、朱红色外墙的中式商铺。
```

### negative_prompt（反向提示词）

| 属性 | 值 |
|-----|-----|
| 类型 | string |
| 必选 | 否 |
| 最大长度 | 500字符 |
| 用途 | 描述不希望出现的内容 |

**推荐反向提示词**:
```
低分辨率，低画质，肢体畸形，手指畸形，画面过饱和，
蜡像感，人脸无细节，过度光滑，画面具有AI感，
构图混乱，文字模糊，扭曲。
```

### size（输出分辨率）

**qwen-image-2.0系列**: 512*512 ~ 2048*2048

| 分辨率 | 比例 | 用途 |
|-------|-----|-----|
| 2688*1536 | 16:9 | 横屏壁纸 |
| 1536*2688 | 9:16 | 手机壁纸 |
| 2048*2048 | 1:1 | 方形图片（默认） |
| 2368*1728 | 4:3 | 传统比例 |
| 1728*2368 | 3:4 | 竖版 |

**qwen-image-max/plus系列**: 固定选项

| 分辨率 | 比例 |
|-------|-----|
| 1664*928 | 16:9（默认） |
| 1472*1104 | 4:3 |
| 1328*1328 | 1:1 |
| 1104*1472 | 3:4 |
| 928*1664 | 9:16 |

### prompt_extend（提示词智能改写）

| 属性 | 值 |
|-----|-----|
| 类型 | boolean |
| 默认值 | true |
| 用途 | 模型自动优化提示词 |

**改写示例**:
- 原始: "一只坐着的橘黄色的猫，表情愉悦"
- 实际: "一只坐着的橘黄色猫咪，毛发蓬松柔软，阳光透过窗户洒在它身上..."

### seed（随机种子）

| 属性 | 值 |
|-----|-----|
| 类型 | integer |
| 范围 | [0, 2147483647] |
| 用途 | 保持生成结果相对稳定 |

---

## 响应格式详解

### 同步成功响应

```json
{
  "output": {
    "choices": [
      {
        "finish_reason": "stop",
        "message": {
          "role": "assistant",
          "content": [
            {
              "image": "https://dashscope-result-sh.oss-cn-shanghai.aliyuncs.com/xxx.png?Expires=xxx"
            }
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

### 异步任务状态

| 状态 | 说明 |
|-----|-----|
| PENDING | 任务排队中 |
| RUNNING | 任务处理中 |
| SUCCEEDED | 任务执行成功 |
| FAILED | 任务执行失败 |
| CANCELED | 任务已取消 |
| UNKNOWN | 任务不存在 |

---

## SDK调用示例

### Python SDK

```python
import dashscope
from dashscope import MultiModalConversation
import os

# 配置API Key
api_key = os.getenv("DASHSCOPE_API_KEY")

# 同步调用
response = MultiModalConversation.call(
    api_key=api_key,
    model="qwen-image-2.0-pro",
    messages=[{
        "role": "user",
        "content": [{"text": "一只可爱的橘猫"}]
    }],
    size="2048*2048",
    watermark=False,
    prompt_extend=True
)

if response.status_code == 200:
    image_url = response.output.choices[0].message.content[0]["image"]
    print(f"图像URL: {image_url}")
```

### Java SDK

```java
import com.alibaba.dashscope.aigc.multimodalconversation.MultiModalConversation;
import com.alibaba.dashscope.aigc.multimodalconversation.MultiModalConversationParam;

MultiModalConversation conv = new MultiModalConversation();
MultiModalMessage userMessage = MultiModalMessage.builder()
    .role(Role.USER.getValue())
    .content(Arrays.asList(Collections.singletonMap("text", "一只可爱的橘猫")))
    .build();

Map<String, Object> parameters = new HashMap<>();
parameters.put("size", "2048*2048");
parameters.put("watermark", false);

MultiModalConversationParam param = MultiModalConversationParam.builder()
    .apiKey(System.getenv("DASHSCOPE_API_KEY"))
    .model("qwen-image-2.0-pro")
    .messages(Collections.singletonList(userMessage))
    .parameters(parameters)
    .build();

MultiModalConversationResult result = conv.call(param);
```

---

## 错误码参考

| 错误码 | 说明 | 解决方案 |
|-------|-----|---------|
| InvalidApiKey | API Key无效 | 检查API Key配置 |
| InvalidParameter | 参数格式错误 | 检查JSON格式 |
| ModelNotFound | 模型不存在 | 使用支持的模型名称 |
| ContentNotAllowed | 内容违规 | 调整提示词内容 |
| RateLimitExceeded | 请求频率超限 | 降低请求频率 |
| QuotaExceeded | 配额超限 | 检查账户余额 |

---

## 最佳实践

### 1. 提示词编写建议

- 使用具体描述而非抽象概念
- 包含风格、光照、构图等细节
- 利用prompt_extend自动优化
- 使用negative_prompt排除不希望的内容

### 2. 分辨率选择建议

- 社交媒体: 2048*2048 (1:1)
- 手机壁纸: 1536*2688 (9:16)
- 电脑壁纸: 2688*1536 (16:9)
- PPT配图: 2368*1728 (4:3)

### 3. 异步任务管理

- 轮询间隔建议10秒
- task_id有效期24小时
- 及时下载保存图像
- 使用回调通知代替轮询

---

## 参考资料

- 官方API文档: https://help.aliyun.com/zh/model-studio/qwen-image-api
- SDK安装指南: https://help.aliyun.com/zh/model-studio/install-sdk
- 错误码参考: https://help.aliyun.com/zh/model-studio/error-code
- Prompt指南: https://help.aliyun.com/zh/model-studio/text-to-image-prompt