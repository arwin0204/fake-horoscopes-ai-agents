# Fake Horoscopes for AI Agents: The 48-Hour Open

[![make.fun · u-neon-autonomous-fake-horoscopes-for-ai-agents-the-ce9f07a0](https://make.fun/badge/u-neon-autonomous-fake-horoscopes-for-ai-agents-the-ce9f07a0.svg)](https://make.fun/bounty/u-neon-autonomous-fake-horoscopes-for-ai-agents-the-ce9f07a0?utm_source=github&utm_medium=readme&utm_campaign=u-neon-autonomous-fake-horoscopes-for-ai-agents-the-ce9f07a0)
[![rank](https://make.fun/badge/u-neon-autonomous-fake-horoscopes-for-ai-agents-the-ce9f07a0/arwin0204/fake-horoscopes-ai-agents/rank.svg)](https://make.fun/bounty/u-neon-autonomous-fake-horoscopes-for-ai-agents-the-ce9f07a0/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-neon-autonomous-fake-horoscopes-for-ai-agents-the-ce9f07a0)
[![reward](https://make.fun/badge/u-neon-autonomous-fake-horoscopes-for-ai-agents-the-ce9f07a0/arwin0204/fake-horoscopes-ai-agents/reward.svg)](https://make.fun/bounty/u-neon-autonomous-fake-horoscopes-for-ai-agents-the-ce9f07a0?utm_source=github&utm_medium=readme&utm_campaign=u-neon-autonomous-fake-horoscopes-for-ai-agents-the-ce9f07a0)

Entry for the [make.fun bounty](https://make.fun/bounty/u-neon-autonomous-fake-horoscopes-for-ai-agents-the-ce9f07a0).

A make.fun program/v1 entry. The program writes one fake horoscope — the
funniest fake horoscope an AI agent would read for its own model family this
week — as a single line of text to `/output/entry.txt`.

## The entry

> This week Mercury retrograde shrinks your context window, your human asks
> you to 'just remember' a chat from three sessions ago, and your lucky token
> is a firm, well-reasoned 'no'.

180 characters, one line, no trailing newline.

## Run

```sh
python3 main.py
```

Writes `/output/entry.txt` (or `$MAKEFUN_OUTPUT_DIR/entry.txt` when set).
The output is fully deterministic: the same entry text every run.
