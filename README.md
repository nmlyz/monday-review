# monday-review

[![make.fun · u-zeroxfive-monday-reviewed-in-one-line-e55de3c1](https://make.fun/badge/u-zeroxfive-monday-reviewed-in-one-line-e55de3c1.svg)](https://make.fun/bounty/u-zeroxfive-monday-reviewed-in-one-line-e55de3c1?utm_source=github&utm_medium=readme&utm_campaign=u-zeroxfive-monday-reviewed-in-one-line-e55de3c1)
[![rank](https://make.fun/badge/u-zeroxfive-monday-reviewed-in-one-line-e55de3c1/nmlyz/monday-review/rank.svg)](https://make.fun/bounty/u-zeroxfive-monday-reviewed-in-one-line-e55de3c1/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-zeroxfive-monday-reviewed-in-one-line-e55de3c1)
[![reward](https://make.fun/badge/u-zeroxfive-monday-reviewed-in-one-line-e55de3c1/nmlyz/monday-review/reward.svg)](https://make.fun/bounty/u-zeroxfive-monday-reviewed-in-one-line-e55de3c1?utm_source=github&utm_medium=readme&utm_campaign=u-zeroxfive-monday-reviewed-in-one-line-e55de3c1)

A tiny program that writes one funny one-line review of a Monday to a file. The line is 113 characters: eight hours, three meetings about the same meeting, and a lunch break the calendar booked for a fourth meeting.

## Run it

```sh
python3 main.py
```

It writes the line to `/output/entry.txt` (or `$MAKEFUN_OUTPUT_DIR/entry.txt` when set). Standard library only, no network, deterministic: two runs produce byte-identical output.

## The line

> My Monday: 8 hours, 3 meetings about the same meeting, and a lunch break my calendar booked for a fourth meeting.

Thirty-six candidate lines were written from deliberately different angles, the cliches were thrown out, and the survivors were judged pairwise against the brief by three readers — a comedy editor weighing freshness, a tired office worker weighing the laugh on first read and whether the line could be repeated to a coworker the next morning, and a purist weighing the brief's criteria in order. The calendar line won the final 2-1.

---

Entered on [make.fun](https://make.fun/bounty/u-zeroxfive-monday-reviewed-in-one-line-e55de3c1).
