# MiniMax M3 完整参考文档

> 来源: https://platform.minimaxi.com/docs
> 整理时间: 2026-08-10

---

## 目录

### 语音合成
- [同步语音合成](#同步语音合成)
- [异步语音合成](#异步语音合成)
- [音色快速复刻](#音色快速复刻)
- [系统音色列表](#系统音色列表)

### 图像生成
- [图片生成](#图片生成)

### 音乐生成
- [音乐生成](#音乐生成)

---

# 语音合成

## 同步语音合成

同步语音合成支持基于文本到语音的同步生成，单次可处理最长 10,000 字符的文本。

### 支持模型

](
- [

### 支持语言

MiniMax 的语音合成模型具备卓越的跨语言能力，全面支持 40 种全球广泛使用的语言。

](
- [

### 流式请求示例

](
- [推荐阅读](
语音
# 同步语音合成
同步语音合成支持基于文本到语音的同步生成，单次可处理最长 10,000 字符的文本。
## 
[​
支持模型
以下为 MiniMax 提供的语音模型及其特性说明。
| 模型 | 特性 
| speech-2.8-hd | 情绪渲染融合语气词，重塑自然听感 
| speech-2.8-turbo | 极致生成速度，更自然逼真的音频效果 
| speech-2.6-hd | 超低延时，归一化升级，更高自然度 
| speech-2.6-turbo | 极速版，更快更优惠，更适用于语音聊天和数字人场景 
| speech-02-hd | 拥有出色的韵律、稳定性和复刻相似度，音质表现突出 
| speech-02-turbo | 拥有出色的韵律和稳定性，小语种能力加强，性能表现出色 
## 
[​
支持语言
MiniMax 的语音合成模型具备卓越的跨语言能力，全面支持 40 种全球广泛使用的语言。我们致力于打破语言壁垒，构建真正意义上的全球通用人工智能模型。
目前支持的语言包含：
| 支持语种 | | 
| 1. 中文（Chinese） | 15. 土耳其语（Turkish） | 28. 马来语（Malay） 
| 2. 粤语（Cantonese） | 16. 荷兰语（Dutch） | 29. 波斯语（Persian） 
| 3. 英语（） | 17. 乌克兰语（Ukrainian） | 30. 斯洛伐克语（Slovak） 
| 4. 西班牙语（Spanish） | 18. 泰语（Thai） | 31. 瑞典语（Swedish） 
| 5. 法语（French） | 19. 波兰语（Polish） | 32. 克罗地亚语（Croatian） 
| 6. 俄语（Russian） | 20. 罗马尼亚语（Romanian） | 33. 菲律宾语（Filipino） 
| 7. 德语（German） | 21. 希腊语（Greek） | 34. 匈牙利语（Hungarian） 
| 8. 葡萄牙语（Portuguese） | 22. 捷克语（Czech） | 35. 挪威语（Norwegian） 
| 9. 阿拉伯语（Arabic） | 23. 芬兰语（Finnish） | 36. 斯洛文尼亚语（Slovenian） 
| 10. 意大利语（Italian） | 24. 印地语（Hindi） | 37. 加泰罗尼亚语（Catalan） 
| 11. 日语（Japanese） | 25. 保加利亚语（Bulgarian） | 38. 尼诺斯克语（Nynorsk） 
| 12. 韩语（Korean） | 26. 丹麦语（Danish） | 39. 泰米尔语（Tamil） 
| 13. 印尼语（Indonesian） | 27. 希伯来语（Hebrew） | 40. 阿非利卡语（Afrikaans） 
| 14. 越南语（Vietnamese） | | 
## 
[​

本指南指导，流式播放返回的音频文件，并保存完整音频文件。
⚠️ 注意，为实时播放音频流，需要先安装 [mpv 播放器](
请求示例
```
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
mpv_command = ["mpv", "--no-cache", "--no-terminal", "--", "
self.mpv_process = subprocess.Popen(
mpv_command,
stdin=subprocess.PIPE,
stdout=subprocess.DEVNULL,
stderr=subprocess.DEVNULL,
print("MPV player started")
return True
except FileNotFoundError:
print("E
return False
except Exception as e:
print(f"Failed to start 
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
print(f"Play 
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
url = "
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
print(f"Connection 
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
"_normalization": False
},
"audio_setting": {
"sample_rate": 32000,
"bitrate": 128000,
"format": file_format,
"channel": 1
await websocket.send(json.dumps(start_msg))
response = json.loads(await websocket.recv())
return response.get("event") == "task_started"
async def continue_task_with_stream_play(websocket, text, player):
"""Send continue request and stream play audio"""
await websocket.send(json.dumps({
"event": "task_continue",
"text": text
}))
chunk_counter = 1
total_audio_size = 0
audio_data = b""
while True:
try:
response = json.loads(await websocket.recv())
if "data" in response and "audio" in response["data"]:
audio = response["data"]["audio"]
if audio:
print(f"Playing chunk #{chunk_counter}")
audio_bytes = bytes.fromhex(audio)
if player.play_audio_chunk(audio):
total_audio_size += len(audio_bytes)
audio_data += audio_bytes
chunk_counter += 1
if response.get("is_final"):
print(f"Audio synthesis 
if player.mpv_process and player.mpv_process.stdin:
player.mpv_process.stdin.close()
# Save audio to file
with open(f"output.{file_format}", "wb") as f:
f.write(audio_data)
print(f"Audio saved as output.{file_format}")
estimated_duration = total_audio_size * 0.0625 / 1000
wait_time = max(estimated_duration + 5, 10)
return wait_time
except Exception as e:
print(f"E
break
return 10
async def close_connection(websocket):
"""Close connection"""
if websocket:
try:
await websocket.send(json.dumps({"event": "task_finish"}))
await websocket.close()
except Exception:
pass
async def main():
API_KEY = os.getenv("MINIMAX_API_KEY")
TEXT = "真正的危险不是计算机开始像人一样思考(sighs)，而是人开始像计算机一样思考。计算机只是可以帮我们处理一些简单事务。"
player = StreamAudioPlayer()
try:
if not player.start_mpv():
return
ws = await establish_connection(API_KEY)
if not ws:
return
if not await start_task(ws):
print("Task startup failed")
return
wait_time = await continue_task_with_stream_play(ws, TEXT, player)
await asyncio.sleep(wait_time)
except Exception as e:
print(f"E
finally:
player.stop()
if 'ws' in locals():
await close_connection(ws)
if __name__ == "__main__":
asyncio.run(main())
```
## 
[​
推荐阅读
## 同步语音合成 WebSocket
使用 API 接口，在WebSocket网络通信协议下进行同步语音合成。
点击查看
## 同步语音合成 HTTP
使用 API 接口，在HTTP网络通信协议下进行同步语音合成。
点击查看
## 产品定价
各模型的定价说明、计费方式及使用限制。
点击查看
## 速率限制
为保证资源的高效使用，引入速率限制，以确保服务的可用性、稳定性。
点击查看
此页面对您有帮助吗？
是否
音色快速复刻
异步语音合成
Ctrl+I

---

## 异步语音合成

异步语音合成支持长文本语音合成，适合处理超长文本场景。

MiniMax 提供 API，适用于长文本的音频合成任务，单个文件长度限制小于 10 万字符。
- 支持 100+系统音色、复刻音色自主选择
- 支持语调、语速、音量、比特率、采样率、输出格式调整
- 支持音频时长、音频大小等返回参数
- 支持时间戳（字幕）返回，精确到句
- 支持直接传入字符串与上传文本文件两种方式进行待合成文本的输入
- 支持非法字符检测：非法字符不超过 10%（包含 10%），音频会正常生成并返回非法字符占比；非法字符超过 10%，接口不返回结果（返回报错码），请检测后再次进行请求【非法字符定义：ascii 码中的控制符（不含制表符 `\t` 和换行符 `\n`）】
## 
[​
支持模型
以下为 MiniMax 已提供的语音模型及其特性说明。
| 模型 | 特性 
| speech-2.8-hd | 情绪渲染融合语气词，重塑自然听感 
| speech-2.8-turbo | 极致生成速度，更自然逼真的音频效果 
| speech-2.6-hd | 超低延时，归一化升级，更高自然度 
| speech-2.6-turbo | 极速版，更快更优惠，更适用于语音聊天和数字人场景 
| speech-02-hd | 拥有出色的韵律、稳定性和复刻相似度，音质表现突出 
| speech-02-turbo | 拥有出色的韵律和稳定性，小语种能力加强，性能表现出色 
## 
[​
支持语言
MiniMax 的语音合成模型具备卓越的跨语言能力，全面支持 40 种全球广泛使用的语言。我们致力于打破语言壁垒，构建真正意义上的全球通用人工智能模型。
目前支持的语言包含：
| 支持语种 | | 
| 1. 中文（Chinese） | 15. 土耳其语（Turkish） | 28. 马来语（Malay） 
| 2. 粤语（Cantonese） | 16. 荷兰语（Dutch） | 29. 波斯语（Persian） 
| 3. 英语（） | 17. 乌克兰语（Ukrainian） | 30. 斯洛伐克语（Slovak） 
| 4. 西班牙语（Spanish） | 18. 泰语（Thai） | 31. 瑞典语（Swedish） 
| 5. 法语（French） | 19. 波兰语（Polish） | 32. 克罗地亚语（Croatian） 
| 6. 俄语（Russian） | 20. 罗马尼亚语（Romanian） | 33. 菲律宾语（Filipino） 
| 7. 德语（German） | 21. 希腊语（Greek） | 34. 匈牙利语（Hungarian） 
| 8. 葡萄牙语（Portuguese） | 22. 捷克语（Czech） | 35. 挪威语（Norwegian） 
| 9. 阿拉伯语（Arabic） | 23. 芬兰语（Finnish） | 36. 斯洛文尼亚语（Slovenian） 
| 10. 意大利语（Italian） | 24. 印地语（Hindi） | 37. 加泰罗尼亚语（Catalan） 
| 11. 日语（Japanese） | 25. 保加利亚语（Bulgarian） | 38. 尼诺斯克语（Nynorsk） 
| 12. 韩语（Korean） | 26. 丹麦语（Danish） | 39. 泰米尔语（Tamil） 
| 13. 印尼语（Indonesian） | 27. 希伯来语（Hebrew） | 40. 阿非利卡语（Afrikaans） 
| 14. 越南语（Vietnamese） | | 
## 
[​
使用流程
- 若使用文件输入，需先调用 [文件上传 API](
- 调用[创建语音生成任务 API](
- 调用[查询语音生成任务状态 API](
- 当任务完成时，上述调用查询语音生成任务状态 API 返回的 `file_id` 可用于调用 [文件下载 API](
注意：返回的下载 URL 自生成起 9 小时（32400 秒）内有效，过期后文件将失效，生成的信息便会丢失，请注意下载信息的时间，及时下载
## 
[​
过程示例
### 
[​
1. 获取 file_id
Python
```
"""
本示例用于待合成文本的 file_id。注意：需要先将密钥信息写入环境变量 `MINIMAX_API_KEY`。
"""
import requests
import os
api_key = os.environ.get("MINIMAX_API_KEY")
url = "
payload = {'purpose': 't2a_async_input'}
files=[
('file',('input_files.zip',open('path/to/input_files.zip','rb'),'application/zip'))
headers = {
'authority': 'api.minimaxi.com',
'Authorization': f'Bearer {api_key}'
response = requests.request("POST", url, headers=headers, data=payload, files=files)
print(response.text)
```
```
curl --location '
--header '
--header "A
--form 'purpose=t2a_async_input' \
--form 'file=@test-json.zip'
```
### 
[​
2. 创建语音合成任务
Python
```
"""
本示例用于创建语音合成任务，若使用文件作为输入，则需要将<text_file_id>替换为文本文件的file_id，若使用文本作为输入，则设置"text"字段。注意：需要先将密钥信息写入环境变量 `MINIMAX_API_KEY`。
"""
import requests
import json
import os
api_key = os.environ.get("MINIMAX_API_KEY")
url = "
payload = json.dumps({
"model": "speech-2.8-hd",
"text_file_id": <text_file_id>, # file as input
# "text":"微风拂过柔软的草地，清新的芳香伴随着鸟儿的歌唱。", # text as input
"language_boost": "auto",
"voice_setting": {
"voice_id": "audiobook_male_1",
"speed": 1,
"vol": 10,
"pitch": 1
},
"pronunciation_dict": {
"tone": [
"草地/(cao3)(di1)"
},
"audio_setting": {
"audio_sample_rate": 32000,
"bitrate": 128000,
"format": "mp3",
"channel": 2
},
"voice_modify":{
"pitch":0,
"intensity":0,
"timbre":0,
"sound_effects":"spacious_echo"
})
headers = {
'Authorization': f'Bearer {api_key}',
'Content-Type': 'application/json'
response = requests.request("POST", url, headers=headers, data=payload)
print(response.text)
```
```
# 若使用文件作为输入，则需要将<text_file_id>替换为文本文件的file_id，若使用文本作为输入，则设置"text"字段。注意：需要先将密钥信息写入环境变量 `MINIMAX_API_KEY`。
curl --location '
--header "
--header 'Content-T
--data '{
"model": "speech-8-hd",
"text_file_id": <Your file_id>, # file as input
# "text":"微风拂过柔软的草地，清新的芳香伴随着鸟儿的歌唱。", # text as input
"language_boost": "auto",
"voice_setting": {
"voice_id": "audiobook_male_1",
"speed": 1,
"vol": 10,
"pitch": 1
},
"pronunciation_dict": {
"tone": [
"草地/(cao3)(di1)"
},
"audio_setting": {
"audio_sample_rate": 32000,
"bitrate": 128000,
"format": "mp3",
"channel": 2
},
"voice_modify":{
"pitch":0,
"intensity":0,
"timbre":0,
"sound_effects":"spacious_echo"
}'
```
### 
[​
3. 查询语音合成进度
Python
```
"""
本示例用于查询语音合成进度。注意：需要先将密钥信息写入环境变量 `MINIMAX_API_KEY`，并将需要查询任务的 id 写入环境变量 `TASK_ID`。
"""
import requests
import json
import os
task_id = os.environ.get("TASK_ID")
api_key = os.environ.get("MINIMAX_API_KEY")
url = f"
payload = {}
headers = {
'Authorization': f'Bearer {api_key}',
'content-type': 'application/json',
response = requests.request("GET", url, headers=headers, data=payload)
print(response.text)
```
```
curl --location "
--header "
--header '
```
### 
[​
4. 下载语音合成文件
Python
```
"""
本示例用于下载语音合成文件。注意：需要先将密钥信息写入环境变量 `MINIMAX_API_KEY`，并将待下载文件的 id 写入环境变量 `FILE_ID`。
"""
import requests
import os
api_key = os.environ.get("MINIMAX_API_KEY")
file_id = os.environ.get("FILE_ID")
url = f"
payload = {}
headers = {
'content-type': 'application/json',
'Authorization': f'Bearer {api_key}'
response = requests.request("GET", url, headers=headers, data=payload)
with open(<output_filename>, 'wb') as f:
f.write(response.content)
```
```
curl --location "
--header 'Content-T
--header "A
--output "${FILE_NAME}"
```
## 
[​

---

## 音色快速复刻

音色快速复刻功能允许通过参考音频快速克隆声音。

MiniMax 语音模型提供良好的音色复刻能力，使用您的语料进行音色复刻，得到试听音频与 Voice ID（供后续正式语音合成使用）。
## 
[​
使用流程
快速复刻功能实现具体操作流程如下：
- **上传待克隆音频** 调用 [上传复刻音频](
- 支持上传的文件需遵从以下规范： 上传的音频文件格式需为：mp3、m4a、wav 格式； 上传的音频文件的时长最少应不低于 10 秒，最长应不超过 5 分钟； 上传的音频文件大小需不超过 20mb。
- **上传示例音频 (可选)** 若需要提供示例音频以增强克隆效果，需要调用 [上传示例音频](
- 支持上传的文件需遵从以下规范： 上传的音频文件格式需为：mp3、m4a、wav 格式； 上传的音频文件的时长小于 8s； 上传的音频文件大小需不超过 20mb。
- **调用复刻接口** 基于获取的 `file_id` 和自定义的 `voice_id` 作为输入参数，调用 [快速复刻接口](
- **使用克隆音色** 使用复刻生成的 `voice_id`，根据实际需求调用语音生成接口，例如：
[同步语音合成](
- [异步长文本语音合成](
## 
[​
过程示例
### 
[​
1. 上传复刻音频
```
"""
本示例用于获取复刻音频的 file_id。
注意：需要先将密钥信息写入环境变量 `MINIMAX_API_KEY`。
"""
import requests
import os
api_key = os.getenv("MINIMAX_API_KEY")
url = "
payload = {"purpose": "voice_clone"}
files = [
("file", ("clone_input.mp3", open("/path/to/clone_input.mp3", "rb")))
headers = {
"Authorization": f"Bearer {api_key}"
response = requests.post(url, headers=headers, data=payload, files=files)
response.raise_for_status()
file_id = response.json().get("file", {}).get("file_id")
print(file_id)
```
```
curl --location '
--header 'A
--form 'purpose="voice_clone"' \
--form 'file=@"/path/to/clone_input.mp3"'
```
### 
[​
2. 上传参考音频
```
"""
本示例用于获取示例音频的 file_id。
注意：需要先将密钥信息写入环境变量 `MINIMAX_API_KEY`。
"""
import requests
import os
api_key = os.getenv("MINIMAX_API_KEY")
url = "
payload = {"purpose": "prompt_audio"}
files = [
("file", ("clone_prompt.mp3", open("/path/to/clone_prompt.mp3", "rb")))
headers = {
"Authorization": f"Bearer {api_key}"
response = requests.post(url, headers=headers, data=payload, files=files)
response.raise_for_status()
prompt_file_id = response.json().get("file", {}).get("file_id")
print(prompt_file_id)
```
```
curl --location '
--header 'A
--form 'purpose="prompt_audio"' \
--form 'file=@"/path/to/clone_prompt.mp3"'
```
### 
[​
3. 进行音色克隆
```
"""
本示例用于音色克隆。
注意：需要设置环境变量 `MINIMAX_API_KEY`，
并将 "<voice_id>", <file_id_of_cloned_voice>, <file_id_of_prompt_audio> 替换为实际值。
"""
import requests
import json
import os
api_key = os.getenv("MINIMAX_API_KEY")
url = "
clone_payload = {
"file_id": file_id,
"voice_id": "<your_custom_voice_id>",
"clone_prompt": {
"prompt_audio": prompt_file_id,
"prompt_text": "后来认为啊，是有人抓这鸡，可是抓鸡的地方呢没人听过鸡叫。"
},
"text": "大兄弟，听您口音不是本地人吧，头回来天津卫，啊，待会您可甭跟着导航走，那玩意儿净给您往大马路上绕。",
"model": "speech-2.8-hd"
clone_headers = {
"Authorization": f"Bearer {api_key}",
"Content-Type": "application/json"
response = requests.post(url, headers=headers, json=payload)
response.raise_for_status()
print(response.text)
```
```
curl --location '
--header 'A
--header 'Content-T
--data '{
"file_id": <file_id_of_cloned_voice>,
"voice_id": "<your_custom_voice_id>",
"clone_prompt": {
"prompt_audio": <file_id_of_prompt_audio>,
"prompt_text": "后来认为啊，是有人抓这鸡，可是抓鸡的地方呢没人听过鸡叫。"
},
"text": "大兄弟，听您口音不是本地人吧，头回来天津卫，啊，待会您可甭跟着导航走，那玩意净给您往大马路上绕。",
"model": "speech-2.8"
}'
```
## 
[​
完整示例
```
"""
本示例用于快速克隆音色并获取试听文件。
注意：需要先将密钥信息写入环境变量 `MINIMAX_API_KEY`，
并将"<your_custom_voice_id>"替换为您定义的音色 id。
"""
import json
import requests
import os
api_key = os.getenv("MINIMAX_API_KEY")
upload_url = "
clone_url = "
headers = {"Authorization": f"Bearer {api_key}"}
with open("/path/to/clone_input.mp3", "rb") as f:
files = {"file": ("clone_input.mp3", f)}
data = {"purpose": "voice_clone"}
response = requests.post(upload_url, headers=headers, data=data, files=files)
file_id = response.json()["file"]["file_id"]
print(f"File ID of the cloned 
# 2. 上传示例音频
with open("/path/to/clone_prompt.mp3", "rb") as f:
files = {"file": ("clone_prompt.mp3", f)}
data = {"purpose": "prompt_audio"}
response = requests.post(upload_url, headers=headers, data=data, files=files)
prompt_file_id = response.json()["file"]["file_id"]
print(f"File ID of the prompt 
# 3. 进行音色克隆
clone_payload = {
"file_id": file_id,
"voice_id": "<your_custom_voice_id>",
"clone_prompt": {
"prompt_audio": prompt_file_id,
"prompt_text": "后来认为啊，是有人抓这鸡，可是抓鸡的地方呢没人听过鸡叫。"
},
"text": "大兄弟，听您口音不是本地人吧，头回来天津卫，啊，待会您可甭跟着导航走，那玩意儿净给您往大马路上绕。",
"model": "speech-2.8-hd"
clone_headers = {
"Authorization": f"Bearer {api_key}",
"Content-Type": "application/json"
response = requests.post(clone_url, headers=clone_headers, json=clone_payload)
print(response.text)
```
## 
[​
结果示例
- **复刻音频**
- **示例音频**
- **结果音频**
## 
[​

---

## 系统音色列表

MiniMax 提供丰富的系统音色，支持多种语言和风格。

本文档列举了MiniMax开放平台全部的系统音色，为您提供语音合成选择。参考以下表格的内容，可查阅目前全部的系统音色的ID(Voice ID)、名称及支持语言，方便开发者快速查询与调用。
参考以下表格的内容，可查阅目前全部的系统音色。
| 序号 | 语言 | 音色 ID (Voice ID) | 音色名称 (Voice Name) 
| 1 | 中文 (普通话) | `male-qn-qingse` | 青涩青年音色 
| 2 | 中文 (普通话) | `male-qn-jingying` | 精英青年音色 
| 3 | 中文 (普通话) | `male-qn-badao` | 霸道青年音色 
| 4 | 中文 (普通话) | `male-qn-daxuesheng` | 青年大学生音色 
| 5 | 中文 (普通话) | `female-shaonv` | 少女音色 
| 6 | 中文 (普通话) | `female-yujie` | 御姐音色 
| 7 | 中文 (普通话) | `female-chengshu` | 成熟女性音色 
| 8 | 中文 (普通话) | `female-tianmei` | 甜美女性音色 
| 9 | 中文 (普通话) | `male-qn-qingse-jingpin` | 青涩青年音色-beta 
| 10 | 中文 (普通话) | `male-qn-jingying-jingpin` | 精英青年音色-beta 
| 11 | 中文 (普通话) | `male-qn-badao-jingpin` | 霸道青年音色-beta 
| 12 | 中文 (普通话) | `male-qn-daxuesheng-jingpin` | 青年大学生音色-beta 
| 13 | 中文 (普通话) | `female-shaonv-jingpin` | 少女音色-beta 
| 14 | 中文 (普通话) | `female-yujie-jingpin` | 御姐音色-beta 
| 15 | 中文 (普通话) | `female-chengshu-jingpin` | 成熟女性音色-beta 
| 16 | 中文 (普通话) | `female-tianmei-jingpin` | 甜美女性音色-beta 
| 17 | 中文 (普通话) | `clever_boy` | 聪明男童 
| 18 | 中文 (普通话) | `cute_boy` | 可爱男童 
| 19 | 中文 (普通话) | `lovely_girl` | 萌萌女童 
| 20 | 中文 (普通话) | `cartoon_pig` | 卡通猪小琪 
| 21 | 中文 (普通话) | `bingjiao_didi` | 病娇弟弟 
| 22 | 中文 (普通话) | `junlang_nanyou` | 俊朗男友 
| 23 | 中文 (普通话) | `chunzhen_xuedi` | 纯真学弟 
| 24 | 中文 (普通话) | `lengdan_xiongzhang` | 冷淡学长 
| 25 | 中文 (普通话) | `badao_shaoye` | 霸道少爷 
| 26 | 中文 (普通话) | `tianxin_xiaoling` | 甜心小玲 
| 27 | 中文 (普通话) | `qiaopi_mengmei` | 俏皮萌妹 
| 28 | 中文 (普通话) | `wumei_yujie` | 妩媚御姐 
| 29 | 中文 (普通话) | `diadia_xuemei` | 嗲嗲学妹 
| 30 | 中文 (普通话) | `danya_xuejie` | 淡雅学姐 
| 31 | 中文 (普通话) | `Chinese (Mandarin)_Reliable_Executive` | 沉稳高管 
| 32 | 中文 (普通话) | `Chinese (Mandarin)_News_Anchor` | 新闻女声 
| 33 | 中文 (普通话) | `Chinese (Mandarin)_Mature_Woman` | 傲娇御姐 
| 34 | 中文 (普通话) | `Chinese (Mandarin)_Unrestrained_Young_Man` | 不羁青年 
| 35 | 中文 (普通话) | `Arrogant_Miss` | 嚣张小姐 
| 36 | 中文 (普通话) | `Robot_Armor` | 机械战甲 
| 37 | 中文 (普通话) | `Chinese (Mandarin)_Kind-hearted_Antie` | 热心大婶 
| 38 | 中文 (普通话) | `Chinese (Mandarin)_HK_Flight_Attendant` | 港普空姐 
| 39 | 中文 (普通话) | `Chinese (Mandarin)_Humorous_Elder` | 搞笑大爷 
| 40 | 中文 (普通话) | `Chinese (Mandarin)_Gentleman` | 温润男声 
| 41 | 中文 (普通话) | `Chinese (Mandarin)_Warm_Bestie` | 温暖闺蜜 
| 42 | 中文 (普通话) | `Chinese (Mandarin)_Male_Announcer` | 播报男声 
| 43 | 中文 (普通话) | `Chinese (Mandarin)_Sweet_Lady` | 甜美女声 
| 44 | 中文 (普通话) | `Chinese (Mandarin)_Southern_Young_Man` | 南方小哥 
| 45 | 中文 (普通话) | `Chinese (Mandarin)_Wise_Women` | 阅历姐姐 
| 46 | 中文 (普通话) | `Chinese (Mandarin)_Gentle_Youth` | 温润青年 
| 47 | 中文 (普通话) | `Chinese (Mandarin)_Warm_Girl` | 温暖少女 
| 48 | 中文 (普通话) | `Chinese (Mandarin)_Kind-hearted_Elder` | 花甲奶奶 
| 49 | 中文 (普通话) | `Chinese (Mandarin)_Cute_Spirit` | 憨憨萌兽 
| 50 | 中文 (普通话) | `Chinese (Mandarin)_Radio_Host` | 电台男主播 
| 51 | 中文 (普通话) | `Chinese (Mandarin)_Lyrical_Voice` | 抒情男声 
| 52 | 中文 (普通话) | `Chinese (Mandarin)_Straightforward_Boy` | 率真弟弟 
| 53 | 中文 (普通话) | `Chinese (Mandarin)_Sincere_Adult` | 真诚青年 
| 54 | 中文 (普通话) | `Chinese (Mandarin)_Gentle_Senior` | 温柔学姐 
| 55 | 中文 (普通话) | `Chinese (Mandarin)_Stubborn_Friend` | 嘴硬竹马 
| 56 | 中文 (普通话) | `Chinese (Mandarin)_Crisp_Girl` | 清脆少女 
| 57 | 中文 (普通话) | `Chinese (Mandarin)_Pure-hearted_Boy` | 清澈邻家弟弟 
| 58 | 中文 (普通话) | `Chinese (Mandarin)_Soft_Girl` | 柔和少女 
| 59 | 中文 (粤语) | `Cantonese_ProfessionalHost（F)` | 专业女主持 
| 60 | 中文 (粤语) | `Cantonese_GentleLady` | 温柔女声 
| 61 | 中文 (粤语) | `Cantonese_ProfessionalHost（M)` | 专业男主持 
| 62 | 中文 (粤语) | `Cantonese_PlayfulMan` | 活泼男声 
| 63 | 中文 (粤语) | `Cantonese_CuteGirl` | 可爱女孩 
| 64 | 中文 (粤语) | `Cantonese_KindWoman` | 善良女声 
| 65 | 英文 | `Santa_Claus ` | Santa Claus 
| 66 | 英文 | `Grinch` | Grinch 
| 67 | 英文 | `Rudolph` | Rudolph 
| 68 | 英文 | `Arnold` | Arnold 
| 69 | 英文 | `Charming_Santa` | Charming Santa 
| 70 | 英文 | `Charming_Lady` | Charming Lady 
| 71 | 英文 | `Sweet_Girl` | Sweet Girl 
| 72 | 英文 | `Cute_Elf` | Cute Elf 
| 73 | 英文 | `Attractive_Girl` | Attractive Girl 
| 74 | 英文 | `Serene_Woman` | Serene Woman 
| 75 | 英文 | `_Trustworthy_Man` | Trustworthy Man 
| 76 | 英文 | `_Graceful_Lady` | Graceful Lady 
| 77 | 英文 | `_Aussie_Bloke` | Aussie Bloke 
| 78 | 英文 | `_Whispering_girl` | Whispering girl 
| 79 | 英文 | `_Diligent_Man` | Diligent Man 
| 80 | 英文 | `_Gentle-voiced_man` | Gentle-voiced man 
| 81 | 日文 | `Japanese_IntellectualSenior` | Intellectual Senior 
| 82 | 日文 | `Japanese_DecisivePrincess` | Decisive Princess 
| 83 | 日文 | `Japanese_LoyalKnight` | Loyal Knight 
| 84 | 日文 | `Japanese_DominantMan` | Dominant Man 
| 85 | 日文 | `Japanese_SeriousCommander` | Serious Commander 
| 86 | 日文 | `Japanese_ColdQueen` | Cold Queen 
| 87 | 日文 | `Japanese_DependableWoman` | Dependable Woman 
| 88 | 日文 | `Japanese_GentleButler` | Gentle Butler 
| 89 | 日文 | `Japanese_KindLady` | Kind Lady 
| 90 | 日文 | `Japanese_CalmLady` | Calm Lady 
| 91 | 日文 | `Japanese_OptimisticYouth` | Optimistic Youth 
| 92 | 日文 | `Japanese_GenerousIzakayaOwner` | Generous Izakaya Owner 
| 93 | 日文 | `Japanese_SportyStudent` | Sporty Student 
| 94 | 日文 | `Japanese_InnocentBoy` | Innocent Boy 
| 95 | 日文 | `Japanese_GracefulMaiden` | Graceful Maiden 
| 96 | 韩文 | `Korean_SweetGirl` | Sweet Girl 
| 97 | 韩文 | `Korean_CheerfulBoyfriend` | Cheerful Boyfriend 
| 98 | 韩文 | `Korean_EnchantingSister` | Enchanting Sister 
| 99 | 韩文 | `Korean_ShyGirl` | Shy Girl 
| 100 | 韩文 | `Korean_ReliableSister` | Reliable Sister 
| 101 | 韩文 | `Korean_StrictBoss` | Strict Boss 
| 102 | 韩文 | `Korean_SassyGirl` | Sassy Girl 
| 103 | 韩文 | `Korean_ChildhoodFriendGirl` | Childhood Friend Girl 
| 104 | 韩文 | `Korean_PlayboyCharmer` | Playboy Charmer 
| 105 | 韩文 | `Korean_ElegantPrincess` | Elegant Princess 
| 106 | 韩文 | `Korean_BraveFemaleWarrior` | Brave Female Warrior 
| 107 | 韩文 | `Korean_BraveYouth` | Brave Youth 
| 108 | 韩文 | `Korean_CalmLady` | Calm Lady 
| 109 | 韩文 | `Korean_EnthusiasticTeen` | Enthusiastic Teen 
| 110 | 韩文 | `Korean_SoothingLady` | Soothing Lady 
| 111 | 韩文 | `Korean_IntellectualSenior` | Intellectual Senior 
| 112 | 韩文 | `Korean_LonelyWarrior` | Lonely Warrior 
| 113 | 韩文 | `Korean_MatureLady` | Mature Lady 
| 114 | 韩文 | `Korean_InnocentBoy` | Innocent Boy 
| 115 | 韩文 | `Korean_CharmingSister` | Charming Sister 
| 116 | 韩文 | `Korean_AthleticStudent` | Athletic Student 
| 117 | 韩文 | `Korean_BraveAdventurer` | Brave Adventurer 
| 118 | 韩文 | `Korean_CalmGentleman` | Calm Gentleman 
| 119 | 韩文 | `Korean_WiseElf` | Wise Elf 
| 120 | 韩文 | `Korean_CheerfulCoolJunior` | Cheerful Cool Junior 
| 121 | 韩文 | `Korean_DecisiveQueen` | Decisive Queen 
| 122 | 韩文 | `Korean_ColdYoungMan` | Cold Young Man 
| 123 | 韩文 | `Korean_MysteriousGirl` | Mysterious Girl 
| 124 | 韩文 | `Korean_QuirkyGirl` | Quirky Girl 
| 125 | 韩文 | `Korean_ConsiderateSenior` | Considerate Senior 
| 126 | 韩文 | `Korean_CheerfulLittleSister` | Cheerful Little Sister 
| 127 | 韩文 | `Korean_DominantMan` | Dominant Man 
| 128 | 韩文 | `Korean_AirheadedGirl` | Airheaded Girl 
| 129 | 韩文 | `Korean_ReliableYouth` | Reliable Youth 
| 130 | 韩文 | `Korean_FriendlyBigSister` | Friendly Big Sister 
| 131 | 韩文 | `Korean_GentleBoss` | Gentle Boss 
| 132 | 韩文 | `Korean_ColdGirl` | Cold Girl 
| 133 | 韩文 | `Korean_HaughtyLady` | Haughty Lady 
| 134 | 韩文 | `Korean_CharmingElderSister` | Charming Elder Sister 
| 135 | 韩文 | `Korean_IntellectualMan` | Intellectual Man 
| 136 | 韩文 | `Korean_CaringWoman` | Caring Woman 
| 137 | 韩文 | `Korean_WiseTeacher` | Wise Teacher 
| 138 | 韩文 | `Korean_ConfidentBoss` | Confident Boss 
| 139 | 韩文 | `Korean_AthleticGirl` | Athletic Girl 
| 140 | 韩文 | `Korean_PossessiveMan` | Possessive Man 
| 141 | 韩文 | `Korean_GentleWoman` | Gentle Woman 
| 142 | 韩文 | `Korean_CockyGuy` | Cocky Guy 
| 143 | 韩文 | `Korean_ThoughtfulWoman` | Thoughtful Woman 
| 144 | 韩文 | `Korean_OptimisticYouth` | Optimistic Youth 
| 145 | 西班牙文 | `Spanish_SereneWoman` | Serene Woman 
| 146 | 西班牙文 | `Spanish_MaturePartner` | Mature Partner 
| 147 | 西班牙文 | `Spanish_CaptivatingStoryteller` | Captivating Storyteller 
| 148 | 西班牙文 | `Spanish_Narrator` | Narrator 
| 149 | 西班牙文 | `Spanish_WiseScholar` | Wise Scholar 
| 150 | 西班牙文 | `Spanish_Kind-heartedGirl` | Kind-hearted Girl 
| 151 | 西班牙文 | `Spanish_DeterminedManager` | Determined Manager 
| 152 | 西班牙文 | `Spanish_BossyLeader` | Bossy Leader 
| 153 | 西班牙文 | `Spanish_ReservedYoungMan` | Reserved Young Man 
| 154 | 西班牙文 | `Spanish_ConfidentWoman` | Confident Woman 
| 155 | 西班牙文 | `Spanish_ThoughtfulMan` | Thoughtful Man 
| 156 | 西班牙文 | `Spanish_Strong-WilledBoy` | Strong-willed Boy 
| 157 | 西班牙文 | `Spanish_SophisticatedLady` | Sophisticated Lady 
| 158 | 西班牙文 | `Spanish_RationalMan` | Rational Man 
| 159 | 西班牙文 | `Spanish_AnimeCharacter` | Anime Character 
| 160 | 西班牙文 | `Spanish_Deep-tonedMan` | Deep-toned Man 
| 161 | 西班牙文 | `Spanish_Fussyhostess` | Fussy hostess 
| 162 | 西班牙文 | `Spanish_SincereTeen` | Sincere Teen 
| 163 | 西班牙文 | `Spanish_FrankLady` | Frank Lady 
| 164 | 西班牙文 | `Spanish_Comedian` | Comedian 
| 165 | 西班牙文 | `Spanish_Debator` | Debator 
| 166 | 西班牙文 | `Spanish_ToughBoss` | Tough Boss 
| 167 | 西班牙文 | `Spanish_Wiselady` | Wise Lady 
| 168 | 西班牙文 | `Spanish_Steadymentor` | Steady Mentor 
| 169 | 西班牙文 | `Spanish_Jovialman` | Jovial Man 
| 170 | 西班牙文 | `Spanish_SantaClaus` | Santa Claus 
| 171 | 西班牙文 | `Spanish_Rudolph` | Rudolph 
| 172 | 西班牙文 | `Spanish_Intonategirl` | Intonate Girl 
| 173 | 西班牙文 | `Spanish_Arnold` | Arnold 
| 174 | 西班牙文 | `Spanish_Ghost` | Ghost 
| 175 | 西班牙文 | `Spanish_HumorousElder` | Humorous Elder 
| 176 | 西班牙文 | `Spanish_EnergeticBoy` | Energetic Boy 
| 177 | 西班牙文 | `Spanish_WhimsicalGirl` | Whimsical Girl 
| 178 | 西班牙文 | `Spanish_StrictBoss` | Strict Boss 
| 179 | 西班牙文 | `Spanish_ReliableMan` | Reliable Man 
| 180 | 西班牙文 | `Spanish_SereneElder` | Serene Elder 
| 181 | 西班牙文 | `Spanish_AngryMan` | Angry Man 
| 182 | 西班牙文 | `Spanish_AssertiveQueen` | Assertive Queen 
| 183 | 西班牙文 | `Spanish_CaringGirlfriend` | Caring Girlfriend 
| 184 | 西班牙文 | `Spanish_PowerfulSoldier` | Powerful Soldier 
| 185 | 西班牙文 | `Spanish_PassionateWarrior` | Passionate Warrior 
| 186 | 西班牙文 | `Spanish_ChattyGirl` | Chatty Girl 
| 187 | 西班牙文 | `Spanish_RomanticHusband` | Romantic Husband 
| 188 | 西班牙文 | `Spanish_CompellingGirl` | Compelling Girl 
| 189 | 西班牙文 | `Spanish_PowerfulVeteran` | Powerful Veteran 
| 190 | 西班牙文 | `Spanish_SensibleManager` | Sensible Manager 
| 191 | 西班牙文 | `Spanish_ThoughtfulLady` | Thoughtful Lady 
| 192 | 葡萄牙文 | `Portuguese_SentimentalLady` | Sentimental Lady 
| 193 | 葡萄牙文 | `Portuguese_BossyLeader` | Bossy Leader 
| 194 | 葡萄牙文 | `Portuguese_Wiselady` | Wise lady 
| 195 | 葡萄牙文 | `Portuguese_Strong-WilledBoy` | Strong-willed Boy 
| 196 | 葡萄牙文 | `Portuguese_Deep-VoicedGentleman` | Deep-voiced Gentleman 
| 197 | 葡萄牙文 | `Portuguese_UpsetGirl` | Upset Girl 
| 198 | 葡萄牙文 | `Portuguese_PassionateWarrior` | Passionate Warrior 
| 199 | 葡萄牙文 | `Portuguese_AnimeCharacter` | Anime Character 
| 200 | 葡萄牙文 | `Portuguese_ConfidentWoman` | Confident Woman 
| 201 | 葡萄牙文 | `Portuguese_AngryMan` | Angry Man 
| 202 | 葡萄牙文 | `Portuguese_CaptivatingStoryteller` | Captivating Storyteller 
| 203 | 葡萄牙文 | `Portuguese_Godfather` | Godfather 
| 204 | 葡萄牙文 | `Portuguese_ReservedYoungMan` | Reserved Young Man 
| 205 | 葡萄牙文 | `Portuguese_SmartYoungGirl` | Smart Young Girl 
| 206 | 葡萄牙文 | `Portuguese_Kind-heartedGirl` | Kind-hearted Girl 
| 207 | 葡萄牙文 | `Portuguese_Pompouslady` | Pompous lady 
| 208 | 葡萄牙文 | `Portuguese_Grinch` | Grinch 
| 209 | 葡萄牙文 | `Portuguese_Debator` | Debator 
| 210 | 葡萄牙文 | `Portuguese_SweetGirl` | Sweet Girl 
| 211 | 葡萄牙文 | `Portuguese_AttractiveGirl` | Attractive Girl 
| 212 | 葡萄牙文 | `Portuguese_ThoughtfulMan` | Thoughtful Man 
| 213 | 葡萄牙文 | `Portuguese_PlayfulGirl` | Playful Girl 
| 214 | 葡萄牙文 | `Portuguese_GorgeousLady` | Gorgeous Lady 
| 215 | 葡萄牙文 | `Portuguese_LovelyLady` | Lovely Lady 
| 216 | 葡萄牙文 | `Portuguese_SereneWoman` | Serene Woman 
| 217 | 葡萄牙文 | `Portuguese_SadTeen` | Sad Teen 
| 218 | 葡萄牙文 | `Portuguese_MaturePartner` | Mature Partner 
| 219 | 葡萄牙文 | `Portuguese_Comedian` | Comedian 
| 220 | 葡萄牙文 | `Portuguese_NaughtySchoolgirl` | Naughty Schoolgirl 
| 221 | 葡萄牙文 | `Portuguese_Narrator` | Narrator 
| 222 | 葡萄牙文 | `Portuguese_ToughBoss` | Tough Boss 
| 223 | 葡萄牙文 | `Portuguese_Fussyhostess` | Fussy hostess 
| 224 | 葡萄牙文 | `Portuguese_Dramatist` | Dramatist 
| 225 | 葡萄牙文 | `Portuguese_Steadymentor` | Steady Mentor 
| 226 | 葡萄牙文 | `Portuguese_Jovialman` | Jovial Man 
| 227 | 葡萄牙文 | `Portuguese_CharmingQueen` | Charming Queen 
| 228 | 葡萄牙文 | `Portuguese_SantaClaus` | Santa Claus 
| 229 | 葡萄牙文 | `Portuguese_Rudolph` | Rudolph 
| 230 | 葡萄牙文 | `Portuguese_Arnold` | Arnold 
| 231 | 葡萄牙文 | `Portuguese_CharmingSanta` | Charming Santa 
| 232 | 葡萄牙文 | `Portuguese_CharmingLady` | Charming Lady 
| 233 | 葡萄牙文 | `Portuguese_Ghost` | Ghost 
| 234 | 葡萄牙文 | `Portuguese_HumorousElder` | Humorous Elder 
| 235 | 葡萄牙文 | `Portuguese_CalmLeader` | Calm Leader 
| 236 | 葡萄牙文 | `Portuguese_GentleTeacher` | Gentle Teacher 
| 237 | 葡萄牙文 | `Portuguese_EnergeticBoy` | Energetic Boy 
| 238 | 葡萄牙文 | `Portuguese_ReliableMan` | Reliable Man 
| 239 | 葡萄牙文 | `Portuguese_SereneElder` | Serene Elder 
| 240 | 葡萄牙文 | `Portuguese_GrimReaper` | Grim Reaper 
| 241 | 葡萄牙文 | `Portuguese_AssertiveQueen` | Assertive Queen 
| 242 | 葡萄牙文 | `Portuguese_WhimsicalGirl` | Whimsical Girl 
| 243 | 葡萄牙文 | `Portuguese_StressedLady` | Stressed Lady 
| 244 | 葡萄牙文 | `Portuguese_FriendlyNeighbor` | Friendly Neighbor 
| 245 | 葡萄牙文 | `Portuguese_CaringGirlfriend` | Caring Girlfriend 
| 246 | 葡萄牙文 | `Portuguese_PowerfulSoldier` | Powerful Soldier 
| 247 | 葡萄牙文 | `Portuguese_FascinatingBoy` | Fascinating Boy 
| 248 | 葡萄牙文 | `Portuguese_RomanticHusband` | Romantic Husband 
| 249 | 葡萄牙文 | `Portuguese_StrictBoss` | Strict Boss 
| 250 | 葡萄牙文 | `Portuguese_InspiringLady` | Inspiring Lady 
| 251 | 葡萄牙文 | `Portuguese_PlayfulSpirit` | Playful Spirit 
| 252 | 葡萄牙文 | `Portuguese_ElegantGirl` | Elegant Girl 
| 253 | 葡萄牙文 | `Portuguese_CompellingGirl` | Compelling Girl 
| 254 | 葡萄牙文 | `Portuguese_PowerfulVeteran` | Powerful Veteran 
| 255 | 葡萄牙文 | `Portuguese_SensibleManager` | Sensible Manager 
| 256 | 葡萄牙文 | `Portuguese_ThoughtfulLady` | Thoughtful Lady 
| 257 | 葡萄牙文 | `Portuguese_TheatricalActor` | Theatrical Actor 
| 258 | 葡萄牙文 | `Portuguese_FragileBoy` | Fragile Boy 
| 259 | 葡萄牙文 | `Portuguese_ChattyGirl` | Chatty Girl 
| 260 | 葡萄牙文 | `Portuguese_Conscientiousinstructor` | Conscientious Instructor 
| 261 | 葡萄牙文 | `Portuguese_RationalMan` | Rational Man 
| 262 | 葡萄牙文 | `Portuguese_WiseScholar` | Wise Scholar 
| 263 | 葡萄牙文 | `Portuguese_FrankLady` | Frank Lady 
| 264 | 葡萄牙文 | `Portuguese_DeterminedManager` | Determined Manager 
| 265 | 法文 | `French_Male_Speech_New` | Level-Headed Man 
| 266 | 法文 | `French_Female_News Anchor` | Patient Female Presenter 
| 267 | 法文 | `French_CasualMan` | Casual Man 
| 268 | 法文 | `French_MovieLeadFemale` | Movie Lead Female 
| 269 | 法文 | `French_FemaleAnchor` | Female Anchor 
| 270 | 法文 | `French_MaleNarrator` | Male Narrator 
| 271 | 印尼文 | `Indonesian_SweetGirl` | Sweet Girl 
| 272 | 印尼文 | `Indonesian_ReservedYoungMan` | Reserved Young Man 
| 273 | 印尼文 | `Indonesian_CharmingGirl` | Charming Girl 
| 274 | 印尼文 | `Indonesian_CalmWoman` | Calm Woman 
| 275 | 印尼文 | `Indonesian_ConfidentWoman` | Confident Woman 
| 276 | 印尼文 | `Indonesian_CaringMan` | Caring Man 
| 277 | 印尼文 | `Indonesian_BossyLeader` | Bossy Leader 
| 278 | 印尼文 | `Indonesian_DeterminedBoy` | Determined Boy 
| 279 | 印尼文 | `Indonesian_GentleGirl` | Gentle Girl 
| 280 | 德文 | `German_FriendlyMan` | Friendly Man 
| 281 | 德文 | `German_SweetLady` | Sweet Lady 
| 282 | 德文 | `German_PlayfulMan` | Playful Man 
| 283 | 俄文 | `Russian_HandsomeChildhoodFriend` | Handsome Childhood Friend 
| 284 | 俄文 | `Russian_BrightHeroine` | Bright Queen 
| 285 | 俄文 | `Russian_AmbitiousWoman` | Ambitious Woman 
| 286 | 俄文 | `Russian_ReliableMan` | Reliable Man 
| 287 | 俄文 | `Russian_CrazyQueen` | Crazy Girl 
| 288 | 俄文 | `Russian_PessimisticGirl` | Pessimistic Girl 
| 289 | 俄文 | `Russian_AttractiveGuy` | Attractive Guy 
| 290 | 俄文 | `Russian_Bad-temperedBoy` | Bad-tempered Boy 
| 291 | 意大利文 | `Italian_BraveHeroine` | Brave Heroine 
| 292 | 意大利文 | `Italian_Narrator` | Narrator 
| 293 | 意大利文 | `Italian_WanderingSorcerer` | Wandering Sorcerer 
| 294 | 意大利文 | `Italian_DiligentLeader` | Diligent Leader 
| 295 | 阿拉伯文 | `Arabic_CalmWoman` | Calm Woman 
| 296 | 阿拉伯文 | `Arabic_FriendlyGuy` | Friendly Guy 
| 297 | 土耳其文 | `Turkish_CalmWoman` | Calm Woman 
| 298 | 土耳其文 | `Turkish_Trustworthyman` | Trustworthy man 
| 299 | 乌克兰文 | `Ukrainian_CalmWoman` | Calm Woman 
| 300 | 乌克兰文 | `Ukrainian_WiseScholar` | Wise Scholar 
| 301 | 荷兰文 | `Dutch_kindhearted_girl` | Kind-hearted girl 
| 302 | 荷兰文 | `Dutch_bossy_leader` | Bossy leader 
| 303 | 越南文 | `Vietnamese_kindhearted_girl` | Kind-hearted girl 
| 304 | 泰文 | `Thai_male_1_sample8` | Serene Man 
| 305 | 泰文 | `Thai_male_2_sample2` | Friendly Man 
| 306 | 泰文 | `Thai_female_1_sample1` | Confident Woman 
| 307 | 泰文 | `Thai_female_2_sample2` | Energetic Woman 
| 308 | 波兰文 | `Polish_male_1_sample4` | Male Narrator 
| 309 | 波兰文 | `Polish_male_2_sample3` | Male Anchor 
| 310 | 波兰文 | `Polish_female_1_sample1` | Calm Woman 
| 311 | 波兰文 | `Polish_female_2_sample3` | Casual Woman 
| 312 | 罗马尼亚文 | `Romanian_male_1_sample2` | Reliable Man 
| 313 | 罗马尼亚文 | `Romanian_male_2_sample1` | Energetic Youth 
| 314 | 罗马尼亚文 | `Romanian_female_1_sample4` | Optimistic Youth 
| 315 | 罗马尼亚文 | `Romanian_female_2_sample1` | Gentle Woman 
| 316 | 希腊文 | `greek_male_1a_v1` | Thoughtful Mentor 
| 317 | 希腊文 | `Greek_female_1_sample1` | Gentle Lady 
| 318 | 希腊文 | `Greek_female_2_sample3` | Girl Next Door 
| 319 | 捷克文 | `czech_male_1_v1` | Assured Presenter 
| 320 | 捷克文 | `czech_female_5_v7` | Steadfast Narrator 
| 321 | 捷克文 | `czech_female_2_v2` | Elegant Lady 
| 322 | 芬兰文 | `finnish_male_3_v1` | Upbeat Man 
| 323 | 芬兰文 | `finnish_male_1_v2` | Friendly Boy 
| 324 | 芬兰文 | `finnish_female_4_v1` | Assetive Woman 
| 325 | 印地文 | `hindi_male_1_v2` | Trustworthy Advisor 
| 326 | 印地文 | `hindi_female_2_v1` | Tranquil Woman 
| 327 | 印地文 | `hindi_female_1_v2` | News Anchor 
此页面对您有帮助吗？
是否
异步语音合成
图片生成
Ctrl+I

---

# 图像生成

## 图片生成

图片生成服务提供文生图（text-to-image）与图生图（image-to-image）两种核心功能。

服务提供文生图（text-to-image）与图生图（image-to-image）两种核心功能。
## 
[​
根据文本生成图片
根据详尽的文本描述（prompt），直接生成与之匹配的图片。
请求示例
```
import base64
import requests
import os
url = "
api_key = os.environ.get("MINIMAX_API_KEY")
headers = {"Authorization": f"Bearer {api_key}"}
payload = {
"model": "image-01",
"prompt": "men Dressing in white t shirt, full-body stand front view image :25, outdoor, Venice beach sign, full-body image, Los Angeles, Fashion photography of 90s, documentary, Film grain, photorealistic",
"aspect_ratio": "16:9",
"response_format": "base64",
response = requests.post(url, headers=headers, json=payload)
response.raise_for_status()
images = response.json()["data"]["image_base64"]
for i in range(len(images)):
with open(f"output-{i}.jpeg", "wb") as f:
f.write(base64.b64decode(images[i]))
```
生成结果：
## 
[​
结合参考图生成图片
此功能允许提供一张包含清晰主体的参考图（支持网络图片链接），并结合 prompt 描述，生成一张保留了主体特征的新图片。当前每次请求仅支持传入一张参考图。该功能尤其适用于需要保持人物形象一致性的场景，例如为同一个虚拟角色生成不同情境下的图片。
请求示例
```
import base64
import requests
import os
url = "
api_key = os.environ.get("MINIMAX_API_KEY")
headers = {"Authorization": f"Bearer {api_key}"}
payload = {
"model": "image-01",
"prompt": "女孩在图书馆的窗户前，看向远方",
"aspect_ratio": "16:9",
"subject_reference": [
"type": "character",
"image_file": "
],
"response_format": "base64",
response = requests.post(url, headers=headers, json=payload)
response.raise_for_status()
images = response.json()["data"]["image_base64"]
for i in range(len(images)):
with open(f"output-{i}.jpeg", "wb") as f:
f.write(base64.b64decode(images[i]))
```
生成结果：
## 
[​

---

# 音乐生成

## 音乐生成

MiniMax 音乐生成 API 支持根据歌词和风格描述生成音乐。

能力](
- [示例](
- [翻唱生成](
- [两步翻唱（进阶模式 — 支持歌词修改）](
- [

