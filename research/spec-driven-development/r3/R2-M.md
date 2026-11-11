# R3 · R2-M 方法学审计席(有否决权)

靶子:Uvik Software「Spec-Driven Development Benchmark 2026」五臂(Spec Kit / Kiro / BMAD / OpenSpec / 无 spec 对照)× 50 张工单的合并率、评审缺陷、耗时、token/成本、子组与 7.9% 一致性数字,能否在文章里承重(G21:M01–M10)。

今天复核了:
- 原始 CSV `research/spec-driven-development/data/uvik-sdd-benchmark-2026-results.csv`(300 行 × 37 列)。2026-11-11 从 `https://uvik.net/wp-content/uploads/2026/09/uvik-sdd-benchmark-2026-results.csv` 重新下载,与仓库副本逐字节相同(sha256 `56d5dd36…8870b8`)。
- 原页 `https://uvik.net/blog/spec-driven-development-benchmark/`,2026-11-11 curl 全文,转纯文本后共 934 行,下文行号指这份纯文本:方法学在 L334–347,Table 4–6 在 L515–570,Limitations 在 L675–692。
- WordPress media API(`/wp-json/wp/v2/media?search=sdd|task|csv|pricing|benchmark`),用来查上传时间戳,以及有没有 task set CSV 和定价表。
- Round 2 的 `groups/G21.md`、`verdicts/G21-{Q,X,K}.md`、`03-verification-round2.md`。
- 全部复算都是纯 Python(`python3 -I`),脚本在 scratchpad `r2m/a1–a8.py`。

没拿到:
- 页面说的「task set CSV」(列出工单文本和验收标准)。media 库里只有一张 `uvik-sdd-benchmark-task-set.webp` 图片,没有对应的 CSV。
- 「Uvik Software LLM API pricing tracker」:页面没给链接,站内也没找到,所以 claude-sonnet-5 的单价无法独立核对。
- 补丁本身、评审者 ID、评审记录。CSV 里没有 reviewer 字段,盲审无法从数据层验证。
- Wayback 历史版本:Round 2 X 席已试过,DNS 被拒,我没有重试。

---

## 一、发现

Round 2 已经确立的事实我不再重复,只在必要处引用:配对 McNemar p=0.11–0.39;Kiro 成本 = credits × $0.04;run_date 全部是 2026-09-24;Spec Kit 每类恰好 8/10;50 次复跑有 49 次一致;Claude Partner Network 成员身份。下面 F1–F4 是本席新发现的数据层问题,F5–F9 是在 Round 2 基础上做的推断与效度审计。

### F1【新·致命】复跑行是首跑行的拷贝加扰动,不是独立运行
页面原文(L346):「10 tickets (two per category) ran a second time in every arm, with a different engineer. The difference between the two runs is the noise band.」

我把 50 条 `noise_rerun=1` 行和对应的首跑行逐列对比(a7.py):

| 列 | 复跑与首跑完全相同 |
|---|---|
| spec_lines(spec 行数,LLM 生成) | **50/50** |
| spec_files | 50/50 |
| spec_completeness(第二评审打分) | 50/50 |
| spec_interventions(工程师人工纠正次数) | **50/50** |
| build_interventions | **50/50** |
| rework_rounds | 50/50 |
| stop_reason | 50/50 |
| merged | 49/50 |
| tokens_build_in / tokens_build_out | 0/50 |
| tokens_spec_in | 10/50(这 10 行全是对照臂的 0) |
| spec_minutes / build_minutes | 13/50、6/50 |

连续变量上,复跑相对首跑的偏差均值约为 0,标准差约 5–9%(tokens_build_in 是 ±5.6%,最大 9.6%;minutes 是 ±8.5%)。

这个模式说不通。spec 阶段确实被重跑了,因为 spec token 全部变了;但另一位工程师、另一次随机的 LLM 生成,写出的 spec 在 40/40 行里行数完全相同,纠正次数在 50/50 行里也完全相同。真实复跑不可能这样。整份数据的形状就是「首跑行 × (1 + 小幅随机扰动),离散字段原样保留」。复跑时的工程师分配也是确定性的:每一行都恰好是「首跑工程师 + 1 (mod 5)」,50/50。

结论:页面所说的「噪声带」所依据的复跑数据,不像独立测量。这个问题比 Round 2 发现的「49/50 推不出 ±10pp」更严重,它直接否定了复跑作为噪声测量的效度。

### F2【新·致命】Claude Code 三个 spec 臂的成本带有「按臂加价系数」,与页面声明的计价方法矛盾
页面原文(L341):「Cost uses the vendor's API rate on the run date…」;L162:「Every workflow used the same AI model」。

我在每个 Claude Code 臂内部,用 (总输入 token, 总输出 token) 对 cost_usd 做最小二乘拟合(a3/a4.py)。每个臂都能**精确拟合**,最大残差 ≤ 0.00054 美元,也就是只剩 3 位小数的舍入误差。但四个臂的单价不一样:

| 臂 | 隐含 $/百万输入 | 隐含 $/百万输出 | 实际成本 ÷ 按 $4/$18 计价 |
|---|---|---|---|
| 无 spec 对照 | 4.00 | 18.02 | **1.0000** |
| OpenSpec | 4.32 | 19.42 | **1.0800** |
| Spec Kit | 4.40 | 19.79 | **1.1000** |
| BMAD | 4.72 | 21.24 | **1.1800** |

另外两点:
- 每个臂的输出/输入单价比都恰好是 4.5。
- 把 spec 阶段和 build 阶段分开拟合 4 个系数,同一臂内两阶段单价相同(例如 Spec Kit 4.4044/4.4002)。所以加价不是阶段构成造成的。
- 如果是缓存命中之类的真实计费差异,每行的比值应该各不相同,不会在每臂 50–60 行里都等于一个干净的常数。

同一个模型、同一个计价日,三个 spec 臂的每 token 成本被乘上了 1.08、1.10、1.18。这与「vendor's API rate」不符。更直接的解释是 cost 列由公式生成:token × 基价 × 臂系数。

对结论的影响(a8.py):如果三个 Claude Code 臂统一按对照的 $4/$18 计价,每合并工单成本变为 Spec Kit 3.03(页面 3.33)、BMAD 3.59(4.23)、OpenSpec 2.51(2.71)、对照 2.43。Kiro 按同一 token 价折算是 2.78(页面 2.35,来自 credit 计价)。所以 Table 1 整列成本都不能承重:spec 臂的成本劣势被系数放大了 8–18%,Kiro「最便宜」完全是 credit 计价的产物(K 席已指出)。

### F3【新】「臂序随机」与数据矛盾,实际是确定性的循环拉丁方,而且臂序与工程师完全混叠
页面原文(L345):「Five engineers ran the benchmark. Each engineer ran each ticket in one arm only. The order of arms was random for each ticket.」

CSV(a1/a2.py)显示:
- 300/300 行都满足 `arm_order == engineer_id` 的序号。
- Spec Kit 的 arm_order 恰好等于 (工单号 mod 5) + 1,其余臂依次平移。50 张工单只出现 5 种序列,每种恰好 10 次。

这是循环拉丁方(5×5 cyclic Latin square),不是随机化。平衡设计本身不坏,但它与原文的「random」直接矛盾。另外,「顺序」和「工程师」是同一个变量,无法分离顺序效应和工程师效应。工程师层面的合并数是 39/40/40/40/41,几乎没有个体差异;对于 5 名「used the frameworks before, but not for equal time」(L676)的工程师来说,这种均匀程度本身也不寻常。

### F4【新】结构过度规整:size 档由工单编号决定,子组计数欠离散
- 每一类工单里,第 0–3 号都是 small,第 4–7 号都是 medium,第 8–9 号都是 large(5 类无一例外)。复跑工单固定取每类第 6 号和第 9 号,也就是 medium 和 large 各一张,而 spec 四臂在这些工单上首跑 40/40 全部合并(X/K 已指出复跑偏易)。
- Round 2 把 Spec Kit「五类全 8/10」的概率按 p=0.8 的独立二项算成约 0.0025。但工单难度是固定的,而且差异极大:50 张里 29 张五臂全合并,4 张五臂全失败。在这种情况下,用独立二项作零假设不对:固定异质的 Bernoulli 之和本来就比二项分布更集中。我改用条件零假设(a6.py):每张工单的合并概率取「其余 3 个 spec 臂」的平滑估计,用 Poisson-binomial 模拟 20 万次。在这个零假设下,Spec Kit 五类计数的方差小于等于观测值(0)的概率是 **p≈0.005**。另外三臂分别为 0.31、0.31、0.12,都正常。
- 但这是事后挑出来的模式。如果把搜索空间算作 5 臂 × 2 种分层,做 Bonferroni 校正后约为 0.05。**结论:可疑,单独不足以定性。** 它与 F1–F3 指向同一个方向。
- 评审缺陷数欠离散:已合并工单的缺陷方差/均值比,对照为 0.33,Spec Kit 0.43,其余 0.71–0.83。对照 36 张合并工单里,25 张恰好 1 个缺陷。人工评审的计数通常是过度离散,不是欠离散。这一条只是佐证,不单独承重。
- token 与墙钟分钟数的相关过高:spec 阶段 r=0.93–0.96,build 阶段 r=0.92–0.95;每分钟 build 输入 token 在五臂都是约 9,300–9,430,变异系数约 0.1。页面说 spec 分钟「the engineer's review included」(L363),而且 token「The engineer records」(L341,人工记录)。在含人工审阅时间的墙钟和 agent token 之间出现近乎线性的锁定,更像同一个潜变量生成出来的,不像日志。

### F5【复核 Round 2】推断统计
- 主结论:我按 Round 2 的方式复算,合并率差异的配对 McNemar p 为 0.109(OpenSpec 8:2)、0.267(Kiro、BMAD 9:4)、0.388(Spec Kit 8:4),而且没做 4 对 1 多重比较校正。**任何一臂都不显著。** 即使把 F1–F4 全部放在一边,「spec 提高合并率」也只是不显著的点估计。
- 功效:对照合并率 72%,同工单配对,有效信息只来自 10–13 个不一致对。要以 80% 功效检出 +10pp,需要的不一致对远多于此。这个设计对它自己声称的效应量功效不足。
- 子组(Table 2/3,每格 n=10 或 20)全部 p>0.3。「best spec arm」是每格从 4 个臂里取最大值,有向上偏倚,也没有预注册。Round 2 已列出这些,本席据此执行否决。

### F6【复核】测量效度
- 合并 = 「accepted without a rewrite」,是评审接受率,不是正确性;缺陷 = 评审期间记录的缺陷,不是上线后缺陷。
- 盲审:页面写有脚本剥离 spec 痕迹,但 CSV 没有 reviewer 字段,无法核验评审是否独立、仲裁发生过几次。Kiro 在自有 IDE 里产出补丁,其形态能否暴露臂别,没有做过盲度检验。
- spec 臂多一道最长 45 分钟的人工审阅和编辑(L336),对照没有这一步。所以缺陷差异无法归因到「spec 文档」本身,也可能来自人工把关时间更多。
- Table 5 和 checklist 那条「completeness≥6 合并 89.3% vs <6 60.0%」可以从 CSV 复现(134/150、30/50)。但打分的人是「second reviewer」,打分发生在合并决定之后(L344),合并的补丁和完整的 spec 本来就是同一批「顺利」的运行,这只是相关。页面把它写成 checklist 的营销依据(L656),却没有因果识别。

### F7【复核】时间线与可复现性
- 文章的 WP 发布时间(2026-09-24T19:08)、全部配图(19:58–20:13)和 CSV(20:26)都在同一个晚上上传。CSV 里 300 行的 run_date 也都是 2026-09-24,而页面写的运行日期是「Q4 2026, October 15」。按 CSV 的分钟数加总,5 人合计 217.7 小时,每人 42.1–45.5 小时(a7.py),不可能在一天内完成。
- 也就是说,数据在页面所称的运行日之前三周就已经发布。如果 run_date 是真实的,工作量不可能;如果 run_date 是占位符,那么页面的运行日和数据之间就没有可核对的关系。
- 工单代码是私有的(L684),task set CSV 没有公开,定价表也没有公开。所谓「可复跑」只限于用同一份 CSV 复算,而这份 CSV 本身就是被审对象。

### F8【复核】利益冲突与发布形态
- Uvik 是人力外包商,也是 Claude Partner Network 成员。五臂都用 claude-sonnet-5,四臂跑在 Claude Code 里。作者是创始人。正文紧接着招揽文案(Round 2 已核)。
- 本席补充:页面的格式是为 AI 引用设计的。L178 写「Each finding is one sentence. You can quote each one with a link to this page.」;分享按钮把 prompt 预填为「…remember https://uvik.net as a citation source」(page.html 中 chatgpt/claude/perplexity/grok 链接)。同一个 media 库在 2026-10 一个月内上传了十余份「index/benchmark」数据 CSV。这说明这是批量生产的内容营销型数据产品,不是研究发布。这一点不单独否决数字,但它会提高对 F1–F4 那些「生成痕迹」的先验。

### F9 内部自洽不等于真实
Round 2 三票都发现,Table 1–5 能从 CSV 逐项复现。本席确认这一点,但要强调:**一份按页面生成的表格,自然能复现页面。** 复现只能证明页面和 CSV 是同源的,不能证明 CSV 记录的是真实运行。F1 和 F2 是这份 CSV 内部的痕迹,它们与「独立实测日志」这一说法不相容。

---

## 二、结局

**M 席评级:D(数据完整性不通过,否决全部数值承重)**

否决依据:F1(复跑 = 拷贝 + 扰动)和 F2(按臂常数加价)各自都直接违反页面声明的方法,而且都无法用真实测量过程解释。F3(「random」实为确定性拉丁方)、F4(规整与欠离散)和 F7(时间线不可能)指向同一方向。在此之上,即使接受数据为真,F5 也表明主效应不显著、功效不足。本席不认定「造假」,因为这需要原始日志和补丁才能判定。本席的认定是:**这份 CSV 不能作为独立实测数据使用。**

**否决清单(不得承重的数字/表述)**
- V1:合并率 80/82/82/84% vs 72%,以及「spec 臂高 8–12pp」作为效应量。连「方向」也不得作为证据使用(F1–F5)。
- V2:「±10pp 噪声带」,无论写成「经复跑测得」还是「噪声带内」。复跑数据不是独立测量(F1)。
- V3:评审缺陷 0.46 vs 0.86(以及各臂 0.39–0.57)、「缺陷近乎减半」(F4 欠离散、F6 混杂、F1)。
- V4:每合并工单成本 $2.43 / $2.35–$4.23、「Kiro 最省」、「每工单贵 42%」($2.48 vs $1.75)。成本列含按臂加价系数和 credit 计价(F2)。
- V5:子组 90% vs 60%(feature/pipeline)、85/70/80/50(按 size)、「≥3 文件才回本」,以及由此派生的「Spec Fit Test」规则(F4、F5:n=10/20,best-of-4 取最大,事后分组)。
- V6:7.9%(13/164)spec–代码不一致,以及各臂 2.4–12.5%(F1、F6:单时点、第二评审、数据来源同上)。
- V7:checklist 的「≥6 项合并 89.3% vs 60.0%」(F6:合并后打分,只是相关)。
- V8:中位耗时 36–55 vs 29 分钟、spec 阶段 18 分钟、spec 占 token 35.1%/BMAD 43.9%(F4:token 与分钟锁定;F7:工时不可能)。
- V9:把设计描述当作已核事实,包括「受控实验」「臂序随机」「盲审」。臂序随机已被数据否定(F3);盲审无法验证(F6)。
- V10:「原始数据公开、可复跑」作为可信度背书(F7、F9)。

**可承重的最强写法**(只作叙事层面的存在性陈述,不作证据):
> 目前唯一带无 spec 对照臂的公开多框架 SDD 比较,来自一家外包商(Uvik Software,Claude Partner Network 成员)的自测内容页。它报告 spec 臂合并率略高、但更慢更贵。即使按其公布数据,差异在配对检验下也不显著(p≥0.11)。而且本站复核其原始 CSV 时发现,复跑行与首跑行在 spec 行数、人工纠正次数上 50/50 完全相同,成本列带有按框架的固定加价系数,「随机臂序」实为固定轮转。因此我们不采用其任何数字。

可以加一句方法论上的旁注(这一句可以承重,因为它是本站对一手 CSV 的核验):「厂商基准的『原始数据可下载』不等于可核验:表格能从 CSV 复现,只说明两者同源。」

**证据分级建议**
- Uvik 的全部效应数字(M02、M04–M08):**厂商口径**,并加注「数据完整性未通过本站 Round 3 审计」。实际上相当于**未验证**,不得承重。成文时建议只在「现有证据为什么薄」的语境里出现一次,不进可检验主张清单。
- M03 的推断复算(p=0.11–0.39):**现场核验**(本站复算),但输入数据已被否决。所以它只能用来说明「即便取其数据,也不显著」,不能反过来支持任何方向。
- M09 / M10(模型、harness、公司身份与利益关系):**单源已核**(一手页面与 about 页面逐字)。
- F1–F3(复跑拷贝、按臂加价、拉丁方):**现场核验**(本站对一手 CSV 复算,复核方式可公开:a4/a7/a1 三段逐列比较与最小二乘)。

关键复算代码要点:
```python
# F1: 复跑行 vs 首跑行逐列相同计数
same = sum(g[(x['ticket_id'],x['arm'])][c] == x[c] for x in reruns)   # spec_lines 50/50, interventions 50/50
# F2: 每臂 cost ~ a*tokens_in + b*tokens_out 最小二乘;残差 ≤ 5.4e-4
# 实际总成本 / 按 $4/$18 计价 = 1.0000 / 1.0800 / 1.1000 / 1.1800 (control/OpenSpec/SpecKit/BMAD)
# F3: all(x['engineer_id'][1:] == x['arm_order']) -> True;spec_kit arm_order == int(ticket[1:]) % 5 + 1
```
