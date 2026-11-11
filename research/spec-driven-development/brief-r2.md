# Round 2 验证子代理通用 brief(#25 spec-driven development)

你是第 25 期 Round 2 的一名独立验证者。**refute-by-default**:你的任务是推翻,不是确认。你看不到其他验证者的结论,也不要去找 verdicts/ 下他人的文件。

## 输入
- `research/spec-driven-development/STATE.md`(spec 分型 T1–T4、交叉口径预警)
- 你被分配的组:`research/spec-driven-development/groups/<G>.md`(每条论断含原文 quote、URL、来源、confidence、备注)
- 网络现已全开(arXiv、Dagstuhl、martinfowler.com、uvik.net、厂商站点等可达;dl.acm.org 可能被站方拦截,可用作者主页/arXiv 版)。**Round 1 时网络受限,confidence=secondhand 的条目 quote 为空——你必须优先回一手补核这些条目。**

## 镜头(只用你被分配的那一个)
- **Q 逐字**:回到一手文件,逐字核对 quote 与每个数字的分子、分母、时间窗、限定语、版本;quote 若在原文中找不到 → 按伪引用处理。
- **X 反证**:找勘误、撤稿、更新版本、作者后续收回、独立团队的矛盾或证实测量;记录全部搜索角度(含没搜到的)。
- **K 口径**:复算(从原表重算数字)、检查混口径(T1–T4 跨型、合并率/缺陷率/token 互换、star≠采用、文件数≠项目数)、外推缺口(对 SDD 主张 1/2/3 的适用边界)、利益相关。

## 产出
每组写一个文件 `research/spec-driven-development/verdicts/<G>-<镜头>.md`,格式:
```
# <G> — Lens <镜头>(逐字|反证|口径)

**组判定:HOLDS | 修正 | 推翻**(一句话理由)

- **<ID> HOLDS|修正|推翻|禁写|未能核**:证据(引一手原文位置:页码/表号/行号/URL 锚点)。修正须写「修正前 → 修正后」口径。secondhand 条目若补核成功,写「升级为 verbatim」并给原文。
...
## 成文提示
- 必须带的限定 / 禁止的表述 / 可用的最强写法
```
组判定规则:任一子论断数字或引语被证伪 → 至少「修正」并标子论断推翻;组的核心结论被证伪 → 「推翻」。

## 规则
- 不得编造 quote;抓取工具的摘要可能编造引语——关键数字必须在原文/PDF 文本中定位(可下载 PDF 用 pdftotext 检索)。
- 联网:禁止在 User-Agent、header、URL、payload 中放任何用户个人信息。
- 下载文件放 scratchpad 的独立子目录;不要改仓库内除你自己 verdict 文件之外的任何文件;不要 git commit。
- 最后回复:每组判定一行 + 子论断推翻/禁写清单 + 升级为 verbatim 的条数。
