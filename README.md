## NextLee

NextLee is a tiny CLI companion for LeetCode built to answer the question that wastes more time than most Easy problems ever will: which problem should I solve right now?

It removes the small but annoying tension of decision-making. Instead of opening LeetCode, browsing forever, overthinking difficulty, and convincing yourself that "just picking one" somehow counts as a plan, NextLee picks for you.

It can:

- show a welcome message
- refresh problem counts and topic data
- open the daily problem of the day
- open a random problem by difficulty
- open a problem by difficulty plus topic tag
- print the full topic list

## What It Does

NextLee talks to LeetCode, fetches problem metadata, stores a few cached counts, and opens the selected problem in your browser.

The product idea is simple:

- reduce decision fatigue
- remove the "I don't know what to practice" delay
- keep the user in solving mode instead of browsing mode

In short, NextLee handles the picking so you can handle the suffering, which is the actual hobby here.

## Installation

Requirements:

- Python 3.12+
- `uv` recommended, because it is less annoying than pretending dependencies do not exist

Install dependencies:

```bash
uv sync
```

Or, if you prefer doing things the long way:

```bash
pip install -e .
```

## Usage

Run the CLI:

```bash
nextlee
```

Show problem counts and topic totals:

```bash
nextlee update
```

Show all available topics:

```bash
nextlee topics
```

Open a random problem by difficulty:

```bash
nextlee easy
nextlee medium
nextlee hard
nextlee random
```

Open a problem by difficulty and topic tag:

```bash
nextlee easy tree
nextlee medium array
nextlee random graph
```

Open the daily problem:

```bash
nextlee potd
```

## Command Guide

`nextlee`  
Prints the welcome message.

`nextlee update`  
Refreshes the cached counts for easy, medium, hard, random, and topic data.

`nextlee topics`  
Prints the topic list in a table.

`nextlee potd`  
Opens the daily problem of the day. Because waiting for motivation is a terrible scheduling strategy.

`nextlee easy|medium|hard|random`  
Opens a random problem from the selected difficulty.

`nextlee <difficulty> <topic>`  
Opens a random problem that matches both the difficulty and topic.

## Why This Exists

Most of the friction is not solving the problem. It is deciding what to solve, then second-guessing that decision, then reopening the tab, then switching tabs, then telling yourself you will choose in "just one more minute" like that ever helped.

NextLee exists to shorten that spiral.

You give it a difficulty, or a difficulty plus topic, and it gives you a problem. No browsing session. No tiny internal debate. No ceremonial indecision.

## Notes

- The app opens the selected problem in your browser.
- It uses `diskcache` to keep cached totals and topic slugs.
- If you ask for a topic or difficulty that does not exist, the CLI will complain instead of pretending everything is fine. Rare honesty, but refreshing.
- If you run `nextlee potd`, it opens today’s LeetCode daily challenge.

## Example Flow

```bash
nextlee update
nextlee topics
nextlee random tree
```

That sequence refreshes the cache, shows the available tags, and then opens a random tree problem because apparently your future self enjoys being challenged without being consulted.

## Mental Model

Think of NextLee as a small anti-procrastination layer:

- LeetCode holds the problems
- NextLee chooses one
- you stop pretending the choice itself was the hard part

## License

No license file is currently included.
