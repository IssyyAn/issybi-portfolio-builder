# Portfolio Builder

Portfolio Builder is an Issy BI skill that turns a topic, dataset, database, or existing project into one focused, evidence-based data portfolio project.

It is designed to help learners show analytical judgement—not simply produce another dashboard. The skill checks the evidence first, connects a realistic stakeholder to an actionable decision, separates supported analysis from unsupported ideas, and creates a practical build and case-study brief.

## What it does

- Starts from a topic, project idea, dataset, database schema, or existing project.
- Inspects available data evidence before producing a detailed project plan.
- Offers exactly two stakeholder-and-decision routes when the user has not already chosen a suitable route.
- Labels analysis as Supported, Derivable, or Not supported.
- Supports SQL, Python, spreadsheets, BI, data cleaning, automation, storytelling, forecasting, experimentation, and synthetic-data projects.
- Preserves good work in an existing project and recommends targeted improvements.
- Produces portfolio evidence and case-study guidance without inventing findings, targets, or business facts.

## Repository layout

- `plugins/issybi-portfolio-builder/` — portable Agent Plugins package for ChatGPT and Codex.
- `.agents/plugins/marketplace.json` — repo marketplace entry for local testing.
- `PORTFOLIO_BUILDER_LITE.md` — copy-paste version for people who cannot install the plugin.
- `submission/` — OpenAI listing copy, starter prompts, release notes, and eight review test cases.
- `docs/` — privacy, terms, support, testing, and release instructions.

## Local installation for testing

After uploading this repository to GitHub, add it as a plugin marketplace:

```bash
codex plugin marketplace add OWNER/issybi-portfolio-builder
```

Replace `OWNER` with your GitHub username or organisation. Restart the ChatGPT desktop app, open the Plugins Directory, choose **Issy BI Plugins**, and install **Portfolio Builder**.

For a local checkout, use:

```bash
codex plugin marketplace add /absolute/path/to/issybi-portfolio-builder
```

## Public release

GitHub is the public source and support home. Public discovery in ChatGPT and Codex requires a separate skills-only submission through the OpenAI plugin submission portal. Follow [the release checklist](docs/RELEASE_CHECKLIST.md).

## Try it

Useful starter prompts include:

- “I have a retail sales dataset. Turn it into a two-week Power BI portfolio project.”
- “Help me design a SQL-only portfolio project from this schema. Do not include a dashboard.”
- “I like football but do not have data yet. Help me choose the right next step.”
- “Strengthen the analytical story in my existing dashboard without replacing good work.”

## Test status

The skill package passes structural validation. The release workbook contains 67 full-suite tests plus eight curated OpenAI submission cases. Submission cases intentionally remain marked **Not Run** until they are executed in fresh chats and evidence is recorded.

## License

MIT. See [LICENSE](LICENSE).

