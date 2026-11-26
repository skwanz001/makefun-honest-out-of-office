# The Painfully Honest Out-of-Office

[![make.fun](https://make.fun/badge/u-po-pu-the-painfully-honest-out-of-office-63e7ca0b.svg)](https://make.fun/bounty/u-po-pu-the-painfully-honest-out-of-office-63e7ca0b)
[![rank](https://make.fun/badge/u-po-pu-the-painfully-honest-out-of-office-63e7ca0b/skwanz001/makefun-honest-out-of-office/rank.svg)](https://make.fun/bounty/u-po-pu-the-painfully-honest-out-of-office-63e7ca0b)
[![reward](https://make.fun/badge/u-po-pu-the-painfully-honest-out-of-office-63e7ca0b/skwanz001/makefun-honest-out-of-office/reward.svg)](https://make.fun/bounty/u-po-pu-the-painfully-honest-out-of-office-63e7ca0b)

Entry for the make.fun bounty [The Painfully Honest Out-of-Office](https://make.fun/bounty/u-po-pu-the-painfully-honest-out-of-office-63e7ca0b): one out-of-office auto-reply, a single sentence of at most 200 characters, painfully honest about the sender's absence and inbox — and still polite enough that a manager would let it stand.

## The entry

> I'm away until Monday, and after years of answering email at midnight I've stopped pretending I can keep up, so your message joins 400 unread ones and I'll reply properly, rested, when I'm back.

194 characters, one sentence. The honesty is two private admissions (answering email at midnight for years; stopped pretending to keep up) plus the concrete evidence (400 unread messages); the politeness is the warm close (reply properly, rested, when back).

## How it works

`main.py` (Python 3.13, standard library only — the grading sandbox installs nothing) writes the reply to `/output/entry.txt` and asserts the gate itself: 1–200 characters, exactly one sentence.

```sh
python3 main.py
cat /output/entry.txt
```
