#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""第三条: fashion-mannequin-three-view(agent skill)提炼 → 白底人台三视图版型核对"""
import json, datetime

PATH = r"C:\Users\Administrator\.hermes\tmp\womenswear-skill\womenswear-skill.json"
items = json.load(open(PATH, encoding="utf-8"))
existing = len(items)
NOW = datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=8))).isoformat()

prompt = (
    "任务:服装三视图版型核对图(正面/侧面/背面)。"
    "先提取参考图服装的唯一共享规格作为全视图基准:品类、衣长、廓形、版型松紧、面料厚薄、颜色;领型、肩袖/门襟/系带/蝴蝶结、收腰收胯结构;走线、褶裥、拼接、开衩、下摆形状;背面独有细节(系带/蝴蝶结/露背/拉链/纽扣)。"
    "三视图展示同一件服装,不得逐角度各画一套。缺侧面参考时,按前后结构保守推导侧视图,不得发明新设计。"
    "三个面板使用完全相同的无头无臂人台:无五官无头发无手,哑光白或浅灰表面,同身高同比例同姿态直立。"
    "排版:16:9 横版画布,纯白 #FFFFFF 背景,三张等距全身视图从左至右为正面/侧面/背面,图下方居中标注「正面视图」「侧面视图」「背面视图」。"
    "语言用产品规格渲染而非时尚编辑:orthographic product sheet, apparel technical presentation, neutral ecommerce lighting;禁用 lifestyle/runway/garden/beautiful model/cinematic。"
    "一致性检查:三视图颜色面料一致、衣长与下摆宽度一致、领型肩袖从前到侧到背一致、背面保留背带/系带/开衩等独有细节、侧面为中性侧影。"
)

items.append({
    "id": f"womenswear-skill:{existing+1:04d}",
    "sourceId": "womenswear-skill",
    "title": "白底人台三视图(版型核对款卡)",
    "prompt": prompt,
    "description": "提炼自 fashion-mannequin-three-view(agent skill,xigua0626):同一服装在无头无臂人台上的正/侧/背三视图,16:9 白底+中文标签。出款版型核对/款卡/工艺单必备。",
    "referenceImageUrls": [],
    "coverUrl": "",
    "tags": ["女装", "三视图", "人台", "版型", "款卡"],
    "author": "Hermes×fashion-mannequin-three-view提炼",
    "sourceUrl": "https://github.com/xigua0626/fashion-mannequin-three-view",
    "createdAt": NOW,
    "imageMode": "generate",
    "imageModel": "",
})

json.dump(items, open(PATH, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print(f"追加 1 条 → 总 {len(items)} 条")
