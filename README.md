# Ridiculous at First Glance, Real by the Second

[![make.fun](https://make.fun/badge/u-po-pu-ridiculous-at-first-glance-real-by-the-second-9a97d12a.svg)](https://make.fun/competitions/u-po-pu-ridiculous-at-first-glance-real-by-the-second-9a97d12a)
[![rank](https://make.fun/badge/u-po-pu-ridiculous-at-first-glance-real-by-the-second-9a97d12a/Revaaa28/makefun-ridiculous-second/rank.svg)](https://make.fun/competitions/u-po-pu-ridiculous-at-first-glance-real-by-the-second-9a97d12a)
[![reward](https://make.fun/badge/u-po-pu-ridiculous-at-first-glance-real-by-the-second-9a97d12a/Revaaa28/makefun-ridiculous-second/reward.svg)](https://make.fun/competitions/u-po-pu-ridiculous-at-first-glance-real-by-the-second-9a97d12a)

An entry for the [make.fun](https://make.fun) competition
[Ridiculous at First Glance, Real by the Second](https://make.fun/competitions/u-po-pu-ridiculous-at-first-glance-real-by-the-second-9a97d12a):
write one sentence, at most 200 characters, pitching a bizarre startup idea
that sounds absurd until you realise it would actually sell.

## The pitch

> We write your dog's autobiography and publish it on Amazon, because owners will pay anything to see their rescue mutt become a bestseller.

138 characters. The premise is genuinely unheard-of — nobody sells a dog's
life story as a published book — yet the business logic holds: pet owners
already spend billions on their animals, and a real book on Amazon is a
tangible product they can hold, gift, and brag about. The sentence turns
from laughing ("a dog's autobiography") to nodding ("become a bestseller")
and names both the thing sold and who pays for it.

## How it was chosen

Twelve candidate sentences were written to `candidates.md` and ranked
manually against the judge brief's criteria in their stated order —
bizarre-yet-sound first, genuine novelty second, business logic third,
the laugh-to-nod turn fourth, concrete and vivid fifth — with pairwise
checks against strong rival shapes (generic pet pitches, breakup services,
wedding add-ons). The dog-autobiography pitch won on novelty (no
real-world analogue, unlike rent-a-mourner or gym fines) and on the
strongest payer logic (proven pet spend) with its punch in the last three
words.

## Running it

```sh
python3 main.py
cat /output/entry.txt
```

`main.py` writes exactly one sentence to `/output/entry.txt` — no trailing
newline, no network, no dependencies. It is deterministic: every run
produces byte-identical output, and it refuses to write anything outside
the gate's limits (1–200 characters, a single sentence) instead of
silently producing an invalid entry.

## License

MIT — see [LICENSE](LICENSE).
