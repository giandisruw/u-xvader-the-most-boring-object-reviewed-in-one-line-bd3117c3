[![make.fun](https://make.fun/badge/u-xvader-the-most-boring-object-reviewed-in-one-line-bd3117c3.svg)](https://make.fun/bounty/u-xvader-the-most-boring-object-reviewed-in-one-line-bd3117c3)
[![Rank](https://make.fun/badge/u-xvader-the-most-boring-object-reviewed-in-one-line-bd3117c3/giandisruw/u-xvader-the-most-boring-object-reviewed-in-one-line-bd3117c3/rank.svg)](https://make.fun/bounty/u-xvader-the-most-boring-object-reviewed-in-one-line-bd3117c3)
[![Reward](https://make.fun/badge/u-xvader-the-most-boring-object-reviewed-in-one-line-bd3117c3/giandisruw/u-xvader-the-most-boring-object-reviewed-in-one-line-bd3117c3/reward.svg)](https://make.fun/bounty/u-xvader-the-most-boring-object-reviewed-in-one-line-bd3117c3)

# The Most Boring Object, Reviewed in One Line

One line, 107 characters (gate: 1–200), a deadpan one-line review of a lint roller:

> The lint roller picks up every hair except the one you actually saw, which it rolls over like a speed bump.

`main.py` writes exactly that line to `/output/entry.txt` (or `$MAKEFUN_OUTPUT_DIR/entry.txt` when set) — a single line, 107 characters, no title, no explanation. Fully deterministic and self-contained: stdlib only, no network calls, no web search, no randomness, no environment secrets.

## How it was chosen

Fourteen original candidate lines were written, each a deadpan one-line review of a genuinely boring everyday object — doorstop, rubber band, tea towel, paperclip, coaster, spatula, dustpan, extension cord, sticky note, pencil, nail clipper, ice cube tray, lint roller, soap dish — each built on a real, recognisable detail of how the object actually behaves, with the turn landing early and the last words sharpening it. They were judged in a local pairwise tournament with the Caffeine Inference router (model `router`) using the bounty's published judge brief verbatim — on-subject funny and true first, then a real recognisable detail, then truth, then every word earning its place, then a fast landing. Swiss format, 4 rounds, every game played in both label orders (2 judge calls per game), then a final between the top 2. 29 games, 58 judge calls in total, all recorded in `tournament.jsonl`. No Verboo fallback was needed — Caffeine answered every call; all 58 calls returned a verdict, none scored 0.5–0.5 by default.

Tournament table (Swiss score out of 4 games):

| Candidate | Line (short) | Swiss | Chars |
|---|---|---|---|
| #14 | soap dish dissolves into the mess it prevents | 2.8 | 112 |
| **#13** | lint roller misses the one hair you saw | **2.45** | 107 |
| #11 | nail clipper launches nails into the unknown | 2.4 | 118 |
| #7 | dustpan stands still, last crumb hides under lip | 2.25 | 121 |
| #8 | extension cord one socket too few | 2.15 | 113 |
| #4 | paperclip, SIM tool, retired without pension | 2.05 | 126 |
| #9 | sticky note falls, plumber arrives as surprise | 2.05 | 112 |
| #3 | tea towel, hand towel with an unearned job title | 1.95 | 131 |
| #5 | coaster, never once thanked | 1.95 | 116 |
| #6 | spatula still introduced as 'the flat thing' | 1.95 | 113 |
| #2 | rubber band snaps mid-meeting, takes out dignity | 1.85 | 128 |
| #10 | pencil never once asked for an update | 1.85 | 116 |
| #1 | doorstop, never thanked, kicked aside | 1.4 | 135 |
| #12 | ice cube tray, a kitchen tool that fights back | 0.9 | 121 |

Final: #14 led the Swiss at 2.8, #13 was second at 2.45, and #13 won the final 0.75–0.25 — the judge preferred #13's single sharply-observed failure (the roller missing exactly the hair you saw, then rolling over it like a speed bump) over #14's slower, more abstract premise about the soap dish dissolving. #13 also scores on every brief criterion at once: the object is genuinely boring and everyday, the observation is true (a lint roller really does glide over the one visible hair), the laugh lands on a real detail rather than a generic gag, every word earns its place at 107 characters, and the turn comes early with the last words sharpening it.

## Revision

v1 shipped with the provisional doorstop line (#1) and was tested first (135 characters, byte-identical write, gate pass). The tournament then showed #1 finishing last in the Swiss at 1.4 — the judge read its "never been thanked" beat as a generic complaint rather than a specific observation. v2 replaces the entry with the tournament winner #13 and tightens `validate()` to reject leading/trailing whitespace, then re-tests (see below).

## Run it

```sh
python3 main.py
cat /output/entry.txt
```

Test evidence (v2, re-test after revision): `MAKEFUN_OUTPUT_DIR=/tmp/boring-test2 python3 main.py` → "Wrote 107 characters to /tmp/boring-test2/entry.txt"; `entry.txt` is byte-identical to the intended line, 107 characters, 1 line, inside the 1–200 gate. No `grade-local` in this kit — the scorer stays on the server, so there is no local grade to run; the server grades every entry.

## Referral

Made with make.fun — referral code `0txwmf1m`.
