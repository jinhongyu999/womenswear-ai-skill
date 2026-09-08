#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""源2: ai-image-prompt-cookbook(image3.org)女装/电商/小红书 精选 → LY-Space 裸数组提示词源
上游: https://github.com/gpt-img-2/ai-image-prompt-cookbook (CC BY 4.0, 保留署名)
"""
import json, datetime, os

SRC_FILE = os.path.expandvars(r"%LOCALAPPDATA%\Temp\cookbook\prompts.zh.json")
OUT = r"C:\Users\Administrator\.hermes\tmp\womenswear-skill\zh-fashion-source.json"
NOW = datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=8))).isoformat()

d = json.load(open(SRC_FILE, encoding="utf-8"))
prompts = d["prompts"]
# 只取女装/电商/产品摄影/小红书/广告(不要童装)
WANT_CATS = {"AI 女装", "电商主图", "产品摄影", "小红书封面", "广告海报"}
items = []
for i, p in enumerate(prompts, 1):
    cat = p.get("category", "")
    if cat not in WANT_CATS:
        continue
    # 模板型条目本身是完整可执行提示词; 填充占位符整理
    prompt = (p.get("prompt") or "").strip()
    title = (p.get("title") or "").strip()
    if not prompt or not title:
        continue
    items.append({
        "id": f"zh-fashion:{i:04d}",
        "sourceId": "zh-fashion-source",
        "title": f"[{cat}] {title}",
        "prompt": prompt,
        "description": (p.get("scenario") or "") + f" 来源: {p.get('sourceUrl','')}",
        "referenceImageUrls": [],
        "coverUrl": "",
        "tags": [cat, "中文图库"] + [t for t in (p.get("tags") or []) if isinstance(t, str)][:4],
        "author": "ai-image-prompt-cookbook (CC BY 4.0)",
        "sourceUrl": p.get("sourceUrl") or "https://github.com/gpt-img-2/ai-image-prompt-cookbook",
        "createdAt": NOW,
        "imageMode": p.get("imageMode") or "generate",
        "imageModel": p.get("imageModel") or "",
    })

json.dump(items, open(OUT, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print(f"输出 {len(items)} 条 → {OUT}")
from collections import Counter
print(Counter(x["tags"][0] for x in items))
