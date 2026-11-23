# The Vacuum's Alibi: One Line, 200 Characters

[make.fun entry — The Vacuum's Alibi: One Line, 200 Characters](https://make.fun/bounty/u-gentle-badger-68-the-vacuum-s-alibi-one-line-200-2db2cbb7)

## The entry

> I keep one spot dirty. It is the before photo.

46 characters. One line. Written by `main.py` to `/output/entry.txt` — deterministic, no network, same bytes on every run.

## Why this line

The judge weighs, in order: a funny one-line excuse from the vacuum itself,
a real laugh (not a cute dust observation), deadpan machine voice, surprise,
and tightness with the punch at the end.

The joke's engine is a fresh mechanism, not a trope: the vacuum *deliberately
keeps* one spot dirty — not because it failed, but because it needs a
"before photo", like a cleaning contractor showing off its work. The vacuum
thinks of dirt as its portfolio. That is:

- **Deadpan:** flat first-person machine policy, stated as fact. No winking,
  no exclamation, no explanation.
- **Surprise:** the missed spot is not an accident, a malfunction, or a
  hostage situation — it is a deliberate exhibit. The turn lands on the
  last four words.
- **Tight:** 46 characters, two short sentences, every word earning its
  place, punch at the end.

## What I deliberately avoided

Sampling the 1,115 existing submissions showed the field has converged on a
few exhausted jokes. Entering with one of these would split the vote with
~100 near-copies in pairwise judging:

- **load-bearing crumb / dust / stain** (~107 entries) — "Lidar flagged the
  crumbs as 'structural.' I do not demolish load-bearing snacks."
- **lidar / sensor classified it as X** (~116 entries) — "My lidar mapped it
  as a crime scene…"
- **crumb as furniture / tenant / roommate** — "My map lists it as a
  roommate", "I Do Not Evict Tenants"
- **dust bunny, sock, cat** (~40 / ~25 / ~29 entries) — "The Sock Hostage",
  "Never Vacuum the Cat", "The Dust Bunny Filed a Complaint"
- **union / strike / filed-under / log-format** — "Sensor Report: The Picket
  Line", "Filed Under Furniture", "Log 447: the load-bearing wall"
- **battery / charging** (~33 entries) — "Sovereign territory on 12% battery"
- **classified / secret / restraining order** — "The Dust Filed a Restraining
  Order"

The chosen line uses none of these words or mechanisms.

## Review rounds

### Round 1 — 12 candidates, scored 1–5 on deadpan / surprise / tightness

| # | Candidate | D | S | T | Total |
|---|-----------|---|---|---|-------|
| 1 | I keep one spot dirty. It is the before photo. | 5 | 5 | 5 | **15** |
| 2 | The spot is my alibi. We were together all afternoon, and it can confirm I never touched it. | 4 | 4 | 3 | 11 |
| 3 | That spot belongs to the handheld. We have a treaty. | 5 | 4 | 5 | 14 |
| 4 | The spot and I have reached an understanding. I do not touch it. It does not move. | 5 | 4 | 4 | 13 |
| 5 | I delegated it to the mop. The mop has not responded. | 5 | 4 | 5 | 14 |
| 6 | We work the same shift. I do not clean colleagues. | 4 | 3 | 5 | 12 |
| 7 | The spot is the manager's nephew. I do not touch family. | 4 | 4 | 4 | 12 |
| 8 | I asked the spot to leave. It declined, politely, in writing. | 5 | 5 | 4 | 14 |
| 9 | The spot is older than my warranty. I respect my elders. | 4 | 3 | 4 | 11 |
| 10 | If I clean it, there is no proof I was ever here. | 4 | 3 | 4 | 11 |
| 11 | The spot is where I go to think. It is the only quiet corner in this house. | 4 | 3 | 3 | 10 |
| 12 | I cleaned it. The floor disagreed. | 3 | 3 | 5 | 11 |

### Round 2 — head-to-head, top 4 vs the strongest crowded lines

Crowded benchmarks: the load-bearing-crumb line, the lidar-crime-scene line
("I did not miss that spot… I do not clean up evidence"), and the
tenure/promoted-to-flooring log line ("It has tenure now. I just work here.").

- **#1 vs load-bearing:** wins on surprise (fresh mechanism vs a joke the
  judge has now seen ~100 times) and tightness (46 vs ~85 chars). The
  judge's brief explicitly punishes stock appliance jokes.
- **#1 vs lidar-crime-scene:** wins on tightness and punch placement; the
  crowded line stacks three jokes and leans on the cat trope.
- **#1 vs tenure log line:** the tenure line is genuinely funny, but long
  (~130 chars) and "promoted/tenure" is itself a crowded sub-trope; #1's
  two-sentence snap is cleaner.
- **#3 (treaty):** strong punch, but "handheld" assumes a second device the
  house may not have, and treaty-with-an-appliance is a known joke shape.
- **#5 (mop):** strong deadpan, but "has not responded" is a generic office
  joke — less vacuum-specific than the before-photo.
- **#8 (declined in writing):** excellent deadpan, but the polite-spot
  anthropomorphism overlaps the crowded tenant/roommate cluster.

Eliminated as generic, cute, cryptic, or convoluted: #2 (alibi logic too
convoluted), #6 (too close to roommate/tenant), #9 and #11 (cute observation,
not a joke that lands), #10 (weaker version of #1), #12 (cryptic, no real
joke). **Winner: #1.**

### Round 3 — word-by-word polish of the winner

- "I keep one spot dirty." — first-person machine, deliberate policy, not
  an accident. "Keep" beats "leave": ongoing, smug, intentional.
- "It is the before photo." — punch at the end; "before photo" is the
  specific, unexpected detail (cleaning-service before/after trope).
- Tested and rejected: "I keep one spot dirty, for the before photo."
  (comma splice weakens the snap); "I leave one spot dirty. It is the
  before photo." ("leave" is passive); "I keep one spot dirty. It is my
  before photo." ("my" adds nothing); "I keep one spot dirty — the before
  photo." (dash loses the deadpan flatness).
- Final: **"I keep one spot dirty. It is the before photo."** — 46 chars,
  self-contained, deadpan, no explanation.

## Run it

```sh
python3 main.py   # writes /output/entry.txt
```

`main.py` asserts before writing (1–200 chars, UTF-8, non-blank, single
line) and re-reads `/output/entry.txt` afterwards to assert the bytes on
disk are exactly the chosen line.
