# STATE — #13 指数化的终局:被动投资会破坏市场吗?

- slug: `indexing-endgame`
- 起跑:2026-08-14
- 题目:被动占比过半后,"指数泡沫论"有没有实证支撑?
- 硬约束:非投资建议声明;所有占比数字必须带口径(基金资产 vs 总市值 vs 成交量;美国 vs 全球);警告方与辩护方都有利益相关(主动管理人 vs 指数基金巨头),口径标注双向执行

## 调研线拆法(由题目结构推出,非沿用上期数量)

题目内在结构 = 一组流行警告 vs 多个互相独立的实证机制。警告是一个整体叙事,但学术实证分散在互不重叠的文献带:占比测量、价格发现、指数效应、基金业绩、治理集中。按机制切 7 条线:

| # | 线 | 独占产出的证据类型 |
|---|---|---|
| L1 | 被动占比的测量 | "过半"到底是什么口径:ICI/Fed(Anadu et al)/学术影子指数估计;基金资产 vs 总市值 vs 成交量三个分母 |
| L2 | 警告者一手 | Michael Green、Einhorn、Burry、Grantham 的原话与原文——他们到底主张什么、拿了什么证据 |
| L3 | 理论底座 | Grossman-Stiglitz 1980 原文;Gabaix-Koijen 非弹性市场假说(乘数~5);Haddad et al 弹性竞争;理论到底预测什么 |
| L4 | 价格发现实证 | price informativeness 测量(Bai-Philippon-Savov、Farboodi、Sammon、Coles-Heath-Ringgenberg Russell 断点) |
| L5 | 指数纳入效应与联动 | 纳入溢价时序(Greenwood-Sammon 消失的指数效应)、comovement、ETF 与波动率(Ben-David et al) |
| L6 | 主动跑输的证据 | SPIVA 逐年数据、Morningstar Active-Passive Barometer、persistence scorecard、以及对 SPIVA 方法学的批评 |
| L7 | 治理与集中 | 三巨头投票权数字(Bebchuk-Hirst)、common ownership(Azar et al + 复现失败)、反垄断动向、指数编制商权力 |

重叠检查:L2 只收原话与警告方自己给的证据,不做学术裁决(裁决归 L3-L5);L1 只做测量口径,占比数字以 L1 为准,其他线引用时不另查;L6 只做基金业绩层,不碰价格发现(那是 L4);L7 只做所有权与治理,不重复 L1 的占比。

## 运行日志

- [x] Round 1:7 线并行调研 → raw/ 全部落盘(L4/L5/L6 另有独立重跑版 -alt.md 可交叉);脚本存 research-round1.workflow.js
- [x] Round 2:32 组承重论断 × 3 票对抗验证进行中(runId wf_d935de5b-80e;29 组 Opus + 3 组 Sonnet;脚本存 verify-round2.workflow.js)。分组清单见脚本 GROUPS;调研 agent 留下的一手提取文本在 session scratchpad(217 文件),验证 agent 复用
- [x] Round 3:单源承重实证双席审计(反证搜索席 + 有否决权的方法学审计席)
- [x] 成文四版 + 一致性回查
- [x] 注册渲染 + 发布 + 钩子收割

## 下一步恢复点

已完成发布(2026-08-20)。四版页面在线,钩子已分流(meta-knowledge Day 73 + 候选池 2 条)。
