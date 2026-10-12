# Portfolio Builder

Portfolio Builder is an Issy BI skill that turns a topic, dataset, database, or existing project into one focused, evidence-based data portfolio project.

It helps learners show analytical judgement and can create polished dashboard mockups or interactive prototypes from a brief. The skill checks the evidence first, connects a realistic stakeholder to an actionable decision, separates supported analysis from unsupported ideas, and creates a practical build and case-study brief.

## What it does

- Starts from a topic, project idea, dataset, database schema, or existing project.
- Matches evidence to the task: conditional plans from schemas, focused reviews from screenshots, executed findings from actual analysis.
- Recommends a feasible stakeholder-and-decision route; offers alternatives when useful.
- Records inspection scope, executed checks, unknowns, and field-level question feasibility.
- Creates dashboard mockups with deliberate visual design, working controls when requested, and explicit illustrative-data labels.
- Labels analysis as Supported, Derivable, or Not supported.
- Supports SQL, Python, spreadsheets, BI, data cleaning, automation, storytelling, forecasting, experimentation, and synthetic-data projects.
- Preserves good work in an existing project and recommends targeted improvements.
- Produces portfolio evidence and case-study guidance without inventing findings, targets, or business facts.

## Repository layout

- `plugins/issybi-portfolio-builder/` — portable Agent Plugins package for ChatGPT and Codex.
- `PORTFOLIO_BUILDER_LITE.md` — copy-paste version for people who cannot install the plugin.
- `submission/` — OpenAI listing copy, starter prompts, release notes, and eight review test cases.
- `docs/` — privacy, terms, support, testing, and release instructions.

## Local packages

The source package is in `plugins/issybi-portfolio-builder/`. Import the plugin or skill archive through your host's supported local installation flow, or use `PORTFOLIO_BUILDER_LITE.md` as a copy-paste alternative. Installation and host compatibility must be checked in the intended client; this source revision does not install itself.

Build local archives with `python tools/package_release.py` (or `--output /path/to/outputs`). The script validates the source, creates source/skill/plugin ZIPs, CRC-checks them and writes SHA-256 hashes. It does not install or publish.

## Public release

GitHub is the public source and support home. Public discovery in ChatGPT and Codex requires a separate skills-only submission through the OpenAI plugin submission portal. Follow [the release checklist](docs/RELEASE_CHECKLIST.md).

## Try it

Useful starter prompts include:

- “I have a retail sales dataset. Turn it into a two-week Power BI portfolio project.”
- “Help me design a SQL-only portfolio project from this schema. Do not include a dashboard.”
- “I like football but do not have data yet. Help me choose the right next step.”
- “Strengthen the analytical story in my existing dashboard without replacing good work.”

## Dashboard mockups

Designs should use relevant Tableau, Dribbble and Figma references where accessible. The skill records what was actually inspected and translates observations into concrete layout, chart and component decisions; see `references/design-references.md` in the skill.

Ask: “Create a polished, functional one-page sales dashboard mockup with region/category filters and reset. Use synthetic data and deliver local HTML.”

Mockups can proceed without real data if clearly labelled illustrative. Interactive prototypes compute their displayed values from demonstration records; they do not establish real findings or a functioning native BI model. See the skill's dashboard-mockups reference for design, interaction, verification, and handoff requirements.

A generated example is in `examples/dashboard-mockup.html`, with its metric/interaction map in `examples/HANDOFF.md`. This example is not a mandatory layout template.

## Test status

The v1.0 workbook is retained as historical coverage and is not a pass record for v1.1. The current behavioural cases and comparison protocol are in `tests/BEHAVIORAL_CASES.md` and `docs/TESTING.md`. Structural checks do not prove model behaviour. See `tests/VALIDATION_RESULTS.md` for the checks actually executed on this revision.

## License

MIT. See [LICENSE](LICENSE).

