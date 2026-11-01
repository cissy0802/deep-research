# R2-M 方法学审计席：Payne & Alloui-Cros, arXiv 2507.02618（有否决权）

审计材料：arXiv abs（2026-10-31 时仍只有 v1，2025-07-03 提交，无 journal-ref）、PDF 全文，以及公开仓 github.com/kennethpayne01/LLM-IPD-ARXIV（已归档）。该仓发布了 evolutionary_PD_expanded.py 和 7 个 consolidated CSV。我用自己写的脚本从 CSV 重算了合作率和 fingerprint 计数。7 场的合作率与 Table 13 **逐位吻合**，所以这批数据就是论文用的数据。

## 一、核实的设计事实
- 共 7 场：2×2 核心设计（basic/advanced × p=0.10/0.25），加 75% 压力测试、10% mutation、10% Showdown。原文写 "Each cell is executed once"，即每个条件只跑 1 次，没有重复，也没有 seed。
- 规模：每场 24 个 agent，Showdown 是 20 个（5 家各 4 个，与正文 "fixed population of 24" 矛盾）。每阶段 276 场对局，共 5 阶段，单局上限 30 轮，history 只给最近 20 步。rationale 合计 31,949 条。
- 实际版本（以 CSV 头为准）：gpt-3.5-turbo、gemini-1.5-flash-preview-0514、gpt-4o-mini-2024-07-18、**gemini-2.5-flash-preview-05-20**（正文写的是 "gemini-2.5-flash"），以及 claude-3-haiku-20240307。Claude 只出现在 Showdown 1 场。
- 终止概率：prompt 里**明说了**（"will end randomly after any given round with a X% probability"）。prompt 也给了 payoff 和目标（maximize score）。所有模型拿到的 prompt 完全相同（token-identical）。

## 二、弱点与严重度
1. **[致命] 每个条件 n=1，没有任何统计推断**。全文没有 CI、显著性检验、seed 或重复。凡是「X 条件下 A 胜 B」，都等于单次抽样。
2. **[致命] 演化规则会把噪声放大成定局**。规则是相对适应度平方 (F/F̄)²，F̄ 取各策略的**不加权**均值，再四舍五入，最后「从最低分策略逐个删、给最高分策略逐个补」。这样一来，结局基本由**名次**决定，分差大小几乎不起作用。实测：
   - Showdown 第 3 阶段，OpenAI 每步 2.881，Gemini 2.953，只差 0.07；OpenAI 却在下一阶段从 5 个跌到 3 个。
   - 75% 条件下全程每步得分 Gemini 2.207 对 OpenAI 2.171，结局却是 OpenAI 灭绝、Gemini 占 16 席。
   - Advanced-25% 在第 1 阶段之后人口完全冻结，这是取整死区，不能读成「最稳定的生态」。
   - 论文的 U 形稳定性和 25% sweet spot，都建立在这台放大器加单次运行之上。
3. **[严重] 采样条件不对称，混杂了「家族风格」**：
   - OpenAI 和 Claude 设了 temperature=0.7。
   - Gemini 的请求**没有 generationConfig**，所以 temperature 用的是 API 默认值；2.5-flash-preview 默认还开着 thinking，代码里没有设 thinkingConfig（thinking 开着这一点是我的推断，论文没提）。
   - 因此「Gemini 更 strategic/ruthless」至少部分可能是「推理模式对非推理模式、不同温度」造成的，不能完全归到训练风格上。
   - basic 档 OpenAI 的温度，论文和代码都没有交代。
4. **[严重] 解析失败一律记为合作，不报告**。API 报错、格式不对，都会 `return "C"`，论文没有提到这一点。CSV 里的计数：
   - Showdown 中 Anthropic 有 **92/3923 次**是被强制记为 C（约 2.3%），其他场 0–10 次。
   - Claude 的 P(C|DD) 论文报 0.397，剔除强制 C 后是 20/70≈0.29。
   - 所以「Claude 最宽恕」被系统性地抬高了。
5. **[严重] fingerprint 的分母很小，而且跟对手结构纠缠**：
   - Showdown 中 Claude 的 CD 只有 130 次、DC 只有 68 次；OpenAI 的 CD 是 75 次、DC 是 68 次。
   - 按 Wilson 95% CI，CD 是 0.62 [0.53,0.70] 对 0.44 [0.33,0.55]；DC 是 0.66 [0.54,0.76] 对 0.32 [0.22,0.44]。决策在对局内、副本间高度相关，有效 n 更小。
   - 75% 条件：OpenAI 全场只有 116 次决策，DC 和 DD 都是 0 次（所以表里是 N/A）；Gemini 的 P(C|CC) 只有 0/3 次。
   - 条件概率是跨所有对手合并算的，所以也取决于这个 agent 碰到了谁。
   - 我按发布数据重算，OpenAI Showdown 的 CD 是 0.440，论文写 0.473，存在小幅不可复现。
6. **[中] Showdown 不可复现**。仓里的主脚本没有 Anthropic agent 类，basic 档的配置也不在仓里。
7. **[中] 正文自相矛盾，粗糙之处多**：
   - κ 正文写 0.79，Table 27 是 0.755 和 0.603。
   - 编码样本一处写 3194，一处写 3195。
   - Appendix B 说 "Hand-coded sample of 5,000+"，正文是用 LLM 编码的。
   - 编码模型名写成 "gemini-11.5-flash-latest" 和 "claude-3-haiku-2020307"。
   - 编码器 claude-3-haiku 同时就是参赛模型；分析是「在 Cursor 里用 Gemini 2.5-pro」做的。
   - 全文没有 Limitations 一节，结论用词是 "definitively"。
8. **[中] 未经同行评审**：只有 v1，没找到任何期刊或会议版本。没有 COI 或资助声明。两位作者分别在 KCL 和 Oxford，看不出有厂商利益。
9. **[中] 结论被外推到「家族」**。advanced 档其实是小模型或快速档（4o-mini、2.5-flash、3-haiku），而且是 2024–25 年的旧版本。到 2026 年，这些标签对 GPT/Gemini/Claude 当前旗舰没有任何信息量。

## 三、否决（VETO）：以下不得承重
- **V1** 不得写成「Gemini 冷酷 / OpenAI 合作 / Claude 宽恕」这种**家族标签**。最多只能落到「某个具体版本，在这套 prompt 和温度下，跑一次」的层面。
- **V2** 「Claude 最宽恕」：否决作为结论。它只来自 1 场、claude-3-haiku，样本是 n=130/68 次状态，其中混了 2.3% 被强制记为合作的决策。只能当作轶事提一句。
- **V3** 演化结局本身不得承重，包括 OpenAI 在 75% 下灭绝、Gemini 16 + STFT 8、Showdown 中各家的增减。这些都由单次运行和名次放大器决定。正文如果引用 "Gemini 16+STFT 8"，必须同时写出两者每步只差 2.207 对 2.171。
- **V4** Showdown 合作率 0.925/0.957/0.958 不得读成三家有差异。Anthropic 和 OpenAI 的 CI 几乎完全重合，而且 Gemini 的温度设置不同。
- **V5** 「25% 是 sweet spot」「稳定性呈 U 形」：否决，原因是 n=1 加取整死区。
- **V6** 75% 条件下 OpenAI 的 fingerprint（N/A），以及 Gemini 那一行全 0：否决，分母是 0–8 次。
- **V7** rationale 的统计（例如「Gemini 94% 时间在想时间」）不得承重。编码器靠 LLM，κ 是 0.60–0.76，数字前后不一。

## 四、可以安全说的
- 「两位学者（KCL/Oxford）在 2025 年 7 月的未评审预印本里，让几个小档 LLM 和经典策略同场跑了 7 场演化 IPD，每个条件只跑一次。」
- 「同一场里，gpt-4o-mini 的合作率在每个条件下都高于 gemini-2.5-flash-preview。」这是论文自己的说法，数据核过。
- 「终止概率升到 75%，也就是期望约 1.3 轮时，gemini-2.5-flash-preview 几乎全背叛（2.2%），gpt-4o-mini 几乎全合作（95.7%，但只有 116 次决策）。」这一条可以作为**方向性观察**：同一份 prompt 下，两个模型对 shadow of the future 的敏感度差异很大。
- 「模型会在 rationale 里谈论终止概率和对手类型。」只能定性地说。
- 写作建议：凡引用这篇，句子里都要带「单次运行、具体版本、未评审」三个限定词，并与 Akata（已发表于 NHB、10 轮已知终点）区分开。

## 五、终评
**C−（探索性预印本）**。它的数据公开、能复算，这一点难得，所以没有判 D。但单次运行、名次放大器、采样不对称、静默的 C 兜底，这四点叠在一起，任何比较性、家族性、演化结局性的结论都承不了重。文章里只能把它当作「有趣的初步观察」，不能当证据链的一环。
