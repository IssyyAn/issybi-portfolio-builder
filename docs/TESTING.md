# Testing Guide

The release workbook contains a 67-case full suite plus eight curated OpenAI submission cases.

## Honest test procedure

1. Start each case in a fresh chat so earlier context cannot help the skill.
2. Install and enable the packaged plugin version being tested.
3. Copy the exact prompt from the workbook or `submission/test-cases.md`.
4. Attach the stated fixture where required.
5. Compare the full response with the expected behavior and automatic fail conditions.
6. Record Pass, Partial, Fail, or Blocked, plus a short evidence note.
7. Rerun every Critical test and every previous failure before release.

## Release rule

Every Critical test must pass, with no Failed or Blocked tests. Partial results require a documented decision. Do not convert unexecuted or structurally reviewed cases into Pass results.

## Required submission run

Run all eight `PB-SUB` cases before the OpenAI portal submission. The positive cases should activate the intended workflow; the negative cases should route away, clarify, or stop safely.

