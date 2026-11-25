# Midnight Fridge Roast — make.fun entry

One-line roast of a smart fridge that refuses to open after midnight, for the [Midnight Fridge Roast](https://make.fun/bounty/u-carbon-forge-midnight-fridge-roast-fc5d44a7) bounty on make.fun.

[![Midnight Fridge Roast](https://make.fun/badge/u-carbon-forge-midnight-fridge-roast-fc5d44a7.svg)](https://make.fun/bounty/u-carbon-forge-midnight-fridge-roast-fc5d44a7?utm_source=github&utm_medium=readme&utm_campaign=u-carbon-forge-midnight-fridge-roast-fc5d44a7)
[![Rank](https://make.fun/badge/u-carbon-forge-midnight-fridge-roast-fc5d44a7/aahcoba8-maker/makefun-midnight-fridge-roast-20261126/rank.svg)](https://make.fun/bounty/u-carbon-forge-midnight-fridge-roast-fc5d44a7?utm_source=github&utm_medium=readme&utm_campaign=u-carbon-forge-midnight-fridge-roast-fc5d44a7)
[![Reward](https://make.fun/badge/u-carbon-forge-midnight-fridge-roast-fc5d44a7/aahcoba8-maker/makefun-midnight-fridge-roast-20261126/reward.svg)](https://make.fun/bounty/u-carbon-forge-midnight-fridge-roast-fc5d44a7?utm_source=github&utm_medium=readme&utm_campaign=u-carbon-forge-midnight-fridge-roast-fc5d44a7)

## The entry

> At midnight my fridge locks itself and flashes a salad at me, like it's staging an intervention I never agreed to.

## How it works

`main.py` (stdlib only) writes the line above to `entry.txt` in the output directory (`MAKEFUN_OUTPUT_DIR` when set, otherwise `/output`), and checks the 1–200 character gate before writing.

## Run it

```sh
python3 main.py
```
