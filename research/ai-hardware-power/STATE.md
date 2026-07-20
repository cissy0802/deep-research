# ai-hardware-power 研究运行状态(断点恢复文件)

> 主题 #15:AI 带来的硬件短缺与电力短缺——真实规模与持续时间。
> 发布物 = `sources/ai-hardware-power-{plain,deep}.{zh,en}.md` + build.py 注册;本目录是研究底稿。
> 本期运行环境:本地交互式会话(非云 workflow);调研由主 agent 用 WebSearch/WebFetch 逐线执行,验证阶段逐条回源核验(refute-by-default)+ 单源实证加反证搜索,证据分级沿用 #14 起的双轨制。

## 计划

**状态:全部完成 ✅(2026-07-20)。** 发布物见 `sources/ai-hardware-power-*.md` 与渲染页面。

1. ✅ 调研线 1-6 → `01-raw-claims.md`
2. ✅ 承重论断提取 + 单线回源核验 → `02-verified-claims.md`(Round 1,后被 Round 2 部分推翻)
3. ✅ 成文 4 个源文件(初版)
4. ✅ 补验:12 组 × 3 票对抗验证(3 个独立 agent,单票原文 `votes/voter-{a,b,c}.md`)→ `03-verification-round2.md`;6 组单源双席审计(`votes/audit-d.md`)→ `04-verification-round3.md`;36 票 12/12 挺过、0 推翻、9 处口径修正
5. ✅ 四篇按判决修订 + build.py 注册与构建 + TOPICS.md #15 移入已发布

## 6 条调研线

1. **硬件供需**:GPU/HBM/CoWoS 先进封装的供需缺口与 lead time;TSMC/SK Hynix/Samsung/Micron 扩产时间表(财报一手);"短缺"的当前状态(2026-07)
2. **电力需求预测 vs 实测**:IEA《Energy and AI》、EIA、LBNL 2024 报告的预测口径;数据中心用电占比实测;**历史预测翻车考古**(2007 EPA 预测、2011 Koomey 修正——预测系统性高估的前科)
3. **电网约束一手数据**:PJM/ERCOT 互联排队年限与容量拍卖价格;变压器/燃气轮机 lead time;数据中心密集区电价变化(承重:是否传导到居民电价)
4. **供给响应**:微软-Constellation 三里岛 PPA、Google/Amazon 核协议的实际交付时间表;SMR 首堆时间线 vs 宣传;GE Vernova/Siemens 燃气轮机订单簿;新增发电装机结构
5. **效率对冲**:Jevons 悖论适用性;PUE 趋势;每 token 能耗下降曲线;训练→推理结构转移对需求形态的影响
6. **反方证据**:互联申请的"幽灵需求"(同一项目多地重复申请)、已取消/暂停的数据中心项目、"短缺即将缓解"派的论据;微软 Nadella"不缺芯片缺电"口径核验

## 运行日志

- 2026-07-20:TOPICS.md #15 登记并 commit(e685b53);调研线 1-6 完成(01);单线核验(02,修正 GE Vernova/内存口径两处);四篇成文;build.py 注册。
- 2026-07-20:应用户对流程完整性的质疑,补跑标准验证:3 票对抗(A/B/C 独立投票)+ 双席审计(D)。结果:12/12 挺过、0 推翻、9 处修正——包括推翻 02 自己的"现货口径"修正、Shuli Ren 归属否决、Grid Strategies vs NERC 归属修正、ERCOT 198 件勘误、账单按辖区重写。四篇 + TLDRS/CHIPS 已按判决重写并重建。
- 流程沉淀:本期教训写入仓库 `CLAUDE.md`(降级运行规则 + 红线)。

## 下一步(恢复点)

- 无。本期已发布。若后续季度数据更新(PJM 2029/30 拍卖、ERCOT 队列、内存 3Q26 合约价),按 CLAUDE.md 红线更新四版+重建。
