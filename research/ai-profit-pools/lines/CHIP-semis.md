# CHIP-semis 芯片层 调研线(截至 2026 年 10 月)

## NVIDIA(一手:SEC 8-K EX-99.2 CFO Commentary / 10-Q)

### C1 NVIDIA 时序(GAAP)
| 财年 | 收入 | 数据中心 | GAAP 毛利率 | GAAP 经营利润 | 经营利润率(算) |
|---|---|---|---|---|---|
| FY23(至2023-01) | $26,974M | $15,005M(10-K) | 56.9% | $4,224M | 15.7% |
| FY24 | $60,922M | $47,525M | 72.7% | $32,972M | 54.1% |
| FY25 | $130,497M | $115,186M | 75.0% | $81,453M | 62.4% |
| FY26(至2026-01-25) | $215,938M | $193,737M | 71.1%(含H20 $4.5B 减值) | $130,387M | 60.4% |
| Q2 FY27(至2026-07-26) | $96,221M | $89,023M | 75.0% | $63,734M | 66.2% |
- 来源: https://www.sec.gov/Archives/edgar/data/1045810/000104581024000028/q4fy24cfocommentary.htm ; https://www.sec.gov/Archives/edgar/data/1045810/000104581026000019/q4fy26cfocommentary.htm ; https://www.sec.gov/Archives/edgar/data/1045810/000104581026000073/q2fy27cfocommentary.htm
- 引文(Q2 FY27):"Revenue $96,221 ... Gross margin 75.0 % ... Operating income $63,734"; "Data Center $89,023 $75,246 $41,096 18 % 117 %"
- 引文(FY24):"Revenue $60,922 $26,974 Up 126% Gross margin 72.7 % 56.9 %... Operating income $32,972 $4,224"
- 引文(FY26):"Revenue $215,938 $130,497 65 % Gross margin 71.1 % 75.0 % (3.9) pts ... Operating income $130,387 $81,453"
- 口径:FY 截至 1 月末(FY27 Q2 = 日历 2026 年 5-7 月)。**Q1 FY27 起 non-GAAP 不再剔除 SBC**,历史 non-GAAP 已重述——旧 non-GAAP(如 FY25 75.5%)与新口径不可直接比。Q2 FY27 起分部重组:Data Center 拆为 Hyperscale $48.7B / AI Clouds, Industrial & Enterprise $40.3B;Edge Computing 取代原 Gaming/ProViz/Auto。

### C2 Q3 FY27 指引:毛利率 74.0% ±50bp(Vera Rubin 爬坡),收入 $108B ±2%
- 引文:"GAAP and non-GAAP gross margins are expected to be 74.0%, plus or minus 50 basis points."
- 解读:小幅压缩信号,与新品爬坡一致(历史上 Blackwell 爬坡时 Q3 FY26 也落到 73.4%)。

### C3 客户集中度(10-Q Note,2026-08-26)
- 引文:"For the second quarter of fiscal year 2027, one direct customer represented 16 % of total revenue... For the first half of fiscal year 2027, three direct customers represented 16 %, 15 %, and 13 % ... For the second quarter of fiscal year 2026, two direct customers represented 23 % and 16 %"
- 引文:"We estimate that one AI research and deployment company contributed a meaningful amount of our revenue by purchasing cloud services from our customers"
- 应收:"Five direct customers accounted for 22 %, 14 %, 13 %, 11 %, and 10 % of our accounts receivable balance"
- 来源 https://www.sec.gov/Archives/edgar/data/1045810/000104581026000075/nvda-20260726.htm

### C4 Hyperscale 占 DC 55%(48,710/89,023);Q4 FY26 "slightly over 50%"

### C5 回流/循环融资迹象(资产负债表)
- 非上市股权投资 $22.3B(2026-01)→ $51.2B(2026-07);可交易股权 $12.9B → $42.8B;Q2 股权投资净收益 $7.8B(GAAP 净利 $59.7B 中含此,non-GAAP 净利 $54.0B)。
- 承诺:供应 $279B(主为内存)、云服务协议 $29B、AI cloud agreements $36B(NVIDIA 向 AI 云回购算力,"which the AI clouds can unilaterally stop providing to us and sell to third-party customers at more advantageous rates"),股权投资承诺 $25B。
- SB Energy/OpenAI PORTS-Pike 担保上限 $105B,~4.25GW:"Each generation of NVIDIA infrastructure deployed at PORTS-Pike could represent approximately 1.5 million NVIDIA GPUs, or approximately $150 billion to $200 billion in NVIDIA revenue."
- DSO 45→60 天:"due to extended payment terms on large, multi-quarter agreements with certain investment-grade customers."
- 解读:芯片层利润部分靠向下游(模型商/AI云)提供股权、回购算力、信用担保来"买"需求——利润质量与周期风险的反证。

## 其他芯片公司(一手 SEC)

### C6 AMD Q2 2026(至 2026-06-27,10-Q)
- DC 收入 $6.7B(+107%),DC 经营利润 $2.1B(≈31% 分部经营利润率),全公司 GAAP 毛利 54%。
- 引文:"Data Center net revenue of $6.7 billion ... increased by 107% ... primarily driven by strong demand for our AMD EPYC processors and AMD Instinct MI350 Series GPUs. Data Center operating income was $2.1 billion"
- 认股权证:"In October 2025 and February 2026, the Company issued warrants to OpenAI OpCo, LLC (OpenAI) and Meta Platforms, Inc. (Meta), each entitling the holder the right to purchase up to 160 million shares ... at an exercise price of $0.01 per share ... vest in tranches based on specified AMD Instinct GPU purchase milestones"
- 解读:第二名 GPU 需用近零价股权"买"大客户——挑战者无定价权;DC 分部(含 EPYC CPU)利润率远低于 NVIDIA。
- 来源 https://www.sec.gov/Archives/edgar/data/2488/000000248826000123/amd-20260627.htm

### C7 Broadcom Q3 FY26(至 2026-08-02,8-K 2026-09-02)
- AI 半导体收入 $16.7B(+221% YoY,+54% QoQ),Q4 指引 $21.7B;全公司收入 $29.6B,GAAP 毛利 $20,456M(69.1%,算)/ non-GAAP $22,191M(75.0%,算);non-GAAP 经营利润率 Q4 指引 66%。
- 引文:"Demand for our custom AI accelerators and networking continues to be very strong. Q3 AI semiconductor revenue of $16.7 billion grew 221% year-over-year, and 54% quarter-over-quarter"
- 口径:Broadcom "AI semiconductor revenue" = 定制 XPU + AI 网络,公司自定义;non-GAAP 剔除 SBC 与无形资产摊销(与 NVIDIA 新口径不同)。
- 来源 https://www.sec.gov/Archives/edgar/data/1730168/000173016826000076/avgo-08022026x8kxex99.htm

### C8 TSMC Q2 2026(6-K,2026-07-16)
- 收入 US$40.20B,毛利率 67.7%,经营利润率 60.3%;HPC 占 66%;Q3 指引毛利 65-67%。
- 引文:"Gross margin for the quarter was 67.7%, operating margin was 60.3%, and net profit margin was 55.6%."
- 电话会(媒体逐字稿,Investing.com):"Our packaging capacity is so tight that now it's limiting my customers' growth";全年增长"slightly above 40%";capex 上调至 $60-64B。
- 来源 https://www.sec.gov/Archives/edgar/data/1046179/000104617926000451/a2q26e_withguidancexfinal.htm ; https://www.investing.com/news/transcripts/earnings-call-transcript-tsmc-lifts-2026-outlook-as-ai-demand-stays-hot-in-q2-2026-93CH-4794777

### C9 Micron FQ4 2026(至 2026-09-03,8-K 2026-09-30)——内存利润率已超过 NVIDIA
- 收入 $54.23B,GAAP 毛利率 86.8%、GAAP 经营利润率 80.7%;FY26 收入 $133.19B,GAAP 毛利 80.7%(FY25 39.8%)。
- 分部:Cloud Memory BU(含 HBM)收入 $16,283M,毛利 83%、经营利润率 76%;但 Mobile & Client BU 毛利 90%、Core Data Center BU 毛利 90%——**高利润来自整体内存短缺,不只 HBM**。
- 引文:"Cloud Memory Business Unit Revenue $ 16,283 $ 13,769 $ 4,543 Gross margin 83 % 83 % 59 % Operating margin 76 % 78 % 48 %"
- 引文:"our Strategic Customer Agreements provide added confidence in the durability of Micron's financial performance."
- 来源 https://www.sec.gov/Archives/edgar/data/723125/000072312526000018/a2026q4ex991-pressrelease.htm

### C10 SK hynix 2Q26(官方新闻稿)
- 收入 79.32 万亿韩元,经营利润 60.54 万亿韩元,经营利润率 76%(历史新高)。与 ~10 家客户签订 LTA。
- 引文:"The company has finalized Long-Term Agreements (LTAs) with around 10 customers"
- 来源 https://news.skhynix.com/en/q2-2026-business-results/(净利率 118% 含非经营收益,口径注意)

### C11 NVIDIA 承诺额暴增至 $279B "primarily related to the procurement of memory"——利润向内存分流的直接证据(NVIDIA 下季毛利指引降至 74%)。

## NVIDIA Q2 FY27 电话会(官方 FactSet Corrected Transcript,2026-08-26)
来源 https://s201.q4cdn.com/141608511/files/content_files/TRANSCRIPT_-NVIDIA-Corp-NVDA-US-Q2-2027-Earnings-Call-26-August-2026-5_00-PM-ET.pdf

### C12 毛利率压缩指引(内存涨价)——NVIDIA 利润被上游内存分流
- 引文(Kress):"we are experiencing extreme pricing conditions in memory. The magnitude of the price increase has exceeded our prior expectations and are headed even higher into next year... We expect margins to bottom in Q4 in the 71% to 72% range before settling at 72% to 73% in fiscal year 2028 as executed price increases take effect in Q1."
- 引文:"Memory scarcity today is being driven in large part by the AI buildout itself ... tighter memory supply is a symptom of the same demand surge that's driving our own growth."
- 对照:Micron FQ4 GAAP 毛利 86.8% > NVIDIA 75.0%;SK hynix 经营利润率 76% > NVIDIA 66%。

### C13 供给约束 + FY28 增速指引
- 引文:"we expect to grow revenue by approximately 70% in fiscal 2028. This is a supply-constrained outlook." "we expect supply to remain a bottleneck at least through the end of fiscal year 2028." "NVIDIA Compute is fully utilized across every cloud we serve."

### C14 资产负债表"买"需求(循环融资,公司自承)
- 引文:"The frontier AI labs ... are growing faster than what their balance sheets and credit profiles can support."
- 引文:"we've invested nearly $50 billion in the frontier AI labs."
- 引文:"we know some will call this circular financing. We see it differently."
- 引文:"we expect demand from the AI labs for which we expect to leverage our balance sheet to contribute toward roughly a quarter of our business next year."
- 另:与 Apollo/BlackRock/Blackstone/Brookfield/Goldman/KKR 建融资平台"raise over $500 billion of third-party capital"。
- 解读:当下芯片层吃到最大利润,但 ~1/4 的明年需求依赖 NVIDIA 自身信用支撑——利润的可持续性取决于下游模型商能否最终赚钱(反向支撑"模型层是否在给人做嫁衣"的问题:目前更像芯片商在给模型商垫资)。

### C15 定制芯片竞争(CEO 回应)
- 分析师(BofA Vivek Arya):"both of them [OpenAI and Anthropic] are designing their own custom chips. In fact, OpenAI just in the last few days spoke about Jalapeño..."
- 黄仁勋:"Whereas many of these XPUs are inference-specific chips for one cloud or one service, NVIDIA is a platform, an entire AI factory platform that spans the entire AI life cycle that you can use in any cloud."
- 黄仁勋:"NVIDIA runs the leading closed models; OpenAI, Anthropic, Grok, Meta, Gemini, and the leading open models"——开源/闭源都跑在 NV 上 = 模型商品化对 NV 中性偏利好(厂商自报)。

## 自研芯片 / 定制 ASIC

### C16 Google TPU 外售:Alphabet 10-Q(Q2 2026)首次披露 TPU 系统作为 Cloud 产品收入
- 引文:"Our Google Cloud product sales generally consist of the sale of TPU systems comprising hardware, software, installation, support, and extended warranty services."
- Cloud 积压:"$ 519.5 billion of remaining performance obligations ... of which $ 513.9 billion related to Google Cloud."(口径:RPO=承诺额,非确认收入)
- 来源 https://www.sec.gov/Archives/edgar/data/1652044/000165204426000071/goog-20260630.htm

### C17 Anthropic–Google–Broadcom TPU 协议(官方博客 2026-04-06,厂商自报)
- 引文:"multiple gigawatts of next-generation TPU capacity that we expect to come online starting in 2027";"Our run-rate revenue has now surpassed $30 billion—up from approximately $9 billion at the end of 2025";"We train and run Claude on a range of AI hardware—AWS Trainium, Google TPUs, and NVIDIA GPUs"
- 媒体:约 3.5GW(DCD/Silicon Republic)。2026-10-01 Reuters 转述 Anthropic IPO 招股书:Broadcom 向 Anthropic 提供至多 $42B 融资用于租赁芯片;Anthropic 预计 2027 年成为 Broadcom 最大客户(媒体转述,未能取得 SEC 原文)。
- 来源 https://www.anthropic.com/news/google-broadcom-partnership-compute ; https://finance.yahoo.com/technology/article/broadcom-to-lend-anthropic-up-to-42-billion-to-lease-chips-in-latest-circular-investing-deal-121617505.html

### C18 TPU 成本优势(分析机构 SemiAnalysis,2025-11-28)
- 引文:"the all-in TCO per Ironwood chip for the full 3D Torus configuration being ~44% lower than the TCO of a GB200 server."
- 引文:Anthropic 1M TPU = "400k TPUv7 Ironwoods, worth ~10 billion in finished racks that Broadcom will sell directly to Anthropic" + "remaining 600k ... rented through GCP in a deal we estimate at $42 billion of RPO"
- 引文:"OpenAI hasn't even deployed TPUs yet and they've already saved ~30% on their entire lab wide NVIDIA fleet."
- 引文:"Nvidia aims to protect its dominant position at the foundation labs by offering equity investment rather than cutting prices, which would lower Gross margins"
- 来源 https://newsletter.semianalysis.com/p/tpuv7-google-takes-a-swing-at-the (分析机构估算,非一手)

### C19 AWS 自研芯片(Q2 2026 电话会,媒体逐字稿)
- Jassy:"Our chips business now has an annual revenue run rate of over $25 billion, growing triple-digit percentages year-over-year."(run-rate,含 Graviton+Trainium,AWS 自定义)
- Jassy:有来自 Anthropic 与 OpenAI 的"multi-year, multi-gigawatt commitments";对外单卖:"I expect there's a real chance we'll do that in the future."
- 来源 https://www.fool.com/earnings/call-transcripts/2026/08/07/amazon-amzn-q2-2026-earnings-call-transcript/

### C20 Microsoft Maia 200(官方博客 2026-01-26,厂商自报)
- 引文:"30% better performance per dollar than the latest generation hardware in our fleet today";"will serve multiple models, including the latest GPT-5.2 models from OpenAI"
- 来源 https://blogs.microsoft.com/blog/2026/01/26/maia-200-the-ai-accelerator-built-for-inference/

### C21 Meta MTIA(官方 2026-03-11)
- 引文:"We deploy hundreds of thousands of MTIA chips for inference workloads across both organic content and ads on our apps.";MTIA 400/450/500 "primarily ... support GenAI inference production in the near future and into 2027"
- 来源 https://about.fb.com/news/2026/03/expanding-metas-custom-silicon-to-power-our-ai-workloads/

## DeepSeek 自然实验

### C22 2025-01-27 NVDA 单日 -17%,市值蒸发 ~$589B(美股史上最大单日市值损失)
- 媒体(CNBC/Bloomberg 标题):"Nvidia sheds almost $600 billion in market cap, biggest one-day loss in U.S. history";收于 $118.58。
- NVIDIA 声明:"DeepSeek is an excellent AI advancement and a perfect example of Test Time Scaling." "Inference requires significant numbers of NVIDIA GPUs and high-performance networking."
- 事后:DC 季收入 Q4 FY25(至 2025-01)$35.6B → Q2 FY27 $89.0B(2.5 倍);2026-10 市值约 $5.7T(媒体)。杰文斯式解读获事后支持——但注意同期有 Blackwell 换代、主权/AI 云需求、NVIDIA 自身融资支撑等混杂因素,不能单独归因于"效率提升刺激需求"。
- 来源 https://www.cnbc.com/2025/01/27/nvidia-sheds-almost-600-billion-in-market-cap-biggest-drop-ever.html ; https://www.cnbc.com/2025/01/27/nvidia-calls-chinas-deepseek-r1-model-an-excellent-ai-advancement.html

## 补充

### C23 Broadcom Q3 FY26 电话会(媒体逐字稿 Motley Fool,2026-09-02 会)
- 毛利:"Gross margin was 75% of revenue in the quarter, down 210 basis points sequentially as AI semiconductor revenue was a greater proportion of our total revenue mix."(non-GAAP;GAAP 计算为 69.1%)Q4 指引约 73%,原因"the increasing mix of XPUs with their increasing memory content"。半导体分部毛利约 67%。
- Hock Tan:"stop focusing on gross margin is what we're saying, look at where it matters, operating margin"
- AI 收入目标:FY26 $58B、FY27 ~$115B、FY28 ~$230B(公司指引/目标,未实现)。客户:Google("multi-tens of billions of dollars of TPUs annually")、Anthropic(2027 最大 XPU 客户)、OpenAI、Meta;6 家前沿模型客户。
- 定制芯片成本:"when you co-develop a chip that is optimized for your particular LLM workloads, you will outperform any GPU" / "half the cost"(厂商自报,利益相关);"dollars per gigawatt will remain in the $20 billion to $30 billion level"。
- 来源 https://www.fool.com/earnings/call-transcripts/2026/09/09/broadcom-avgo-q3-2026-earnings-call-transcript/
- 解读:定制 ASIC 让利润从 NVIDIA(~75% 毛利)转移到 Broadcom(半导体 ~67% 毛利)+ 云厂自身 + 内存商——"去 NVIDIA 化"并未让芯片层利润消失,而是在芯片层内部重分配且总体毛利率下移。

### C24 Marvell Q2 FY27(8-K 2026-08-27)
- 收入 $2.739B(+37%),GAAP 毛利 53.1% / non-GAAP 58.9%;DC 收入增速 46%,"significant acceleration in our Custom business beginning in the second half of fiscal 2027"。
- 解读:定制芯片/互联二线供应商毛利显著低于 NVIDIA、Broadcom——ASIC 设计服务并非高利润池。
- 来源 https://www.sec.gov/Archives/edgar/data/1835632/000183563226000022/q227_8kx812026ex-991.htm

### C25 TSMC AI 加速器占比与长期毛利(4Q25 电话会,经分析机构 Futurum 转述)
- AI 加速器收入占 2025 年总收入"high-teens percent";2024-2029 AI 加速器 CAGR "approach a mid-to-high 50%";长期毛利目标"56% or higher through the cycle"(实际 Q2 2026 已 67.7%)。
- 来源 https://futurumgroup.com/insights/tsmc-q4-fy-2025-results-and-fy-2026-outlook-signal-ai-led-growth/

### C26 NVIDIA 下游信用/担保规模(C5 汇总):Vivek Arya 在电话会估算 CFO commentary 中所有承诺/担保合计"about $500 billion or so"。

## 综合判断(本线)
1. **当下**:芯片层(含内存)是 AI 价值链最赚钱的一层——NVIDIA GAAP 经营利润率 66%,Micron 81%,SK hynix 76%,TSMC 60%,Broadcom non-GAAP 68%。
2. **利润沿供应链上游分流**:2026 年内存短缺使 Micron/SK hynix 利润率反超 NVIDIA;NVIDIA 自己指引毛利从 75% 压到 71-73%。TSMC 的 CoWoS 也是瓶颈。"卖铲子"内部,最稀缺的零件拿走最多利润,且稀缺点在移动(GPU→CoWoS→HBM/DRAM→电力)。
3. **NVIDIA 定价权的反证**:(a)客户集中度高(单一直接客户 16%,Hyperscale 占 DC 55%);(b)自研 ASIC(TPU/Trainium/Maia/MTIA)与 Broadcom 定制芯片规模化,SemiAnalysis 称仅 TPU 威胁就让 OpenAI 省 ~30%;(c)NVIDIA 以股权投资(近 $50B)、算力回购、$105B 租约担保而非降价来维持需求与毛利——毛利率表观稳定但部分经济让利转移到了资产负债表。
4. **长期**:芯片层利润高度周期化(内存利润率从 40% 到 87% 只用一年;NVIDIA FY23 经营利润率仅 16%)。若模型层/应用层无法产生足够收入,~1/4 由 NVIDIA 信用支撑的需求是脆弱点。
