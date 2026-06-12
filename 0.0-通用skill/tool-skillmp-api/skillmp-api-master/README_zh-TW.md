# SkillsMP API Skill

[![License: ISC](https://img.shields.io/badge/License-ISC-blue.svg)](https://opensource.org/licenses/ISC)
[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)

[English](README.md) | [繁體中文](README_zh-TW.md)

專為 [SkillsMP](https://skillsmp.com) 技能市場打造的通用搜尋與安裝工具。相容於所有支援 SKILL 格式的 AI 代理（如 Claude、Cursor、Windsurf、Antigravity 等）。

## ✨ 功能特色

- 🔍 **關鍵字搜尋** - 快速搜尋 SkillsMP 技能庫
- 🤖 **AI 語意搜尋** - 使用 Cloudflare AI 進行智慧語意搜尋
- 📦 **安裝輔助工具** - 自動生成技能安裝指令
- ⚡ **一鍵安裝** - 整合 `add-skill` CLI，支援從 GitHub 直接安裝技能

## 📋 前置需求

- [Python](https://www.python.org/) 3.8 或更高版本
- [Node.js](https://nodejs.org/) (用於執行 `npx` 指令安裝技能)
- [SkillsMP](https://skillsmp.com) 帳號與 API Key

## 🚀 快速開始

### 1. 安裝依賴

```bash
pip install requests
```

> **注意**：`requests` 是唯一需要的外部依賴。

### 2. 設定 API Key

#### 方式一：使用設定腳本（推薦）

```bash
python scripts/setup.py <YOUR_API_KEY>
```

#### 方式二：手動建立 .env 檔案

複製 `.env.example` 為 `.env` 並填入您的 API Key：

```bash
cp .env.example .env
```

編輯 `.env` 檔案：

```env
SKILLSMP_API_KEY=sk_live_skillsmp_xxxxxxxxxx
```

> **📍 取得 API Key**  
> 前往 [SkillsMP API 設定頁面](https://skillsmp.com/settings/api) 取得您的 API Key

## 📖 使用方式

### 關鍵字搜尋

```bash
python scripts/search.py "<關鍵字>" [頁碼] [每頁筆數] [排序方式]
```

**參數說明：**

| 參數 | 必填 | 說明 |
|------|------|------|
| 關鍵字 | ✓ | 搜尋關鍵字 |
| 頁碼 | | 頁碼，預設 1 |
| 每頁筆數 | | 每頁筆數，預設 20，最大 100 |
| 排序方式 | | `stars` 或 `recent` |

**範例：**

```bash
# 基本搜尋
python scripts/search.py "SEO"

# 指定分頁與排序
python scripts/search.py "web scraper" 1 10 stars
```

### AI 語意搜尋

使用自然語言進行智慧搜尋：

```bash
python scripts/ai_search.py "<查詢內容>"
```

**範例：**

```bash
python scripts/ai_search.py "如何建立網頁爬蟲"
python scripts/ai_search.py "建立 REST API 的技能"
```

### 安裝輔助工具

搜尋技能並取得安裝指令建議：

```bash
python scripts/install_helper.py "<關鍵字>" [顯示筆數]
```

**範例：**

```bash
# 搜尋 Spring Boot 相關技能
python scripts/install_helper.py "spring boot"

# 顯示前 10 筆結果
python scripts/install_helper.py "react" 10
```

## 🔧 技能安裝流程

> ⚠️ **注意**  
> SkillsMP 的技能 ID 無法直接用於 `npx add-skill` 安裝。請按照以下步驟操作：

1. **搜尋技能**
   
   使用輔助腳本找到儲存庫與技能名稱：
   ```bash
   python scripts/install_helper.py "spring boot"
   ```

2. **確認儲存庫內容**
   
   列出儲存庫中的所有可用技能：
   ```bash
   npx add-skill <owner>/<repo> --list
   ```

3. **安裝技能**

   安裝特定技能到全域（User-level）：
   ```bash
   npx add-skill <owner>/<repo> --skill "<skill-name>" -g -a antigravity -y
   ```

   **其他安裝選項：**
   
   - 安裝該儲存庫**所有**技能：`npx add-skill <owner>/<repo> -g -a antigravity -y`
   - 安裝到**目前專案**（Local）：`npx add-skill <owner>/<repo> --skill "<skill-name>" -a antigravity -y`

4. **驗證安裝**
   檢查 Agent 的技能目錄，確認檔案已成功建立。

## 📦 API 回應格式

### 成功回應

```json
{
  "success": true,
  "data": {
    "skills": [...]
  }
}
```

### 錯誤回應

```json
{
  "success": false,
  "error": {
    "code": "ERROR_CODE",
    "message": "錯誤訊息"
  }
}
```

## 🔐 安全性注意事項

- `.env` 檔案包含敏感資訊，已被加入 `.gitignore`，不會上傳到 GitHub
- 請妥善保管您的 API Key，切勿公開分享

## 🌐 相容性

此 Skill 相容於所有支援 SKILL 格式的 AI 代理：

- **Claude** (Anthropic)
- **Cursor**
- **Windsurf**
- **Antigravity** (Google DeepMind)
- 以及更多...

### 支援的 Agent 識別符

| Agent | 識別名稱 | 全域技能目錄 |
|-------|----------|--------------|
| **Antigravity** | `antigravity` | `~/.gemini/antigravity/skills/` |
| **Claude Code** | `claude-code` | `~/.claude/skills/` |
| **Cursor** | `cursor` | `.cursor/skills/` |
| **Codex** | `codex` | `.codex/skills/` |
| **OpenCode** | `opencode` | `.opencode/skills/` |
| **GitHub Copilot** | `github-copilot` | `.github/copilot/skills/` |
| **Roo Code** | `roo` | `.roo/skills/` |

## 📄 授權

本專案採用 [ISC License](https://opensource.org/licenses/ISC) 授權。

## 🔗 相關連結

- [SkillsMP 官網](https://skillsmp.com)
- [SkillsMP API 文件](https://skillsmp.com/docs/api)
- [add-skill CLI](https://www.npmjs.com/package/add-skill)
