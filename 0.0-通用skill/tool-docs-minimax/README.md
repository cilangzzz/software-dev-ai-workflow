# MiniMax M3 原始文档

> 来源: https://platform.minimaxi.com/docs
> 整理时间: 2026-08-10

## 📁 文件说明

本目录包含从 MiniMax 官方文档手动爬取并转换的 Markdown 文件。

---

## 📚 文档列表

### 🎤 语音合成

| 文件 | 大小 | 说明 |
|------|------|------|
| [同步语音合成.md](同步语音合成.md) | 8.7 KB | 同步语音合成 API 详解，支持模型、语言列表、流式请求示例 |
| [异步语音合成.md](异步语音合成.md) | 9.2 KB | 异步长文本语音合成 API，4 步流程示例 |
| [音色快速复刻.md](音色快速复刻.md) | 7.5 KB | 通过参考音频快速克隆声音 |
| [系统音色列表.md](系统音色列表.md) | 19.0 KB | 全部 327 个系统预置音色 ID 及描述 |

### 🖼️ 图像生成

| 文件 | 大小 | 说明 |
|------|------|------|
| [图片生成.md](图片生成.md) | 3.3 KB | 文生图与图生图 API |

### 🎵 音乐生成

| 文件 | 大小 | 说明 |
|------|------|------|
| [音乐生成.md](音乐生成.md) | 9.2 KB | Music 3.0 音乐生成、翻唱、歌词生成 |

---

## 📖 合并文档

| 文件 | 大小 | 说明 |
|------|------|------|
| [MiniMax_M3_语音合成完整参考.md](MiniMax_M3_语音合成完整参考.md) | 22.0 KB | 语音合成完整参考（含代码示例） |
| [MiniMax_M3_完整参考.md](MiniMax_M3_完整参考.md) | 45.7 KB | 所有文档合并版 |

---

## 🔑 重要 API 端点

| 功能 | 端点 |
|------|------|
| 同步语音合成 | `wss://api.minimaxi.com/ws/v1/t2a_v2` |
| 异步语音合成 | `POST https://api.minimaxi.com/v1/t2a_v2_async` |
| 音色克隆 | `POST https://api.minimaxi.com/v1/voice_clone` |
| 图片生成 | `POST https://api.minimaxi.com/v1/image_generation` |
| 音乐生成 | `POST https://api.minimaxi.com/v1/music_generation` |
| 歌词生成 | `POST https://api.minimaxi.com/v1/lyrics_generation` |
| 翻唱前处理 | `POST https://api.minimaxi.com/v1/music_cover_preprocess` |

---

## 🚀 快速开始

### 环境变量设置

```bash
export MINIMAX_API_KEY="your_api_key_here"
```

### 安装依赖

```bash
pip install requests websockets
```

### 同步语音合成示例

```python
import asyncio
import websockets
import json
import os

async def synthesize_speech(text, voice_id="male-qn-qingse"):
    api_key = os.environ.get("MINIMAX_API_KEY")
    url = "wss://api.minimaxi.com/ws/v1/t2a_v2"
    
    # 建立连接
    ws = await websockets.connect(url, additional_headers={"Authorization": f"Bearer {api_key}"})
    
    # 发送配置
    await ws.send(json.dumps({
        "event": "task_start",
        "model": "speech-2.8-hd",
        "voice_setting": {"voice_id": voice_id, "speed": 1, "vol": 1, "pitch": 0},
        "audio_setting": {"sample_rate": 32000, "bitrate": 128000, "format": "mp3", "channel": 1}
    }))
    
    # 发送文本
    await ws.send(json.dumps({"event": "task_continue", "text": text}))
    
    # 结束任务
    await ws.send(json.dumps({"event": "task_finish"}))
    
    # 接收音频
    audio_data = bytearray()
    while True:
        msg = await ws.recv()
        data = json.loads(msg)
        if data.get("event") == "task_finished":
            break
        if "data" in data and "audio" in data["data"]:
            audio_data.extend(bytes.fromhex(data["data"]["audio"]))
    
    return bytes(audio_data)

# 使用
audio = asyncio.run(synthesize_speech("你好，欢迎使用MiniMax语音合成服务"))
with open("output.mp3", "wb") as f:
    f.write(audio)
```

---

## 📋 支持的语音模型

| 模型 | 特性 |
|------|------|
| speech-2.8-hd | 情绪渲染融合语气词，重塑自然听感 |
| speech-2.8-turbo | 极致生成速度，更自然逼真的音频效果 |
| speech-2.6-hd | 超低延时，归一化升级，更高自然度 |
| speech-2.6-turbo | 极速版，更快更优惠 |
| speech-02-hd | 出色的韵律、稳定性和复刻相似度 |
| speech-02-turbo | 小语种能力加强，性能表现出色 |

---

## 🌍 支持的语言

MiniMax 语音合成支持 **40 种语言**：

中文、粤语、英语、西班牙语、法语、俄语、德语、葡萄牙语、阿拉伯语、意大利语、日语、韩语、印尼语、越南语、土耳其语、荷兰语、乌克兰语、泰语、波兰语、罗马尼亚语、希腊语、捷克语、芬兰语、印地语、保加利亚语、丹麦语、希伯来语、马来语、波斯语、斯洛伐克语、瑞典语、克罗地亚语、菲律宾语、匈牙利语、挪威语、斯洛文尼亚语、加泰罗尼亚语、尼诺斯克语、泰米尔语、阿非利卡语

---

*文档整理完成 - 2026-08-10*
