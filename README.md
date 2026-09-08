# 女装电商 AI 技能提示词源(Womenswear Skill Source)

供 LY-Space / infinite-canvas 使用的自定义提示词源(JSON 数组格式,兼容
[image-prompts](https://github.com/yukkcat/image-prompts) 注册表规范)。

## 内容(29 条)

- **7 条 女装模特姿势×场景**:都市街头(站姿/迈步/倚靠/全身)、街角咖啡(坐姿/持杯/倚门回眸)——提炼自开源商拍工坊(commerce-shoot-studio)的姿势结构,女装电商化改写
- **8 条 电商输出规格**:白底主图、全身展示、半身展示、面料特写、平铺摆拍、挂拍、隐形人台、多角度网格
- **9 条 卖点场景方向**:杂志编辑、轻奢氛围、UGC 买家秀、通勤街拍、约会、直播间、店铺陈列、季节 Campaign、多品组合
- **5 条 一致性约束工具**:版型材质颜色一致、人物一致、系列一致、负面约束、换背景不换衣

## 在 LY-Space 里接入

1. 打开 LY-Space → 右上角设置 → 提示词源
2. 新增来源,填:

```
名称: 女装电商技能
URL: https://raw.githubusercontent.com/jinhongyu999/womenswear-ai-skill/main/womenswear-skill.json
```

3. 刷新后在提示词库面板搜索"女装 / 姿势 / 白底 / 面料特写"即可检索插入

## 用法建议

- 生图前先把服装商品图/模特图导入画布作为参考图,再把技能提示词插入生成节点
- "一致性约束"条目可附加到任意提示词末尾提升稳定性
- 提示词里已内置"严格保持版型材质颜色一致"约束,适合女装改款/出款/上架图

## 维护

- `womenswear-skill.json`:主数据源(29 条)
- `gen_womenswear_source.py`:生成脚本(改后重跑再提交)

来源:姿势结构提炼自 [commerce-shoot-studio](https://github.com/lifei6671/commerce-shoot-studio)(Apache-2.0),女装化改写由 Hermes 完成。
