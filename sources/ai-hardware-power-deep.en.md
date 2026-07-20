# AI's Hardware Shortage and Power Shortage: Real, and For How Long? (Deep Dive)

> Methodology note: this issue ran as a single-thread verification pass (not the 3-vote adversarial panel of earlier issues), with grading tightened to compensate — any number that could not be traced to a primary document was downgraded or dropped. Load-bearing claims were checked against primary sources one by one; two circulating figures were corrected in the process (GE Vernova "sold out through 2030" and the memory "+90%" print — see text). Evidence grades: 【multi-source】 = ≥2 independent sources concur; 【single-source, checked】 = primary document traced; 【contested】 = independent sources conflict; 【vendor claim】 = interested party's own statement — direction usable, magnitude not. All figures as of July 2026; memory prices and auction results move quarterly.

## 0. Two questions, split into four

"Is AI causing a hardware shortage and a power shortage, and how long will they last?" — the question as usually asked assumes the shortage is one thing. The first step of the physical is to split it: hardware and power are two shortages of entirely different natures, and "is it real" is independent of "are the forecasts credible."

The shape of the answer up front: **the hardware shortage is a price-clearing shortage** — the market still clears, prices have doubled but money buys the goods, and the losers are the lower bidders (consumer-electronics buyers). **The power shortage is a queue-rationing shortage** — in parts of the US grid, prices have hit the regulatory ceiling and supply still falls short; the clearing mechanism has failed, and the costs spill onto the electricity bills of people who have never used AI. Both shortages are real, but the mechanism, the duration, and who pays differ completely.

And "how long" depends on whether you trust the forecasts — a field with two famous derailments on its record. This article's method is to strictly separate **what has already happened** (auction results, bills, order books, sold-out announcements) from **what is forecast** (945 TWh, 12%, 166 GW): the former depends on nobody's model; the latter all comes with enormous ranges.

## 1. The hardware shortage: price-clearing

### 1.1 2026, sold out

【multi-source】The memory industry's 2026 capacity sold out before 2026 was half over. SK Hynix confirmed on its earnings call that all three product lines — DRAM, NAND, and HBM — are sold out for 2026; Micron confirmed its entire 2026 HBM output is under contract; Samsung concurs. Those three firms are approximately the entire global HBM supply — and HBM (high-bandwidth memory) is the mandatory companion of every AI accelerator, 8–12 stacks per flagship GPU.

Buyer behavior changed too: cloud providers are signing multi-year long-term agreements (LTAs) with memory makers, accepting higher prices to lock in supply — classic commodity-shortage-cycle behavior. TrendForce's primary press release (2026-03-31) records the mechanism: "CSPs are willing to accept higher prices and sign LTAs to secure a stable supply."

### 1.2 Prices: get the yardsticks straight first

The most widely circulated number is "DRAM up 90% in a quarter." Back at TrendForce's primary figures, there are two tracks: **contract prices** (quarterly negotiated, large buyers) rose 58–63% QoQ for conventional DRAM in Q2 2026 and 70–75% for NAND; the +89–90% in headlines is **spot prices or specific parts** (e.g. LPDDR5X). Same direction, different magnitude — conflating them overstates by about a third. Q3 forecasts have cooled to +13–18% for DRAM — not because the shortage ended, but because consumers hit their affordability ceiling.

The consumer-side passthrough is the most visible part of this shortage: a 16GB DDR4 stick went from $137 to $207 retail in one quarter (+51%); HP's CFO said memory plus storage went from 15–18% of a PC's bill of materials to roughly 35%; Lenovo, Dell, HP, Acer and ASUS have all notified channels of 15–20% price increases. The mechanism is plain: memory makers reallocated capacity from consumer DRAM to HBM and server DDR5 (HBM now takes roughly 23% of DRAM wafers), AI outbids, consumer electronics gets crowded out — **the shortage isn't stopping AI from getting chips; it's stopping you from affording a RAM stick**.

### 1.3 The binding constraint has migrated: not wafers — packaging and memory

The 2023–24 "GPU famine" narrative was "not enough chips." By 2026 the binding constraint has migrated: 【multi-source】leading-edge wafer fabrication is no longer the bottleneck; **advanced packaging** (CoWoS — the step that assembles GPU dies with HBM stacks) and memory itself are. TSMC's CoWoS capacity is growing at roughly 80% a year and still falls short — 2026 is fully booked; NVIDIA alone has locked up over 60% of it (roughly 800–850k wafers booked for 2026), leaving little for AMD and Broadcom. TSMC's response: outsource steps to ASE and Amkor (ASE expects its advanced-packaging revenue to double in 2026) and build two new packaging plants in Taiwan plus two in Arizona.

One under-noticed implication of this migration: packaging plants and memory fabs take **2–3 years** to build, versus 4–5 for a leading-edge logic fab. That timescale drives the next section's answer.

### 1.4 How long: 2027 is the consensus, 2028 is the split

Statements about duration must be sorted by who is speaking. Vendors: Samsung's memory chief warns of "significant shortages" through at least 2027; SK Group's chairman says AI memory demand pressure could persist toward 2030 — note that firms calling a long shortage are the beneficiaries of the price spike, a built-in incentive to overstate. Analysts: UBS expects DRAM undersupply until at least Q2 2028; IDC sees tightness through 2027, with 2026 DRAM bit-supply growth at just 16% (below historical norms); TrendForce says HBM contract prices could double again in 2027. The other side: Bloomberg Intelligence argues the shortage peaked in Q2 2026 and could tip into **oversupply** by 2028 as Micron's Idaho and SK Hynix's Yongin fabs ramp in 2027–28.

【contested, but the structure is clear】Stacking the three: **tight through the end of 2027 is consensus** (new capacity physically cannot arrive sooner); **2028 is the fork** — if AI demand keeps compounding, a soft landing; if it decelerates (see this site's AI-capex-vs-1999 physical on demand quality), a 2028–29 flip to glut is a live scenario. Memory is a violently cyclical industry, and every supercycle in its history has ended in oversupply — the only novelty this time is that the demand side is wired to a trillion-dollar capex race.

## 2. The power shortage: queue-rationing

### 2.1 Already happened: three straight price-cap auctions and a 6,831 MW hole

The hardest evidence on power is not a forecast — it's an auction gavel. PJM is America's largest grid operator (13 states plus DC, including data-center-capital Virginia); its capacity auction prices "electricity availability in a future year." The price chain 【official, checked — PJM press releases】:

- Delivery year 2024/25: $28.92/MW-day
- 2025/26: $269.92 (9× in one year)
- 2026/27: $329.17 — at the FERC-approved price cap
- 2027/28: $333.44 — at the cap again
- 2028/29 (announced 2026-07-14): $325.00 — **third consecutive auction at the cap**; 138,318 MW procured, **6,831 MW short** of the reliability requirement, wider than the prior auction's 6,500 MW gap

A price pinned at the cap means this is no longer "expensive" — it is **unavailable at any permitted price**: the clearing mechanism has failed. PJM's CEO, verbatim: "demand for electricity continues to grow faster than electricity supply."

How much of this is data centers? PJM's independent market monitor, Monitoring Analytics (report of 2026-01-05), did the attribution 【official, checked】: in the 2027/28 auction, data-center load accounted for 40% of capacity costs ($6.5B of $16.4B) — $6.2B of it from data centers **not yet built**; across the last three auctions, forecast data-center load above existing installations contributed $21.3B, 45% of the $47.2B total.

### 2.2 Who pays: the bill passthrough

Capacity costs are socialized across all ratepayers. Consumer-advocacy calculations from rate filings 【single-source, checked — advocacy figures】: Pepco customers in Washington DC pay an average of $21/month more since June 2025 (about half attributed to capacity prices); western Maryland +$18/month; Ohio roughly +$16/month. The direction matches the auction results exactly; the specific figures were not independently recomputed. This is the deepest difference from the hardware shortage: **memory price hikes are paid by PC buyers; capacity price hikes are paid by everyone with a wall socket** — including people who have never touched AI. Hence its politicization: by 2026, data-center electricity pricing is on legislative and regulatory agendas in multiple states.

### 2.3 ERCOT's 438 GW: the official ghost count

The demand side carries a paradox that must be faced squarely: **requested demand vastly exceeds real demand**. Texas grid operator ERCOT's official figures 【official, checked】: roughly 410 GW of large-load interconnection requests on file in April 2026 (87% data centers), rising to 438 GW by mid-year (~90% data centers), with 198 GW of new requests in Q1 2026 alone. For scale: ERCOT's all-time system peak is about 85 GW — **the queue is five times the entire grid's peak**.

That cannot physically all get built, and the mechanism is well understood: developers file the same project with multiple utilities in multiple states, negotiate, build in one place — and the rest of the applications sit in queues as live megawatts. Industry experts estimate requests run 5–10× actual construction. This is "phantom load" — it contaminates load forecasts, and load forecasts feed straight into the capacity auction's demand curve, raising everyone's costs (the $6.2B of "not-yet-built data center" cost above is this mechanism, invoiced).

The squeeze-out has begun 【regulatory, primary-checkable】: ComEd in Chicago charges $1 million to apply for ≥50 MW; Ohio requires new data centers to pay for at least 85% of forecast usage (take-or-pay); Virginia is moving to 14-year lock-in contracts; Texas law requires large-load applicants to disclose duplicate filings and fund network upgrades. Once raising your hand becomes placing a bet, the queue will shrink — watching ERCOT's queue through 2027 is the best available window onto true demand.

### 2.4 "Chips sitting in inventory that I can't plug in"

Microsoft CEO Satya Nadella's November 2025 remarks on the BG2 podcast are quoted everywhere; the verbatim record 【vendor claim; quote multi-source consistent】: "The biggest issue we are now having is not a compute glut, but it's power — it's sort of the ability to get the builds done fast enough close to power… if you can't do that, you may actually have a bunch of chips sitting in inventory that I can't plug in. In fact, that is my problem today. It's not a supply issue of chips; it's actually the fact that I don't have warm shells to plug into."

Discount accordingly: the speaker is the party defending enormous capex — the same structural problem as issue #9's "all demand evidence comes from the sellers." But directionally it agrees with a chain of **non-vendor evidence** — PJM at the cap, ERCOT's queue, the turbine order book (next section) — so "the bottleneck has moved from chips to power" can bear weight as a direction; "how many GPUs Microsoft actually has gathering dust" cannot.

## 3. Can the forecasts be trusted? Two priors — and one real difference this time

### 3.1 The official forecasts carry huge ranges

The two most-cited forecasts are both more honest in the original than in citation. IEA, *Energy and AI* (April 2025) 【official, checked】: Base Case global data-center consumption doubles to ~945 TWh by 2030 — just under 3% of world electricity; but the same report's scenario band for 2035 runs from >1,700 TWh (Lift-Off) through ~970 TWh (High Efficiency) to ~700 TWh (Headwinds) — **a 2.4× spread**, with "substantial uncertainty" in the IEA's own words. LBNL (DOE-commissioned, December 2024) 【official, checked】: US data centers measured at 176 TWh in 2023 (4.4% of US electricity); the 2028 projection is 325–580 TWh, 6.7%–12% — **a 1.8× spread**.

Quoting 945 TWh or "12%" as a point estimate, without the band, is this topic's most common abuse. Panic pieces cite the ceiling; reassurance pieces cite the floor; same report.

### 3.2 Two priors: a history of systematic overestimation

Forecasts in this field have derailed twice, both in the same direction. First, 1999–2000: the claim that the internet would consume half of US electricity within a decade (the Mills/Forbes "dig more coal" lineage) spread widely and was dismantled line-by-line by LBNL's Jonathan Koomey; by 2020, data centers actually used 1–2% of US electricity. Second, 2007: the EPA's congressionally-mandated data-center forecast came in far above reality — 2005–2010 growth halved on virtualization, efficiency, and the financial crisis. The longer arc: from 2010 to 2018, global data-center compute multiplied severalfold while electricity use stayed roughly flat — hyperscale efficiency ate the growth.

【multi-source】Both priors share one structure — identical to the "traffic doubles every 100 days" myth this site's issue #9 excavated: **the demand narrative was spread by equipment and capacity sellers, and the person with independent data was right**. Every power-demand forecast today carries that original sin.

### 3.3 But this time one thing is materially different

The two prior scares were pure forecast failures — the predicted peak never arrived. This time, **the constraint has already cashed out in measurements**: US data-center consumption rose from 58 to 176 TWh over 2014–2023 (LBNL measurement, not forecast — and more than doubling over 2017–2023); PJM prices hit the cap three times running (gavel down); ERCOT has 438 GW on file (official); bills went up (invoiced); GE Vernova has 100 GW under contract (signed). The forecasts may still be too high — phantom demand all but guarantees the paper numbers are inflated — but "is the power constraint real" no longer hangs on a forecast: **it has already happened, in the form of prices and queues**. "The forecasts are unreliable" and "the shortage is not real" are two different propositions, and the first does not imply the second.

### 3.4 The forecast-of-forecasts fight

How much too high? That is itself now a professional dispute 【contested】. NERC (North American Electric Reliability Corporation), 2025 assessment: US peak load +166 GW over five years, ~90 GW tied to data centers; ten-year peak demand +24%. Grid Strategies, in rebuttal: utility-reported data-center load may be overstated by up to 40% (double-counting plus slower-than-expected interconnection), and independent trackers estimate 60–65 GW of data-center load actually online by 2029–30, not 90. Note the shape of the fight: **the sides are arguing 60 versus 90 GW — nobody is arguing zero**. Even at the deflated number, five years of 60 GW is roughly eight New York Cities of peak load added to the US grid.

## 4. When does supply catch up? Lay out the delivery timetables

How long the power shortage lasts is a function of physical delivery times on the supply side. Lay out the primary-source timetables as of July 2026 and the answer mostly derives itself.

### 4.1 Gas turbines: queued to 2030

【single-source checked + correction】GE Vernova (the largest turbine maker), Q1 2026 earnings call: 100 GW of gas turbines under contract (83 GW three months earlier), targeting 110 GW including slot reservations by year-end; prices on new bids running 10–20% above the year-ago backlog. CEO Scott Strazik, verbatim: "about 10 GW of turbine production capacity remaining through 2030 and continue to expect to take on orders for 2031 and beyond" — note the gap between this and July 2026 media prints of "sold out through 2030": it is **nearly sold out** (about 10 GW of slack left before 2030), not fully. Industry-wide, the three turbine OEMs (GE Vernova / Siemens Energy / Mitsubishi) quote lead times stretching to 8 years. Translation: **a gas plant ordered in 2026 generates power around 2029–2033**.

### 4.2 Nuclear: an answer for the 2030s, not the 2020s

Tech companies have signed many nuclear deals; line up the delivery dates and their contribution to this decade's gap rounds to zero 【multi-source】:

- **Microsoft–Constellation (Three Mile Island / Crane Clean Energy Center)**: 835 MW, 20-year PPA, $1B DOE loan. Signed September 2024; restart pulled forward from 2028 to **2027** — and this is the fastest path in America, because it resurrects an existing reactor: roughly 3 years from signature to electrons.
- **Google–Kairos**: first reactor 2030 (Tennessee, TVA); the 500 MW fleet complete by **2035**.
- **Amazon–X-energy**: initial ~320 MW online in the **early 2030s**; the 5 GW target sits in **2039**.

No commercial SMR is grid-connected in the United States today. Nuclear is a genuine long-term answer to AI's power problem — but any argument that runs "tech giants are buying nuclear, so the 2027 gap is covered" is off by a decade.

### 4.3 In the 2026–28 window, only three things scale fast

Read the timetables backwards: turbines 2029+, nuclear 2030s, transmission lines 5–10 years — so in the back half of this decade, the only supply that scales in *years* is: **solar plus storage** (fastest through interconnection; ERCOT's generation queue holds 178 GW of storage and 163 GW of solar versus 61 GW of gas), **demand response**, and data centers' **own on-site generation** (turbines and fuel cells that bypass the queue). This is inference, not measurement 【flagged as analysis】, but it explains what is visibly happening: the storage boom, OpenAI and xAI bringing their own power plants, and why the US crunch is structural — **demand signs up in months; supply delivers in five to eight years, and no short-term policy erases that spread**.

Grid-equipment evidence points the same way: GE Vernova's electrification segment (transformers, switchgear, HVDC) booked orders up 86% year-over-year in Q1 2026, backlog up from $25B to $42.4B — the queue for grid hardware is as long as the queue for generation.

## 5. Will efficiency ride to the rescue? A Jevons physical

The strongest counterargument is efficiency: AI's unit energy cost is collapsing — will the forecasts be embarrassed again, 2007-style?

The primary data is genuinely startling 【vendor claim, methodology published】: Google's August 2025 measurement puts the median Gemini text prompt at 0.24 Wh, with unit energy improving 33× in one year. But two scope restrictions must be nailed down: this is the **median, text-only** prompt — no images, video, long context, or reasoning chains, and no training; 0.24 Wh must not be quoted as "what AI uses per use."

And the Jevons paradox (efficiency lowers unit price → usage balloons → total consumption rises anyway) is not a theory in this case — it already happened 【multi-source】: the same Google that improved unit efficiency 33× **doubled** its data-center electricity use since 2020, with greenhouse emissions up roughly 50% since 2019 (Google's own environmental reports). Globally, the 2010–2018 "efficiency eats growth" plateau is precisely what AI broke in 2017–2023 (LBNL: US consumption more than doubled).

The honest conclusion: efficiency decides whether the forecast lands in the high or the low scenario (IEA's 2035 spread of 970 vs 1,700 TWh *is* the efficiency assumption) — **it changes the slope, not the constraint**, because the other end of the constraint (transformers, turbines, interconnection queues) does not respond to chip efficiency. One methodological reminder 【research】: AI's electricity use has no independent metering anywhere; every "AI share of power" number is an estimate (chip-shipment extrapolation, vendor disclosure, model ensembles). In this field, even the "measurements" carry error bars.

## 6. Whose shortage is this? A geography physical

"The power shortage" carries a qualifier that headlines almost never print: **America's** (plus a few European grid nodes — Dublin, Amsterdam).

【multi-source】The contrast is stark: China's electricity consumption grew ~8% a year for twenty years, generation and grid investment never paused, parts of its grid run at a **surplus**, and data centers can soak up existing slack. The US spent twenty years at near-zero demand growth; its utilities' planning, supply chains and regulatory clocks were all calibrated to flatness, and the sudden upturn caught the system flat-footed. The Oxford Institute for Energy Studies titled its February 2026 comment *The China data centre advantage*; Fortune's August 2025 report on AI researchers returning from China — "the US grid is so weak, the race may already be over" — is hyperbolic, but the direction is multi-source.

This geography reframes the question: the power shortage is not a global physical constraint of AI — it is **a mismatch between America's infrastructure investment cycle and AI's demand cycle**. Its end date depends not on chips but on the pace of US grid construction — the slowest line in the entire timetable.

## 7. The verdict

**Hardware: real, price-clearing, tight through 2027, 2028 contested.** Sold-out 2026 capacity is multi-source hard fact; doubled prices have reached consumers; the binding constraint sits in packaging and memory with 2–3-year build times; whether 2028 is a soft landing or a memory-supercycle glut depends entirely on whether AI demand keeps compounding — the second half of the hardware story is chained to demand (see issue #9).

**Power: real, queue-rationing, US-specific, structural to around 2030.** PJM capped three times running, a 6,831 MW hole, ERCOT's 438 GW queue, 8-year turbine lead times, nuclear in the 2030s — every item already happened or is already signed; none depends on a forecast. Meanwhile the paper demand numbers are systematically contaminated by phantom filings (requests ≈ 5–10× builds), the forecasts carry two priors of overestimation, and IEA/LBNL themselves publish ~2× ranges.

**The distinction that matters most**: "the forecasts are unreliable" and "the shortage is not real" are different propositions. What separates this episode from 1999 and 2007 is that the constraint has already **cashed out** — in auction prices, electricity bills, and order books. You may reasonably doubt 945 TWh; you cannot doubt $325/MW-day.

**Who is talking**: the loudest shortage voices (Nadella, memory makers, turbine makers) are all beneficiaries of the price spike or the capex; the loudest relief voices (Grid Strategies, the BI peak call) have their own positions. The reliable method is not to pick a side — it is to watch the variables that have already happened.

## 8. Ten testable claims

Ordered by evidence strength, each with its test.

1. **2026 memory capacity is sold out industry-wide and doubled prices have reached consumers** — multi-source primary; test: the three makers' quarterlies and TrendForce quarterly contract prints.
2. **PJM capacity prices capped three consecutive times with a widening gap (6,831 MW)** — official primary; test: whether the 2027 auction caps a fourth time, and whether the gap narrows.
3. **Data centers drove 45% of PJM's last three auctions' costs ($21.3B), much of it from unbuilt projects** — market-monitor primary; test: subsequent IMM reports; the share's response to state take-or-pay reforms.
4. **ERCOT's queue (438 GW) is ~5× system peak and mostly phantom** — official primary; test: how far the queue shrinks after Texas's disclosure rules bite (the sharper the shrink, the more phantom confirmed).
5. **Turbines queued to ~2030; new-order lead times 5–8 years** — vendor filings + industry multi-source; test: GE Vernova's quarterly backlog and capacity-expansion announcements.
6. **Nuclear's contribution to the 2020s gap ≈ 0** — deal timetables, primary; test: whether Crane connects on schedule in 2027 (the litmus for the fastest path); the year the first commercial SMR connects.
7. **Unit efficiency gains have not stopped total growth (Google 33× vs doubled consumption)** — vendor reports, primary; test: Google/Microsoft annual environmental-report consumption curves.
8. **The power shortage is a US-regional phenomenon; power does not bind in China** — multi-source; test: Chinese data-center power pricing and build times; whether any non-US market produces a capacity-auction-cap analogue.
9. **Memory may flip to glut in 2028 (conditional on AI demand decelerating)** — analyst inference; test: contract-price direction when 2027 capacity ramps; whether capex guidance gets cut.
10. **Official demand forecasts will be revised down again** (phantom squeeze-out + efficiency) — historical induction, lowest confidence; test: whether NERC/utility 2027 forecasts come down from 2026 vintages; if they rise instead and are validated by actual connections, this claim is refuted.

## Appendix: principal sources

- IEA, *Energy and AI* (April 2025) and scenario data; LBNL, *2024 United States Data Center Energy Usage Report* (December 2024, DOE-commissioned)
- PJM press releases: 2028/29 Base Residual Auction results (2026-07-14) and prior auctions; Monitoring Analytics, *IMM Analysis of the 2027/2028 RPM Base Residual Auction Part A* (2026-01-05)
- ERCOT: Large Load Update (April 2026 Senate hearing materials), Large Load Interconnection Status (March 2026 TAC report); Texas PUC large-load interconnection rules
- GE Vernova Q1 2026 8-K and earnings call; TrendForce press release (2026-03-31); IDC/UBS/Bloomberg Intelligence memory outlooks; SK Hynix/Micron/Samsung earnings-call reports (flagged as vendor claims)
- Constellation/Microsoft Crane Clean Energy Center announcements and DOE loan; Google–Kairos and Amazon–X-energy agreements
- Google, *Measuring the environmental impact of delivering AI* (August 2025) and annual environmental reports; Koomey's retrospectives on the 2007 EPA report and the 1999 "half of all electricity" narrative
- NERC 2025 Long-Term Reliability Assessment (January 2026); Grid Strategies annual load-growth reports and LTRA review; SemiAnalysis, "Stop Saying Half of 2026 US Datacenter Capacity Is Canceled" (commercial position flagged)
- OIES, *The China data centre advantage* (February 2026); CUB and other consumer-advocacy rate analyses (advocacy grading flagged); Nadella on the BG2 podcast (November 2025, vendor claim)

*This issue ran single-thread verification with tightened grading; faithful citation does not equal truth. Related on this site: [Is this AI capex cycle 1999 again?](https://cissy0802.github.io/deep-research/ai-capex-1999-deep.en.html) (demand quality and financing structure), [The "95% of pilots fail" physical](https://cissy0802.github.io/deep-research/ninety-five-percent-deep.en.html) (a ladder of yardsticks for reading survey numbers).*
