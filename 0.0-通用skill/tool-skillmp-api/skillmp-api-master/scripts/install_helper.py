#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
SkillsMP 技能安裝查詢腳本
搜尋技能並提供安裝指令

用法: python install_helper.py <query> [limit]

參數:
    query - 搜尋關鍵字 (必填)
    limit - 顯示筆數，預設 5
"""

import sys
import json
import os
import re
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


def parse_github_url(github_url):
    """
    從 GitHub URL 解析 owner/repo
    
    Args:
        github_url: GitHub 儲存庫 URL
    
    Returns:
        dict 或 None: 包含 owner, repo, fullPath 的字典
    """
    if not github_url:
        return None
    
    # 格式: https://github.com/owner/repo/tree/branch/path
    match = re.search(r"github\.com/([^/]+)/([^/]+)", github_url)
    if not match:
        return None
    
    owner = match.group(1)
    repo = match.group(2)
    
    return {
        "owner": owner,
        "repo": repo,
        "fullPath": f"{owner}/{repo}"
    }


def search_skills(query, limit=5):
    """
    執行關鍵字搜尋
    
    Args:
        query: 搜尋關鍵字
        limit: 每頁筆數
    
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
    
    url = f"{API_BASE_URL}/api/v1/skills/search"
    params = {
        "q": query,
        "page": 1,
        "limit": limit,
        "sortBy": "stars"
    }
    
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


def select_agent():
    """
    讓使用者選擇目標 Agent
    
    Returns:
        str: 選擇的 Agent 識別符
    """
    agents = {
        "1": ("antigravity", "Antigravity (Google DeepMind)"),
        "2": ("claude-code", "Claude Code (Anthropic)"),
        "3": ("cursor", "Cursor"),
        "4": ("roo", "Roo Code"),
        "5": ("github-copilot", "GitHub Copilot"),
        "a": ("all", "列出所有 Agent 指令")
    }
    
    print("請問要安裝到哪個 Agent 環境？")
    for key, (agent_id, name) in agents.items():
        print(f"  [{key}] {name}")
    print("  [q] 離開")
    
    while True:
        choice = input("\n請選擇 (預設 1): ").strip().lower()
        
        if not choice:
            return "antigravity"
        
        if choice == 'q':
            sys.exit(0)
            
        if choice in agents:
            return agents[choice][0]
            
        print("❌ 無效的選擇，請重試")


def generate_install_command(repo_path, skill_name=None, agent_id="antigravity"):
    """
    生成安裝指令
    
    Args:
        repo_path: 儲存庫路徑 (owner/repo)
        skill_name: 技能名稱 (可選)
        agent_id: Agent ID
    
    Returns:
        list: 指令列表
    """
    commands = []
    
    # 定義 Agent ID 列表
    target_agents = [agent_id]
    if agent_id == "all":
        target_agents = ["antigravity", "claude-code", "cursor"]
    
    for agent in target_agents:
        agent_flag = f"-a {agent}"
        agent_name = agent.capitalize()
        
        if skill_name:
            cmd = f'npx add-skill {repo_path} --skill "{skill_name}" -g {agent_flag} -y'
            desc = f"# 安裝到 {agent_name} (全域)"
        else:
            cmd = f'npx add-skill {repo_path} -g {agent_flag} -y'
            desc = f"# 安裝所有技能到 {agent_name} (全域)"
            
        commands.append((desc, cmd))
        
    return commands


def format_output(skills):
    """
    格式化輸出技能資訊
    
    Args:
        skills: 技能列表
    """
    print("\n=== 搜尋結果 ===\n")
    
    # 收集所有唯一的儲存庫
    repos = {}
    
    for index, skill in enumerate(skills):
        parsed = parse_github_url(skill.get("githubUrl"))
        
        name = skill.get("name") or skill.get("id", "Unknown")
        author = skill.get("author", "Unknown")
        stars = skill.get("stars", 0)
        description = skill.get("description", "")
        
        print(f"【{index + 1}】{name}")
        print(f"    作者: {author}")
        print(f"    ⭐ Stars: {stars}")
        
        if description:
            desc = description[:80] + "..." if len(description) > 80 else description
            print(f"    說明: {desc}")
        
        if parsed:
            print(f"    GitHub: {skill.get('githubUrl')}")
            
            # 記錄儲存庫
            full_path = parsed["fullPath"]
            if full_path not in repos:
                repos[full_path] = []
            repos[full_path].append(name)
        else:
            skill_url = skill.get("skillUrl", "")
            if skill_url:
                print(f"    SkillsMP: {skill_url}")
        
        print()
    
    # 輸出快速安裝指令
    if repos:
        # 詢問目標 Agent
        selected_agent = select_agent()
        
        print("\n=== 快速安裝指令 ===\n")
        
        for repo_path, skill_names in repos.items():
            print(f"📦 儲存庫: {repo_path}")
            print(f"📋 列出可用技能: npx add-skill {repo_path} --list\n")
            
            # 安裝所有技能指令
            print(f"⬇️  安裝該儲存庫所有技能:")
            for desc, cmd in generate_install_command(repo_path, agent_id=selected_agent):
                print(f"  {cmd}")
            print()
            
            if skill_names:
                print(f"⬇️  安裝特定技能:")
                for name in skill_names:
                    for desc, cmd in generate_install_command(repo_path, name, selected_agent):
                        print(f"  {cmd}")
            print("-" * 40 + "\n")


def main():
    """主程式入口"""
    args = sys.argv[1:]
    
    if len(args) == 0:
        print("SkillsMP 技能安裝查詢工具")
        print()
        print("用法: python install_helper.py <query> [limit]")
        print()
        print("範例:")
        print('  python install_helper.py "spring boot"')
        print('  python install_helper.py "react" 10')
        sys.exit(1)
    
    # 檢查 API Key
    if not get_api_key():
        print("錯誤: 請設定環境變數 SKILLSMP_API_KEY")
        print("提示: 複製 .env.example 為 .env 並填入您的 API key")
        sys.exit(1)
    
    query = args[0]
    limit = int(args[1]) if len(args) > 1 else 5
    
    print(f'正在搜尋: "{query}" (顯示前 {limit} 筆，依 Stars 排序)')
    
    result = search_skills(query, limit)
    
    if not result.get("success"):
        error_msg = result.get("error", {}).get("message", "未知錯誤")
        print(f"搜尋失敗: {error_msg}")
        sys.exit(1)
    
    skills = result.get("data", {}).get("skills", [])
    
    if not skills:
        print("找不到相關技能")
        sys.exit(0)
    
    format_output(skills)
    
    total = result.get("data", {}).get("pagination", {}).get("total", len(skills))
    print(f"總共找到 {total} 個相關技能")


if __name__ == "__main__":
    main()
