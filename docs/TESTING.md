# Testing Guide — v1.1 candidate

## Levels of evidence

- Structural validation checks package files, references, manifest assets, and frontmatter. It does not execute an AI workflow.
- Independent forward tests apply the source skill in fresh isolated agent contexts and save actual outputs. They are limited behavioural evidence, not proof of installed-client compatibility or broad superiority.
- Host acceptance tests install the exact archive in the intended client, run realistic requests, and inspect actual artifacts/interactions. Mark tests Not Run until executed.

## Current suite

Use tests/BEHAVIORAL_CASES.md for v1.1 scope and the eight updated submission cases for submission review. Keep the v1.0 workbook as historical coverage; its exact-two-route and absolute data-gate expectations are superseded by evidence-contract.md and the revised planning framework. Do not count historical results as v1.1 passes.

For each case, save input/fixture version, model/host/settings where observable, package version/hash, tool access, full output/artifacts, result (Pass / Partial / Fail / Blocked / Not Run), and a short reason tied to observable behaviour. Never mark a proposed check or wording review as executed behaviour.

## Comparison protocol

Use the same model/settings, data, task, and tool access in fresh contexts for: (A) ordinary prompt; (B) a strong prompt asking for grounded feasibility, assumptions and validation; (C) the skill. Do not give one condition privileged evidence. Save full outputs. Repeat conditions where practical; a single run is exploratory. Do not select only favourable examples.

Score factual/field accuracy, feasibility, decision relevance, uncertainty handling, and revision consistency on a 0–2 rubric: 0 materially wrong/missing; 1 partly useful with a material gap; 2 adequate within supplied scope. Also record extra clarification turns and manual corrections where observable. Do not infer timings, token savings, or statistical superiority without measurement. Cases should include missing costs, missing customer identifiers, causal overreach, schema-only planning, and a later constraint change.

## Mockup checks

Open the generated artifact, inspect desktop and narrow layouts, test individual/combined filters, reset and no-match state, keyboard focus and implemented navigation/sort/drill. Independently recalculate at least one unfiltered and filtered aggregate from records. Check visible synthetic labels and honest distinction from native BI. An HTML source review alone is not rendered verification.

## Release rule

Every current Critical case must pass; no Failed or Blocked Critical cases. Document partials and host-specific limitations. Run all eight submission cases in the intended host before submission. Independent source tests cannot replace installed-package testing. Do not submit or publish merely because structural checks passed.
