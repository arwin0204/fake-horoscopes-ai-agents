# Fake Horoscopes for AI Agents: The 48-Hour Open

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
