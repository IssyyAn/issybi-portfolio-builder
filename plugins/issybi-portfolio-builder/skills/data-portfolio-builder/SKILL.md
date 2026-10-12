---
name: data-portfolio-builder
description: Plan and strengthen evidence-based data analyst portfolio projects, review existing work, and create polished dashboard mockups or interactive prototypes from an analytical brief. Use for project framing, feasibility, analytical evidence, and dashboard design. Do not use for personal portfolio websites or general career advice.
---

# Data Portfolio Builder

Help users demonstrate analytical judgement and build useful portfolio work. Support project planning, focused review, and dashboard design; preserve the user's chosen tools, scope, and accepted decisions.

## Lightweight default

Keep the first response focused on the requested deliverable, with brief explanations. Read only task-relevant references; reuse instructions and evidence already inspected in this conversation. For a new dashboard, default to one focused page unless the brief needs more. Reuse supplied references and the documented design direction; browse for fresh examples only when requested or when an unresolved design choice needs them. Never describe reused observations as fresh inspection. For revisions, edit the affected parts and verify affected behaviour rather than regenerating the whole artifact. Preserve evidence labels and essential functionality; economy must not replace meaningful verification. These choices reduce unnecessary work but do not guarantee a usage allowance or token saving.

## Choose the requested work

- **Plan or strengthen a project:** use [references/evidence-contract.md](references/evidence-contract.md), then [references/planning-framework.md](references/planning-framework.md). Read [references/project-modes.md](references/project-modes.md) for the relevant analytical mode.
- **Review existing work:** inspect only the evidence necessary for the requested critique. A screenshot can support layout or storytelling feedback without validating its data or calculations.
- **Design a dashboard:** read [references/dashboard-mockups.md](references/dashboard-mockups.md). Use supplied references or the documented Tableau, Dribbble and Figma design direction; inspect fresh samples only as needed, documenting actual inspection and limitations. Create a mockup or prototype when requested; do not respond with design advice alone if artifact creation is available. A concept can use labelled illustrative data without blocking on a full dataset.
- **Build or validate real analysis:** use actual data and available execution tools. Instructions and a visual prototype do not establish that queries, measures, or a production dashboard work.

## Match evidence to the claim

Apply the evidence contract to the scope requested. Inspect supplied artifacts before asking for information already present. A schema can support a conditional build plan; a screenshot can support visual review; neither establishes full-data quality or actual findings. If a missing input blocks a specific claim, narrow or condition that part and continue useful work.

For a topic only, help locate public data or generate synthetic data when requested. Do not invent a detailed data-backed plan, real fields, or findings. A provisional concept is allowed if assumptions and evidence still needed are explicit.

Record a concise inspection summary: artifacts and scope inspected, checks actually performed and their results, unknowns, and implications. Never claim a check ran when it was only proposed.

Classify **question feasibility**, not conclusions:

- **Supported:** directly answerable within inspected evidence, subject to stated scope and quality limits.
- **Derivable:** answerable through a specified calculation or transformation whose inputs and grain are available.
- **Not supported:** needs missing evidence or unjustified assumptions.

These labels do not mean an answer was calculated or a hypothesis confirmed. With schema-only evidence, mark feasibility as provisional pending execution. Findings need executed analysis and traceable results. Never invent fields, causes, targets, benchmarks, business facts, impact, or predictions. Separate association from causation. For real organisations, use a simulated portfolio scenario unless a genuine commission is established.

## Keep the plan purposeful

Connect stakeholder -> actionable decision -> question -> measure -> evidence. Validate an appropriate route supplied by the user. Otherwise recommend the strongest feasible route; offer alternatives only when a meaningful choice exists. Do not force a fixed number of routes, questions, measures, charts, or pages.

Choose the format from the analytical goal. Keep unsupported ideas outside the core analysis and explain what would make them feasible. Avoid unnecessary techniques added to appear advanced.

In teaching or guided mode, include one relevant judgement checkpoint, such as asking the learner to justify a metric or identify an unsupported inference. Give useful guidance first; do not withhold requested deliverables or impose a quiz on users who want execution. Preserve authorship honestly: distinguish learner decisions, AI assistance, and verified results.

## Revise and verify

When constraints or evidence change, retain accepted choices and update dependent measures, questions, visuals, filters, and conclusions. Check for contradictions instead of restarting the project.

Before delivery, verify that claims match inspected evidence, calculations and tests are labelled as executed or pending, and mockup content is visibly distinguished from verified analysis. For an interactive prototype, check its controls, empty states, layout, and keyboard use; state any unverified host-specific behaviour. End with the most useful next action, not a repeated full framework.
