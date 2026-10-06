# Who Ends Up With the Money AI Makes? Are Model Makers Just Sewing Someone Else's Wedding Dress? (Plain-Language Edition)

> This is the plain-language edition, written for people who have never read an earnings report. For the source of every number, the original quotes and the strength of the evidence, see the [deep dive](https://hub.cissychen.com/deep-research/ai-profit-pools-deep.en.html). All figures are as of early October 2026.

## First, what are we actually asking

The AI business can be roughly split into five layers: the chipmakers; the people generating power and building data centers; the cloud providers that rent out computing power; the labs that build models; and the companies that make apps and own the users. Everyone is asking the same question: which layer does the money end up in?

There are four popular answers, and they contradict each other: "In a gold rush, the people selling shovels win" (chips); "Models will keep getting cheaper and will end up worthless"; "Whoever owns the users wins" (companies like Google, Microsoft and Apple); and "The strongest lab takes everything." Lately a fifth has joined them: "Electricity is the scarcest thing of all."

Every one of these answers can find numbers to back it up, partly because people are using different measuring sticks. This article starts by agreeing on one:

- **Look at the money made from the business itself (operating profit), not the bottom-line net profit.** In 2026, the net profits of several big companies were padded with huge "paper gains" — the AI lab shares they hold went up in value. For example, Amazon booked a pretax gain of about $50.5 billion from its Anthropic stake in a single quarter, 3 times the operating profit of its entire cloud business that quarter. Comparing net profits would count the same value several times over.
- **Look at revenue actually recognized, not "annualized revenue."** "Annualized" means taking the latest month's revenue and multiplying by 12; for fast-growing companies it is often double the actual revenue.
- **Separate "money that has already changed hands" from "money in signed contracts."** Orders worth hundreds of billions and guarantees worth tens of billions are mostly commitments stretching over many years.
- **Separate "where the money is now" from "where the money will be later."** The first can be read from financial reports; for the second, all we can offer is a few possibilities, plus how to tell early which one is happening.

## Two theories: where does the profit go

**The first theory comes from Harvard Business School professor Clayton Christensen.** He argued that when one step in a chain becomes a standard part anyone can make, the profit moves to the step next to it; and while a product is still "not good enough," the companies that tightly integrate all the parts make the most money. He himself wrote that this is "still a hypothesis." Applied to AI: if the strongest models still aren't good enough for customers, then labs that bundle the model and the product together will make money; if they're already good enough, models become standard parts.

**The second theory comes from analyst Ben Thompson.** He argues that in the internet era, whoever owns the users can squeeze suppliers into commodities with no bargaining power. By this logic, the money ends up wherever users enter.

Interestingly, Thompson himself changed his view three times in 2026: in March he said that if AI agents need the model tightly integrated with the shell around it, the labs could be more profitable than expected; in June he said the biggest winners right now are NVIDIA, TSMC and the memory makers, while the most valuable thing long term is still the user entry point; in September, reasoning from a single event, he said customers have started to feel current capabilities are "good enough," and that "Pure capability no longer translates directly into a moat." When one of the analysts following this industry most closely changes his call three times in a year, that alone tells you how hard the question is.

The two theories give opposite answers, but both point to the same two observable things: **whether customers feel the strongest models are already "good enough,"** and **whether physical bottlenecks like chips, memory and power get resolved.** At the end of the article, these two things are used to build four possibilities.

## Who took the profit in past booms

**The PC era.** Around 2000, Intel and Microsoft together made about $21.3 billion in operating profit; all of Dell plus Compaq's two PC divisions made about $3.1 billion — a gap of about 7 times (the two sides aren't measured in exactly the same way; depending on how you convert, it's 6 to 8 times). Those who controlled the standards — chips and the operating system — were fat; those who assembled the machines were thin.

**Fiber and railways.** Around 2000, many of the companies laying fiber went bankrupt, but that fiber was later bought up cheaply and became the backbone of today's nearly free internet. In Britain's railway mania of the mid-19th century, investors lost about a third of their money, by one scholar's estimate (an estimate, and other scholars disagree). The pattern: those who build the road carry the risk; those who use the road get the benefit.

**This time may be different.** Fiber and railways last for decades, so after the builders went bust, latecomers could pick them up cheaply and keep using them. AI chips are depreciated over 5 to 6 years for accounting purposes, and in practice may be made obsolete by the next generation even sooner. If this round overbuilds, what's left for bargain hunters will be the buildings, the power equipment and the land already connected to the grid — not the computing power itself.

## Chips: the most profitable layer today — but the money is moving to memory

In the quarter ending July 2026, NVIDIA's revenue was about $96.2 billion, with about $66 of operating profit for every $100 of revenue. Three years ago that figure was only about $16.

But right now the memory-chip makers are even more profitable than NVIDIA. Micron made about $81 of operating profit for every $100 of revenue in its latest quarter, and South Korea's SK hynix about $76. The reason: AI has bought up the entire memory market, and prices have soared.

A counterintuitive detail: the most profitable product isn't the high-end memory built specifically for AI (HBM), but ordinary memory and flash storage — their shortages pushed prices up even harder. Micron itself says it plans to raise HBM prices sharply in 2027 to catch up with the margins on ordinary memory.

NVIDIA's reports confirm this too: it lowered its gross margin forecast, and its finance chief said the reason was "extreme pricing conditions in memory"; its purchase commitments jumped from $119 billion to $279 billion, mostly to buy memory. But NVIDIA also said it plans to win its margins back by raising its own prices. So this "money moving to memory" may be only temporary.

**Two more caveats.** First, Google, Amazon and others are designing their own chips, but that hasn't made the chip layer's profit disappear — it has just been reshuffled within the chip layer. Second, one investor estimates that the chip layer's share of gross profit across the whole AI ecosystem fell from about 87% two years ago to about 79% — still overwhelming, but declining.

## Cloud: high margins, resting on three assumptions

The cloud businesses of Amazon, Google and Microsoft make $35 to $41 of operating profit for every $100 of revenue, which looks very profitable. But that number rests on three assumptions:

- **Research and development isn't counted.** Google's huge model-training costs are booked at the group level, not charged to the cloud business.
- **It assumes a GPU stays useful for 5 to 6 years.** Several of these companies have stretched the depreciation period for their servers to 5.5 to 6 years, which makes the yearly cost look lower. Amazon, by contrast, shortened it for part of its equipment, saying AI technology moves too fast.
- **It assumes the profit on renting out GPUs will rise.** The only concrete number comes from the press: according to a report citing internal Oracle documents, in summer 2025 its gross margin on renting out NVIDIA chips was only about 14%. Oracle says it can reach 30% to 40% in the long run on an adjusted basis, but this has yet to show up in its financial reports.

On cash, you can't just say "the cloud providers are burning money." The ones genuinely spending more than they take in are Amazon (over the past year) and Oracle; Google had one negative quarter and, unusually, raised about $49.6 billion in the stock market; Microsoft still has plenty of cash coming in.

The cloud providers' contracted orders add up to about $2.46 trillion. That sounds alarming, but it can't be treated as total AI demand: it includes a lot of non-AI contracts, and the same few AI labs have placed orders with several cloud providers at once, so they're counted more than once.

## GPU renters and electricity: profits eaten by interest, and a scarcity nobody priced

**At the new companies that specialize in renting out GPUs, profits are eaten by interest.** Take CoreWeave: in the second quarter of 2026 its revenue was about $2.6 billion. Before depreciation it looks very profitable; after depreciation it barely makes money; and after about $640 million in interest, it lost about $630 million in a single quarter. It carries about $35.1 billion in debt, against only $5 billion of shareholders' money. The big cloud providers deliberately left this structure to them: Microsoft's CEO has said he doesn't want to be locked into one generation of hardware for four or five years.

**GPU rental prices did not crash by 80%.** The often-quoted "H100 went from $8 an hour to $1.70" stitches two different kinds of prices together. Comparing like with like: the big cloud providers' list prices fell only about 20%; one-year contract prices have rebounded about 40% from their low in October 2025. 2026 is a market where the renters-out call the shots — CoreWeave raised prices across its models by about 25% in July.

**Electricity is only a small slice.** Several independent estimates show that electricity makes up only about 7% to 17% of an AI data center's total cost; the bulk is the chips themselves.

**But that doesn't mean "the people selling power can't make money."** Going from "electricity is a small share of costs" to "the people selling power can't make money" doesn't hold up. Precisely because electricity matters so little to the overall bill, customers don't care about the price of power at all — they only care whether they can get connected right away. A rough calculation: if a large AI data center gets power a year late, the losses from idle chips come to about 10 times a full year's electricity bill. So "being able to plug in right away" is very valuable. That money has mostly not gone to price-regulated utilities (in America's largest grid region, capacity prices have hit the government-set cap three times in a row, and the cap has been extended through 2030). Instead it has flowed to the makers of gas turbines, developers holding grid-connection slots, and data centers that already have power hooked up.

## Model makers: revenue has pulled apart, profit hasn't shown up

None of the model-making labs are publicly listed. All their financial figures come from company statements, leaked documents or press reports, so treat them as rough guides only.

**On revenue, one lab overtook the other.** According to reports, in the second quarter of 2026 Anthropic's revenue was about $11.5 billion and OpenAI's about $6.7 billion — the first time Anthropic has overtaken OpenAI. But the two book revenue differently: Anthropic counts the full amount of sales made through Amazon's and Google's clouds, while OpenAI first deducts the share it pays Microsoft. Measured the same way, Anthropic is still ahead, but not by the 1.7 times in the headlines — rather by 1.3 to 1.6 times.

**There's almost no profit yet.** Anthropic turned a profit in only one quarter, the second, and only on its own "adjusted" measure (which excludes stock compensation for employees and so on), about $560 million; for all of 2025 its operating loss was about $8.1 billion. OpenAI's operating loss in the second quarter was about $12.3 billion, about 1.8 times its revenue; its forecast to investors is a cumulative net cash outflow of about $278 billion from 2026 to 2030.

**They owe a lot upstream.** Leaked documents show that Anthropic has about $518 billion in ten-year computing contracts with six cloud and chip partners, most of them non-cancelable.

So the claim that "model makers as a group are sewing someone else's wedding dress" — that is, doing all the work so someone else gets the payoff — is too crude: revenue has already pulled apart among the leaders, so you have to look at each company separately; but so far none of them has actually made a profit under formal accounting rules.

## Two price curves: why both camps think they're right

The "models will keep getting cheaper" camp and the "the strongest models keep getting more valuable" camp have been arguing for two years. In fact, they are looking at two different curves.

**Curve one: AI at the same level gets about ten times cheaper every year.** The research group Epoch found that the lowest cost of reaching a fixed level of capability falls about 13-fold each year (between 9 and 30 times, depending on how you calculate it); other teams have measured anywhere from 5 to 50 times, all in the same direction. People who think "models will become commodities" are looking at this curve.

**Curve two: getting a task done with the strongest model keeps getting more expensive.** MIT researchers found that the cost of running a full set of tests with the strongest model of the day rises 3 to 18 times each year, mainly because new models "think" longer and use up more text. People who believe "the frontier commands a premium" are looking at this curve.

**The sticker price itself hasn't risen all the way.** The claim that "the price of the strongest models rises with each generation" doesn't hold. OpenAI's flagship standard tier did go up from $10 per million tokens for GPT-5 to $50 for its newest top tier (tokens are the units of text a model processes; this is the output price), but at the same time it launched a main tier costing only $10; Anthropic's most expensive tier is actually cheaper than in 2025. The current picture: the top tier is going up, while cheap, capable main tiers have appeared alongside it.

**Open-source models are about 4 months behind, but most of the money still goes to closed models.** One working paper found that on a platform developers use a lot (it accounts for only about 1% of global spending on model APIs), closed models accounted for about 80% of usage and 96% of revenue, at prices averaging 6 times those of open-source models.

Whether model companies can make money depends on which curve customers' money stays on: whether they keep paying ever-larger bills for top capability, or switch to cheap "good enough" options. The coding tool Cursor turned its money-losing gross margin into a slim profit only by swapping the base of its own model to the open-source Kimi.

## Apps: the money is with whoever already owns the users

**The old giants weren't disrupted by AI — they became even more secure.** Google's search revenue grew 17% in the second quarter, and its search and advertising business made about $42 of operating profit for every $100 of revenue (not counting AI research costs booked at the group level); Microsoft's office software business, about $58; Apple's services business has a gross margin of about 76%, and it barely has to spend its own money building AI data centers — Apple's next-generation foundation models will be based on Google's Gemini. Compare: according to a Bloomberg report before the deal was signed, Apple pays Google about $1 billion a year for the model (formal terms undisclosed), while a court found that in 2022 Google paid Apple more than $20 billion to be the default search on the iPhone. Whoever owns the users collects far more than it pays.

(Meta's consolidated operating profit fell 8% in the second quarter, which is often blamed on "AI costs being too high." In fact it was mainly one-off legal costs and severance; strip those out and profit grew.)

**The new AI app companies grow fast, make thin profits, and have their lifeline in someone else's hands.** One venture firm tracked the ten fastest-growing AI app companies and found an average gross margin of only about 25%, often negative. Cursor only recently went from losing money to a slim profit. Worse, suppliers upstream can cut them off at any time: according to the CEO of the coding tool Windsurf, in 2025 Anthropic cut off nearly all of its direct supply of Claude 3.x models with less than five days' notice; in August 2026, after SpaceX bought Cursor for about $60 billion, OpenAI promptly stopped providing it with models.

**The model makers are also building apps themselves.** Anthropic's coding tool Claude Code passed $2.5 billion in annualized revenue by February 2026; OpenAI has started selling ads.

## Side by side: where the money is today

Putting every layer on the same measuring stick (latest quarter, operating profit for every $100 of revenue): memory about $76 to $81, NVIDIA about $66, TSMC about $60, cloud businesses about $36 to $41, GPU renter CoreWeave a loss of about $2, OpenAI a loss of about $184 (press reports).

The conclusion is clear: **right now, the closer you are to physical scarcity (memory, advanced chips, chip manufacturing), the more money there is; the closer you are to the models, the less.** "The shovel sellers win" is true for now.

How much do the downstream layers need to earn to support all this? The consulting firm Bain estimated in 2026 that by 2031, AI infrastructure will cost about $1.5 trillion a year, which would require an annual market of nearly $6 trillion, while existing AI products can contribute only $1.2 to $1.8 trillion — a gap of about $4.2 to $4.8 trillion. A year earlier, its estimate for 2030, assuming companies moved all their on-premises IT budgets to the cloud, put the gap at about $800 billion.

## The money goes in a circle: the 'someone else's wedding dress' story is half right

If you look only at cash, model makers really are working for the layers above them: Microsoft took in about $24.1 billion from OpenAI in one fiscal year (FY2026), mostly for cloud computing.

But bring the other flows into the picture, and you get a circle:

- **Cash flows up**: labs pay cloud providers and chipmakers for computing power.
- **Equity and credit flow down**: NVIDIA has already invested nearly $50 billion in frontier labs, and expects about a quarter of its business next year to come from labs supported by NVIDIA's balance sheet; it states plainly in its reports that these labs and new cloud companies "currently lack the ability to secure long-term infrastructure contracts and investment-grade financing capacity." One of Amazon's financing facilities for Anthropic even states outright that the money is released in step with AWS delivering computing power — the investment and the purchase of computing power are written into the same contract.
- **Valuations flow back into the upstream income statements**: whenever a lab raises money at a higher valuation, Amazon, NVIDIA and Microsoft, which hold shares, book a paper gain. That is where Amazon's $50.5 billion that quarter came from.

So the claim that "model makers are working for someone else's benefit" is right about cash but backwards about risk: **the upstream companies are underwriting the labs' credit.** A big chunk of NVIDIA's business next year, a big chunk of the cloud providers' orders, and more than half of Amazon's pretax profit that quarter all hinge on whether a handful of labs can keep raising money. The real question is no longer just "which layer has the highest margin," but "if a lab runs into trouble, who pays the bill?"

## What happens next: two variables, four possibilities

Cross the two observable things mentioned earlier — **whether the strongest models are "good enough"** and **whether the physical bottlenecks are resolved** — and you get four possibilities:

1. **Bottlenecks remain, the strongest models still aren't good enough**: chips, memory and the strongest labs make money together.
2. **Bottlenecks remain, models are already good enough**: models become interchangeable parts, and the money is soaked up by chips, memory and data centers that already have power.
3. **Bottlenecks resolved, the strongest models still aren't good enough**: computing power gets cheap, and labs that bundle the model with the product win.
4. **Bottlenecks resolved, models are already good enough**: both models and computing power get cheap, and the money goes back to the companies that own the users — Google, Microsoft, Apple, Meta.

As of October 2026, reality sits somewhere between possibilities 1 and 2: the bottlenecks are clearly still there (record memory profits, rebounding rental prices, electricity prices hitting the cap), and signs of "good enough" are only just emerging and can't yet be confirmed.

## The things that matter most

**Right now the money is upstream, and the closer to physical scarcity, the more of it.** Memory > chips > chip manufacturing > cloud > GPU renters > model makers. This is backed by formal financial reports and is the firmest conclusion in this article.

**Money is moving from GPUs to memory, but this may be temporary.** And the biggest profits come from shortage-driven price rises in ordinary memory, not memory built specifically for AI.

**The cloud's high margins rest on assumptions.** R&D isn't counted, GPUs are depreciated over 5 to 6 years, and the profit on renting out GPUs is assumed to rise — there are counterexamples to all three. Amazon and Oracle are already spending more cash than they take in.

**Model makers' revenues have pulled apart, but profit hasn't shown up.** Only one company, for one quarter, on its own custom measure, made money.

**The "someone else's wedding dress" story is only half right.** Cash flows up, risk is pushed down: the upstream companies are underwriting the labs, and the labs' valuations are in turn booked as upstream profit. The question to ask is "who is carrying the labs' risk?"

**Electricity is cheap, but "plugging in right away" is very valuable.** That money has mostly not gone to the utilities, but to gas turbine makers and whoever holds grid-connection slots.

**What happens next depends on two observable things: whether models are "good enough," and whether the bottlenecks are resolved.**

## How to check this article's judgments

Ordered from most confident to least:

1. **On formal accounting for the latest quarter, the operating margins of memory and chip companies (about 60% to 81%) are higher than those of cloud businesses (about 36% to 41%), and far higher than GPU renters (losing money) and model labs (losing a lot).** How to disprove it: watch the next few quarters' reports — if a cloud business or a lab catches up with the chip companies' margins.
2. **Lab valuations are being booked as profit at upstream companies, so comparing layers by net profit double-counts.** Amazon booked about $50.5 billion (pretax) in one quarter, 3 times its cloud business's operating profit that quarter. How to disprove it: if some lab's valuation is cut, an equally large loss in the opposite direction should appear in upstream income statements.
3. **Companies that specialize in renting out GPUs pay more in interest than they earn in operating profit.** How to disprove it: CoreWeave's operating profit covers its interest for the first time, or similar companies turn out not to fit this pattern.
4. **The cloud providers' cash positions have split: margins are high, but Amazon and Oracle are spending more cash than they take in, and Google has started raising money in the stock market.** How to disprove it: look at cash flows in the second half of 2026.
5. **AI at the same level gets about ten times cheaper each year, while getting things done with the strongest model gets more expensive; the two camps are looking at different curves.** How to disprove it: if the cost of getting things done with the strongest model also starts falling year by year.
6. **Money has already moved from GPUs to memory, mainly to ordinary memory.** How to disprove it: after memory capacity expands in 2027, if memory companies' margins drop back below NVIDIA's and NVIDIA's margins recover, the shift was only temporary.
7. **The money from AI apps is mostly taken by the old giants that own the users; new AI app companies have thin margins and can be cut off by suppliers upstream.** How to disprove it: an AI-native app company publicly discloses a long-term, stable gross margin above 50%.
8. **About a quarter of NVIDIA's business next year is propped up by its own balance sheet.** How to disprove or confirm it: look at its actual disclosures for the next fiscal year, and whether its guarantees for OpenAI's data centers get triggered.
9. **Model makers' revenues have pulled apart, but profit hasn't concentrated in anyone's hands: as of October 2026, only Anthropic has been profitable for one quarter on its own custom measure, and none has been profitable for a single quarter under formal accounting rules.** How to disprove it: Anthropic formally files to go public, or publishes its actual third-quarter results.
10. **Electricity is only around a tenth of an AI data center's costs, but "plugging in right away" is worth about 10 times the electricity bill; that money mainly flows to gas turbine makers, developers holding grid-connection slots and data centers that already have power, not to the utilities.** How to disprove it: look at these companies' margins, and at prices after the electricity price cap expires in 2030.
11. **Where the money ends up in the long run depends on "whether models are good enough" and "whether the bottlenecks are resolved"; current readings lean toward "bottlenecks remain."** How to disprove it: watch the four things below.

**What to watch.** If any of these four things happens, this article's judgments should change:

First, **memory companies' margins fall back below NVIDIA's** — a sign the physical bottlenecks are starting to ease.

Second, **a lab turns a profit under formal accounting rules for the first time**, or, the other way round, **a lab raises money at a lower valuation** — the latter would leave a loss in the opposite direction on upstream companies' income statements.

Third, **the share of corporate spending going to open-source or cheap main-tier models rises again** — the most direct signal of "good enough will do."

Fourth, **NVIDIA's guarantees for OpenAI's data centers, or its backstop commitments to new cloud companies, actually get triggered** — the first hard sign that this money circle is under strain.

## Appendix: where this article was overturned

Review changed the original draft in many places. Here are the most important:

- The original draft said "the price of the strongest models rises with each generation" — in fact, OpenAI launched a cheap main tier at the same time, and Anthropic's most expensive tier got cheaper.
- The original draft said "electricity is a small share of costs, so the power layer can't make money" — review found this reasoning didn't hold: electricity being a small share is exactly why customers don't care about the price of power, only about whether they can plug in right away.
- The original draft said "the money Microsoft collects from OpenAI exceeds OpenAI's annual revenue" — the two figures cover different time periods and the comparison figure comes from press reports, so they can't be compared like that; it's more accurate to say this money mainly comes from what OpenAI raised from investors.
- The original draft said "Anthropic has been profitable for two quarters in a row" — in fact only one; the second was the company's own forecast.
- The original draft said "GPU rental prices crashed 80% and then rebounded 60% to 90%" — that stitched different kinds of prices together.
- The original draft said "the memory companies' biggest profits come from HBM built specifically for AI" — in fact ordinary memory is more profitable.
- The original draft said "Meta's profit was eaten by AI costs" — it was mainly one-off charges.

**Almost every number that made some layer look more extreme — rental prices crashing harder, thinner power profits, faster-rising model prices, more concentrated profits — became a bit milder once checked against the original sources.**

For the full argument and sources, read the [deep dive](https://hub.cissychen.com/deep-research/ai-profit-pools-deep.en.html). Related plain-language editions on this site: ["Is the AI Build-Out Another 1999? What Rhymes, What Doesn't, What Not to Believe"](https://hub.cissychen.com/deep-research/ai-capex-1999-plain.en.html) and ["Is AI Really Causing a Hardware Shortage and a Power Shortage? For How Long?"](https://hub.cissychen.com/deep-research/ai-hardware-power-plain.en.html).
