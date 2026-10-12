# Current revision: v1.1.1 — 2026-10-12

Reference-led design revision applied by the primary agent after the user's visual feedback. See examples/DESIGN_REFERENCES.md for inspected references, changes and access limitations. Package structure and revised embedded prototype logic checks passed. The prior independent planning tests below were executed on v1.1.0; the mockup example was subsequently redesigned, so the independent generation test is historical. No new independent visual-generation or installed-host run is claimed.

Local file access is blocked by browser policy. Rendered appearance, responsive layout, native controls and keyboard checks remain pending. No attempt was made to bypass that rejection. The Figma official gallery listing was reviewed, but the linked Community file was inaccessible.

# Portfolio Builder v1.1.0 — revision and validation

Prepared 2026-10-12 as a local candidate from IssyyAn/issybi-portfolio-builder. No GitHub push, public release, account installation or submission was performed.

## Changes

- Match evidence requirements to requested claims; schemas permit conditional planning, samples permit sample-level checks, screenshots permit visual critique.
- Record inspection scope, executed checks, unknowns and their implications.
- Separate question feasibility (Supported / Derivable / Not supported) from calculated findings or confirmed hypotheses.
- Remove route/question/measure quotas and keep useful accepted decisions.
- Add optional judgement checkpoints while respecting execution-only requests.
- Add dashboard mockups and local functional prototypes: visual hierarchy, typography, colour, spacing, accessibility intent, responsive layout, consistent filtering, reset, empty states, and honest evidence labels.
- Keep native BI implementation and validation separate from HTML prototypes.
- Synchronise Lite prompt, UI metadata, release copy and current behavioural cases.
- Fix an existing validator requirement for a marketplace file absent from the repository and enforce the 30-character listing subtitle limit.

## Executed checks

| Check | Result | Evidence and limits |
| --- | --- | --- |
| Repository release validator | Pass | Python tools/validate_release.py: required files, manifest, contained references, assets, submission-case counts and secret-pattern scan. Structural only. |
| Git diff whitespace check | Pass | git diff --check returned success. |
| E1 schema-only planning | Pass in one independent source-skill run | tests/evidence/skill-planning-response.md: useful conditional PostgreSQL plan, no dashboard/quiz, missing cost/customer inputs and causal overreach correctly bounded; checks labelled unexecuted. |
| E6 later region removal | Pass in continuation | tests/evidence/skill-revision-response.md: removes region-dependent questions, filters, grouping and checks; retains revenue/category plan and unsupported boundaries. |
| M1 prototype generation | Partial | Actual self-contained HTML created with synthetic label, shared-record calculations, requested filters and reset. Rendered visual quality not verified. |
| M2 prototype logic | Pass for logic; rendered checks blocked | node tests/check_mockup.mjs exercises actual embedded script through a DOM stub: initial $476,400 / 30; North $271,800 / 18; Furniture $78,000 / 6; North + Technology $90,600 / 6; South + Furniture $0 / 0; reset restores initial state. These known totals are independent acceptance constants. Native selects, keyboard and responsive layout still need browser checks. |
| Bundled Skill Creator quick_validate.py | Blocked by dependency | Python runtime lacks PyYAML. Attempted isolated dependency resolution was blocked by temporary-file permissions and DNS access. No pass claimed. |
| Rendered prototype/browser acceptance | Blocked | File URL access was unavailable; two loopback preview services timed out in the available browser. No desktop/narrow screenshot or keyboard verification claimed. |
| Installed target-client acceptance | Not Run | Source package has not been installed or exercised in the intended host. |
| Remaining current behavioural cases / eight submission cases | Not Run | See BEHAVIORAL_CASES.md and docs/TESTING.md. Historical workbook results do not establish v1.1 behaviour. |

## Exploratory strong-prompt comparison

One isolated ordinary-agent run used the same schema/task plus explicit grounding, feasibility, uncertainty and validation instructions, without reading the skill. The independent skill run used the revised source and same task. Full outputs are saved in tests/evidence/. Neither condition had source rows or production access. Exact host model/settings were not recorded, so this is a limited qualitative comparison, not a controlled benchmark.

Both outputs correctly rejected unsupported margin, repeat-purchase and causal conclusions and provided useful conditional SQL plans. The skill output made its inspection record and field/feasibility mapping explicit. The strong prompt also handled the central analytical risks well. This does not establish superiority or measured time savings; the skill's supported benefit here is packaging a reusable workflow. Only the skill condition received the later revision turn, so no comparative revision advantage is claimed.

## Dashboard example and handoff

examples/dashboard-mockup.html is a light-theme revenue review generated in the independent test. Its data is synthetic at month × region × category grain for Jan–Jun 2026; it contains no real company findings. examples/HANDOFF.md documents metrics and interactions. It is an example, not a fixed mandatory design or a native .pbix.

## Before a public release

Run the current Critical cases and all submission cases in the intended installed host. Visually inspect desktop and narrow layouts, test native controls/keyboard, independently confirm any new calculations, and record the exact package hash/model/tool conditions. The package is usable for local evaluation, but is not represented as fully release-validated.
