# ai-hardware-power 研究运行状态(断点恢复文件)

> 主题 #15:AI 带来的硬件短缺与电力短缺——真实规模与持续时间。
> 发布物 = `sources/ai-hardware-power-{plain,deep}.{zh,en}.md` + build.py 注册;本目录是研究底稿。
> 本期运行环境:本地交互式会话(非云 workflow);调研由主 agent 用 WebSearch/WebFetch 逐线执行,验证阶段逐条回源核验(refute-by-default)+ 单源实证加反证搜索,证据分级沿用 #14 起的双轨制。

## 计划

1. ☐ 调研线 1-6 → `01-raw-claims.md`
2. ☐ 承重论断提取 + 逐条回源核验 + 反证搜索 → `02-verified-claims.md`
3. ☐ 成文 4 个源文件(格式对齐 ai-capex-1999 系列)
4. ☐ build.py 注册 + `python3 build.py` + TOPICS.md #15 移入已发布 + commit/push

## 6 条调研线

1. **硬件供需**:GPU/HBM/CoWoS 先进封装的供需缺口与 lead time;TSMC/SK Hynix/Samsung/Micron 扩产时间表(财报一手);"短缺"的当前状态(2026-07)
2. **电力需求预测 vs 实测**:IEA《Energy and AI》、EIA、LBNL 2024 报告的预测口径;数据中心用电占比实测;**历史预测翻车考古**(2007 EPA 预测、2011 Koomey 修正——预测系统性高估的前科)
3. **电网约束一手数据**:PJM/ERCOT 互联排队年限与容量拍卖价格;变压器/燃气轮机 lead time;数据中心密集区电价变化(承重:是否传导到居民电价)
4. **供给响应**:微软-Constellation 三里岛 PPA、Google/Amazon 核协议的实际交付时间表;SMR 首堆时间线 vs 宣传;GE Vernova/Siemens 燃气轮机订单簿;新增发电装机结构
5. **效率对冲**:Jevons 悖论适用性;PUE 趋势;每 token 能耗下降曲线;训练→推理结构转移对需求形态的影响
6. **反方证据**:互联申请的"幽灵需求"(同一项目多地重复申请)、已取消/暂停的数据中心项目、"短缺即将缓解"派的论据;微软 Nadella"不缺芯片缺电"口径核验

## 运行日志

- 2026-07-20:TOPICS.md #15 登记并 commit(e685b53)。开始调研线 1。

## 下一步(恢复点)

- 若 `01-raw-claims.md` 不存在或不完整 → 从缺失的调研线继续
- 若 01 完整、02 缺失 → 从承重论断提取开始
- 若 02 完整 → 成文
