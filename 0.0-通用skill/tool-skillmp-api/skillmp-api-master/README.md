# SkillsMP API Skill

[![License: ISC](https://img.shields.io/badge/License-ISC-blue.svg)](https://opensource.org/licenses/ISC)
[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)

[English](README.md) | [繁體中文](README_zh-TW.md)

A universal skill for searching and discovering AI skills from the [SkillsMP](https://skillsmp.com) marketplace. Compatible with all AI agents that support the SKILL format (Claude, Cursor, Windsurf, Antigravity, etc.).

## ✨ Features

- 🔍 **Keyword Search** - Fast keyword-based search of the SkillsMP library
- 🤖 **AI Semantic Search** - Intelligent semantic search powered by Cloudflare AI
- 📦 **Install Helper** - Automatically generate skill installation commands

## 📋 Prerequisites

- [Python](https://www.python.org/) 3.8 or higher
- [Node.js](https://nodejs.org/) (for `npx` command to install skills)
- [SkillsMP](https://skillsmp.com) account and API Key

## 🚀 Quick Start

### 1. Install Dependencies

```bash
pip install requests
```

> **Note**: `requests` is the only external dependency required.

### 2. Configure API Key

#### Option 1: Using Setup Script (Recommended)

```bash
python scripts/setup.py <YOUR_API_KEY>
```

#### Option 2: Create .env File Manually

Copy `.env.example` to `.env` and add your API Key:

```bash
cp .env.example .env
```

Edit the `.env` file:

```env
SKILLSMP_API_KEY=sk_live_skillsmp_xxxxxxxxxx
```

> **📍 Get Your API Key**  
> Visit the [SkillsMP API Settings](https://skillsmp.com/settings/api) page to obtain your API Key

## 📖 Usage

### Keyword Search

```bash
python scripts/search.py "<keyword>" [page] [per_page] [sort]
```

**Parameters:**

| Parameter | Required | Description |
|-----------|----------|-------------|
| keyword | ✓ | Search keyword |
| page | | Page number, default: 1 |
| per_page | | Items per page, default: 20, max: 100 |
| sort | | `stars` or `recent` |

**Examples:**

```bash
# Basic search
python scripts/search.py "SEO"

# With pagination and sorting
python scripts/search.py "web scraper" 1 10 stars
```

### AI Semantic Search

Use natural language for intelligent searching:

```bash
python scripts/ai_search.py "<query>"
```

**Examples:**

```bash
python scripts/ai_search.py "How to create a web scraper"
python scripts/ai_search.py "skills for building REST APIs"
```

### Install Helper

Search for skills and get installation command suggestions:

```bash
python scripts/install_helper.py "<keyword>" [limit]
```

**Examples:**

```bash
# Search for Spring Boot related skills
python scripts/install_helper.py "spring boot"

# Show top 10 results
python scripts/install_helper.py "react" 10
```

## 📂 Project Structure

```
skillmp-api/
├── scripts/
│   ├── search.py         # Keyword search script
│   ├── ai_search.py      # AI semantic search script
│   ├── install_helper.py # Installation helper tool
│   └── setup.py          # API Key setup script
├── .env.example          # Environment variables example
├── .gitignore            # Git ignore file
├── SKILL.md              # Skill documentation (for AI agents)
└── README.md             # This file
```

## 🔧 Skill Installation Workflow

> ⚠️ **Note**  
> SkillsMP skill IDs cannot be used directly with `npx add-skill`. Follow these steps:


1. **Search for skills**
   Use the helper script to find the repository and skill name:
   ```bash
   python scripts/install_helper.py "spring boot"
   ```

2. **Verify repository content**
   
   List all skills available in the repository:
   ```bash
   npx add-skill <owner>/<repo> --list
   ```

3. **Install the skill**

   Install specific skill to global scope (User-level):
   ```bash
   npx add-skill <owner>/<repo> --skill "<skill-name>" -g -a antigravity -y
   ```

   **Other Installation Options:**
   
   - Install ALL skills: `npx add-skill <owner>/<repo> -g -a antigravity -y`
   - Install to Local Project: `npx add-skill <owner>/<repo> --skill "<skill-name>" -a antigravity -y`


## 📦 API Response Format

### Success Response

```json
{
  "success": true,
  "data": {
    "skills": [...]
  }
}
```

### Error Response

```json
{
  "success": false,
  "error": {
    "code": "ERROR_CODE",
    "message": "Error message"
  }
}
```

## 🔐 Security Notes

- The `.env` file contains sensitive information and is excluded from Git via `.gitignore`
- Never share or expose your API Key publicly

## 🌐 Compatibility

This skill is compatible with all AI agents that support the SKILL format:

- **Claude** (Anthropic)
- **Cursor**
- **Windsurf**
- **Antigravity** (Google DeepMind)
- And more...

## 📄 License

This project is licensed under the [ISC License](https://opensource.org/licenses/ISC).

## 🔗 Related Links

- [SkillsMP Website](https://skillsmp.com)
- [SkillsMP API Documentation](https://skillsmp.com/docs/api)
- [add-skill CLI](https://www.npmjs.com/package/add-skill)
