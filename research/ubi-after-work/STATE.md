# 24. 被供养之后 — 运行状态

- **Slug**: ubi-after-work
- **运行日期**: 2026-11-03(用户点名;#20 为上篇、尚未发布)
- **时效声明**: 成文标注「截至 2026 年 11 月」
- **运行规模**: 标准运行:7 条调研线(目标 80–160 源)、约 15–20 组承重论断 × 3 票、单源承重实证双席审计;编排用 Agent 子代理(非 Workflow)
- **联网约束(写进每个子代理 brief)**: 禁止把用户邮箱或任何个人信息放进 User-Agent、header、URL 或 payload;要求 UA 带联系方式的站点(SEC 等)用通用 UA 或跳过。

## 核心问题
如果 AI 真的让转移支付大规模化:(1)现有 UBI/现金转移试验测出了什么(工作、健康、幸福、意义),口径边界在哪;(2)失业/退休/中奖的证据说明工作的「非收入功能」有多大、钱能不能补上;(3)国民劳动不被需要时,政治议价权会不会像食利国家那样流失(intelligence curse 只给机制与可检验信号);(4)外推到「AI 之后的全民永久 UBI」的缺口在哪里。

## 与 #20 的分工(不得越界)
#20 管总量与分配(劳动份额、需求不足、恢复机制、「钱不再重要」、后稀缺);本期只管「如果真的发了钱」对个人与公民身份的效果与后果。不论证劳动份额与宏观恢复,只在开头一句承接。

## 调研线(7 条)
1. **US** 美国随机/准随机现金试验:OpenResearch(ORUS,Vivalt 等 2024)、Stockton SEED、Baby's First Years、各市保障收入试点(Denver、Cook County 等)、1970s 负所得税实验(SIME/DIME 等)、Dauphin Mincome(准实验)、切罗基赌场分红(Akee 等)。
2. **INTL** 国际试验与全民项目:芬兰 2017–18、GiveDirectly 肯尼亚长期 UBI(Banerjee 等)、Egger 等一般均衡、Haushofer-Shapiro 及长期随访、伊朗 2011 全民现金(Salehi-Isfahani)、阿拉斯加 PFD(Jones-Marinescu)、德国 Mein Grundeinkommen、印度中央邦试点、纳米比亚、加拿大安省试点、Banerjee 等 2017「懒惰福利领取者」七国再分析。
3. **WINDFALL** 意外之财与退休:彩票中奖者劳动供给与福祉(Cesarini 等 2017、Lindqvist 等 2020、Golosov 等 2024、Imbens 等 2001、Brickman 1978 及其流行误读)、退休对健康/幸福/认知的因果研究(断点、meta)。
4. **JOBLESS** 失业与工作的非收入功能:Jahoda 马林塔尔原始研究与潜在剥夺理论、Paul-Moser 2009/McKee-Ryan 2005 meta、Lucas 等 2004 不完全适应、Clark 等 2008 前后滞后、工厂关闭外生失业、收入 vs 非金钱成本分解(Winkelmann 1998 等)、失业者时间使用与日常情绪(Knabe 等 2010)、「中奖后还会继续工作吗」调查、SDT 与工作意义、享乐适应与地位竞争(个人福祉侧)。
5. **RENTIER** 议价权与食利国家:Mahdavy 1970、Beblawi-Luciani、Ross 2001/2012、Haber-Menaldo 2011 反驳及后续、税收-问责实验(Paler 2013、Weigel 2020、Martin 等)、兵役/罢工/税基与选举权扩展(Scheve-Stasavage、Acemoglu-Robinson)、挪威与海湾的反例、阿拉斯加 PFD 的政治经济学、AI 版 intelligence curse(Drago-Laine 2025)与 gradual disempowerment(Kulveit 等 2025)。
6. **VOICES** 厂商与倡导者口径:Altman(Moore's Law for Everything、universal basic compute)、Musk(universal high income)、Zuckerberg 2017、Amodei、Yang、Hughes;OpenResearch 与 GiveDirectly 的资助与自我叙事;对手方(「养懒汉」论)的一手表态;公众态度调查;UBI 设计:分红权利 vs 年度拨款、Hoynes-Rothstein 2019 对 UBI 与现有项目的比较。
7. **META** 综述与测量:现金转移系统综述(Bastagli 等 2016 ODI、Baird 等 2018 劳动供给、Evans-Popova 诱惑品)、现金对主观福祉的 meta(McGuire 等 2022)、贫困与精神健康(Ridley 等 2020 Science)、长期效应衰减(Blattman 等 Uganda 9 年、Haushofer 长期随访)、UBI 健康综述(Gibson 等 2020 Lancet PH)、幸福感测量口径(生活满意度/情绪/意义/量表)。

## 运行日志
- 2026-11-03: 登记 #24(f5b98ed,已推送)。STATE 落盘;Round 1 派 7 个调研子代理,产出 lines/<LINE>.{json,md}。

- 2026-11-03: Round 1 中途电脑休眠,INTL 续跑、WINDFALL/RENTIER/VOICES 重派;7 线全部返回:US 27 / INTL 27 / WINDFALL 24 / JOBLESS 31 / RENTIER 27 / VOICES 24 / META 27 = 187 论断,139 个独立一手来源 URL(不含 notes 内引用)。
- 2026-11-03: groups.py 合并 01-raw-claims.md;抽 22 组(groups/G01–G22)。Round 2:3 批(B1 G01–G08 / B2 G09–G15 / B3 G16–G22)× 3 镜头(逐字 Q / 反证 X / 口径 K)= 9 个验证子代理,判决落 verdicts/<G>-<镜头>.md,共 66 票。
- 2026-11-03: Round 3 并行派 5 条单源承重实证 × 反证席 X / 方法席 M = 10 子代理:R1 ORUS 劳动供给与时间去向;R2 巴塞罗那 B-MINCOME −22%;R3 失业者退休(Hetschko)与社会规范缓冲;R4 德国 Mein Grundeinkommen 心理健康/人生意义;R5 阿拉斯加 PFD 与投票率(对照 gradual disempowerment 预测)。产出 r3/R*-{X,M}.md。

- 2026-11-03: Round 2 全部返回:66 票 = 4 HOLDS / 62 修正 / 0 组级推翻;子论断推翻 2 处(I22 德国「意义延迟」、R09 Andersen-Ross 引语),W16「80%」禁写。Round 3 全部返回:10 份审计,5 条全部降级或拆分,34 项否决;3 处方向升级多源。限制:WebSearch 共享配额在 Round 2 后段至 Round 3 耗尽,部分反证检索改为 DOI 直取与引用追踪(已在 04 披露)。02/03/04 落盘。非降级运行(3 票制与双席均由独立子代理完成)。

## 下一步
成文 zh deep → zh plain → en(子代理翻译后回核引语)→ build.py 注册 → TOPICS 归档 → 钩子。
