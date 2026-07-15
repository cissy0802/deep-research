# agent-readme 研究运行状态(断点恢复文件)

> 用途:Fable quota 可能中断运行;每个阶段的中间结论物化到本目录并 push,恢复时从「下一步」继续。
> 分支:`claude/readme-agent-discovery-plan-ufc90m`。最终发布物是 `sources/agent-readme-{plain,deep}.{zh,en}.md` + `build.py` 注册;本目录是研究底稿,发布不依赖它,但保留作为验证底座存档。

## 总计划(已获批准,全文见 commit 历史或 /root/.claude/plans/deep-research-topic-industry-readme-fil-zany-quasar.md)

**状态:全部完成 ✅(2026-07-15)。** 本文件保留作研究底座存档;发布物见 `sources/agent-readme-*.md` 与 `agent-readme-*.html`。

1. ✅ TOPICS.md 登记 #14(commit 1668b95)
2. ✅ deep-research workflow:Round 1(wf_71d43d15-568)+ Round 2 对抗验证(wf_9f678178-eaf),105 票 35/35 挺过
3. ✅ 成文 4 个源文件(commit 5a45bbf);✅ build.py 注册与构建(commit 31d731c);✅ TOPICS.md #14 移入已发布
4. 原步骤清单(存档):成文 4 个源文件(格式对齐 sources/machine-oracles-*):
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
- 2026-07-15:Round 1 deep-research workflow 完成(wf_71d43d15-568):108 agents、26 源、124 论断提取、25 条验证全部 3-0 挺过。**但 25 条全部落在线 1-2(标准之争、厂商最佳实践)**;线 3-7 的原始论断已提取但未进入验证。
  - `01-raw-claims.md`:26 个来源的全部原始论断(含线 3-7 的关键一手材料:arXiv 2602.11988 AGENTbench 对照、2605.10039 遵从率因子实验、2511.12884 2303 文件实证、2601.20404 Codex 效率对照、Chroma context rot、Ahrefs llms.txt 137k 域名实测、NVIDIA AGENTS.md 注入 PoC、prompt.security VS Code 攻击面、Anthropic large-codebases 文档、Sentry/Cloudflare/Airflow 生产实例)
  - `02-verified-claims.md`:Round 1 已验证的 10 组合并结论(全部线 1-2)+ caveats + open questions
- 2026-07-15:Round 2 第一次启动因 quota 失败(0 票);重试后完成:**10/10 组全部 3-0 挺过,大量口径修正**,详见 `03-verification-round2.md`。研究阶段完成,进入成文。

## 下一步(恢复点)

- 若本目录有 `03-verification-round2.md` 且完整 → 研究阶段完成,从计划步骤 3(成文 4 个源文件)继续,材料 = 02 + 03(+01 作背景色)。
- 若 03 缺失/不完整 → 重跑 Round 2:承重组是 (V1) arXiv 2602.11988 数字组、(V2) arXiv 2605.10039 数字组、(V3) arXiv 2511.12884 数字组、(V4) arXiv 2601.20404 数字组、(V5) Chroma context rot、(V6) llms.txt(Ahrefs 数字+Mueller/Illyes 表态+Lighthouse 矛盾)、(V7) NVIDIA 注入 PoC、(V8) VS Code 自动注入 AGENTS.md、(V9) Anthropic large-codebases 官方口径、(V10) Sentry/Cloudflare/Airflow/coder 生产文件逐字核验;每组 3 票,refute-by-default。
