#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
测试多个搜索引擎 API 的可用性
"""

import sys
import json
import time
import io

# Windows 编码处理
if sys.platform == 'win32':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

import requests

# Clash 代理配置
PROXIES = {
    "http": "http://127.0.0.1:7897",
    "https": "http://127.0.0.1:7897"
}

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

TEST_QUERY = "python web framework"

# 搜索引擎 API 配置
SEARCH_APIS = [
    {
        "name": "SearXNG (searx.be)",
        "url": "https://searx.be/search",
        "params": {"q": TEST_QUERY, "format": "json"},
        "method": "GET",
        "need_api_key": False
    },
    {
        "name": "SearXNG (search.bus-hit.me)",
        "url": "https://search.bus-hit.me/search",
        "params": {"q": TEST_QUERY, "format": "json"},
        "method": "GET",
        "need_api_key": False
    },
    {
        "name": "SearXNG (searx.fmac.xyz)",
        "url": "https://searx.fmac.xyz/search",
        "params": {"q": TEST_QUERY, "format": "json"},
        "method": "GET",
        "need_api_key": False
    },
    {
        "name": "SearXNG (search.sapti.me)",
        "url": "https://search.sapti.me/search",
        "params": {"q": TEST_QUERY, "format": "json"},
        "method": "GET",
        "need_api_key": False
    },
    {
        "name": "DuckDuckGo Instant Answer API",
        "url": "https://api.duckduckgo.com/",
        "params": {"q": TEST_QUERY, "format": "json", "no_html": 1, "skip_disambig": 1},
        "method": "GET",
        "need_api_key": False
    },
    {
        "name": "GitHub Search API",
        "url": "https://api.github.com/search/repositories",
        "params": {"q": TEST_QUERY, "sort": "stars", "per_page": 5},
        "method": "GET",
        "need_api_key": False,
        "headers": {"Accept": "application/vnd.github.v3+json"}
    },
    {
        "name": "Wikipedia API",
        "url": "https://en.wikipedia.org/w/api.php",
        "params": {"action": "query", "list": "search", "srsearch": TEST_QUERY, "format": "json", "srlimit": 5},
        "method": "GET",
        "need_api_key": False
    },
    {
        "name": "Wikipedia 中文API",
        "url": "https://zh.wikipedia.org/w/api.php",
        "params": {"action": "query", "list": "search", "srsearch": TEST_QUERY, "format": "json", "srlimit": 5},
        "method": "GET",
        "need_api_key": False
    },
    {
        "name": "Stack Overflow API",
        "url": "https://api.stackexchange.com/2.3/search",
        "params": {"intitle": "python web framework", "site": "stackoverflow", "pagesize": 5, "sort": "votes"},
        "method": "GET",
        "need_api_key": False
    },
    {
        "name": "Hacker News API",
        "url": "https://hn.algolia.com/api/v1/search",
        "params": {"query": TEST_QUERY, "hitsPerPage": 5},
        "method": "GET",
        "need_api_key": False
    },
    {
        "name": "Reddit API (无需认证)",
        "url": f"https://www.reddit.com/search.json",
        "params": {"q": TEST_QUERY, "limit": 5, "sort": "relevance"},
        "method": "GET",
        "need_api_key": False
    },
    {
        "name": "Brave Search API (需API Key)",
        "url": "https://api.search.brave.com/res/v1/web/search",
        "params": {"q": TEST_QUERY},
        "method": "GET",
        "need_api_key": True,
        "note": "需要 API Key: https://brave.com/search/api/"
    },
    {
        "name": "Bing Search API (需API Key)",
        "url": "https://api.bing.microsoft.com/v7.0/search",
        "params": {"q": TEST_QUERY},
        "method": "GET",
        "need_api_key": True,
        "note": "需要 Azure API Key"
    },
    {
        "name": "Google Custom Search (需API Key)",
        "url": "https://www.googleapis.com/customsearch/v1",
        "params": {"q": TEST_QUERY, "cx": "YOUR_SEARCH_ENGINE_ID"},
        "method": "GET",
        "need_api_key": True,
        "note": "需要 API Key 和 Search Engine ID"
    },
    {
        "name": "Serper API (Google代理)",
        "url": "https://google.serper.dev/search",
        "params": {"q": TEST_QUERY},
        "method": "POST",
        "need_api_key": True,
        "note": "免费: 2500次/月 https://serper.dev/"
    },
    {
        "name": "Tavily API (AI搜索)",
        "url": "https://api.tavily.com/search",
        "params": {"query": TEST_QUERY},
        "method": "POST",
        "need_api_key": True,
        "note": "免费: 1000次/月 https://tavily.com/"
    },
    {
        "name": "Jina AI Reader API",
        "url": f"https://r.jina.ai/{TEST_QUERY}",
        "params": {},
        "method": "GET",
        "need_api_key": False,
        "note": "URL前缀读取网页内容"
    }
]


def test_api(api_config, use_proxy=True):
    """
    测试单个 API

    Returns:
        dict: 测试结果
    """
    result = {
        "name": api_config["name"],
        "status": "unknown",
        "response_time": 0,
        "results_count": 0,
        "error": None,
        "sample_result": None
    }

    if api_config["need_api_key"]:
        result["status"] = "need_api_key"
        result["error"] = api_config.get("note", "需要 API Key")
        return result

    proxies = PROXIES if use_proxy else None
    headers = HEADERS.copy()
    if api_config.get("headers"):
        headers.update(api_config["headers"])

    start_time = time.time()

    try:
        if api_config["method"] == "GET":
            response = requests.get(
                api_config["url"],
                params=api_config["params"],
                headers=headers,
                proxies=proxies,
                timeout=15
            )
        elif api_config["method"] == "POST":
            response = requests.post(
                api_config["url"],
                json=api_config["params"],
                headers=headers,
                proxies=proxies,
                timeout=15
            )

        result["response_time"] = round(time.time() - start_time, 2)

        if response.status_code == 200:
            data = response.json()
            result["status"] = "success"

            # 尝试提取结果数量和示例
            if "results" in data:
                result["results_count"] = len(data.get("results", []))
                if data["results"]:
                    item = data["results"][0]
                    result["sample_result"] = item.get("title", item.get("name", str(item)[:100]))
            elif "items" in data:
                result["results_count"] = len(data.get("items", []))
                if data["items"]:
                    item = data["items"][0]
                    result["sample_result"] = item.get("full_name", item.get("name", str(item)[:100]))
            elif "query" in data and "search" in data.get("query", {}):
                # Wikipedia format
                search_results = data.get("query", {}).get("search", [])
                result["results_count"] = len(search_results)
                if search_results:
                    result["sample_result"] = search_results[0].get("title", "")
            elif "Abstract" in data:
                # DuckDuckGo
                result["sample_result"] = data.get("Abstract", "")[:100]
                result["results_count"] = 1 if data.get("Abstract") else 0
            elif "total_count" in data:
                result["results_count"] = data.get("total_count", 0)
                if "items" in data:
                    result["sample_result"] = data["items"][0].get("full_name", "")
            elif "hits" in data:
                # Hacker News / Algolia
                hits = data.get("hits", [])
                result["results_count"] = len(hits)
                if hits:
                    result["sample_result"] = hits[0].get("title", "")
            elif "data" in data and "children" in data.get("data", {}):
                # Reddit
                children = data["data"]["children"]
                result["results_count"] = len(children)
                if children:
                    result["sample_result"] = children[0]["data"].get("title", "")
            elif "items" in data:
                # Stack Overflow
                items = data.get("items", [])
                result["results_count"] = len(items)
                if items:
                    result["sample_result"] = items[0].get("title", "")
            else:
                result["results_count"] = 1
                result["sample_result"] = str(data)[:100]

        elif response.status_code == 403:
            result["status"] = "forbidden"
            result["error"] = "403 Forbidden"
        elif response.status_code == 401:
            result["status"] = "unauthorized"
            result["error"] = "401 Unauthorized"
        elif response.status_code == 429:
            result["status"] = "rate_limit"
            result["error"] = "429 Rate Limited"
        else:
            result["status"] = "http_error"
            result["error"] = f"HTTP {response.status_code}"

    except requests.exceptions.Timeout:
        result["status"] = "timeout"
        result["error"] = "请求超时 (>15s)"
        result["response_time"] = 15
    except requests.exceptions.ConnectionError as e:
        result["status"] = "connection_error"
        result["error"] = "连接失败"
    except json.JSONDecodeError:
        result["status"] = "parse_error"
        result["error"] = "JSON 解析失败"
    except Exception as e:
        result["status"] = "error"
        result["error"] = str(e)[:50]

    return result


def main():
    """主测试函数"""
    print("=" * 60)
    print("搜索引擎 API 可用性测试")
    print("=" * 60)
    print(f"测试关键词: {TEST_QUERY}")
    print(f"代理: {PROXIES['http']}")
    print("=" * 60)
    print()

    results = []

    for api in SEARCH_APIS:
        print(f"测试: {api['name']}...")
        result = test_api(api)
        results.append(result)

        # 显示结果
        status_icon = {
            "success": "[OK]",
            "forbidden": "[403]",
            "timeout": "[TIMEOUT]",
            "connection_error": "[FAIL]",
            "need_api_key": "[KEY]",
            "http_error": "[ERR]",
            "rate_limit": "[LIMIT]",
            "unauthorized": "[AUTH]",
            "parse_error": "[PARSE]",
            "error": "[ERR]",
            "unknown": "[???]"
        }.get(result["status"], "[???]")

        print(f"  {status_icon} 状态: {result['status']}")
        print(f"  耗时: {result['response_time']}s")
        if result["results_count"]:
            print(f"  结果数: {result['results_count']}")
        if result["sample_result"]:
            print(f"  示例: {result['sample_result'][:80]}")
        if result["error"]:
            print(f"  错误: {result['error']}")
        print()

        # 延迟避免被封
        time.sleep(0.5)

    # 汇总报告
    print("=" * 60)
    print("测试汇总")
    print("=" * 60)

    success_count = sum(1 for r in results if r["status"] == "success")
    need_key_count = sum(1 for r in results if r["status"] == "need_api_key")
    fail_count = sum(1 for r in results if r["status"] not in ["success", "need_api_key"])

    print(f"成功: {success_count}")
    print(f"需要API Key: {need_key_count}")
    print(f"失败: {fail_count}")
    print()

    # 可用的 API
    print("=" * 60)
    print("可立即使用的 API:")
    print("=" * 60)
    for r in results:
        if r["status"] == "success":
            print(f"  [OK] {r['name']}")
            print(f"       耗时: {r['response_time']}s | 结果: {r['results_count']}")
            if r["sample_result"]:
                print(f"       示例: {r['sample_result'][:60]}")
            print()

    print("=" * 60)
    print("需要 API Key 的 API:")
    print("=" * 60)
    for r in results:
        if r["status"] == "need_api_key":
            print(f"  [KEY] {r['name']}")
            print(f"        {r['error']}")
            print()


if __name__ == "__main__":
    main()
