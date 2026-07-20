# Is AI Really Causing a Hardware Shortage and a Power Shortage? For How Long? (Plain Version)

> This is the condensed version of the deep dive of the same name. Every key number has been checked against primary sources; for the full argument and citations, read the deep dive. Figures as of July 2026.

## Split the question first

"Is AI causing shortages" is really two questions: hardware (chips, memory) is one shortage, electricity is another — and they work completely differently.

**The hardware shortage is a price-clearing one**: the goods exist, prices have doubled, and the people priced out are the lower bidders (like you, buying a PC). **The power shortage is a queue-rationing one**: in parts of the US grid, prices have hit the regulatory ceiling and there still isn't enough — money can't buy it — and the cost lands on everyone's electricity bill, including people who have never used AI.

Both shortages are real. But how long they last, and who pays, differ.

## Hardware: 2026's memory sold out in the opening months

The three big memory makers (SK Hynix, Samsung, Micron) sold out their entire 2026 capacity — including HBM, the high-bandwidth memory every AI chip requires — before the year was half over. Cloud giants are signing multi-year contracts at elevated prices just to lock in supply, textbook shortage-cycle behavior.

The primary price record: in Q2 2026, DRAM contract prices rose 58–63% in a single quarter and NAND 70–75% (the "+90%" in headlines is spot prices or specific parts — mildly exaggerated). The passthrough to you: a 16GB RAM stick went from $137 to $207; HP says memory and storage now make up a third of a PC's cost; the big PC makers have all raised prices 15–20%. The mechanism is simple: memory makers moved production lines to AI-grade memory, and consumer parts got crowded out — **the shortage isn't stopping AI from getting chips; it's stopping you from affording a RAM stick**.

How long? **Tight through the end of 2027 — that's the consensus** (new factories physically can't arrive sooner). The split is 2028: if AI demand keeps surging, gradual relief; if AI demand slows, the memory industry's old script is a hard flip into **glut** — every memory supercycle in history has ended that way. Note who's talking: the loudest "shortage will last years" voices are the memory makers profiting from the price spike.

## Power: the auction has hit its ceiling three times running

The hardest evidence on power isn't a forecast — it's what already happened. PJM, America's largest grid (13 states, including data-center-capital Virginia), auctions "future power capacity" every year. That price went up 11× in three years: from $28.92 to $329.17, then $333.44, then $325 — **three consecutive auctions pinned at the regulatory price cap**, and the latest (July 2026) still came up 6,831 MW short. A price stuck at the ceiling means: not expensive — unavailable.

Who caused it? PJM's independent market monitor did the math: 45% of the costs of the last three auctions ($21.3 billion) trace to forecast data-center load — much of it from data centers **that don't exist yet**.

Who pays? Everyone. Washington DC residents pay $21/month more since June 2025; Maryland +$18; Ohio +$16 — roughly half attributed directly to the capacity-price spike.

## But the demand numbers are full of ghosts

Texas's grid (ERCOT) has 438 GW of connection requests queued — while the entire Texas grid's all-time peak is 85 GW. **The queue is five times the whole system's peak.** It cannot physically be built. The reason: developers file the same project in multiple states, build in one, and leave the rest as "phantom demand" in the queues. Experts estimate requests run 5–10× actual construction.

Regulators have started squeezing the water out: Chicago charges $1 million just to apply for a big connection, Ohio makes data centers pay for 85% of forecast usage whether they use it or not, Texas mandates disclosure of duplicate filings. Once raising your hand becomes placing a bet, watch how fast the queue shrinks — that's the best gauge of true demand over the next two years.

## Forecasts have derailed twice — but this time differs in one way

Data-center power forecasts have two famous priors: 1999's "the internet will eat half of US electricity within a decade" (reality by 2020: 1–2%), and the EPA's 2007 forecast that actual usage came in far below (efficiency gains plus the financial crisis). Both times, **equipment sellers spread the demand myth, and the person with independent data was right**. So today's forecasts — "global data-center power doubles to 945 TWh by 2030," "12% of US electricity by 2028" — deserve a discount: the official reports themselves publish ~2× ranges. Panic pieces quote the ceiling; reassurance pieces quote the floor.

But this time has one material difference: **in the prior scares, the predicted peak never arrived; this time the constraint has already cashed out** — the auctions were gaveled, the bills were mailed, the turbine orders were signed. You can doubt 945 TWh. You can't doubt $325/MW-day. "The forecasts are unreliable" and "the shortage isn't real" are two different claims.

## When supply catches up: lay out the delivery dates and the answer writes itself

- **Gas turbines**: GE Vernova, the biggest maker, is booked to about 2030 (100 GW under contract; the CEO says only ~10 GW of capacity remains before 2030), and industry lead times stretch to 8 years. A plant ordered in 2026 generates power in 2029–2033.
- **Nuclear**: Microsoft's Three Mile Island restart — the fastest path in America, since it revives an existing reactor — arrives in 2027. Google's and Amazon's small modular reactors: first units after 2030, scale in 2035–2039. **Nuclear is the 2030s' answer; it cannot rescue this decade.**
- What **can** scale fast: solar plus batteries (shortest queues), and data centers building their own power plants.

So the conclusion is structural: **demand signs up in months, supply delivers in five to eight years.** America's power crunch most likely runs to around 2030.

## Two important "buts"

**Efficiency won't ride to the rescue — but it bends the slope.** Google says one Gemini request now uses 33× less energy than a year ago — true; and the same Google's total data-center power use doubled over the same era (the classic Jevons paradox: the cheaper each use gets, the more everyone uses). Efficiency decides whether the forecast lands high or low; it does nothing for the queue of transformers and power lines.

**This is America's shortage, not the world's.** China grew its power supply 8% a year for two decades and parts of its grid run at a surplus — data centers just plug in. The US spent twenty years with flat demand, calibrated its whole system to flatness, and got caught flat-footed. At bottom, the power shortage is **a mismatch between America's infrastructure cycle and AI's demand cycle**.

## One-sentence verdict

**Hardware: really short, tight through 2027, and 2028 depends on AI demand (keeps surging = gradual relief; slows = flips to glut). Power: really short, US-specific, structural to around 2030 — and this one doesn't hinge on any forecast: it's already written into auction results and your electricity bill.**

## What matters most

- Distinguish price-clearing from queue-rationing shortages: markets fix the first on their own; the second waits for construction, on a timescale twice as long.
- Distinguish what happened from what's forecast: auction prices, bills and order books are measurements; 945 TWh, 12% and 166 GW are forecasts with 2× ranges and a track record of running high.
- Watch who's talking: "shortage forever" comes from price-spike beneficiaries (memory makers, turbine makers, CEOs defending capex); "relief is coming" has its own positions too. Track the variables that already happened; don't pick a team.
- The three numbers most worth watching: whether PJM's next auction caps a fourth time; how far ERCOT's queue shrinks once disclosure rules bite; whether Three Mile Island connects on schedule in 2027.
