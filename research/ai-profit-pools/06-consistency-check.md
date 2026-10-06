# 06 — 成文后一致性检查(对照 05-locked-calibers + 04-round3 可用表述)

检查范围:deep.zh / deep.en / plain.zh / plain.en。链接(全部 hub.cissychen.com,语言与版本匹配,目标页存在)、标题(全部 "## ")、** 配对:均无问题。亿/万亿换算逐项抽核 deep zh↔en、plain zh↔en,未发现错位。共 58 处修改(deep.zh 10、deep.en 13、plain.zh 17、plain.en 18)。

## deep.zh(10 处)
1. §1 Spolsky「是它的一个特例」→「与它相关但不是同一命题」— G02/G04:Spolsky 讲互补品商品化,不得与 Aggregation Theory 混为同一命题。
2. §4 Amazon 折旧 +$14 亿 → 加「(2025 10-K 实际值)」— G17 要求注明。
3. §4 Meta 折旧 −$29.2 亿 → 加「按 2024 年底前已投用资产测算」— G17 口径。
4. §4「Alphabet 和 Meta 在逼近零」→「Alphabet 只有单季为负,Meta 单季接近零但为正」— G18:Alphabet TTM +$53.3B,不是逼近零。
5. §7「审计席认为…原稿里…被判死,下面是改写后的版本」→ 直述「这种说法不成立。下面分开看」— 写作间口吻。
6. §7 Nagle & Yue 工作论文 → 加「SSRN…(经 Linux Foundation 博客介绍)」— G28 来源归属。
7. §8 Meta 广告 +27% → +27.5% — G31。
8. §8「原稿里…−23%…判死」→「流传的…一说无人核到原文,不可用」— 写作间口吻。
9. §10「原稿里…被判死」→「常见的…说法不成立」— 写作间口吻。
10. §10「Amazon 和 Alphabet 本季利润的大头」→「Amazon 本季税前利润的大头…(Alphabet 另有一大块来自未具名私营公司)」— G20:Alphabet 不是干净例证、不得归于实验室。

## deep.en(13 处)
1–10(编号外 3 条见下):与 deep.zh 1–10 一一镜像(Spolsky、$1.4B 实际值、Meta 存量资产口径、Alphabet/Meta 现金流、§7 原稿口吻、Nagle 来源、+27.5%、−23% 口吻、OpenAI 收入对比口吻、Alphabet 例证)。
5. §1 "called "the labs will never recoup their costs" "the bear case…" → 去掉伪引号,改为 the scenario in which… — 不是 Thompson 原话,不得加引号。
11. §1 Amodei "treated each model as a company" 伪引号 → 换成 G04 逐字 "If you consider each model to be a company, the model that was trained in 2023 was profitable"。
12. §5 SemiAnalysis "not because it is cheaper but because it is sooner," 伪引号 → 去引号转述 — R1 只有转述,无逐字。

## plain.zh(17 处)
1. 页首「见深入版」→ 加深入版链接(与 en 对齐)。
2. Amazon 505 亿收益 → 「税前收益」— G20。
3. Thompson 3 月 → 改为条件句「如果…紧密整合…可能更赚钱」;9 月加「从一个事件推断」— G02 条件式/单一事件。
4. 铁路「投资人估计亏掉」→「据一位学者估算…(也有学者不同意)」— G06:估算非实测、方向存争。
5. Oracle 14% →「据媒体援引 Oracle 内部文件报道」;30–40% 加「经调整口径」— G16。
6.「这是本期审稿时被推翻的一个推论」→ 直述推论站不住 — 写作间口吻。
7. Anthropic「按正式会计口径亏了约 81 亿」→「经营亏损约 81 亿」— G26:GAAP 净亏是 $41.97B,$8.06B 是经营亏损。
8.「原稿写…审稿时被推翻了」→ 直述;「OpenAI 最贵的一档」→「旗舰标准档从 GPT-5 的 10 美元涨到最新顶档 50 美元」— 写作间口吻 + G27(pro 档 $180,"最贵一档"不准)。
9. 闭源 80%/96% → 改「工作论文」并加「该平台只占全球支出约 1%」— G28。
10. Google 42 美元 → 加「不含集团层面 AI 研发」— G31。
11.「下一代 Siri 背后用的是 Gemini」→「Apple 下一代基础模型将基于 Gemini」— G31 联合声明原意。
12. Apple 付 10 亿 →「据彭博签约前报道…(正式条款未披露)」— G31 降级表述。
13. Meta「利润下降 8%」→「合并经营利润下降 8%」— G31。
14. Windsurf 断供 → 加「据 Windsurf CEO 说」,「大部分模型供应」→「Claude 3.x 几乎全部直接供应」— G30 单方说法。
15. Bain「一年前缺口约 8,000 亿」→ 补「针对 2030、假设全部本地 IT 迁云」前提 — G29 判死项。
16. 微软 241 亿「一年」→「2026 财年」;Amazon「这一季利润」→「税前利润」— G21/G20。
17. 可检验主张 2「一季度记了 505 亿」→「一个季度…(税前)」;主张 10「上限取消」→「到期」— 歧义/G24。

## plain.en(18 处)
与 plain.zh 2–17 镜像,另:
- "extreme memory prices" 伪引号 → G07 逐字 "extreme pricing conditions in memory"。
- "raw capability no longer translates directly into a moat" → G02 逐字 "Pure capability no longer translates directly into a moat."
- "lack the ability to obtain investment-grade financing" → G09 逐字 "currently lack the ability to secure long-term infrastructure contracts and investment-grade financing capacity";"supported by NVIDIA's balance sheet" 去伪引号。

## 未改(核对后保留)
- deep 正文的【R3 审计…】「三票中两票判死」「审计席做了降级」等:属证据标注/方法交代,非编辑指令。
- 附录「原稿」清单:方法附录,允许。
- Nadella「有芯片没有通电机房」:R1 已核(BG2 2025-11)。
