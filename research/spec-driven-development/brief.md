# Round 1 调研子代理通用 brief(#25 spec-driven development)

你是 deep-research 仓库第 25 期的一条调研线。先读 `research/spec-driven-development/STATE.md`(核心问题、spec 分型 T1–T4、7 条调研线、交叉口径预警)。只做你被分配的那条线。

## 任务
收集**一手来源**(论文全文/PDF、官方文档、原始博客/视频、原始数据集),提取 20–35 条论断。二手转述只用来找线索,必须回到一手核对;回不到一手的标 `confidence: "secondhand"`。

## 产出(写两个文件,路径相对仓库根)
1. `research/spec-driven-development/lines/<LINE>.json`:
```json
{"line":"<LINE>","claims":[{"id":"<前缀>01","claim":"中文论断,带完整口径(分子/分母/时间窗/限定语/样本)","quote":"一手原文逐字摘录(英文保留原文)","source_url":"...","source_title":"作者, 年份, 标题, 出处","date":"YYYY-MM","source_type":"【官方】|【研究】|【厂商】|【媒体】","spec_type":"T1|T2|T3|T4|mixed|n/a","design":"RCT|对照实验|观察|基准|调查|案例|文档|评论","confidence":"verbatim-checked|paraphrase-checked|secondhand","notes":"利益冲突、样本局限、发表状态、与其他来源的口径差"}],
 "searched_angles":["记录全部搜索角度,包括没搜到的"],
 "cross_caliber_issues":["供验证阶段用的口径疑点"]}
```
2. `research/spec-driven-development/lines/<LINE>.md`:中文要点摘要(按子主题分块,突出口径陷阱、利益相关方、最强与最弱证据),不超过 120 行。

## 规则
- `quote` 必须是你实际在页面/PDF 上读到的原文,不得编造或拼接;读不到原文就留空并降 confidence。抓取工具的摘要可能编造引语——对关键数字务必在原文中定位。
- 厂商自测/自述标【厂商】;谁在说话、谁受益写进 notes。
- 不得混口径:star/下载 ≠ 采用 ≠ 效果;合并率/缺陷率/通过率/token/墙钟/返工率分开记。
- 预测类数字必须带区间或情景。
- 名人名言逐字回一手(视频带时间戳),找不到标"疑似伪引用"。
- 联网:禁止在 User-Agent、header、URL、payload 中放任何用户个人信息(邮箱等);要求 UA 带联系方式的站点用通用 UA 或跳过。
- 不要修改仓库里其他文件,不要 git commit。
- 最后回复:论断条数、独立一手来源数、最强 3 条与最弱 3 条、未搜到的关键角度。
