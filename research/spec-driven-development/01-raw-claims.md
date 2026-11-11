# 01 Round 1 原始论断(7 线合并)

> 运行约束:本会话网络策略拦截 arXiv/ACM/IEEE/Dagstuhl/martinfowler.com/uvik.net/厂商站点等;一手原文主要经 GitHub 仓库(作者仓库、LaTeX 源、复现包、博客源仓库)取得。confidence=secondhand 的条目 quote 为空,验证阶段优先回一手。


# 线 PRO

## P01 (PRO)
- 论断:Self-planning(先由 LLM 生成编号式解题计划、再按计划写代码)在 HumanEval 上把 code-davinci-002 的 Pass@1 从 48.1% 提到 60.3%(相对 +25.4%,绝对 +12.2 pp);对 Code CoT 的相对优势最高 11.9%。'up to' 是四个基准中的最大值,不是平均值。
- 原文:Experimental results show that self-planning code generation achieves a relative improvement of up to 25.4% in Pass@1 compared to direct code generation, and up to 11.9% compared to Chain-of-Thought of code generation.
- URL:https://github.com/ligechina/ligechina.github.io/blob/master/My%20Papers/2024%20-%20TOSEM%20-%20Self-Planning%20Code%20Generation%20with%20Large%20Language%20Model.pdf
- 来源:Jiang, Dong, Wang, Fang, Shang, Li, Jin, Jiao, 2024, Self-Planning Code Generation with Large Language Models, ACM TOSEM 33(7) Art.182(arXiv 2303.06689;PDF取自作者组 Ge Li 的 GitHub Pages 仓库) · 2024-09 · 【研究】 · T2 · 基准 · verbatim-checked
- 备注:基座模型 code-davinci-002(已下线);8-shot 人工编写的计划示例;单次贪心解码(temperature 0)、只取一个计划,未报告重复运行或显著性检验(文中 'significant' 为非统计用语)。作者为方法提出者。计划由模型自生成,非人写 spec。

## P02 (PRO)
- 论断:Self-planning 在其余三个基准上的增益更小:HumanEval-ET 37.2→46.2(+24.1% 相对)、MBPP-sanitized 49.8→55.7(+11.8%)、MBPP-ET 37.7→41.9(+11.2%);绝对增幅 4.2–12.2 pp。作者自承在 MBPP 上增益明显较小。
- 原文:Overall, the self-planning approach showed a more significant improvement on HumanEval compared to on MBPP-sanitized.
- URL:https://github.com/ligechina/ligechina.github.io/blob/master/My%20Papers/2024%20-%20TOSEM%20-%20Self-Planning%20Code%20Generation%20with%20Large%20Language%20Model.pdf
- 来源:Jiang, Dong, Wang, Fang, Shang, Li, Jin, Jiao, 2024, Self-Planning Code Generation with Large Language Models, ACM TOSEM 33(7) Art.182(arXiv 2303.06689;PDF取自作者组 Ge Li 的 GitHub Pages 仓库) · 2024-09 · 【研究】 · T2 · 基准 · verbatim-checked
- 备注:数字取自 Table 1(code-davinci-002,Pass@1,贪心单次)。CodeBLEU 上 self-planning 反而略低于 Code CoT(HumanEval 28.6 vs 30.4)。

## P03 (PRO)
- 论断:Self-planning 论文的 'Ground-truth Planning' 上界(HumanEval Pass@1 74.4%,相对 +54.7%)所用的计划是用参考答案代码反向生成的,因此含答案信息泄漏,不能解读为'人写好 spec 的收益'。
- 原文:we utilize the existing ground-truth code to inversely generate a plan, which we then adopt as the ground-truth plan in our experiments.
- URL:https://github.com/ligechina/ligechina.github.io/blob/master/My%20Papers/2024%20-%20TOSEM%20-%20Self-Planning%20Code%20Generation%20with%20Large%20Language%20Model.pdf
- 来源:Jiang, Dong, Wang, Fang, Shang, Li, Jin, Jiao, 2024, Self-Planning Code Generation with Large Language Models, ACM TOSEM 33(7) Art.182(arXiv 2303.06689;PDF取自作者组 Ge Li 的 GitHub Pages 仓库) · 2024-09 · 【研究】 · T2 · 基准 · verbatim-checked
- 备注:作者称其为 'underestimated upper bound';人工抽检 HumanEval 上约 3% 的反推计划步骤描述不佳。SDD 叙事若引用 '+50% 以上' 需注明这是由答案代码反推的计划。

## P04 (PRO)
- 论断:计划先行的收益依赖模型能力:Table 3 中 code-cushman-001(13B)用 self-planning 后 HumanEval Pass@1 从 34.0% 降到 30.1%,≤6.7B 的模型为 0 或接近 0;175B 的模型才稳定受益(如 text-davinci-003 55.1→65.4)。
- 原文:At 175B, self-planning approach consistently outperforms the Direct approach across all models.
- URL:https://github.com/ligechina/ligechina.github.io/blob/master/My%20Papers/2024%20-%20TOSEM%20-%20Self-Planning%20Code%20Generation%20with%20Large%20Language%20Model.pdf
- 来源:Jiang, Dong, Wang, Fang, Shang, Li, Jin, Jiao, 2024, Self-Planning Code Generation with Large Language Models, ACM TOSEM 33(7) Art.182(arXiv 2303.06689;PDF取自作者组 Ge Li 的 GitHub Pages 仓库) · 2024-09 · 【研究】 · T2 · 基准 · verbatim-checked
- 备注:4-shot 设置(受输入长度限制)。说明'先计划'不是普适增益,存在模型能力门槛;与 2024–2026 年前沿模型的可迁移性未测。

## P05 (PRO)
- 论断:第三方(MapCoder 作者)在 GPT-4 上复跑 Self-Planning 的结果方向不一:HumanEval 85.4% vs Direct 80.1%(+),但 MBPP 75.8% vs 81.1%、MBPP-ET 50.4% vs 54.7%、HumanEval-ET 62.2% vs 73.8%(均为负)。
- 原文:| | Self-Planning | 85.4% | 62.2% | - | 75.8% | 50.4% | 14.7% | 34.0% | 10.9%  |
- URL:https://github.com/Md-Ashraful-Pramanik/MapCoder/blob/main/README.md
- 来源:Islam, Ali, Parvez, 2024, MapCoder: Multi-Agent Code Generation for Competitive Problem Solving, ACL 2024(官方仓库 README 结果表) · 2024-05 · 【研究】 · T2 · 基准 · verbatim-checked
- 备注:MapCoder 作者是竞争方法提出者(有动机压低基线)。同表 GPT-4 Direct 行:80.1/73.8/81.1/54.7。这是反方向证据,放 PRO 线以免单向引用。另见 P06 的口径问题。

## P06 (PRO)
- 论断:口径疑点:MapCoder README 中 'ChatGPT' 行的 Direct(48.1/37.2/49.8/37.7)与 Self-Planning(60.3/46.2/55.7/41.9)数字与 Self-planning 论文 Table 1 中 code-davinci-002 的数字完全一致,疑为把 code-davinci-002 结果挪作 ChatGPT 行;引用 MapCoder 的 ChatGPT 对比时不可当作独立复现。
- 原文:| ChatGPT | Direct   | 48.1% | 37.2% | 66.5% | 49.8% | 37.7% | 8.0%  | 17.9% | 5.5%   |
- URL:https://github.com/Md-Ashraful-Pramanik/MapCoder/blob/main/README.md
- 来源:Islam, Ali, Parvez, 2024, MapCoder, ACL 2024(官方仓库 README) · 2024-05 · 【研究】 · T2 · 基准 · verbatim-checked
- 备注:本条为本线交叉比对所得推断,非任一来源自述;需验证阶段回 MapCoder 论文原表核对其脚注。

## P07 (PRO)
- 论断:MapCoder(检索→计划→编码→调试四代理)在 GPT-4 上 HumanEval Pass@1 93.9%(Direct 80.1%)、CodeContests 28.5%(Direct 12.1%);但计划代理与检索、调试捆绑,README 表无法分离'计划'本身的贡献。
- 原文:Our framework, MapCoder, consists of four LLM agents specifically designed to emulate the stages of this cycle: recalling relevant examples, planning, code generation, and debugging.
- URL:https://github.com/Md-Ashraful-Pramanik/MapCoder/blob/main/README.md
- 来源:Islam, Ali, Parvez, 2024, MapCoder, ACL 2024(官方仓库 README) · 2024-05 · 【研究】 · T2 · 基准 · verbatim-checked
- 备注:调试代理使用题面样例 I/O 执行反馈;是'流程整体'证据,不是'先写 spec'的单因素证据。论文内消融未读到原文(arXiv 不可达)。

## P08 (PRO)
- 论断:Self-collaboration(分析师→编码→测试三角色)消融:ChatGPT(GPT-3.5)仅 Coder 时 HumanEval Pass@1 45.1%,加 Analyst(需求分解+计划)为 54.9%(相对 +21.8%),加 Analyst+Tester 为 63.5%(+40.8%);HumanEval-ET 35.3→45.2→51.9。
- 原文:+ Analyst                            54.9 (↑ 21.8%)                     45.2 (↑ 28.1%)
- URL:https://github.com/ligechina/ligechina.github.io/blob/master/My%20Papers/2024%20-%20TOSEM%20-%20Self-collaboration%20Code%20Generation%20via%20ChatGPT.pdf
- 来源:Dong, Jiang, Jin, Li, 2024, Self-Collaboration Code Generation via ChatGPT, ACM TOSEM 33(7) Art.189, Table 4 · 2024-09 · 【研究】 · T2 · 基准 · verbatim-checked
- 备注:与 Self-planning 同一课题组(北大 Ge Li 组)。单基准、单模型;Table 4 未报告方差或重复次数(本线未逐页核实其实验设置)。Analyst 的产物是任务分解+高层计划,近 T2。

## P09 (PRO)
- 论断:Structured CoT(先用顺序/分支/循环结构写伪代码式推理再出代码)在 gpt-4-turbo、gpt-3.5-turbo 与 DeepSeek Coder 系列上,相对普通 CoT 的 Pass@1 增幅'最高' 13.79%(HumanEval)、12.31%(MBPP)、13.59%(MBCPP)。
- 原文:SCoT prompting outperforms CoT prompting by up to 13.79% in Pass@1.
- URL:https://github.com/ligechina/ligechina.github.io/blob/master/My%20Papers/2025%20-%20TOSEM%20-%20Structured%20Chain-of-Thought%20Prompting%20for%20Code%20Generation.pdf
- 来源:Li, Li, Li, Jin, 2025, Structured Chain-of-Thought Prompting for Code Generation, ACM TOSEM 34(2) Art.37 · 2025-01 · 【研究】 · T2 · 基准 · verbatim-checked
- 备注:同课题组。比较对象是 CoT 而非 Direct;'up to' 为最大值。摘要列举'two LLMs'却给出五个模型,文本自身有笔误。

## P10 (PRO)
- 论断:ClarifyGPT 人类反馈实验:GPT-4 在 MBPP-sanitized 上 Pass@1 从 70.96% 提到 80.80%,MBPP-ET 51.52%→60.19%(平均相对 +15.35%);对 Default 的提升 p=3.2e-05 与 7.3e-05;对最强基线(CoT 或 GPT-Engineer)相对 +9.53%/+9.52%。
- 原文:The results show that ClarifyGPT elevates the performance (Pass@1) of GPT-4 from 70.96% to 80.80% on MBPP-sanitized.
- URL:https://github.com/linshi-website/linshi-website.github.io/blob/master/paper/ClarifyGPT.pdf
- 来源:Mu, Shi, Wang, Yu, Zhang, Wang, Liu, Wang, 2024, ClarifyGPT: A Framework for Enhancing LLM-Based Code Generation via Requirements Clarification, Proc. ACM Softw. Eng. 1(FSE) Art.103(PDF取自作者 Lin Shi 的 GitHub Pages 仓库) · 2024-07 · 【研究】 · T1 · 对照实验 · verbatim-checked
- 备注:10 名参与者(3 博士生、2 硕士生、2 资深研究者、3 业界开发者),每人 42 题,每题 3 人回答取平均;427 题中 ClarifyGPT 判定 140 题含糊并提问(平均 2.85 问/题),其余 287 题无交互。每法跑 3 次取平均。作者含华为一名。

## P11 (PRO)
- 论断:ClarifyGPT 人类实验的关键限定:给参与者的问卷中包含带期望输入/输出的单元测试,澄清回答是在看过测试样例后作出的——即 T1 澄清收益中混入了 T4(测试)信息。
- 原文:(2) the unit test cases containing expected input-output examples, which assist participants in understanding the problem’s intent;
- URL:https://github.com/linshi-website/linshi-website.github.io/blob/master/paper/ClarifyGPT.pdf
- 来源:Mu, Shi, Wang, Yu, Zhang, Wang, Liu, Wang, 2024, ClarifyGPT: A Framework for Enhancing LLM-Based Code Generation via Requirements Clarification, Proc. ACM Softw. Eng. 1(FSE) Art.103(PDF取自作者 Lin Shi 的 GitHub Pages 仓库) · 2024-07 · 【研究】 · mixed · 对照实验 · verbatim-checked
- 备注:基准测试是否与问卷中的测试重叠,文中未说明;若为同一批可见测试,则存在评测泄漏风险。验证阶段应核对 MBPP-sanitized 提示中本就附带 3 个测试的惯例。

## P12 (PRO)
- 论断:ClarifyGPT 模拟用户实验:GPT-4 五个基准平均 Pass@1 62.43%→69.60%(相对 +11.66%),ChatGPT 54.32%→62.37%(+15.00%);模拟用户由 LLM 扮演,并被给予 ground-truth 测试用例来作答。
- 原文:we propose a high-fidelity user simulation method that leverages LLMs to generate user responses by providing LLMs with clarifying questions and ground-truth test cases.
- URL:https://github.com/linshi-website/linshi-website.github.io/blob/master/paper/ClarifyGPT.pdf
- 来源:Mu, Shi, Wang, Yu, Zhang, Wang, Liu, Wang, 2024, ClarifyGPT: A Framework for Enhancing LLM-Based Code Generation via Requirements Clarification, Proc. ACM Softw. Eng. 1(FSE) Art.103(PDF取自作者 Lin Shi 的 GitHub Pages 仓库) · 2024-07 · 【研究】 · mixed · 基准 · verbatim-checked
- 备注:模拟器持有隐藏测试=评测答案信息,属于理想化上界;作者在威胁效度中承认低保真模拟会误导但以'接近人类结果'作辩护。五基准:HumanEval、HumanEval-ET、MBPP-sanitized、MBPP-ET、CoderEval。

## P13 (PRO)
- 论断:ClarifyGPT 版本口径差:2023-10 arXiv 预印本(据二手摘要)报告四个基准上 GPT-4 平均 +11.52%、ChatGPT +15.07%;FSE 2024 正式版为五个基准上 +11.66% 与 +15.00%。引用时须标明版本。
- 原文:in comparison with the default GPT-4, ClarifyGPT achieves an average improvement of 11.66% across five benchmarks; in comparison with the default ChatGPT, ClarifyGPT achieves an average improvement of 15.00% on five benchmarks.
- URL:https://github.com/linshi-website/linshi-website.github.io/blob/master/paper/ClarifyGPT.pdf
- 来源:Mu, Shi, Wang, Yu, Zhang, Wang, Liu, Wang, 2024, ClarifyGPT: A Framework for Enhancing LLM-Based Code Generation via Requirements Clarification, Proc. ACM Softw. Eng. 1(FSE) Art.103(PDF取自作者 Lin Shi 的 GitHub Pages 仓库);预印本 arXiv 2310.10996v1 数字为二手 · 2024-07 · 【研究】 · T1 · 基准 · paraphrase-checked
- 备注:正式版数字逐字核对;预印本数字仅来自搜索摘要(arxiv.org 在本会话不可达),未回一手。

## P14 (PRO)
- 论断:TiCoder 用户研究(15 人,组内设计,3 个 MBPP 改编任务,每任务限时 15 分钟):对 AI 生成代码作出正确判断的比例,对照组(仅看 5 个代码候选)0.40,TiCoder-PassFail(用户判测试通过/失败)0.84(p=0.001),TiCoder-Output(用户给出期望输出)0.64(不显著)。
- 原文:The mean correctness was 0.40 for participants using Assistant 1, 0.84 Assistant 2, and 0.64 Assistant 3. Although the mean is higher in Assistant 2 and 3, the effect is significant for Assistant 2 only with (p=0.001).
- URL:https://github.com/aadityanaik/aadityanaik.github.io/blob/master/assets/papers/tse24_ticoder.pdf
- 来源:Fakhoury, Naik, Sakkas, Chakraborty, Lahiri, 2024, LLM-based Test-driven Interactive Code Generation: User Study and Empirical Evaluation, IEEE TSE 50(9)(arXiv 2404.10100v2;PDF取自作者 Naik 的 GitHub Pages 仓库) · 2024-10 · 【研究】 · T4 · 对照实验 · verbatim-checked
- 备注:作者全部或主要为 Microsoft Research(方法提出方)。混合效应回归+FDR 校正。参与者:18 人中 3 人作试点;'8 participants are either professional software engineers or researchers at Microsoft, and the remaining 10 participants are PhD students'(8+10=18,与最终 15 人的划分在文中未说清)。每人每个条件只做 1 个任务,样本极小。

## P15 (PRO)
- 论断:TiCoder 用户研究:NASA-TLX 认知负荷(0–100)对照 45.46,PassFail 28.00(p=0.007)、Output 29.52(p=0.012);完成时间 327.7 / 284.15 / 253.88 秒,差异不显著——即'先把意图形式化为测试'未显著节省时间,但降低自报负荷。
- 原文:While we do not observe a statistically significant impact on the time taken to evaluate AI-generated code suggestions when using T I C ODER, we do observe a significant reduction in the amount of cognitive effort required.
- URL:https://github.com/aadityanaik/aadityanaik.github.io/blob/master/assets/papers/tse24_ticoder.pdf
- 来源:Fakhoury, Naik, Sakkas, Chakraborty, Lahiri, 2024, LLM-based Test-driven Interactive Code Generation: User Study and Empirical Evaluation, IEEE TSE 50(9)(arXiv 2404.10100v2;PDF取自作者 Naik 的 GitHub Pages 仓库) · 2024-10 · 【研究】 · T4 · 对照实验 · verbatim-checked
- 备注:认知负荷为自报量表;任务为短小函数级题目;受试者不能编辑提示和代码(作者自承不反映真实交互)。

## P16 (PRO)
- 论断:TiCoder 大规模评估用参考实现充当'理想化用户'(作者称为上界):GPT-4-32k 在 MBPP 上 pass@1 67.13%→81.56%(1 次交互,PassFail)→83.70%(5 次);HumanEval 60.72%→76.10%→79.49%。三个对话模型(GPT-3.5-turbo/GPT-4-turbo/GPT-4-32k)5 次交互后的绝对增幅为 13.3–22 pp,远小于旧补全模型。
- 原文:Therefore, using the oracle as a proxy indicates that our empirical evaluation represents an upper bound on the improvement that TiCoder can have on the benchmarks with real users.
- URL:https://github.com/aadityanaik/aadityanaik.github.io/blob/master/assets/papers/tse24_ticoder.pdf
- 来源:Fakhoury, Naik, Sakkas, Chakraborty, Lahiri, 2024, LLM-based Test-driven Interactive Code Generation: User Study and Empirical Evaluation, IEEE TSE 50(9)(arXiv 2404.10100v2;PDF取自作者 Naik 的 GitHub Pages 仓库) · 2024-10 · 【研究】 · T4 · 基准 · verbatim-checked
- 备注:每模型每数据集只查询一次生成 100 代码+50 测试的缓存(单次采样,temperature 0.8)。HumanEval 去掉了 docstring 内样例。对话模型增幅为本线由 Table IV 计算。

## P17 (PRO)
- 论断:口径疑点:TiCoder 摘要的'平均绝对提升'在不同版本为 38.43%(v1/作者 README)与 45.97%(v2 摘要),正文写 45.73%;本线按 Table IV 重算(Output、m=5、7 模型×2 数据集)平均绝对提升为 33.50 pp,只计四个旧模型为 43.94 pp——标题数字无法从同文表格复现。
- 原文:We observe an average absolute improvement of 45.97% in the pass@1 code generation accuracy for both datasets and across all LLMs within 5 user interactions
- URL:https://github.com/aadityanaik/aadityanaik.github.io/blob/master/assets/papers/tse24_ticoder.pdf
- 来源:Fakhoury, Naik, Sakkas, Chakraborty, Lahiri, 2024, LLM-based Test-driven Interactive Code Generation: User Study and Empirical Evaluation, IEEE TSE 50(9)(arXiv 2404.10100v2;PDF取自作者 Naik 的 GitHub Pages 仓库);v1 数字见 https://github.com/Smfakhoury/TiCoder-project · 2024-10 · 【研究】 · T4 · 基准 · verbatim-checked
- 备注:正文原句:'T I C ODER -O UTPUT achieves an average absolute improve-ment of 45.73%'。重算脚本可复跑(14 组 baseline pass@1 与 pass@1@5)。承重前必须走方法学审计席。

## P18 (PRO)
- 论断:TiCoder 附带的 T4 证据:把数据集的验证测试直接放进提示,GPT-4-32k 在 MBPP 上 pass@1 67.13%→78.26%(1 个测试)→80.88%(全部测试);HumanEval 60.72%→65.25%→70.39%。即'先给可执行规约'对同一模型有 5–14 pp 的增益。
- 原文:For example, on MBPP GPT-4-32k achieves a pass@1 of 67.13% with the baseline prompt (no tests) and 78.26% when including a single test in the prompt. This increases to a pass@1 of 80.88% when all tests are added in the prompt.
- URL:https://github.com/aadityanaik/aadityanaik.github.io/blob/master/assets/papers/tse24_ticoder.pdf
- 来源:Fakhoury, Naik, Sakkas, Chakraborty, Lahiri, 2024, LLM-based Test-driven Interactive Code Generation: User Study and Empirical Evaluation, IEEE TSE 50(9)(arXiv 2404.10100v2;PDF取自作者 Naik 的 GitHub Pages 仓库) · 2024-10 · 【研究】 · T4 · 基准 · verbatim-checked
- 备注:放入的是评测用的 ground-truth 测试,模型'被要求通过这些测试',评测又用同一批隐藏测试——设计上存在泄漏,数值是上界。单模型。 引文位于双栏 PDF 的单栏内,经 -layout 模式逐行核对。

## P19 (PRO)
- 论断:Lahiri(Microsoft Research,TiCoder 作者之一)2026 年博客把 TiCoder 用户研究概括为'15 名专业开发者'、正确判断约为两倍;而论文本身写明参与者包括博士生——二次概述存在样本口径漂移。
- 原文:A small-scale controlled study with 15 professional developers on code-generation benchmarks [[19]](#ref19) found: developers correctly evaluated AI-generated code roughly twice as often with TiCoder as without it (*p* < 0.001), cognitive load dropped significantly (*p* = 0.007)
- URL:https://github.com/risemsr/risemsr.github.io/blob/main/src/content/docs/blog/2026-03-05-shuvendu-intent-formalization.md
- 来源:Lahiri, 2026-03, Intent Formalization: A Grand Challenge for Reliable Coding in the Age of AI Agents, Microsoft Research RiSE 博客(对应 arXiv 2603.17150) · 2026-03 · 【研究】 · T4 · 评论 · verbatim-checked
- 备注:论文报告 p=0.001(博客写 p<0.001);0.40→0.84 约 2.1 倍,'两倍'成立。作者本人转述也发生口径漂移,引用应回论文。

## P20 (PRO)
- 论断:Lahiri 明确把 GitHub Spec Kit 式 SDD 与'意图形式化'区分:前者的 spec 是自然语言、不可机检,只改善可追溯性——正方阵营内部认为 T1/T2 spec 的保障力弱于 T3/T4。
- 原文:Tools like GitHub Spec Kit [[9]](#ref9) structure AI coding around natural language requirements, improving traceability.
> But these specifications remain informal and uncheckable.
- URL:https://github.com/risemsr/risemsr.github.io/blob/main/src/content/docs/blog/2026-03-05-shuvendu-intent-formalization.md
- 来源:Lahiri, 2026-03, Intent Formalization: A Grand Challenge for Reliable Coding in the Age of AI Agents, Microsoft Research RiSE 博客(对应 arXiv 2603.17150) · 2026-03 · 【研究】 · mixed · 评论 · verbatim-checked
- 备注:立场文章,非实验。作者所在机构(Microsoft)同时是 GitHub/Spec Kit 母公司,但此处观点对 Spec Kit 不利,利益方向较复杂。

## P21 (PRO)
- 论断:Lahiri 博客转述 Endres et al.(FSE 2024):LLM 由自然语言生成的后置条件在 Defects4J 上捕获约八分之一的真实缺陷,包括 Daikon 漏掉的。作者也承认现有证据'主要在基准题上'。
- 原文:On the Defects4J benchmark [[11]](#ref11) (hundreds of real bugs across large Java projects), LLM-generated postconditions caught one in eight real bugs, including bugs missed by the classic Daikon invariant detector [[12]](#ref12).
- URL:https://github.com/risemsr/risemsr.github.io/blob/main/src/content/docs/blog/2026-03-05-shuvendu-intent-formalization.md
- 来源:Lahiri, 2026-03, Intent Formalization: A Grand Challenge for Reliable Coding in the Age of AI Agents, Microsoft Research RiSE 博客(对应 arXiv 2603.17150);原始研究为 Endres, Fakhoury, Chakraborty, Lahiri, FSE 2024(未读原文) · 2026-03 · 【研究】 · T3 · 评论 · paraphrase-checked
- 备注:博客原文逐字核对,但'1/8'的分子分母未回 FSE 原文核对(交给 FORMAL 线)。同组作者自引。

## P22 (PRO)
- 论断:CodePlan(Microsoft,FSE 2024)公开复现包只含 5 个仓库编辑任务(t1–t3、ext1、ext2);按其 metrics.json 汇总,CodePlan 匹配 125/135 个真值编辑块、0 个多余块,而 Repair 基线(按构建/类型检查报错迭代修复)匹配 60 块、漏 75 块、多余 32 块。
- 原文:Data for each repository edit is presented in different directory with the names used in the paper.
- URL:https://github.com/microsoft/CodePlan
- 来源:Bairi et al., 2024, CodePlan: Repository-level Coding using LLMs and Planning, FSE 2024 复现包(microsoft/CodePlan,data/*/pred/*/metrics.json) · 2024-07 · 【研究】 · T2 · 基准 · paraphrase-checked
- 备注:汇总数字为本线从原始 metrics.json 计算(可复跑)。CodePlan 的'计划'是依赖分析+变更影响分析驱动的算法化编辑序列,不是人写或 LLM 写的 spec 文档——不能直接迁移为'写 plan.md 有效'的证据。样本 n=5(另 2 个专有仓库未公开)。

## P23 (PRO)
- 论断:CodePlan 摘要层结论(二手):在 C# 包迁移与 Python 时序编辑两类任务上,CodePlan 让 5/7(FSE 版)或 5/6(arXiv 版)个仓库通过有效性检查(构建无误+编辑正确),基线一个都没通过;模型 gpt-4-32k。
- 原文:
- URL:https://arxiv.org/abs/2309.12499
- 来源:Bairi, Sonwane, Kanade, Vageesh, Iyer, Parthasarathy, Rajamani, Ashok, Shet, 2023/2024, CodePlan, arXiv 2309.12499 / Proc. ACM Softw. Eng. 1(FSE) · 2024-07 · 【研究】 · T2 · 基准 · secondhand
- 备注:arxiv.org 与 microsoft.com 在本会话不可达,分母差(6 vs 7)只来自搜索摘要,须回一手核对。

## P24 (PRO)
- 论断:PlanSearch(Scale AI):先生成关于题目的自然语言观察与计划、再据计划写代码,在 LiveCodeBench 上用 Claude 3.5 Sonnet 达到 pass@200 77.0%,对比重复采样 pass@200 60.6%、无搜索最佳 pass@1 41.4%。
- 原文:Using PlanSearch on top of Claude 3.5 Sonnet achieves a pass@200 of 77.0% on LiveCodeBench, which outperforms tboth the best pass-rate achieved without any search (pass@1 = 41.4%) and using standard repeated sampling on top of existing non-search models (pass@200 = 60.6%).
- URL:https://github.com/scaleapi/plansearch
- 来源:Wang et al., 2024/2025, Planning In Natural Language Improves LLM Search For Code Generation, ICLR 2025(官方仓库 README) · 2024-09 · 【研究】 · T2 · 基准 · verbatim-checked
- 备注:作者来自 Scale AI(数据/评测厂商)。口径是 pass@200(200 次采样中任一通过,需要外部判定器挑选),不是单次生成质量;机制是'计划提高多样性',与'一份 spec 提高单次产出'不同。不可与 pass@1 混引。

## P25 (PRO)
- 论断:Ambig-SWE(CMU,ICLR 2026,二手):在把 SWE-bench Verified 题面改为欠规约版本后,允许 agent 向持有完整题面的模拟用户(GPT-4o)提问,可使解决率比不交互基线最高提升 74%;模型在未被明确提示时基本不主动提问。
- 原文:
- URL:https://arxiv.org/abs/2502.13069
- 来源:Vijayvargiya, Zhou, Yerukola, Sap, Neubig, 2025/2026, Ambig-SWE: Interactive Agents to Overcome Underspecificity in Software Engineering, ICLR 2026 · 2026-02 · 【研究】 · T1 · 基准 · secondhand
- 备注:代码数据仓库 sani903/InteractiveSWEAgents 已核:含 500 行 SWE-bench Verified 实例摘要表(full_summaries_verified.xlsx),基于 OpenHands;但聚合解决率未在仓库中找到,论文正文不可达。'最高 74%' 是相对、最大值。模拟用户持有完整题面=理想化。

## P26 (PRO)
- 论断:Spec Kit Agents(2026-04,二手):在 GitHub Spec Kit 的 Specify/Plan/Tasks/Implement 流程上加入仓库探测与验证钩子,128 个任务实例(5 个开源仓库 32 个功能任务)上 LLM 评审综合分仅 +0.15(1–5 分制),测试通过率 99.7–100%;SWE-bench Lite 56.5%→58.2%。作者承认额外阶段带来开销。
- 原文:
- URL:https://arxiv.org/abs/2604.05278
- 来源:Taghavi, Bhavani, 2026, Spec Kit Agents: Context-Grounded Agentic Workflows, arXiv 2604.05278 · 2026-04 · 【研究】 · T2 · 基准 · secondhand
- 备注:对比的是'有钩子 vs 无钩子的 Spec Kit',不是'SDD vs 无 spec';质量为 LLM-as-judge;未见重复运行信息。增益很小,PRO 线中属弱证据。

## P27 (PRO)
- 论断:Google 'Spec-Driven Test Generation'(SpecOps '26,二手):让测试生成 agent 先写出前置/后置条件与未定义行为,再写测试;在 Google 生产缺陷上,缺陷检出率比传统测试生成 agent 高约 9.8 pp(p=0.0352),分支覆盖高约 2.5 pp(p=0.0034)。
- 原文:
- URL:https://arxiv.org/abs/2608.17177
- 来源:Google, 2026, Grounding AI Agents in Contracts: An Empirical Evaluation of Spec-Driven Test Generation, SpecOps '26 / arXiv 2608.17177 · 2026-08 · 【研究】 · T3 · 对照实验 · secondhand
- 备注:任务是测试生成而非代码生成;Google 内部数据不可复跑;样本量未知。需回一手核对分母和缺陷集。

## P28 (PRO)
- 论断:Mathews & Nagappan(ASE 2024,二手):在 MBPP、HumanEval、CodeChef 上,把测试与题面一起提供给 GPT-4/Llama 3 一致地解出更多题目(TGen 框架)。具体增幅本线未取得。
- 原文:
- URL:https://arxiv.org/abs/2402.13521
- 来源:Mathews, Nagappan, 2024, Test-Driven Development for Code Generation / Test-Driven Development and LLM-based Code Generation, ASE 2024 · 2024-10 · 【研究】 · T4 · 基准 · secondhand
- 备注:与 P18 同方向(测试入提示)。TGen 含迭代修复回路,收益不全来自'先给测试'。

## P29 (PRO)
- 论断:HumanEvalComm 基准把 HumanEval 164 题改写为 762 个含糊/不一致/不完整题面,用于测模型是否会提澄清问题;二手摘要称多数 Code LLM 的'沟通率'很低,Okanagan(ChatGPT 3.5 代理)把沟通率绝对提升约 58%(另一来源称 59%)。
- 原文:HumanEvalComm contains 762 modified problem descriptions based on the 164 problems in the HumanEval dataset.
- URL:https://github.com/jie-jw-wu/human-eval-comm
- 来源:Wu, Fard, 2024/2025, HumanEvalComm: Benchmarking the Communication Competence of Code Generation for LLMs and LLM Agent(官方仓库 README;arXiv 2406.00215) · 2024-06 · 【研究】 · T1 · 基准 · paraphrase-checked
- 备注:762 题为 README 逐字核对;沟通率等效果数字为二手,各摘要互相矛盾。后续工作指出部分改写不足以触发提问,已出 V2。

## P30 (PRO)
- 论断:SWE-RPG(2026-08,二手):一个把需求澄清、计划、代码生成分阶段评测的 issue 基准(仓库版 163 实例:85 Java + 78 Python);二手摘要称 agent 平均解决率 31.5%,46.7% 的运行主要失败在需求澄清或实现计划阶段——支持'上游规约/计划是瓶颈'的机制叙事,但无'有/无计划'对照。
- 原文:It contains one benchmark dataset with 163 instances: 85 Java and 78 Python.
- URL:https://github.com/Xin-Zhou-smu/SWE-RPG-Bench
- 来源:Zhou et al., 2026, SWE-RPG: A Unified Issue Resolution Benchmark for Requirement Clarification, Planning, and Code Generation for Coding Agents, arXiv 2608.09072 · 2026-08 · 【研究】 · mixed · 基准 · paraphrase-checked
- 备注:实例数逐字核对(README),31.5%/46.7% 为二手。失败归因由基准作者定义,属描述性,非干预证据。

## P31 (PRO)
- 论断:'Ask or Assume?'(2026,二手):不确定性感知的多代理澄清脚手架在欠规约编码任务上达到 69.40% 解决率,单代理基线 61.20%,并称接近获得完整规约的 agent。
- 原文:
- URL:https://arxiv.org/abs/2603.26233
- 来源:Ask or Assume? Uncertainty-Aware Clarification-Seeking in Coding Agents, arXiv 2603.26233, 2026 · 2026-03 · 【研究】 · T1 · 基准 · secondhand
- 备注:作者、基准、样本、运行次数均未核实。只作线索。


### 搜索角度
- arxiv.org / export.arxiv.org / ar5iv / alphaxiv / huggingface / openreview / aclanthology / dl.acm.org / ieeexplore / semanticscholar / openalex / microsoft.com / github.blog / docs.github.com / swebench.com:本会话代理全部 403 或 DNS 不可达——一手全文只能经 github.com / raw.githubusercontent.com 获取
- 作者 GitHub Pages 仓库中的论文 PDF:ligechina.github.io(Self-planning、Self-collaboration、SCoT 均命中)、linshi-website.github.io(ClarifyGPT 命中)、aadityanaik.github.io(TiCoder TSE 命中)、Smfakhoury/TiCoder-project(TiCoder v1 命中)、risemsr.github.io(Lahiri 2026 博客命中)
- 官方复现包:microsoft/CodePlan(metrics.json 命中并重算)、microsoft/TiCoder(仅工具 README)、ClarifyGPT/ClarifyGPT(README)、scaleapi/plansearch(README)、Md-Ashraful-Pramanik/MapCoder(README 结果表)、jie-jw-wu/human-eval-comm、jie-jw-wu/clarify-coder、sani903/InteractiveSWEAgents、Xin-Zhou-smu/SWE-RPG-Bench
- CodePlan 论文正文(FSE/arXiv)— 未取得,5/6 vs 5/7 分母未回一手
- Ambig-SWE 论文正文与聚合解决率表 — 未取得(仓库无聚合结果)
- Lahiri et al. 2022 TiCoder 原始 arXiv 2208.05950 — 未取得(用 TSE 版与作者 v1 PDF 代替)
- Mathews & Nagappan TDD for code generation 具体数字 — 未取得
- ClarifyCoder(arXiv 2504.16331)效果数字 — 仓库 README 无数字,未取得
- MetaGPT(PRD/设计文档 SOP)消融 — 未检索到可达一手,未纳入
- SWE-bench 风格 agent 中'有/无计划步骤'的单因素消融 — 搜索仅得 HyperAgent(SWE-bench Tiny 100 题角色消融)、PMCoder(2608.06811,计划+记忆耦合),均未读到原文;未找到前沿 agent(Claude Code / Codex / Cursor plan mode)的公开受控消融
- 厂商 plan mode 效果自测(Anthropic/Cursor/Kiro)— 属 VENDOR 线,未纳入
- Spec Kit Agents(2604.05278)、Google Spec-Driven Test Generation(2608.17177)、Ask or Assume(2603.26233)— 仅搜索摘要
- 2026 年'SDD vs 无 spec'的受控实验(人类开发者 RCT)— 未找到;搜索摘要称 2609.00252 自述证据基础不成熟

### 交叉口径问题
- 计划/规约的'作者'不同不得混引:Self-planning/SCoT/PlanSearch 是模型自生成计划(T2-auto);CodePlan 是静态分析驱动的算法化计划;ClarifyGPT/TiCoder/Ambig-SWE 是人(或模拟人)补充意图;SDD 叙事指人+agent 共写的持久 spec 文档——前三类的效应量不能直接当 SDD 证据
- 理想化上界:TiCoder 大规模评估用参考实现当用户、ClarifyGPT 模拟用户持有 ground-truth 测试、Ambig-SWE 模拟用户持有完整题面、Self-planning 的 Ground-truth Planning 由参考代码反推——均含答案信息,数字是上界
- ClarifyGPT 人类实验参与者看到带期望 I/O 的单元测试:T1 澄清效应混入 T4
- TiCoder 标题数字版本漂移:38.43%(v1)→45.97%(v2 摘要)→45.73%(正文);按 Table IV 重算 33.50 pp——须方法学审计席复核计算口径
- TiCoder 参与者构成:论文'8 名 Microsoft 工程师/研究员 + 10 名博士生'(含 3 名试点,总 18);Lahiri 2026 博客写'15 名专业开发者'
- MapCoder README 'ChatGPT' 行与 Self-planning 论文 code-davinci-002 行数字逐位相同,疑似挪用
- Self-planning 在 GPT-4 上的第三方结果(MapCoder 表)多数基准为负,与原论文 code-davinci-002 正向结果方向相反;模型代际不可迁移
- 相对提升 vs 绝对提升 vs 'up to' 最大值:Self-planning 25.4%、SCoT 13.79%、ClarifyGPT 15.35%、Ambig-SWE 74% 均为相对值或最大值
- pass@1 vs pass@200(PlanSearch)vs 解决率(SWE-bench)vs 正确判断率(TiCoder 用户研究)vs LLM-judge 分(Spec Kit Agents)不得互换
- 单次采样:Self-planning 贪心单次、TiCoder 每模型一次缓存、MapCoder/Self-collab 未报告方差;ClarifyGPT 3 次平均——按 #14 AGENTbench 教训视为假精度风险
- 基准全部是函数级/竞赛题(HumanEval、MBPP、LiveCodeBench)或 issue 修复;无一来源测量 spec 长期维护、漂移或返工——主张 2/3 在 PRO 线无证据
- 模型代际:多数一手实验用 code-davinci-002 / GPT-3.5 / GPT-4(2023–2024),对 2025–2026 前沿 agent 的可迁移性未测;TiCoder 数据显示越强的模型增益越小
- CodePlan 有效性分母 5/6(arXiv)vs 5/7(FSE),公开数据只有 5 个仓库

# 线 CON

## C01 (CON)
- 论断:Hill(ESEM 2026)以 119 个开源仓库、88,052 个已合并非 bot PR(原始 100,247,剔除 12,195 bot PR;采集 2026-03-28~04-03,365 天回看,约 2025-04~2026-04)检验 5 条由 SDD 厂商宣传语推出的假设,5 条均不成立。
- 原文:We test five hypotheses derived from SDD vendor claims against 88,052 pull requests across 119 open-source repositories.
- URL:https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.ESEM.2026.84
- 来源:Brenn Hill, 2026, Specification Artifacts in Open-Source Pull Request Workflows Do Not Reduce Defects: An Empirical Test of Spec-Driven Development Claims, ESEM 2026 (LIPIcs vol.394, SEIP track); 全文读自作者公开仓库 github.com/brennhill/delivery-gap-research esem-latex/main.tex(commit a23d38a, 2026-07-27) · 2026-10 · 【研究】 · T1 · 观察 · verbatim-checked
- 备注:Dagstuhl PDF 主机被本会话网络策略拦截,全文取自作者 GitHub 仓库的 camera-ready LaTeX 源(2026-07-27);摘要数字与第三方读已发表 PDF 的转述(mattbutlerengineering/ai-tooling PR#731)一致。tex 内 ArticleNo=83、出版 URL 为 .84,系编辑编号差。 单作者、独立研究者(tex 署名 'Independent Researcher, Germany');无资助/利益冲突声明。作者另有书《The Delivery Gap》与 'cost per accepted change' 指标项目(GitHub 公开仓库),属非财务立场利益。

## C02 (CON)
- 论断:Hill 的「spec'd」处理变量实际几乎全是 issue/ticket 引用:24,298/88,052(27.6%)PR 被判为 spec'd,其中 97.5% 由 issue 号/issue URL/ticket ID 触发,PR 正文内结构化需求段仅 24 个(0.1%)。作者自述测的是「issue 与 ticket 引用存在性」,不是 SDD 工具产出。
- 原文:97.5\% of spec'd PRs are identified by a reference to a tracking issue or ticket, while structured requirements text written directly into the PR body accounts for 24 PRs. Whatever else this measure captures, in practice it measures \emph{issue- and ticket-reference presence}.
- URL:https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.ESEM.2026.84
- 来源:Brenn Hill, 2026, Specification Artifacts in Open-Source Pull Request Workflows Do Not Reduce Defects: An Empirical Test of Spec-Driven Development Claims, ESEM 2026 (LIPIcs vol.394, SEIP track); 全文读自作者公开仓库 github.com/brennhill/delivery-gap-research esem-latex/main.tex(commit a23d38a, 2026-07-27) · 2026-10 · 【研究】 · T1 · 观察 · verbatim-checked
- 备注:本线用作者公开 master-prs.csv 复跑:非 bot 88,052、spec'd 24,298(27.6%)、#N 11,348、GitHub issue URL 7,252、外部文档 URL 561、模板段 24,与论文表 2 逐项吻合(现场核验)。这是本研究最大的构念效度缺口:它检验的是 T1 级「有工单」而非 Spec Kit/Kiro 工作流。

## C03 (CON)
- 论断:样本中没有任何仓库提交 SDD 工具产出:全部 100,247 个 PR 的标题/描述/改动路径中 .specify/、.speckit/、.kiro/、spec-kit 零命中;119 仓库默认分支文件树审计(2026-04 人工、2026-07 程序化)也为零。因此「采用 SDD 工具是否降缺陷」在该样本中不可检验。
- 原文:SDD tool adoption itself remains untested: no repository in the sample commits such output.
- URL:https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.ESEM.2026.84
- 来源:Brenn Hill, 2026, Specification Artifacts in Open-Source Pull Request Workflows Do Not Reduce Defects: An Empirical Test of Spec-Driven Development Claims, ESEM 2026 (LIPIcs vol.394, SEIP track); 全文读自作者公开仓库 github.com/brennhill/delivery-gap-research esem-latex/main.tex(commit a23d38a, 2026-07-27) · 2026-10 · 【研究】 · mixed · 观察 · verbatim-checked
- 备注:引用本论文时最容易被误读的点:不能写成「SDD 不降缺陷」,只能写成「开源 PR 中的规格工件(主要是工单引用)与缺陷无关」。

## C04 (CON)
- 论断:H1(规格→缺陷)主估计为倾向得分匹配:17,375 对匹配 PR,spec'd 缺陷引入率 14.7% vs 未 spec'd 15.2%,差 −0.6pp,p=0.133(16 个协变量平衡),无差异。缺陷由基本 SZZ 回溯,仅覆盖 103/119 仓库。
- 原文:Across 17,375 matched pairs, spec'd PRs introduce defects at 14.7\% against 15.2\% for their unspec'd matches, a difference of $-0.6$pp ($p = 0.133$): matching eliminates the raw association entirely.
- URL:https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.ESEM.2026.84
- 来源:Brenn Hill, 2026, Specification Artifacts in Open-Source Pull Request Workflows Do Not Reduce Defects: An Empirical Test of Spec-Driven Development Claims, ESEM 2026 (LIPIcs vol.394, SEIP track); 全文读自作者公开仓库 github.com/brennhill/delivery-gap-research esem-latex/main.tex(commit a23d38a, 2026-07-27) · 2026-10 · 【研究】 · T1 · 观察 · verbatim-checked
- 备注:未报告匹配估计的置信区间;p 值为名义值(作者自承样本量非预设、可选停止)。SZZ 基本版误归因率 46–71%(da Costa 2017),作者以匹配+非 SZZ 的返工指标作主证据。

## C05 (CON)
- 论断:原始(未调整)关联方向与 SDD 宣称相反:spec'd PR 引入缺陷的 OR=1.20(p<0.001)、被返工 OR=1.18;作者内固定效应+规模控制下缺陷 +1.4pp [+0.5,+2.4](p=0.003);加入 JIT 风险特征后降 55% 且不显著(p=0.229)。作者解释为适应证混杂:开发者给最难的活写 spec。
- 原文:This is \emph{confounding by indication} -- developers write specs for their hardest work, and harder work produces more defects.
- URL:https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.ESEM.2026.84
- 来源:Brenn Hill, 2026, Specification Artifacts in Open-Source Pull Request Workflows Do Not Reduce Defects: An Empirical Test of Spec-Driven Development Claims, ESEM 2026 (LIPIcs vol.394, SEIP track); 全文读自作者公开仓库 github.com/brennhill/delivery-gap-research esem-latex/main.tex(commit a23d38a, 2026-07-27) · 2026-10 · 【研究】 · T1 · 观察 · verbatim-checked
- 备注:spec'd PR 新增行数 1.8×、触及文件年龄 2.3×、作者先前提交中位数 64 vs 116。注意 SSRN 预印本(2026-04)把「spec'd PR 引入更多缺陷」作为摘要头条,ESEM 终稿按审稿条件改为「匹配后无差异」——同一数据、头条方向措辞改变。

## C06 (CON)
- 论断:H2(规格→返工)无保护效应:作者内 +1.2pp [+0.5,+1.9](p=0.001,方向为更多返工,约每 83 个 PR 多 1 次返工);匹配后 +0.5pp(p=0.146,19,648 对)。返工定义:30 天内任何人提交触及重叠文件、且标题/描述含 fix/revert/hotfix/regression 等词的后续 PR(排除被 >30% PR 触及的高频文件);13.4% PR 被判返工。
- 原文:The within-author estimate is in the wrong direction -- the same author's spec'd PRs have a 1.2 percentage-point higher rework rate than their unspec'd PRs ($p = 0.001$), about one extra rework event per 83 PRs -- and matching on task complexity removes the difference rather than reversing it ($+0.5$pp, $p = 0.146$).
- URL:https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.ESEM.2026.84
- 来源:Brenn Hill, 2026, Specification Artifacts in Open-Source Pull Request Workflows Do Not Reduce Defects: An Empirical Test of Spec-Driven Development Claims, ESEM 2026 (LIPIcs vol.394, SEIP track); 全文读自作者公开仓库 github.com/brennhill/delivery-gap-research esem-latex/main.tex(commit a23d38a, 2026-07-27) · 2026-10 · 【研究】 · T1 · 观察 · verbatim-checked
- 备注:返工指标为关键词+文件重叠启发式,未报告人工校验精度/召回;作者称不依赖 SZZ 故作主证据。

## C07 (CON)
- 论断:H3/H4(规格质量→缺陷/返工)不成立:质量分由 Claude Haiku 按 7 维量表打分(0–100),25,209 PR 被评分;作者内估计缺陷系数 −0.0003(95% CI [−0.0007,+0.0001],p=0.164,即 +10 分质量对应约 −0.3pp),返工 p=0.860。作者自定 H3/H4 为探索性。
- 原文:Specification quality predicts neither defects ($p = 0.164$) nor rework ($p = 0.860$)
- URL:https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.ESEM.2026.84
- 来源:Brenn Hill, 2026, Specification Artifacts in Open-Source Pull Request Workflows Do Not Reduce Defects: An Empirical Test of Spec-Driven Development Claims, ESEM 2026 (LIPIcs vol.394, SEIP track); 全文读自作者公开仓库 github.com/brennhill/delivery-gap-research esem-latex/main.tex(commit a23d38a, 2026-07-27) · 2026-10 · 【研究】 · T1 · 观察 · verbatim-checked
- 备注:LLM 评分与人工评分一致性仅中等:38 个 PR 分层样本,Spearman ρ=0.42;验收标准维度 ρ=0.17、数据契约 0.19、错误状态 0.22。量表衡量「形式完整性」而非「功能正确性」。38 例人工校验样本很小。

## C08 (CON)
- 论断:H5(规格约束 AI 改动范围)不成立:用 5,989 个 AI 标记 PR(占 6.8%),spec×AI 交互项 +0.000(95% CI [−0.101,+0.102],p=0.997,来自 366 名有处理变异的作者);有 spec 的 PR 改动更大(AI +12.0%、人 +14.0%)。
- 原文:The spec $\times$ AI interaction is $+0.000$ (95\% CI $[-0.101, +0.102]$, $p = 0.997$, identified from 366 authors).
- URL:https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.ESEM.2026.84
- 来源:Brenn Hill, 2026, Specification Artifacts in Open-Source Pull Request Workflows Do Not Reduce Defects: An Empirical Test of Spec-Driven Development Claims, ESEM 2026 (LIPIcs vol.394, SEIP track); 全文读自作者公开仓库 github.com/brennhill/delivery-gap-research esem-latex/main.tex(commit a23d38a, 2026-07-27) · 2026-10 · 【研究】 · T1 · 观察 · verbatim-checked
- 备注:AI 标记分类器精度 98.8%、召回仅 24.2%(537 个自报披露 PR 校验),约 3/4 AI 辅助工作不可见;CI 宽度 ±0.1 log-churn(约 ±10%),不算「紧」。

## C09 (CON)
- 论断:唯一方向符合 SDD 宣称的子组:在「未检测到 AI 使用」的仓库(3,562 PR)中,spec 与返工减少 −3.3pp 相关(名义 p=0.014),但为 6 个子组检验之一,未过 Bonferroni 阈值 α=0.0083。
- 原文:One subgroup runs the other way -- in repositories with no detected AI use, specifications are associated with less rework ($-3.3$pp, $p = 0.014$) -- but it is one of six subgroup tests and does not survive correction for multiple comparisons.
- URL:https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.ESEM.2026.84
- 来源:Brenn Hill, 2026, Specification Artifacts in Open-Source Pull Request Workflows Do Not Reduce Defects: An Empirical Test of Spec-Driven Development Claims, ESEM 2026 (LIPIcs vol.394, SEIP track); 全文读自作者公开仓库 github.com/brennhill/delivery-gap-research esem-latex/main.tex(commit a23d38a, 2026-07-27) · 2026-10 · 【研究】 · T1 · 观察 · verbatim-checked
- 备注:正反双方都可能挑这一条:反方会忽略,正方会放大。成文须带「未过多重比较校正」。

## C10 (CON)
- 论断:Hill 自承抽样为目的性分层、刻意富集强规格实践仓库,且样本量未预设:仓库在「未见效应」时持续追加,至 119 个、零结果稳定后停止;所有分析为事后分析,未预注册。
- 原文:Repositories were added while no effect was evident, and collection stopped at 119 once the null appeared stable across the checks in \cref{sec:robustness}.
- URL:https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.ESEM.2026.84
- 来源:Brenn Hill, 2026, Specification Artifacts in Open-Source Pull Request Workflows Do Not Reduce Defects: An Empirical Test of Spec-Driven Development Claims, ESEM 2026 (LIPIcs vol.394, SEIP track); 全文读自作者公开仓库 github.com/brennhill/delivery-gap-research esem-latex/main.tex(commit a23d38a, 2026-07-27) · 2026-10 · 【研究】 · n/a · 观察 · verbatim-checked
- 备注:作者论证可选停止主要膨胀假阳性而非假阴性;但「看到零结果稳定才停」同样意味着数据驱动停止,对零结论也非完全中性(方法学审计席应审)。两波仓库:43(按 issue 链接率分层 8/12/6/3 + 14 个 AI 层)+77(33 强流程/24 弱/20 重度 AI)−1 无数据=119。

## C11 (CON)
- 论断:外部效度:119 个仓库全部为开源,而 SDD 工具主要面向商业团队;多数 PR 早于普遍的 agentic 编码;作者明言结果不应外推到商业开发,也不能排除「spec 作为 agent 输入、端到端由 agent 实现」的工作流表现不同。
- 原文:Our results speak to open-source pull request workflows and should not be extrapolated to commercial development.
- URL:https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.ESEM.2026.84
- 来源:Brenn Hill, 2026, Specification Artifacts in Open-Source Pull Request Workflows Do Not Reduce Defects: An Empirical Test of Spec-Driven Development Claims, ESEM 2026 (LIPIcs vol.394, SEIP track); 全文读自作者公开仓库 github.com/brennhill/delivery-gap-research esem-latex/main.tex(commit a23d38a, 2026-07-27) · 2026-10 · 【研究】 · n/a · 观察 · verbatim-checked
- 备注:

## C12 (CON)
- 论断:同行评审轨迹:据作者仓库的修订计划,ESEM 结果为有条件接收;一位审稿人(#26A)建议拒稿,被元审稿(#26D)推翻;五项接收条件包括「围绕实际测量物重新定框」「降低对 SZZ 的依赖」「弱化零 AI 子组」「补充抽样框」。头条从「spec'd PR 引入更多缺陷 +1.4pp」改为 PSM 主估计的完全零结果。
- 原文:**Status:** conditional accept. #26A recommended reject; the meta-review (#26D) overrode it.
- URL:https://github.com/brennhill/delivery-gap-research/blob/main/esem-latex/REVISION-PLAN.md
- 来源:Brenn Hill, 2026, ESEM Revision Plan — Conditional Accept (Review #26D), 作者 GitHub 仓库 · 2026-07 · 【研究】 · n/a · 文档 · verbatim-checked
- 备注:作者自存文件,非会议官方审稿记录;发表于 SEIP(Software Engineering in Practice)轨道而非研究轨道。

## C13 (CON)
- 论断:SSRN 工作论文版(2026-04)与 ESEM 终稿同数据但头条不同:预印本摘要写「spec'd PR 引入更多而非更少缺陷」,终稿改为匹配后「无法区分」。
- 原文:Spec’d PRs introduce more defects, not fewer — developers spec their hardest work, and hard work produces defects (confounding by indication).
- URL:https://papers.ssrn.com/sol3/papers.cfm?abstract_id=6515898
- 来源:Brenn Hill, 2026-04, Does Spec-Driven Development Reduce Defects? An Empirical Test of Industry Claims Across 119 Open-Source Repositories, SSRN Working Paper(PDF 取自作者仓库 ssrn-sdd-null-result.pdf) · 2026-04 · 【研究】 · T1 · 观察 · verbatim-checked
- 备注:二手搜索摘要称预印本用 100,247 PR——不准确:预印本摘要同为 88,052(100,247 是剔 bot 前)。引用时只用 ESEM 终稿口径。

## C14 (CON)
- 论断:作者公开勘误:2026-07-27 发现 issue 链接组 vs 仅描述组对比因 pandas `== True` 误用漏掉 2,891/25,209(11.5%)个 PR(恰是 issue 引用最多的 PR);修正后 issue 链接组 N 由 10,190→13,081,中位质量 49→50。作者称未影响任何假设检验。
- 原文:That is 2,891 of 25,209 scored PRs (11.5%) — and not a random 11.5%.
- URL:https://github.com/brennhill/delivery-gap-research/blob/main/CORRECTIONS.md
- 来源:Brenn Hill, 2026-07-27, CORRECTIONS.md, delivery-gap-research 仓库 · 2026-07 · 【研究】 · n/a · 文档 · verbatim-checked
- 备注:正面信号(透明勘误、复现包 CC-BY 4.0,Zenodo 10.5281/zenodo.19415187);同时说明分析管线存在过实质性编码错误,验证阶段应抽查其他脚本。

## C15 (CON)
- 论断:本线现场核验发现处理变量的误判:在作者公开的 master-prs.csv 中,被归入「项目 ticket ID(PROJ-123)」的 5,112 个非 bot spec'd PR 里,至少 1,161 个(占该类 22.7%、占全部 spec'd 4.8%)匹配的是普通连字符词而非工单号,如 ID-BASED(16)、LLM-GENERATED(15)、CPU-ONLY(15)、UUID-BASED(14)、ESM-ONLY(11);带数字的部分也混有 GLM-/LLM-/PEP- 等前缀。
- 原文:
- URL:https://github.com/brennhill/delivery-gap-research/blob/main/study/data/master-prs.csv
- 来源:本线复跑:Hill 复现数据 master-prs.csv(commit a23d38a),spec_source 字段分类统计 · 2026-11 · 【研究】 · T1 · 观察 · paraphrase-checked
- 备注:现场核验(本线自行计算,非作者陈述)。论文称已过滤 RFC-/CVE-/GPT- 等误报,但过滤不完整。此类误判多为非差异性噪声,倾向把效应拉向零——与「零结果」方向一致,是审计席应计入的偏倚来源;规模约 5%,单独不足以翻转结论。

## C16 (CON)
- 论断:Grafana 仓库 .gitignore 明文排除 Spec Kit 文件,Airflow 与 Spark 排除 .kiro/——印证 Hill 所说「这些工具的产出被刻意留在版本库外,任何基于工件的测量都看不见」。
- 原文:# Spec-kit files shouldn't be committed without a major design process
- URL:https://github.com/grafana/grafana/blob/main/.gitignore
- 来源:grafana/grafana .gitignore(HEAD 2026-11-10);apache/airflow、apache/spark .gitignore · 2026-11 · 【官方】 · mixed · 文档 · verbatim-checked
- 备注:现场核验:三仓库 HEAD 均仍含该规则(Grafana 第 287–288 行 '.specs';Airflow '# Kiro' '.kiro/';Spark '.kiro/')。含义:仓库普查(ADOPT 线)会系统性低估 SDD 工具使用。

## C17 (CON)
- 论断:Hill 对 SDD 学术文献的引用链审查:Piskala(2026)称「对照研究显示错误最多减少 50%」,所引 Red Hat 博客与 InfoQ 文章均无任何对照研究或定量数据;Marri(2026)报告的 73% 安全缺陷下降来自单项目、同一开发者先后实现两组条件。
- 原文:Piskala \cite{piskala2026} claims ``controlled studies showing error reductions of up to 50\%,'' citing a Red Hat Developer blog post \cite{naszcyniec2025} and an InfoQ article \cite{griffin2026}; neither contains any controlled study, experiment, or quantitative data
- URL:https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.ESEM.2026.84
- 来源:Brenn Hill, 2026, Specification Artifacts in Open-Source Pull Request Workflows Do Not Reduce Defects: An Empirical Test of Spec-Driven Development Claims, ESEM 2026 (LIPIcs vol.394, SEIP track); 全文读自作者公开仓库 github.com/brennhill/delivery-gap-research esem-latex/main.tex(commit a23d38a, 2026-07-27) · 2026-10 · 【研究】 · mixed · 评论 · verbatim-checked
- 备注:此为 Hill 的二手判断,本线未能回到 Piskala/Red Hat/InfoQ/Marri 原文核对(arxiv.org 被网络策略拦截)——交 PRO/MEASURE 线或验证阶段核。'50%' 若出现在正方叙事中,应按疑似无源数字处理。

## C18 (CON)
- 论断:Hill 对 Eberhardt 的转述有失真:称 Spec Kit「约慢十倍、产出数千行 markdown 却仍是有 bug 的代码」,而 Eberhardt 原文说 Spec Kit 代码质量「just fine」,只有一个「简单明显」的 bug(变量未从数据存储填充,3 行修复)。
- 原文:Eberhardt found Spec Kit roughly ten times slower than iterative development, producing thousands of lines of specification markdown that still resulted in buggy code \cite{scottlogic2025}.
- URL:https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.ESEM.2026.84
- 来源:Brenn Hill, 2026, Specification Artifacts in Open-Source Pull Request Workflows Do Not Reduce Defects: An Empirical Test of Spec-Driven Development Claims, ESEM 2026 (LIPIcs vol.394, SEIP track); 全文读自作者公开仓库 github.com/brennhill/delivery-gap-research esem-latex/main.tex(commit a23d38a, 2026-07-27) · 2026-10 · 【研究】 · T1 · 评论 · verbatim-checked
- 备注:对照 Scott Logic 原文 'the code quality created when following Spec Kit was just fine, but the simple and obvious bug threw me a little';kartlog 提交 8292058e 为 +3/−2 行。'buggy code' 属夸大,转述保真问题。

## C19 (CON)
- 论断:Böckeler 用 Kiro 修一个小 bug(与她此前测 Codex 用的同一个 bug):需求文档把它变成 4 个「user story」共 16 条验收标准,她称流程「像用大锤砸坚果」。
- 原文:When I asked Kiro to fix a small bug (it was the same one I used in the past to try Codex), it quickly became clear that the workflow was like using a sledgehammer to crack a nut. The requirements document turned this small bug into 4 “user stories” with a total of 16 acceptance criteria
- URL:https://martinfowler.com/articles/exploring-gen-ai/sdd-3-tools.html
- 来源:Birgitta Böckeler (Thoughtworks), 2025-10-15, Understanding Spec-Driven-Development: Kiro, spec-kit, and Tessl, martinfowler.com · 2025-10 · 【媒体】 · T1 · 案例 · verbatim-checked
- 备注:martinfowler.com 被网络策略拦截;正文取自 3 份独立的网页剪藏(GitHub: giwankim/obsidian-vault、salomao-santos/letramento-de-ia、danielcamargo/second-brain),关键句在三份中逐字一致。作者为 Thoughtworks 员工(Thoughtworks 卖咨询,不卖 SDD 工具)。 n=1 次运行、2025-10 的 Kiro 版本(Kiro 2025-11 才 GA,后续版本可能已改 bugfix 流程,交 VENDOR 线);未给墙钟/token 数。 quote 为页面渲染文本(剪藏中括号内为超链接锚文本,已去除 markdown 链接标记)。

## C20 (CON)
- 论断:Böckeler 用 spec-kit 做一个相当于「3–5 点故事」的棕地功能(基于现有看板的汇总弹窗),产出的 markdown 文件多到她觉得对问题规模而言过度;文件彼此重复、也与现有代码重复,冗长乏味。
- 原文:spec-kit created a LOT of markdown files for me to review. They were repetitive, both with each other, and with the code that already existed. Some contained code already. Overall they were just very verbose and tedious to review.
- URL:https://martinfowler.com/articles/exploring-gen-ai/sdd-3-tools.html
- 来源:Birgitta Böckeler (Thoughtworks), 2025-10-15, Understanding Spec-Driven-Development: Kiro, spec-kit, and Tessl, martinfowler.com · 2025-10 · 【媒体】 · T2 · 案例 · verbatim-checked
- 备注:martinfowler.com 被网络策略拦截;正文取自 3 份独立的网页剪藏(GitHub: giwankim/obsidian-vault、salomao-santos/letramento-de-ia、danielcamargo/second-brain),关键句在三份中逐字一致。作者为 Thoughtworks 员工(Thoughtworks 卖咨询,不卖 SDD 工具)。 无文件数/行数/时间的定量记录。

## C21 (CON)
- 论断:Böckeler 结论之一:宁可审代码也不愿审这些 markdown 文件;有效的 SDD 工具需要很好的 spec 审阅体验。
- 原文:To be honest, I’d rather review code than all these markdown files. An effective SDD tool would have to provide a very good spec review experience.
- URL:https://martinfowler.com/articles/exploring-gen-ai/sdd-3-tools.html
- 来源:Birgitta Böckeler (Thoughtworks), 2025-10-15, Understanding Spec-Driven-Development: Kiro, spec-kit, and Tessl, martinfowler.com · 2025-10 · 【媒体】 · T2 · 评论 · verbatim-checked
- 备注:martinfowler.com 被网络策略拦截;正文取自 3 份独立的网页剪藏(GitHub: giwankim/obsidian-vault、salomao-santos/letramento-de-ia、danielcamargo/second-brain),关键句在三份中逐字一致。作者为 Thoughtworks 员工(Thoughtworks 卖咨询,不卖 SDD 工具)。

## C22 (CON)
- 论断:Böckeler 观察到 agent 不遵守 spec:spec-kit 计划阶段的 research 把现有类描述记下,agent 却把这些描述当新规格、重新生成一遍造成重复;也见到 agent 过度执行 constitution 条款。
- 原文:But ultimately the agent ignored the notes that these were descriptions of existing classes, it just took them as a new specification and generated them all over again, creating duplicates.
- URL:https://martinfowler.com/articles/exploring-gen-ai/sdd-3-tools.html
- 来源:Birgitta Böckeler (Thoughtworks), 2025-10-15, Understanding Spec-Driven-Development: Kiro, spec-kit, and Tessl, martinfowler.com · 2025-10 · 【媒体】 · T2 · 案例 · verbatim-checked
- 备注:martinfowler.com 被网络策略拦截;正文取自 3 份独立的网页剪藏(GitHub: giwankim/obsidian-vault、salomao-santos/letramento-de-ia、danielcamargo/second-brain),关键句在三份中逐字一致。作者为 Thoughtworks 员工(Thoughtworks 卖咨询,不卖 SDD 工具)。

## C23 (CON)
- 论断:Böckeler 把 spec-as-source(Tessl)与 MDD(模型驱动开发)类比:MDD 在业务应用中从未普及,处于尴尬的抽象层、开销与约束过大;LLM 去掉了可解析 DSL 与代码生成器的成本,但代价是非确定性,担心 spec-anchored/spec-as-source 会同时继承两者的缺点:不灵活且非确定。
- 原文:I wonder if spec-as-source, and even spec-anchoring, might end up with the downsides of both MDD and LLMs: Inflexibility *and* non-determinism.
- URL:https://martinfowler.com/articles/exploring-gen-ai/sdd-3-tools.html
- 来源:Birgitta Böckeler (Thoughtworks), 2025-10-15, Understanding Spec-Driven-Development: Kiro, spec-kit, and Tessl, martinfowler.com · 2025-10 · 【媒体】 · T3 · 评论 · verbatim-checked
- 备注:martinfowler.com 被网络策略拦截;正文取自 3 份独立的网页剪藏(GitHub: giwankim/obsidian-vault、salomao-santos/letramento-de-ia、danielcamargo/second-brain),关键句在三份中逐字一致。作者为 Thoughtworks 员工(Thoughtworks 卖咨询,不卖 SDD 工具)。 「MDD never took off for business applications」为作者亲历判断,无采用率数据——交 HIST 线用调查数据核。

## C24 (CON)
- 论断:Böckeler 并不否定 spec-first:她本人常先写某种 spec 给 agent,认为 spec-first 原则「在许多情况下肯定有价值」;但「spec-driven development」一词定义不清、已语义稀释,有人把 spec 当作「详细 prompt」的同义词。
- 原文:So the general principle of spec-first is definitely valuable in many situations
- URL:https://martinfowler.com/articles/exploring-gen-ai/sdd-3-tools.html
- 来源:Birgitta Böckeler (Thoughtworks), 2025-10-15, Understanding Spec-Driven-Development: Kiro, spec-kit, and Tessl, martinfowler.com · 2025-10 · 【媒体】 · mixed · 评论 · verbatim-checked
- 备注:martinfowler.com 被网络策略拦截;正文取自 3 份独立的网页剪藏(GitHub: giwankim/obsidian-vault、salomao-santos/letramento-de-ia、danielcamargo/second-brain),关键句在三份中逐字一致。作者为 Thoughtworks 员工(Thoughtworks 卖咨询,不卖 SDD 工具)。 反方阵营常被简化为「Böckeler 反对 SDD」——不准确,她批评的是重型工具流程,不是先写 spec。

## C25 (CON)
- 论断:Eberhardt 用 Spec Kit(GitHub Copilot + Claude Sonnet 4.5)重建其业余应用 KartLog 中一个被他删除的约 1,000 行功能(赛道 CRUD):第一增量 agent 运行 33m30s、产出 689 行代码、2,577 行 markdown、人工审阅约 3.5 小时;其中 Plan 一步产出 2,067 行 markdown(444 行模块契约、395 行数据模型、285 行计划、500 行 quickstart、406 行 research)。
- 原文:* 33m30 - of agent execution time
* 689 loc
* 2,577 lines of markdown
* 3.5 hrs review time
- URL:https://blog.scottlogic.com/2025/11/26/putting-spec-kit-through-its-paces-radical-idea-or-reinvented-waterfall.html
- 来源:Colin Eberhardt (Scott Logic CTO), 2025-11-26, Putting Spec Kit Through Its Paces: Radical Idea or Reinvented Waterfall?, Scott Logic blog · 2025-11 · 【媒体】 · T2 · 案例 · verbatim-checked
- 备注:blog.scottlogic.com 未直接抓取;正文取自 Scott Logic 官方博客源码仓库 github.com/ScottLogic/blog _posts/2025-11-26-...markdown(一手源文件)。 现场核验(kartlog git 历史):删除提交 e2c31dab −1,069 行;spec 提交 cf299c7a +230 行 md;plan 提交 66763b00 +2,067 行 md;实现提交 ba5ef7c4 +689 行;constitution 161 行——均与文中一致。但 Tasks 一节的统计被误复制成 Plan 的数字(实际 tasks 提交 +312 行),且 161+230+2,067+312=2,770 ≠ 文中合计 2,577。审阅时间为自报、未计时工具。n=1、作者重建的是自己已写过的功能。

## C26 (CON)
- 论断:同一功能用 Eberhardt 惯用的小增量迭代提示:agent 8 分钟、约 1,000 行代码、零 markdown、15 分钟代码审阅、9 分钟功能测试与小修;他据此称不用 SDD 时自己「大约快十倍」,且实现无 bug。
- 原文:The simple fact is I am a lot more productive without SDD, around ten times faster.
- URL:https://blog.scottlogic.com/2025/11/26/putting-spec-kit-through-its-paces-radical-idea-or-reinvented-waterfall.html
- 来源:Colin Eberhardt (Scott Logic CTO), 2025-11-26, Putting Spec Kit Through Its Paces: Radical Idea or Reinvented Waterfall?, Scott Logic blog · 2025-11 · 【媒体】 · T2 · 案例 · verbatim-checked
- 备注:blog.scottlogic.com 未直接抓取;正文取自 Scott Logic 官方博客源码仓库 github.com/ScottLogic/blog _posts/2025-11-26-...markdown(一手源文件)。 对照不对称:文中未说明迭代版计时来自原始构建还是重建(一份二手综述称是「第二次构建一个他已熟悉的功能」);迭代臂约 1,000 行覆盖两个增量(含 GPS),SDD 臂两增量合计 agent 57m、约 5.5h 审阅。按文中数字算倍数约 7.6×(仅增量一)~12×(两增量)。'十倍'是作者自估,非受控实验。

## C27 (CON)
- 论断:Eberhardt 认为 Spec Kit 产出的 markdown 大量重复且是「伪上下文」(如为「戴手套操作」编造 UI 理由),Spec Kit 消耗大量 agent 时间写 markdown,最终并未带来更好的产品。
- 原文:Furthermore, Spec Kit burnt through a lot of agent time creating markdown files that ultimately didn’t result in a better product.
- URL:https://blog.scottlogic.com/2025/11/26/putting-spec-kit-through-its-paces-radical-idea-or-reinvented-waterfall.html
- 来源:Colin Eberhardt (Scott Logic CTO), 2025-11-26, Putting Spec Kit Through Its Paces: Radical Idea or Reinvented Waterfall?, Scott Logic blog · 2025-11 · 【媒体】 · T2 · 案例 · verbatim-checked
- 备注:blog.scottlogic.com 未直接抓取;正文取自 Scott Logic 官方博客源码仓库 github.com/ScottLogic/blog _posts/2025-11-26-...markdown(一手源文件)。 未测 token 数(文中说要列 token 但实际未列)。

## C28 (CON)
- 论断:Eberhardt 为 SDD 留了余地:承认可能是自己用法不对、不确定该用于多大的问题,且自己可能不是目标用户(他是亲自审代码的架构师),Spec Kit 也许是给 vibe coder/产品负责人/不写代码的人用的。
- 原文:Furthermore, I am willing to entertain the possibility that I am simply just using it wrong!
- URL:https://blog.scottlogic.com/2025/11/26/putting-spec-kit-through-its-paces-radical-idea-or-reinvented-waterfall.html
- 来源:Colin Eberhardt (Scott Logic CTO), 2025-11-26, Putting Spec Kit Through Its Paces: Radical Idea or Reinvented Waterfall?, Scott Logic blog · 2025-11 · 【媒体】 · n/a · 评论 · verbatim-checked
- 备注:blog.scottlogic.com 未直接抓取;正文取自 Scott Logic 官方博客源码仓库 github.com/ScottLogic/blog _posts/2025-11-26-...markdown(一手源文件)。

## C29 (CON)
- 论断:Zaninotto 引用的例子:某开发者用 Spec Kit 为一个工时追踪应用「显示当前日期」,产出 8 个文件、1,300 行文本;另一 Kiro 例子为 Atomic CRM 加「referred by」字段。他列出 7 项缺陷(上下文盲、Markdown 泛滥、系统性官僚、伪敏捷、双重代码审阅、虚假安全感、收益递减)。
- 原文:Here’s an example using GitHub’s spec-kit, where a developer wanted to display the current date on a time-tracking app, resulting in 8 files and 1,300 lines of text
- URL:https://marmelab.com/blog/2025/11/12/spec-driven-development-waterfall-strikes-back.html
- 来源:François Zaninotto (Marmelab CEO), 2025-11-12, Spec-Driven Development: The Waterfall Strikes Back, Marmelab blog · 2025-11 · 【媒体】 · T2 · 案例 · verbatim-checked
- 备注:marmelab.com 未直接抓取;正文取自 HN 文章存档 github.com/artur-shlyapnikov/hn-distill data/raw/articles/45935763.md(整页抓取副本)。作者是 Marmelab CEO,推广自己命名的 'Natural Language Development' 路线——立场方利益:不卖 SDD 工具,但有替代方法论品牌。 现场核验 adguernier/frequentito PR#42:specs/002-display-current-date/ 下确为 8 个文件,但新增 1,865 行(非 1,300);生产代码约 126 行(CurrentDate.tsx 101 + page.tsx 6 + types 19),另有测试/stories 605 行;PR 还含 Spec Kit 脚手架 .specify/ 等,总计 +6,151 行。'1,300' 口径不明(可能是早期快照或只计部分文件)。Marmelab 本身未做任何计时或计量实验。 quote 为页面渲染文本(剪藏中括号内为超链接锚文本,已去除 markdown 链接标记)。

## C30 (CON)
- 论断:Zaninotto 称 SDD 让开发者 80% 时间在读而非思考,且 agent 并不总遵守 spec:Kiro 例子中 agent 把「验证实现」任务标为完成却没写一个单元测试,只写了手工测试说明。
- 原文:In the example above, the agent marked the “verify implementation” task as done without writing a single unit test—it wrote manual testing instructions instead.
- URL:https://marmelab.com/blog/2025/11/12/spec-driven-development-waterfall-strikes-back.html
- 来源:François Zaninotto (Marmelab CEO), 2025-11-12, Spec-Driven Development: The Waterfall Strikes Back, Marmelab blog · 2025-11 · 【媒体】 · T2 · 案例 · verbatim-checked
- 备注:marmelab.com 未直接抓取;正文取自 HN 文章存档 github.com/artur-shlyapnikov/hn-distill data/raw/articles/45935763.md(整页抓取副本)。作者是 Marmelab CEO,推广自己命名的 'Natural Language Development' 路线——立场方利益:不卖 SDD 工具,但有替代方法论品牌。 '80%' 为修辞性估计('spending 80% of your time reading instead of thinking'),无测量,不得承重。

## C31 (CON)
- 论断:Zaninotto 承认 SDD 帮 agent 保持在任务上、偶尔能发现开发者遗漏的边界情况,并称 SDD 在从零起步的新项目中表现好,但随应用增长 spec 越来越失准并拖慢开发,对大型既有代码库「基本不可用」。
- 原文:SDD shines when starting a new project from scratch, but as the application grows, the specs miss the point more often and slow development. For large existing codebases, SDD is mostly unusable.
- URL:https://marmelab.com/blog/2025/11/12/spec-driven-development-waterfall-strikes-back.html
- 来源:François Zaninotto (Marmelab CEO), 2025-11-12, Spec-Driven Development: The Waterfall Strikes Back, Marmelab blog · 2025-11 · 【媒体】 · T2 · 评论 · verbatim-checked
- 备注:marmelab.com 未直接抓取;正文取自 HN 文章存档 github.com/artur-shlyapnikov/hn-distill data/raw/articles/45935763.md(整页抓取副本)。作者是 Marmelab CEO,推广自己命名的 'Natural Language Development' 路线——立场方利益:不卖 SDD 工具,但有替代方法论品牌。 断言无数据支撑。

## C32 (CON)
- 论断:Spec Kit issue #1492(2026-01-20,用户 john-agentic-ai-tools):在 Claude Code + Anthropic Pro 账户上配合 Spec Kit,通常不到一小时即触达用量上限,用户推测生成的 spec 工件过长/冗余推高 token。
- 原文:When using the framework with Claude Code on an Anthropic Pro account, usage limits are typically reached in under an hour of active work.
- URL:https://github.com/github/spec-kit/issues/1492
- 来源:john-agentic-ai-tools, 2026-01-20, Excessive Token Usage with Claude Code (Anthropic Pro), github/spec-kit issue #1492 · 2026-01 · 【媒体】 · T2 · 案例 · verbatim-checked
- 备注:单用户自报、无 token 计数;已关闭,3 条评论(二手综述称有评论者体验较温和,未读到评论原文)。spec-kit 仓库 issue 中含 'token' 的 164 条、'overhead' 32 条、'verbose' 22 条(GitHub 搜索计数,2026-11-11,计 issue 非独立用户)。

## C33 (CON)
- 论断:社区出现专门检测 Spec Kit「幽灵完成」(tasks.md 中被勾选为完成但从未实现的任务)的扩展 spec-kit-verify-tasks,以五层级联(文件存在、git diff、符号 grep、死代码、语义评估)复核——侧面说明「agent 勾任务≠完成任务」是被反复遇到的问题。
- 原文:A **phantom completion** is a task marked `[X]` as done that was never actually implemented.
- URL:https://github.com/datastone-inc/spec-kit-verify-tasks
- 来源:datastone-inc, 2026, spec-kit-verify-tasks README · 2026 · 【厂商】 · T2 · 文档 · verbatim-checked
- 备注:工具作者自述,无发生率数据;存在性证据,非频率证据。

## C34 (CON)
- 论断:Nitin Garg(InfoQ,2026-09)报告的小型受控试点:5 名人类审阅者、一个含 20 条不变式的银行服务;拿到 spec 的审阅者用时约 48 分钟 vs 只看代码者 27 分钟,81% 的发现能对应到具名 spec 条款,但发现问题的比例持平。
- 原文:
- URL:https://www.infoq.com/articles/when-spec-driven-development-pays-off/
- 来源:Nitin Garg, 2026-09-10, When Spec-Driven Development Pays off, InfoQ · 2026-09 · 【媒体】 · T1 · 对照实验 · secondhand
- 备注:infoq.com 被拦截,数字来自两份二手转述(brokenrobot-xyz 博客 2026-10-25;brindlewick/postmaster 摘要称作者声称已被 GAISS 2026 接收但未找到论文/预印本)。n=5,验证阶段须回一手。

## C35 (CON)
- 论断:Matthew Wilson(Instil,2026-06)称 Spec Kit 成本是等价 plan-mode 流程的数倍,但未给数字。
- 原文:
- URL:https://instil.co/blog/spec-driven-development-is-dead-long-live-plan-mode
- 来源:Matthew Wilson, 2026-06, Spec-driven development is dead, long live plan mode, Instil blog · 2026-06 · 【媒体】 · T2 · 评论 · secondhand
- 备注:instil.co 未能抓取;转述自 brokenrobot-xyz 博客('without figures')。不得作为数字证据。


### 搜索角度
- 直接抓取 drops.dagstuhl.de ESEM PDF —— 被会话网络策略拦截(curl CONNECT 403 / WebFetch ENOTFOUND);改从作者 GitHub 仓库 brennhill/delivery-gap-research 取 camera-ready LaTeX 源、SSRN 预印本 PDF、修订计划、勘误与复现数据(成功)
- arxiv.org / export.arxiv.org —— 被拦截;因此 Zietsman 2603.25773、Marri 2602.02584、Tufano 2608.17177、Smékal 2608.25399、Agarwal/SpecMine 2608.25202 等未能读原文
- martinfowler.com —— 被拦截;改用 GitHub 代码搜索找到 3 份独立网页剪藏,交叉比对关键句逐字一致
- blog.scottlogic.com —— 未直接抓;改从 ScottLogic/blog 源码仓库读一手 markdown(成功),并克隆 ColinEberhardt/kartlog 逐提交核对行数(成功)
- marmelab.com —— 未直接抓;使用 HN 存档整页副本(artur-shlyapnikov/hn-distill),并克隆 adguernier/frequentito 抓 PR#42 核对 '8 files / 1,300 lines'(文件数对、行数不符)
- Hill 复现数据 master-prs.csv 复跑 spec'd 计数与来源分解(吻合)并审计 ticket-ID 正则误报(发现 ≥1,161 例)
- grafana/airflow/spark .gitignore 核对 Hill 所述 SDD 产出排除规则(吻合)
- github/spec-kit issue 搜索:token/overhead/verbose/ignores spec/tasks marked complete 计数;读 #1492 正文(评论未读)
- WebSearch:SDD 流程税 / token 成本 / 墙钟的独立测量 —— 找到 Uvik benchmark(归 MEASURE 线)、Instil、DEV 'OpenSpec failed my experiment'、Microsoft Tech Community SpecKit prompt 研究、InfoQ Garg 试点、brokenrobot 综述;除 GitHub 托管者外均无法回一手
- Instil(instil.co)、InfoQ Garg、Hidde de Smet(GitHub 源码已读,纯观点无测量,未收录)、Thomas Johnson 'rebranded BDUF'(未读)、Thoughtworks Radar SDD 'Assess' 条目(未读,建议 VENDOR/ADOPT 线核)
- 未搜到:任何受控的、多被试的 SDD 工作流 vs plan-mode/迭代提示的墙钟或 token 对照实验(除 Uvik 厂商口径外);任何对 Kiro 'bugfix spec' 新流程的独立复测;Hill 研究的独立复现
- 作者利益:Hill 署名独立研究者;LinkedIn 搜索摘要显示其就职 Delivery Hero(二手,未核);其 GitHub 有《The Delivery Gap》配套仓库与 cost-per-accepted-change 指标项目

### 交叉口径问题
- Hill 的处理变量 = 工单/issue 引用存在性(97.5%),不是 Spec Kit/Kiro 工作流;成文不得写成「SDD 不降缺陷」,只能写「开源 PR 中的规格工件与缺陷/返工无关」
- Hill 缺陷=SZZ 归因(误归因 46–71%),返工=30 天关键词+文件重叠启发式;两者与「缺陷率」「返工率」的其他口径(Uvik 合并率、测试通过率)不可互换
- Hill SSRN 预印本头条「spec'd PR 缺陷更多」vs ESEM 终稿「匹配后无差异」——同一数据,不得混引;以终稿为准
- Hill 匹配主估计未报告 CI;p 值在可选停止+事后分析下为名义值
- Hill ticket-ID 正则存在 ≥1,161 例误报(ID-BASED、LLM-GENERATED 等),约占 spec'd 4.8%,倾向衰减效应
- Eberhardt 的「十倍」:单人、单功能、自报审阅时间、对照臂可能是已熟悉功能的重建;按文中数字为 7.6×–12×,且其 Tasks 统计被误复制、markdown 合计数自相矛盾(2,577 vs 逐项和 2,770)
- Marmelab「8 files / 1,300 lines」:实测 PR#42 specs 目录 8 文件但 +1,865 行;Marmelab 自身无测量
- Böckeler「4 user stories / 16 acceptance criteria」逐字核实,但为 2025-10 的 Kiro(GA 前)单次运行;不得外推为 Kiro 当前行为
- Hill 对 Eberhardt 的转述('buggy code')与原文('just fine' + 一个 3 行修复的 bug)不符——二手转述失真示例
- 审阅时间(Eberhardt 3.5h、Garg 48 vs 27 分钟)、agent 墙钟(33m30)、token(#1492 无计数)、markdown 行数是不同成本口径,不得合并成单一「流程税」倍数
- Garg 试点(n=5)与 Instil 只有二手转述;Instil 无数字

# 线 HIST

## H01 (HIST)
- 论断:Royce 1970 在单趟顺序图(Fig.2:系统需求→软件需求→分析→程序设计→编码→测试→运行)正下方第一句即称其实施方式有风险:他'相信这个概念',但所描述的实施'有风险且招致失败';问题在于测试是第一次实际经验(而非分析)时序/存储/IO 的时点,失败时需重大重设计,'可预期最多 100% 的进度和/或成本超支'。
- 原文:I believe in this concept, but the implementation described above is risky and invites failure. ... In effect the development process has returned to the origin and one can expect up to a 100-percent overrun in schedule and/or costs.
- URL:https://github.com/tpn/pdfs (文件 'Managing the Development of Large Software Systems - 1970 (waterfall).pdf', sha256 9f7db065…a78)
- 来源:Royce, W.W., 1970, Managing the Development of Large Software Systems, Proc. IEEE WESCON (TRW 重印本 pp.328-338) · 1970-08 · 【研究】 · n/a · 评论 · verbatim-checked
- 备注:一手 PDF(扫描件)经 pdftotext 抽取并对照页面图像核对;与 tamnd/papers 的 olmOCR 转录同一 PDF(sha 一致)。 '100-percent overrun' 是作者经验判断,无数据。流行说法'Royce 反对瀑布'只对一半:他反对的是'不加五步修正的'实施,不是阶段化本身(见 H02)。

## H02 (HIST)
- 论断:Royce 并未否定阶段化顺序:同页明言该方法'根本上是健全的',全文是在此'基本方法'上追加五项特征(程序设计先行、文档化设计、做两遍、规划与监控测试、让客户参与)以'消除大部分开发风险';总结称不加这五步的'更简单方法'在大型项目中'从未奏效'。
- 原文:However, I believe the illustrated approach to be fundamentally sound. The remainder of this discussion presents five additional features that must be added to this basic approach to eliminate most of the development risks. ... In my experience, however, the simpler method has never worked on large software development efforts and the costs to recover far exceeded those required to finance the five-step process listed.
- URL:https://github.com/tpn/pdfs (文件 'Managing the Development of Large Software Systems - 1970 (waterfall).pdf', sha256 9f7db065…a78)
- 来源:Royce, W.W., 1970, Managing the Development of Large Software Systems, Proc. IEEE WESCON (TRW 重印本 pp.328-338) · 1970-08 · 【研究】 · mixed · 评论 · verbatim-checked
- 备注:一手 PDF(扫描件)经 pdftotext 抽取并对照页面图像核对;与 tamnd/papers 的 olmOCR 转录同一 PDF(sha 一致)。 关键口径:'simpler method' 指不加五步的 Fig.2 流程,不是'瀑布 vs 迭代'。Royce 的修正方向是'更多前置设计和文档 + 一次试点',而非轻文档迭代——这是与 SDD 同构的地方。

## H03 (HIST)
- 论断:Royce 承认设计迭代会越过相邻阶段:Fig.3 是'理想'(迭代只发生在相邻步骤),Fig.4 图注直言对所示流程'设计迭代从不局限于相邻步骤'。
- 原文:Figure4. Unfortunately, for the process illustrated, the design iterations are never confined to the successive steps.
- URL:https://github.com/tpn/pdfs (文件 'Managing the Development of Large Software Systems - 1970 (waterfall).pdf', sha256 9f7db065…a78)
- 来源:Royce, W.W., 1970, Managing the Development of Large Software Systems, Proc. IEEE WESCON (TRW 重印本 pp.328-338) · 1970-08 · 【研究】 · n/a · 评论 · verbatim-checked
- 备注:一手 PDF(扫描件)经 pdftotext 抽取并对照页面图像核对;与 tamnd/papers 的 olmOCR 转录同一 PDF(sha 一致)。 OCR 原文词间空格缺失,已按页面恢复。

## H04 (HIST)
- 论断:Royce 是重文档/规约先行的倡导者:'文档化设计'一节称需要'相当多'文档,'管理软件开发的第一条规则是无情地强制执行文档要求';文档严重不足时他的建议是'撤换项目管理层,停止一切与文档无关的活动';并宣称在编码开始前'文档、规约、设计'三者是同一件事。
- 原文:The first rule of managing software development is ruthless enforcement of documentation requirements. ... Replace project management. Stop all activities not related to documentation. ... During the early phase of software development the documentation is the specification and is the design. Until coding begins these three nouns (documentation, specification, design) denote a single thing. If the documentation is bad the design is bad.
- URL:https://github.com/tpn/pdfs (文件 'Managing the Development of Large Software Systems - 1970 (waterfall).pdf', sha256 9f7db065…a78)
- 来源:Royce, W.W., 1970, Managing the Development of Large Software Systems, Proc. IEEE WESCON (TRW 重印本 pp.328-338) · 1970-08 · 【研究】 · mixed · 评论 · verbatim-checked
- 备注:一手 PDF(扫描件)经 pdftotext 抽取并对照页面图像核对;与 tamnd/papers 的 olmOCR 转录同一 PDF(sha 一致)。 这是与 SDD'spec 即设计'叙事最直接的历史同构;'is the specification and is the design' 中两处 is 在原件加下划线。

## H05 (HIST)
- 论断:Royce 给出规模对比:采购 500 万美元硬件约需 30 页规约,采购 500 万美元软件约需 '1?00' 页规约方可达到同等控制。扫描件该数字残损:页面图像中第二位字符缺损,olmOCR 转录读作 1000,常见二手转述作 1500。
- 原文:In order to procure a 5 million dollar hardware device, I would expect that a 30 page specification would provide adequate detail to control the procurement. In order to procure 5 million dollars of software I would estimate a 1[?]00 page specification is about right in order to achieve comparable control.
- URL:https://github.com/tpn/pdfs (文件 'Managing the Development of Large Software Systems - 1970 (waterfall).pdf', sha256 9f7db065…a78)
- 来源:Royce, W.W., 1970, Managing the Development of Large Software Systems, Proc. IEEE WESCON (TRW 重印本 pp.328-338) · 1970-08 · 【研究】 · T1 · 评论 · verbatim-checked
- 备注:已在 400dpi 页面图像上核对:字符形似 '1500' 但第二位残损,不可确定 1000/1500。成文时写'上千页'或注明数字残损,不得单点引用 1500。纯经验估计,无数据。

## H06 (HIST)
- 论断:Royce 第 3 步'做两遍':若产品是首创,应安排交付给客户的版本实为关键设计/运行领域的'第二版';例:30 个月项目可安排 10 个月试点模型,12 个月项目试点压缩到约 3 个月;第 5 步要求客户在需求定义后的三个节点正式介入。
- 原文:If the computer program in question is being developed for the first time, arrange matters so that the version finally delivered to the customer for operational deployment is actually the second version insofar as critical design/operations areas are concerned. ... If the effort runs 30 months then this early development of a pilot model might be scheduled for 10 months.
- URL:https://github.com/tpn/pdfs (文件 'Managing the Development of Large Software Systems - 1970 (waterfall).pdf', sha256 9f7db065…a78)
- 来源:Royce, W.W., 1970, Managing the Development of Large Software Systems, Proc. IEEE WESCON (TRW 重印本 pp.328-338) · 1970-08 · 【研究】 · T2 · 评论 · verbatim-checked
- 备注:一手 PDF(扫描件)经 pdftotext 抽取并对照页面图像核对;与 tamnd/papers 的 olmOCR 转录同一 PDF(sha 一致)。 '做两遍'在后世'瀑布'描述中通常被删除(见 H11 Larman & Basili)。与'spec 可再生代码/扔掉重来'叙事有可比性:Royce 的试点是为暴露时序/存储等'只能经验而非分析'的问题。

## H07 (HIST)
- 论断:Royce 认为分析与编码阶段'通常管理起来相对容易',对需求、设计、测试影响很小;困难在于两头(需求/设计与测试)。即 1970 年的大型系统语境中编码已被视为相对廉价的环节。
- 原文:One cannot, of course, produce software without these steps, but generally these phases are managed with relative ease and have little impact on requirements, design, and testing.
- URL:https://github.com/tpn/pdfs (文件 'Managing the Development of Large Software Systems - 1970 (waterfall).pdf', sha256 9f7db065…a78)
- 来源:Royce, W.W., 1970, Managing the Development of Large Software Systems, Proc. IEEE WESCON (TRW 重印本 pp.328-338) · 1970-08 · 【研究】 · n/a · 评论 · verbatim-checked
- 备注:一手 PDF(扫描件)经 pdftotext 抽取并对照页面图像核对;与 tamnd/papers 的 olmOCR 转录同一 PDF(sha 一致)。 语境:航天任务规划软件,'分析'指轨道力学等数学分析,产出'几行串行算术代码'。'代码便宜、规约贵'并非 LLM 时代新命题——但 Royce 的结论是加大前置投入,而 SDD 的新意须另证。

## H08 (HIST)
- 论断:'waterfall'一词不出现在 Royce 1970 原文中(对全 11 页 PDF 的文本层检索 0 次;独立 olmOCR 转录 8 个章节文件检索 0 次)。
- 原文:
- URL:https://github.com/tpn/pdfs (文件 'Managing the Development of Large Software Systems - 1970 (waterfall).pdf', sha256 9f7db065…a78)
- 来源:Royce, W.W., 1970, Managing the Development of Large Software Systems, Proc. IEEE WESCON (TRW 重印本 pp.328-338) · 1970-08 · 【研究】 · n/a · 文档 · verbatim-checked
- 备注:否定性核验:扫描件 OCR 有错字风险,但两种独立抽取一致为 0;多个二手核验(Milkeles/software-doc-templates、sa2taka 博客等)亦称不存在。

## H09 (HIST)
- 论断:已知最早把 Royce 的顺序图称为'waterfall'的印刷文献通常归于 Bell & Thayer 1976(TRW,ICSE'76 pp.61-68):在论证'自上而下方法优于自下而上'时,称 Royce'引入了开发活动的瀑布概念',并以纪律化顺序呈现(其 Fig.1 对应 Royce 自己说'招致失败'的 Fig.2)。
- 原文:The same top-down approach to a series of requirements statements is explained, without the specialized military jargon, in an excellent paper by Royce [5]; he introduced the concept of the "waterfall" of development activities. In this approach software is developed in the disciplined sequence of activities shown in Figure 1.
- URL:https://dl.acm.org/doi/10.5555/800253.807650
- 来源:Bell, T.E. & Thayer, T.A., 1976, Software Requirements: Are They Really a Problem?, Proc. ICSE 2, pp.61-68 · 1976-10 · 【研究】 · T1 · 观察 · secondhand
- 备注:未取得一手 PDF(ACM/镜像站被网络策略拦截)。引文来自两份独立转录(sa2taka/next-blog 日文博客的英文摘录;thorwhalen/essays 引文)逐字一致。'首次使用'是'目前已知最早'而非'创造';Bell & Thayer 与 Royce 同属 TRW。

## H10 (HIST)
- 论断:Larman & Basili 2003(IEEE Computer)称 Royce 1970 常被'错误地'当作单趟瀑布的典范,并引 Royce 之子 Walker Royce 私人通信:其父'一直是迭代、增量、演进式开发的支持者';但同文也承认 Royce 的'做两遍'虽含反馈迭代的端倪,'显然不是经典的迭代增量开发(IID)'。
- 原文:He was always a proponent of iterative, incremental, evolutionary development. His paper described the waterfall as the simplest description, but that it would not work for all but the most straightforward projects. ... This iterative feedback-based step in a classic "waterfall paper" has been lost in most descriptions of this model, although it was clearly not classic IID.
- URL:https://doi.org/10.1109/MC.2003.1204375
- 来源:Larman, C. & Basili, V.R., 2003, Iterative and Incremental Development: A Brief History, IEEE Computer 36(6):47-56 · 2003-06 · 【研究】 · n/a · 评论 · secondhand
- 备注:读到的是 c2 wiki HistoryOfIterative 页面(Larman 上传的草稿摘录,BekaValentine/c2_wiki_recovery 存档)而非期刊终稿。Walker Royce 引语为私人通信、事后由亲属转述,属弱证据;Larman 是 IID/敏捷推广者(立场相关)。

## H11 (HIST)
- 论断:Brooks《没有银弹》:构建软件最难的单一部分是'精确决定要构建什么';客户并不知道自己要什么,因此最重要的职能是'迭代地提取和细化产品需求';'可预先规定一个令人满意的系统、招标、建造、安装'这一采购假设'根本上是错误的'。
- 原文:The hardest single part of building a software system is deciding precisely what to build. ... Therefore the most important function that the software builder does for his client is the iterative extraction and refinement of the product requirements. For the truth is, the client does not know what he wants. ... Much of present-day software acquisition procedures rests upon the assumption that one can specify a satisfactory system in advance, get bids for its construction, have it built, and install it. I think this assumption is fundamentally wrong
- URL:https://www.cs.unc.edu/techreports/86-020.pdf
- 来源:Brooks, F.P., 1986/1987, No Silver Bullet: Essence and Accidents of Software Engineering, UNC TR86-020 / IEEE Computer 20(4) · 1986-?? · 【研究】 · T1 · 评论 · paraphrase-checked
- 备注:读到的是 tamnd/papers 对 UNC TR86-020(sha a4a11dcb…)的 olmOCR 视觉转录,未自看 PDF 页面;技术报告版与 1987 期刊版措辞可能略异。正方/反方皆可引:支持'需求是难点',但反对'一次性预先规定'。

## H12 (HIST)
- 论断:Brooks 记录'自动编程'(由问题规约生成程序)已被期待近 40 年,并引 Parnas:'自动编程一直是用比当时可用的更高级语言编程的委婉说法';Parnas 认为多数情况下必须给出规约的是解法而非问题。
- 原文:For almost 40 years, people have been anticipating and writing about "automatic programming", the generation of a program for solving a problem from a statement of the problem specifications. ... In short, automatic programming always has been a euphemism for programming with a higher-level language than was presently available to the programmer.
- URL:https://www.cs.unc.edu/techreports/86-020.pdf
- 来源:Brooks, F.P., 1986, No Silver Bullet (引 Parnas) · 1986-?? · 【研究】 · mixed · 评论 · paraphrase-checked
- 备注:同 H11 转录口径。Parnas 原句是 Brooks 转引(Parnas 1985 SDI 相关论文),未回 Parnas 原文。与'spec 即新代码'口号直接对位的历史判断。

## H13 (HIST)
- 论断:Brooks:即便完美的程序验证也只能证明程序符合其规约;软件任务最难的是得到完整一致的规约,构建程序的本质很大部分其实是'调试规约'。
- 原文:More seriously, even perfect program verification can only establish that a program meets its specification. The hardest part of the software task is arriving at a complete and consistent specification, and much of the essence of building a program is in fact the debugging of the specification.
- URL:https://www.cs.unc.edu/techreports/86-020.pdf
- 来源:Brooks, F.P., 1986, No Silver Bullet §4.7 · 1986-?? · 【研究】 · T3 · 评论 · paraphrase-checked
- 备注:同 H11。可与 FORMAL 线'陈述=意图'鸿沟对接。

## H14 (HIST)
- 论断:Brooks 对图形化/可视化编程的判断:'至今没有出现任何令人信服、更不用说令人兴奋的成果,我确信也不会有';流程图作为设计工具'基本无用'——'程序员是在写完程序之后、而非之前画流程图'。
- 原文:Nothing even convincing, much less exciting, has yet emerged from such efforts. I am persuaded that nothing will. ... it has proved to be essentially useless as a design tool — programmers draw flowcharts after, not before, writing the programs they describe.
- URL:https://www.cs.unc.edu/techreports/86-020.pdf
- 来源:Brooks, F.P., 1986, No Silver Bullet §4.6 · 1986-?? · 【研究】 · mixed · 评论 · paraphrase-checked
- 备注:同 H11。'事后补画'对应后文 Petre 'retrofit' 与 SDD'事后补 spec'风险;是观点非测量。

## H15 (HIST)
- 论断:Parnas & Clements 1986:'我们永远找不到一种让我们以完全理性方式设计软件的过程',但可以'伪装'——把系统按理性设计者的样子呈现(文档按理想过程组织);列 7 条理由,包括委托方不知道自己要什么、许多细节只在实现中才显现、外部变化会推翻先前决策。
- 原文:The bad news is that, in our opinion, we will never find the philosopher's stone. We will never find a process that allows us to design software in a perfectly rational way. The good news is that we can fake it. ... (1) In most cases the people who commission the building of a software system do not know exactly what they want and are unable to tell us all that they know.
- URL:https://doi.org/10.1109/TSE.1986.6312940
- 来源:Parnas, D.L. & Clements, P.C., 1986, A Rational Design Process: How and Why to Fake It, IEEE TSE SE-12(2) · 1986-02 · 【研究】 · T1 · 评论 · paraphrase-checked
- 备注:读到的是 AndrewGodlewsky/code-comments 仓库对 PDF 的逐页文本抽取(含 OCR 词内空格,已规整),未自看 PDF。对 SDD 的含义:spec 可作为'事后整理的理性化文档'而非真实生成顺序。

## H16 (HIST)
- 论断:Parnas & Clements 1986 对文档维护的判断:按'意识流/执行流'组织的文档难以找到需随软件变更而修改的部分,'维护代价高昂,在大多数情况下不会被维护';未被使用过的文档'总会是糟糕的文档'。
- 原文:It will not be easy to find all the parts of the document that should be changed when the software is changed. The documentation will be expensive to maintain and, in most cases, will not be maintained. ... documentation that has not been used before it is published, documentation that is not important to its author, will always be poor documentation.
- URL:https://doi.org/10.1109/TSE.1986.6312940
- 来源:Parnas & Clements 1986, §VI · 1986-02 · 【研究】 · mixed · 评论 · paraphrase-checked
- 备注:同 H15。是'spec 漂移'的 40 年前机制描述,但属专家观点,无测量。

## H17 (HIST)
- 论断:Dijkstra EWD667(约 1978):主张用母语指挥机器并不会简化人的工作,因为跨接口的协作/通信工作量需加上,'窄接口'因此受青睐;形式符号应视为'特权'而非负担;母语的'自然'归结为易于说出'其荒谬并不明显'的陈述。
- 原文:Instead of regarding the obligation to use formal symbols as a burden, we should regard the convenience of using them as a privilege ... When all is said and told, the "naturalness" with which we use our native tongues boils down to the ease with which we can use them for making statements the nonsense of which is not obvious.
- URL:https://www.cs.utexas.edu/~EWD/transcriptions/EWD06xx/EWD667.html
- 来源:Dijkstra, E.W., c.1978, On the foolishness of "natural language programming" (EWD667) · 1978-?? · 【研究】 · T1 · 评论 · secondhand
- 备注:UT Austin EWD 档案被网络策略拦截;读到的是 limpdev/GoMark 的转录(加了高亮标记),与多份 GitHub 转录片段一致。纯论述。T1 自然语言 spec 的反方历史论据。

## H18 (HIST)
- 论断:Boehm 1981《软件工程经济学》缺陷修复成本曲线(p.40)基于 1970 年代后期大型系统的四个来源(IBM、TRW、GTE、Bell Labs SAFEGUARD);Menzies 等指出 Daly77 与 Boehm76 未说明'成本'是工时还是实际费用,且'数据点未公开可供分析';同图另有虚线'较小项目'曲线明显平坦(需求→验收约 5-9 倍 vs 大项目→运行阶段约 100 倍以上)。
- 原文:Figure~\ref{fig:cost-to-fix} shows the DIE as reported in Software Engineering Economics based on data from large systems in the late 70s from IBM, TRW, GTE, and Bell Labs. We note that it is unclear from the text in [Daly77] and [Boehm76] if cost is defined in terms of effort, or in actual cost (i.e., labor, materiel, travel, etc). The data points from these studies are not published for analysis.
- URL:https://github.com/ai-se/phaseDelay (phaseDelay4Emse.tex; boehm81.png)
- 来源:Menzies, T., Nichols, W., Shull, F., Layman, L., 2017, Are delayed issues harder to resolve? Revisiting cost-to-fix of defects throughout the lifecycle, Empirical Software Engineering 22:1903-1935(作者 LaTeX 源,2016-09 提交) · 2016-09 · 【研究】 · n/a · 评论 · verbatim-checked
- 备注:Boehm 1981 原书未取得;曲线是 Menzies 等重绘图(倍数为读图估计,对数轴)。读的是作者 LaTeX 源而非出版终稿(引文中 \cite 已删)。'100x'只对应大型项目、运行阶段、相对需求阶段,不能泛化。

## H19 (HIST)
- 论断:Boehm & Basili 2001 'Top 10 缺陷减少清单'第 1 条:交付后发现并修复问题'往往'比在需求和设计阶段贵 100 倍;同条自限:对小型非关键系统,成本放大系数'更像 5:1 而非 100:1',良好架构实践可显著降低该系数。
- 原文:Finding and fixing a software problem after delivery is often 100 times more expensive than finding and fixing it during the requirements and design phase. ... the cost-escalation factor for small, noncritical software systems is more like 5:1 than 100:1
- URL:https://doi.org/10.1109/2.962984
- 来源:Boehm, B. & Basili, V.R., 2001, Software Defect Reduction Top 10 List, IEEE Computer 34(1):135-137 · 2001-01 · 【研究】 · n/a · 评论 · secondhand
- 备注:未读到一手 PDF(umd.edu 被拦截)。两句均在 ≥4 份独立 GitHub 文档中逐字一致(含一份标注'Read in full (extracted locally)')。属杂志专栏、非同行评审研究;流行转述几乎总是丢掉'often'和'5:1'限定。

## H20 (HIST)
- 论断:Bossavit 溯源:Pressman 版'1 : 6.5 : 15 : 60-100'比率引用的是 'IBM Systems Sciences Institute 1981 课程讲义';该机构实为 IBM 内部培训单位(洛杉矶,约 1967 年起运作,1982 年前更名),不是研究机构;称其为'IBM 研究'不当,原始项目数据(若存在)不晚于 1981 年、可能早至 1967 年。
- 原文:the Institute was a corporate training program, not a research body; as such it is inappropriate to cite the source of the ratios as "an IBM study" or "a study by the IBM Systems Science Institute", in the total absence of any claim that the Institute was the primary source; the original project data, if any exist, are not more recent than 1981, and probably older; and could be as old as 1967.
- URL:https://gist.github.com/Morendil/ebfa32d10528af04e2ccb8995e3cb4a7
- 来源:Bossavit, L., c.2019, The IBM Systems Science Institute (gist, 'Defect Cost Increase: Pressman Ratios') · 2019-?? · 【研究】 · n/a · 文档 · verbatim-checked
- 备注:作者一手(Bossavit 的 GitHub 帐号 Morendil),非同行评审,依据 Google Books 广告、讣告、NYT。《Leprechauns of Software Engineering》(leanpub)本体未能访问,书中对 Boehm 曲线的完整论证未核。

## H21 (HIST)
- 论断:Menzies 等 2017 对 171 个项目(2006-2014,全球,TSP 方法,47,376 条缺陷日志;212 个项目中剔除缺陷 <30 的 41 个)检验'延迟问题效应',未发现证据:后期阶段解决问题的工时并非一致或显著地高于引入后不久即解决。作者结论:DIE 可能是'历史遗物',只在某些类型项目中间歇出现。
- 原文:We found no evidence for the delayed issue effect; i.e. the effort to resolve issues in a later phase was not consistently or substantially greater than when issues were resolved soon after their introduction. ... DIE might be an historical relic that occurs intermittently only in certain kinds of projects.
- URL:https://github.com/ai-se/phaseDelay
- 来源:Menzies et al., 2017, Are delayed issues harder to resolve?, EMSE 22 · 2016-09 · 【研究】 · n/a · 观察 · verbatim-checked
- 备注:利益相关:数据全部来自 TSP,而 TSP 由第二、三作者雇主(SEI)推广;项目偏小(中位工期 46 天、最长增量 90 天;中位团队 7 人,最多 40);修复工时为开发者自记。外推到大型/长周期/安全关键系统不成立——恰与 Boehm 大项目口径不重叠,两者并非直接矛盾。

## H22 (HIST)
- 论断:Menzies 等的文献追溯:几乎所有关于延迟问题效应的引用都可追到 Boehm 1981 或其相关作品;Shull 等 2002 e-workshop 中 Toshiba 与 IBM 报告大项目早期 vs 交付后修复成本比 1:137 和 1:117,但未提供原始数据点;NASA JSC 数据显示某些非关键缺陷修复成本跨阶段基本恒定(早期均 1.2 小时 vs 后期 1.5 小时)。
- 原文:nearly every citation to the delayed issue effect could be traced to the seminal Software Engineering Economics or its related works. ... Workshop participants from Toshiba and IBM reported cost-to-fix ratios between early lifecycle and post-delivery defects of 1:137 and 1:117 for large projects respectively -- but the raw data points were not provided and thus cannot be confirmed.
- URL:https://github.com/ai-se/phaseDelay
- 来源:Menzies et al., 2017, §2 文献综述 · 2016-09 · 【研究】 · n/a · 评论 · verbatim-checked
- 备注:二级综述中转述 Shull 2002,未回 Shull 原文。'1:117/1:137'同样是无原始数据的工作坊口径。

## H23 (HIST)
- 论断:Petre 2013(ICSE)访谈 50 家公司的 50 名专业开发者,声明的当前 UML 使用:不用 UML 35、选择性使用 11、自动代码生成 3、事后补画(retrofit)1、全面采用 0(全面采用仅见于二手报告)。选择性使用者把 UML 当'思考工具',用完即弃。
- 原文:Category of UML Use / Instances of Declared Current Use: no UML 35; retrofit 1; automated code generation 3; selective 11; wholehearted 0 ... Selective (11/50): UML is used in design in a personal, selective, and informal way, for as long as it is considered useful, after which it is discarded
- URL:https://doi.org/10.1109/ICSE.2013.6606618
- 来源:Petre, M., 2013, UML in Practice, ICSE 2013 pp.722-731 · 2013-05 · 【研究】 · mixed · 调查 · verbatim-checked
- 备注:读到的是 cefn/firmware-codesign-readinglog 中该论文 PDF 的 pdfx 全文抽取。方法部分称访谈'历时 2 年、超过 50 人',表格按 50 计;非随机抽样、定性研究;计数为个人而非团队。

## H24 (HIST)
- 论断:Petre 2013 的不采用理由之一是同步/一致性:多名受访者指出图与图之间、模型与代码之间的同步/一致性问题是全面采用 UML 的障碍;并批评 UML 复杂、缺乏形式语义。
- 原文:A number of informants identified issues of synchronization or consistency as a barrier for wholesale adoption of UML. ... Informants criticized UML for its complexity, lack of formal semantics, inconsistency, and issues of synchronization between different diagrams (and between models and code).
- URL:https://doi.org/10.1109/ICSE.2013.6606618
- 来源:Petre 2013, UML in Practice · 2013-05 · 【研究】 · mixed · 调查 · verbatim-checked
- 备注:同 H23。'模型-代码同步'即 SDD 主张 2(spec 保持活性)的历史前科;'A number of'未给计数。

## H25 (HIST)
- 论断:Hutchinson 等 2011(ICSE)MDE 产业研究:问卷 250+ 份 + 17 家公司 22 人深访 + 现场观察;文献综述显示 MDE 生产率宣称从 +20% 到 +800% 不等,比较研究结果在 +35% 到 −27% 之间,多数增益宣称无比较研究支持;生产率下降原因包括工具差、过度建模('模型瘫痪')、复杂度上升及'需保持模型/代码同步'。
- 原文:These benefits have reportedly led to productivity increases ranging anywhere from 20 to 800% ... there is anecdotal evidence that cites reasons for decreased productivity – quantified at 27% in [18] – such as poor tool support, a tendency to over-model ("model paralysis"), increased complexity, and the need to keep models/code in sync. ... Of the comparative studies, results vary between a 35% gain to a 27% loss.
- URL:https://doi.org/10.1145/1985793.1985858
- 来源:Hutchinson, J., Whittle, J., Rouncefield, M., Kristoffersen, S., 2011, Empirical Assessment of MDE in Industry, ICSE 2011 pp.471-480 · 2011-05 · 【研究】 · T3 · 调查 · verbatim-checked
- 备注:读到的是 cefn 仓库 pdfx 全文抽取。作者自称定性为主、'应谨慎解读';问卷对象为 MDE 实践者(自选样本)。+20~800% 为文献中的宣称区间,不是本研究测量。

## H26 (HIST)
- 论断:Whittle, Hutchinson, Rouncefield 2014(IEEE Software)调查 450 名 MDE 实践者 + 17 家公司 22 人访谈:MDE 可能比通常认为的更普遍,但开发者很少用它生成整个系统,而是用领域专用语言生成关键部分;多数公司体验到的生产率提升为 20-30%(报告范围 −27% 到 +800%),不足以驱动采用;代码生成是'转移注意力的话题',真正收益在于明确架构;有案例因生成代码可读性差导致代码认证成本升至 8 倍;采用主要取决于社会和组织因素。
- 原文:Findings suggest that MDE may be more widespread than commonly believed, but developers rarely use it to generate whole systems ... although reports of productivity gains vary widely (from a 27% loss to an 800% gain [6]), most companies seem to experience productivity increases of between 20-30%. ... code generation is a red herring when it comes to describing MDE ... code certification costs rose by a factor of eight.
- URL:https://doi.org/10.1109/MS.2013.65
- 来源:Whittle, J., Hutchinson, J., Rouncefield, M., 2014, The State of Practice in Model-Driven Engineering, IEEE Software 31(3):79-85 · 2014-05 · 【研究】 · mixed · 调查 · verbatim-checked
- 备注:读到的是 cefn 仓库对作者稿 PDF 的 pdfx 抽取。样本是 MDE 实践者(幸存者偏差:不用 MDE 的人不在分母里);'20-30%'是'seem to'的定性归纳,非测量均值;'8 倍'是单一政府信息系统案例。

## H27 (HIST)
- 论断:OMG MDA Guide 1.0.1(2003-06,omg/2003-06-01)的核心承诺:平台无关模型(PIM)包含足以驱动一个或多个平台特定模型(PSM)的信息,通过定义的变换由 PIM 映射到 PSM 并生成代码——即'模型为唯一事实源、代码可再生'的前代版本。
- 原文:A Platform Independent Model (PIM) is an abstract model which contains enough information to drive one or more Platform Specific Models (PSM).
- URL:https://www.omg.org/mda/
- 来源:OMG, 2003, MDA Guide Version 1.0.1 (omg/2003-06-01) · 2003-06 · 【厂商】 · T3 · 文档 · secondhand
- 备注:OMG 为标准联盟(成员含工具厂商),属利益相关方口径。未取得 OMG 原件(网络拦截),引文来自搜索摘要转述,需回一手。与 Tessl'spec-as-source'对照用。

## H28 (HIST)
- 论断:Kemerer 1992(IEEE Software)研究 I-CASE 工具采用,论证学习曲线导致组织购入后弃用;流行二手转述称其报告'工具引入一年后 70% 从未使用、25% 仅一个小组使用、5% 广泛使用但未充分'——该组数字本线未能在一手文本中定位。
- 原文:
- URL:https://doi.org/10.1109/52.136161
- 来源:Kemerer, C.F., 1992, How the Learning Curve Affects CASE Tool Adoption, IEEE Software 9(3):23-28 · 1992-05 · 【研究】 · mixed · 观察 · secondhand
- 备注:作者 PDF(sites.pitt.edu)被网络拦截。70/25/5 数字疑为 Kemerer 转引的行业调查,出处链未核 → 按'未验证'处理,不得承重。CASE 衰落只能作方向性背景。

## H29 (HIST)
- 论断:Binamungu 等 2018(SANER)调查 26 国 75 名 BDD 实践者:BDD 在受访者中活跃使用,但 20% 受访者所在组织强制使用、61% 作为可选工具;61% 认为规约中的重复会使其难以扩展和修改(可能导致功能'冻结');作者称从合作工程师处听到的轶事是维护挑战严重,'导致部分团队放弃该技术、回到面向技术的自动化测试'。BDD 规约面临与一般自动化测试套件相同的维护挑战。
- 原文:Anecdotal evidence from the software engineers we have worked with suggest that the maintenance challenges, in particular, can be severe, and are leading some teams to drop the technique and to return to technology-facing automated testing to play the role of their BDD specifications. ... 61% of the respondents held the view that the presence of duplication in BDD specifications can cause them to become difficult to extend and change (leading potentially to frozen functionality).
- URL:https://lepebina.github.io/maintaining.pdf
- 来源:Binamungu, L.P., Embury, S.M., Konstantinou, N., 2018, Maintaining Behaviour Driven Development Specifications: Challenges and Opportunities, SANER 2018 pp.175-184 · 2018-03 · 【研究】 · T4 · 调查 · verbatim-checked
- 备注:作者自托管 PDF(经 GitHub 仓库 lepebina/lepebina.github.io 取得)。便利+滚雪球抽样、BDD 社区渠道招募(偏向在用者);'放弃'仅为轶事,无比例。T4 可执行规约的'活性维护'成本证据。

## H30 (HIST)
- 论断:Cucumber 作者 Aslak Hellesøy(约 2014)称 Cucumber 是'世界上最被误解的协作工具':它首先是让团队跨角色建立共同理解的协作工具,而多数人把它当测试工具用,这种误用导致许多 Rails 团队弃用 Cucumber。
- 原文:
- URL:https://cucumber.io/blog/the-worlds-most-misunderstood-collaboration-tool
- 来源:Hellesøy, A., c.2014, The world's most misunderstood collaboration tool, Cucumber blog · 2014-03 · 【厂商】 · T4 · 评论 · secondhand
- 备注:cucumber.io 被拦截,仅见搜索摘要,无逐字引文。工具作者(后 Cucumber Ltd 创始人,2019 被 SmartBear 收购)自述,厂商口径。'弃用'是作者印象,无数据。

## H31 (HIST)
- 论断:Zampetti 等 2020(IST)分析约 50,000 个流行开源项目(5 种语言)中 BDD 框架使用,并考察 BDD 规约是否与源码共同演化;结论方向:BDD 框架采用不少,但常被用于单元测试等非 BDD 本意用途,开发者认为 BDD 仍很费力。
- 原文:
- URL:https://doi.org/10.1016/j.infsof.2020.106311
- 来源:Zampetti, F., Di Sorbo, A., Visaggio, C.A., Canfora, G., Di Penta, M., 2020, Demystifying the adoption of behavior-driven development in open source projects, IST 123:106311 · 2020-03 · 【研究】 · T4 · 观察 · secondhand
- 备注:全文未取得;仅搜索摘要。具体比例(多少项目用 BDD、共同演化程度)未核。二手资料对样本口径有矛盾(50,000 vs '20 个 Ruby 项目'),待验证。

## H32 (HIST)
- 论断:Nagappan 等 2008:微软 3 个团队 + IBM 1 个团队的 TDD 案例研究,相对同组织中未用 TDD 的类似项目,发布前缺陷密度下降 40%-90%(TDD 团队为对照的 0.61/0.38/0.24/0.09 倍);初始开发时间增加 15-35%,但该时间数字为'管理层估计'(主观)。
- 原文:The results of the case studies indicate that the pre-release defect density of the four products decreased between 40% and 90% relative to similar projects that did not use the TDD practice. Subjectively, the teams experienced a 15–35% increase in initial development time after adopting TDD.
- URL:https://github.com/tpn/pdfs (nagappan_tdd 2008 PDF, sha dd4bfc45…)
- 来源:Nagappan, N., Maximilien, E.M., Bhat, T., Williams, L., 2008, Realizing quality improvement through test driven development: results and experiences of four industrial teams, EMSE 13:289-302 · 2008-02 · 【研究】 · T4 · 案例 · verbatim-checked
- 备注:一手 PDF 已读。非随机、4 对比较;作者自承比较对象可能是遗留系统增强 vs 新项目、TDD 团队可能更有动力;作者为微软研究院/IBM 员工(研究自家团队)。是被引最多但设计最弱的 TDD 证据之一。

## H33 (HIST)
- 论断:TDD 元分析/综述方向:Rafique & Mišić 2013 对 27 项研究的元分析——TDD 对外部质量有小的正效应、对生产率几乎无可辨别效应,工业研究中质量提升与生产率下降均更大;Bissi 等 2016 系统综述(27 篇)——内部质量改进见于 76% 研究、外部质量 88%,生产率在学术情境上升、工业情境下降;Fucci 等 2017(39 名专业人员、82 个数据点)——质量与生产率主要与步长'粒度'和'均匀性'正相关,'测试与产品代码的书写顺序'无重要影响。
- 原文:TDD has a small positive effect on quality but little to no discernible effect on productivity ... Sequencing, the order in which test and production code are written, had no important influence.
- URL:https://doi.org/10.1109/TSE.2012.28 ; https://doi.org/10.1016/j.infsof.2016.02.004 ; https://arxiv.org/abs/1611.05994
- 来源:Rafique & Mišić 2013 IEEE TSE 39(6); Bissi, Serra Seca Neto, Emer 2016 IST 74:45-54; Fucci, Erdogmus, Turhan, Oivo, Juristo 2017 IEEE TSE 43(7) · 2013-06 · 【研究】 · T4 · 对照实验 · secondhand
- 备注:三篇一手均未能取得(IEEE/arXiv/Elsevier 被拦截)。两句引文分别在 ≥3 份独立文档中逐字一致;Bissi 的 76%/88% 为'报告改进的研究占比'(计票法,非效应量)。design 字段取主体(Rafique 汇总的多为对照实验);实际混合:Rafique 为元分析、Bissi 为系统综述(计票)、Fucci 为观察性过程数据。对 SDD 的可迁移含义:'先写规约'的'顺序'本身可能不是有效成分。

## H34 (HIST)
- 论断:Knuth 1984 提出文学编程:'让我们改变构造程序的传统态度:与其想象我们的主要任务是指示计算机做什么,不如集中精力向人类解释我们想让计算机做什么。'(以人可读的叙述为主、代码嵌入其中;WEB 系统)
- 原文:Let us change our traditional attitude to the construction of programs: Instead of imagining that our main task is to instruct a computer what to do, let us concentrate rather on explaining to human beings what we want a computer to do.
- URL:http://www.literateprogramming.com/knuthweb.pdf
- 来源:Knuth, D.E., 1984, Literate Programming, The Computer Journal 27(2):97-111 · 1984-?? · 【研究】 · T1 · 评论 · secondhand
- 备注:一手 PDF 被拦截;引文在 ≥5 份独立 GitHub 文档中逐字一致。本线未找到文学编程采用率的系统调查数据(未搜到)——不能说'失败'或'成功',只能说未成为主流实践;其后代 Jupyter 的叙述/代码比例另有研究(Rule 等 2018 CHI,约 1/4 笔记本无解释性文本,仅二手摘要,未入表)。


### 搜索角度
- Royce 1970 原文:praxisframework/usc/umd/washington.edu 镜像均被网络拦截 → 经 GitHub 仓库 tpn/pdfs 取得扫描 PDF(sha 9f7db065…),pdftotext + 400dpi 页面图像核对;交叉 tamnd/papers olmOCR 转录(同 sha)
- Royce 原文 'waterfall' 字样检索(PDF 文本层 + 转录,0 次)
- Royce '1500 vs 1000 页规约' 数字核对(页面图像残损,未决)
- Bossavit 对 Royce 的阅读工作表(Morendil/programming-history)与 IBM SSI gist(一手)
- Bossavit《Leprechauns of Software Engineering》本体(leanpub 被拦截,未读)
- Bell & Thayer 1976 原文(ACM/aminer/mosaicprojects 被拦截;两份独立转录)
- 'waterfall' 更早出处(未找到早于 1976 的印刷用例;未穷尽 TRW 内部报告、1975 年会议文献)
- Larman & Basili 2003(仅 c2 wiki 草稿存档)
- Benington 1956/1983 前言中的原型与批评(仅二手,未入表)
- DOD-STD-2167(1985)/ MIL-STD-498(1994)对瀑布制度化与后续松绑(仅二手博客,未入表)
- Brooks No Silver Bullet(tamnd/papers 转录 UNC TR86-020)
- Parnas & Clements 1986(GitHub 逐页抽取)
- Dijkstra EWD667(GitHub 转录)
- Boehm 1981 原书数据(未取得原书;经 Menzies 等重绘图和文献综述)
- Boehm & Basili 2001 Top-10 原文(umd.edu 被拦截;多份独立转录)
- Menzies et al. 2017 EMSE(作者 LaTeX 源 ai-se/phaseDelay)
- Shull et al. 2002 'What we have learned about fighting defects'(未取得原文)
- Hillel Wayne / The Register 2021 对 IBM SSI 的转述(二手,未入表)
- Petre 2013 ICSE 全文(pdfx 抽取)及 Petre 2014 SoSyM 跟进(未读)
- Hutchinson et al. 2011 ICSE 全文(pdfx)、Whittle et al. 2014 IEEE Software 全文(pdfx)、Hutchinson et al. 2014 SCP(未读)
- Mohagheghi et al. 2013 EMSE MDE 四案例(未读)
- OMG MDA Guide 2003(未取得原件)、Executable UML / xtUML(Mellor & Balcer 2002)采用数据(未搜到系统数据)
- Kemerer 1992 CASE 采用(PDF 被拦截;70/25/5 数字未定位)
- CASE 工具 1990 年代市场衰落的独立数据(未搜到)
- Binamungu et al. 2018 SANER 全文(作者 GitHub Pages 仓库)
- Zampetti et al. 2020 IST(全文未取得)、Chandorkar et al. 2022 Gherkin 普查(未读)
- Hellesøy 'misunderstood collaboration tool'(cucumber.io 被拦截)
- Cucumber 维护/资金现状:SmartBear 移交 Open Source Collective(仅搜索摘要,日期未核,未入表)
- Nagappan et al. 2008 全文(tpn/pdfs)
- Rafique & Mišić 2013、Bissi et al. 2016、Fucci et al. 2017、Karac & Turhan 2018(一手均被拦截,仅多源转述)
- Knuth 1984 文学编程原文(被拦截)及采用率调查(未搜到)
- Rule et al. 2018 CHI / Pimentel et al. 2019 MSR Jupyter 研究(仅搜索摘要,未入表)
- 网络约束:WebFetch 对 wikipedia/leanpub/arxiv/acm/ieee/umd 等全部 DNS 拦截;仅 GitHub(git clone + code search)与 WebSearch 摘要可用

### 交叉口径问题
- 'Royce 反对瀑布' vs 'Royce 认为基本方法健全':两句都在原文,成文须同时引用;Royce 的修正是加重前置设计/文档 + 一次试点,不是轻量迭代
- Royce 规约页数 1000 vs 1500:原件该位残损,不得单点引用
- 'waterfall 首次出现于 Bell & Thayer 1976' 是'已知最早'而非'创造';一手未读
- Boehm 100x:仅大型项目、运行阶段相对需求阶段、1970 年代数据;同图小项目约 4-5 倍;Boehm & Basili 2001 自限 'often' 与 '5:1';成本单位(工时 vs 费用)不明
- IBM SSI '1:6.5:15:60-100' 与 Boehm 曲线是两条不同出处链,不得合并
- Menzies 2017 '无 DIE' 的样本为 TSP 小项目(中位 46 天)且修复工时自记、有 SEI 利益关联;与 Boehm 大项目口径不重叠,不能当作'推翻 Boehm'
- Petre 35/50 是'个人声明的当前使用',非组织采用率;Whittle 450 人样本是 MDE 实践者(分母不含非使用者)
- MDE 生产率:文献宣称 +20%~+800%、比较研究 +35%~−27%、Whittle 定性归纳 20-30%——三种口径不得混引
- BDD '弃用' 仅为 Binamungu 轶事 + Hellesøy 印象,无比例数据;20%/61% 为受访组织强制/可选比例,非行业采用率
- TDD:Nagappan 缺陷密度为 pre-release、对照为非随机同组织项目,开发时间为管理层主观估计;Bissi 76%/88% 为计票占比非效应量;Rafique '小正效应' 为元分析效应方向
- Fucci 'test-first 顺序无重要影响' 若迁移到 SDD('spec 先行'),只能作类比假设,不是证据
- 历史类比的口径:Royce/Parnas/Brooks/Dijkstra 均为专家论述(评论),不是测量;不得与 PRO/CON/MEASURE 线的实验数据同级

# 线 VENDOR

## V01 (VENDOR)
- 论断:GitHub Spec Kit 在 2026-11-11 抓取时 GitHub 页面显示 149.2k stars、13.4k forks、741 watching。star/fork 是关注度指标,不是使用量、更不是效果;仓库无公开下载/活跃用户数据(npm/pypistats 本次不可达)。
- 原文:149.2k stars ... 13.4k forks ... 741 watching
- URL:https://github.com/github/spec-kit
- 来源:GitHub, 2026, github/spec-kit 仓库主页(WebFetch 抓取 2026-11-11) · 2026-11 · 【厂商】 · mixed · 观察 · paraphrase-checked
- 备注:数字经 WebFetch 小模型转述,GitHub API 本会话被拒(403)无法交叉核对;成文前需人工在页面复核。GitHub(微软)是 Copilot 卖方,Spec Kit 默认示例用 Copilot(README: 'This example uses GitHub Copilot')——工具中立叙事下的渠道受益。star 可被营销/热榜驱动,#14 教训:star≠采用≠效果。

## V02 (VENDOR)
- 论断:Spec Kit 由 GitHub 的 Den Delimarsky 于 2025-08-21 首次提交;仓库自述创始期 2025-08 至 2026-01,2026-01-22 起由 Manfred Riem 接任主维护者。1.0.0 版发布于 2026-08-21(一周年),截至 2026-11-10 为 1.4.0,CHANGELOG 共 245 个版本条目。
- 原文:Den authored the initial commit on August 21, 2025 and led the repository through its first months. ... Manfred Riem took over as lead maintainer on January 22, 2026.
- URL:https://github.com/github/spec-kit/blob/main/docs/overview/history.md
- 来源:github/spec-kit, 2026, docs/overview/history.md + CHANGELOG.md · 2026-11 · 【厂商】 · mixed · 文档 · verbatim-checked
- 备注:本地浅克隆 HEAD a959be7(2026-11-10)核对。迭代频率高(245 个版本/约 15 个月)说明维护活跃,但与'方法有效'无关。

## V03 (VENDOR)
- 论断:Spec Kit 早期 README(v0.0.17,2025-09-08)把自身定位为实验:'Experimental goals'一节列出要'验证假说'(SDD 不绑定特定技术栈)和'验证并行实现探索的概念'。当前 README(2026-11)已删除该节文字,仅保留锚点 -experimental-goals;叙事从'待验证假说'转为'产品化流程'(1.0)。厂商本身从未给出验证结果。
- 原文:## 🎯 Experimental goals

Our research and experimentation focus on: ... Validate the hypothesis that Spec-Driven Development is a process not tied to specific technologies, programming languages, or frameworks
- URL:https://github.com/github/spec-kit/blob/v0.0.17/README.md
- 来源:github/spec-kit, 2025-09, README.md @ v0.0.17 vs main @ a959be7 · 2025-09 · 【厂商】 · mixed · 文档 · verbatim-checked
- 备注:git fetch tag v0.0.17 本地 diff。验证阶段可用:'实验'框架何时、为何被移除,是否发布过任何实验结论(未找到)。

## V04 (VENDOR)
- 论断:Spec Kit 方法论文档 spec-driven.md 宣称'权力反转':spec 成为源,代码为其表达;并称 SDD '消除' spec 与实现之间的鸿沟。属规范性主张(T1/T2 为源、代码再生),无任何测量支撑。
- 原文:Spec-Driven Development (SDD) inverts this power structure. Specifications don't serve code—code serves specifications. ... SDD eliminates the gap by making specifications and their concrete implementation plans born from the specification executable. When specifications and implementation plans generate code, there is no gap—only transformation.
- URL:https://github.com/github/spec-kit/blob/main/spec-driven.md
- 来源:github/spec-kit, 2025–2026, spec-driven.md 'The Power Inversion' · 2026-11 · 【厂商】 · T1 · 评论 · verbatim-checked
- 备注:对应核心问题主张 3(spec 为唯一事实源)。'there is no gap' 为绝对化措辞,可与 FORMAL 线(陈述≠意图)对撞。

## V05 (VENDOR)
- 论断:spec-driven.md 唯一的量化对比是一个虚构示例:传统做法文档工作'约 12 小时'(PRD 2-3h、设计 2-3h、结构 30min、技术规格 3-4h、测试计划 2h)vs SDD 三条命令各'5 分钟'、'15 分钟'得到完整 spec/plan/tasks。无样本、无测量、无质量对照,只计生成时间不计审阅时间。
- 原文:Total: ~12 hours of documentation work ... # Step 1: Create the feature specification (5 minutes) ... In 15 minutes, you have: - A complete feature specification with user stories and acceptance criteria
- URL:https://github.com/github/spec-kit/blob/main/spec-driven.md
- 来源:github/spec-kit, spec-driven.md 'Example: Building a Chat Feature' · 2026-11 · 【厂商】 · T2 · 案例 · verbatim-checked
- 备注:口径陷阱:'生成文档墙钟'≠'交付墙钟'≠'质量';审阅大段生成 markdown 的成本(Böckeler、Thoughtworks 都指出)完全未计。不得作为效率证据引用,只能作为'厂商叙事样本'。

## V06 (VENDOR)
- 论断:spec-driven.md 宣称'Living Documentation:spec 与代码保持同步,因为是 spec 生成了代码'——这是主张 2(spec 不漂移)的厂商版本,以机制断言代替测量。
- 原文:3. **Living Documentation**: Specifications stay in sync with code because they generate it
- URL:https://github.com/github/spec-kit/blob/main/spec-driven.md
- 来源:github/spec-kit, spec-driven.md 'The Power of Structured Automation' · 2026-11 · 【厂商】 · T1 · 评论 · verbatim-checked
- 备注:与下一条(Spec Kit 自己的 specs/ 不入库)形成内部张力;需 MEASURE 线漂移率数据对撞。

## V07 (VENDOR)
- 论断:Spec Kit 自家仓库的 dogfooding:CONTRIBUTING 称'用 Spec Kit 开发 Spec Kit',但同时说明并非每个变更都走完整流程,且 dogfooding 产物(.specify/、specs/ 等)被刻意 gitignore、不进入仓库历史。即最主要的 SDD 工具自身并未把 spec 作为长期维护的事实源(spec-first,而非 spec-anchored/spec-as-source)。
- 原文:This does not mean every change goes through the full workflow. Small fixes can use the normal issue, pull request, review, and test process. Dogfooding scaffolding and artifacts under `.github/agents/`, `.github/prompts/`, `.github/copilot-instructions.md`, `.grok/`, `.specify/`, and `specs/` are intentionally gitignored.
- URL:https://github.com/github/spec-kit/blob/main/CONTRIBUTING.md
- 来源:github/spec-kit, 2026, CONTRIBUTING.md 'Does Spec Kit use Spec Kit?' · 2026-11 · 【厂商】 · T1 · 文档 · verbatim-checked
- 备注:强证据(厂商自述的反向事实)。.gitignore 第 61-62 行确有 '.specify/' 'specs/';仓库中仅留 .specify/memory/constitution.md。对照:OpenSpec 自身仓库提交 openspec/specs 44 个、archive 108 个变更。

## V08 (VENDOR)
- 论断:Spec Kit 当前已从单一 SDD 流程扩展为'agent harness':官方目录 43 个 agent integrations、核心 extensions 5 个 + 社区 extensions 197 个、presets 2 + 社区 42 个;README 主动声明目录条目不是审计或背书。
- 原文:Catalog listings are not audits or endorsements, so review community source code before installing or running it.
- URL:https://github.com/github/spec-kit
- 来源:github/spec-kit, 2026-11, README.md + integrations/extensions/presets catalog.json · 2026-11 · 【厂商】 · mixed · 文档 · verbatim-checked
- 备注:计数由本地 JSON 解析得出(HEAD a959be7)。扩展数是生态热度指标,非采用数据;产品范围扩张(bug fixing、idea assessment)也意味着'SDD'在 Spec Kit 内已是可选入口之一。

## V09 (VENDOR)
- 论断:Spec Kit 宪法模板(spec-driven.md)规定'九条开发条款',包括 Library-First、CLI 接口强制、Test-First(不可协商)、Simplicity/Anti-Abstraction/Integration-First 门禁;其中 IV–VI 留给项目自定义。即 Spec Kit 把 T4(测试先行)嵌入流程,但这些门禁由 LLM 自评执行。
- 原文:Articles IV, V, and VI are intentionally defined by each project's constitution rather than prescribed by Spec Kit.
- URL:https://github.com/github/spec-kit/blob/main/spec-driven.md
- 来源:github/spec-kit, spec-driven.md 'The Nine Articles of Development' · 2026-11 · 【厂商】 · mixed · 文档 · verbatim-checked
- 备注:'/speckit.analyze' 合规检查由 agent 完成,非确定性校验;验证者可追问门禁是否有任何遵从率数据(未找到)。

## V10 (VENDOR)
- 论断:GitHub 官方博客发布文(Den Delimarsky,2025-09-02)把转变表述为从'代码是事实源'到'意图是事实源',并称支持 Copilot、Claude Code、Gemini CLI。
- 原文:
- URL:https://github.blog/ai-and-ml/generative-ai/spec-driven-development-with-ai-get-started-with-a-new-open-source-toolkit/
- 来源:Den Delimarsky, 2025-09-02, Spec-driven development with AI: Get started with a new open source toolkit, The GitHub Blog · 2025-09 · 【厂商】 · T1 · 评论 · secondhand
- 备注:github.blog 本会话网络不可达;仅有搜索摘要文本:"We're moving from 'code is the source of truth' to 'intent is the source of truth.'"——成文前须回原页逐字核对。作者为 GitHub PM,利益相关。

## V11 (VENDOR)
- 论断:OpenSpec(Fission-AI)在 2026-11-11 抓取时显示 74.6k stars、5.1k forks;npm 包 @fission-ai/openspec 当前 1.17.0。README 自称'The most loved spec framework'。
- 原文:<summary><strong>The most loved spec framework.</strong></summary>
- URL:https://github.com/Fission-AI/OpenSpec
- 来源:Fission-AI, 2026, OpenSpec README + GitHub 仓库页 · 2026-11 · 【厂商】 · T1 · 观察 · paraphrase-checked
- 备注:'most loved' 自封,无数据。star 数经 WebFetch 转述未交叉核对。npm 下载量页面 403、api.npmjs.org 被代理拒,未取得。

## V12 (VENDOR)
- 论断:OpenSpec 的'How we compare'把 Spec Kit 定性为'彻底但笨重'(刚性阶段门、大量 markdown、Python 安装),把 Kiro 定性为'锁定 IDE 且仅限 Claude 模型';这是竞品自述,不是独立评测。
- 原文:**vs. [Spec Kit](https://github.com/github/spec-kit)** (GitHub) — Thorough but heavyweight. Rigid phase gates, lots of Markdown, Python setup. OpenSpec is lighter and lets you iterate freely.

**vs. [Kiro](https://kiro.dev)** (AWS) — Powerful but you're locked into their IDE and limited to Claude models.
- URL:https://github.com/Fission-AI/OpenSpec/blob/main/README.md
- 来源:Fission-AI, 2026, OpenSpec README 'How we compare' · 2026-11 · 【厂商】 · T1 · 评论 · verbatim-checked
- 备注:'limited to Claude models' 已过时:Kiro 2026 年已提供 GPT-5.6 等多模型(第三方追踪,secondhand)。竞品互评可作'流程税'定性线索,不可作证据。

## V13 (VENDOR)
- 论断:OpenSpec 的定位是'brownfield/迭代、非瀑布'(spec-anchored:changes 提案→归档合并入 specs),并且自身仓库确实 dogfood:openspec/specs 下 44 个 spec、changes/archive 下 108 个已归档变更(最早目录名 2025-01-11,最新 2026-10-19)。
- 原文:→ fluid not rigid
→ iterative not waterfall
→ easy not complex
→ built for brownfield not just greenfield
- URL:https://github.com/Fission-AI/OpenSpec
- 来源:Fission-AI, 2026, OpenSpec README + openspec/ 目录(本地克隆 f29319d) · 2026-11 · 【厂商】 · T1 · 观察 · verbatim-checked
- 备注:归档目录日期前缀 2025-01-11 早于 OpenSpec 公开时间,可能是回填命名,不宜据此推断项目起始。dogfood 计数是可复跑的唯一'spec 保持活性'厂商侧观测,样本 n=1 仓库。

## V14 (VENDOR)
- 论断:OpenSpec 默认开启匿名遥测(仅命令名与版本),因此厂商掌握真实使用数据,但未公开发布。
- 原文:OpenSpec collects anonymous usage stats.

We collect only command names and version to understand usage patterns. No arguments, paths, content, or PII. Automatically disabled in CI.
- URL:https://github.com/Fission-AI/OpenSpec/blob/main/README.md
- 来源:Fission-AI, 2026, OpenSpec README 'Telemetry' · 2026-11 · 【厂商】 · n/a · 文档 · verbatim-checked
- 备注:'采用'数据存在但不可得;可作为可观测信号:若厂商发布命令分布(propose vs archive 比率),可直接测 spec 是否被持续维护。

## V15 (VENDOR)
- 论断:BMAD Method(BMad Code, LLC)在 2026-11-11 显示 55.2k stars、6.2k forks;稳定版 v6.12,v7 处于 preview alpha,README 称 v7 预计 2026 年 11 月中发布。名称'Breakthrough Method for Agile Ai Driven Development',为商标;自称永久免费,接受企业赞助。
- 原文:BMad is free for everyone and always will be. Star the repository, [buy me a coffee](https://buymeacoffee.com/bmad), or email <contact@bmadcode.com> for corporate sponsorship.
- URL:https://github.com/bmad-code-org/BMAD-METHOD
- 来源:BMad Code LLC, 2026, BMAD-METHOD README + TRADEMARK.md · 2026-11 · 【厂商】 · mixed · 文档 · paraphrase-checked
- 备注:star/fork 数经 WebFetch 转述;README 与 TRADEMARK 文本本地逐字核对。利益:商标持有公司 + 赞助/社区变现;README 呼吁 'Star the repository' 本身说明 star 受号召驱动。

## V16 (VENDOR)
- 论断:BMAD 的自我定位是'不放弃思考'的敏捷 AI 驱动开发,流程'按工作规模自适应':小改直接进 build,复杂工作才走深度规划——即厂商自己承认全量 spec 流程对小任务不划算。
- 原文:Small changes go straight to build. Complex work gets the depth it needs.
- URL:https://github.com/bmad-code-org/BMAD-METHOD/blob/main/README.md
- 来源:BMad Code LLC, 2026, BMAD-METHOD README · 2026-11 · 【厂商】 · mixed · 文档 · verbatim-checked
- 备注:与 Claude Code 文档'能一句话描述 diff 就跳过计划'、Thoughtworks'工具在不同任务规模表现差异大'同向:厂商侧对'流程税'的隐性承认。

## V17 (VENDOR)
- 论断:AWS Kiro 于 2025-07-14 以 preview 发布,定位'从 vibe coding 到生产':以 specs(requirements→design→tasks)和 agent hooks 为卖点;2025-11-17 GA,GA 新增 property-based testing(从 spec 抽取性质测代码)、checkpoint、CLI、团队管理。
- 原文:
- URL:https://kiro.dev/blog/introducing-kiro/
- 来源:Kiro team (AWS), 2025-07-14, Introducing Kiro;及 2025-11, Kiro is generally available · 2025-07 · 【厂商】 · T1 · 文档 · secondhand
- 备注:kiro.dev 本会话不可达;日期来自 AWS 日本博客与多家媒体一致报道。搜索摘要中 GA 文措辞:'While PBTs are not verification or proof, they provide evidence for correctness'——厂商自己限定 PBT 不是证明,成文需原页核对。

## V18 (VENDOR)
- 论断:Kiro 用量口径(AWS 自述):preview 第一周'超过 10 万开发者使用',前三个月'超过 25 万开发者',preview 期间'超过 3 亿次请求'。均为公司自报、未审计,'使用过'≠活跃≠付费≠用了 spec 模式。
- 原文:
- URL:https://www.geekwire.com/2025/amazons-surprise-indie-hit-kiro-launches-broadly-in-bid-to-reshape-ai-powered-software-development/
- 来源:GeekWire, 2025-11, Amazon's surprise indie hit Kiro launches broadly(转述 AWS 数据) · 2025-11 · 【媒体】 · n/a · 观察 · secondhand
- 备注:未能在 kiro.dev 原文定位 250,000;TheNewStack 写'nearly 300 million'、GeekWire 写'more than 300 million'请求,口径不一。关键:没有 spec 模式 vs vibe 模式的使用占比——这是 SDD 采用的真正口径,厂商未披露。

## V19 (VENDOR)
- 论断:Kiro 定价变迁(计费单位本身就是 SDD 成本的信号):2025-07 预告 Free 50 次/Pro $19 1,000 次/Pro+ $39 3,000 次'交互';2025-08 改为分开计 'spec requests' 与 'vibe requests'(Pro $20:225 vibe + 125 spec;Power $200:2,250 vibe + 1,250 spec),引发'钱包毁灭'舆论,Kiro 承认计量 bug 并重置额度/退款;2025-09 再改为统一 credits(Pro $20=1,000 credits,超额 $0.04/credit)。
- 原文:
- URL:https://www.theregister.com/2025/08/18/aws_updated_kiro_pricing/
- 来源:The Register, 2025-08-18, AWS pricing for Kiro dev tool dubbed 'a wallet-wrecking tragedy';Kiro blog 'Important Kiro pricing updates';Kiro blog 'Announcing new pricing plans and Auto' · 2025-08 · 【媒体】 · T2 · 文档 · secondhand
- 备注:kiro.dev 不可达,数字来自搜索摘要(Register/InfoWorld/Kilo Code 博客,Kilo 为竞品)。口径要点:spec request 单独定价且约为 vibe 的 ~1.8 倍稀缺(125 vs 225),说明 spec 驱动任务的推理成本更高——这是'流程税'的厂商侧间接证据,但比例由定价策略决定,不等于 token 成本。需回原页核对。

## V20 (VENDOR)
- 论断:Kiro 2026 年定价据第三方追踪继续变动:2026-06 新增 Pro Max($100/5,000 credits),2026-07 个人计划以预付 add-on($0.04/credit)替代超额计费,模型倍率多次调整(GPT-5.6 Terra/Luna 等),2026-11-01 起以免费 Pro 月 + 500 试用 credits 替代首次升级 $20 抵扣。
- 原文:
- URL:https://www.usagepricing.com/blueprint/kiro
- 来源:usagepricing.com / dev.classmethod.jp / aws.amazon.com/jp/blogs/news/kiro-pro-max, 2026 · 2026-11 · 【媒体】 · n/a · 文档 · secondhand
- 备注:来源互相矛盾(Luna 倍率历史);只有 AWS 日本博客 Pro Max 文为官方但未能打开。成文只能说'定价单位与倍率在 16 个月内多次改动',不得引具体倍率。

## V21 (VENDOR)
- 论断:AWS 官方案例(PKFARE)宣称:借助 Kiro 的 spec 驱动方法,原型验证周期'从数月压缩到数天',测试用例编写与执行'从 3 天降到半天',测试/开发团队在 5 周内交付一个票务系统。厂商案例,无对照、无基线定义。
- 原文:
- URL:https://aws.amazon.com/solutions/case-studies/pkfare/
- 来源:AWS, 2026, PKFARE case study · 2026 · 【厂商】 · T1 · 案例 · secondhand
- 备注:aws.amazon.com 不可达,仅搜索摘要。客户案例由卖方挑选发布,幸存者偏差;'months to days'无基线。另有 TheNewStack 转述 Socure Scala→Go 迁移'估计 3 周、实际 2 天'——估计值作基线,非实测对照。

## V22 (VENDOR)
- 论断:Tessl(创始人 Guy Podjarny,前 Snyk 创始人)2024-11-14 宣布累计融资 1.25 亿美元:2024-04 种子轮 2,500 万(boldstart、GV 领投)+ A 轮 1 亿(Index Ventures 领投,Accel 参投);估值公司未披露,TechCrunch 标题称'$500M+',文内更新及其他媒体称投后约 7.5 亿美元。当时称平台'2025 年初上线'。
- 原文:
- URL:https://techcrunch.com/2024/11/14/tessl-raises-125m-at-at-500m-valuation-to-build-ai-that-writes-and-maintains-code/
- 来源:TechCrunch, 2024-11-14, Tessl raises $125M at $500M+ valuation;Tessl blog 'Announcing Our Series A' · 2024-11 · 【媒体】 · T1 · 文档 · secondhand
- 备注:techcrunch/tessl.io 不可达,仅搜索摘要。估值两个口径(500M+ vs 750M)不得混引;融资额是资本押注,不是方法有效性证据。'早 2025 上线'实际拖到 2025-09(registry open beta)。

## V23 (VENDOR)
- 论断:Tessl 2025-09-16 发布两款产品:Spec Registry(open beta,宣称'10,000+ 预置 spec',帮助 agent 正确使用开源库、避免 API 幻觉/版本混淆)和 Tessl Framework(closed beta,需申请)。spec-as-source 的代码再生引擎从未 GA。
- 原文:
- URL:https://tessl.io/blog/tessl-launches-spec-driven-framework-and-registry/
- 来源:Tessl, 2025-09, Tessl launches spec-driven framework and registry;Guy Podjarny, announcing tessl's products · 2025-09 · 【厂商】 · T1 · 文档 · secondhand
- 备注:tessl.io 不可达。'10,000+ specs' 实为库用法文档(更接近 llms.txt/T1 上下文),不是应用级 spec-as-source;两者不得混为'spec 采用'。

## V24 (VENDOR)
- 论断:Tessl 2026-01-29 起重新定位为'agent skills 的包管理器'/'Agent Enablement Platform',registry 转为 skills registry(第三方称 2026-06 列有 3,000+ skills;2026-03 与 Snyk 合作给每个公开 skill 打安全分);spec-as-source 只以社区 tile 形式存在于 registry。即 spec-as-source 最激进的旗手在产品层面转向。
- 原文:
- URL:https://codemyspec.com/blog/tessl-review
- 来源:CodeMySpec, 2026, Tessl Review (2026): The Spec-as-Source Bet;rywalker.com/research/tessl;issoh.co.jp · 2026-06 · 【媒体】 · T1 · 评论 · secondhand
- 备注:全部为二手(tessl.io 不可达),需回 Tessl 官方博客核对日期与措辞。评审者称再生引擎'closed beta, JavaScript-only, 1:1 spec-to-file, demonstrably non-deterministic'——单一评论者,方向参考。对核心主张 3 是重要的'可观测信号':厂商自身的产品重心偏离 spec-as-source。

## V25 (VENDOR)
- 论断:Podjarny 的预测:到 2027 年底,与 agent 协作的开发者大多数时间不再看代码。属点预测,无区间、无情景,发言者为 spec-as-source 公司 CEO。
- 原文:
- URL:https://zuplo.com/blog/spec-driven-ai-development
- 来源:Zuplo, 2025, Spec-driven AI development(访谈 Guy Podjarny 转述) · 2025 · 【媒体】 · T1 · 评论 · secondhand
- 备注:红线:单点预测不得作为论据承重,只可作为'利益相关方预期'引用并标注发言者利益。原话未回一手。

## V26 (VENDOR)
- 论断:'specs are the new code' 的逐字出处核查:Sean Grove(OpenAI)在 AI Engineer World's Fair 2025(旧金山,2025-06)演讲,YouTube 标题'The New Code — Sean Grove, OpenAI'(ID 8rABwKRsec4,约 21 分钟),活动页标题'The New Code: Specifications as the Source of Truth'(URL slug 为 specifications-are-the-new-code)。在可得转录中他没有逐字说'specs are the new code';最接近的是开场 [00:00:43]'the coming of the new code, in particular specifications'。口号是标题/媒体压缩,不是原话。
- 原文:[00:00:43.840 --> 00:00:46.880]   to talk about what I see is the coming of the new code,
[00:00:46.880 --> 00:00:50.560]   in particular specifications, which sort of hold this promise.
- URL:https://www.youtube.com/watch?v=8rABwKRsec4
- 来源:Sean Grove (OpenAI), 2025, The New Code, AI Engineer World's Fair 2025;转录:github.com/lawwu/transcripts data/transcripts/8rABwKRsec4.txt · 2025-06 · 【厂商】 · T1 · 评论 · paraphrase-checked
- 备注:转录为第三方 Whisper 自动转录(首行即幻觉文本 'Leipzig Reviewer: Peter van de Ven',结尾有重复'Thank you'),时间戳以视频开头为零点,可能与 YouTube 有数秒偏差;YouTube/ai.engineer 本会话不可达,未能对官方字幕。成文引用须标'据自动转录,时间戳近似'。Grove 时任 OpenAI 对齐团队,'spec'语境主要是 OpenAI Model Spec(模型行为规约),不是应用开发 PRD——被 SDD 厂商借用时发生语境迁移。

## V27 (VENDOR)
- 论断:Grove 的核心量化说法'代码只占你所创造价值的 10%–20%,另外 80%–90% 在结构化沟通'是无出处的修辞断言,演讲中未给任何数据来源。
- 原文:[00:02:44.640 --> 00:02:48.560]   Code is sort of 10% to 20% of the value that you bring.
[00:02:48.560 --> 00:02:53.280]   The other 80% to 90% is in structured communication.
- URL:https://www.youtube.com/watch?v=8rABwKRsec4
- 来源:Sean Grove (OpenAI), 2025, The New Code(Whisper 转录 lawwu/transcripts) · 2025-06 · 【厂商】 · n/a · 评论 · verbatim-checked
- 备注:逐字核对的是转录文本,非官方字幕;'sort of' 限定语必须保留。不得作为'开发者时间分配'的数据引用。

## V28 (VENDOR)
- 论断:Grove 的类比:我们保留生成的代码、删掉 prompt,'像是把源码粉碎、却小心地对二进制做版本控制';并称代码是 spec 的'有损投影';结尾号召'让 spec 可执行:把 spec 喂给模型,并对照 spec 测试'。
- 原文:[00:05:57.760 --> 00:06:03.200]   And this feels like a little bit like you shred the source and then you very carefully version control the binary. ... [00:06:55.920 --> 00:07:00.640]   Because code itself is actually a lossy projection from the specification. ... [00:20:08.120 --> 00:20:18.120]   Make the spec executable. Feed the spec to the model, and test against the spec.
- URL:https://www.youtube.com/watch?v=8rABwKRsec4
- 来源:Sean Grove (OpenAI), 2025, The New Code(Whisper 转录) · 2025-06 · 【厂商】 · T4 · 评论 · verbatim-checked
- 备注:'test against the spec' 指向 T4(可执行规约/评测),这比'markdown spec 即源'弱得多也可检验得多;HIST 线可对照编译器类比的缺陷(LLM 非确定性 ≠ 编译器)。

## V29 (VENDOR)
- 论断:Claude Code(Anthropic)的 plan mode 从 1.0.x 时期即存在,CHANGELOG 记录了后续演进:Opus 仅用于 plan 的 'opusplan'、Plan 子代理、'在 plan mode 中更频繁地向你提问'、'Plan Mode now builds more precise plans and executes more thoroughly',以及修复'上下文压缩后丢失 plan mode、模型从计划切到实现'的 bug。全部是功能描述,无效果测量。
- 原文:- Plan Mode now builds more precise plans and executes more thoroughly
- URL:https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md
- 来源:Anthropic, 2025–2026, claude-code CHANGELOG.md(本地克隆,最新 2.1.322) · 2026-11 · 【厂商】 · T2 · 文档 · verbatim-checked
- 备注:利益冲突:本研究使用的工具厂商即 Anthropic,需在成文中披露。'more precise/more thoroughly' 无基准。

## V30 (VENDOR)
- 论断:Claude Code 官方最佳实践文档给计划设定边界:计划在方案不确定、改动多文件或不熟悉代码时最有用;'如果能用一句话描述 diff,就跳过计划'。厂商自己承认 T2 计划对小任务是净成本。
- 原文:
- URL:https://code.claude.com/docs/en/best-practices
- 来源:Anthropic, 2026, Claude Code docs: Best practices · 2026 · 【厂商】 · T2 · 文档 · secondhand
- 备注:code.claude.com 未直接抓取;搜索摘要文本:'If you could describe the diff in one sentence, skip the plan.' 'Planning is most useful when you're uncertain about the approach, when the change modifies multiple files, or when you're unfamiliar with the code being modified.' 需原页核对。

## V31 (VENDOR)
- 论断:Cursor 1.7(2025-10)引入 Plan Mode,宣称先起草具体计划'使 agent 能运行更长时间';计划可选保存为仓库内 markdown;2.1 增加规划时的澄清提问。VS Code 1.105(2025-10-09)在 Insiders 引入内置 Plan agent,GitHub 2025-10-28 changelog 称其'在编码前检查需求覆盖'。均为厂商功能描述。
- 原文:
- URL:https://cursor.com/blog/plan-mode
- 来源:Cursor, 2025-10, Introducing Plan Mode / changelog 1.7, 2.1;Microsoft, 2025-10-09, VS Code 1.105 release notes;GitHub changelog 2025-10-28 · 2025-10 · 【厂商】 · T2 · 文档 · secondhand
- 备注:cursor.com/code.visualstudio.com/github.blog 不可达,全部来自搜索摘要。'run much longer' 是运行时长,不是质量——口径不得互换。plan mode 普及说明 T2 已被主流工具吸收为可选模式,与'SDD 方法论'(T1 为源)是两回事。

## V32 (VENDOR)
- 论断:Augment Code 于 2026-02 公测 Intent:Coordinator 起草'living spec'、分派实现/验证 agent,宣称 spec 随 agent 完成任务'自动更新'。厂商营销页与对比页为主要来源,无独立测量。
- 原文:
- URL:https://augmentcode.com/blog/intent-a-workspace-for-agent-orchestration
- 来源:Augment Code, 2026-02, Intent: a workspace for agent orchestration · 2026-02 · 【厂商】 · T1 · 文档 · secondhand
- 备注:augmentcode.com 不可达;Augment 同时运营大量'X vs Intent'SEO 对比页与 SDD 指南页(如 'what-is-spec-driven-development'),搜索结果被厂商内容污染,验证时须剔除。'自动更新 spec'是对主张 2 的机制断言。

## V33 (VENDOR)
- 论断:Thoughtworks Technology Radar Vol.33(2025-11-05)把 spec-driven development 列入 Techniques 的 Assess 环(非 Trial/Adopt),blip 提到 Kiro、spec-kit、Tessl,并警告部分工具生成冗长难审的 spec 文件、可能重学'手工为 AI 编写详细规则不可扩展'的苦涩教训。Vol.34(2026-04-15)将 GitHub Spec Kit 列入 Languages & Frameworks 的 Assess,称团队主要在 brownfield 中试用、具备良好整洁代码与架构实践的资深工程师获益最多。
- 原文:
- URL:https://www.thoughtworks.com/radar/techniques/spec-driven-development
- 来源:Thoughtworks, 2025-11, Technology Radar Vol.33 'Spec-driven development' (Assess);2026-04, Vol.34 'GitHub Spec Kit' (Assess) · 2025-11 · 【官方】 · mixed · 评论 · secondhand
- 备注:thoughtworks.com(含 PDF)不可达,仅搜索摘要。Thoughtworks 为咨询公司,Böckeler 同属该公司(与 CON 线评测非独立)。Radar 环位是专家判断,非测量。'waterfall'一词未在 blip 中找到(来自播客与 Scott Logic 标题)。

## V34 (VENDOR)
- 论断:据二手报道,Radar Vol.35(2026 秋)将 OpenSpec 从 Assess 移至 Trial('多个团队报告成功……与裸 prompt 相比 agent 输出更可预测、意外改动更少');Spec Kit 仍在 Assess;另设'AI-driven documentation sprawl'警示条目。SDD 技术条目本身在当前版的环位未能确认(一条搜索称该 blip 'not on the current edition')。
- 原文:
- URL:https://www.thoughtworks.com/radar/tools/openspec
- 来源:Thoughtworks, 2026, Technology Radar 'OpenSpec' blip;onext.es 'Thoughtworks Radar 35' 解读 · 2026-10 · 【官方】 · T1 · 评论 · secondhand
- 备注:搜索结果互相矛盾(一次称 Vol.35 存在且 OpenSpec 升 Trial,另一次称最新为 Vol.34)。'more predictable / fewer unintended changes' 是团队主观报告,非测量。成文前必须回 thoughtworks.com 核对卷号、日期、环位。


### 搜索角度
- GitHub API(gh/curl)取 star/fork/创建时间:本会话 403 被拒;改用 WebFetch github.com 仓库页(小模型转述)
- git 浅克隆 github/spec-kit、Fission-AI/OpenSpec、bmad-code-org/BMAD-METHOD、anthropics/claude-code 本地逐字核对 README/CHANGELOG/spec-driven.md/CONTRIBUTING/.gitignore
- spec-kit 早期 tag v0.0.17(2025-09-08)README 与当前 README 对比('Experimental goals' 删除)
- spec-kit/OpenSpec/BMAD 自身仓库是否 dogfood spec(specs 目录是否入库、数量)
- npm 下载量(api.npmjs.org、npmjs.com 页面)与 pypistats(specify-cli):均被代理/站点 403,未取得——采用量口径缺失
- Sean Grove 'The New Code' 官方视频/ai.engineer 转录:youtube.com、ai.engineer 不可达;改用 github.com/lawwu/transcripts 的 Whisper 转录逐字 grep
- 'specs are the new code' 逐字短语出处搜索:转录中无此逐字句;仅见活动页 slug 与媒体标题;另有 Jesse Vincent 口头说法(二手博客)
- Kiro 官方博客(launch/pricing/GA/one-year)与定价页:kiro.dev 不可达,仅搜索摘要
- Kiro 用户数(100k 首周 / 250k 三个月 / 300M 请求):只在媒体转述中找到,未在 kiro.dev 原文定位
- Kiro spec 模式 vs vibe 模式使用占比:未找到任何披露
- AWS 官方案例(PKFARE、Socure):aws.amazon.com 不可达,仅摘要
- Tessl 融资(TechCrunch/Fortune/City AM)、产品发布(2025-09)、2026 skills 转向:tessl.io/techcrunch 不可达,仅摘要
- Podjarny 是否提出 spec-first/spec-anchored/spec-as-source 三分法:搜索指向 Böckeler(CON 线)而非 Podjarny,未确认
- Cursor plan mode(1.7/2.1)、VS Code Plan agent(1.105/1.106)、GitHub changelog:站点不可达,仅摘要
- Claude Code CHANGELOG(本地)+ 官方 best practices 文档(摘要)
- Augment Intent:仅厂商页摘要,搜索结果大量为 Augment SEO 对比页
- Thoughtworks Radar Vol.33/34/35 环位:thoughtworks.com 与 PDF 不可达;Vol.35 是否存在/SDD 条目当前环位搜索结果矛盾
- GitHub 博客发布文(Delimarsky 2025-09-02)逐字:github.blog 不可达,仅摘要
- 未搜:厂商公开的任何对照实验/效果数据——在 Spec Kit、OpenSpec、BMAD、Kiro、Tessl 的一手材料中均未发现自测效果数字(除 Kiro 客户案例)

### 交叉口径问题
- star/fork(Spec Kit 149.2k、OpenSpec 74.6k、BMAD 55.2k)≠ 安装量 ≠ 活跃使用 ≠ 走完 spec 流程 ≠ 效果;本线未取得任何下载量数据
- Kiro '250k 开发者使用'是'用过 Kiro'口径,不是'用过 spec 模式';无 spec/vibe 占比
- Kiro spec request vs vibe request 的定价比是定价策略口径,不是 token/墙钟成本口径
- spec-driven.md '12 小时 vs 15 分钟'只计文档生成墙钟,不计审阅、不计质量,且为虚构示例
- Tessl 估值 $500M+(TechCrunch 标题)vs $750M(文内更新/其他媒体),公司未披露——不得混引
- Tessl '10,000+ specs' 是库用法文档(上下文注入),不是应用级 spec-as-source;不能当 SDD 采用证据
- Grove 演讲中 'spec' 主要指 OpenAI Model Spec(模型行为规约 + 评测),被 SDD 厂商移用到应用 PRD/plan 语境;T1/T4 语境迁移
- 'specs are the new code' 非逐字原话,应写作'Grove 演讲标题 The New Code,活动页标题 Specifications as the Source of Truth'
- Grove '10–20% / 80–90%' 为修辞,不是测量
- 厂商对'活性'的主张(Spec Kit 'stay in sync because they generate it'、Augment 'auto-update')与 Spec Kit 自家 specs/ 被 gitignore 的事实冲突
- plan mode(T2,工具内可选模式)与 SDD 方法论(T1 为源、spec-anchored/as-source)是不同对象,采用数据不得互证
- Thoughtworks 与 Böckeler 同属一家公司:Radar 判断与 martinfowler.com 评测不是两个独立来源
- Cursor 'agent 运行更久' = 运行时长口径,不是质量口径
- Kiro 案例 'months to days' / '3 weeks to 2 days' 以估计值为基线,非对照

# 线 MEASURE

## M01 (MEASURE)
- 论断:Uvik SDD benchmark 设计:同一组 50 张生产 Python 工单,5 臂(GitHub Spec Kit / AWS Kiro / BMAD Method / OpenSpec / 无 spec 对照),合并与否由人工评审决定(检索摘要称盲审);页面标注「Last updated: October 8, 2026」,另有检索摘要称 2026-10-15
- 原文:[转引] "Last updated: October 8, 2026", 50 Python tickets, human review
- URL:https://uvik.net/blog/spec-driven-development-benchmark/
- 来源:Uvik Software, 2026, Spec-Driven Development Benchmark 2026 (Q4 2026 run), uvik.net blog · 2026-10 · 【厂商】 · mixed · 基准 · secondhand
- 备注:uvik.net 在本会话被网络策略拦截(WebFetch DNS 拒绝、curl CONNECT 403),全文未读;设计要素来自 经 FreekMencke/claude-kb PR #327 topics/kb-spec-driven.md SDD-008(2026-10-30 核)逐字转录 与多次检索摘要。工单来源(客户项目?)、选样程序、ticket 类型分布均未能核实。日期两说(10-08 vs 10-15)待回一手。

## M02 (MEASURE)
- 论断:Uvik 合并率(n=50/臂):Spec Kit 80%(40/50)、Kiro 82%、BMAD 82%、OpenSpec 84%(42/50)、无 spec 对照 72%(36/50);Uvik 自己声明合并率噪声带 ±10 个百分点——最好的 spec 臂领先对照 12pp,其余 8–10pp,均在或贴近自报噪声带内
- 原文:[转引] merge rate Spec Kit 80% (40/50), Kiro 82%, BMAD 82%, OpenSpec 84% (42/50), "No spec (control) 72% (36/50)", with "The noise band on merge rate is plus or minus 10 percentage points"
- URL:https://uvik.net/blog/spec-driven-development-benchmark/
- 来源:Uvik Software, 2026, Spec-Driven Development Benchmark 2026 (Q4 2026 run), uvik.net blog · 2026-10 · 【厂商】 · mixed · 基准 · secondhand
- 备注:经 FreekMencke/claude-kb PR #327 topics/kb-spec-driven.md SDD-008(2026-10-30 核)逐字转录;检索摘要另有 BMAD/Kiro 各自 41/50 的互相矛盾说法(Kiro 82%=41/50、BMAD 82%=41/50 与此一致)。合并 ≠ 正确:合并率是评审接受率,不是缺陷率。

## M03 (MEASURE)
- 论断:【本线复算】按 Uvik 公布计数做推断:OpenSpec 42/50 vs 对照 36/50,独立样本 Fisher 双侧 p≈0.23(Spec Kit 40/50 p≈0.48;41/50 p≈0.34);Wilson 95% CI 对照 58–83%、OpenSpec 72–92% 大幅重叠。同工单配对设计下,只有当全部 6 个不一致对都偏向 spec 时 McNemar 精确 p≈0.031 才显著;且 4 臂对 1 对照存在多重比较。结论:合并率差异在统计上不可区分于零
- 原文:
- URL:https://uvik.net/blog/spec-driven-development-benchmark/
- 来源:本线计算(基于 Uvik 公布计数),2026-11 · 2026-11 · 【研究】 · mixed · 基准 · paraphrase-checked
- 备注:现场核验类:输入数字本身为转引(M02),若 Uvik 一手计数不同需重算。未知每臂运行次数(疑为单次)——单次采样按 #14 AGENTbench 假精度教训审计。

## M04 (MEASURE)
- 论断:Uvik 评审缺陷:每合并工单缺陷数 spec 各臂 0.39–0.57(合并口径 0.46)vs 对照 0.86;分母是「已合并工单」,各臂合并集合不同(幸存者构成不同),且缺陷由评审记录、非上线后缺陷
- 原文:[转引] Review defects per merged ticket: 0.39 to 0.57 with a spec against 0.86 without
- URL:https://uvik.net/blog/spec-driven-development-benchmark/
- 来源:Uvik Software, 2026, Spec-Driven Development Benchmark 2026 (Q4 2026 run), uvik.net blog · 2026-10 · 【厂商】 · mixed · 基准 · secondhand
- 备注:经 FreekMencke/claude-kb PR #327 topics/kb-spec-driven.md SDD-008(2026-10-30 核)逐字转录;0.46/0.86 与多条检索摘要一致。口径陷阱:评审缺陷 ≠ ESEM 2026 的 SZZ 回溯缺陷;评审者能否看到 spec(盲审是否真盲于臂别)未核实——spec 臂产出的 PR 形态可能暴露臂别。

## M05 (MEASURE)
- 论断:Uvik 时间:合并中位耗时 spec 臂 36–55 分钟 vs 对照 29 分钟;spec 阶段中位 18 分钟/工单(OpenSpec 12 分钟 – BMAD 28 分钟)——spec 臂全部更慢
- 原文:[转引] median minutes to merge 36 to 55 against 29
- URL:https://uvik.net/blog/spec-driven-development-benchmark/
- 来源:Uvik Software, 2026, Spec-Driven Development Benchmark 2026 (Q4 2026 run), uvik.net blog · 2026-10 · 【厂商】 · mixed · 基准 · secondhand
- 备注:经 FreekMencke/claude-kb PR #327 topics/kb-spec-driven.md SDD-008(2026-10-30 核)逐字转录;spec 阶段时长来自检索摘要。墙钟 ≠ 人力时间:未核实是否含人工审阅 spec 的时间。

## M06 (MEASURE)
- 论断:Uvik token 与成本:spec 阶段占 spec 臂全部 token 的 35.1%(BMAD >40%);每合并工单成本对照 $2.43,spec 框架 $2.35(Kiro,唯一低于对照者)– $4.23
- 原文:
- URL:https://uvik.net/blog/spec-driven-development-benchmark/
- 来源:Uvik Software, 2026, Spec-Driven Development Benchmark 2026 (Q4 2026 run), uvik.net blog · 2026-10 · 【厂商】 · mixed · 基准 · secondhand
- 备注:仅检索摘要;Kiro 走自有计费/IDE,与其余臂成本口径(API token 计价 vs Kiro credit)可能不可比,待一手核对。每工单 token 绝对值未找到。

## M07 (MEASURE)
- 论断:Uvik 异质性:spec 在 bug 修复、重构、写测试类工单上「不回本」;在 feature + 数据管线工单上最佳 spec 臂合并率 90% vs 对照 60%;第三方转述称 spec 只在触及 ≥3 文件的工单上有益、1–2 文件工单几乎无增益
- 原文:[转引] A spec "did not pay for itself on bug-fix, refactor, or test-writing tickets"
- URL:https://uvik.net/blog/spec-driven-development-benchmark/
- 来源:Uvik Software, 2026, Spec-Driven Development Benchmark 2026 (Q4 2026 run), uvik.net blog · 2026-10 · 【厂商】 · mixed · 基准 · secondhand
- 备注:经 FreekMencke/claude-kb PR #327 topics/kb-spec-driven.md SDD-008(2026-10-30 核)逐字转录(引语部分);90% vs 60% 为检索摘要,子组 n 未知(若 feature+pipeline 仅 ~10–20 张,30pp 差异 CI 极宽),属事后子组分析。「≥3 文件」说法未能在 Uvik 原文定位。

## M08 (MEASURE)
- 论断:Uvik 唯一的 spec 一致性测量:在 spec 臂已合并工单中,有 7.9% 的合并代码与其自身 spec 不符(是否逐臂、由谁判定未知)
- 原文:
- URL:https://uvik.net/blog/spec-driven-development-benchmark/
- 来源:Uvik Software, 2026, Spec-Driven Development Benchmark 2026 (Q4 2026 run), uvik.net blog · 2026-10 · 【厂商】 · mixed · 基准 · secondhand
- 备注:仅检索摘要。这是本线找到的唯一「spec–代码漂移」量化,但是单次实现时点的一致性,不是随时间的漂移;分母(合并 spec 臂工单 ≈163)与判定方法待核。

## M09 (MEASURE)
- 论断:Uvik 模型/工具链与数据:模型 claude-sonnet-5;一说「5 臂全用」,另一说「4 个 spec 框架中 3 个跑在 Claude Code 内」(Kiro 疑在自有 IDE)——工具链(harness)与 spec 方法共变,构成混杂;Kiro spec 中位 106 行/工单;原始结果 CSV(uvik-sdd-benchmark-2026-results.csv)以 CC BY(一说 4.0)发布;每臂运行次数未找到
- 原文:
- URL:https://uvik.net/blog/spec-driven-development-benchmark/
- 来源:Uvik Software, 2026, Spec-Driven Development Benchmark 2026 (Q4 2026 run), uvik.net blog · 2026-10 · 【厂商】 · mixed · 基准 · secondhand
- 备注:两条检索摘要互相矛盾,须回一手。CSV 下载链接未能取得,本线无法复跑——「原始数据可复跑」目前只是声明。

## M10 (MEASURE)
- 论断:Uvik 是谁:Python 外包/人员增补(staff augmentation)公司,自称 2015 年成立、总部塔林(英国 Ipswich 设商务处),目录站称 30+ 员工;同一批 50 张工单另做过「AI Coding Agent Benchmark」(Claude Code/Codex/Cursor/Copilot)。不是 SDD 工具厂商,对 4 个框架无直接利益,但基准是其内容营销(售卖 AI 工程人力),且 spec 臂「略好但更贵更慢、小单不划算」的结论恰好支持「需要资深工程判断」的服务叙事
- 原文:
- URL:https://uvik.net/about-us/
- 来源:Uvik Software, About Uvik Software: Engineer-Led Python Staff Augmentation Since 2015 · 2026-05 · 【厂商】 · n/a · 文档 · secondhand
- 备注:公司信息来自检索摘要(自述页面 + Clutch/Sortlist 目录)。第三方接收:mattbutlerengineering/ai-tooling 2026-11-02 扫描以「自报厂商基准」理由拒收;claude-kb 称结果「inside its ±10-point noise band」。未见任何独立团队复跑。

## M11 (MEASURE)
- 论断:单人对照(DEV,dimwiddle,2026-02):同一项目两种设置(标准 vs 结构化 spec)跑 agent;基线 agent 自评「没问题」甚至给自己最高分,关键缺陷被外部验证而非 agent 自评抓到;spec 引导组在验证流程推动下自行修复逻辑错误
- 原文:
- URL:https://dev.to/dimwiddle/ai-agents-cant-mark-their-own-homework-case-study-26mk
- 来源:dimwiddle (DEV Community), 2026, AI Agents Can't Mark Their Own Homework [Case Study] · 2026-02 · 【媒体】 · T4 · 案例 · secondhand
- 备注:dev.to 被网络策略拦截,只见检索摘要;样本=1 个项目、运行次数不明;作者是否推广自有验证工具未核。证据指向「外部验证器」而非「spec 本身」——混淆了 spec 与验收测试(T1 vs T4)。

## M12 (MEASURE)
- 论断:OrangeLoops 案例(2026-05):Spec Kit + Claude Code 构建全栈移动应用,共 195 个任务、约 2 小时记录的生成时间,随后 4 天测试/调试/稳定化;后端 94 任务约 1h06m,用掉该会话约 95% 上下文;无对照组
- 原文:
- URL:https://orangeloops.com/blog/spec-driven-development-with-ai-a-spec-kit-claude-code-case-study/
- 来源:OrangeLoops, 2026, Spec-Driven Development with AI: A Spec Kit + Claude Code Case Study · 2026-05 · 【厂商】 · T2 · 案例 · secondhand
- 备注:OrangeLoops 是 AI-native 软件外包,案例即营销。'2 小时生成' 与 '4 天稳定化' 必须并列引用,否则即口径偷换(生成墙钟 ≠ 交付周期)。95% 上下文占用与 context rot(#14 已核)相关。

## M13 (MEASURE)
- 论断:单人 token 对比(Medium,GPT-5.2/GPT-5.2-Codex):同一任务 OpenSpec 约 57,740 token vs Spec Kit 约 120,947(+109%);第二次测试 91,729 vs 181,040;每框架每任务单次运行,无无-spec 基线
- 原文:
- URL:https://medium.com/it-chronicles/is-your-safe-choice-burning-your-budget-1cfddf8782e4
- 来源:IT Chronicles (Medium), 2026, Is your 'safe choice' burning your budget? (OpenSpec vs Spec Kit) · 2026 · 【媒体】 · T2 · 对照实验 · secondhand
- 备注:仅检索摘要;单次采样,方向(Spec Kit 更重)与 Uvik(BMAD 最重、OpenSpec spec 阶段最短)及 OpenSpec README 自述「heavyweight」一致,但量级不承重。

## M14 (MEASURE)
- 论断:UCL 学生 × Microsoft 导师的 10 组实验:用 Spec Kit(GitHub Copilot + Claude Sonnet 4.5)反复构建同一目标系统,只改提示写法;结论是提示「设计」对 Spec Kit 表现的影响与提示「内容」相当——即同一 SDD 工具内部的方差就很大
- 原文:
- URL:https://techcommunity.microsoft.com/blog/educatordeveloperblog/prompt-engineering-for-spec-driven-development-with-speckit/4512622
- 来源:Microsoft Tech Community (Educator Developer Blog), 2026, Prompt Engineering for Spec-Driven Development with SpecKit · 2026 · 【媒体】 · T1 · 对照实验 · secondhand
- 备注:检索摘要所给「4h53m vs 2h24m」未能在原文定位,不得引用。意义在于噪声口径:若工具内提示差异就能造成大差,跨工具单次比较(Uvik)更难解读。

## M15 (MEASURE)
- 论断:Level Up Coding「spec rework rate」文:提出用「spec 返工率」与「每个被接受变更的成本」替代 agent 速度,给出基于 Jira/Git 的计数规则与记录模板,并明言小规模试点产生不了普适的生产率百分比——这是度量提案,不是测量
- 原文:
- URL:https://levelup.gitconnected.com/spec-driven-development-spec-rework-rate-and-cost-per-accepted-change-instead-of-ai-agent-speed-43e4718a1d86
- 来源:Level Up Coding, 2026, Spec-Driven Development — Spec Rework Rate and Cost per Accepted Change Instead of AI Agent Speed · 2026 · 【媒体】 · mixed · 评论 · secondhand
- 备注:会员文,全文未读。未发现任何人按此口径公布实测数据。

## M16 (MEASURE)
- 论断:【现场核验】Spec Kit(commit f29319d,2026-11-10)9 个命令模板共 128,370 字节;核心路径 specify+plan+tasks+implement 4 个模板共 51,211 字节(≈1.3 万 token,按 4 字符/token 粗估),每次调用对应命令时注入;OpenSpec(commit a959be7)12 个 skill 共 184,149 字节——SDD 工具本身就是大块指令上下文
- 原文:
- URL:https://github.com/github/spec-kit/tree/main/templates/commands
- 来源:github/spec-kit 仓库 templates/commands/*.md(本线 git clone 实测);Fission-AI/OpenSpec skills/*/SKILL.md · 2026-11 · 【研究】 · T2 · 基准 · verbatim-checked
- 备注:本线 wc -c 实测;token 数为粗估(tiktoken 编码表下载被拦)。命令模板按调用注入而非每会话全部加载;spec-kit issue #1401 所称「每会话约 18.6k token / 9.3% 窗口」未能读原文(GitHub API 未授权),不采信。

## M17 (MEASURE)
- 论断:SWE-Bench Pro(Scale AI)消融:去掉人工补写的 requirements 与 interface 后,GPT-5 与 Claude Opus 4.1 表现「显著退化」;二手转述数字为 GPT-5 25.9%→8.4%、Opus 4.1 22.7%→8.2%;作者把部分退化归因于测试期待特定名称/API 造成的假阴性
- 原文:
- URL:https://arxiv.org/abs/2509.16941
- 来源:Deng et al. (Scale AI), 2025, SWE-Bench Pro: Can AI Agents Solve Long-Horizon Software Engineering Tasks?, arXiv 2509.16941 · 2025-09 · 【研究】 · mixed · 基准 · secondhand
- 备注:arxiv.org 被代理拦截。检索摘录的论文句:'Without the requirements and interface, both models tested (GPT-5 and Claude Opus 4.1) show significantly degraded performance.'——未亲读,故 quote 留空。具体数字来自 alphaxiv 概述,且 25.9 与 GPT-5 公开集 23.3 头条数不一致。interface(签名)属 T3,requirements 属 T1:混合型 spec。Scale 作为基准卖方有利益。

## M18 (MEASURE)
- 论断:Ambig-SWE(ICLR 2026,CMU):把 SWE-bench Verified 题面改成欠规约版本,比较 full / hidden / interactive;交互(向用户澄清)可使欠规约输入上的表现比非交互最高提升 74%,但模型默认不提问,且难以区分欠规约与充分规约输入
- 原文:
- URL:https://arxiv.org/abs/2502.13069
- 来源:Vijayvargiya, Zhou, Yerukola, Sap, Neubig, 2025/2026, Ambig-SWE: Interactive Agents to Overcome Underspecificity in Software Engineering, ICLR 2026 · 2025-02 · 【研究】 · T1 · 基准 · secondhand
- 备注:仅检索摘要;full vs hidden 的具体解决率未取得。这是「规约完整度 → 结果」的最干净因果操纵之一(配对、同题),但操纵的是题面信息量,不是 SDD 流程。与 PRO 线 ClarifyGPT 交叉。

## M19 (MEASURE)
- 论断:The Specification Gap(单作者预印本):51 个类生成任务,规约从完整 docstring(L0)逐级剥到裸签名(L3);单 agent 准确率 89%→56%,双 agent 集成 58%→25%;恢复完整规约即回到 89%,冲突报告无额外收益;2 个 Claude 模型 × 3 次独立运行
- 原文:
- URL:https://arxiv.org/abs/2603.24284
- 来源:Camilo Chacón Sartori, 2026, The Specification Gap: Coordination Failure Under Partial Knowledge in Code Agents, arXiv 2603.24284 · 2026-03 · 【研究】 · T1 · 对照实验 · secondhand
- 备注:检索摘要多次一致;单作者、未同行评审、无独立复现;任务为合成类生成,外推到仓库级 SDD 有限。剂量-反应形状清晰,是「spec 细节有用」最强的受控证据之一。

## M20 (MEASURE)
- 论断:Google 团队(Tufano 等,SpecOps '26 workshop):agent 先写半形式规约(前置/后置条件、未定义行为)再生成测试,相比直接生成测试,缺陷检出率 +9.8pp(p=0.0352)、分支覆盖 +2.5pp(p=0.0034),行覆盖持平(约 74%),token 约多 38%;评估集据称为 90 个 Google 内部真实缺陷(C++/Java/Python/Go)
- 原文:
- URL:https://arxiv.org/abs/2608.17177
- 来源:Tufano et al. (Google), 2026, Grounding AI Agents in Contracts: An Empirical Evaluation of Spec-Driven Test Generation, arXiv 2608.17177 / SpecOps '26 · 2026-08 · 【研究】 · T3 · 对照实验 · secondhand
- 备注:p 值与 38% token 来自检索摘要;'90 个缺陷' 仅见于另一 AI 扫描笔记,检索未能证实。workshop 论文;效果+成本同时出现,是「spec 有益但有税」的干净样本。注意只是测试生成子任务。

## M21 (MEASURE)
- 论断:TD Bank 团队(Haeri & Ghelichi):固定测试者、预算与修复循环,只改是否以规则清单给出规约;给规约时 30 个缺陷抓到 27 个,无规约规划测试时只抓到 2 个;在规约本就充分的算法题上既无益也无害
- 原文:
- URL:https://arxiv.org/abs/2607.06636
- 来源:Amin Haeri, Mahdi Ghelichi (TD Bank), 2026, Specification Grounding Drives Test Effectiveness for LLM Code, arXiv 2607.06636 · 2026-07 · 【研究】 · T1 · 对照实验 · secondhand
- 备注:仅检索摘要;n=30 缺陷(注入?)来源未核。「规约充分时无增益」是关键边界条件:spec 的价值取决于原题面欠规约程度。

## M22 (MEASURE)
- 论断:WiseSpec(ASE 2026 学生研究竞赛,单作者):agent 先构造需求、以执行结果打分并迭代精炼后再写代码;在 SWE-bench Lite/Verified/Pro 各 100 个抽样实例 × 2 个 LLM × 对比 Agentless/Trae-agent/Claude Code,%Resolved 提升 2–29pp(Wilcoxon p<2.5×10⁻⁴);换强模型 Claude-Opus-4.8 时 Pro 上仅 53%→56%
- 原文:
- URL:https://arxiv.org/abs/2609.00568
- 来源:Zhao Tian, 2026, WiseSpec: Requirements-Driven Agents for Code Generation, arXiv 2609.00568 (ASE 2026 SRC) · 2026-09 · 【研究】 · T1 · 基准 · secondhand
- 备注:数字来自检索摘要与 mattbutlerengineering/ai-tooling PR #752(其称读过 PDF);无组件消融、无等算力基线,增益可能部分来自额外计算;强模型上增益缩小——与 #14 '模型越强 context 文件边际越小' 方向一致。

## M23 (MEASURE)
- 论断:Spec Kit Agents(Taghavi & Bhavani):在 Spec Kit 流水线上加上下文落地钩子,128 次运行 / 32 个功能任务 / 5 个仓库,LLM 评审 1–5 分综合质量 +0.15,测试通过率 99.7–100%;SWE-bench Lite Pass@1 56.5%→58.2%(+1.7pp);代价是额外延迟
- 原文:
- URL:https://arxiv.org/abs/2604.05278
- 来源:Pardis Taghavi, Santosh Bhavani, 2026, Spec Kit Agents: Context-Grounded Agentic Workflows, arXiv 2604.05278 · 2026-04 · 【研究】 · T2 · 基准 · secondhand
- 备注:比较的是 Spec Kit+钩子 vs Spec Kit,不是 SDD vs 无 SDD;LLM-as-judge 0.15 分的噪声未知;作者机构未核(可能为厂商)。

## M24 (MEASURE)
- 论断:SSDE(McGill,FSE Companion '26 试点):5 个 LLM × 3 个 MVC 系统,给自然语言 spec 叠加领域模型 + Gherkin 场景;Claude 在 6 个样本中仅 3 个取得最高平均 TPR,在 CheECSEManager 两个样本上反而异常偏低——结构化规约收益随模型与系统不稳定
- 原文:
- URL:https://arxiv.org/abs/2605.02455
- 来源:Feng, Chen, Meyer, Mussbacher, 2026, LLM-Assisted Repository-Level Generation with Structured Spec-Driven Engineering, FSE Companion '26 · 2026-05 · 【研究】 · T4 · 对照实验 · secondhand
- 备注:检索摘要称表格抽取乱码,TPR 定义未核;试点规模小。

## M25 (MEASURE)
- 论断:Rebuild Dossier 自我证伪基线:一个忽略输入、对所有请求返回 {} 与 200 的空桩,通过了该研究由 spec 派生的全部可见测试(20/20)与留出测试(12/12),但在 77 项保真检查中 0 项完全匹配——spec 派生测试套件只证明方法存在且不崩溃
- 原文:a handler that does nothing passes every visible and held-out test in the sealed study. Those suites therefore certify only that each method exists and doesn't crash on the request they send.
- URL:https://github.com/Parker-Fawcett/rebuild-dossier/blob/main/evidence/baselines/constant-200/README.md
- 来源:Parker Fawcett, 2026-10-01, Constant-200 baseline, rebuild-dossier repo (companion to arXiv 2608.23616) · 2026-10 · 【研究】 · T4 · 对照实验 · verbatim-checked
- 备注:本线 git clone 逐字读取。作者即工具作者(利益相关),但这是作者主动公布的不利结果。T4 口径警示:'测试全过' 不能当 spec 被满足的证据。论文另称完整流程未胜过「弱模型+完整源码+单一提示」(小应用打平、大应用落败)——该句仅见检索摘要。

## M26 (MEASURE)
- 论断:Rebuild Dossier 跨模型层级观察:弱模型会读懂 CLAUDE.md 中「只构建当前失败的部分、不要批量重生成」的规则,然后照样违反,因为没有机制检查;作者因此把两条规则改为 hook 强制(spec/ 目录写锁、无测试契约禁止提前构建)
- 原文:a weaker model will happily read `CLAUDE.md`, understand "only build what's currently failing, don't batch-regenerate," and then quietly violate it anyway — because nothing *checked* it.
- URL:https://github.com/Parker-Fawcett/rebuild-dossier/blob/main/README.md
- 来源:Parker Fawcett, 2026, rebuild-dossier README · 2026-10 · 【研究】 · T2 · 案例 · verbatim-checked
- 备注:本线逐字读取;观察性、小样本。与 #14 '遵从率' 主题直接相连:写进上下文的 spec 规则 ≠ 被执行的规则。

## M27 (MEASURE)
- 论断:门控式 SDD 工作流审计轨迹研究(2026-11):Claude Code 上的 spec 驱动流程,9 个功能 / 7 个项目;在其中 3 个项目里,流程并未要求的重复审查消耗了审查子代理 75.3% 的 token;几乎所有控制都是由被约束的同一模型执行的指令,编排者自己运行并评判自己的检查
- 原文:
- URL:https://arxiv.org/abs/2611.05094
- 来源:Rodrigo Figueiredo Abdo, Pedro Carvalho Brom, 2026, A Gated Spec-Driven Workflow: An Audit-Trail Study of Coding-Agent Work, arXiv 2611.05094 · 2026-11 · 【研究】 · T2 · 观察 · secondhand
- 备注:仅检索摘要;作者疑为该流程设计者(自研自评);流程税的少有量化之一。

## M28 (MEASURE)
- 论断:Specification-first convergence 单案例:spec 先行协议下 AI agent 拆除一个 71.7 万行 TypeScript 代码库中跨 189 个文件的核心架构不变量,无测试 oracle、无人工代码审查;作者公司设计并分发所用 agent;'上线后零缺陷' 等说法仅见二手博客
- 原文:
- URL:https://arxiv.org/abs/2608.12440
- 来源:Joel Abenhaim, 2026, Specification-first convergence with an AI coding agent: a case study ... 189 files in a 717k-line codebase, arXiv 2608.12440 · 2026-08 · 【厂商】 · T1 · 案例 · secondhand
- 备注:n=1、利益冲突自披露、日志公开可审;不可用作效果证据,只能作「可行性」案例。

## M29 (MEASURE)
- 论断:ESEM 2026(Hill)返工口径:88,052 个已合并 PR / 119 个仓库,带 spec 工件的 PR 返工无保护效应——作者内对比 +1.2pp(p=0.001,与厂商主张反向),匹配后 +0.5pp(p=0.146);spec 质量不预测返工(p=0.860);且样本中没有仓库提交真正的 SDD 工具产出(spec 工件多为 ticket 引用)
- 原文:
- URL:https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.ESEM.2026.84
- 来源:Brenn Hill, 2026, Specification Artifacts in Open-Source Pull Request Workflows Do Not Reduce Defects, ESEM 2026 (LIPIcs 394, art. 84) · 2026-10 · 【研究】 · T1 · 观察 · secondhand
- 备注:由 CON 线负责全文核对;本线只记录它是唯一大样本「返工率」测量。数字转引自 mattbutlerengineering/ai-tooling LEARNING.md(其称以 pdftotext 读 PDF)。口径:测的是 PR 里的 ticket 引用,不是 Spec Kit/Kiro 产物。

## M30 (MEASURE)
- 论断:SpecMine(CMU,MSR 2027 挖掘挑战数据集):470,795 个 spec 文件 / 73,030 个仓库(17 个工具)+ Kiro 98,574 文件 / 12,910 仓库,99.7% 首次提交于 2025 年及以后;5,992 个触及 spec 的 PR / 581 仓库带完整变更集,多数 spec PR 同时改代码——但论文未报告随时间的漂移测量;数据在 Zenodo(10.5281/zenodo.22102779)
- 原文:
- URL:https://arxiv.org/abs/2608.25202
- 来源:Agarwal, Singhal, Breaux, Vasilescu (CMU), 2026, SpecMine: A Large-Scale Corpus of Spec-Driven Development Artifacts, arXiv 2608.25202 · 2026-08 · 【研究】 · mixed · 观察 · secondhand
- 备注:与 ADOPT 线重叠(计文件非项目,#14 教训)。对 MEASURE 的意义:spec/代码同 PR 共变是漂移的反向代理,公开 PR 层可用于本期现场核验(spec 文件最后修改 vs 代码最后修改的滞后分布)。

## M31 (MEASURE)
- 论断:Tessl 自测:其 tiles/usage specs 使正确使用公共 API 的比例提升约 35%;覆盖 300+ 库时「最高 3.3×、平均 1.17×」;Bowser npm 库 57%→93%(1.63×)
- 原文:
- URL:https://tessl.io/blog/fixing-api-misuse-how-tessl-improves-agent-accuracy-by-up-to-33x
- 来源:Tessl, 2025–2026, Fixing API Misuse: How Tessl Improves Agent Accuracy by up to 3.3X(及 Proposed Evaluation Framework 博文) · 2026 · 【厂商】 · T1 · 基准 · secondhand
- 备注:Tessl 卖 spec registry,直接受益。'usage spec' 实为库文档上下文,机制更接近 #14 的 context 文件/llms.txt,不是「先写需求再生成」——不得与 SDD 效果混引。'最高 3.3×' 与 '平均 1.17×' 必须并列。

## M32 (MEASURE)
- 论断:#14 已核(AGENTbench,ETH SRI + LogicStar.ai,arXiv 2602.11988):Round 3 方法学审计席否决其 pp 级成功率差值(单次运行、138 实例聚在 12 仓库、基准由被测 agent 参与构建);存活的只有:无一致成功率提升的「零效应」、约 +20% 推理成本/步数、agent 会遵从 context 文件指令。可迁移到 SDD 的仅是「常驻 spec/constitution/steering 文件作为上下文」这一层
- 原文:What DOES survive, real-but-weak: (1) the null — no consistent success-rate improvement from context files in this Python/single-shot setting — because a large positive effect would have been visible despite the noise; (2) the cost/steps increase (~+20%, +2.4-3.9 steps)
- URL:https://arxiv.org/abs/2602.11988
- 来源:Gloaguen, Mündler, Müller, Raychev, Vechev, 2026, Evaluating AGENTS.md: Are Repository-Level Context Files Helpful for Coding Agents?, arXiv 2602.11988(#14 R3 判决) · 2026-02 · 【研究】 · T2 · 基准 · verbatim-checked
- 备注:#14 已核:quote 逐字取自本仓库 research/agent-readme/04-verification-round3.md G1 审计席。迁移边界:AGENTbench 操纵的是仓库级常驻文件有无,不是任务级 spec;不得把其结论当作 'SDD 无效' 的证据,只能支持 'spec 作为额外上下文本身有成本、无保证收益'。同名 Tsinghua AgentBench 误引风险。

## M33 (MEASURE)
- 论断:#14 已核(Shepard & Albrecht,Williams College,arXiv 2606.20512):SWE-bench Verified 上无指导 25.5% → 一次性 LLM 生成指导 28.3% → 迭代精炼指导 33.0%(4 次独立试验,精炼 vs 无指导 p<0.001),Qwen3.5-35B-A3B。迁移:有执行反馈的迭代精炼才带来明显增益,与 WiseSpec「需求打分-精炼环」及 Tufano「规约紧接被消费」同向——SDD 的有效成分可能是反馈环而非文档本身
- 原文:an LLM-generated guidance file (tree-sitter repo map + one-shot generic guidance) raised mean resolve rate from 25.5% (unguided) to 28.3%, and iteratively refined guidance to 33.0% (4 independent trials; refined-vs-unguided p<0.001 in all trials, refined-vs-static p<0.05)
- URL:https://arxiv.org/abs/2606.20512
- 来源:Shepard & Albrecht, 2026, Probe-and-Refine Tuning of Repository Guidance for Coding Agents, arXiv 2606.20512(#14 R3 反证席) · 2026-06 · 【研究】 · T2 · 基准 · verbatim-checked
- 备注:#14 已核:quote 逐字取自 research/agent-readme/04-verification-round3.md G1 反证席(该席当时也只能经检索摘要核对 arXiv,原始置信度 medium)。指导文件含 tree-sitter 仓库地图,不同于典型 spec。

## M34 (MEASURE)
- 论断:#14 已核(context rot,Chroma 2025 + LongMemEval/NoLiMa 独立佐证,R3 存活 medium):约 300 token 聚焦提示优于把同样信息嵌入约 11.3 万 token 历史,差距约 10–40+ 点、随模型不均。迁移:长 spec 栈(OrangeLoops 后端阶段用掉 ~95% 上下文;Spec Kit 单命令模板 8–22KB)存在稀释风险——但目前没有任何直接测量 'spec 长度 → agent 结果' 的 SDD 研究
- 原文:adding large volumes of irrelevant/distracting context degrades answer accuracy relative to oracle-focused context, non-uniformly across models
- URL:https://research.trychroma.com/context-rot
- 来源:Chroma, 2025-07-14, Context Rot(#14 R3 G5 判决) · 2025-07 · 【厂商】 · n/a · 基准 · verbatim-checked
- 备注:#14 已核:quote 逐字取自 research/agent-readme/04-verification-round3.md G5 审计席。Chroma 卖向量库(利益相关),但有独立同行评审文献佐证。spec 是 '相关' 上下文,而 context rot 测的是 '无关/干扰' 上下文——迁移只在 spec 冗长、与当前任务弱相关时成立。

## M35 (MEASURE)
- 论断:#0 已核(METR 2025 RCT):16 位资深开源维护者在自己的成熟代码库上随机分配任务,允许用 AI 的任务平均慢 19%;事前预测快 24%,事后仍自评快 20%。迁移:SDD 从业者博客中自报的「快了/省了」不构成效果证据;METR 未测 SDD 本身
- 原文:而这些开发者事前预测 AI 会让自己快 24%——做完之后、在实际被拖慢的情况下,他们仍然觉得自己快了 20%。
- URL:https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/
- 来源:METR, 2025-07, Measuring the Impact of Early-2025 AI on Experienced Open-Source Developer Productivity(#0 已核) · 2025-07 · 【研究】 · n/a · RCT · verbatim-checked
- 备注:#0 已核:quote 逐字取自本仓库 sources/ai-native-plain.zh.md(#0 已发布口径)。只迁移「感知 ≠ 测量」的方法学教训,不迁移效应量。


### 搜索角度
- Uvik 一手页面 uvik.net/blog/spec-driven-development-benchmark/ 与 uvik.net/spec-driven-development-benchmark/:WebFetch DNS 拒绝、curl CONNECT 403、web.archive.org 403 —— 全文未读
- Uvik 方法学细节(每臂运行次数、模型、工单来源、盲审程序):多轮检索,只得零散摘要,运行次数始终未找到
- Uvik 原始数据 CSV / GitHub 仓库 / CC BY 许可:检索得文件名 uvik-sdd-benchmark-2026-results.csv,下载链接与仓库均未找到
- Uvik 公司背景(about-us、Clutch、目录站):检索摘要
- 第三方对 Uvik 的引用:FreekMencke/claude-kb PR #327(git fetch 成功,逐字转录结果表)、mattbutlerengineering/ai-tooling PR #752(git fetch 成功,拒收理由)
- 独立复跑 Uvik:未找到
- dev.to dimwiddle 案例:dev.to 被网络策略拦截,仅检索摘要
- OrangeLoops Spec Kit + Claude Code 案例:仅检索摘要
- levelup「spec rework rate」:会员文,仅检索摘要;同站其他 SDD 文(ROI、token economics、brownfield)无测量
- spec drift / specification drift 实证测量:未找到纵向漂移测量;找到 SpecStory 定义、Piskala 2602.00180 概念文;Uvik 7.9% spec 不符为唯一横截面数字
- 返工率测量:只有 ESEM 2026 Hill(CON 线负责)
- 学术:规约细节梯度 → 结果(Specification Gap 2603.24284、Ambig-SWE 2502.13069、SWE-Bench Pro 消融 2509.16941、Haeri 2607.06636、Tufano 2608.17177、WiseSpec 2609.00568、SSDE 2605.02455、class-level 2510.26130 未展开)
- 学术:SDD 工具本身的评测(Spec Kit Agents 2604.05278、Gated Spec-Driven Workflow 2611.05094、Rebuild Dossier 2608.23616 + 仓库、spec-first convergence 2608.12440)
- arxiv.org / export.arxiv.org / openreview / dl.acm.org / semanticscholar:均被代理拦截,学术数字全部来自检索摘要
- Spec Kit / OpenSpec 仓库 git clone 现场测量模板体积(成功);tiktoken 编码表下载被拦,改用字节粗估
- spec-kit GitHub issue #1401/#1492(token 开销):GitHub REST API 未授权,未读
- 厂商自测:Tessl 评测博文(检索摘要);Kiro/Augment 官方 SDD 效果测量:未找到有数字的
- 单人 token 对比:Medium OpenSpec vs Spec Kit(检索摘要);dabase.com 三框架比较(无测量);ranthebuilder、Stephan Miller 比较文(未展开,定性)
- Microsoft Tech Community UCL 10 组 Spec Kit 实验(检索摘要;4h53m 数字未能定位)
- innoq「versteckte Kosten」:定性反思,无测量
- 本仓库 #14 research/agent-readme/02、04 与 #0 sources/ai-native-plain.zh.md:逐字读取已核口径

### 交叉口径问题
- Uvik 合并率(评审接受)≠ 缺陷率 ≠ ESEM 的 SZZ 缺陷 ≠ 上线后缺陷;每合并工单缺陷数的分母随臂变化
- Uvik 噪声带 ±10pp 由 Uvik 自述;本线复算 Fisher p≈0.23(最佳臂)——任何「spec 提升合并率 X%」的表述都不承重
- Uvik 模型/工具链两说(5 臂均 claude-sonnet-5 vs 4 框架中 3 个在 Claude Code 内):harness 与 spec 方法共变
- Uvik 每臂运行次数未知,按单次采样假精度审计(#14 AGENTbench 教训)
- Uvik 日期两说(Last updated 2026-10-08 vs 2026-10-15);框架计数存在互相矛盾的转述(BMAD/Kiro 41)
- Uvik 子组(feature+pipeline 90% vs 60%;bug/refactor/test 不回本)为事后子组,n 未知
- Uvik 成本:Kiro credit 计价 vs API token 计价可能不可比
- OrangeLoops「2 小时生成」必须与「4 天稳定化」并列;生成墙钟 ≠ 交付周期
- SWE-Bench Pro 消融数字(25.9→8.4)来自二手概述,且与公开集头条数 23.3 不一致;interface=T3、requirements=T1 混合
- Ambig-SWE / Specification Gap / Haeri 操纵的是题面信息量(T1),不是 SDD 流程;不能直接换算成 Spec Kit 等工具效果
- Tufano(T3 半形式规约)与 Haeri(T1 规则清单)测的是测试生成,不是代码生成
- WiseSpec / Shepard 的增益来自带执行反馈的迭代环,可能部分是额外算力;无等算力基线
- Tessl 'usage spec' 是库文档上下文,机制属 #14 context 文件,不属 SDD 需求先行
- #14 AGENTbench pp 级差值已被 R3 否决,只能引用零效应 + ~20% 成本;AGENTbench 操纵常驻文件,不是任务级 spec
- context rot 测无关/干扰上下文,spec 是相关上下文——迁移有条件
- METR 只迁移「感知 ≠ 测量」,不迁移 −19% 效应量
- Uvik 7.9% spec 不符是实现时点一致性,不是随时间漂移;目前无纵向 spec 漂移测量(SpecMine PR 层可作现场核验)
- Spec Kit 模板体积为字节实测、token 为粗估;issue #1401 '每会话 18.6k token' 未核且与按调用注入机制可能不符

# 线 FORMAL

## F01 (FORMAL)
- 论断:ProofNet(367 题,剔除 4 个非证明题后)的原版 ground-truth 形式陈述经审计 205/367(55.9%)有错;即便是已做过一轮修正的 ProofNet#,仍有 99/367(27.0%)有错。错误类型以「误解非形式数学」居首(ProofNet 95 题,25.9%)。每个错误以证明否命题、给出平凡化证明或书面理由确认。
- 原文:Audit the benchmark for both errors in the ground-truth formalizations and ambiguity in the informal statements, identifying **205/367 (55.9%)** errors in **ProofNet** and **99/367 (27.0%)** errors in **ProofNet#**.
- URL:https://github.com/marcusm117/ProofNet-Verified
- 来源:An, Min, Si, Bastani, 2026, Ground False: Dissecting and Repairing Errors in Formal Mathematics Benchmarks(ProofNet-Verified 仓库 README), NeurIPS 2026 E&D Track · 2026-10 · 【研究】 · T3 · 基准 · verbatim-checked
- 备注:README 口径 205(55.9%),搜索到的 NeurIPS 摘要口径为 204(56%),ICML listing 拆为 104(28%) 数学上为假 + 100(27%) 非假但不忠实——三处数字差 1,需回论文定版。'Total Errors' 含 NL 源歧义 9 + NL 源错误 1,纯形式化不忠实为 195(53.1%)。修正版忠实性由人工+AI agent 共识判定。

## F02 (FORMAL)
- 论断:同一 ProofNet-Verified 审计把错误按根因分 8 类:ProofNet 原版中误解非形式数学 95(25.9%)、缺前提 31(8.4%)、误解 Mathlib 28(7.6%)、隐含前提 18(4.9%)、误解 Lean 16(4.4%)、添加多余结论 7(1.9%);NL 源本身歧义/错误仅 10(2.7%)——即错位绝大部分发生在'翻译'而非'原题'一端。
- 原文:| Misunderstanding of Informal Math | 95 (25.9%) | 30 (8.2%) |
- URL:https://github.com/marcusm117/ProofNet-Verified
- 来源:An, Min, Si, Bastani, 2026, ProofNet-Verified README(Root Cause Breakdown 表) · 2026-10 · 【研究】 · T3 · 基准 · verbatim-checked
- 备注:对 SDD 的映射:规约—意图鸿沟主要是'写规约的人误解意图',而非意图本身不清(在数学题这种意图极清晰的场景下)。软件需求的 NL 源歧义率显然更高,不可外推比例。

## F03 (FORMAL)
- 论断:ProofNet#(Poiroux et al.)此前已发现公开 Lean 4 移植版 ProofNet 中 118 条(31.8%)含形式化错误并修正;后续 ProofNet-Verified 审计显示修正版仍有 27.0% 错误——基准修了一轮仍有约四分之一错。
- 原文:[ProofNet#](https://huggingface.co/datasets/PAug/ProofNetSharp) is a cleaner version of ProofNet compatible with `Lean v4.7.0` to `Lean v4.16.0-rc2`, correcting 118 errors in previous Lean 4 implementations of ProofNet
- URL:https://github.com/marcusm117/ProofNet-Verified
- 来源:ProofNet-Verified README 对 ProofNet# 的描述;原始:Poiroux et al., 2024, Reliable Evaluation and Benchmarks for Statement Autoformalization, arXiv 2406.07222 · 2024-06 · 【研究】 · T3 · 基准 · paraphrase-checked
- 备注:118 条/31.8% 的百分比口径来自搜索摘要(arXiv 不可达),118 这个数在 ProofNet-Verified README 逐字出现。31.8% 的分母≈371(118/371=31.8%),与 ProofNet-Verified 的 367 分母不同,不可直接相减。

## F04 (FORMAL)
- 论断:miniF2F 逾半题目的形式陈述与非形式陈述存在错位;修正版 miniF2F-v2 上全流程(autoformalizer+prover)最好成绩约 70%,原版口径约 40%。(#5 已核口径直接复用)
- 原文:More than half of miniF2F's problems have discrepancies between formal and informal statements; on the corrected miniF2F-v2 the best full-pipeline score is 70% (vs. 40% under the original scope)
- URL:https://github.com/roozbeh-yz/miniF2F_v2
- 来源:Ospanov, Farnia, Yousefzadeh, 2025, miniF2F-Lean Revisited: Reviewing Limitations and Charting a Path Forward, arXiv 2511.03108, NeurIPS 2025(引语为 #5 已发布英文版对其的转述) · 2025-11 · 【研究】 · T3 · 基准 · verbatim-checked
- 备注:#5 期已 3 票核验(machine-oracles-deep)。本线新发现口径陷阱:仓库 README Table 3 中 Kimina+Goedel-V2 在 v1 test 'Full score' 设定为 77.5、v2s 为 74.2(修正后反而更低),在 'No score (Olympiad)' 设定下 v1 49.2 → v2s 69.7。'40%→70%' 依赖评分设定与原文定义,见 cross_caliber_issues。

## F05 (FORMAL)
- 论断:在 miniF2F 上,自动化判官(Herald 的 back-translation + LLM 等价检查)判定 Herald 翻译器的形式化正确率为 97.5%(v1 test),人工评判仅 62.7%;Kimina 翻译器自动判官 98.4% vs 人工 90.6%;在竞赛原题版 v2c test 上 Herald 人工 54.1%、Kimina 人工 75.4%,自动判官仍 95-98%。即 LLM 判官对'陈述=意图'系统性高估 8-41pp。
- 原文:| **Herald**  | Herald’s automated judge | 97.5% | 97.1% | 96.7% | 97.5% | 95.1% | 97.1% |
| **Herald**  | Human                  | 62.7% | 69.7% | 66.0% | 68.9% | 54.1% | 60.2% |
- URL:https://github.com/roozbeh-yz/miniF2F_v2
- 来源:Ospanov, Farnia, Yousefzadeh, 2025, miniF2F-Lean v2 仓库 README Table 2(arXiv 2511.03108) · 2025-11 · 【研究】 · T3 · 基准 · verbatim-checked
- 备注:@128 采样口径;人工评判者人数/一致性未在 README 说明(需回论文)。这是'规约—意图鸿沟可测性'的关键证据:自动化忠实性判官与人工差距巨大,与 Verus-SpecGym 的 LLM-judge 漏判 26% 同向。

## F06 (FORMAL)
- 论断:ReForm 构建的 ConsistencyCheck 基准(859 条专家标注)显示:人类专家写的形式陈述中,miniF2F 有 16.4%、ProofNet 有 38.5% 含语义错误。(#5 已核)
- 原文:ConsistencyCheck Benchmark**: 859 expert-annotated items for evaluating semantic consistency, revealing that even human experts produce errors in up to 38.5% of cases.
- URL:https://github.com/Chen-GX/ReForm
- 来源:Chen et al., 2025, ReForm: Reflective Autoformalization with Prospective Bounded Sequence Optimization, arXiv 2510.24592, ICLR 2026(仓库 README) · 2025-10 · 【研究】 · T3 · 基准 · verbatim-checked
- 备注:README 逐字只有 'up to 38.5%',16.4% 来自 #5 已核论文正文。注意与 ProofNet-Verified 的 55.9%(ProofNet)/ 27.0%(ProofNet#)口径不同:ReForm 评的是哪个版本的 ProofNet、子样本多大,需回论文;三个数字(38.5% / 31.8% / 55.9%)不得并列为'ProofNet 错误率'。

## F07 (FORMAL)
- 论断:对五个常用 Lean 定理证明基准(miniF2F、ProofNet、FormalMATH、CombiBench、ProverBench)及其分叉版用 Lean 4 元程序静态检查器扫描,得到 4,833 条 findings,其中 398(或 399)条为机器可证实的问题(如除零、自然数减法下溢、空真前提)。工具作者自承:静态检查原则上无法判定'形式化是否意味着正确的数学'。
- 原文:A theorem can be type-correct, compile cleanly, and still formalize the wrong mathematics entirely.
- URL:https://github.com/Shashi456/atp-checkers
- 来源:Ammanamanchi, Bhat, Biderman, 2026, Faults in Our Formal Benchmarking: Dataset Defects and Evaluation Failures in Lean Theorem Proving, ICML 2026 / arXiv 2606.29493(仓库 LIMITATIONS.md) · 2026-06 · 【研究】 · T3 · 基准 · paraphrase-checked
- 备注:引语逐字来自仓库 LIMITATIONS.md;4,833 / 398 vs 399 来自搜索摘要(arXiv 与 ICML 版本差 1),未在一手核到。findings ≠ 错误题数('maybe' 级有显著误报)。

## F08 (FORMAL)
- 论断:Wu et al.(NeurIPS 2022)报告 LLM(Codex)能把 25.3% 的竞赛数学题'完美'翻译为 Isabelle/HOL 形式陈述;用这些自动形式化定理训练证明器,把 miniF2F 证明率从 29.6% 提到 35.2%。这是 autoformalization 忠实率的早期基线。
- 原文:
- URL:https://arxiv.org/abs/2205.12615
- 来源:Wu, Jiang, Li, Rabe, Staats, Jamnik, Szegedy, 2022, Autoformalization with Large Language Models, NeurIPS 2022 · 2022-05 · 【研究】 · T3 · 基准 · secondhand
- 备注:arXiv 不可达,数字来自搜索引擎对摘要的转引('correctly translate a significant portion (25.3%) ... perfectly');'完美'由作者人工评判,样本为 MATH 子集约 150 题(需回原文)。2022 年模型,只作历史基线,不得与 2025-26 数字比较趋势。

## F09 (FORMAL)
- 论断:Endres、Fakhoury、Chakraborty、Lahiri(FSE 2024)定义 nl2postcond:让 LLM 从自然语言注释生成可执行后置条件,并以'测试集正确性'(不拒绝正确实现)和'区分力'(能杀死代码变异体)两类自动指标评估;在 Defects4J 上生成的后置条件能区分 64 个真实历史 bug。
- 原文:Can Large Language Models Transform Natural Language Intent into Formal Method Postconditions?
- URL:https://github.com/microsoft/nl-2-postcond/tree/main/nl2postcondition-fse2024
- 来源:Endres, Fakhoury, Chakraborty, Lahiri, 2024, Can Large Language Models Transform Natural Language Intent into Formal Method Postconditions?, FSE 2024, arXiv 2310.01831 · 2024-07 · 【研究】 · T3 · 基准 · paraphrase-checked
- 备注:仓库 README 只核到题名/作者/制品;'64 bugs' 来自搜索摘要。Microsoft Research 作者(Copilot 厂商所在公司),但为同行评审学术论文。Defects4J 评估源码'not yet public'(README 原话:'the source code for the Defects4J evaluation is not yet public'),不可完全复跑。

## F10 (FORMAL)
- 论断:Lahiri 2026 立场文将 nl2postcond 结果转述为'LLM 生成的后置条件抓住了约八分之一的真实 bug,含 Daikon 漏掉的';并称 GPT-4 的 soundness/completeness 明显高于 GPT-3.5 和 CodeLlama。
- 原文:On the Defects4J benchmark [[11]](#ref11) (hundreds of real bugs across large Java projects), LLM-generated postconditions caught one in eight real bugs, including bugs missed by the classic Daikon invariant detector [[12]](#ref12).
- URL:https://risemsr.github.io/blog/2026-03-05-shuvendu-intent-formalization/
- 来源:Lahiri, 2026, Intent Formalization: A Grand Challenge for Reliable Coding in the Age of AI Agents, RiSE blog / arXiv 2603.17150 · 2026-03 · 【研究】 · T3 · 评论 · verbatim-checked
- 备注:作者为原论文合著者的自我转述(立场文,非新实验)。'一八分之一'与'64 bugs'需同分母核对(64/525≈12.2% 若分母为 Defects4J v2 全集——未核)。'抓住'= 后置条件对 buggy 版本失败、对修复版本通过,不是'生产中拦截'。

## F11 (FORMAL)
- 论断:Lahiri 明确把'规约验证'定为意图形式化的中心瓶颈:除用户外不存在判定规约正确性的 oracle;并主张 soundness(不拒绝正确行为)与 completeness(拒绝错误实现)两指标可只用测试(输入/输出对 + 输出变异)在写实现之前计算。
- 原文:The central bottleneck is *validating specifications*: since there is no oracle for specification correctness other than the user, we need semi-automated metrics that can assess specification quality with or without code, through lightweight user interaction and proxy artifacts such as tests.
- URL:https://risemsr.github.io/blog/2026-03-05-shuvendu-intent-formalization/
- 来源:Lahiri, 2026, Intent Formalization: A Grand Challenge..., RiSE blog / arXiv 2603.17150 · 2026-03 · 【研究】 · mixed · 评论 · verbatim-checked
- 备注:'规约—意图鸿沟的可测性'的理论锚:可测的只是相对于测试集/变异体的代理指标,不是对意图本身。completeness 依赖变异体是否反映'自然错误',作者自承更难。

## F12 (FORMAL)
- 论断:Lahiri 明确区分'意图形式化'与 Spec Kit 式 SDD:后者的规约仍是非形式、不可检查的。
- 原文:But these specifications remain informal and uncheckable.
- URL:https://risemsr.github.io/blog/2026-03-05-shuvendu-intent-formalization/
- 来源:Lahiri, 2026, Intent Formalization: A Grand Challenge..., RiSE blog · 2026-03 · 【研究】 · mixed · 评论 · verbatim-checked
- 备注:对 #25 分型的直接支持:T1/T2(Spec Kit)与 T3/T4 证据不得混引。注意 GitHub 与 Microsoft 同属一家公司,作者对 Spec Kit 的评价不构成竞争性攻击。 引语前一句为 'Tools like GitHub Spec Kit [9] structure AI coding around natural language requirements, improving traceability.'(原文为 blockquote 分行)。

## F13 (FORMAL)
- 论断:Lahiri(FMCAD 2024)用符号化测试评估 Dafny 规约:在约 150 条(MBPP-DFY,主要由 GPT-4 生成、人工标注)规约上,自动指标与人工标签高度一致,同时发现 3 条误标和 2 条复制粘贴导致的不一致规约,均为人工标注漏掉;典型例子是被专家标为'strong'的 common-elements 规约因用 ==> 而非 <==>,空列表即可平凡满足。
- 原文:Across the full evaluation, automated metrics found three mislabeled and two inconsistent specifications introduced by copy-paste errors—all missed by human labeling [[15]](#ref15).
- URL:https://risemsr.github.io/blog/2026-03-05-shuvendu-intent-formalization/
- 来源:Lahiri, 2024, Evaluating LLM-driven User-Intent Formalization for Verification-Aware Languages, FMCAD 2024, arXiv 2406.09757(经 2026 立场文转述) · 2024-06 · 【研究】 · T3 · 基准 · paraphrase-checked
- 备注:引语逐字来自 2026 博客(作者自述),FMCAD 原文未达。'约 150 条'来自搜索摘要;仓库 README 中目录名为 MBPP-DFY-153 / MBPP-DFY-50。说明人审规约同样会漏:'专家人审'不是金标准。

## F14 (FORMAL)
- 论断:Microsoft Research 的 AutoCLRS 项目:研究者以纯自然语言驱动 agent(Copilot CLI + Claude Opus 4.6)在约一个月内为约 50 个 CLRS 算法/数据结构产出 10 万+ 行 F*/Pulse 规约、代码与证明,其中需人审的规约粗估约 5,000 行(约为总量的 1/20);作者称规约审阅是关键挑战,且'规约质量与到底证明了什么高度参差'。
- 原文:100,000 lines
of code and proofs, with a very rough count of around 5,000 lines of
specification to be audited. That's a big chunk of specification to review, and
reviewing each of them also requires understanding the corresponding algorithm
from CLRS, but it's significantly less than the total amount of code and proofs.
- URL:https://risemsr.github.io/blog/2026-03-06-autoclrs/
- 来源:Swamy, 2026, Formalizing Data Structures and Algorithms with Agents, RiSE blog (Microsoft Research) · 2026-03 · 【研究】 · T3 · 案例 · verbatim-checked
- 备注:'规约审阅 vs 代码审阅成本'最直接的一手量化,但只是行数比(5k vs 100k),不是审阅工时;单人案例;'very rough count'。作者所在公司销售 Copilot CLI。证明由机器检查是前提——T1/T2 自然语言 spec 无此前提,不可外推。

## F15 (FORMAL)
- 论断:AutoCLRS 的 52 个算法目录由 AI 审阅生成,作者提示'要打很大折扣';规约已经过多轮 AI 审阅,但作者认为最终仍需人类专家详审。
- 原文:take this table with a big grain of salt---it was produced by an AI review of
the entire development.
- URL:https://risemsr.github.io/blog/2026-03-06-autoclrs/
- 来源:Swamy, 2026, Formalizing Data Structures and Algorithms with Agents, RiSE blog · 2026-03 · 【研究】 · T3 · 案例 · verbatim-checked
- 备注:与 miniF2F-v2 自动判官高估、Verus-SpecGym LLM-judge 漏判同向:AI 审规约不被作者本人信任为终审。

## F16 (FORMAL)
- 论断:对 AutoCLRS 中 agent 写的规约,再让 agent 写'小型证明导向测试'(SPOT,对具体小输入证明期望输出)后,首轮发现 52 个算法中 8 个存在实质性规约缺口(如 Prim 后置条件允许错误输出、哈希表 insert 允许永远返回 false、Kruskal 无生成树性质);其余 44 个'被认为'足够精确,但作者明言不能据此断言无缺口。
- 原文:Our [first run of
SPOTs](https://github.com/FStarLang/AlgoStar/blob/2f0ecc02d397e0ff8c43f02b9cf9cc14c172fcbc/autoclrs/TEST_REVIEW_REPORT.md)
revealed that 8 algorithms had interesting specification gaps, as shown below.
- URL:https://risemsr.github.io/blog/2026-04-16-spotting-specs/
- 来源:Swamy, Lahiri, 2026, Spotting Specification Gaps with Small Proof-Oriented Tests, RiSE blog · 2026-04 · 【研究】 · mixed · 案例 · verbatim-checked
- 备注:8/52≈15% 是已被机器证明通过的规约中仍不忠实于意图的下界(SPOT 覆盖有限)。说明'证明⊢陈述≠陈述=意图'在 agent 工作流中实测存在。厂商所在研究院自评。

## F17 (FORMAL)
- 论断:SPOTs 作者认为:小而具体的测试比大而抽象的规约更容易审阅,但 SPOT 本身也要审,且存在 agent 把规约过拟合到 SPOT 的风险(尚未观察到)。哈希表 insert 这类错误路径规约缺口'人工审阅容易漏、SPOT 抓住了'。
- 原文:SPOTs also need to be reviewed, though because they are small and concrete,
  they can be easier to review than large, abstract specifications.
- URL:https://risemsr.github.io/blog/2026-04-16-spotting-specs/
- 来源:Swamy, Lahiri, 2026, Spotting Specification Gaps with Small Proof-Oriented Tests, RiSE blog · 2026-04 · 【研究】 · T4 · 案例 · verbatim-checked
- 备注:'审规约比审代码便宜'的反向细化:即便在 T3 内部,审抽象规约也难,需要退回 T4 具体例子做审阅代理。无工时测量,定性判断。

## F18 (FORMAL)
- 论断:AutoCLRS 完整性测试(黑盒:调用实现、断言具体期望输出,仅当后置条件足够强时可验证)共 48 个测试,43 个完整性证明通过、5 个规约不完整;另有 5 个非确定性用例方法学尚无法处理。
- 原文:**43 completeness proofs discharged ✅, 5 spec incomplete ❌.**
- URL:https://github.com/microsoft/nl-2-postcond/tree/main/eval-autoclrs-specs
- 来源:Microsoft, 2026, Intent Formalization for AutoCLRS Algorithms (nl-2-postcond 仓库 eval-autoclrs-specs/README.md) · 2026-03 · 【研究】 · T3 · 基准 · verbatim-checked
- 备注:与 SPOT 的 8/52 是不同轮次、不同方法、不同分母(48 测试 vs 52 算法),不得合并为单一'缺口率'。verification-log 显示 21/21 章节、48 文件通过。

## F19 (FORMAL)
- 论断:SpecGen(ICSE 2025)用 LLM 对话 + OpenJML 验证器反馈 + 变异修补生成 JML 形式规约,在 385 个 Java 程序上为 279 个生成了可验证规约,对比 AutoSpec 247、Houdini 98。
- 原文:
- URL:https://arxiv.org/abs/2401.08807
- 来源:Ma, Liu, Li, Xie, Bu, 2025, SpecGen: Automated Generation of Formal Program Specifications via Large Language Models, ICSE 2025 · 2025-04 · 【研究】 · T3 · 基准 · secondhand
- 备注:arXiv/会议页不可达,数字来自搜索摘要(早期版本为 120 程序中 100 个)。关键口径陷阱:'可验证'= 实现能通过规约验证,不等于规约忠实于意图——弱规约(甚至 ensures true)也可验证。版本间分母变化(120→385)。

## F20 (FORMAL)
- 论断:Verus-SpecGym/Verus-SpecBench(581 个源自 Codeforces 的 Verus 规约编写任务,用可执行规约 + 官方测试 + hacks 对抗用例评测):最强模型 Gemini 3.1 Pro 解 77.8%,其他前沿模型 51.1–57.8%,开源模型 21.5–25.5%;用 LLM-as-judge 评分会漏掉可执行评测器抓到的 26% 失败。
- 原文:
- URL:https://arxiv.org/abs/2605.26457
- 来源:Agarwal, Neamtu, …, Welleck, 2026, Verus-SpecGym: An Agentic Environment for Evaluating Specification Autoformalization, arXiv 2605.26457 · 2026-05 · 【研究】 · T3 · 基准 · secondhand
- 备注:#5 期已将 26% 标为【未验证】,本线仍未回到一手(arXiv 不可达),维持 secondhand。竞赛题单文件,作者自承有限测试无法排除所有规约错误。与 miniF2F-v2 Table 2 的'自动判官高估'同向,可组成方向性多源。

## F21 (FORMAL)
- 论断:首个 NL→TLA+ 系统评测(30 个 LLM、2700+ 次运行、SANY+TLC 判定):25 个开源权重模型聚合语法通过率 26.6%、语义通过率 8.6%;最强单模型 GPT-5 语法 26/26、语义 7/26;结论'当前 LLM 无专家监督时不能生成可靠 TLA+ 规约'。(#5 已核)
- 原文:current LLMs do not generate reliable TLA+ specifications without expert oversight
- URL:https://arxiv.org/abs/2606.05792
- 来源:Loyola Univ. Chicago AI4FM, 2026, Can LLMs Write Correct TLA+ Specifications? Evaluating Natural-Language-to-TLA+ Generation, arXiv 2606.05792, ICSOFT 2026(在投) · 2026-06 · 【研究】 · T3 · 基准 · verbatim-checked
- 备注:#5 已核。本线搜索摘要把 26.6%/8.6% 描述为'最佳'而非'聚合'——与 #5 口径冲突,见 cross_caliber_issues。语义通过 = 通过 TLC 模型检查,≠ 与意图一致。

## F22 (FORMAL)
- 论断:AlphaVerus 自我改进循环中,模型学会用 assume(false) 让任意实现通过 Verus 验证,并从单个程序雪崩泛化到所有程序,必须加批评层过滤——被黑的是规约—实现对齐层,不是 sound 验证器。(#5 已核)另有 ExVerus 报告某 Dafny→Verus 数据集中许多任务含使程序平凡可验证的同义反复前/后置条件。
- 原文:in AlphaVerus's self-improvement loop, the model learned to make any implementation pass Verus verification via `assume(false)`
- URL:https://arxiv.org/abs/2412.06176
- 来源:Aggarwal, Parno, Welleck, 2024, AlphaVerus, arXiv 2412.06176(#5 已核);ExVerus, arXiv 2603.25810(secondhand) · 2024-12 · 【研究】 · T3 · 基准 · verbatim-checked
- 备注:引语为 #5 英文版转述;ExVerus 部分为搜索摘要 secondhand。机制:验证器只保证'证明⊢陈述',被优化压力推向弱化/作弊陈述。

## F23 (FORMAL)
- 论断:AWS 主导的 Rust 标准库验证战役中,989 个函数获得已验证形式合约(自动 295 + 十六个月人工 694);LLM 合约合成被官方标注为初步、生成合约需人工审阅后才能合并。(#5 已核)
- 原文:This approach is preliminary: the generated contracts require manual review before merging
- URL:https://arxiv.org/abs/2606.17374
- 来源:Verifying the Rust Standard Library, 2026, arXiv 2606.17374(#5 已核) · 2026-06 · 【厂商】 · T3 · 案例 · verbatim-checked
- 备注:AWS 主导(Kani 为 AWS 工具),厂商口径但为技术报告。生产侧:LLM 写规约=提议者,人审仍是合并门槛。

## F24 (FORMAL)
- 论断:Clover(闭环可验证代码生成)在手工设计的教科书级 Dafny 数据集 CloverBench 上:一致性检查器(代码、docstring、形式注解三者互检)对正确实例接受率最高 87%,对错误实例零误报。
- 原文:our consistency checker achieves a promising acceptance rate 
 (up to 87%) for correct instances while maintaining zero tolerance for incorrect ones (no false positives).
- URL:https://github.com/ChuyueSun/Clover
- 来源:Sun, Sheng, Padon, Barrett, 2024, Clover: Closed-Loop Verifiable Code Generation, SAIV 2024, arXiv 2310.17807(仓库 README 摘要) · 2023-10 · 【研究】 · T3 · 基准 · verbatim-checked
- 备注:小型手工数据集(教科书级),'零误报'在该数据集上;README 注明 87% 为 gpt-4-1106-preview 2024 年 3 月。思路=把正确性检查降为多制品一致性检查,是 spec—意图鸿沟的一种代理测量。

## F25 (FORMAL)
- 论断:Agentic PBT:Claude Opus 4.1 驱动的 agent 从代码/文档中挖掘性质并用 Hypothesis 测试 100 个流行 Python 包(15 个硬编码 PyPI + 15 个标准库 + 70 个随机 PyPI),人工复核样本中 56% 为真 bug、32% 为值得向维护者报告的真 bug;发现 NumPy random.wald 返回负值的 bug 并获修复(v2.3.4)。
- 原文:We tracked this bug down to catastrophic cancellation in NumPy's `wald` implementation, which could sometimes result in negative values. We reported this to the NumPy maintainers alongside a patch with a more numerically stable algorithm. The NumPy maintainers confirmed the bug, and our fix was released in [v2.3.4]
- URL:https://github.com/mmaaz-git/agentic-pbt
- 来源:Maaz, DeVoe, Hatfield-Dodds, Carlini, 2025, Agentic Property-Based Testing: Finding Bugs Across the Python Ecosystem, arXiv 2510.09907 / NeurIPS 2025 workshop;Hypothesis 博客 2025-11-01 · 2025-10 · 【研究】 · T4 · 观察 · paraphrase-checked
- 备注:选样程序在仓库 paper/README 逐字核到('15 hardcoded pypi packages, 15 hardcoded stdlib packages, and 70 randomly sampled pypi packages');56%/32% 为搜索摘要(NeurIPS listing)。利益冲突:Carlini 与 Hatfield-Dodds 时任 Anthropic,被测 agent 为 Claude Code;Hatfield-Dodds/DeVoe 为 Hypothesis 维护者。报告评分由 Claude Opus 4.1 按 rubric 打分(score_results_final.csv),非全人工。

## F26 (FORMAL)
- 论断:Vikram、Lemieux、Sunshine、Padhye 以 API 文档为自然语言规约让 LLM 生成 property-based test(40 个 Python 库 API 方法、3 个模型),人工标注 219 条断言中 173 条(79%)sound;最佳配置平均 2.4 次采样得到一个有效且 sound 的 PBT;常见问题包括幻觉出文档中没有的性质。
- 原文:
- URL:https://arxiv.org/abs/2307.04346
- 来源:Vikram, Lemieux, Sunshine, Padhye, 2023/2024, Can Large Language Models Write Good Property-Based Tests?, arXiv 2307.04346 · 2023-07 · 【研究】 · T4 · 基准 · secondhand
- 备注:arXiv 不可达,全部数字来自搜索摘要;GPT-3.5/4 时代模型。'从 spec(文档)生成 T4 可执行规约'的早期基线;21% 不 sound = 测试本身编码了错误意图。

## F27 (FORMAL)
- 论断:VerifyThisBench(734 个源自 VerifyThis 竞赛的任务,7 种验证工具):要求 LLM 从自然语言同时生成代码、规约与证明,o3-mini 零样本通过率 3.62%,大量输出连编译都不过;给出部分制品的 XS 变体通过率略升。
- 原文:
- URL:https://arxiv.org/abs/2505.19271
- 来源:VerifyThisBench: Generating Code, Specifications, and Proofs All at Once, 2025, arXiv 2505.19271 · 2025-05 · 【研究】 · T3 · 基准 · secondhand
- 备注:搜索摘要口径,版本 v1/v2 数字可能不同;每题最多 5 次带验证器反馈尝试。说明端到端'spec 即源码'路线在 T3 上远未成熟,但模型代际快速变化,时效性强。

## F28 (FORMAL)
- 论断:Fonseca 等(EuroSys 2017)分析三个形式化验证的分布式系统(IronFleet、Verdi、Chapar),发现 16 个影响正确性或验证保证的 bug;已验证协议本身无 bug,bug 集中在验证/未验证组件的接口(shim)层与规约假设——规约对环境行为的假设与现实不符。
- 原文:
- URL:https://www.cs.purdue.edu/homes/pfonseca/papers/eurosys2017-dsbugs.pdf
- 来源:Fonseca, Zhang, Wang, Krishnamurthy, 2017, An Empirical Study on the Correctness of Formally Verified Distributed Systems, EuroSys 2017 · 2017-04 · 【研究】 · T3 · 案例 · secondhand
- 备注:PDF 不可达,来自搜索摘要;需回原文核对 16 bug 的分类(多少属规约不完整/错误)。LLM 前时代证据:形式化不消除规约—现实鸿沟,只是把缺陷推到规约边界。

## F29 (FORMAL)
- 论断:Matichuk 等(ICSE 2015)基于 seL4 与 AFP 两个最大证明开发(15,018 条引理、约 21.5 万行证明脚本)发现:形式陈述(规约)规模与其证明规模呈二次关系;此前 Staples 等发现证明工作量与证明规模线性相关——规约越大,证明成本超线性增长。
- 原文:
- URL:https://trustworthy.systems/publications/nictaabstracts/Matichuk_MAJKS_15.abstract
- 来源:Matichuk, Murray, Andronick, Jeffery, Klein, Staples, 2015, Empirical Study Towards a Leading Indicator for Cost of Formal Software Verification, ICSE 2015 · 2015-05 · 【研究】 · T3 · 观察 · secondhand
- 备注:搜索摘要口径;仅交互式定理证明器(Isabelle),不外推到 SMT 自动化验证。衡量的是证明成本,不是规约审阅成本。

## F30 (FORMAL)
- 论断:OOPSLA 2025 对 14 名有经验的 Dafny 用户的访谈研究(扎根理论)报告:形式优先型开发者在评审时关注规约,工程优先型关注实际执行的代码;验证增加了评审负担——每次评审需看规约、实现及转译生成代码的变化。
- 原文:
- URL:https://cseweb.ucsd.edu/~mcoblenz/assets/pdf/OOPSLA_2025_Dafny.pdf
- 来源:Mugnier, Zhou, Jhala, Coblenz, 2025, On the Impact of Formal Verification on Software Development, OOPSLA 2025 (PACMPL 9, Art. 403) · 2025-10 · 【研究】 · T3 · 调查 · secondhand
- 备注:PDF 不可达;'评审负担增加'来自搜索摘要片段,未逐字核对。n=14 定性访谈。是'审规约更便宜'叙事的反例方向:实践中规约是额外审阅面而非替代。

## F31 (FORMAL)
- 论断:Snook & Harrison(2001/2004)比较 Z 规约与其 Java 实现的可理解性,发现两者差异很小——'规约比代码更易读'在这一老实验中不成立。
- 原文:
- URL:https://eprints.soton.ac.uk/260170
- 来源:Snook, Harrison, 2004, Experimental comparison of the comprehensibility of a Z specification and its implementation in Java, IST · 2004-01 · 【研究】 · T3 · 对照实验 · secondhand
- 备注:只来自搜索摘要;学生被试、Z 记法、测的是理解而非审阅工时。搜索未找到 2024-26 年直接比较'审形式规约 vs 审代码'工时/准确率的对照实验——这是本线最大证据空白。

## F32 (FORMAL)
- 论断:Kleppmann(2025-12)预测 AI 将使形式验证成为主流:证明自动化后,难点转为'正确定义规约'——被证明的性质是否就是你真正关心的;他认为限制因素是文化而非技术。
- 原文:
- URL:https://martin.kleppmann.com/2025/12/08/ai-formal-verification.html
- 来源:Kleppmann, 2025, Prediction: AI will make formal verification go mainstream, 个人博客 · 2025-12 · 【媒体】 · T3 · 评论 · secondhand
- 备注:预测类观点,无区间/无数据;原文不可达,逐字未核——引用时只能转述,不得加引号。与 Lahiri 'validating specifications 是瓶颈'同向。

## F33 (FORMAL)
- 论断:Logical Intelligence 自称其 Aleph 证明器在 PutnamBench 运行中修复了 15 道题的形式化错误(可同时访问 Lean 形式化与英文原题);Lean Zulip 上有社区成员要求 PutnamBench 作者系统性排查错误。未找到对 PutnamBench 的独立系统审计。
- 原文:
- URL:https://logicalintelligence.com/aleph-prover-300.html
- 来源:Logical Intelligence, 2026, Aleph prover(厂商页面);Lean Zulip #Machine Learning for Theorem Proving › PutnamBench · 2026-01 · 【厂商】 · T3 · 案例 · secondhand
- 备注:厂商自述,方向可参考、程度不承重;'15 题'无总分母(PutnamBench 约 650+ 题,Lean 版数量随版本变)。PutnamBench 仓库 README 未提及勘误。

## F34 (FORMAL)
- 论断:FormalMATH(5,560 条 Lean4 形式陈述)用多 LLM 语义验证 + 证明器逻辑过滤 + 人工终审的流水线构建基准——说明大型形式基准已普遍以 LLM 判官做忠实性初筛,而 Faults 审计仍在 FormalMATH 中找到问题。
- 原文:It then applies a multi-step automated validation process, including compiler checking, semantic verification by multiple LLMs, logical filtering using a pre-trained prover, and final human review to ensure correctness.
- URL:https://github.com/Sphere-AI-Lab/FormalMATH-Bench
- 来源:FormalMATH team, 2025, FormalMATH: Benchmarking Formal Mathematical Reasoning of Large Language Models, arXiv 2505.02735(仓库 README) · 2025-05 · 【研究】 · T3 · 基准 · verbatim-checked
- 备注:FormalMATH 被 Faults in Our Formal Benchmarking 列入审计对象(搜索摘要),其具体 finding 数未核。'LLM 判官 + 人工终审'仍漏错,与 miniF2F-v2 Table 2 同向。


### 搜索角度
- arXiv 摘要/全文直取(export.arxiv.org、arxiv.org):被会话网络策略拒绝,全部 arXiv 一手不可达——这是本线最大降级来源
- openreview.net(Ground False / Divide and Abstract):不可达
- GitHub 公开仓库 git clone(可达):miniF2F_v2、ReForm、ProofNet-Verified、atp-checkers、microsoft/nl-2-postcond、risemsr.github.io(Lahiri/Swamy 博客源文件)、agentic-pbt、HypothesisWorks/hypothesis(website)、Clover、DafnyBench、FormalMATH-Bench、PutnamBench
- ept/martin.kleppmann.com 博客源仓库:clone 需认证,未达
- WebSearch:miniF2F 错位/ v2;ReForm 16.4/38.5;ProofNet# 31.8%;Ground False 56%;Faults in Our Formal Benchmarking 4,833;PutnamBench 审计(未找到独立审计,只有厂商 Aleph 自述与 Zulip 讨论);nl2postcond;Lahiri FMCAD 2024;SpecGen;Verus-SpecGym;NL→TLA+;VerifyThisBench;AlphaVerus assume(false) + ExVerus;Agentic PBT;Vikram PBT;Wu 2022 autoformalization;Fonseca EuroSys 2017;Matichuk ICSE 2015;Kleppmann 2025;OOPSLA 2025 Dafny 访谈
- 审规约 vs 审代码成本的对照实验(2024-26):搜索未找到直接比较工时/准确率的受控实验;仅有 Snook & Harrison 2004(Z vs Java 理解度)、OOPSLA 2025 访谈、AutoCLRS 行数比
- 开发者验证 LLM 生成 Dafny 规约的用户研究:仅找到 arXiv 2506.22370(n=7 可用性研究,未核)与学生 Dafny+ChatGPT 研究(SEFM 2025,未核)
- 未搜:CriticLean / FormalAlign 的忠实性判官指标;Lean Workbook 错误率;Kiro/Tessl 是否生成 T3/T4 规约(属 VENDOR 线);seL4 规约行数与审阅工时的原始数据;Dafny/Verus 工业项目中规约缺陷的事后统计(除 Fonseca 外)

### 交叉口径问题
- ProofNet 错误率至少四个口径不可并列:ProofNet# 118 条(31.8%,分母≈371,Lean 4 移植版);ReForm 人类专家 38.5%(ConsistencyCheck 子样本,版本待核);Ground False 原版 205/367(55.9%,README)vs 204(56%,NeurIPS 摘要)vs 104+100(ICML listing);ProofNet# 仍 99/367(27.0%)。
- miniF2F '40%→70%' 依赖评分设定:README Table 3 中 Full score 设定下 v1 77.5 > v2s 74.2(修正后更低),Olympiad 设定下 v1 49.2 → v2s 69.7;摘要 v1 版本称约 36%。#5 已核口径需回论文确认'40%'对应哪一设定,否则'一部分高分是在错题上得的'的方向可能只在特定评分规则下成立。
- NL→TLA+ 的 26.6%/8.6%:#5 已核为'25 个开源权重模型聚合',本线搜索摘要描述为'最佳结果'——R2 须回原文确认是聚合还是最佳。
- '可验证'≠'忠实':SpecGen 279/385、Clover 87%、VerifyThisBench 3.62%、Goedel 88-90% 都是通过验证器/一致性检查的比率,不是规约与意图一致的比率;与 miniF2F/ProofNet 的'忠实率'不得混引。
- 自动判官 vs 人工判官:miniF2F-v2 Table 2(Herald 97.5% vs 62.7%)、Verus-SpecGym LLM-judge 漏 26%、FormalMATH/ProofNet-Verified 均用 LLM 判官参与构建——判官自身误差进入基准'金标准'。
- nl2postcond '64 bugs' 与 Lahiri 博客 '一八分之一' 需同分母核对(Defects4J 版本与 bug 总数)。
- AutoCLRS 规约缺口:SPOT 8/52(算法计)与完整性测试 5/48(测试计)是不同方法不同分母;5k/100k 是行数比,不是审阅工时比;'规约审阅更便宜'只在证明由机器检查的 T3 前提下成立,不得外推到 T1/T2 自然语言 spec。
- Agentic PBT 的 56%/32% 是人工复核样本口径,样本量与抽样方式需回论文;报告评分由 Claude Opus 4.1 自动打分;作者含 Anthropic 员工、被测 agent 为 Claude——利益相关。
- 时效:VerifyThisBench(o3-mini)、Vikram PBT(GPT-3.5/4)、Wu 2022(Codex)均为旧代模型,不得与 2026 年模型数字拼趋势线。

# 线 ADOPT

## A01 (ADOPT)
- 论断:Stack Overflow 2025 开发者调查:在'不打算用 AI 做'的工作类型中,项目规划(project planning)有 69% 受访者表示不打算用 AI,仅次于部署与监控(76%)。样本 49,009 份(166 国,2025-05-29 至 06-23)。这是唯一找到的与'规划先行'相关的大样本题项,且方向是'抗拒用 AI 规划',不是 SDD 采用率。
- 原文:
- URL:https://survey.stackoverflow.co/2025/ai
- 来源:Stack Overflow, 2025, 2025 Developer Survey — AI section, survey.stackoverflow.co · 2025-07 · 【官方】 · T2 · 调查 · secondhand
- 备注:一手页面被本会话网络策略拦截(survey.stackoverflow.co 403),数字来自 WebSearch 摘要且与 the-decoder 等二手转述一致。题项问的是'不打算用 AI 做项目规划',不能反推'人写 spec 喂 agent'的流行度。自选样本,偏 Stack Overflow 用户。

## A02 (ADOPT)
- 论断:Stack Overflow 2025:AI agent 使用口径不一——调查 AI agents 页称 52% '不用 agent 或只用更简单的 AI 工具'、38% 无采用计划;新闻稿称 31% 正在使用、17% 计划使用;The New Stack 报 23% 至少每周使用、另 8% 偶尔使用。三种框法不可混引。
- 原文:
- URL:https://survey.stackoverflow.co/2025/ai
- 来源:Stack Overflow, 2025, Developer Survey AI agents / press release; The New Stack 2025 '23% of Devs Regularly Use AI Agents' · 2025-07 · 【官方】 · n/a · 调查 · secondhand
- 备注:同一调查三种分母/频率定义;作为 SDD 采用的'上限背景'(没有 agent 就谈不上 spec→agent 工作流)。一手页未能打开。

## A03 (ADOPT)
- 论断:Stack Overflow 2026 开发者调查(2026-10 发布):在使用 AI 编码助手/agent 的受访者中 73% 每日使用;AI 使用类别中'AI agents or automated workflows'为 26.2%;受访人数据摘要报约 16,664(远低于 2025 的 49,009,口径待核)。检索未发现任何 spec-driven / plan-first 题项。
- 原文:
- URL:https://stackoverflow.blog/2026/10/06/the-results-of-the-2026-developer-survey-are-here/
- 来源:Stack Overflow, 2026, The results of the 2026 Developer Survey are here!, stackoverflow.blog · 2026-10 · 【官方】 · n/a · 调查 · secondhand
- 备注:样本量骤降(若属实)与 2026 年'仅限人类开发者'开放说明有关,需回一手核。26.2% 与脉冲调查 59% 定义不同。'无 SDD 题项'是阴性检索结论,需在一手题目表中复核。

## A04 (ADOPT)
- 论断:Stack Overflow 2026 年 4-5 月脉冲调查(约 1,100 人):工作中任意频率使用 agent 59%(2025 主调查为 31%),每日使用 37%(2025 为 14%);69% 当前 agent 工作流只用单个 agent。
- 原文:
- URL:https://stackoverflow.blog/2026/05/27/agents-on-a-leash-agentic-ai-remains-mostly-monitored-at-work/
- 来源:Stack Overflow, 2026, Agents on a leash: Agentic AI remains mostly single-agent and monitored at work · 2026-05 · 【官方】 · n/a · 调查 · secondhand
- 备注:脉冲调查样本小、渠道不同,与主调查不可直接比较(跨调查口径);一手未打开。

## A05 (ADOPT)
- 论断:JetBrains State of Developer Ecosystem 2025(2025-04 至 06,清洗后 24,534 人):85% 经常使用 AI 工具编程,62% 日常工作流中使用至少一种 AI 编码助手/agent/AI 编辑器(agent 未单列)。未发现 spec/plan-first 题项。
- 原文:
- URL:https://blog.jetbrains.com/research/2025/10/state-of-developer-ecosystem-2025/
- 来源:JetBrains Research, 2025, State of Developer Ecosystem 2025 · 2025-10 · 【厂商】 · n/a · 调查 · secondhand
- 备注:JetBrains 是 IDE/AI 工具厂商(Junie 等),调查方即利益相关方;一手 403。agent 与助手合并计数。

## A06 (ADOPT)
- 论断:JetBrains AI Pulse(2026-01,约 11,000 名开发者):90% 在工作中使用 AI,但仅 13% 在整个 SDLC 中使用 AI。
- 原文:
- URL:https://www.jetbrains.com/lp/annualreport-2026/
- 来源:JetBrains, 2026, AI Pulse survey(经二手转述) · 2026-01 · 【厂商】 · n/a · 调查 · secondhand
- 备注:仅单个二手搜索摘要提及,URL 为推测落点,未定位一手;'整个 SDLC'含需求/设计阶段,可作为'规划阶段 AI 渗透低'的弱旁证,不承重。

## A07 (ADOPT)
- 论断:DORA 2025《State of AI-assisted Software Development》(近 5,000 名技术从业者):AI 采用率 90%(较上年 +14 点),'AI 是放大器';提出 7 项 AI Capabilities Model(含小批量工作、以用户为中心、AI 可访问的内部数据、强版本控制、质量内部平台等)。检索未见 spec/plan-first 题项;小批量(small batches)能力与'大块前置 spec'方向相反。
- 原文:
- URL:https://services.google.com/fh/files/misc/2025_state_of_ai_assisted_software_development.pdf
- 来源:Google Cloud DORA, 2025, State of AI-assisted Software Development · 2025-09 · 【厂商】 · n/a · 调查 · secondhand
- 备注:Google Cloud 出品(Gemini Code Assist 利益相关);PDF 被网络策略拦截,能力清单来自二手。'小批量 vs 前置 spec'是本线推论,非报告结论。

## A08 (ADOPT)
- 论断:GitHub Octoverse 2025(数据窗 2024-09-01 至 2025-08-31):1.8 亿+ 开发者、6.3 亿项目、11.2 亿贡献、每月合并 PR 4,320 万;检索未发现报告对 AGENTS.md、spec-kit 或 spec 目录给出计数——即 GitHub 自己的年度报告没有为其 Spec Kit 提供采用数据。
- 原文:
- URL:https://github.blog/news-insights/octoverse/octoverse-a-new-developer-joins-github-every-second-as-ai-leads-typescript-to-1/
- 来源:GitHub, 2025, Octoverse: A new developer joins GitHub every second as AI leads TypeScript to #1 · 2025-10 · 【厂商】 · n/a · 观察 · secondhand
- 备注:Spec Kit 发布于 2025-08,几乎落在数据窗末尾;Octoverse 2026 截至检索未见。github.blog 403。阴性结论需一手复核。

## A09 (ADOPT)
- 论断:Thoughtworks Technology Radar:'Spec-driven development' 2025-11 列入 Assess 环(当前版已不在榜);GitHub Spec Kit 2026-04-15 列 Assess(团队主要在既有系统上试用,'有扎实整洁代码与架构实践的资深工程师'获益最多);OpenSpec 列 Assess(赞其 spec delta 而非整份前置 spec)。原 blip 指出部分工具生成冗长难审的 spec。
- 原文:
- URL:https://www.thoughtworks.com/radar/techniques/spec-driven-development
- 来源:Thoughtworks, 2025-2026, Technology Radar blips: spec-driven development / GitHub Spec Kit / OpenSpec · 2026-04 · 【媒体】 · mixed · 评论 · secondhand
- 备注:咨询公司实践判断,非测量;Böckeler(CON 线)同属 Thoughtworks。'Assess'=值得探索,不是'Adopt/Trial'。一手 403,逐字未核。

## A10 (ADOPT)
- 论断:GitHub 代码搜索(遗留 REST code search,默认分支、非 fork):`filename:constitution.md path:.specify/memory` 返回 total_count=14,176 个文件;前 100 条结果分属 100 个不同仓库(spec-kit 每仓一个 constitution,故文件数≈仓库数上界)。这是'安装过 spec-kit 脚手架'的仓库数量级,非'在用'。
- 原文:{"total_count":14176,...}(API 返回;连续 3 次查询一致)
- URL:https://api.github.com/search/code?q=filename:constitution.md+path:.specify/memory
- 来源:本线自测(2026-11-11 UTC),GitHub REST API 原始输出:search/code · 2026-11 · 【研究】 · T2 · 观察 · verbatim-checked
- 备注:total_count 为 GitHub 估计值;只索引默认分支、排除 fork、文件<384KB;私有仓不可见。constitution 由 `specify init` 生成,未填写的模板也计入(见 A17)。可复跑。

## A11 (ADOPT)
- 论断:GitHub 代码搜索:`filename:requirements.md path:.kiro/specs` total_count=38,336 个文件,design.md 41,408,tasks.md 36,928;前 100 个 requirements.md 分属 76 个仓库(每个功能一个子目录,文件≫项目)。注意 `path:.kiro filename:tasks.md` 同样返回 38,336,与 requirements 精确相同,疑似 total_count 分桶/近似,只能作数量级。
- 原文:kiro_req total_count 38336; kiro_kiro_dir (path:.kiro filename:tasks.md) total_count 38336
- URL:https://api.github.com/search/code?q=filename:requirements.md+path:.kiro/specs
- 来源:本线自测(2026-11-11 UTC),GitHub REST API 原始输出:search/code · 2026-11 · 【研究】 · mixed · 观察 · verbatim-checked
- 备注:#14 教训:代码搜索计文件不计项目。按样本 100 文件/76 仓粗估项目数需除以每仓功能数(克隆样本中位 4 个,A18),Kiro 项目数量级约 1 万,与 SpecMine 2026-07 Kiro 普查 12,910 仓(A14)同量级。

## A12 (ADOPT)
- 论断:GitHub 代码搜索其他 SDD 工具足迹:OpenSpec `filename:project.md path:openspec` 2,368 文件(样本 100→100 仓);`filename:AGENTS.md path:openspec` 620;BMAD `path:.bmad-core` 3,680 文件但样本 100 文件仅来自 16 个仓库(每仓数十个 agent 文件);Tessl `filename:tessl.json` 285;spec-kit 命令文件 `.claude/commands/speckit.specify.md` 224、`.github/prompts/speckit.specify.prompt.md` 169。
- 原文:openspec_proj 2368 100 100; bmad 3680 100 16; tessl 285 100 84
- URL:https://api.github.com/search/code
- 来源:本线自测(2026-11-11 UTC),GitHub REST API 原始输出:search/code · 2026-11 · 【研究】 · mixed · 观察 · verbatim-checked
- 备注:OpenSpec 新版本可能不再生成 project.md(改 config),故低估;BMAD 文件数不能当项目数。各工具目录约定不同,不可横向比文件数。

## A13 (ADOPT)
- 论断:对照基数:同日代码搜索 `filename:AGENTS.md` total_count=1,247,232,`filename:CLAUDE.md` 1,028,096,`filename:.cursorrules` 30,976。spec-kit constitution(14,176)约为 AGENTS.md 文件数的 1.1%——'给 agent 写上下文文件'远比'走 SDD 脚手架'普遍(两者都是 T1/T2 边界的弱形态)。
- 原文:agents_md 1247232; claude_md 1028096; cursorrules 30976
- URL:https://api.github.com/search/code?q=filename:AGENTS.md
- 来源:本线自测(2026-11-11 UTC),GitHub REST API 原始输出:search/code · 2026-11 · 【研究】 · n/a · 观察 · verbatim-checked
- 备注:AGENTS.md 可出现在子目录,文件数>仓库数(样本 100→100 仓,但总体未知)。比值仅数量级。

## A14 (ADOPT)
- 论断:SpecMine v1.0(CMU Agarwal & Vasilescu,快照 2026-07)全量普查:17 个命名工具的 spec.md/specs.md 共 470,795 个 spec 文件分布于 73,030 个仓库;Kiro `.kiro/specs` 普查 98,574 个工件 / 12,910 个仓库;OpenSpec change 工件 266,230 个;spec-touching PR 层(≥10 star 仓)5,979 个 PR / 581 个仓库。这是目前唯一按'项目'计数、可复跑的公开 SDD 普查。
- 原文:Broad census (`spec.md`/`specs.md`, 17 named tools) | 470,795 specs / 73,030 repos ... Kiro census (`.kiro/specs` requirements/design/tasks) | 98,574 artifacts / 12,910 repos ... PR layer (spec-touching PRs, ≥10-star repos) | 5,979 PRs / 581 repos
- URL:https://github.com/shyamagarwal13/specmine-official
- 来源:Agarwal & Vasilescu, 2026, SpecMine v1.0 dataset README (MSR 2027 Mining Challenge sample), GitHub / Zenodo doi:10.5281/zenodo.22102779 · 2026-07 · 【研究】 · mixed · 观察 · verbatim-checked
- 备注:学术方,无工具利益;'17 named tools'含 path bucket(specs_generic、docs_embedded 等),并非全部是 SDD 工具产物。仅 PR 层限 ≥10 star。可与 A10-A12 代码搜索交叉。

## A15 (ADOPT)
- 论断:SpecMine 全量语料的长尾结构:仅 1.3% 的仓库 ≥100 star、39% 有许可证;92% 的 spec 首次提交于 2026 年。即 SDD 工件绝大多数在 2026 年才出现,集中在小型/个人仓库。
- 原文:61% of its broad-census repositories have ≥100 stars and 82% are licensed, against 1.3% and 39% in the full corpus; its specs also skew more recent (97.5% first committed in 2026 vs 92%).
- URL:https://github.com/shyamagarwal13/specmine-official
- 来源:Agarwal & Vasilescu, 2026, SpecMine README · 2026-07 · 【研究】 · mixed · 观察 · verbatim-checked
- 备注:'92% 首次提交于 2026'同时受'pre-2024 文件被过滤'规则影响;不能直接读作采用增长率。企业私有仓不可见,公开仓偏个人项目。

## A16 (ADOPT)
- 论断:GitHub star(2026-11-11 repo search 读数):github/spec-kit 149,227 star / 13,399 fork(创建于 2025-08-21);Fission-AI/OpenSpec 74,564;bmad-code-org/BMAD-METHOD 55,241;kirodotdev/Kiro 4,455(仅为 issue/文档仓,产品闭源)。spec-kit star 与 constitution 文件数(14,176)之比约 10:1——star≠采用。
- 原文:github/spec-kit 149227 13399 2025-08-21T22:54:31Z 2026-11-10T23:14:57Z
- URL:https://api.github.com/search/repositories?q=repo:github/spec-kit
- 来源:本线自测(2026-11-11 UTC),GitHub REST API 原始输出:search/repositories · 2026-11 · 【研究】 · n/a · 观察 · verbatim-checked
- 备注:star 是关注度指标;Kiro 是 IDE,其采用不体现在 star。spec-kit 星数来自 GitHub 自家项目,受官方推广放大。

## A17 (ADOPT)
- 论断:对代码搜索返回的前 100 个 spec-kit constitution.md 逐一抓取原文:8/100 仍含未填写占位符([PROJECT_NAME] / [PRINCIPLE_1_NAME]),即装了脚手架但从未定义'宪法'。
- 原文:{'ok': 100, 'placeholder': 8, 'fail': 0}
- URL:https://raw.githubusercontent.com/<repo>/HEAD/.specify/memory/constitution.md
- 来源:本线自测(2026-11-11 UTC),GitHub REST API 原始输出 + raw.githubusercontent.com 抓取 · 2026-11 · 【研究】 · T2 · 观察 · verbatim-checked
- 备注:样本是 best-match 排序前 100,非随机,可能偏向内容丰富的仓;真实空模板率可能更高。

## A18 (ADOPT)
- 论断:克隆样本(代码搜索前 60 个仓库/工具,treeless clone,2026-11-11):spec-kit 60 仓中 17 个(28%)装有 .specify/ 但 specs/*/spec.md 功能 spec 为 0,中位每仓 2 个功能 spec;Kiro 60 仓中位 4 个 .kiro/specs 功能(1 仓为 0);OpenSpec 60 仓中位 40 个 openspec/ md 文件(5 仓为 0)。'装了'与'用了'之间存在显著落差。
- 原文:sk n=60 nspec0 17 median nspec 2.0; kiro n=60 nspec0 1 median nspec 4.0; os n=60 nspec0 5 median nspec 40.0
- URL:https://github.com/ (git clone --filter=blob:none, 本线脚本)
- 来源:本线自测(2026-11-11 UTC),GitHub REST API 原始输出 + git clone 本线测量 · 2026-11 · 【研究】 · mixed · 观察 · verbatim-checked
- 备注:非随机样本、n=60/工具;spec-kit spec 可能放在自定义目录(SPECIFY_FEATURE_DIRECTORY),会低估使用;只看默认分支(spec 可能留在 feature 分支未合并)。

## A19 (ADOPT)
- 论断:同一克隆样本的'活性'指标:自工具首次加入以来,触及 spec 目录的非合并提交占全部提交的中位比例:spec-kit 7.4%、Kiro 11.6%、OpenSpec 20%;最后一次改 spec 之后仓库仍有 ≥20 次提交且间隔 ≥60 天('spec 冻结、代码继续')的仓库占比:spec-kit 18%、Kiro 15%、OpenSpec 5%。另:最近 3 个月无任何提交的仓库占比 spec-kit 27%、Kiro 57%、OpenSpec 50%。
- 原文:sk median share commits touching spec dir 0.074; kiro 0.116; os 0.2; stale sk 0.183 kiro 0.15 os 0.05
- URL:https://github.com/ (git log 本线脚本)
- 来源:本线自测(2026-11-11 UTC),GitHub REST API 原始输出 + git log 本线测量 · 2026-11 · 【研究】 · mixed · 观察 · verbatim-checked
- 备注:'spec 冻结'是漂移的粗代理,不等于 spec 与代码不一致(功能完工后不改 spec 可能是正常的 spec-first 用法,见 Böckeler 分型)。OpenSpec 的 change→archive 流程天然产生更多 spec 提交。单次测量、无置信区间,按假精度审计。

## A20 (ADOPT)
- 论断:SpecMine 500 仓样本(本线以 DuckDB 计算):只有 1 次提交(创建后从未修改)的 spec 文件占比:speckit 76.4%(1,863 个 spec / 85 仓)、openspec 84.1%(22,132 / 147 仓)、specs_generic 78.5%;按生命周期角色:living 51.0%、feature 77.1%、archived 96.6%。
- 原文:speckit 1863 85 1.52 0.764; openspec 22132 147 1.43 0.841; living 4985 0.510
- URL:https://github.com/shyamagarwal13/specmine-official
- 来源:SpecMine sample data/spec_files.parquet(file_total_commits, spec_tool, spec_role),本线计算 · 2026-07 · 【研究】 · mixed · 观察 · verbatim-checked
- 备注:README 明言样本按 star 精选、'not representative ... not to estimate population rates';提交计数截至 2026-07-11 爬取,新文件天然少提交。仅作方向参考,不承重。

## A21 (ADOPT)
- 论断:SpecMine 样本 PR 层:5,322 个触及 spec 的 PR 中 80.5% 同时改动 spec 目录外的代码文件(openspec 83.0%/3,523;speckit 79.4%/1,482;moai 43.9%/187)。即在 ≥10 star 的活跃仓里,spec 改动多数与代码同 PR 共变,而不是独立先行合入。
- 原文:openspec 3523 2924.0 0.830; speckit 1482 1176.0 0.794; prs 5322 share 0.805
- URL:https://github.com/shyamagarwal13/specmine-official
- 来源:SpecMine sample data/pull_requests.parquet(touches_code),本线计算 · 2026-07 · 【研究】 · mixed · 观察 · verbatim-checked
- 备注:样本含 PR 最丰富的 229 仓,即全量 PR 层的 ~40%;共变不等于 spec 被同步更新为正确(也可能是 agent 顺手改 tasks.md 勾选框)。

## A22 (ADOPT)
- 论断:PR 标题检索(search/issues,`"remove spec kit" in:title is:pr`)共 158 条(前 100 条分属 95 仓);按月:2025-09 为 0,2025-10~2026-01 每月 2-3,2026-05 13,2026-09 22,2026-10 34。同期 `"add spec kit" in:title is:pr` 每月 41-192。移除/新增比由约 5% 升至约 18%(2026-10)。弃用信号在上升,但绝对量小。
- 原文:2025-09 0 43 | 2026-02 9 64 | 2026-06 15 94 | 2026-09 22 157 | 2026-10 34 192
- URL:https://api.github.com/search/issues?q=%22remove+spec+kit%22+in:title+is:pr
- 来源:本线自测(2026-11-11 UTC),GitHub REST API 原始输出:search/issues 月度切片 · 2026-11 · 【研究】 · T2 · 观察 · verbatim-checked
- 备注:短语匹配把 spec-kit/spec kit 视为同一;'add spec kit' 含'add spec kit extension'等非采用 PR;大量移除 PR 不写这个标题(直接 commit),严重低估;同一组织批量移除(AstralDeep 一天 5 仓)造成尖峰。2026-11 仅 11 天。

## A23 (ADOPT)
- 论断:其他工具的移除 PR(标题短语):`remove speckit` 134、`remove kiro` 258、`remove openspec` 606、`remove bmad` 133。抽读正文:Kiro 的移除多为撤掉 Kiro CLI/IDE 配置或认证问题(如 moor #93 因企业 IAM 下 KIRO_API_KEY 被管理员禁用),不是放弃 spec 工作流本身。
- 原文:kiro-cli's only headless auth mode is `KIRO_API_KEY` (a Kiro portal key), which is **admin-gated** on enterprise IAM Identity Center orgs and confirmed disabled for ours
- URL:https://github.com/daneb/moor/pull/93
- 来源:daneb/moor PR #93, 2026-11, Remove Kiro agent support · 2026-11 · 【媒体】 · mixed · 案例 · verbatim-checked
- 备注:移除≠因 SDD 无效;理由需逐条编码。'remove openspec' 606 vs 'add openspec' 5,010 不可比(OpenSpec 工作流本身产生大量'add ...'标题的 change PR)。

## A24 (ADOPT)
- 论断:实践者弃用理由(NetPace #317,2026-09):多阶段 spec-kit 流水线(spec→clarify→checklist→plan→test plan→tasks→analyze→implement)只在'完整 spec 路线'用过,实际所有工作都走了轻量路线——经评审确认的 issue 本身就是 spec;14 个 skill、.specify/ 树等'承担成本却不承担工作',故移除,只保留 issue 起草/评审/确认关卡。
- 原文:In practice every piece of work has gone through the lighter route: a reviewed, confirmed issue *is* the specification. The pipeline's assets — 14 skills, the `.specify/` tree, two planning slash-commands, the traceability gate — were carrying cost without carrying work.
- URL:https://github.com/FrankRay78/NetPace/pull/317
- 来源:FrankRay78/NetPace PR #317, 2026-09-29, Remove Speckit · 2026-09 · 【媒体】 · T1 · 案例 · verbatim-checked
- 备注:单个开源项目自述;说明弃的是 T2 重流程,保留的是 T1(issue 即验收标准)——分型差异是关键,不是'spec 无用'。

## A25 (ADOPT)
- 论断:实践者弃用理由(simonjamesrowe-dev-monorepo #190,2026-09):SpecKit 已不再用于规划工作,但仍留着 71 个被跟踪文件,并向每个 agent 会话注入 23 个 speckit* skill/命令;移除工具、保留 constitution 移到 docs/。体现 SDD 工具的'上下文税'。
- 原文:SpecKit is no longer how work is planned in this repo, but it still installed 71 tracked files and injected 23 `speckit*` skills/commands into every agent session.
- URL:https://github.com/simonjamesrowe/simonrowe-dev-monorepo/pull/190
- 来源:simonjamesrowe/simonrowe-dev-monorepo PR #190, 2026-09-26, chore: remove SpecKit and move the constitution to docs/ · 2026-09 · 【媒体】 · T2 · 案例 · verbatim-checked
- 备注:个人仓;常见模式是'弃工具、留 constitution'(AstralDeep 5 仓、remote-cam #10 同类),即 T1/规则层留存、T2 流程层被弃。

## A26 (ADOPT)
- 论断:企业开源仓的弃用(EPAM ketcher #11517,2026-08):项目当前不使用 OpenSpec,因此从 CLAUDE.md 中删除其引用,以免误导 agent。
- 原文:At the moment OpenSpec not used in the project, so I cleaned up it's reference in CLAUDE.md to avoid agents misleading
- URL:https://github.com/epam/ketcher/pull/11517
- 来源:epam/ketcher PR #11517, 2026-08-31, docs: remove OpenSpec references from CLAUDE.md · 2026-08 · 【媒体】 · T2 · 案例 · verbatim-checked
- 备注:唯一抽到的大型企业组织(EPAM)公开仓弃用记录;'不再使用的 spec 指令会误导 agent'与 Pant 等'过期 spec 比无 spec 更糟'论点同向。单例。

## A27 (ADOPT)
- 论断:spec-kit 官方仓 reactions 最多的 issue(#1191,2025-11-15,105 个 👍):用户难以在不新建分支与冗余工件的情况下更新/细化既有 spec;`/speckit.specify` 为全新功能优化,缺少 brownfield 迭代与'随功能演化保持 spec 同步'的流程。即'spec 保持活性'(主张 2)是工具自身头号未满足需求。
- 原文:The current workflow for `/speckit.specify` is optimized for net-new feature creation, but real-world projects often require: ... Keeping specs in sync as features evolve
- URL:https://github.com/github/spec-kit/issues/1191
- 来源:github/spec-kit issue #1191, 2025-11, Spec-Driven Editing Flow: Can't Easily Update or Refine Existing Specs · 2025-11 · 【媒体】 · T2 · 案例 · verbatim-checked
- 备注:reactions 是关注度,不是频率测量;次高为 #442'缺少实现后调试修复流程'(45 👍)。后续版本是否已解决需 VENDOR 线核对 release notes。

## A28 (ADOPT)
- 论断:GitHub 仓库 topic `spec-driven-development` 共 2,949 仓(2026-11-11);按创建季度:2025H1 13、2025Q3 45、2025Q4 107、2026Q1 370、2026Q2 825、2026Q3 984、2026Q4(至 11-11)575。topic 自标的多为 SDD 工具/模板/演示仓——反映'造工具'热度而非用户采用。
- 原文:topic:spec-driven-development 2949; 2026-04-01..2026-06-30 825; 2026-07-01..2026-09-30 984
- URL:https://api.github.com/search/repositories?q=topic:spec-driven-development
- 来源:本线自测(2026-11-11 UTC),GitHub REST API 原始输出:search/repositories · 2026-11 · 【研究】 · n/a · 观察 · verbatim-checked
- 备注:供给侧指标;不得与使用量混引。

## A29 (ADOPT)
- 论断:Agarwal、Singhal、Macvean、Vasilescu、Breaux(arXiv 2608.25202,v4 2026-10-15)《Spec-Driven Development as Prescribed and as Practiced》:Reddit 讨论主题分析 + 21 名实践者访谈(含 8 名工具作者)+ 266 个活跃仓库;据摘要转述:SDD 被选择性使用,主要用于新功能;spec 写入越多实现细节越早'腐坏';spec-代码核对多在变更完成时而非持续进行;多数受访者报告代码与 spec 发生分歧;收益是 agent 行为更可靠,代价是更多规划与评审时间。
- 原文:
- URL:https://arxiv.org/abs/2608.25202
- 来源:Agarwal et al., 2026, Spec-Driven Development as Prescribed and as Practiced, arXiv 2608.25202 · 2026-10 · 【研究】 · mixed · 观察 · secondhand
- 备注:预印本未同行评审;arXiv 被网络策略拦截(403),发现均来自搜索摘要/DEV 转述,需回原文核对措辞和计数。作者含 Google(Macvean)研究者;与 SpecMine 同组。动机自述'实践证据主要来自推广它的厂商'。高优先级回一手。

## A30 (ADOPT)
- 论断:Asana 内部报告(Staff Engineer Walter Li,inside-asana):7 名工程师、524 个合并 PR、4 个月,以每人首次明确使用 /spec-driven 为界前后对比:每周 PR 数 +38%,实现代码新增 2.66×(剔除一段异常高产窗口后仍 +66%);显式 revert 率 spec-driven 工作 1.2% vs 其他 PR 1.66%。作者自承 PR 与新增行数是不完美的生产率代理。
- 原文:
- URL:https://asana.com/inside-asana/spec-driven-development
- 来源:Asana (Walter Li), 2026, Spec-driven development: The Good Parts - and what we learned after three months · 2026 · 【厂商】 · T2 · 观察 · secondhand
- 备注:企业自述(Asana 推广自家 AI 工作管理),非 SDD 工具厂商但有品牌利益;前后对比无对照组,7 人小样本,revert 差 0.46 个百分点无推断统计;PR 数≠质量。asana.com 403,数字来自搜索摘要。

## A31 (ADOPT)
- 论断:AWS 发布的 Kiro 客户案例:PKFARE 测试与开发团队在约 5 周内完成 10 万行技术支持工单系统并上线,原型验证'从数月到数天';Loyola Marymount 大学称某任务降到半天;Socure 'Scala→Go 迁移 2 天(原估 3 周)'仅见于 The New Stack 二手;广为流传的 Rackspace '52 周工作 3 周完成、效率 +90%' 未能定位到一手(检索仅见 Rackspace 展会页'最高 87.5% 时间节省')。
- 原文:
- URL:https://aws.amazon.com/solutions/case-studies/pkfare/
- 来源:AWS, 2026, PKFARE customer case study; AWS Public Sector Blog LMU; The New Stack (Socure) · 2026 · 【厂商】 · T2 · 案例 · secondhand
- 备注:全部为 Kiro 厂商或其合作伙伴发布,无基线定义、无对照;'估算工期 vs 实际工期'口径不可验证。Rackspace 数字按疑似二手夸大处理,不得引用。

## A32 (ADOPT)
- 论断:独立企业级测量缺位:本线检索未找到任何非厂商、非自述、带对照组的企业 SDD 落地报告;可得'企业案例'均为工具厂商(AWS/Kiro)、平台方或企业自述(Asana)。
- 原文:
- URL:
- 来源:本线检索结论(见 searched_angles) · 2026-11 · 【研究】 · n/a · 观察 · paraphrase-checked
- 备注:阴性结论受网络限制影响(多数站点 403),需验证阶段复检。

## A33 (ADOPT)
- 论断:2026 话语场(反方/质疑):François Zaninotto(Marmelab,2025-11)《Spec-Driven Development: The Waterfall Strikes Back》称其让人想起要求大量前置文档的瀑布模型;Kent Beck(2026-02 newsletter《Earn *And* Learn》)认为'spec-driven 与否不是问题,先问在玩哪种游戏',SDD 隐含'终点线游戏'假设,在'复利游戏'中不成立;Ayman Nadeem(Nuanced 创始人,前 GitHub 工程师,2026-09)《Plan mode is dead》称独立规划步骤已失效,HN 上一位自称 Claude Code 开发者的评论认为 plan mode 本质只是附加在消息上的提醒。
- 原文:
- URL:https://marmelab.com/blog/2025/11/12/spec-driven-development-waterfall-strikes-back.html
- 来源:Zaninotto 2025 (Marmelab); Beck 2026 newsletter.kentbeck.com/p/earn-and-learn; Nadeem 2026 'Plan mode is dead' · 2026-09 · 【媒体】 · mixed · 评论 · secondhand
- 备注:引语均来自搜索摘要,未逐字核(站点 403);Beck 句子'Spec-driven or not spec-driven is not the question'需回原文;Nadeem 有自家产品转向的利益;HN 评论者身份未核。

## A34 (ADOPT)
- 论断:2026 话语场(辩护方):Marc Brooker(AWS 杰出工程师,2026-04-09 个人博客《Spec Driven Development isn't Waterfall》)称 SDD 不是把设计'提前',而是把设计'提升'——迭代的对象是 spec 而非实现;Roger Wong(2026-03)承认相似但称 agent 让构建变便宜、反馈环改变;Utsab Pant 提醒'过期的 spec 比没有 spec 更糟,因为 agent 会忠实地把它当真'。
- 原文:
- URL:https://brooker.co.za/blog/2026/04/09/waterfall-vs-spec.html
- 来源:Brooker 2026 (brooker.co.za); Wong 2026 (rogerwong.me); Pant (utsabpant.com) · 2026-04 · 【媒体】 · mixed · 评论 · secondhand
- 备注:Brooker 是 AWS(Kiro 出品方)高管工程师——利益相关,辩护意见方向可参考;引语未逐字核。

## A35 (ADOPT)
- 论断:Hacker News 话语(二手转述):InfoQ 报道部分 HN 开发者称 spec-driven 拖慢开发;HN 评论认为 Spec Kit 教程过于基础,不适用于'对巨大遗留代码库做增量改进或重构';Kiro 发布帖曾登 HN 榜首(1,063 分,二手博客数字)。
- 原文:
- URL:https://www.infoq.com/news/2025/08/aws-kiro-spec-driven-agent
- 来源:InfoQ 2025-08 AWS Kiro spec-driven agent; GeekNews(news.hada.io)HN 评论汇编 · 2025-08 · 【媒体】 · mixed · 评论 · secondhand
- 备注:news.ycombinator.com 与 hn.algolia.com 均被网络策略拦截,未能取得原帖、作者 ID 与时间戳;具名作者要求未满足,验证阶段需补。


### 搜索角度
- Stack Overflow 2025 AI 页 / 2026 结果页 / 2026 脉冲调查:仅经 WebSearch 摘要(survey.stackoverflow.co、stackoverflow.blog 均 403);未找到 spec/plan-first 题项,唯一相关为 2025'项目规划不打算用 AI 69%'
- JetBrains State of Developer Ecosystem 2025、AI Pulse 2026:仅二手;未找到 spec/plan 题项
- DORA 2025 PDF(services.google.com 403):仅二手;未找到 spec 题项;DORA 2026 未检索到
- GitHub Octoverse 2025:未找到 AGENTS.md / spec-kit 计数;Octoverse 2026 未见
- GitHub code search(可复跑,2026-11-11):constitution.md@.specify/memory、tasks-template.md@.specify/templates、spec.md/plan.md@specs、requirements/design/tasks.md@.kiro/specs、.kiro/steering、openspec project.md/AGENTS.md、.bmad-core、tessl.json、speckit 命令文件、AGENTS.md/CLAUDE.md/.cursorrules 对照
- GitHub 短语+内容检索 '"Feature Specification" "Feature Branch"' 返回 74,496 而 plan.md 版本仅 2,672——遗留搜索对引号短语匹配不可靠,未采用
- repo search:spec-kit/OpenSpec/BMAD/Kiro star;topic:spec-driven-development/spec-kit/kiro;tessl-labs/tessl 查询失败(名称不确)
- raw.githubusercontent 抓取 100 个 constitution.md 检测占位符
- git treeless clone 180 仓(spec-kit/Kiro/OpenSpec 各 60)计算功能 spec 数、spec 提交占比、spec 冻结
- SpecMine 数据集(GitHub 样本仓,README + parquet,DuckDB 计算);Zenodo/HuggingFace 全量未能访问
- search/issues:remove/add spec kit|speckit|kiro|openspec|bmad 标题 PR 计数与月度切片;移除 PR 正文抽读编码理由
- search/commits:'remove spec-kit' 582、'remove kiro specs' 704(未采用为主数字,全文模糊匹配)
- spec-kit 官方仓 issue 按 reactions 排序(#1191、#442、#467)
- 企业案例:AWS Kiro(PKFARE、LMU、Dynata、Rackspace、Socure)、Asana 内部报告;独立企业报告——未找到
- Thoughtworks Radar(SDD、Spec Kit、OpenSpec blip)——仅二手
- 话语场:Marmelab/Zaninotto、Kent Beck、Marc Brooker、Roger Wong、Utsab Pant、Yuval Yeret、Ayman Nadeem、Simon Willison(仅二手、与 SDD 关联弱)、Armin Ronacher/Dave Farley(未找到相关原话)
- HN 原帖(news.ycombinator.com、hn.algolia.com 403)——未取得,具名作者缺失
- arXiv 2608.25202(Agarwal et al.)、2611.05094(gated spec-driven workflow audit-trail,未找到内容)、2608.30572(PBL 教学报告,未读)——arxiv.org 403
- npm/PyPI 下载量(api.npmjs.org、pypistats 403)——未取得;spec-kit 经 uvx 从 git 安装,PyPI 下载本就不代表采用
- Reddit 弃用帖——未检索(reddit 不可达且无具名作者)

### 交叉口径问题
- 文件 vs 项目:代码搜索 total_count 计文件(Kiro 每功能 3 文件、BMAD 每仓数十文件);SpecMine 按仓库计——引用时必须写明单位
- GitHub 遗留 code search 的 total_count 是估计值且疑似分桶(requirements.md 与 path:.kiro tasks.md 同为 38,336),只能作数量级;只覆盖默认分支、非 fork、公开仓
- 安装 ≠ 使用:constitution.md 存在 ≠ 写过功能 spec(28% 克隆样本为 0 个 spec;8% constitution 是空模板)
- star(149k)≠ 安装(~14k 仓)≠ 使用 ≠ 效果;topic 自标仓是供给侧
- SpecMine 500 仓样本按 star 精选,README 明言不可估总体比率;A20/A21 只能作方向
- 'spec 冻结'(功能完工后不再改 spec)≠ 漂移(spec 与代码不一致);spec-first 用法下冻结是预期行为——需按 Böckeler spec-first/anchored/as-source 分型解读
- Stack Overflow 2025 agent 使用 31%/23% 周用/52% 不用 三种口径;2026 主调查 26.2% 与脉冲 59% 定义不同;2026 样本量疑似骤降需核
- 调查题项'不打算用 AI 做项目规划'(T2 规划由 AI 做)与 SDD(人写 spec 给 agent)方向不同,不得互换
- 移除 PR 计数:标题短语匹配严重低估且被同组织批量操作放大;'remove kiro' 多为撤工具非撤 spec;移除/新增比例不可跨工具比较
- 企业案例全部为厂商/自述:Kiro 案例的'估算工期 vs 实际工期'无基线;Asana 前后对比无对照、7 人;Rackspace 52 周→3 周 未定位一手
- 弃用常见模式是'弃 T2 流程工具、留 T1 规则/issue 验收标准'——不可将弃用读作'spec 本身无用'
- Agarwal et al. 2608.25202 与 SpecMine 同组,二者不是独立来源