# R3 · R6-X 反证搜索席
靶子:形式基准「形式陈述 vs 题意」错位率的几个承重数字(G25;F01–F07):ProofNet-Verified 195–205/367(ProofNet)与 99/367(ProofNet#);miniF2F-v2 Table 2 自动判官 97.5% vs 人工 62.7%(及「LLM 判官系统性高估 8–41pp」);Faults 4,833 findings / 398(399)proven。

今天复核了(2026-11-11):
- ProofNet-Verified 仓库(git clone,HEAD b7ca411,2026-11-07):README;`error_taxonomy/proofnet{,#}/results.jsonl` 逐题标签(各 367 行);`data/proofnet/proofnet-4.28.jsonl`、`data/proofnet#/proofnet#.jsonl`
- ReForm ConsistencyCheck 数据集 HF `GuoxinChen/ConsistencyCheck`(`consistency_check.jsonl`,859 行)+ arXiv 2510.24592 PDF §4.5、Table 3、附录 B
- miniF2F_v2 仓库(`datasets/miniF2F_v2s.jsonl`、`miniF2F_v2c.jsonl`,各 488)+ arXiv 2511.03108 PDF §2–4、Table 2/3
- Faults arXiv 2606.29493 PDF Table 4(逐行复加)、atp-checkers 仓库(无逐题结果文件)
- 独立判官—人工对照:Xu, Quan, Freitas arXiv 2606.09449v2(Table 4、附录 D.7/Table 11);Zhang, Valentino, Meadows, Freitas arXiv 2506.10903v2 §3;Zhang et al. arXiv 2606.31002v4(Table 1/2);Poiroux et al. arXiv 2406.07222(BEq 精确率/召回);Herald arXiv 2410.10878 v1/v2
- 下载与脚本:scratchpad `r6x/`(数据)、`xmatch2.py`、`xm3.py`、`xm4.py`(脚本)

没拿到:Ground False 论文定版 PDF(OpenReview 被拦截;204 vs 205 只能对 listing 摘要);Faults 逐题 findings(仓库未发布,无法与 ProofNet-Verified 逐题对齐);Herald 或 Kimina 译文的第二份独立人工评测(没搜到);ConsistencyCheck 16.4%/38.5% 对应的分母与快照(论文没给)。

## 一、发现

**X1 · ProofNet:独立团队逐题交叉,方向证实,ProofNet-Verified 是更严的上沿。** ConsistencyCheck(ReForm 团队:6 名博士生,两人独立标注、第三人裁决)和 ProofNet-Verified(An/Min/Si/Bastani;人工 + AI agent,并给出证明或否命题证明)是两个团队、两套判定,标签互相独立。我用「题号 + 非形式陈述模糊匹配(ratio>0.8)」把两边对齐,匹配上 257/367 题;再只保留 **ConsistencyCheck 的形式陈述和 ProofNet-Verified「原版」(proofnet-4.28)去空白后逐字相同**的 130 题,保证两边评的是同一个对象:
- 2×2(ReForm 判错, PNV 判错):(是,是) 54 /(否,否) 59 /(否,是) 17 /(是,否) **0**。一致率 86.9%,Cohen κ=0.74。
- 错误率:ReForm 41.5%,PNV 54.6%。ReForm 判错的题 PNV **全部**也判错;PNV 多出的 17 题以 missing_implicit_premise / nl_ambiguous / 按惯例补前提为主,其中 9 题 PNV 标 q3_provability=false(已给出否命题证明)。
- 结论:「ProofNet 原版约一半形式陈述不忠实」得到独立团队、独立标注的证实。两团队的差距来自判定严格度:PNV 是 ReForm 的超集,不存在互相矛盾的题。按同题比例 54.6/41.5≈1.32 折算,PNV 的 55.9% 大致对应 ReForm 尺度下的 42%,和 ReForm 自己报的 38.5%(论文)/48.2%(发布数据,见 X3)都在同一区间。
- 子集 43 题(CC 用原版陈述、ProofNet# 改过该题):ReForm 判错 40/43,PNV 判错 43/43。Poiroux 修正、ReForm 标注、PNV 审计三方同向,这是最强的三角互证。

**X2 · ProofNet# 99/367:独立证实「修过一轮仍有残余错」,幅度 PNV 偏高。** 在 87 题上 ProofNet# 没有改原版陈述,ConsistencyCheck 也用的正是这条陈述(三方文本相同)。这 87 题里 ReForm 独立判错 14 题(16.1%),PNV 判错 27 题(31.0%),仍然没有 ReForm 判错而 PNV 判对的题(κ=0.60)。所以 Poiroux 团队放行的陈述里,确有独立第三方确认的残余错误。这支持「ProofNet# 仍有错」这个方向。至于 27.0% 的具体幅度,ReForm 尺度下大约只有 PNV 的一半(这个子集不是随机样本:都是 Poiroux 当初认为没问题的题,所以偏低)。

**X3 · ReForm 自己的数字不能直接当「独立旁证数」用:发布数据和论文对不上。** 论文 §4.5 写 "16.4% of miniF2F and 38.5% of ProofNet's human-written formal statements contain semantic errors"。我按 data_source 统计 HF 发布的 859 条:miniF2F 110/488=**22.5%**,ProofNet 179/371=**48.2%**。论文数字反推的整数是 80/488 和 143/371,发布数据比它多 30 和 36 条。另外,标签里有一部分是写法偏好(例如 "use Polynomial.roots"、"use finsum"),不一定是语义错误。Round 2 三席都把 38.5% 当作逐字已核的独立数字;它逐字确实没错,但和作者自己发布的数据不一致。

**X4 · ProofNet-Verified 内部:逐题数据支持 README 的 205/195,不支持会议摘要的 104 条为假。** results.jsonl 复算:q4≠none 205(=195 不忠实 + nl_ambiguous 9 + nl_wrong 1);q3_provability=false **106**、independent 1,而 ICML 摘要写的是 104(28%)为假 + 100 不忠实但不假 = 204;ProofNet# 侧 99 题(其中 60 题为假)。8 类根因计数和 README 表逐项一致。需要披露的方法学事实:原版这一侧 367 条里有 261 条带 `cost_usd`/`duration_ms` 字段,每条 reasoning 都写成 "ORIGINAL vs CORRECTED" 对比。可见**错误分类这一步由 AI agent 拿原版去对照作者自己的修正版生成**,README 所说的人工 + agent 共识针对的是修正版是否忠实。这一点交方法学席判断,但它削弱了「每个错误都经人工逐条确认」的读法。

**X5 · miniF2F「97.5% vs 62.7%」:同一论文内部就有反向结果,独立测量方向不一。**
- 同论文 Table 3(@1):LLM 判官反而**低于**人工,Kimina v1 test 是 LLM 58.6% vs 人工 88.1%,Herald 是 49.6 vs 55.3。正文原句:"Here, the opposite pattern appears: the LLM evaluator assigns lower accuracies than the human evaluator."。所以「LLM 判官系统性高估 8–41pp」只在 @128 设定下成立。而且在 @128 下,"human evaluation is performed only on the first translation that successfully passes the Lean compiler, rather than on all 128 translations",LLM 和人工评的不是同一批对象(测量效度问题,交方法学席)。判官模型也换过:用 DeepSeek-V3 替代了 Herald 原用的 V2.5。Round 2 三席都没提 Table 3 的反向结果。
- 自动判官那一端有独立复现:Herald 作者用自家管线报 miniF2F-test @128 为 93.2%(v1 摘要)/ 96.7%(v2 正文;v2 摘要仍写 93.2%,论文内部不一致),和 97.5% 同量级。
- 人工那一端(62.7%)**没有找到第二份对 Herald 译文的独立人工评测**,属单源。
- 独立判官—人工对照,结果双向:
  - Xu/Quan/Freitas Table 4:fidelity judge 的漏放率(错误输出被判通过的比例)ProofNet 72.1%、miniF2F 只有 2.1%,每个数据集只标注 25 题且过采样分歧题。
  - ReForm Table 3:7 个前沿判官在 859 条上 accuracy 77–86%、precision 75.7–88.9、recall 79.0–96.9;以 Correct 为正类时,有的高估(Gemini recall/precision≈1.15),有的低估(GPT-5 ≈0.93)。
  - Zhang et al. 2606.31002:双判官严格准则 "rarely accepts an unfaithful output but rejects some faithful ones"(precision 44/46,负类确认 10/13)。
  - Poiroux BEq:precision≈100、recall 30.9–48.3,系统性低估。
  - 结论:LLM 判官会不会高估,取决于判官配置、采样预算和数据集。Herald 式 back-translation 管线 @128 大幅高估,这一点是单源已核;推广成「LLM 判官系统性高估」属于方向存争。
- 2506.10903 另外提供了一个背景事实:两名人类评审对同一组形式化的排序,精确一致只有 38%(miniF2F)/22%(ProofNet),说明「人工」本身也不是干净的金标准。

**X6 · miniF2F-v2「全部匹配」:有两条独立反证。** (a) Faults Table 4:v2c、v2s 各有 8 条 proven 问题(带机器证书)。(b) 我把 ConsistencyCheck 在 miniF2F 上判错的 110 题对照 v2 数据:v2s 改了其中 87 题的形式陈述(79%,对照组 CC 判对的题只改了 41.8%,说明两个独立审计高度同向)。但有 **11 题 v2s 和 v2c 的形式陈述与非形式陈述都没动**,而 ReForm 给的理由是实质性的,例如 mathd_algebra_282 "Goal is wrong, it is cubic root of $-8$ not cubic root of $8$"、imo_1987_p6 "n should be greater than or equal to 2"、mathd_numbertheory_64 "missing hypothesis that x is positive",另有 imo_1982_p1 和 mathd_algebra_170/275 的自然数减法、自然数除法问题。也有几题只是写法偏好(Polynomial.roots、finsum)。所以 v2 应写作「大幅修正」,不能写「完全对齐」。注:v2s 和 v1 相比改动了 50.2% 的形式陈述(含排版级改动),这只是「逾半错位」的一个上界,不能当证实。ReForm 在 v1 上的错误率(16.4%/22.5%)明显低于「逾半」,因为两者定义不同:Ospanov 的统计包含非形式侧的问题。

**X7 · Faults 398/399:复算没问题,没有独立复现;和 PNV 对照能看出它的召回很低。** Table 4 的 13 行复加:Find. 合计 4,833,Proven 合计 **398**,和 Total 行一致;正文 "4,833 findings and 399 proven issues" 是笔误级的内部不一致,表格支持 398。搜索没找到复现、回应或批评。独立对照:同一个 ProofNet original(371 题),Faults 只证实 5 条(ProofNet# 1 条),而 PNV 的逐题数据有 106 条已给出否命题证明。也就是说,静态检查器对语义不忠实的召回量级大约是 5%,398 只能当下限,不能当「错误率」。ProverBench 一行贡献 208(其中 Axiom 199),占 52%。

## 二、结局

**X 席:独立证实(方向)/ 部分独立矛盾(幅度与推广)**,逐项如下:
- ProofNet 原版约一半不忠实:**独立证实**(逐题 κ=0.74,零反向题)。PNV 的 55.9% 是严格口径的上沿;ReForm 尺度下大约 40–48%。
- ProofNet# 残余错误:**方向独立证实**;99/367 的幅度只有 PNV 单源,独立尺度下约为它的一半。
- 97.5% vs 62.7%:自动判官一端有作者自报的复现;人工一端是**单源**;「系统性高估 8–41pp」这一推广被同论文 Table 3 @1 和多份独立判官研究**矛盾**,结论是方向存争。
- Faults 398:**无独立测量**(复算成立);和 PNV 对照显示它是低召回的下限。
- miniF2F-v2 完全修正:**独立矛盾**(Faults 8 条 + ReForm 标出的 11 题未动)。

| 角度 | 查询/来源 | 结果 |
|---|---|---|
| ProofNet 逐题独立标注交叉 | HF ConsistencyCheck × PNV results.jsonl(130 题同文本) | 一致 86.9%,κ 0.74,0 反向;PNV 54.6% vs CC 41.5% |
| ProofNet# 残余 | 同上,87 题三方同文本子集 | CC 16.1% vs PNV 31.0%,0 反向 → 方向证实,幅度减半 |
| 三方互证 | 43 题 ProofNet# 改过的题 | CC 40/43、PNV 43/43 判错 |
| ReForm 数字自洽 | 发布 jsonl 复算 | 22.5%/48.2% ≠ 论文 16.4%/38.5% |
| PNV 内部 204/205/104 | results.jsonl 复算 | 205 / 195 / false 106;不支持摘要的 104 |
| PNV 标注程序 | results.jsonl 字段 | 261 条带 cost_usd:分类由 AI agent 生成 |
| miniF2F 判官 vs 人工(同源) | 2511.03108 Table 3 @1 | 反向:LLM < 人工(58.6 vs 88.1) |
| 自动判官复现 | Herald 2410.10878 v1/v2 | 93.2%/96.7% @128,同量级 |
| Herald 译文第二份人工评测 | 网络搜索(Herald/Kimina human evaluation miniF2F) | 未找到 |
| 独立判官—人工对照 | 2606.09449 T4;2510.24592 T3;2606.31002 T1/2;2406.07222 BEq | 双向:有的高估(ProofNet 漏放 72%),有的低估(严格双判官、BEq) |
| 人工金标准稳定性 | 2506.10903 §3 | 两名评审排序精确一致 38%/22% |
| miniF2F-v2 残余 | Faults T4;CC × v2s/v2c 文本对照 | 8 条 proven;11 题被 CC 判错但 v2 未动 |
| Faults 复现/回应 | 网络搜索;atp-checkers 仓库 | 无复现、无逐题数据;T4 复加 398 |
| Faults 召回 | T4 ProofNet 行 × PNV q3=false | 5 vs 106 |
| 勘误/撤稿 | arXiv 版本、会议页搜索 | 无 |

成文建议(供方法学席与成文参考):
- 最强写法:「两个互不相关的团队逐题审计同一批 ProofNet 形式陈述,结论高度一致(κ≈0.74):约四到五成半与题意不符;更严的那个团队判错的题完全包含另一团队判错的题。」
- ProofNet# 写「仍有约 15–30% 残余错误(两团队尺度不同)」。
- 97.5/62.7 必须带三个限定:@128、Herald 管线、人工只评首个能编译的译文;同时写明 @1 下方向相反。
- 禁止写「LLM 判官系统性高估 8–41pp」。
- ReForm 的 38.5% 如果引用,要注明发布数据为 48.2%。
