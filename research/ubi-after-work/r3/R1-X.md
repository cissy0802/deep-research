# R3 · R1-X 反证搜索席
靶子:R1「高收入国家无条件现金使劳动供给小幅下降:ORUS 参与 −4.2pp、工时 −1–2h/周,释放时间主要流向休闲」(U02–U07)

今天复核了:
- Bernhard, Bohmann, Fiedler, Kasy, Schupp, Schwerter (2026-03-28) *Basic income and labor supply: Theory and evidence from an RCT in Germany*,https://maxkasy.github.io/home/files/papers/basic_income_econ.pdf (全文 pdftotext,表 2–4)
- DIW Wochenbericht 15/2025(Bohmann 等),https://www.diw.de/de/diw_01.c.945347.de/publikationen/wochenberichte/2025_15_1/pilotprojekt_grundeinkommen__kein_rueckzug_vom_arbeitsmarkt__aber_bessere_mentale_gesundheit.html
- Golosov, Graber, Mogstad, Novgorodsky,NBER w29000 / QJE 139(2) 2024,摘要页
- Cesarini, Lindqvist, Notowidigdo, Östling,NBER w21762 / AER 2017,摘要页
- Jones & Marinescu,NBER w24312(阿拉斯加 PFD),摘要页
- Ananat, Glasner, Hamilton, Parolin,NBER w29823(2021 CTC),摘要页
- Verho, Hämäläinen, Kanninen,AEJ:Policy 14(1) 2022(芬兰),摘要页
- ORUS NBER 摘要页 w32719(确认 QJE 141(4) 已刊)

没拿到:本轮 WebSearch 配额在会话层面已耗尽(首次调用即被拒),以下只能靠直连已知 URL,未能定位/复核:NIT 四实验(SIME/DIME 等)原始汇总、Price & Song 长期随访、巴塞罗那 B-MINCOME 终报、Compton Pledge 评估、Baby's First Years 母亲就业论文、AEI 2026 汇总、Golosov/Cesarini 正文中的时间使用部分。以上均不进入本席证据。

## 一、发现
1. **德国 RCT(独立团队、独立行政数据 IAB,预注册 AEARCTR-0007734,€1,200/月×3 年,2021-06 起)**——最直接的独立复现。
   - 外延:就业 ATE −0.003(SE 0.025,表 2),可排除 ±5pp 以外效应;失业金领取无变化。
   - 内延:全职 −5.1pp(SE 2.7,p≈0.065)、兼职 +3.0pp(ns);自报工时 −1.35h/周(SE 1.02,p=0.19,表 3)。
   - 时间:与亲友伴侣共处 +3.8h/周(DIW);睡眠 +约 1h;志愿/运动/教育/其他休闲差异小且不显著;培训/在读 +2.6pp(ns);求职时数 −0.35h/周(p=0.012,表 4)。
   - 作者自述其结果与 Vivalt 等"大体一致",但引用的是 2024 初版 2pp。
   - 注意可比性:样本基线**全部在职**、单身独居、收入 €1,100–2,600,处理组仅 107 人(功效:80% 只能检出 ±6.2pp)。ORUS 的 −4.2pp 落在其 95% CI(约 −5.2~+4.6)之内——**不能拒绝,也不能证实**。
2. **Golosov 等(美国彩票,行政税务数据)**:每 $1 非劳动收入使税前劳动收入约 −$0.50,高收入四分位降得更多。ORUS 隐含:−$1,900/$12,000 ≈ −0.16。方向一致,彩票为一次性财富冲击、样本非低收入定向,量级不可直接比。
3. **Cesarini 等(瑞典彩票,行政数据)**:收入"适度"下降、立即且持久,终身边际收入倾向 −0.11;Kasy 文转述为"工时降、就业不降"。方向一致,量级与 ORUS −0.16 同一数量级。
4. **阿拉斯加 PFD(Jones & Marinescu,CPS + 合成控制)**:就业无影响,兼职 +1.8pp(17%)。全民、永久、金额小、含一般均衡效应——与"外延 −4.2pp"矛盾,但设定不同。
5. **2021 扩大版 CTC(Ananat 等,CPS/Pulse DiD)**:就业与参与"很小、符号不一、不显著"。金额小、6 个月——外延零效应,弱反证。
6. **芬兰(Verho 等)**:以基本收入替代失业金,就业效应"至多很小"。人群(失业者)与机制(拆福利陷阱)不同,不能用来证伪 ORUS 的收入效应。

## 二、结局
**拆分判定**:
- **方向(劳动供给小幅下降、主要在内延/工时)→ 升级多源证实**。德国 RCT 工时 −1.3h 与 ORUS 调查口径 −1.3h(U03)几乎相同,两国彩票研究方向一致;但德国这一项单独不显著。
- **量级:外延参与 −4.2pp → 方向存争**。德国、阿拉斯加、CTC、芬兰四个独立来源外延均≈0;ORUS 的 −4.2pp 主要由 UI 行政口径(−6.6pp)驱动,调查口径仅 −2.3pp。高收入国家文献里它是外延效应的**上端孤例**。
- **时间流向休闲 → 维持单源已核,德国部分呼应**:德国增量集中在社交时间与睡眠,"休闲"大类不显著;两者都未发现转向培训/求职(德国求职时间反而显著下降),"未被生产性活动抵消"这一点方向一致。

## 三、成文时可以怎么写 / 不得怎么写
可以写:
- "美德两国独立随机试验都发现,每月约 $1,000–1,200 的无条件现金使每周工时少约 1.3 小时,主要表现为全职转兼职,而不是退出劳动力。"
- "彩票研究(瑞典、美国)同样显示非劳动收入会小幅压低劳动收入。"
- "ORUS 的参与率 −4.2pp 在同类研究中偏高,且依赖行政数据口径;德国、阿拉斯加、2021 儿童税收抵免均未见就业率下降。"

不得写:
- "多项研究证实无条件现金使就业率下降约 4 个百分点。"(外延量级无独立证实)
- "德国试验证明基本收入对劳动供给毫无影响。"(n=107,CI 宽,工时与全职点估计都朝下)
- 用阿拉斯加/CTC/芬兰直接"推翻" ORUS(金额、人群、期限、机制都不同)。
- "释放的时间被普遍用于休闲"作为跨国结论——只有 ORUS 一源显著。
