# 23. 以牙还牙还是赢家吗 — 运行状态

- **Slug**: axelrod-tournament
- **运行日期**: 2026-10-31(BigCat 点名插队)
- **时效声明**: 成文标注「截至 2026 年 10 月」
- **运行规模**: 按 #22 小一档:5 条调研线、约 12 组承重论断 × 3 票、单源承重实证双席审计;编排用 Agent 子代理(非 Workflow)

## 核心问题
Axelrod 1980 两届锦标赛到底发生了什么(口径)?TFT 夺冠与「四原则」在四十年后的文献里还剩多少:噪声、ESS、零行列式、合谋、ML 进化策略、人类/动物证据、LLM 锦标赛。

## 调研线(5 条)
1. **ORIGIN** 原始锦标赛口径:JCR 1980a/b、Science 1981、1984 书;参赛数、轮数、终止规则、得分、生态模拟、TFTT 反事实、「四行代码」等流行细节。
2. **NOISE** 噪声与理论:Molander 1985、Boyd-Lorberbaum 1987、Nowak-Sigmund 1992/1993、Wu-Axelrod 1995、无名氏定理。
3. **ZD** 零行列式:Press-Dyson 2012、Stewart-Plotkin 2012/2013、Adami-Hintze 2013、Hilbe 等实验。
4. **MODERN** 后续锦标赛:2004/2005 二十周年赛与南安普顿合谋、Axelrod-Python(Knight 2016、Harper 2017)、TFT 在大规模锦标赛中的排名。
5. **EVIDENCE** 现实与 LLM:人类实验(Dal Bó-Fréchette)、动物互惠证据、一战堑壕、LLM 重复博弈实验(Akata 2025 等、2025 演化锦标赛预印本)。

## 运行日志
- 2026-10-31: 登记 #23(c1f55f0);STATE 落盘;Round 1 派 5 个调研子代理。

## 下一步
等 5 条线返回 → 合并 01-raw-claims.md → 抽组。
- 2026-10-31: Round 1 全部完成:ORIGIN 30 / NOISE 30 / ZD 28 / MODERN 30 / EVIDENCE 32 = 150 论断。要点:第一届 14+RANDOM、TFT 504.5 vs 500.4;「四行」= FORTRAN 四行;参赛者事先收到预赛报告(TFT 非黑马);生态模拟 Science「fixation」vs 1980b 第 1000 代 14.5% 冲突;南安普顿 112 个(Wired 60 为媒体口径);Wu-Axelrod 1995 带噪重跑 GTFT/CTFT 胜;Knight 2025 复现第二届只 63.3% 种子夺冠;Payne 2025 LLM 锦标赛为未评审 v1。
- 2026-10-31: 01-raw-claims.md 合并;抽 14 组(groups/G01–G14,groups.py 生成)。Round 2:2 批(B1 G01–G07 / B2 G08–G14)× 3 镜头(逐字 V / 反证 R / 口径 K)= 6 个验证子代理,判决落 verdicts/<G>-<镜头>.md。
