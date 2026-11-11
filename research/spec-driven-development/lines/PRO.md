# PRO 线 · 正方一手与 LLM 侧机制证据(#25 SDD)

> 31 条论断(P01–P31),其中 22 条一手逐字核对、3 条转述核对、6 条二手。
> **联网降级**:本会话 arxiv.org、ACM DL、IEEE、OpenReview、Hugging Face、microsoft.com、github.blog 全部 403/DNS 不可达。一手全文只能从作者的 GitHub Pages 仓库和官方复现包拉取(git clone / raw.githubusercontent.com)。凡只能靠搜索摘要的条目都标为 `secondhand`,quote 留空。

## 1. 计划先行(T2,模型自己生成计划)

- **Self-planning(北大 Ge Li 组,TOSEM 2024)** P01–P04。基座是 code-davinci-002。HumanEval Pass@1 从 48.1% 到 60.3%,相对 +25.4%,这是四个基准里的**最大值**。其余三个基准相对 +11–24%,绝对 +4.2–12.2 pp。
  - 陷阱 1:每个配置只跑一次贪心解码,没有显著性检验。文中的 "significant" 不是统计意义上的显著。
  - 陷阱 2:"Ground-truth Planning" 上界(74.4%)用的计划是**从参考答案代码反推出来的**,含答案信息,不能当作"人写好的 spec 能带来 +50%"。
  - 陷阱 3:有模型能力门槛。code-cushman-001(13B)用了计划反而下降(34.0→30.1),小模型接近 0。
- **第三方结果方向相反**(P05)。MapCoder README 中 GPT-4 + Self-Planning 只在 HumanEval 上为正,MBPP、MBPP-ET、HumanEval-ET 都低于 Direct。注意 MapCoder 作者是竞争方法的提出者。
- **口径疑点**(P06)。MapCoder 表中 "ChatGPT" 行的 Direct 和 Self-Planning 数字,与 Self-planning 论文里 code-davinci-002 的数字逐位相同,疑似挪用,不能当独立复现。
- **同组的其他方法**:Self-collaboration 消融(P08),加 Analyst(需求分解+计划)后相对 +21.8%;SCoT(P09)相对 CoT 最多 +13.79%。两篇都与 Self-planning 同一课题组,都是单基准或"up to"口径。
- **MapCoder**(P07)和 **PlanSearch**(P24)是整体流程或搜索型证据。PlanSearch 用的是 pass@200(77.0% vs 重复采样 60.6%),机制是靠计划增加候选多样性,**不能**与 pass@1 或"单次 spec 提质"混引。作者来自 Scale AI。

## 2. 需求澄清(T1:人或模拟人补充意图)

- **ClarifyGPT(FSE 2024)** P10–P13。人类实验:GPT-4 在 MBPP-sanitized 上 70.96→80.80,在 MBPP-ET 上 51.52→60.19,p 值在 1e-4 到 1e-5 量级;10 人,140 道含糊题,每题 3 人作答,每法跑 3 次取平均。
  - **关键限定(P11)**:问卷里给参与者看了带期望输入/输出的单元测试,所以 T1 澄清的收益里混进了 T4 信息。
  - 模拟用户实验(P12)中,模拟器持有 ground-truth 测试,结果属于理想化上界。
  - 预印本与 FSE 正式版的数字不同(四基准 11.52/15.07 vs 五基准 11.66/15.00)。
- **Ambig-SWE(CMU,ICLR 2026)** P25,二手。在欠规约的 SWE-bench Verified 上允许提问,解决率最高相对 +74%;模型在没有明确提示时几乎不主动提问。模拟用户持有完整题面。复现仓库已核到 500 条实例表,但没找到聚合解决率。
- HumanEvalComm(P29)、Ask or Assume(P31)、SWE-RPG(P30)只到 README 或二手层级。它们支持"上游意图不清是瓶颈"这个**机制**,但都不是"有 spec 对比无 spec"的干预实验。

## 3. 测试驱动的意图形式化(T4)。本线最强证据

- **TiCoder 用户研究(TSE 2024,Microsoft)** P14、P15。15 人,组内设计,3 个 MBPP 改编任务。
  - 正确判断 AI 代码的比例:对照 0.40,PassFail 0.84(p=0.001);Output 变体为 0.64,不显著。
  - NASA-TLX 认知负荷:45.46 降到 28.00(p=0.007)。
  - **完成时间无显著差异**。
  - 样本极小,每人每个条件只做 1 个任务,任务是函数级小题,受试者不能编辑提示。
- **TiCoder 大规模评估**(P16)用参考实现充当"理想化用户",作者自己称之为**上界**。越强的模型增益越小:GPT-3.5/GPT-4 系 5 次交互后绝对 +13–22 pp,旧补全模型 +35–54 pp。
- **标题数字审计(P17,承重前必须过方法学审计席)**。"平均绝对提升"有三个版本:38.43%(v1)、45.97%(v2 摘要)、45.73%(正文)。本线按 Table IV 重算(Output、m=5、7 模型×2 数据集)只有 **33.50 pp**;只算四个旧模型是 43.94 pp。标题数字无法从同文表格复现。
- **测试放进提示**(P18):GPT-4-32k 在 MBPP 上从 67.13 升到 78.26(1 个测试)和 80.88(全部测试)。但放进去的是评测用的同一批测试,设计上存在泄漏。Mathews & Nagappan(P28,二手)方向相同。
- **作者转述也会漂移**(P19)。Lahiri 2026 博客把参与者写成"15 名专业开发者",论文写明其中有博士生;p=0.001 被写成 p<0.001。

## 4. 仓库级与 agent 级

- **CodePlan(FSE 2024)** P22、P23。本线用公开 metrics.json 重算:CodePlan 匹配 125/135 个真值编辑块、0 个多余块;Repair 基线匹配 60 块,漏 75 块,多余 32 块。
  - 公开数据只有 5 个仓库;有效性分母是 5/6 还是 5/7 没能回到一手核对。
  - **CodePlan 的"计划"是静态依赖分析驱动的算法化编辑序列,不是 plan.md**,不能迁移成"写计划文档有效"。
- **SDD 本体的实验**(P26 Spec Kit Agents、P27 Google 测试生成,均二手)。Spec Kit Agents 的 LLM 评审分只 +0.15(5 分制),SWE-bench Lite +1.7 pp,对比的是"有钩子 vs 无钩子的 Spec Kit",**不是 SDD vs 无 spec**。Google 那篇做的是测试生成,不是代码生成,数据不可复跑。
- **没找到**:前沿 agent(Claude Code、Codex、Cursor、Kiro 的 plan mode)"有/无计划"的公开受控消融。

## 5. 正方阵营内部的分歧

- Lahiri(P20)明确说 Spec Kit 式的自然语言 spec "remain informal and uncheckable",只改善可追溯性。正方最强证据(TiCoder)本身属于 T4/T3,作者也认为 T1/T2 文档 spec 的保障力弱。**引用 TiCoder 来支持 Spec Kit/Kiro 式 SDD 属于跨型混引。**

## 最强 3 条
1. P14/P15 TiCoder 用户研究:随机化组内设计,混合效应回归加 FDR 校正,一手逐字核对。样本小,但设计最干净。
2. P18 / P16 TiCoder 的 T4 机制:同一模型上的受控对比,一手表格可复算(都是上界)。
3. P10 ClarifyGPT 人类实验:真人作答,有 p 值,跑 3 次取平均。但要连同 P11 的测试信息混入一起引用。

## 最弱 3 条
1. P26 Spec Kit Agents:二手;LLM 评审分,增益只有 +0.15;比较对象也不是"无 spec"。
2. P31 Ask or Assume:二手,样本和设置全部未知。
3. P06/P05 MapCoder 对 Self-planning 的"复现":数字疑似挪用,且来自竞争方。

## 未搜到 / 未能回一手的关键角度
- CodePlan、Ambig-SWE、Mathews & Nagappan、ClarifyCoder、HumanEvalComm、Spec Kit Agents、Google SDTG 的论文正文(arXiv/ACM 不可达)。
- SWE-bench 级前沿 agent 的计划步骤单因素消融,以及 plan mode 的独立测量。
- 任何关于 spec **维护成本、漂移、返工率**的正方实证(主张 2),以及 spec-as-source(主张 3)的实证。PRO 线在这两点上没有证据。
- 人类开发者"SDD vs 无 spec"的 RCT:未找到。
