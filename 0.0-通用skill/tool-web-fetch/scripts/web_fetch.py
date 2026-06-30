#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
网页抓取脚本（带反爬处理 + Clash 代理自适应）
用法: python scripts/web_fetch.py "<url>" [options]

参数:
    url         - 目标 URL (必填)
    --user-agent, -u  - 自定义 User-Agent
    --cookies, -c     - Cookie 字符串
    --timeout, -t     - 超时时间(秒)，默认 30
    --output, -o      - 输出文件路径
    --json            - 尝试解析为 JSON
    --proxy           - 自定义代理地址 (如 http://127.0.0.1:7890)
    --no-proxy        - 禁用代理

示例:
    python scripts/web_fetch.py "https://github.com/user/repo"
    python scripts/web_fetch.py "https://api.github.com/repos/user/repo" --json
    python scripts/web_fetch.py "https://example.com" -u chrome -o page.html
    python scripts/web_fetch.py "https://raw.githubusercontent.com/user/repo/main/README.md"
"""

import sys
import json
import argparse
import os
import gzip
from io import BytesIO

try:
    import requests
except ImportError:
    print("错误: 请先安装 requests 库")
    print("执行: pip install requests")
    sys.exit(1)

# ============================================
# Clash 代理自适应配置
# ============================================

# Clash 默认端口配置
CLASH_CONFIGS = {
    # Windows Clash 默认端口
    "clash_windows": {
        "http": "http://127.0.0.1:7890",
        "socks5": "socks5://127.0.0.1:7891"
    },
    # Clash Verge / Clash Meta
    "clash_verge": {
        "http": "http://127.0.0.1:7897",
        "socks5": "socks5://127.0.0.1:7898"
    },
    # Clash for Windows (CFW)
    "cfw": {
        "http": "http://127.0.0.1:7890",
        "socks5": "socks5://127.0.0.1:7891"
    },
    # macOS ClashX
    "clashx": {
        "http": "http://127.0.0.1:7890",
        "socks5": "socks5://127.0.0.1:7891"
    },
    # Linux Clash
    "clash_linux": {
        "http": "http://127.0.0.1:7890",
        "socks5": "socks5://127.0.0.1:7891"
    }
}

# 默认使用的代理类型
DEFAULT_PROXY_TYPE = "http"


def detect_clash_proxy():
    """
    自动检测 Clash 代理配置

    检测顺序:
    1. 环境变量 HTTP_PROXY / HTTPS_PROXY / ALL_PROXY
    2. Clash 默认端口 (7890/7891)
    3. Clash Verge 端口 (7897/7898)

    Returns:
        dict: 代理配置 {"http": ..., "https": ...} 或 None
    """
    proxies = {}

    # 1. 检查环境变量
    http_proxy = os.environ.get("HTTP_PROXY") or os.environ.get("http_proxy")
    https_proxy = os.environ.get("HTTPS_PROXY") or os.environ.get("https_proxy")
    all_proxy = os.environ.get("ALL_PROXY") or os.environ.get("all_proxy")

    if http_proxy:
        proxies["http"] = http_proxy
    if https_proxy:
        proxies["https"] = https_proxy
    if all_proxy:
        if not http_proxy:
            proxies["http"] = all_proxy
        if not https_proxy:
            proxies["https"] = all_proxy

    if proxies:
        return proxies

    # 2. 检测 Clash 默认端口是否可用
    clash_ports = [
        ("Clash 默认", 7890),
        ("Clash Verge", 7897),
        ("Clash Meta", 7890),
    ]

    for name, port in clash_ports:
        proxy_url = f"http://127.0.0.1:{port}"
        try:
            # 尝试连接代理端口
            import socket
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)
            result = sock.connect_ex(('127.0.0.1', port))
            sock.close()

            if result == 0:  # 端口开放
                print(f"[代理] 检测到 {name} 代理: {proxy_url}")
                return {
                    "http": proxy_url,
                    "https": proxy_url
                }
        except:
            pass

    # 3. 未检测到代理
    return None


def get_proxies(custom_proxy=None, no_proxy=False):
    """
    获取代理配置

    Args:
        custom_proxy: 自定义代理地址
        no_proxy: 是否禁用代理

    Returns:
        dict: 代理配置或 None
    """
    if no_proxy:
        return None

    if custom_proxy:
        return {
            "http": custom_proxy,
            "https": custom_proxy
        }

    # 自动检测
    return detect_clash_proxy()


# ============================================
# 常用 User-Agent 列表
# ============================================
USER_AGENTS = {
    "chrome": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "firefox": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:121.0) Gecko/20100101 Firefox/121.0",
    "safari": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.2 Safari/605.1.15",
    "edge": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0",
    "googlebot": "Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)",
    "curl": "curl/8.0",
    "bot": "Python-requests/2.31.0"
}

DEFAULT_USER_AGENT = USER_AGENTS["chrome"]


def fetch_url(url, user_agent=None, cookies=None, headers=None, timeout=30, allow_redirects=True, proxy=None, no_proxy=False):
    """
    抓取网页内容

    Args:
        url: 目标 URL
        user_agent: 自定义 User-Agent 或预设名称 (chrome/firefox/safari/edge/googlebot/curl/bot)
        cookies: Cookie 字符串或字典
        headers: 额外请求头字典
        timeout: 超时时间(秒)
        allow_redirects: 是否跟随重定向
        proxy: 自定义代理地址
        no_proxy: 是否禁用代理

    Returns:
        dict: 包含 status, content, headers, error 等字段
    """
    # 获取代理配置
    proxies = get_proxies(proxy, no_proxy)

    # 处理 User-Agent
    if user_agent and user_agent.lower() in USER_AGENTS:
        ua = USER_AGENTS[user_agent.lower()]
    else:
        ua = user_agent or DEFAULT_USER_AGENT

    # 构建请求头
    request_headers = {
        "User-Agent": ua,
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,application/json;q=0.8,*/*;q=0.7",
        "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
        "Accept-Encoding": "gzip, deflate",
        "Connection": "keep-alive",
        "Cache-Control": "max-age=0"
    }

    # 添加额外请求头
    if headers:
        request_headers.update(headers)

    # 处理 Cookie
    if cookies:
        if isinstance(cookies, dict):
            request_headers["Cookie"] = "; ".join(f"{k}={v}" for k, v in cookies.items())
        else:
            request_headers["Cookie"] = cookies

    try:
        response = requests.get(
            url,
            headers=request_headers,
            timeout=timeout,
            allow_redirects=allow_redirects,
            stream=True,
            proxies=proxies  # 添加代理支持
        )

        # 获取内容
        content = response.text

        return {
            "status": response.status_code,
            "content": content,
            "headers": dict(response.headers),
            "url": response.url,  # 最终 URL（可能有重定向）
            "encoding": response.encoding,
            "success": response.status_code == 200,
            "proxy_used": proxies is not None
        }

    except requests.exceptions.Timeout:
        return {"error": "请求超时", "error_type": "timeout", "success": False}
    except requests.exceptions.ConnectionError as e:
        return {"error": f"连接错误: {e}", "error_type": "connection", "success": False}
    except requests.exceptions.SSLError:
        return {"error": "SSL 证书错误", "error_type": "ssl", "success": False}
    except requests.exceptions.TooManyRedirects:
        return {"error": "重定向过多", "error_type": "redirects", "success": False}
    except Exception as e:
        return {"error": str(e), "error_type": "unknown", "success": False}


def fetch_github_raw(owner, repo, branch="main", path="README.md"):
    """
    获取 GitHub 文件原始内容

    Args:
        owner: 仓库所有者
        repo: 仓库名称
        branch: 分支名
        path: 文件路径

    Returns:
        str: 文件内容
    """
    url = f"https://raw.githubusercontent.com/{owner}/{repo}/{branch}/{path}"
    result = fetch_url(url)
    return result.get("content", "")


def fetch_github_api(endpoint):
    """
    调用 GitHub API

    Args:
        endpoint: API 端点 (如 repos/owner/repo)

    Returns:
        dict: JSON 响应
    """
    url = f"https://api.github.com/{endpoint}"
    result = fetch_url(url, headers={"Accept": "application/vnd.github.v3+json"})

    if result.get("success"):
        try:
            return json.loads(result["content"])
        except json.JSONDecodeError:
            return {"error": "JSON 解析失败"}
    return result


def extract_json(content):
    """
    尝试从内容中提取 JSON

    Args:
        content: 文本内容

    Returns:
        dict: 解析的 JSON 或错误信息
    """
    try:
        return json.loads(content)
    except json.JSONDecodeError:
        # 尝试查找 JSON 块
        import re
        json_pattern = r'\{[\s\S]*\}|\[[\s\S]*\]'
        matches = re.findall(json_pattern, content)
        if matches:
            try:
                return json.loads(matches[0])
            except:
                pass
        return {"error": "无法解析 JSON"}


def main():
    """主程序入口"""
    # 设置 Windows 控制台编码
    import io
    if sys.platform == 'win32':
        sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

    parser = argparse.ArgumentParser(
        description="网页抓取工具（带反爬处理）",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
示例:
  %(prog)s "https://github.com/user/repo"
  %(prog)s "https://api.github.com/repos/user/repo" --json
  %(prog)s "https://example.com" -u chrome -o page.html
  %(prog)s "https://raw.githubusercontent.com/user/repo/main/README.md"

预设 User-Agent:
  chrome, firefox, safari, edge, googlebot, curl, bot
        """
    )

    parser.add_argument("url", help="目标 URL")
    parser.add_argument("--user-agent", "-u", help="自定义 User-Agent 或预设名称")
    parser.add_argument("--cookies", "-c", help="Cookie 字符串")
    parser.add_argument("--timeout", "-t", type=int, default=30, help="超时时间(秒)")
    parser.add_argument("--output", "-o", help="输出文件路径")
    parser.add_argument("--json", action="store_true", help="解析为 JSON 输出")
    parser.add_argument("--headers", help="额外请求头 (JSON 格式)")
    parser.add_argument("--summary", "-s", action="store_true", help="只显示摘要")
    parser.add_argument("--proxy", "-p", help="自定义代理地址 (如 http://127.0.0.1:7890)")
    parser.add_argument("--no-proxy", action="store_true", help="禁用代理")

    args = parser.parse_args()

    # 解析额外请求头
    extra_headers = None
    if args.headers:
        try:
            extra_headers = json.loads(args.headers)
        except:
            print("警告: 无法解析 headers 参数")

    print(f"[抓取] {args.url}")
    if args.user_agent:
        print(f"[User-Agent] {args.user_agent}")
    if args.proxy:
        print(f"[代理] {args.proxy}")
    elif args.no_proxy:
        print("[代理] 已禁用")
    print("-" * 50)

    result = fetch_url(
        args.url,
        user_agent=args.user_agent,
        cookies=args.cookies,
        headers=extra_headers,
        timeout=args.timeout,
        proxy=args.proxy,
        no_proxy=args.no_proxy
    )

    if not result.get("success"):
        print(f"[错误] {result.get('error', '未知错误')}")
        sys.exit(1)

    # 处理输出
    if args.json:
        try:
            data = json.loads(result["content"])
            output = json.dumps(data, indent=2, ensure_ascii=False)
        except json.JSONDecodeError:
            print("[警告] 响应不是有效的 JSON")
            output = result["content"][:1000]
    elif args.summary:
        # 显示摘要
        content = result["content"]
        lines = content.split("\n")[:20]
        output = "\n".join(lines)
        print(f"[状态码] {result['status']}")
        print(f"[内容长度] {len(content)} 字符")
        print(f"[最终URL] {result.get('url', args.url)}")
        print("-" * 50)
    else:
        output = result["content"]

    # 写入文件或输出
    if args.output:
        with open(args.output, "w", encoding="utf-8") as f:
            f.write(output)
        print(f"[已保存] {args.output}")
    else:
        print(output)


if __name__ == "__main__":
    main()
