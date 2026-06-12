---
name: SkillsMP API
description: Search and discover AI skills from the SkillsMP marketplace
---

# SkillsMP API Skill

This skill provides search functionality for the SkillsMP skill marketplace, supporting both keyword search and AI semantic search.

## Prerequisites

- **Python** 3.8 or higher
- **requests** library (`pip install requests`)
- **SkillsMP API Key** from [skillsmp.com/settings/api](https://skillsmp.com/settings/api)

## Installation

First-time setup requires installing the requests library:

```bash
pip install requests
```

> [!NOTE]
> This step only needs to be run once. Python's requests library is the only external dependency required.

## API Key Configuration

### Check if API Key is configured

Before running any search script, check if `.env` file exists:

```bash
# Check if .env exists
test -f .env && echo "Configured" || echo "Not configured"
```

### Setup API Key

**Option 1: Using setup script (Recommended)**

```bash
python scripts/setup.py <API_KEY>
```

**Option 2: Create .env file directly**

Create a `.env` file with the following content:

```env
SKILLSMP_API_KEY=sk_live_skillsmp_xxxxxxxxxx
```

> [!TIP]
> Get your API Key from [SkillsMP API Settings](https://skillsmp.com/settings/api)

---

## Features

### 1. Keyword Search

Search the skill library using keywords.

**Usage:**
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

---

### 2. AI Semantic Search

Use AI-powered semantic search (Cloudflare AI).

**Usage:**
```bash
python scripts/ai_search.py "<query>"
```

**Parameters:**

| Parameter | Required | Description |
|-----------|----------|-------------|
| query | ✓ | Natural language query |

**Examples:**
```bash
python scripts/ai_search.py "How to create a web scraper"
python scripts/ai_search.py "skills for building REST APIs"
```

---

### 3. Install Helper

Search skills and get installation command suggestions.

**Usage:**
```bash
python scripts/install_helper.py "<keyword>" [limit]
```

**Parameters:**

| Parameter | Required | Description |
|-----------|----------|-------------|
| keyword | ✓ | Skill keyword to search |
| limit | | Number of results to show, default: 5 |

**Examples:**
```bash
python scripts/install_helper.py "spring boot"
python scripts/install_helper.py "react" 10
```

**Output includes:**
- Skill name, author, stars, description
- GitHub search link to find the repository
- Installation command instructions

---


---

## Skill Installation

This skill integrates with `add-skill` CLI to install skills directly from Git repositories.

### Supported Agents

| Agent | Identifier | Global Skills Directory |
|-------|------------|-------------------------|
| **Antigravity** | `antigravity` | `~/.gemini/antigravity/skills/` |
| **Claude Code** | `claude-code` | `~/.claude/skills/` |
| **Cursor** | `cursor` | `.cursor/skills/` |
| **Codex** | `codex` | `.codex/skills/` |
| **OpenCode** | `opencode` | `.opencode/skills/` |
| **GitHub Copilot** | `github-copilot` | `.github/copilot/skills/` |
| **Roo Code** | `roo` | `.roo/skills/` |

### Install Command References

The `add-skill` tool installs skills from any Git repository.

**Install specific skill to global scope (User-level):**
```bash
npx add-skill <owner>/<repo> --skill "<skill-name>" -g -a antigravity -y
```

**Install ALL skills from a repo:**
```bash
npx add-skill <owner>/<repo> -g -a antigravity -y
```

**Install to project scope (Local):**
```bash
npx add-skill <owner>/<repo> --skill "<skill-name>" -a antigravity -y
```

**List available skills in a repo:**
```bash
npx add-skill <owner>/<repo> --list
```

### Complete Installation Workflow

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
   Choose one of the installation commands above. For most cases, use the **Global Install**:
   ```bash
   npx add-skill <owner>/<repo> --skill "<skill-name>" -g -a antigravity -y
   ```

4. **Verify Installation**
   Check if the skill files are created in the agent's skill directory.


---

## Response Format

**Success Response:**
```json
{
  "success": true,
  "data": {
    "skills": [...]
  }
}
```

**Error Response:**
```json
{
  "success": false,
  "error": {
    "code": "ERROR_CODE",
    "message": "Error message"
  }
}
```

---

## Agent Workflow

When a user requests SkillsMP search functionality:

1. **Check if `.env` exists**
   - If exists → Run search script directly
   - If not → Guide user through setup

2. **Guide user to get API Key**
   - Direct user to https://skillsmp.com/settings/api
   - Ask user to provide the API Key

3. **Configure API Key**
   - Use `setup.py` script or create `.env` file
   - Verify setup before running search

> [!CAUTION]
> The `.env` file contains sensitive information and is excluded from Git.
> Never share or expose your API Key publicly.
