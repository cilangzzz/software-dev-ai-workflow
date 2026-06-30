#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
SearXNG 搜索脚本（带 Clash 代理自适应）
用法: python scripts/searxng_search.py "<query>" [options]

参数:
    query    - 搜索关键词 (必填)
    instance - SearXNG 实例地址 (可选，默认使用 searx.be)
    --proxy  - 自定义代理地址
    --no-proxy - 禁用代理

示例:
    python scripts/searxng_search.py "Python web framework"
    python scripts/searxng_search.py "!github React hooks" https://search.bus-hit.me
    python scripts/searxng_search.py "test" --proxy http://127.0.0.1:7890
"""

import sys
import json
import os
import urllib.parse
import socket

try:
    import requests
except ImportError:
    print("错误: 请先安装 requests 库")
    print("执行: pip install requests")
    sys.exit(1)

# ============================================
# Clash 代理自适应配置
# ============================================

CLASH_PORTS = [7890, 7897, 7891]  # Clash 默认 HTTP 端口


def detect_clash_proxy():
    """
    自动检测 Clash 代理

    Returns:
        dict: 代理配置或 None
    """
    # 1. 检查环境变量
    http_proxy = os.environ.get("HTTP_PROXY") or os.environ.get("http_proxy")
    https_proxy = os.environ.get("HTTPS_PROXY") or os.environ.get("https_proxy")

    if http_proxy or https_proxy:
        return {
            "http": http_proxy or https_proxy,
            "https": https_proxy or http_proxy
        }

    # 2. 检测 Clash 默认端口
    for port in CLASH_PORTS:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)
            result = sock.connect_ex(('127.0.0.1', port))
            sock.close()

            if result == 0:
                proxy_url = f"http://127.0.0.1:{port}"
                return {"http": proxy_url, "https": proxy_url}
        except:
            pass

    return None


def get_proxies(custom_proxy=None, no_proxy=False):
    """获取代理配置"""
    if no_proxy:
        return None
    if custom_proxy:
        return {"http": custom_proxy, "https": custom_proxy}
    return detect_clash_proxy()


# ============================================
# 搜索配置
# ============================================

# 默认公开实例列表
PUBLIC_INSTANCES = [
    "https://searx.be",
    "https://search.bus-hit.me",
    "https://searx.fmac.xyz",
    "https://search.sapti.me",
    "https://searxng.nicfab.eu"
]

DEFAULT_INSTANCE = PUBLIC_INSTANCES[0]

# 搜索引擎快捷语法
SEARCH_SHORTCUTS = {
    "!gh": "github",
    "!github": "github",
    "!so": "stackoverflow",
    "!stackoverflow": "stackoverflow",
    "!g": "google",
    "!google": "google",
    "!bing": "bing",
    "!ddg": "duckduckgo",
    "!wp": "wikipedia",
    "!wikipedia": "wikipedia",
    "!yt": "youtube",
    "!youtube": "youtube"
}


def search_searxng(query, instance=DEFAULT_INSTANCE, format="json", timeout=30, proxy=None, no_proxy=False):
    """
    执行 SearXNG 搜索

    Args:
        query: 搜索关键词
        instance: SearXNG 实例地址
        format: 输出格式 (json/html)
        timeout: 超时时间(秒)
        proxy: 自定义代理地址
        no_proxy: 是否禁用代理

    Returns:
        dict: 搜索结果
    """
    params = {
        "q": query,
        "format": format,
        "language": "zh-CN"
    }

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        "Accept": "application/json, text/javascript, */*",
        "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8"
    }

    proxies = get_proxies(proxy, no_proxy)

    try:
        response = requests.get(
            f"{instance}/search",
            params=params,
            headers=headers,
            timeout=timeout,
            proxies=proxies
        )
        response.raise_for_status()
        return response.json()
    except requests.exceptions.Timeout:
        return {"error": "请求超时", "error_type": "timeout"}
    except requests.exceptions.ConnectionError as e:
        return {"error": f"无法连接到 {instance} (代理: {proxies})", "error_type": "connection"}
    except requests.exceptions.HTTPError as e:
        return {"error": f"HTTP 错误: {e}", "error_type": "http"}
    except json.JSONDecodeError:
        return {"error": "响应解析失败", "error_type": "parse"}
    except Exception as e:
        return {"error": str(e), "error_type": "unknown"}


def format_results(result, max_results=10):
    """
    格式化输出搜索结果

    Args:
        result: 搜索结果字典
        max_results: 最大显示结果数

    Returns:
        str: 格式化的结果字符串
    """
    if "error" in result:
        return f"[错误] {result['error']}"

    if "results" not in result or not result["results"]:
        return "未找到相关结果"

    output = []
    results = result["results"][:max_results]

    for i, item in enumerate(results, 1):
        title = item.get("title", "无标题")
        url = item.get("url", "")
        content = item.get("content", "")
        engine = item.get("engine", "")

        output.append(f"\n### 结果 {i}")
        output.append(f"标题: {title}")
        output.append(f"链接: {url}")
        if content:
            # 截断过长的内容
            content_short = content[:200] + "..." if len(content) > 200 else content
            output.append(f"摘要: {content_short}")
        if engine:
            output.append(f"来源: {engine}")

    return "\n".join(output)


def get_quick_result(result):
    """
    获取第一个结果的摘要（用于快速预览）

    Args:
        result: 搜索结果字典

    Returns:
        dict: 第一个结果或错误信息
    """
    if "error" in result:
        return result

    if "results" in result and result["results"]:
        item = result["results"][0]
        return {
            "title": item.get("title"),
            "url": item.get("url"),
            "content": item.get("content", "")[:500]
        }

    return {"error": "未找到结果"}


def main():
    """主程序入口"""
    # 设置 Windows 控制台编码
    import io
    if sys.platform == 'win32':
        sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

    args = sys.argv[1:]

    # 解析参数
    query = None
    instance = DEFAULT_INSTANCE
    proxy = None
    no_proxy = False
    json_output = False

    for arg in args:
        if arg == "--json" or arg == "-j":
            json_output = True
        elif arg == "--no-proxy":
            no_proxy = True
        elif arg.startswith("--proxy="):
            proxy = arg.split("=", 1)[1]
        elif arg == "--proxy":
            # 下一个参数是代理地址
            idx = args.index(arg)
            if idx + 1 < len(args) and not args[idx + 1].startswith("-"):
                proxy = args[idx + 1]
        elif arg.startswith("http"):
            instance = arg
        elif not arg.startswith("-") and query is None:
            query = arg

    if query is None:
        print("用法: python scripts/searxng_search.py \"<query>\" [instance] [--proxy URL] [--no-proxy]")
        print("\n公开实例列表:")
        for inst in PUBLIC_INSTANCES:
            print(f"  - {inst}")
        print("\n搜索引擎快捷语法:")
        for shortcut, engine in list(SEARCH_SHORTCUTS.items())[:8]:
            print(f"  {shortcut} - {engine}")
        print("\n代理选项:")
        print("  --proxy http://127.0.0.1:7890  使用指定代理")
        print("  --no-proxy                    禁用代理（自动检测也会被禁用）")
        sys.exit(1)

    # 检测代理
    proxies = get_proxies(proxy, no_proxy)
    proxy_info = "自动检测" if proxies and not proxy else (proxy if proxy else "无")

    print(f"[搜索] {query}")
    print(f"[实例] {instance}")
    if proxies:
        print(f"[代理] {proxy_info}")
    print("-" * 50)

    result = search_searxng(query, instance, proxy=proxy, no_proxy=no_proxy)

    if json_output:
        # JSON 输出模式
        print(json.dumps(result, indent=2, ensure_ascii=False))
    else:
        # 格式化输出
        print(format_results(result))

        # 输出统计信息
        if "results" in result:
            print(f"\n[统计] 共找到 {len(result['results'])} 个结果")


if __name__ == "__main__":
    main()
