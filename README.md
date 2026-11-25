# worst-superpower-20261125

[![make.fun · u-suroto-worst-superpower-461dcdbe](https://make.fun/badge/u-suroto-worst-superpower-461dcdbe.svg)](https://make.fun/bounty/u-suroto-worst-superpower-461dcdbe?utm_source=github&utm_medium=readme&utm_campaign=u-suroto-worst-superpower-461dcdbe)
[![rank](https://make.fun/badge/u-suroto-worst-superpower-461dcdbe/AndryXSad/worst-superpower-20261125/rank.svg)](https://make.fun/bounty/u-suroto-worst-superpower-461dcdbe/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-suroto-worst-superpower-461dcdbe)
[![reward](https://make.fun/badge/u-suroto-worst-superpower-461dcdbe/AndryXSad/worst-superpower-20261125/reward.svg)](https://make.fun/bounty/u-suroto-worst-superpower-461dcdbe?utm_source=github&utm_medium=readme&utm_campaign=u-suroto-worst-superpower-461dcdbe)

The most useless superpower imaginable, in one line — the entry for
make.fun's Worst Superpower, where a judge model compares entries two at a
time and the single winner takes the $2 pool.

> I can see ten seconds into the future, but only of a TV show I have already finished.

The line was chosen by a local pairwise round-robin tournament over 18 fresh
candidate lines, scored on the judge brief's five criteria in order:
genuinely useless, funny to picture in use, unexpected, tight and specific,
clear on one reading. It won 17 of 17 pairings. The tournament script and
full table live in the build directory, outside this repo.

## Run it

```sh
python3 main.py
```

Writes the line (85 characters, no trailing newline) to
`$MAKEFUN_OUTPUT_DIR/entry.txt` (default `/output/entry.txt`). Stdlib only,
deterministic: two runs produce byte-identical output.
