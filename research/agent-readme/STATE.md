# agent-readme 研究运行状态(断点恢复文件)

> 用途:Fable quota 可能中断运行;每个阶段的中间结论物化到本目录并 push,恢复时从「下一步」继续。
> 分支:`claude/readme-agent-discovery-plan-ufc90m`。最终发布物是 `sources/agent-readme-{plain,deep}.{zh,en}.md` + `build.py` 注册;本目录是研究底稿,发布不依赖它,但保留作为验证底座存档。

## 总计划(已获批准,全文见 commit 历史或 /root/.claude/plans/deep-research-topic-industry-readme-fil-zany-quasar.md)

1. ✅ TOPICS.md 登记 #14(commit 1668b95)
2. ⏳ deep-research workflow:多线调研 → 承重论断 3 票对抗验证
3. ☐ 成文 4 个源文件(格式对齐 sources/machine-oracles-*):
   - deep 版:H1 带"(深入版)/(Deep Dive)"、blockquote 方法学前言(票数统计)、`## N.` 编号章节、`【verified】/【unverified, source: …】` 标注、结尾来源索引、落地 playbook 独立章节
   - plain 版:blockquote 指向深入版,无 inline 验证标注
4. ☐ build.py 注册:ARTICLES 4 条 tuple(约 L1535)+ INDEX_ENTRIES 1 条(约 L1938);`python3 build.py` 构建验证
5. ☐ TOPICS.md #14 移入「已发布」(底座统计+钩子 ≤5 条),commit + push

## 已确认的范围决定(用户 2026-07-15)

- 全流程跑完发布;落地 plan = 通用 playbook 章节(可发布);生态全平铺(AGENTS.md/CLAUDE.md/Cursor rules/Copilot instructions/GEMINI.md/llms.txt),重点在跨生态共识与标准之争。

## 7 条调研线(deep-research args 起点,原文见 TOPICS.md #14)

1. 标准之争与采用现状(含 llms.txt 单独体检:Google 表态不消费)
2. 厂商官方最佳实践一手汇总(Anthropic/OpenAI/GitHub Copilot/Cursor;共识 vs 矛盾;厂商口径单独标注)
3. 实证体检(对抗验证主战场):带/不带 context 文件对照评测、遵从率研究、context rot 文献
4. 大型开源库实地考察(根级 vs 分层、monorepo、自动生成 vs 手写、git log 更新频率)
5. 反模式与坑(文档腐烂、超长文件、复制 README、prompt injection 攻击面、agent 忽略指令、维护成本)
6. 维护与工程化(docs-as-code、CI 校验、/init 与 repomix 类工具边界、效果度量)
7. 落地 playbook 综合(盘点→试点→模板分层→rollout→度量→维护 owner;每步标证据等级)

## 运行日志

- 2026-07-15:计划获批;TOPICS.md #14 已登记并 push(1668b95)。
- 2026-07-15:启动 deep-research workflow(5 角度并行搜索 → 抓取 15 源 → 3 票对抗验证 → 综合)。
- (workflow 完成后:把 findings/claims/verdicts 写入本目录 `01-search-*.md`、`02-claims.md`、`03-verification.md`、`04-synthesis.md`,commit + push)

## 下一步(恢复点)

若 workflow 已完成且本目录有 04-synthesis.md → 从步骤 3(成文)继续。
若本目录只有本文件 → 重跑 deep-research workflow(args 用上面 7 条线的摘要)。
