import re, json

with open("E:/ai/program/google seo web/ai coding match/scripts/generate.py", "r", encoding="utf-8") as f:
    code = f.read()

code = code.replace(
    'tool_map = {t["id"]: t for t in tools}',
    'tool_map = {t["id"]: t for t in tools}\ncategory_display = {"ide-assistant": "IDE Assistant", "ai-native-ide": "AI-Native IDE", "cli-agent": "CLI Agent", "open-source-agent": "Open-Source Agent", "open-source-cli": "Open-Source CLI", "autonomous-agent": "Autonomous Agent", "multi-agent-platform": "Multi-Agent Platform", "open-source-ide": "Open-Source IDE"}'
)

# Add g2 variable
code = code.replace(
    'has_free = any(p["price_monthly"] == 0 for p in t["plans"])',
    'has_free = any(p["price_monthly"] == 0 for p in t["plans"])\n        g2 = t.get(\'g2_rating\', \'N/A\') or \'N/A\''
)

with open("E:/ai/program/google seo web/ai coding match/scripts/generate.py", "w", encoding="utf-8") as f:
    f.write(code)

print("Modified successfully")
