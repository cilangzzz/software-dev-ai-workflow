#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
SkillsMP AI 語意搜尋腳本
使用 AI 語意搜尋 SkillsMP 技能市場 (Cloudflare AI 驅動)

用法: python ai_search.py <query>

參數:
    query - AI 搜尋查詢 (必填)
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


def ai_search_skills(query):
    """
    執行 AI 語意搜尋
    
    Args:
        query: AI 搜尋查詢
    
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
    
    url = f"{API_BASE_URL}/api/v1/skills/ai-search"
    
    try:
        response = requests.get(
            url,
            params={"q": query},
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
        print("錯誤: 請提供 AI 搜尋查詢")
        print("用法: python ai_search.py <query>")
        sys.exit(1)
    
    # 檢查 API Key
    if not get_api_key():
        print("錯誤: 請設定環境變數 SKILLSMP_API_KEY")
        print("提示: 複製 .env.example 為 .env 並填入您的 API key")
        sys.exit(1)
    
    # 合併所有參數作為查詢字串（支援空格）
    query = " ".join(args)
    
    print(f'正在進行 AI 語意搜尋: "{query}"')
    print("---")
    
    result = ai_search_skills(query)
    
    # 輸出結果
    print(json.dumps(result, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
