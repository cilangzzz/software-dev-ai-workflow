---
name: notion
description: Read, search, create, and update content in shared Notion pages and databases through the local `notion-cli.js` tool. Use when Codex needs to work with a Notion workspace, especially for database entry management, page body updates, schema inspection, or workspace search. Prefer the standalone CLI in this folder. Load `NOTION_TOKEN` from the current shell, a workspace `.env` or `.openclaw.env`, and only fall back to `~/.openclaw/.env` when needed.
---

# Notion

Use the standalone CLI in this folder:

```bash
node notion-cli.js <command> ...
```

Prefer running from this skill directory or from a project directory that already contains `.env` or `.openclaw.env`.

## Setup

1. Create a Notion integration at `https://www.notion.so/my-integrations`.
2. Copy the internal integration token.
3. Put `NOTION_TOKEN=secret_...` in one of these places, in this order of preference:
   - Current shell environment
   - Project `.env`
   - Project `.openclaw.env`
   - `~/.openclaw/.env`
4. Share each target page or database with the integration in Notion.

Notion integrations cannot see anything until you explicitly share it.

## Permission Notes

- Every CLI call still performs a live request to the Notion API.
- This skill no longer needs to write temp mapping files for `--numbered`.
- This skill no longer assumes you must write to `~/.openclaw/.env`.
- If `node_modules` already exists, `install.sh` skips `npm install`.

These changes reduce extra local permission prompts, but they do not remove network approval requirements enforced by the host agent runtime.

## Commands

```bash
node notion-cli.js test
node notion-cli.js search "content ideas"
node notion-cli.js get-database DATABASE_ID
node notion-cli.js query-database DATABASE_ID
node notion-cli.js query-database DATABASE_ID --filter '{"property":"Status","select":{"equals":"In Progress"}}'
node notion-cli.js add-entry DATABASE_ID --title "My entry"
node notion-cli.js update-page PAGE_ID --properties '{"Status":{"select":{"name":"Done"}}}'
node notion-cli.js append-body PAGE_ID --text "Research Notes" --type h2
```

## ID Usage

Use either:

- Direct UUID from the Notion URL
- Notion auto-ID such as `#3`

When using `#3`, also provide the database ID:

```bash
node notion-cli.js get-page '#3' DATABASE_ID
node notion-cli.js append-body '#3' --database DATABASE_ID --text "Content"
```

## Common Property Shapes

```json
{ "select": { "name": "In Progress" } }
{ "multi_select": [{ "name": "Tag 1" }, { "name": "Tag 2" }] }
{ "status": { "name": "Done" } }
{ "rich_text": [{ "text": { "content": "Notes here" } }] }
{ "date": { "start": "2026-02-15" } }
{ "number": 42 }
{ "checkbox": true }
{ "url": "https://example.com" }
```

## Troubleshooting

- `NOTION_TOKEN not set`: define the token in shell, `.env`, `.openclaw.env`, or `~/.openclaw/.env`.
- `object_not_found`: share the page or database with the integration.
- `validation_error`: verify property names and property types match the database schema.
- `rate_limited`: retry with fewer requests.

## Install

Use the local install script only when dependencies are missing:

```bash
./install.sh
```

If `node_modules` is already present, no install step is needed for the standalone CLI.
