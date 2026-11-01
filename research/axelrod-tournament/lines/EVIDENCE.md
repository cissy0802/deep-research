# EVIDENCE 线：TFT 式互惠在人、动物、历史、LLM 中是否存在

32 条论断见 EVIDENCE.json，其中 28 条 verbatim-checked，3 条 paraphrase，1 条 secondhand。

## 1. 人类实验室（结论：有互惠，但不是 TFT 独大，门槛比 SPE 高）
- **Dal Bó & Fréchette 2011 AER**
  - 逐字核对过摘要：合作「may prevail」，但所需条件比 SPE 更严，甚至比 risk dominance 还严（E01）。
  - WP 数字：risk-dominant 处理组首轮合作率从 46.5% 升到 70.6%；非均衡组从 29% 降到 5.5%（E02–E03）。
- **JEL 2018 survey**
  - meta 数据：15 篇论文、32 个 treatment、2,415 名被试、157,170 次选择。这组数字取自 2016 年稿（E05）。
  - 判据是 SizeBAD，即 AD 对 Grim 的吸引盆大小（E06）。
  - 策略分布：AD、Grim、TFT 三种在 17 个 treatment 中的 15 个里合计过半；WSLS「never a sizeable fraction」（E07）。
  - 文中还有一句：「Given the work of Axelrod, one could have expected subjects to use TFT ... both Grim and TFT are present」。
- **Fudenberg-Rand-Dreber 2012**
  - 摘要已逐字核对：有噪声时，成功的策略是 lenient（宽容）+ forgiving（原谅）的（E09）。
  - 噪声 1/8、b/c 取值这些参数**没能回到原文**（DASH 返回 429），目前只有 survey 的二手转述（E10）。
- 待补反方：Breitmoser 2015 AER「Cooperation, but no reciprocity」。

## 2. 动物（共识措辞：严格 TFT 罕见；宽义互惠可能广泛）
- **正方一手**
  - Wilkinson 1984：吸血蝠分食取决于亲缘和互惠机会，两者影响「equally and independently」（E11）。
  - Carter & Wilkinson 2013：「收到多少」预测「给出多少」的权重是亲缘的 8.5 倍；64% 的分食二元组无亲缘关系（E12）。
  - Carter 2020：吸血蝠先用低成本梳毛试探、再逐步加码到分食（raising-the-stakes），这是关系模型，不是 TFT（E13）。
  - Milinski 1987：棘鱼镜子实验，「behaved according to TIT FOR TAT」（E14）。当年即遭 Lazarus & Metcalfe 1990 等批评，批评原文未读（E15）。
- **怀疑派**
  - Clutton-Brock 2009：「Firm evidence of reciprocity in animal societies is rare」（E16）。
  - Hammerstein 2003：多数重复的动物互动根本不构成重复博弈。原文是 OCR 扫描件，引文已从乱码中还原（E17）。
  - Stevens & Hauser 2004：认知约束让互惠难以实现（E18）。
  - Raihani & Bshary 2011：精确记账式策略「relatively uncommon」（E20）。
- **修正派**
  - Carter 2014：「罕见」主要来自用 TFT 定义互惠，等于把互惠定义没了（E19）。
  - Schweinfurth & Call 2019：「reciprocity might be a widespread phenomenon」（E21）。
  - 大鼠：广义互惠（Rutte & Taborsky 2007）和直接互惠（Dolivo & Taborsky 2015），见 E22。
- 写作建议：「TFT 在动物中」的命题已基本退场，留下的是「条件性合作 / 伙伴选择 / 关系」。

## 3. 历史：一战 live-and-let-live
- Axelrod 第 4 章的材料和历史解释都依赖 Ashworth 1980（Ashworth 是社会学家），并自承「Ashworth does not put it this way」（E23，逐字核对）。
- Axelrod 自己也写到三处偏离 TFT（E24）：
  - 报复常是二报一、三报一；
  - 伦理和仪式的出现改变了偏好；
  - 体系是被高层下令的突袭终结的。
- Gelman 2008：认为士兵「not generally in a prisoner's dilemma」，自保足以解释克制（E25）。注意 Gelman 是统计学家，不是史学家。
- **职业 WWI 史学家对 Axelrod 的批评：没找到。** Gowa 1986 的书评未读。

## 4. LLM
- **Akata et al.**（NHB 9(7):1380–1390，2025-05-08 上线，已核）
  - 设定是 10 轮有限重复、对局长度已知。
  - GPT-4 遇到「背叛一次后永远合作」的对手，从此「never cooperates again」（E27）。
  - 告诉它「对方可能失误」后，它会恢复合作。
  - 注意：已知终点时，背叛本身就可以是均衡。
- **Fontana et al. 2024**
  - Llama2 和 GPT-3.5 比人更合作、更宽恕（对手背叛率低于 30% 时）；Llama3 更像人，偏剥削（E28）。
  - 对手是随机策略，不是互惠策略。
- **Payne & Alloui-Cros 2025**（arXiv v1，未同行评审）
  - 共 7 场锦标赛：每场 24 个 agent，每阶段 276 场对局，共 5 阶段；单局上限 30 轮；约 32,000 条决策加理由（E29）。
  - 终止概率取 10%、25%、75%；**每个条件只跑一次**。
  - 「Claude 最宽恕」只来自 1 场 Showdown，参赛的是 claude-3-haiku（E30）。
  - 75% 条件：Gemini 合作率 2.2%，OpenAI 95.7%；OpenAI 被淘汰，最终种群是 Gemini 16 + STFT 8。
  - Showdown 合作率：Gemini 0.925、OpenAI 0.957、Anthropic 0.958。
- **2025 后续**
  - Willis/Leibo 等：让 LLM 写整套策略，再跑演化动态（E31）。
  - Singh 等（Microsoft）：对阵 240 个经典策略，表现「on par with... exceeding」最佳经典策略（E31）。
  - FAIRGAME 框架（E32）。

## 未触达
- FRD 2012 全文；JEL 2018 定稿（现用 2016 稿）；Gowa 1986 全文；Lazarus & Metcalfe 1990 全文；Gelman 2008 全文（付费墙）。
- Hammerstein 原文只有 OCR 质量很差的扫描件。
- Payne 论文是否已发表。
