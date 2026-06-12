#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
SkillsMP 關鍵字搜尋腳本
使用關鍵字搜尋 SkillsMP 技能市場

用法: python search.py <query> [page] [limit] [sortBy]

參數:
    query  - 搜尋關鍵字 (必填)
    page   - 頁碼，預設 1
    limit  - 每頁筆數，預設 20，最大 100
    sortBy - 排序方式，可選 'stars' 或 'recent'
"""

import sys
import json
import os
from pathlib import Path

# 嘗試導入 requests，如果沒有則提示安裝
try:
    import requests
except ImportError:
    print("錯誤: 請先安裝 requests 套件")
    print("執行: pip install requests")
    sys.exit(1)


# API 設定
API_BASE_URL = "https://skillsmp.com"


def load_env():
    """
    從 .env 檔案載入環境變數
    
    Returns:
        dict: 環境變數字典
    """
    env_path = Path(__file__).parent.parent / ".env"
    env_vars = {}
    
    if env_path.exists():
        with open(env_path, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                # 跳過空行和註解
                if not line or line.startswith("#"):
                    continue
                # 解析 KEY=VALUE 格式
                if "=" in line:
                    key, value = line.split("=", 1)
                    env_vars[key.strip()] = value.strip()
    
    return env_vars


def get_api_key():
    """
    取得 API Key，優先從環境變數，其次從 .env 檔案
    
    Returns:
        str: API Key
    """
    # 優先從系統環境變數讀取
    api_key = os.environ.get("SKILLSMP_API_KEY")
    
    # 如果沒有，從 .env 檔案讀取
    if not api_key:
        env_vars = load_env()
        api_key = env_vars.get("SKILLSMP_API_KEY")
    
    return api_key


def search_skills(query, page=1, limit=20, sort_by=None):
    """
    執行關鍵字搜尋
    
    Args:
        query: 搜尋關鍵字
        page: 頁碼
        limit: 每頁筆數
        sort_by: 排序方式 ('stars' 或 'recent')
    
    Returns:
        dict: 搜尋結果
    """
    api_key = get_api_key()
    
    if not api_key:
        return {
            "success": False,
            "error": {
                "code": "NO_API_KEY",
                "message": "請設定環境變數 SKILLSMP_API_KEY"
            }
        }
    
    # 建立請求參數
    params = {
        "q": query,
        "page": page,
        "limit": limit
    }
    
    # 加入可選的排序參數
    if sort_by and sort_by in ["stars", "recent"]:
        params["sortBy"] = sort_by
    
    url = f"{API_BASE_URL}/api/v1/skills/search"
    
    try:
        response = requests.get(
            url,
            params=params,
            headers={"Authorization": f"Bearer {api_key}"}
        )
        
        return response.json()
    except requests.RequestException as e:
        return {
            "success": False,
            "error": {
                "code": "FETCH_ERROR",
                "message": str(e)
            }
        }


def main():
    """主程式入口"""
    args = sys.argv[1:]
    
    # 檢查必填參數
    if len(args) == 0:
        print("錯誤: 請提供搜尋關鍵字")
        print("用法: python search.py <query> [page] [limit] [sortBy]")
        sys.exit(1)
    
    # 檢查 API Key
    if not get_api_key():
        print("錯誤: 請設定環境變數 SKILLSMP_API_KEY")
        print("提示: 複製 .env.example 為 .env 並填入您的 API key")
        sys.exit(1)
    
    # 解析參數
    query = args[0]
    page = int(args[1]) if len(args) > 1 else 1
    limit = int(args[2]) if len(args) > 2 else 20
    sort_by = args[3] if len(args) > 3 else None
    
    print(f'正在搜尋: "{query}"')
    print(f"參數: 頁碼={page}, 每頁={limit}, 排序={sort_by or '預設'}")
    print("---")
    
    result = search_skills(query, page, limit, sort_by)
    
    # 輸出結果
    print(json.dumps(result, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
