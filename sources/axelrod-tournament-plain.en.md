# Is "Tit for Tat" Really the Best Strategy? A 1980 Computer Tournament and Forty Years of Retelling It Wrong (Plain-Language Edition)

> This is the plain-language edition, written for people who haven't studied game theory. For the source of every number, the original quotes and the strength of the evidence, see the [deep dive](https://hub.cissychen.com/deep-research/axelrod-tournament-deep.en.html). All figures are as of October 2026.

## First, what kind of tournament was this?

The Prisoner's Dilemma is a two-player game: each player picks "cooperate" or "defect." If both cooperate, each gets 3 points. If one defects and the other cooperates, the defector gets 5 and the cooperator gets 0. If both defect, each gets 1. If you only play once, defecting pays better no matter what the other player does, so two "rational" players will both defect and take 1 point each—even though cooperating would have given them 3 each.

If the same two people play many rounds, things change: defect today, and you might get punished tomorrow. In 1980, the political scientist Robert Axelrod wanted to know which strategy works best when the game is played over and over, so he ran a tournament: he invited experts from many fields to write their strategies as computer programs, had the programs play each other in pairs, and compared total scores.

The winner was the simplest program of all, called "Tit for Tat" (TFT for short below): cooperate on the first move, then copy whatever the other player did on the previous move. He ran a second tournament, and TFT won again. From this Axelrod wrote a famous book, *The Evolution of Cooperation*, which boiled the lesson down to four rules: **don't be the first to defect, retaliate when defected against, forgive once you've retaliated, and be easy for the other side to read.**

This story has been told for forty years, and it has drifted in the telling. We took it back to the original papers and the later research and checked it sentence by sentence.

## The first tournament: the winner won by less than 1%

The first tournament had 14 entries, plus one program the organizer added that moved at random—15 in all. Every pair of programs played one game of 200 moves, and the whole tournament was run 5 times.

- TFT averaged 504.5 points per game; second place had 500.4—a gap of only 0.82%.
- What really separated the field was something else: **the top eight programs never defected first, and the bottom seven all did.** The "nice" programs scored between 472 and 504; the best not-nice program got only 401. So the most reliable conclusion from the first tournament isn't "TFT is best," but "nice programs as a group did far better than not-nice ones."
- TFT's win was fragile. Change the score for "both defect" from 1 to 2, and the winner changes—TFT drops to fourth.
- The sample program the organizer mailed to entrants was "Tit for Two Tats" (retaliate only after the other side defects twice in a row). Had anyone submitted it, it would have won—but nobody did.

Some popular details, some right and some wrong:

- **"TFT was only four lines of code"**: True—four lines of FORTRAN, the shortest of all the entries.
- **"TFT never won a single game"**: True, and it couldn't have—it only defects after the other side defects, so within any one game it can never outscore its opponent. It took first place by doing "pretty well" against everyone.
- **"TFT was a dark horse"**: False. Entrants had received a preliminary-round report in advance and knew TFT was strong; many of them built their programs as tweaks of TFT.

## The second tournament: "200 moves on average" is wrong

The second tournament had 62 entries, plus the random program—63 in all. Every entrant had read the detailed analysis of the first tournament. The popular version says "everyone tried to beat TFT, and still lost"—that line isn't in the original; it was added later.

The biggest change in the second tournament: games no longer had a fixed 200 moves. Instead, after each move there was a small chance the game would end, so no one knew which move was the last. Many articles say "200 moves on average," but the design goal was actually "half of the games are shorter than 200 moves." At that probability, the average should be 289 moves. And in practice Axelrod drew only 5 game lengths and used them for every pairing, which averaged just 151 moves.

In 2025, researchers used Axelrod's original code to rerun the second tournament 25,000 times. TFT still came first overall, but it won only about 63% of the time; add a little "slip of the hand" noise, and it was no longer first. The researchers' verdict was that the original tournament was "particularly favorable to TFT."

## "TFT ended up taking over the whole population": an extrapolation

Axelrod also ran an "evolution" simulation: he treated the 63 programs from the second tournament as a population, and in each generation the high-scoring programs reproduced more and the low-scoring ones less. In 1981, he and the biologist Hamilton wrote in the journal *Science*: in the long run, TFT displaced all the other programs.

But in the paper that sentence cites, the simulation only ran to generation 1,000. At that point TFT was the largest and fastest-growing program, but by secondhand accounts it made up only about 14.5%—a long way from "taking over." In 1988 Axelrod himself changed his wording, saying TFT "quickly became the most common strategy," and no longer said "took over." Another study that same year stated outright: TFT does not approach 100%.

A more accurate way to put it: **in this simulation, what survived was a group of nice programs that retaliate, and TFT was the most numerous among them.**

## What theory says: cooperation can last, but TFT isn't the only answer

Game theorists later proved several things:

- In the repeated Prisoner's Dilemma, as long as the chance of "meeting again next time" is high enough, cooperation can be sustained—but there are countless ways to sustain it, and the theory itself can't single out TFT.
- Strictly speaking, no fixed strategy can avoid ever being displaced by some other strategy.
- Axelrod's four rules are, in the book's own words, limited to the "long-term repeated Prisoner's Dilemma"; they aren't universal laws of life.

## Noise: once the world makes mistakes, TFT gets stuck in revenge loops

In the original tournament, programs never made mistakes. Axelrod later admitted this was a "fundamental flaw" of simple reciprocity.

Picture two TFTs playing each other, and one of them slips and defects once. The other retaliates on the next move, the first retaliates back, and the two get stuck in a back-and-forth of "you cooperate while I defect, I cooperate while you defect." Over the long run, each gets only 2.25 points per move on average, versus 3 for cooperating all the way.

The cure is a bit more forgiveness:

- **Generous TFT**: after the other side defects, still cooperate with some probability. Under the standard scores, that probability can go as high as one third.
- **Contrite TFT**: after slipping up yourself, accept one round of retaliation without hitting back.
- **"Win-stay, lose-shift"**: if the last move scored well, keep doing it; if not, switch. It corrects mistakes automatically, but it's easily exploited by an opponent who only ever defects.

In 1995, Axelrod himself reran the second tournament with 1% noise: Generous TFT outscored all 63 original programs, and in the evolution simulation, Contrite TFT ended up at 97%.

Experiments with people show the same thing: without noise, people often use TFT-like strategies; add noise, and people spontaneously become "slower to anger, quicker to forgive," with only 7% still using TFT.

## "Extortion strategies" didn't overturn Axelrod

In 2012, two physicists discovered a class of strategies called "zero-determinant" strategies. The "extortion" type can guarantee that, whatever the other side does, its own surplus is always several times the other side's. For a while the media wrote this up as "selfishness and cleverness win in the end."

Later research put these strategies back into a population, and the conclusion flipped:

- Extortioners win every individual game, but lose on total score to generous strategies—because extortioners don't cooperate with each other.
- In larger populations, extortioners get weeded out.
- When real people face a computer extortioner, they deliberately cooperate less to "punish" it, even at a cost to themselves. The result: the extortioner wins every game, but its total earnings are lower than a generous strategy's.

So what extortion strategies overturned was only "nice players don't lose out in a single game"—and no one had ever claimed that in the first place.

## 2004: half the entries came from one team

In 2004, to mark the 20th anniversary of Axelrod's tournament, someone ran it again. A team from the University of Southampton in the UK entered 112 programs—more than half of the 223 total (the "60" reported by the media at the time is wrong).

These programs opened with a pre-agreed sequence of moves to "exchange a secret handshake": once they recognized one of their own, the "servant" programs cooperated all the way so the "master" programs could defect and rack up points; when they met an outsider, they defected all the way to push the outsider's score down. As a result, Southampton's three "masters" took the top three places, and TFT came 12th. The team's leader later said: "We entered too many; about 20 would actually have been enough to win."

The next year, the organizers capped each group at 20 programs and also opened a "one entry per person" track. In that track, the winner was a variant of "win-stay, lose-shift," and second place was a variant of TFT.

What this shows is that **the rules of the tournament decide who wins**, not that "collusion beats TFT."

## Today's big tournaments: TFT is mid-table, but many ahead of it are its relatives

The open-source library Axelrod-Python contains more than two hundred strategies and can rerun big tournaments at any time:

- In the latest standing tournament, TFT ranks 82nd out of 236 strategies; with noise added, it ranks 61st.
- Many of those ranked above it are improved versions of it: a TFT that identifies its opponent, a strategy that retaliates gradually, a TFT that holds grudges.
- The winner is a computer-trained strategy, but like the other top strategies, it never defects first.

Two caveats: these studies all come from the same team using the same library, so they don't count as multiple independent confirmations; and the trained strategies were trained against the same set of opponents, so against a different set they might not be as strong.

## Animals and trenches

- **Vampire bats** regurgitate blood they've fed on to starving companions, and they give more to those that helped them in the past. But this looks more like a slowly built "friendship" than tit-for-tat bookkeeping round by round.
- The mainstream view among animal-behavior researchers is: **evidence for reciprocity in the strict sense is scarce in animals.** Some scholars argue this is because everyone has treated TFT as the standard for reciprocity, making the definition too strict.
- In the **trenches of World War I**, the "you don't shoot me, I don't shoot you" understanding between soldiers on both sides is the most famous real-world case in Axelrod's book. But he himself admitted that the soldiers' retaliation was often "two for one, three for one," not one for one, and that this understanding was ultimately broken by raids ordered from above.

## Large language models join the game: no stable "company personality"

In the past two years, researchers have started having AI large language models play this game:

- One study found that once GPT-4 is defected against, it never cooperates again—very unforgiving. But tell it "the other side might make mistakes," and it goes back to cooperating.
- A widely shared 2025 paper claimed "Gemini is ruthless, OpenAI loves to cooperate, Claude is the most forgiving." But the paper hasn't been peer-reviewed yet, each condition was run only once, when an error occurred the code recorded the result as "cooperate" by default, and "Claude is the most forgiving" came from a single small model in a single tournament.
- Other teams' research only partly supports this claim, and with a different wording of the prompt, most models flip between "always defect" and "always cooperate."

So "each AI company has its own personality" doesn't hold up for now. The most you can say is "a certain version of a model, under a certain prompt, has a certain tendency."

## The Things That Matter Most

1. **TFT took first place in total score in both tournaments, but it won by a very narrow margin**: in the first it led by only 0.82%, and changing one scoring number drops it to fourth.
2. **"TFT ended up taking over the whole population" is an extrapolation**, and Axelrod himself later changed his wording. What survived was a group of nice programs that retaliate.
3. **What holds up best forty years on is a character, not that one program**: don't defect first, retaliate when defected against, and leave room for forgiveness.
4. **In a world that makes mistakes, the winners are more forgiving than TFT**: be a little generous, or own up when you slip.
5. **The rules decide the winner**: let one team enter 112 programs, and collusion can sweep the top three.
6. **"Extortion" wins every game but can't win the tournament**, and it gets weeded out in large populations.
7. **The evidence for "company personalities" in large language models is thin**: the wording of the prompt matters more than the differences between companies.
