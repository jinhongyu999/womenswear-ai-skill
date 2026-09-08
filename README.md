# 女装电商 AI 技能提示词源(Womenswear Skill Source)

供 LY-Space / infinite-canvas 使用的自定义提示词源(JSON 数组格式,兼容
[image-prompts](https://github.com/yukkcat/image-prompts) 注册表规范)。

## 两个源

### ① womenswear-skill.json — 女装电商技能源(41 条,自研提炼)

| 分组 | 条数 | 来源 |
|---|---|---|
| 女装模特姿势×场景 | 7 | 商拍工坊(commerce-shoot-studio)姿势结构,女装化改写 |
| 电商输出规格 | 8 | 白底主图/全身/半身/面料特写/平铺/挂拍/隐形人台/多角度网格 |
| 卖点场景方向 | 9 | 杂志编辑/轻奢/UGC买家秀/通勤/约会/直播间/店铺陈列/季节/多品组合 |
| 一致性约束 | 5 | 版型材质颜色一致/人物一致/系列一致/负面防翻车/换背景不换衣 |
| Lovart 市场技能转译 | 11 | lovart.ai/zh/skills 验证过的高频技能(电商3图换人/多角度/样机/Amazon主图组/详情叙事/UGC广告/小红书封面/视觉策略/模特角色表/品牌识别/前后对比) |
| 三视图版型核对 | 1 | fashion-mannequin-three-view(agent skill)提炼:无头人台正侧背三视图+中文标签 |

### ② zh-fashion-source.json — 中文女装图库源(80 条,第三方 CC BY 4.0)

[ai-image-prompt-cookbook](https://github.com/gpt-img-2/ai-image-prompt-cookbook)(89★,image3.org)
的女装/电商子集:AI 女装 40 + 电商主图 10 + 产品摄影 10 + 小红书封面 10 + 广告海报 10。
每条为完整可执行中文提示词(含对镜自拍/直播间/白底/种草封面等场景)。

## 在 LY-Space 里接入

设置 → 提示词源 → 新增来源,填:

```
名称: 女装电商技能
URL: https://raw.githubusercontent.com/jinhongyu999/womenswear-ai-skill/main/womenswear-skill.json
```
```
名称: 中文女装图库
URL: https://raw.githubusercontent.com/jinhongyu999/womenswear-ai-skill/main/zh-fashion-source.json
```

刷新后在提示词库搜索「女装/姿势/面料特写/三视图/小红书/白底」即可检索插入。

## 用法建议

- 生图前把服装商品图/模特图导入画布作参考图,再插技能提示词到生成节点
- 一致性约束条目可附加到任意提示词末尾
- Lovart 转译条目描述里标注了所需参考图数量,照做即可

## 许可与维护

- `womenswear-skill.json` 自研部分可自由使用;`zh-fashion-source.json` 遵循上游 CC BY 4.0(已署名 ai-image-prompt-cookbook)
- 生成脚本:`gen_womenswear_source.py` / `gen_lovart_batch.py` / `gen_mannequin.py` / `gen_zh_source.py`
- 上游参考:commerce-shoot-studio (Apache-2.0) · lovart.ai/zh/skills · fashion-mannequin-three-view · ai-image-prompt-cookbook
