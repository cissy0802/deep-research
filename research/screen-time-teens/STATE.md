# Run state — screen-time-teens (#11 屏幕时间与青少年心理健康:Haidt 对不对?)

- Started: 2026-07-27 (scheduled weekly-deep-research run)
- Slug: `screen-time-teens`
- Topic: 《焦虑的一代》的因果主张,经得起方法学检验吗?

## 调研线拆法(重叠检查后定 5 条)

本期题目是"单一争议、双方阵营清晰"型:正反双方都有重量级学者且已在公开文档逐条对账,所以不开发现型线索,按证据类型切 5 条:

1. **L1 正方一手**:Haidt/Twenge 的完整论证(时序 2012 拐点、剂量、国际同步、集体行动问题框架)+ 逐字引语 + 公开协作文档(与批评者对账的 Google Docs)。独占证据:Anxious Generation / After Babel / 协作评审文档。
2. **L2 反方一手**:Odgers/Przybylski/Orben 的方法学批评(specification curve、"土豆"效应量、因果方向、Nature 书评)。独占证据:批评方论文的确切效应量与措辞。
3. **L3 因果证据**:自然实验(Braghieri Facebook rollout)+ 剥夺/减用 RCT + RCT meta 分析。**不含学校禁手机评估(归 L5)**。独占证据:因果设计研究。
4. **L4 趋势数据审计**:青少年心理指标是否真的在恶化、在哪些国家、测量伪影(诊断编码/报告倾向变化)、国际同步性主张体检。独占证据:官方统计与趋势研究。
5. **L5 2024-2026 新进展与政策自然实验**:学校禁手机评估(挪威/英格兰/荷兰)、澳大利亚 16 岁以下禁令、2024 后新 meta、Haidt-批评者新交锋。独占证据:政策评估与最新文献。

## 运行日志

- [x] git pull、读 TOPICS/CLAUDE/build.py 版式
- [x] Round 1 调研(5 线并行,wf_fd87e84a-732,~53 万 tokens)→ line1-5.md(约 107 条论断)
- [x] 承重论断分组:24 组 → 02-claims-for-verification.md
- [x] Round 2 完成:24 组 × 3 票 opus(wf_b68deb94-356,72 票,6.16M tokens):票级 3 HOLDS / 69 CORRECTED / 0 REFUTED;分票 JSON 在 r2-votes/C01-C24.json
- [x] 合并判决完成(r2-merged/C01-C24.md):组级 1 HOLDS(C03)/ 23 CORRECTED / 0 REFUTED;票级 3H/69C
- [x] Round 3 完成(10 席):nagata 反证席=升级多源;其余 9 席=限制使用(附条件);两处实质否决:Abrahamsson"专科就诊-60%"与"霸凌下降"不得承重、Currie"自伤/未遂平"全国口径不得承重(作者 2025 全国续作自行修正:自伤 ED +77% > 自杀死亡 +66%)
- [x] 03-verification-round2.md / 04-verification-round3.md 落盘
- [ ] writing-calibers.md 蒸馏中(agent a8f3...)——40-60KB 成稿口径表
- [ ] 成文 4 版 → sources/(slug=screen-time-teens)
- [ ] 一致性回查 agent
- [ ] build.py 注册 + FIGURES + python3 build.py
- [ ] TOPICS.md 移已发布 + commit + push + curl 验证
- [ ] 钩子收割 + 收尾报告

## 下一步(断点恢复用)

已完成并发布(2026-07-28)。TTS bake workflow 在 push 后自动运行,新页面的 data-tts 由 bot 注入——本地不要手动重跑 build.py 覆盖(会剥掉全站已烘焙的 data-tts;本期已踩过一次,靠 git checkout 还原)。

发布物:
- 页面 https://hub.cissychen.com/deep-research/screen-time-teens-{plain,deep}{,.en}.html(均 200)
- 研究材料已归档进仓库 research/screen-time-teens/(含 72 张分票 JSON)
- 钩子:候选池 2 条 + meta-knowledge Day 72 + leadership Day 72(均已单独 commit push)
