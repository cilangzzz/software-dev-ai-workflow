#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
SkillsMP API Key 設定腳本
用於設定 .env 檔案中的 API Key

用法: python setup.py <api_key>

參數:
    api_key - SkillsMP API Key (必填)
"""

import sys
import re
from pathlib import Path


def is_valid_api_key_format(api_key):
    """
    驗證 API Key 格式
    
    Args:
        api_key: 要驗證的 API Key
    
    Returns:
        bool: 是否為有效格式
    """
    # SkillsMP API Key 格式: sk_live_skillsmp_...
    pattern = r"^sk_live_skillsmp_[a-zA-Z0-9]+$"
    return bool(re.match(pattern, api_key))


def setup_env_file(api_key):
    """
    建立或更新 .env 檔案
    
    Args:
        api_key: 要儲存的 API Key
    """
    env_path = Path(__file__).parent.parent / ".env"
    env_content = f"""# SkillsMP API 設定
SKILLSMP_API_KEY={api_key}
"""
    
    try:
        with open(env_path, "w", encoding="utf-8") as f:
            f.write(env_content)
        
        print("✅ API Key 設定成功！")
        print(f"📁 已儲存至: {env_path}")
        print()
        print("現在您可以執行搜尋腳本：")
        print('  python scripts/search.py "關鍵字"')
        print('  python scripts/ai_search.py "查詢內容"')
    except IOError as e:
        print(f"❌ 寫入 .env 檔案失敗: {e}")
        sys.exit(1)


def main():
    """主程式入口"""
    args = sys.argv[1:]
    
    # 檢查必填參數
    if len(args) == 0:
        print("SkillsMP API Key 設定工具")
        print()
        print("用法: python scripts/setup.py <api_key>")
        print()
        print("如何取得 API Key:")
        print("  1. 前往 https://skillsmp.com 並登入/註冊帳號")
        print("  2. 進入 https://skillsmp.com/settings/api 取得您的 API Key")
        print("  3. API Key 格式為 sk_live_skillsmp_...")
        print()
        print("範例:")
        print("  python scripts/setup.py sk_live_skillsmp_您的金鑰")
        sys.exit(1)
    
    api_key = args[0]
    
    # 驗證 API Key 格式
    if not is_valid_api_key_format(api_key):
        print("❌ API Key 格式無效")
        print("   正確格式: sk_live_skillsmp_...")
        print(f"   您輸入的: {api_key}")
        sys.exit(1)
    
    # 設定 .env 檔案
    setup_env_file(api_key)


if __name__ == "__main__":
    main()
