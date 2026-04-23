#!/bin/bash
# Install script for Notion Skill

echo "Installing Notion Skill..."

cd "$(dirname "$0")"

# Prefer the checked-in standalone CLI when dependencies already exist.
if [ -d "node_modules" ]; then
    echo "Dependencies already present - skipping npm install/build."
    echo "Standalone CLI ready."
elif [ -f "package.json" ]; then
    echo "Installing dependencies..."
    npm install
    echo "Standalone CLI ready."
else
    echo "package.json not found"
    exit 1
fi

echo ""
echo "Next steps:"
echo "1. Set NOTION_TOKEN in .env, .openclaw.env, or ~/.openclaw/.env"
echo "2. Share your Notion pages with the integration"
echo "3. Test: node notion-cli.js test"
echo ""
echo "See SKILL.md for usage details."
