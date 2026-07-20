# 03 · Round 2 三票对抗验证判决汇总(2026-07-20)

> 3 名独立验证 agent(A/B/C)对 12 组承重论断 refute-by-default 投票,互不见对方结论;单票原文见 `votes/voter-{a,b,c}.md`(每组附一手 URL)。
> 结果:**36 票,12/12 组挺过,0 推翻;5 组含修正票**。

## 计票

| 组 | A | B | C | 合议 |
|---|---|---|---|---|
| G1 内存售罄 | 修正 | 修正 | 修正 | **修正**(3-0) |
| G2 内存价格口径 | 修正 | 修正 | 修正 | **修正**(3-0) |
| G3 CoWoS/NVIDIA | HOLDS(附警示) | 修正 | 修正 | **修正**(2-1) |
| G4 PJM 价格链 | HOLDS | HOLDS | HOLDS | **HOLDS**(3-0,逐字命中一手 PDF) |
| G5 IMM 归因 | HOLDS | HOLDS | HOLDS | **HOLDS**(3-0) |
| G6 ERCOT 队列 | HOLDS | HOLDS | HOLDS | **HOLDS**(3-0;另见 04 的 198 勘误) |
| G7 GE Vernova | HOLDS | 修正 | HOLDS | **修正**(1-2,B 的口径发现成立) |
| G8 核电时间表 | HOLDS | HOLDS | HOLDS | **HOLDS**(3-0) |
| G9 IEA/LBNL/前科 | HOLDS | HOLDS | HOLDS | **HOLDS**(3-0,逐字命中) |
| G10 Google 效率 | HOLDS | HOLDS | HOLDS | **HOLDS**(3-0) |
| G11 Nadella 引语 | HOLDS | HOLDS | HOLDS | **HOLDS**(3-0,拼接忠实) |
| G12 NERC vs Grid Strategies | 修正 | 修正 | 修正 | **修正**(3-0,归属错误) |

## 合议修正(成文按此执行)

- **G1**:"三家 2026 产能整体售罄"→ 一手仅支持:SK Hynix 全线(DRAM/NAND/HBM)售罄、Micron 2026 HBM 全部签约;**Samsung 官方仅确认 HBM/HBM4 售罄**,"全线售罄"是分析师口径。
- **G2**(三票收敛,推翻我 Round 1 的"现货口径"修正):流传的 "+90%" 实为 **TrendForce 2026-02-02 对 1Q26 常规 DRAM 合约价的上修(90-95%)**——是合约实录,不是现货;2Q26 官方口径:常规 DRAM +58-63%、NAND +70-75%、**LPDDR5X 78-83%**("+89%" 无一手,弃用);**16GB DDR4 $137→$207 三票均无法回溯到一手,弃用**(方向不受影响:现货涨幅更极端)。
- **G3**:NVIDIA 锁定 CoWoS "60%+ 份额"与"80-85 万片"是两套互相矛盾的供应链估算(60% × ~100 万总量 ≈ 59.5 万片),**不得并引**;取"约六成份额(供应链估算)";"产能年增 ~80%"仅对 2025 年成立。
- **G7**:GE Vernova 的 83→100→110 GW 均为 **backlog + slot reservation 合并口径**,非纯签约 backlog(Q1 新增 21 GW 中 19 GW 是 slot reservation);"签约 backlog 100 GW"表述降为"订单簿(含产能预约)100 GW"。"8 年 lead time"三票均未独立核实原始出处,降为"媒体综合口径"。
- **G12**(三票收敛,归属错误):"5 年峰值 +166 GW(~90 GW 数据中心)"出自 **Grid Strategies 对公用事业/FERC 申报的汇编**(2025 报告),不是 NERC;NERC LTRA 自身口径为十年峰值 +24%(~224 GW)、2030 前 ~160 GW。原文把"预测的预测之争"的两方数字归到了同一方名下,必须掰开。
- **账单数字**(A 票 + 审计 D 收敛):"Pepco +$21"归属错误——**+$21/月是 BGE(马里兰 OPC 口径)**;Pepco DC ~$20(OPC-DC/Synapse)、Pepco 马里兰 +$14;俄亥俄 $16 是 IEEFA 估算保守端(AEP Ohio 自报 ~$27)。归属从"CUB"改为**各州消费者监护办公室(OPC)/IEEFA**;马里兰传导自 2025 年 10 月起(非 6 月)。
