# 18. AI 价值链的利润池会落在哪一层? — 运行状态

- **Slug**: ai-profit-pools
- **运行日期**: 2026-10-05(自动 routine)
- **时效声明**: 成文标注「截至 2026 年 10 月」(最新季报:NVIDIA Q2 FY27 截至 2026-07-26;云厂商 2026 Q2)
- **底稿位置**: repo research/ai-profit-pools/(~/design/deep-research-runs/ai-profit-pools 为其软链)

## 2026-10 刷新要点(定题依据,均待验证)
- NVIDIA Q2 FY27(截至 2026-07-26,8-26 发布):总收入 $96.2B,数据中心 $89.0B(同比 +117%),GAAP 毛利率 75.0%。
- 四大云厂商 2026 capex 合计指引约 $650-725B(各家口径不同,待核);Meta 指引上调至 $130-145B;微软把建筑使用年限 15→25 年把部分租赁移出 capex(待核)。
- 前四大云厂商 4 个季度(至 2026-03)购置 PP&E $433.9B vs 折旧约 $149B(二手分析,待核)。
- OpenAI 年化收入约 $70B(2026-09,媒体/二手);FT 2026-09 报道 2026–2030 累计负自由现金流 $278B;毛利 33%、Anthropic 40%(二手,待回一手报道)。
- Anthropic 年化收入 $30B(2026-04,媒体)。

## 调研线(7 条,重叠检查后;题目是「五层价值链 × 四套叙事 × 口径混战」,按层切线 + 理论线 + 跨层资金流线)
每条线独占产出:
1. **T 理论与历史类比**——Bain 利润池、微笑曲线(施振荣)、Christensen 利润守恒、Thompson 聚合者、1999 光纤/铁路/电力/PC Wintel 的利润分布数字。独占:原典逐字 + 历史各层利润分配数据。
2. **CHIP 芯片层**——NVIDIA/AMD/Broadcom/TSMC/SK hynix 收入与毛利时序;自研芯片(TPU/Trainium/MTIA/Maia)成本与份额;CUDA 护城河正反;DeepSeek-R1 冲击事件研究。独占:半导体财报数字。
3. **CLOUD 超大云厂商层**——MSFT/GOOG/AMZN/META(+Oracle)「AI 收入」口径、capex、折旧年限变更、云业务经营利润率、RPO/积压订单。独占:云厂商财报与 10-K/10-Q 口径。
4. **PHYS 算力租赁与电力层**——neocloud(CoreWeave/Nebius/Lambda)财报与债务、GPU 小时租价时序、电力/IPP/公用事业利润与电网接入稀缺、数据中心物业。独占:租价与电力经济学(复用 #15 底座,只取"谁拿走稀缺租金"角度)。
5. **MODEL 模型层**——前沿实验室收入/亏损/毛利(多为厂商口径或媒体转述)、API 定价时序、同等能力每 token 价格降速(Epoch/a16z)、开源权重追赶与蒸馏、推理成本结构。独占:模型层单位经济学。
6. **APP 应用/分发层**——AI 应用公司毛利(Cursor/Perplexity/Replit 等对模型供应商的依赖)、聚合者(Google/Apple/Meta/微软的分发)、模型公司纵向整合(ChatGPT C 端、Claude Code、订阅)。独占:应用层单位经济学与分发争夺。
7. **FLOW 跨层资金流与总量**——"$600B 问题"类收入缺口测算、循环融资(NVIDIA-OpenAI、AMD-OpenAI 认股权、Oracle-OpenAI、CoreWeave)、供应商融资、各层收入/利润总量的第三方估算。独占:跨层资金流与总量账。

## 运行日志
- 2026-10-05: 取题(#18 为待研究首条)、刷新搜索 3 次、STATE 落盘。
- 2026-10-05: Round 1 启动 wf_231fd921-f2c(7 agents),各线落盘 lines/<key>.md。断点恢复:`Workflow({scriptPath: "<repo>/research/ai-profit-pools/round1.workflow.js", resumeFromRunId: "wf_231fd921-f2c"})`。
- 2026-10-05: **Round 1 完成**(wf_231fd921-f2c,7 agents,1.17M tokens,547 次工具调用,0 失败)。246 条论断、160 条承重候选,落盘 01-raw-claims.json/.md + lines/*.md。
  分线:T 38/27★、CHIP 33/22、CLOUD 32/25、PHYS 33/21、MODEL 38/23、APP 33/17、FLOW 39/25。
- 2026-10-05: Round 2 启动 wf_88852845-cda(31 组 × 3 票 = 93 票,12 批 × 3 = 36 agents;三镜头:逐字/反证/口径;B01-B02 理论原话与历史数字用 sonnet,其余 opus)。
  **断点恢复**:`Workflow({scriptPath: "<repo>/research/ai-profit-pools/verify-round2.workflow.js", resumeFromRunId: "wf_88852845-cda"})`。
  规模依据:本题是「数字混战型」——五层各自财报口径(财年错位/GAAP vs non-GAAP/run-rate vs 确认/承诺 vs 落地)+ 非上市实验室的泄露数字,承重论断约 150 条子论断,同源同口径并成 31 组。

## 文章设计草案(Round 2 前,待验证后定稿)
核心判断候选:
1. **当下利润分布**:压倒性在芯片层,且稀缺租金在芯片层内部向上游迁移(GPU→CoWoS→HBM/DRAM:Micron/SK hynix 经营利润率已超过 NVIDIA,NVIDIA 下调毛利指引)。云层分部经营利润率高(35-41%)但自由现金流转负;neocloud 是带杠杆的折旧套利(利息>调整后经营利润);电力层持久但薄(能源约占 TCO 7%,容量价被政治封顶);模型层除 Anthropic adjusted 外亏损;应用层的利润落在握有分发的现有巨头(Google/Meta/微软/Apple),AI 原生应用毛利薄。
2. **"嫁衣"方向反了,而且层与层互相持股**:现金从模型层流向上游(微软 FY26 从 OpenAI 收 $24.1B),信用与股权从上游流回模型层(NVIDIA 近 $50B 投资 + $105B 担保 + 明年约 1/4 业务靠资产负债表支撑),模型层的估值又以未实现收益记回上游 GAAP 利润(Amazon $50.5B ≈ 3× AWS 经营利润)。「哪一层赚钱」在会计上已不可分——真正的问题变成「谁承担模型层的信用风险」。
3. **两条价格曲线**:固定能力价格每年降约一个数量级(商品化叙事对),前沿旗舰价格逐代上调、开源落后约 4 个月且未收窄(前沿溢价叙事也对)——两派说的是两条不同的曲线;模型层能否赚钱取决于需求留在前沿还是滑向「够好」。
4. **理论给不出答案,但给得出判据**:Christensen「性能不够好→整合者赚」vs Thompson「供需平衡后→用户触点赚」;两者对 AI 的分歧可归结为一个可观测量:客户是否认为当前能力「够好」。
5. **历史类比的失效点**:光纤/铁路的「建设者破产、使用者赢」依赖长寿命资产被廉价接手;GPU 3-6 年折旧,泡沫后不会留下廉价遗产——留下的是电力、场地和 fab。
- 2026-10-05: **Round 2 完成**(wf_88852845-cda,36 agents 全成功,4.16M tokens,1416 次工具调用,21 分钟)。组级票型:90 CORRECTED / 3 HOLDS / 0 REFUTED;31 组中 30 组全票需修正。产出 02-verification-round2.json、03-verdicts-full.md。锁定口径由汇总 agent 写入 05-locked-calibers.md(成文唯一依据)。
- 2026-10-05: Round 3 启动 wf_d2a6b23c-b3a(3 条单源承重实证 × 反证席/方法席 = 6 agents):R1 Epoch 电力占 TCO 7%、R2 两条价格曲线、R3 Anthropic 季度确认收入超 OpenAI。
- 2026-10-05: **Round 3 完成**(wf_d2a6b23c-b3a,6 agents,429k tokens):R1 电费占 TCO 升级多源(约 7%–17%),但「电力租金薄」被方法席否决(成本占比 ≠ 租金;晚通电一年机会成本约为全年电费 10 倍);R2 两席均判方向存争 → 改写为「固定能力最低价 vs 前沿每任务成本」,标价为分层;R3 反证席升级多源(Bloomberg+WSJ 各自看到材料)、方法席降级(OpenAI 一端单源;gross vs net;仅 Q2 一季 adjusted 盈利)。产出 04-verification-round3.md。
- 2026-10-05: 6 个汇总 agent 合并 93 票为 05-locked-calibers.md。成文:zh 深入版/易读版手写,en 两版由翻译 agent 忠实翻译;8 张内联 SVG(qlmanage/headless Chrome 双语渲染检查,修 5 处溢出/碰撞/标签悬空);build.py 注册四处,无 WARN。钩子:system-design Day 57 已单独 commit+push(60df35e);候选池 1 条随发布 commit。
