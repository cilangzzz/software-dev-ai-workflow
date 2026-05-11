#!/usr/bin/env python3
"""
阿里云百炼 Qwen-Image 文生图 API 调用脚本
基于官方文档: https://help.aliyun.com/zh/model-studio/qwen-image-api

使用方法:
    python generate_image.py [--prompt "提示词"] [--size "分辨率"]
"""

import os
import sys
import argparse
import requests
from pathlib import Path
from datetime import datetime

# Windows编码设置
if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')

try:
    import dashscope
    from dashscope import MultiModalConversation
except ImportError:
    print("请先安装 dashscope SDK: pip install dashscope")
    sys.exit(1)


def generate_image(prompt: str, size: str = "2048*2048",
                   negative_prompt: str = "", watermark: bool = False,
                   prompt_extend: bool = True, output_dir: str = None,
                   model: str = "qwen-image-2.0-pro"):
    """
    使用 DashScope SDK 调用 Qwen-Image API 生成图像

    Args:
        prompt: 正向提示词，描述期望的图像内容
        size: 输出分辨率，格式为 宽*高
        negative_prompt: 反向提示词，描述不希望出现的内容
        watermark: 是否添加水印
        prompt_extend: 是否开启提示词智能改写
        output_dir: 输出目录路径
        model: 模型名称 (qwen-image-max, qwen-image-2.0-pro, qwen-image-2.0)

    Returns:
        str: 生成图片的保存路径
    """
    # API Key配置 - 从环境变量或直接设置
    api_key = os.getenv("DASHSCOPE_API_KEY")
    if not api_key:
        # 读取.env文件
        env_path = Path(__file__).parent.parent / ".env"
        if env_path.exists():
            with open(env_path, "r", encoding="utf-8") as f:
                for line in f:
                    if "DASHSCOPE_API_KEY" in line and "=" in line:
                        api_key = line.split("=")[1].strip()
                        break

    if not api_key:
        print("错误: 未配置 DASHSCOPE_API_KEY")
        print("请在 .env 文件中设置或使用环境变量")
        return None

    dashscope.api_key = api_key

    # 北京地域URL
    dashscope.base_http_api_url = 'https://dashscope.aliyuncs.com/api/v1'

    # 默认反向提示词
    if not negative_prompt:
        negative_prompt = "低分辨率，低画质，肢体畸形，手指畸形，画面过饱和，蜡像感，人脸无细节，过度光滑，画面具有AI感。构图混乱。文字模糊，扭曲。"

    # 构建消息 - 官方文档格式
    messages = [
        {
            "role": "user",
            "content": [
                {"text": prompt}
            ]
        }
    ]

    print(f"\n正在生成图像...")
    print(f"  模型: {model}")
    print(f"  提示词: {prompt[:50]}{'...' if len(prompt) > 50 else ''}")
    print(f"  分辨率: {size}")

    # 调用API - 官方SDK方式
    response = MultiModalConversation.call(
        model=model,
        messages=messages,
        result_format='message',
        stream=False,
        watermark=watermark,
        prompt_extend=prompt_extend,
        negative_prompt=negative_prompt,
        size=size
    )

    # 处理响应
    if response.status_code == 200:
        # 提取图像URL
        choices = response.output.get('choices', [])
        if choices:
            content = choices[0].get('message', {}).get('content', [])
            if content:
                image_url = content[0].get('image')

                # 下载并保存图像
                output_path = Path(output_dir) if output_dir else Path(__file__).parent.parent / "output"
                output_path.mkdir(exist_ok=True)

                timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                save_path = output_path / f"qwen_image_{timestamp}.png"

                # 下载图片
                img_response = requests.get(image_url, timeout=30)
                with open(save_path, "wb") as f:
                    f.write(img_response.content)

                # 输出信息
                usage = response.usage
                print(f"\n生成成功!")
                print(f"  Request ID: {response.request_id}")
                print(f"  图像尺寸: {usage.get('width')}x{usage.get('height')}")
                print(f"  保存路径: {save_path}")

                return str(save_path)
    else:
        print(f"\n生成失败!")
        print(f"  错误码: {response.code}")
        print(f"  错误信息: {response.message}")
        return None


def main():
    parser = argparse.ArgumentParser(description="阿里云百炼 Qwen-Image 文生图")
    parser.add_argument("--prompt", "-p",
                        default="一只可爱的橘黄色猫咪，坐在温暖的阳光下，毛发蓬松柔软，表情愉悦活泼，背景是温馨的现代家居客厅。",
                        help="图像描述提示词")
    parser.add_argument("--model", "-m", default="qwen-image-2.0-pro",
                        choices=["qwen-image-max", "qwen-image-2.0-pro", "qwen-image-2.0"],
                        help="模型名称")
    parser.add_argument("--size", "-s", default="2048*2048",
                        help="输出分辨率 (如: 2048*2048, 1024*1024)")
    parser.add_argument("--negative", "-n", default="",
                        help="反向提示词")
    parser.add_argument("--output", "-o", default=None,
                        help="输出目录")
    parser.add_argument("--watermark", "-w", action="store_true",
                        help="添加水印")

    args = parser.parse_args()

    generate_image(
        prompt=args.prompt,
        model=args.model,
        size=args.size,
        negative_prompt=args.negative,
        watermark=args.watermark,
        output_dir=args.output
    )


if __name__ == "__main__":
    main()