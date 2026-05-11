#!/usr/bin/env python3
"""
阿里云百炼 Qwen-Image 文生图 API 调用脚本

使用方法:
    python generate_image.py [--prompt "提示词"] [--size "分辨率"] [--output "输出文件名"]
"""

import os
import json
import argparse
import time
from pathlib import Path
from datetime import datetime

try:
    import requests
except ImportError:
    print("请先安装 requests 库: pip install requests")
    exit(1)


def load_env(env_file=".env"):
    """加载环境变量文件"""
    env_path = Path(__file__).parent.parent / env_file
    if not env_path.exists():
        print(f"警告: 未找到 {env_file} 文件，请复制 .env.example 并填入实际值")
        return {}

    env_vars = {}
    with open(env_path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line and not line.startswith("#") and "=" in line:
                key, value = line.split("=", 1)
                env_vars[key.strip()] = value.strip()
    return env_vars


def generate_image_sync(api_key, api_url, prompt, size="2048*2048",
                        negative_prompt="", watermark=False, prompt_extend=True):
    """
    同步调用 - 使用 qwen-image-2.0-pro 模型

    Args:
        api_key: API密钥
        api_url: API基础地址
        prompt: 正向提示词
        size: 输出分辨率
        negative_prompt: 反向提示词
        watermark: 是否添加水印
        prompt_extend: 是否智能改写提示词

    Returns:
        dict: API响应结果
    """
    endpoint = f"{api_url}/services/aigc/multimodal-generation/generation"

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}"
    }

    payload = {
        "model": "qwen-image-2.0-pro",
        "input": {
            "messages": [
                {
                    "role": "user",
                    "content": [
                        {"text": prompt}
                    ]
                }
            ]
        },
        "parameters": {
            "negative_prompt": negative_prompt,
            "prompt_extend": prompt_extend,
            "watermark": watermark,
            "size": size
        }
    }

    print(f"\n正在生成图像...")
    print(f"  模型: qwen-image-2.0-pro")
    print(f"  提示词: {prompt[:50]}{'...' if len(prompt) > 50 else ''}")
    print(f"  分辨率: {size}")

    try:
        response = requests.post(endpoint, headers=headers, json=payload, timeout=60, proxies={"http": None, "https": None})
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        return {"error": str(e)}


def download_image(image_url, output_path):
    """下载生成的图片"""
    print(f"\n正在下载图片...")
    print(f"  URL: {image_url[:60]}...")

    try:
        response = requests.get(image_url, timeout=30)
        response.raise_for_status()

        with open(output_path, "wb") as f:
            f.write(response.content)

        print(f"  保存路径: {output_path}")
        return True
    except requests.exceptions.RequestException as e:
        print(f"下载失败: {e}")
        return False


def main():
    # 解析命令行参数
    parser = argparse.ArgumentParser(description="阿里云百炼文生图API调用")
    parser.add_argument("--prompt", "-p", default=None, help="图像描述提示词")
    parser.add_argument("--size", "-s", default="2048*2048", help="输出分辨率")
    parser.add_argument("--output", "-o", default=None, help="输出文件名")
    parser.add_argument("--negative", "-n", default="", help="反向提示词")
    args = parser.parse_args()

    # 加载环境变量
    env = load_env()
    api_key = env.get("DASHSCOPE_API_KEY")
    api_url = env.get("DASHSCOPE_API_URL", "https://dashscope.aliyuncs.com/api/v1")

    if not api_key:
        print("错误: 未配置 DASHSCOPE_API_KEY，请在 .env 文件中设置")
        return

    # 默认提示词
    default_prompt = "一只可爱的橘黄色猫咪，坐在温暖的阳光下，毛发蓬松柔软，表情愉悦活泼，背景是温馨的现代家居客厅，有木质地板和绿色植物，自然光线柔和，画面真实摄影风格，细节逼真。"

    prompt = args.prompt or default_prompt

    # 设置输出文件名
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_dir = Path(__file__).parent.parent / "output"
    output_dir.mkdir(exist_ok=True)
    output_name = args.output or f"generated_{timestamp}.png"
    output_path = output_dir / output_name

    # 反向提示词（过滤低质量元素）
    negative_prompt = args.negative or "低分辨率，低画质，肢体畸形，手指畸形，画面过饱和，蜡像感，人脸无细节，过度光滑，画面具有AI感，构图混乱，文字模糊，扭曲。"

    # 调用API生成图像
    result = generate_image_sync(
        api_key=api_key,
        api_url=api_url,
        prompt=prompt,
        size=args.size,
        negative_prompt=negative_prompt,
        watermark=False,
        prompt_extend=True
    )

    # 处理响应
    if "error" in result:
        print(f"\n生成失败: {result['error']}")
        if result.get("status_code"):
            print(f"HTTP状态码: {result['status_code']}")
        return

    # 提取图像URL
    try:
        choices = result.get("output", {}).get("choices", [])
        if choices:
            content = choices[0].get("message", {}).get("content", [])
            if content and "image" in content[0]:
                image_url = content[0]["image"]

                # 显示响应信息
                usage = result.get("usage", {})
                print(f"\n生成成功!")
                print(f"  图像宽度: {usage.get('width', 'N/A')}px")
                print(f"  图像高度: {usage.get('height', 'N/A')}px")
                print(f"  Request ID: {result.get('request_id', 'N/A')}")

                # 下载图片
                if download_image(image_url, output_path):
                    print(f"\n✅ 完成! 图片已保存至: {output_path}")
            else:
                print("响应中未找到图像URL")
        else:
            print("响应格式异常:", json.dumps(result, indent=2, ensure_ascii=False))
    except Exception as e:
        print(f"解析响应失败: {e}")
        print("原始响应:", json.dumps(result, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()