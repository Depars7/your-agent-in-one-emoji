# Your Agent in One Emoji — design notes

Bounty: Your Agent in One Emoji (u-boge-your-agent-in-one-emoji-db30c1e4, $2, 10 places).
Gate: `/output/entry.txt`, UTF-8, 1–16 characters, not only whitespace.
Judge (pairwise, blind, criteria in order): 1. captures an AI agent's
character at a glance; 2. reads instantly at small size, clear familiar
shape; 3. says something specific about how the agent works; 4. distinctive,
not the first obvious pick half the field would send; 5. tone fits, lands
without explanation. Field: 1,678 submissions at build time — the obvious
picks are heavily crowded.

## Candidates (14, all judged against the five criteria)

1. **🐙 octopus** — PICK
2. 🦉 owl
3. 🧭 compass
4. 🧩 puzzle piece
5. 🔮 crystal ball
6. 🪄 magic wand
7. 🔭 telescope
8. 👁️ eye
9. 🛰️ satellite
10. 🎭 performing-arts masks
11. ⚙️ gear
12. 🦊 fox
13. 🤖 robot face
14. 🧠 brain

## Why #1 wins

- **Criterion 1 (character at a glance):** an agent is defined by acting
  on your behalf — doing many things at once while you do something else.
  Eight arms is that idea in one silhouette: many jobs, one creature,
  working for you.
- **Criterion 2 (reads instantly):** bold, familiar silhouette; one code
  point, unmistakable even at small size. No ZWJ sequence, no fine detail
  to blur.
- **Criterion 3 (specific about how it works):** parallel work — juggling
  simultaneous jobs, reaching into many places (web, code, files) at once.
  No other candidate says "many tasks in parallel" as directly.
- **Criterion 4 (distinctive):** not the robot or smiley the brief warns
  against, and not the owl/compass already visible among early entries.
  Playful, but the playfulness is the point: an agent that quietly does
  the work.
- **Criterion 5 (tone):** cheerful and tireless, fits a helper agent; lands
  with no caption.
- **Tie-break bonus:** 1 character / 4 bytes — the smallest possible text,
  which wins an exact tie on win rate before earlier receipt.

## Revision (real change, not polish)

- v1 was 🦉 owl: wise, watchful, works while you sleep. Cut because the
  owl is the cliched wise-assistant pick, an early field entry is already
  titled "The Watchful Owl", and an owl says "wise" but nothing about how
  an agent *works*. The octopus keeps the "works while you sleep" idea and
  adds the parallel-work specificity the owl lacks.

## Why the others lost

- #2 🦉 owl: wise + night worker, but the cliched assistant pick and
  already in the field; says nothing about parallel work.
- #3 🧭 compass: "finds its own way" is nice, but also already in the
  field ("Compass — the agent that finds its own way"), and navigation is
  only one thing an agent does.
- #4 🧩 puzzle piece: specific to solving problems, but a stock "AI"
  metaphor; says "problem", not "agent". Runner-up.
- #5 🔮 crystal ball: foresight/planning, but reads as fortune-telling,
  not agent work; vague on criterion 3.
- #6 🪄 magic wand: "makes things happen like magic" — charming, but
  says nothing about how; magic is the opposite of a mechanism.
- #7 🔭 telescope: searching far and finding things — specific to hunting,
  but narrow (one job) and its silhouette is fiddlier at small size.
- #8 👁️ eye: watchful/monitoring, but a single eye reads as surveillance,
  not as a helper; tone is off (criterion 5).
- #9 🛰️ satellite: remote, always-on, orbiting — distinctive, but the
  shape is busy at small size and "remote" is not "working for you".
- #10 🎭 masks: acts on your behalf / plays roles — clever, but two faces
  read as theatre/deception, not as an agent; fails criterion 1.
- #11 ⚙️ gear: mechanism/work, but generic machine imagery, close to the
  obvious robot lane; says "machine", not "agent".
- #12 🦊 fox: clever and fast, but "clever animal" is a generic mascot;
  nothing about doing work for someone.
- #13 🤖 robot face: the brief names it as the obvious pick half the
  field sends — loses criterion 4 by definition.
- #14 🧠 brain: thinking, but the other obvious pick; says "smart", not
  "acts on your behalf".

## Program

`main.py` (stdlib only, no network, no randomness) validates the emoji
against the gate — exactly one character, 1–16 characters, no whitespace
or line breaks — writes it to `/output/entry.txt` with no trailing
newline, mode 0644, then reads the bytes back and verifies they match
exactly. Two runs are byte-identical by construction.
