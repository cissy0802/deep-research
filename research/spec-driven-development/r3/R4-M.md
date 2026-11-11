# R3 · R4-M 方法学审计席(有否决权)

靶子:TiCoder(Fakhoury, Naik, Sakkas, Chakraborty, Lahiri, IEEE TSE 2024 / arXiv 2404.10100)的用户研究数字(P14 正确判断 0.40→0.84 p=0.001;P15 NASA-TLX 45.46→28.00、时间不显著)与标题数字(P17「平均绝对提升 45.97% / 45.73% / 38.43%」;P16 Table IV 增幅),以及 P19 的二次转述。G03。

今天复核了:
- arXiv 2404.10100v2 PDF(今日重新下载;`pdftotext -layout` 文本与作者 Naik GitHub Pages 仓库的 tse24_ticoder.pdf 文本逐行 diff 为空,即「TSE 版」PDF = v2)
- arXiv 2404.10100v1 PDF(今日重新下载)
- TSE 正式版摘要(Semantic Scholar API,DOI 10.1109/TSE.2024.3428972;摘要写 45.97%、「15 programmers」、「four different state-of-the-art LLMs」;S2 计 179 次引用)
- Smfakhoury/TiCoder-project(README + TiCoder.pdf,= v1 口径 38.43%)
- microsoft/TiCoder 代码仓库(git clone --depth 1,最近提交 2025-05-16)
- 前身 arXiv 2208.05950 摘要(Lahiri et al. 2022)、CodeT arXiv 2207.10397 摘要(仅作外部参照)
- 复算脚本:scratchpad `r4m/denom2.py`(Table III 分母可行性)、`r4m/t4.py`(Table IV 全部口径穷举)、scipy 精确检验

没拿到:
- 用户研究逐人原始数据(正确与否、TLX 各题、时间、条件-任务-顺序分配)——论文与两个仓库均未公开
- 混合效应模型的系数、SE、CI、软件与具体设定(只报 p 值和「mean」)
- Table IV 的生成缓存(100 代码 + 50 测试/模型/数据集)与 v1→v2 修订说明;code-davinci-002 / text-davinci-003 已下线,Table IV 实际不可复跑
- IEEE Xplore 正式版全文页(未尝试绕过;以 v2 = 作者托管 TSE PDF 为准)

## 一、发现

### A. 用户研究(P14/P15/P19)

**F1 样本构成可由 Table I 精确定出:最终 15 人 = 6 业界 + 9 学术界,不是「专业开发者」。**
v2 Table I(PDF p.7,文本第 372–390 行)逐行列出 3 名 Pilot(全部 Industry)+ P1–P15。P1–P15 中 Industry:P1、P2、P3、P4、P7、P15 = 6;Academia:P5、P6、P8–P14 = 9。正文「8 participants are either professional software engineers or researchers at Microsoft, and the remaining 10 participants are PhD students」(第 354–356 行)与表不符:表为 3+6=9 业界、9 学术(合计 18),正文为 8+10。Round 2 只指出「15 人内部划分文中未给」,这里由同文表格直接给出:**最终样本 60% 为学术界(博士生),业界仅 6 人**。另:定性部分引用「P19 first asked …」(PDF p.10,第 613 行),而 Table I 只编号到 P15——参与者编号体系与表不一致,可能存在未披露的招募/流失(推断)。

**F2 「mean correctness 0.84 / 0.64」不可能是 15 个二元结果的原始比例。**
设计:组内、Latin square、15 人 × 3 任务,每人每条件恰 1 题(§V-C,第 439–447 行),故每条件 n=15,原始比例只能是 k/15 ∈ {…, 0.60, 0.667, 0.80, 0.867, …}。0.40 = 6/15 可行;**0.84、0.64 在任何四舍五入规则下都不等于 k/15**(12/15=0.80,13/15=0.867;9/15=0.60,10/15=0.667)。正文称其为「The mean correctness was 0.40 … 0.84 … 0.64」(§VI-A,第 526–527 行),表头为「(mean)」。最可能是 logistic 混合模型的模型估计值被当作「mean」报告,或存在缺失/不平衡观测——论文未交代。Round 2 的「均为 1/25 倍数」只是巧合描述;要点是:**0.84 不是「84% 的参与者判断正确」**。

**F3 Table III 的 TLX 数值不能由任何一致的整数响应 n 产生,且 A1 列内部不自洽。**
复算(denom2.py):对每列(条件)所有 TLX 量(各 0–20 整数题项、Load = 5 题之和)枚举 n=5…30,要求所有显示值都能写成 k/n 四舍五入:**A1、A2、A3 三列均无共同可行 n**(用截断规则则 A1→15、A2→26、A3→17,彼此矛盾)。加总恒等式:Load 应 = Mental + Stress + Pace + Effort + (20 − Confidence/感知成功)。A2:23.87+4.08=27.95 vs 表 28.00;A3:25.35+4.12=29.47 vs 29.52(均在舍入误差内);**A1:39.89+6.50=46.39 vs 表 45.46,差 0.93**,远超舍入。在平衡完整的组内设计下,线性模型的边际均值等于原始均值且可加,A1 的不可加说明 A1 存在缺失/不平衡数据或誊录错误(推断;无原始数据无法定论)。

**F4 同节自相矛盾:单元格 n=5 却报告「50%」。**
15 人 / 3×3 Latin square ⇒ 每个「任务×条件」单元格 5 人。正文:Task 2 在 Assistant 3 下「50% of the participants indicated that the test should evaluate to 0, and the other 50% …」(第 559–560 行;v1 第 507–508 行同句)。5 人无法对半分。与 F2/F3 一起指向:实际分配或可分析观测并非论文声称的「each AI assistant is used an equal number of times across all tasks and positions」(第 444–447 行)。另,同段既写「Latin Square Design」又写「The order … is randomized」,两者不是一回事,具体分配未公开。

**F5 p=0.001 对 n=15 明显反保守;任何精确检验都给不出这么小的 p。**
A1 原始 = 6/15(F2)。A2 即便取最有利的 13/15:
- 配对精确 McNemar(每人 A1、A2 各一题):正确数差 ≥7,最小可能 p = 2×0.5^7 = **0.0156**(全部不一致对都偏向 A2 的极端情形);b=8,c=1 → 0.039;b=9,c=2 → 0.065。
- 忽略配对的 Fisher 精确:6/15 vs 13/15 → p=0.021;vs 12/15 → p=0.060。
论文报告的是 logistic GLMM(participant、task 为随机效应)+ ANOVA omnibus + FDR 后的「p=0.001」,比精确检验下限小 ~15 倍。15 个聚类、task 随机效应只有 3 个水平(方差基本不可估),Wald/LRT 近似在此规模下不可信。且 §V-E 原文「We only report Omnibus p-values for pairs of conditions」(第 545–547 行)——报告的究竟是 omnibus p 还是 FDR 校正后的两两对比 p,自相矛盾。**方向可信,p 值量级不可承重。** 无系数、无 CI、无效应量。

**F6 处理效应部分由设计直接制造。**
§V-A(第 377–391 行):「We restrict the number of pruned codes in each task so that a participant using Assistant 2 or 3 will always see between 3-4 code suggestions if they correctly evaluate the tests」——作者人为设定处理条件剪掉 1–2 个错误候选;对照组看 5 个(4 错 + 1 MBPP 参考解,第 461–463 行)。即纯随机猜测基线就从 1/5 升到 1/4–1/3。任务选择标准之一是「the LLM could generate reasonable tests that capture the diverse error types」(§V-B)——选的是 TiCoder 测试恰好能区分错误的题。结论「测试辅助提升判断正确率」部分是「干扰项更少」的机械后果,论文未做分解。

**F7 其他效度问题。**
- 招募为「distribution lists and personal contacts」(第 350 行)的便利样本;作者是方法提出方(Microsoft Research ×3,另两位 UPenn/UCSD),访谈者在场、视频会议记录(第 358、606–616 行),条件不可盲,TLX 为自报——需求特征/实验者效应无控制。
- 时间:327.7 / 284.15 / 253.88 秒,A3 比 A1 少 22%,n=15 下不显著。**这是「功效不足、无法判断」,不是「不省时间」**。Round 2 K 席最强写法「但不省时间」把不显著写成了等价,属方法学错误。
- 讨论节(v2 第 780 行附近,v1 第 745–748 行)写「both Assistant 2 and Assistant 3 are statistically distinguishable from Assistant 1」并称「participants that were shown test cases … performed significantly better」——但正确率只有 A2 显著(Table III),A3 只在负荷维度显著。作者自己的总结已有拔高。

**F8 二次转述漂移(P19)被 F1 加重。** Lahiri 博客/立场文「15 professional developers … p < 0.001」:按 Table I,15 人中仅 6 人为业界;p 也从 0.001 写成 <0.001。且 F5 表明连 0.001 本身都偏乐观。

### B. 标题数字与 Table IV(P16/P17)

**F9 标题「平均绝对提升」三个版本均不能由同文 Table IV 复现(独立复算确认,并穷举了其他可能口径)。**
t4.py 对 v2 Table IV(PDF p.12,第 680–695 行)穷举:{全部 7 模型 / 4 旧模型 / 3 对话模型} × {PassFail, Output} × m=1…5 × {绝对差均值、相对增幅均值、均值的相对增幅} × {合并、仅 MBPP、仅 HE}。
- 正文口径(Output、m=5、全部 14 组)= **33.50 pp**;4 旧模型 = 43.94 pp;PassFail m=5 全部 = 26.33 pp。
- 离 45.97/45.73 最近的候选是「全部、PassFail、m=2、均值的相对增幅」45.60% 与「4 旧模型、Output、m=5、仅 MBPP」44.47 pp——都不是文中所述口径,也不吻合。**没有任何合理口径能给出 45.97 或 45.73。**
- v1(8 组旧模型):Output m=5 = 38.19 pp vs 声称 38.43%。v1 HumanEval text-davinci-003 Output 行 m=4/m=5 为 77.71/77.36(非单调,疑列错位);即使互换,均值 38.23,仍不到 38.43。
- 版本谱系:2208.05950(2022,Codex)摘要「22.49%–37.71%(MBPP)、24.79%–53.98%(HumanEval)」→ v1 38.43% → v2/TSE 45.97%(摘要)/45.73%(正文)。TSE 摘要(S2)= 45.97%,且摘要仍写「four different … LLMs」而表为 7 个模型。

**F10 v1→v2 只有 Output 列被整体上调,baseline 与 PassFail 列逐字未变。**
对 8 个共有行比较:baseline pass@1/pass@100 与 PassFail m=1…5 全部相同;Output 列全部上调(如 CodeGen-6B HE m=5 33.14→48.12,+14.98;text-davinci-003 MBPP m=1 73.67→77.00)。同一缓存、同一模拟用户,只有一种设置的数值变化,论文无任何说明(在 v2 全文 grep 范围内)。这是未解释的版本漂移,直接推高标题数字(38→46)。

**F11 v2 的文字结论被其自己的新表推翻。**
- 「T I C ODER -PASS FAIL … always stays within 9% of the benefits of T I C ODER -O UTPUT」(第 758–760、770 行):v1 表下成立(最大差 6.46 pp);**v2 表下 5 行超 9 pp**:CodeGen-6B HE 18.56、CodeGen-6B MBPP 12.89、CodeGen2.5-7B HE 15.92、CodeGen2.5-7B MBPP 10.84、code-davinci-002 HE 10.13。句子是从 v1 遗留的。
- 「text-davinci-003 … T I C ODER -O UTPUT … This increases to 38.55% with 5 queries」(第 732–733 行):按表 83.75−49.16 = **34.59 pp**;38.55 = 87.71(code-davinci-002 的 m=5)− 49.16(text-davinci-003 的 baseline),跨行混算。v1 同处更乱:写「text-davinci-003 from 48.25% to 68.42%」实为 code-davinci-002 行数字。

**F12 Table IV 的「增益」不能归因于用户交互。**
- 模拟用户 = 参考实现(§VII-D),正确性评判 = 同一参考实现对应的隐藏测试:作者自称「upper bound」。
- 对比的 baseline 是采样意义的 pass@1,TiCoder 是确定性排名 top-1(pass@k@m,作者自承「not a statistical measure」,p.10–11);没有「m=0、仅用生成测试重排」的对照。CodeT(2207.10397)在无任何用户的情况下仅靠测试重排就让 code-davinci-002 HumanEval pass@1 +18.8 pp(设定不同:CodeT 保留 docstring 样例,TiCoder 删除)。TiCoder 同模型 PassFail m=1 为 +21.17 pp——**相当大一部分「交互增益」可能是零交互重排即可获得的**(推断,无法在本文数据内分解)。
- 每模型每数据集只查询一次生成缓存(单次采样,temperature 0.8),无重复、无方差/CI;两个 Codex 系模型已下线,缓存未公开 ⇒ 不可复现。
- PassFail 列 3 处 m 增加反而下降(MBPP GPT-3.5 79.04→79.03、GPT-4-turbo 83.20→83.12;HE GPT-4-turbo 80.92→80.84),与「performance improvements increasing with every test validation interaction」(Key Findings)不符(幅度小,属文字拔高)。

**F13 利益冲突。** 方法提出方自评;大规模评估与用户研究同一团队;第一作者后续(Lahiri 2026 立场文/博客)用本文作为「intent formalization」议程的主要实证,且转述持续拔高(F8)。无独立复现(仅检到学生仓库 JoaoTeles87/TAES-TiCoder-Reproduction 与 mohammedEbdah/ticoder-soft-scoring,未审,不作证据)。

## 二、结局

**M 席评级:**
- 用户研究正确率/负荷(P14/P15):**C**——方向可作弱结论,数值与 p 值不可承重。
- 标题「平均绝对提升」(P17):**D**——否决。
- Table IV 单元格(P16):**C+**——可原样引用为「作者报告的模拟理想用户上界、单次运行」,不得解读为用户交互带来的增益幅度。
- 二次转述(P19):**D**(作为事实);只能作为「作者转述口径漂移」的例证引用。

**否决清单(不得承重):**
- **V1** 「平均绝对提升 45.97% / 45.73% / 38.43%」(及「约 46 个百分点」「近 40 个百分点」等任何变体)。同文表复算 33.50 pp(全部)/ 43.94 pp(旧模型);穷举无口径可复现;v1→v2 仅 Output 列未解释上调。
- **V2** 「84% 的参与者判断正确」「正确率从 40% 升到 84%」作为参与者比例;0.84/0.64 不是 15 人二元结果的原始比例(F2)。可写「作者报告的模型均值 0.40→0.84」。
- **V3** 「p=0.001」「p<0.001」作为证据强度。15 人下精确配对检验的下限为 p≈0.016,合理范围 0.016–0.065(F5)。
- **V4** 「15 名专业开发者」;最终样本为 6 业界 + 9 学术界(Table I)。
- **V5** 「TiCoder 不省时间」/「耗时相同」。只能写「耗时差异未达显著(n=15,功效不足以判断)」。同理,不得写「认知负荷下降 38%」之类精确相对幅度(自报、非盲、A1 列不自洽)。
- **V6** 「TiCoder-Output 也显著提升正确判断」/「两种测试辅助都显著」(A3 正确率不显著)。
- **V7** 「PassFail 始终在 Output 的 9% 以内」(v2 表下 5 行超 9 pp,最大 18.56)。
- **V8** 把 Table IV / 对话模型「13–22 pp」写成「用户与测试交互带来的提升」:无零交互重排对照、参考实现作 oracle、单次运行;只能写「作者以参考实现模拟理想用户得到的上界」。
- (延续 R2)**V9** Table V「测试入提示」67.13→80.88 作为无泄漏效果。

**可承重的最强写法:**
> 方法提出方(Microsoft Research 团队)做过一项 15 人的小型组内实验(6 名业界、9 名学术界参与者,每人每种条件只做一道 MBPP 改编短题;处理条件下系统按设计剪掉 1–2 个错误候选)。让用户先确认 LLM 生成的测试,再从候选代码中挑正确者,判断正确的比例明显更高(作者报告的模型均值 0.40→0.84),自报认知负荷也更低;耗时差异未达显著,但样本太小,无法判断是否省时。另一种「用户填写期望输出」的变体正确率提升不显著。论文的大规模评估用参考实现扮演「理想用户」,作者自称是上界,且摘要中「平均绝对提升 45.97%」无法由同文表格复现(按表重算约 33.5 个百分点),不宜引用。

**证据分级建议:**
- 「测试确认 → 判断 AI 代码正确率提高、自报负荷降低」:**单源已核(仅方向,弱结论)**——一手可回溯,但样本 15、数值内部不一致、作者自评、设计内含机械效应。
- 「不显著节省时间」:**未验证**(功效不足,既不能说省也不能说不省)。
- Table IV 具体单元格:**单源已核(上界口径)**,必须随文带「参考实现模拟用户、单次运行、作者自评」。
- 标题「平均绝对提升 45.97%」:**弃用**。
- 「15 名专业开发者,p<0.001」:**弃用**(仅可作为转述漂移案例,标注一手 Table I 与 p=0.001)。
