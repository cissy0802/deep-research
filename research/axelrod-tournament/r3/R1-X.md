# R1-X 反证席：第二届「生态 / 未来世代」模拟——TFT 是否 fixation？

## 判决：降级（「went to fixation」不可作事实印）；「第1000代时份额最大且仍在增长」= 方向一致、多源支持；「14.5%」= 单源转引未见原文

- 「fixation」只有 Axelrod & Hamilton 1981 Science 一处说，且注 24 引的是 1980b JCR——而 1980b 据转引只报告到第 1000 代（14.5%、仍在增长），没有跑到固定。即 Science 是对 1980b 的外推表述。
- Axelrod 本人 1988（与 Dion，Science）已收回到「quickly became the most common strategy」，不再说 fixation。
- Hirshleifer & Martinez Coll 1988 JCR 明确反驳：TFT「does not approach 100% fixation」。
- 没找到任何独立复现 Axelrod 原 1000 代生态模拟的工作（Knight et al. 2025 没做这个）。
- **纠正背景笔记**：Binmore「a little more than 1/6」不是 Axelrod 第 1000 代的读数，而是 Axelrod 加 Linster（无限重复版重跑）收敛后的混合均衡，与 14.5% 不是同一个量。

## 证据

1. **Axelrod & Hamilton 1981, Science 211:1390**。全文 PDF（JSTOR 盖章副本）：https://the-foundation-series.netlify.app/teaching/3-order-and-chaos/modules/2-strategies-in-pd/Axelrod-Hamilton.pdf
   已用 pdftotext 抽出原句：「The results showed that, as the less successful rules were displaced, TIT FOR TAT continued to do well with the rules which initially scored near the top. In the long run, TIT FOR TAT displaced all the other rules and went to fixation (24).」注 24 =「R. Axelrod, J. Conflict Resolution 24, 379 (1980)」，即 1980b。措辞是「In the long run」，没给代数，也没给份额。
2. **Axelrod 1980b JCR 24:379–403, p.401**（付费，未见原文）。经 Ostrom 2007《Biography of Robert Axelrod》（PS 40(1):171–174）转引，来自搜索摘要：「By the 1000th generation, it was 14.5% of the whole population . . . 」，仍以约 .05%/代增长，「faster rate than any other rule」；同处还说「never losing its slight lead」。直连 cambridge.org 只拿到摘录页，代理链接按规则未用。→ 单源转引。
3. **Axelrod & Dion 1988, Science 242:1385**。https://public.websites.umich.edu/~axe/research/Axelrod%20Dion%20Further%20EC%20Science%201988.pdf ，pdftotext 原句：「In this ecological simulation, TFT quickly became the most common strategy.」——这是 Axelrod 本人后来的口径，已无 fixation。
4. **Hirshleifer & Martinez Coll 1988, JCR 32(2):367–398**。https://ideas.repec.org/a/sae/jocore/v32y1988i2p367-398.html ，摘要：「TIT-FOR-TAT does not approach 100% fixation in the population」，并称 PUNISHER 会产生合作与不合作策略共存的内点均衡。→ 直接反证。
5. **Binmore 1998, JASSS 1(1) review1**（评 *Complexity of Cooperation*）。https://jasss.soc.surrey.ac.uk/1/1/review1.html
   - 「TIT-FOR-TAT is the most numerous, but nevertheless controls only a little more than 1/6 of the population」；「Actually a mixture of strategies survives」。
   - 语境是 Axelrod 与 Linster 的工作（Linster 1990/1992，无限重复版），系统收敛到混合 Nash 均衡、TFT 概率约 1/6。没给代数。
   - Linster 遍历所有初始条件后，TFT「only about 1/4 of the time」是份额最大者；Axelrod 自己试了 6 个初始条件，TFT 5 次份额最大。
6. **Hoffmann 2000, JASSS 3(2) forum/1**。https://jasss.soc.surrey.ac.uk/3/2/forum/1.html ¶2.3：「after one thousand generations, reciprocating cooperators accounted for about 75% of the total population」；「TFT itself displayed the highest representation among all」。这一段没有引注，也没有 fixation。
7. **Knight, Campbell, Harper, Gaffney, Glynatsi 2025**，arXiv:2510.15438。https://arxiv.org/html/2510.15438v1 ：只复现了锦标赛排名（TFT 在 63.3% 的随机种子下胜出），没有做生态 / 种群模拟。查 GitHub 仓 Axelrod-Python/revisiting-axelrod-second 的文件树，也没有 ecosystem 相关代码。
8. **Axelrod-Python 文档 ecological_variant 教程**（github.com/Axelrod-Python/Axelrod docs/tutorials/further_topics/ecological_variant.rst）：只有一个通用的 Ecosystem 工具，没有发布对第二届 63 条规则的 1000 代复跑结果。
9. **弱二手来源**：
   - Cornell INFO2040 博客：「within a few hundred generations … occupying over 14%」（引 1984 书）。
   - Bart Stewart 网页：「the most prevalent strategy at the end of 1000 rounds」+「the strategy with the highest rate of growth」，未给引注。
   - 2003 年课程讲义 axeltmts.pdf：「1000 "generations"… Winner = Tit-for-Tat」。
   三者都没说 fixation。

## 搜索角度（含落空的）

- 「1000th generation」「14.5%」→ 找到 Ostrom 转引（代理链接未用；直连只有摘录）。
- Knight 2025 / Fortran 复现 → 有，但不含生态模拟（全文 + 仓库文件树都查了）。
- Science 1981 原文措辞 → 拿到 PDF，核了原句和注 24。
- Axelrod & Dion 1988 → 拿到 PDF，核了原句。
- Binmore 1/6 的出处语境 → 是 Linster 重跑，不是第 1000 代读数。
- Hoffmann 75% 的引注 → 没有引注。
- 「went to fixation」反驳 → 找到 Hirshleifer & Martinez Coll 1988。
- Axelrod-Python ecological 文档 → 只有工具，没有结果。
- 1980b 全文（econpapers / scilit / umich）→ 没有免费全文。MIT 链接走 ezproxy，未用。
- 1984 书第 2 章（Figure 2，生态成功曲线）→ archive.org 四个本子的 fulltext 检索都返回 403（借阅受限）；USP e-Disciplinas 要登录。**Figure 2 实际画了什么、到第几代，本席未能核实。**
- 「By the one-thousandth generation」「never lost this lead」短语搜索 → 没有命中书的原文。
- Linster 1992 的 TFT 具体份额（DTIC ADA224480）→ 没打开。
- Dawkins《Selfish Gene》第 12 章、Nowak/Sigmund 评述 → 没找到具体份额 / 代数的表述。Nowak & Sigmund 1992 只确认了一点：有噪声时 TFT 不是最终胜者。
- 落空的结论：没有任何独立来源说原生态模拟里 TFT 达到了 100%。

## 文章可安全印的句子

> 在 Axelrod 用第二届 63 条规则做的「生态」模拟里（每一代按上一代得分比例重新分配份额），TFT 从头到尾保持领先；据 Axelrod 1980 年论文的转述，到第 1000 代它约占 14.5%，是份额最大、增长最快的规则，但并没有一统天下——存活下来的是一批「善良」的互惠策略。Axelrod 与 Hamilton 1981 年在 Science 上写的「最终取代所有规则、走向固定」，是对这一趋势的长期外推，Axelrod 本人 1988 年已改口为「迅速成为最常见的策略」。

（若不想挂「转述」，就删掉 14.5%，改为「到第 1000 代份额最大、仍在增长」——这一点有 1988 Science 原文和多份二手材料共同支持。「1/6」「75%」都不要和「第 1000 代」并列：前者来自 Linster 的变体模型；后者 Hoffmann 没给引注，而且统计的是互惠合作者合计。）
