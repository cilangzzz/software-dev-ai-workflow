# MiniMax M3 语音合成完整参考

> 来源: https://platform.minimaxi.com/docs
> 整理时间: 2026-08-10

---

## 目录

1. [同步语音合成](#1-同步语音合成)
2. [异步语音合成](#2-异步语音合成)
3. [音色快速复刻](#3-音色快速复刻)
4. [系统音色列表](#4-系统音色列表)
5. [图片生成](#5-图片生成)
6. [音乐生成](#6-音乐生成)

---

## 1. 同步语音合成

同步语音合成支持基于文本到语音的同步生成，单次可处理最长 **10,000 字符**的文本。

### 1.1 支持模型

| 模型 | 特性 |
|------|------|
| speech-2.8-hd | 情绪渲染融合语气词，重塑自然听感 |
| speech-2.8-turbo | 极致生成速度，更自然逼真的音频效果 |
| speech-2.6-hd | 超低延时，归一化升级，更高自然度 |
| speech-2.6-turbo | 极速版，更快更优惠，更适用于语音聊天和数字人场景 |
| speech-02-hd | 拥有出色的韵律、稳定性和复刻相似度，音质表现突出 |
| speech-02-turbo | 拥有出色的韵律和稳定性，小语种能力加强，性能表现出色 |

### 1.2 支持语言

MiniMax 的语音合成模型具备卓越的跨语言能力，全面支持 **40 种**全球广泛使用的语言。

| 序号 | 语言 | 序号 | 语言 | 序号 | 语言 |
|------|------|------|------|------|------|
| 1 | 中文（Chinese） | 15 | 土耳其语（Turkish） | 28 | 马来语（Malay） |
| 2 | 粤语（Cantonese） | 16 | 荷兰语（Dutch） | 29 | 波斯语（Persian） |
| 3 | 英语（English） | 17 | 乌克兰语（Ukrainian） | 30 | 斯洛伐克语（Slovak） |
| 4 | 西班牙语（Spanish） | 18 | 泰语（Thai） | 31 | 瑞典语（Swedish） |
| 5 | 法语（French） | 19 | 波兰语（Polish） | 32 | 克罗地亚语（Croatian） |
| 6 | 俄语（Russian） | 20 | 罗马尼亚语（Romanian） | 33 | 菲律宾语（Filipino） |
| 7 | 德语（German） | 21 | 希腊语（Greek） | 34 | 匈牙利语（Hungarian） |
| 8 | 葡萄牙语（Portuguese） | 22 | 捷克语（Czech） | 35 | 挪威语（Norwegian） |
| 9 | 阿拉伯语（Arabic） | 23 | 芬兰语（Finnish） | 36 | 斯洛文尼亚语（Slovenian） |
| 10 | 意大利语（Italian） | 24 | 印地语（Hindi） | 37 | 加泰罗尼亚语（Catalan） |
| 11 | 日语（Japanese） | 25 | 保加利亚语（Bulgarian） | 38 | 尼诺斯克语（Nynorsk） |
| 12 | 韩语（Korean） | 26 | 丹麦语（Danish） | 39 | 泰米尔语（Tamil） |
| 13 | 印尼语（Indonesian） | 27 | 希伯来语（Hebrew） | 40 | 阿非利卡语（Afrikaans） |
| 14 | 越南语（Vietnamese） | | | | |

### 1.3 流式请求示例

本指南指导流式播放返回的音频文件，并保存完整音频文件。

> ⚠️ 注意：为实时播放音频流，需要先安装 [mpv 播放器](https://mpv.io/)。并且，需要先将密钥信息写入环境变量 `MINIMAX_API_KEY`。

```python
import asyncio
import websockets
import json
import ssl
import subprocess
import os

model = "speech-2.8-hd"
file_format = "mp3"

class StreamAudioPlayer:
    def __init__(self):
        self.mpv_process = None

    def start_mpv(self):
        """Start MPV player process"""
        try:
            mpv_command = ["mpv", "--no-cache", "--no-terminal", "--", "fd://0"]
            self.mpv_process = subprocess.Popen(
                mpv_command,
                stdin=subprocess.PIPE,
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL,
            )
            print("MPV player started")
            return True
        except FileNotFoundError:
            print("Error: mpv not found. Please install mpv")
            return False
        except Exception as e:
            print(f"Failed to start mpv: {e}")
            return False

    def play_audio_chunk(self, hex_audio):
        """Play audio chunk"""
        try:
            if self.mpv_process and self.mpv_process.stdin:
                audio_bytes = bytes.fromhex(hex_audio)
                self.mpv_process.stdin.write(audio_bytes)
                self.mpv_process.stdin.flush()
                return True
        except Exception as e:
            print(f"Play failed: {e}")
            return False
        return False

    def stop(self):
        """Stop player"""
        if self.mpv_process:
            if self.mpv_process.stdin and not self.mpv_process.stdin.closed:
                self.mpv_process.stdin.close()
            try:
                self.mpv_process.wait(timeout=20)
            except subprocess.TimeoutExpired:
                self.mpv_process.terminate()

async def establish_connection(api_key):
    """Establish WebSocket connection"""
    url = "wss://api.minimaxi.com/ws/v1/t2a_v2"
    headers = {"Authorization": f"Bearer {api_key}"}
    ssl_context = ssl.create_default_context()
    ssl_context.check_hostname = False
    ssl_context.verify_mode = ssl.CERT_NONE

    try:
        ws = await websockets.connect(url, additional_headers=headers, ssl=ssl_context)
        connected = json.loads(await ws.recv())
        if connected.get("event") == "connected_success":
            print("Connection successful")
            return ws
        return None
    except Exception as e:
        print(f"Connection failed: {e}")
        return None

async def start_task(websocket):
    """Send task start request"""
    start_msg = {
        "event": "task_start",
        "model": model,
        "voice_setting": {
            "voice_id": "male-qn-qingse",
            "speed": 1,
            "vol": 1,
            "pitch": 0,
            "english_normalization": False
        },
        "audio_setting": {
            "sample_rate": 32000,
            "bitrate": 128000,
            "format": file_format,
            "channel": 1
        }
    }
    await websocket.send(json.dumps(start_msg))

async def send_text(websocket, text):
    """Send text to synthesize"""
    text_msg = {
        "event": "task_continue",
        "text": text
    }
    await websocket.send(json.dumps(text_msg))

async def end_task(websocket):
    """End the task"""
    end_msg = {"event": "task_finish"}
    await websocket.send(json.dumps(end_msg))

async def receive_audio(websocket, player):
    """Receive and play audio"""
    audio_buffer = bytearray()

    while True:
        try:
            msg = await asyncio.wait_for(websocket.recv(), timeout=30)
            data = json.loads(msg)

            if data.get("event") == "task_finished":
                print("Task finished")
                break
            elif data.get("event") == "task_failed":
                print(f"Task failed: {data}")
                break
            elif "data" in data and "audio" in data["data"]:
                hex_audio = data["data"]["audio"]
                if hex_audio:
                    audio_buffer.extend(bytes.fromhex(hex_audio))
                    player.play_audio_chunk(hex_audio)

        except asyncio.TimeoutError:
            print("Timeout")
            break
        except Exception as e:
            print(f"Error: {e}")
            break

    return bytes(audio_buffer)

async def main():
    api_key = os.environ.get("MINIMAX_API_KEY")
    if not api_key:
        print("Please set MINIMAX_API_KEY environment variable")
        return

    text = "你好，欢迎使用MiniMax语音合成服务。这是一个流式语音合成的示例。"

    player = StreamAudioPlayer()
    if not player.start_mpv():
        return

    ws = await establish_connection(api_key)
    if not ws:
        return

    try:
        await start_task(ws)
        await send_text(ws, text)
        await end_task(ws)
        audio_data = await receive_audio(ws, player)

        # Save audio file
        with open(f"output.{file_format}", "wb") as f:
            f.write(audio_data)
        print(f"Audio saved to output.{file_format}")

    finally:
        player.stop()
        await ws.close()

if __name__ == "__main__":
    asyncio.run(main())
```

---

## 2. 异步语音合成

异步语音合成支持长文本语音合成，适合处理超长文本场景。

### 2.1 主要特性

- 支持超长文本合成（无字符限制）
- 异步任务模式，支持轮询和回调
- 支持多种音频格式输出

### 2.2 请求示例

```python
import requests
import os
import time

api_key = os.environ.get("MINIMAX_API_KEY")
url = "https://api.minimaxi.com/v1/t2a_v2_async"

headers = {
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json"
}

payload = {
    "model": "speech-2.8-hd",
    "text": "这是一段很长的文本..." * 100,
    "voice_setting": {
        "voice_id": "male-qn-qingse",
        "speed": 1.0,
        "vol": 1.0,
        "pitch": 0
    },
    "audio_setting": {
        "sample_rate": 32000,
        "bitrate": 128000,
        "format": "mp3",
        "channel": 1
    }
}

# 创建任务
response = requests.post(url, headers=headers, json=payload)
task_id = response.json()["task_id"]
print(f"Task created: {task_id}")

# 轮询任务状态
while True:
    status_url = f"https://api.minimaxi.com/v1/t2a_v2_async/query?task_id={task_id}"
    status_response = requests.get(status_url, headers=headers)
    status = status_response.json()

    if status["status"] == "completed":
        print("Task completed!")
        # 下载音频文件
        audio_url = status["audio_url"]
        audio_response = requests.get(audio_url)
        with open("async_output.mp3", "wb") as f:
            f.write(audio_response.content)
        print("Audio saved to async_output.mp3")
        break
    elif status["status"] == "failed":
        print(f"Task failed: {status}")
        break

    time.sleep(2)
```

---

## 3. 音色快速复刻

音色快速复刻功能允许通过参考音频快速克隆声音。

### 3.1 主要特性

- 仅需 10-30 秒参考音频
- 支持多种语言
- 快速克隆，低延迟

### 3.2 请求示例

```python
import requests
import os

api_key = os.environ.get("MINIMAX_API_KEY")
url = "https://api.minimaxi.com/v1/voice_clone"

headers = {
    "Authorization": f"Bearer {api_key}"
}

# 上传参考音频
with open("reference_audio.mp3", "rb") as f:
    files = {"audio_file": f}
    data = {
        "voice_name": "my_custom_voice",
        "description": "Custom voice clone"
    }
    response = requests.post(url, headers=headers, files=files, data=data)

voice_id = response.json()["voice_id"]
print(f"Voice cloned successfully! Voice ID: {voice_id}")

# 使用克隆的音色进行语音合成
tts_url = "https://api.minimaxi.com/v1/t2a_v2"
tts_payload = {
    "model": "speech-2.8-hd",
    "text": "这是使用克隆音色生成的语音。",
    "voice_setting": {
        "voice_id": voice_id,
        "speed": 1.0,
        "vol": 1.0,
        "pitch": 0
    }
}

tts_response = requests.post(tts_url, headers=headers, json=tts_payload)
with open("cloned_voice_output.mp3", "wb") as f:
    f.write(tts_response.content)
print("Audio saved to cloned_voice_output.mp3")
```

---

## 4. 系统音色列表

MiniMax 提供丰富的系统音色，支持多种语言和风格。

### 4.1 中文音色

| 音色 ID | 名称 | 性别 | 风格描述 |
|---------|------|------|----------|
| male-qn-qingse | 青涩青年 | 男 | 年轻、清新 |
| male-qn-jingying | 精英青年 | 男 | 成熟、稳重 |
| male-qn-badao | 霸道青年 | 男 | 强势、有力 |
| female-shaonv | 活泼少女 | 女 | 年轻、活泼 |
| female-yujie | 御姐 | 女 | 成熟、优雅 |
| female-chengshu | 成熟女性 | 女 | 稳重、温柔 |

### 4.2 英文音色

| 音色 ID | 名称 | 性别 | 风格描述 |
|---------|------|------|----------|
| male-en-1 | English Male 1 | 男 | 标准美式英语 |
| male-en-2 | English Male 2 | 男 | 英式英语 |
| female-en-1 | English Female 1 | 女 | 标准美式英语 |
| female-en-2 | English Female 2 | 女 | 英式英语 |

### 4.3 多语言音色

| 音色 ID | 语言 | 性别 | 备注 |
|---------|------|------|------|
| male-ja-1 | 日语 | 男 | 标准日语 |
| female-ja-1 | 日语 | 女 | 标准日语 |
| male-ko-1 | 韩语 | 男 | 标准韩语 |
| female-ko-1 | 韩语 | 女 | 标准韩语 |

---

## 5. 图片生成

图片生成服务提供文生图（text-to-image）与图生图（image-to-image）两种核心功能。

### 5.1 根据文本生成图片

根据详尽的文本描述（prompt），直接生成与之匹配的图片。

```python
import base64
import requests
import os

url = "https://api.minimaxi.com/v1/image_generation"
api_key = os.environ.get("MINIMAX_API_KEY")
headers = {"Authorization": f"Bearer {api_key}"}

payload = {
    "model": "image-01",
    "prompt": "men Dressing in white t shirt, full-body stand front view image :25, outdoor, Venice beach sign, full-body image, Los Angeles, Fashion photography of 90s, documentary, Film grain, photorealistic",
    "aspect_ratio": "16:9",
    "response_format": "base64",
}

response = requests.post(url, headers=headers, json=payload)
response.raise_for_status()

images = response.json()["data"]["image_base64"]
for i in range(len(images)):
    with open(f"output-{i}.jpeg", "wb") as f:
        f.write(base64.b64decode(images[i]))
```

### 5.2 结合参考图生成图片

此功能允许提供一张包含清晰主体的参考图（支持网络图片链接），并结合 prompt 描述，生成一张保留了主体特征的新图片。

```python
import base64
import requests
import os

url = "https://api.minimaxi.com/v1/image_generation"
api_key = os.environ.get("MINIMAX_API_KEY")
headers = {"Authorization": f"Bearer {api_key}"}

payload = {
    "model": "image-01",
    "prompt": "女孩在图书馆的窗户前，看向远方",
    "aspect_ratio": "16:9",
    "subject_reference": [
        {
            "type": "character",
            "image_file": "https://example.com/reference.jpg"
        }
    ],
    "response_format": "base64",
}

response = requests.post(url, headers=headers, json=payload)
response.raise_for_status()

images = response.json()["data"]["image_base64"]
for i in range(len(images)):
    with open(f"output-{i}.jpeg", "wb") as f:
        f.write(base64.b64decode(images[i]))
```

---

## 6. 音乐生成

MiniMax 音乐生成 API 支持根据歌词和风格描述生成音乐。

### 6.1 Music 3.0 核心特性

- **更懂创作意图**：语义理解模型升级，减少"AI 味"偏移
- **音质全面跃升**：告别拥挤和浑浊，支持指定乐器与真实技法（滑音、连奏等），一键触达商业唱片级听感
- **人声合成更自然**：新一代人声引擎彻底消除高频"机器嘶嘶声"，可控制旋律、咬字、呼吸与多层和声，逼近真人录音室表现

### 6.2 音乐生成示例

下面以生成一首 1940 年代大乐队摇摆爵士风格的歌曲为例：

#### 步骤 1：调用歌词生成接口（可选）

只需告诉模型你想要什么主题，歌词生成接口就会自动为你写出包含段落结构的完整歌词。

```python
import requests
import os

api_key = os.environ.get("MINIMAX_API_KEY")
url = "https://api.minimaxi.com/v1/lyrics_generation"

payload = {
    "mode": "write_full_song",
    "prompt": "欢快的 1940 年代大乐队摇摆爵士（Big Band Swing），充满活力的铜管乐组吹奏着干脆的切分音，标志性的 Walking Bass 贝斯线与跃动的镲片构建极强的律动。中段有一段极具表现力且快速的次中音萨克斯即兴 Solo。"
}

headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {api_key}"
}

response = requests.post(url, json=payload, headers=headers)
print(response.text)
```

#### 步骤 2：调用音乐生成接口

```python
import requests
import json
import os

api_key = os.environ.get("MINIMAX_API_KEY")
url = "https://api.minimaxi.com/v1/music_generation"

headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {api_key}"
}

payload = {
    "model": "music-3.0",
    "prompt": "欢快的 1940 年代大乐队摇摆爵士（Big Band Swing），充满活力的铜管乐组吹奏着干脆的切分音，标志性的 Walking Bass 贝斯线与跃动的镲片构建极强的律动。中段有一段极具表现力且快速的次中音萨克斯即兴 Solo。",
    "lyrics": "[Intro]\n[verse]\n听，苔岩在回应空弦的尾音\n雾穿过年轮 将年轮浸润\n漫游的鹿 就忽然停步\n静默如一枚 湿润的菌\n\n[pre_chorus]\n把整座森林的寂静 弹成涟漪...\n\n[chorus]\n直到群青 被洗成更深的群青\n每一片清醒的叶子 都垂下脖颈\n承接碎银般的颤音\n垂落，垂落... 千万条弦在交织\n把天光纺成发亮丝线\n缝补雏鸟羽翼间 疏漏的蓝\n\n[verse]\n泥壤下的根须 开始游移\n蘑菇们撑开 潮润的伞顶\n偷运星光的蚯蚓 暂停书写\n在休止符里 蜷成初生的形\n\n[chorus]\n直到群青 被洗成更深的群青\n每一片清醒的叶子 都垂下脖颈\n承接碎银般的颤音\n\n[bridge]\n当最后一道滑音 漫过树梢\n年轮深处 传来菌丝合唱\n每滴雨都成了 回授的弦\n把未完成的 交给苔衣去延长\n\n[outro]\n而寂静 比雨声更为丰盈\n竖琴把自身 长成梧桐木的年轮\n每圈涟漪 都在收拢时\n藏好一枚欲坠的月亮",
    "audio_setting": {
        "sample_rate": 44100,
        "bitrate": 256000,
        "format": "mp3"
    },
    "output_format": "url"
}

response = requests.post(url, headers=headers, json=payload)
result = response.json()
print(json.dumps(result, ensure_ascii=False, indent=2))
```

### 6.3 翻唱生成

Music Cover 可以基于已有歌曲生成不同风格的翻唱版本。支持两种模式：

- **一步翻唱**：直接传入参考音频，系统自动通过 ASR 提取歌词
- **两步翻唱**：先对音频进行前处理，提取并修改歌词后再生成翻唱

#### 一步翻唱（快捷模式）

```python
import requests
import json
import os

api_key = os.environ.get("MINIMAX_API_KEY")
url = "https://api.minimaxi.com/v1/music_generation"

headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {api_key}"
}

payload = {
    "model": "music-cover",
    "audio_url": "https://example.com/reference_song.mp3",
    "prompt": "爵士风格，慵懒深夜酒吧，萨克斯",
    "audio_setting": {
        "sample_rate": 44100,
        "bitrate": 256000,
        "format": "mp3"
    },
    "output_format": "url"
}

response = requests.post(url, headers=headers, json=payload)
result = response.json()
print(json.dumps(result, ensure_ascii=False, indent=2))
```

#### 两步翻唱（进阶模式 — 支持歌词修改）

如需修改歌词，可使用两步流程：先调用前处理接口提取音频特征和歌词，修改歌词后再生成翻唱。

**步骤 1：预处理参考音频**

调用翻唱前处理接口，获取：
- `cover_feature_id`：音频特征唯一标识（有效期 24 小时）
- `formatted_lyrics`：带段落标签的结构化歌词，可自由编辑
- `structure_result`：JSON 字符串，包含段落类型和时间戳
- `audio_duration`：参考音频时长（秒）

```python
import requests
import json
import os

api_key = os.environ.get("MINIMAX_API_KEY")
url = "https://api.minimaxi.com/v1/music_cover_preprocess"

headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {api_key}"
}

payload = {
    "model": "music-cover",
    "audio_url": "https://example.com/reference_song.mp3"
}

response = requests.post(url, headers=headers, json=payload)
result = response.json()

# 保存 cover_feature_id 并查看提取的歌词
cover_feature_id = result["cover_feature_id"]
formatted_lyrics = result["formatted_lyrics"]
print(f"特征 ID: {cover_feature_id}")
print(f"提取的歌词:\n{formatted_lyrics}")
```

**步骤 2：修改歌词并生成翻唱**

```python
import requests
import json
import os

api_key = os.environ.get("MINIMAX_API_KEY")
url = "https://api.minimaxi.com/v1/music_generation"

headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {api_key}"
}

# 使用上一步返回的 cover_feature_id
# 根据需要修改提取的歌词
modified_lyrics = "[Verse 1]\n这里是修改后的第一段歌词\n用新的文字讲述你的故事\n\n[Chorus]\n全新的副歌部分\n用不同的感觉演唱"

payload = {
    "model": "music-cover",
    "cover_feature_id": cover_feature_id,
    "lyrics": modified_lyrics,
    "prompt": "爵士风格，慵懒深夜酒吧，萨克斯",
    "audio_setting": {
        "sample_rate": 44100,
        "bitrate": 256000,
        "format": "mp3"
    },
    "output_format": "url"
}

response = requests.post(url, headers=headers, json=payload)
result = response.json()
print(json.dumps(result, ensure_ascii=False, indent=2))
```

> ⚠️ 注意：使用 `cover_feature_id` 时，不要传入 `audio_url` 或 `audio_base64`（三者互斥）。`lyrics` 参数为必填（10–1000 字符）。

---

## 附录：API 端点参考

| 功能 | HTTP 方法 | 端点 |
|------|-----------|------|
| 同步语音合成 | WebSocket | `wss://api.minimaxi.com/ws/v1/t2a_v2` |
| 异步语音合成 | POST | `https://api.minimaxi.com/v1/t2a_v2_async` |
| 异步任务查询 | GET | `https://api.minimaxi.com/v1/t2a_v2_async/query?task_id={task_id}` |
| 音色克隆 | POST | `https://api.minimaxi.com/v1/voice_clone` |
| 图片生成 | POST | `https://api.minimaxi.com/v1/image_generation` |
| 音乐生成 | POST | `https://api.minimaxi.com/v1/music_generation` |
| 歌词生成 | POST | `https://api.minimaxi.com/v1/lyrics_generation` |
| 翻唱前处理 | POST | `https://api.minimaxi.com/v1/music_cover_preprocess` |

## 相关链接

- [MiniMax 开放平台](https://platform.minimaxi.com)
- [API 文档](https://platform.minimaxi.com/docs/api-reference/api-overview)
- [定价说明](https://platform.minimaxi.com/docs/pricing/overview)
- [更新日志](https://platform.minimaxi.com/docs/release-notes/models)

---

*文档整理完成 - 2026-08-10*
