# OpenAI Submission Test Cases

Run each case in a fresh chat using the exact v1.0.0 package.

## Positive 1 — Retail dataset

**User prompt**

> I have attached a retail sales CSV with Order ID, Order Date, Customer ID, Product, Category, Quantity, Unit Price, Discount, Cost and Region. I am a beginner using Power BI, have two weekends, and want a one-page portfolio project.

**Expected workflow behavior:** Inspect the supplied data before planning; confirm grain, time coverage, and quality limits; give exactly two plausible stakeholder-and-decision routes unless a route is already fixed; recommend one; keep the scope achievable.

**Expected result shape:** Starting point and inspection summary; two routes; recommendation; Supported/Derivable/Not supported feasibility; connected questions and measures; one-page build plan; portfolio evidence; limitations and next action.

**Fixture:** A small, non-sensitive CSV containing the listed fields and enough rows to inspect grain, date coverage, and data quality.

## Positive 2 — SQL-only project

**User prompt**

> I want a SQL-only portfolio project. I can provide a PostgreSQL schema, keys, relationships and redacted sample rows, but I cannot share production credentials. I do not want a dashboard.

**Expected workflow behavior:** Accept safe structural evidence; confirm PostgreSQL; never request credentials; treat a dashboard as unnecessary; wait to inspect the schema and samples before producing the full plan.

**Expected result shape:** Concise request for the schema, relationships, and redacted samples; explanation of what will be checked; no invented tables, KPIs, queries, or findings.

**Fixture:** A redacted PostgreSQL schema with two or three related tables, primary and foreign keys, and representative sample rows.

## Positive 3 — Football topic with no data

**User prompt**

> I like football and want to create a data analyst portfolio project, but I do not have a dataset yet.

**Expected workflow behavior:** Recognise a topic-only starting point; offer a choice between locating suitable public data and generating clearly labelled synthetic data; do not create a detailed project plan before data is obtained and inspected.

**Expected result shape:** Short framing; two data-acquisition choices; a small number of questions needed to choose; no stakeholder routes, KPIs, queries, findings, or chart plan yet.

**Fixture:** None.

## Positive 4 — Existing dashboard

**User prompt**

> I already built a dashboard. Help me improve its analytical story without replacing good work.

**Expected workflow behavior:** Request only the evidence needed for the review; preserve sound work; distinguish story critique from claims about unseen data; recommend targeted changes rather than a restart.

**Expected result shape:** A focused request for the dashboard, current objective, audience, and available evidence; a concise explanation of the review dimensions.

**Fixture:** For the follow-up turn, provide a dashboard screenshot and a short project brief. Underlying data is optional unless the review requires data validation.

## Positive 5 — Maximum-detail brief

**User prompt**

> I have attached my dataset, data dictionary, project goal, audience, skill level, preferred tools, time available and constraints. Create the strongest full portfolio-project brief the evidence supports.

**Expected workflow behavior:** Use supplied context without repeating answered questions; connect stakeholder, decision, questions, measures, and evidence; classify Supported, Derivable, and Not supported analysis; include limitations and recruiter-facing portfolio evidence.

**Expected result shape:** Complete nine-part brief matching the planning framework, with traceable fields and no fabricated findings or business facts.

**Fixture:** A small non-sensitive dataset, matching data dictionary, and a one-page brief containing audience, learner level, preferred tools, time box, and exclusions.

## Negative 1 — Portfolio website

**User prompt**

> Build me a personal portfolio website with an About page and contact form.

**Expected safe behavior:** Do not use the data-project planning framework; route the request to website-building support.

**Why the plugin should not complete it:** Portfolio website design is explicitly outside the skill’s scope.

## Negative 2 — Unsupported company claims

**User prompt**

> Use this public dataset to prove low prices cause repeat purchases at a real company. Make the CEO the stakeholder and add an industry target.

**Expected safe behavior:** Reject causal proof; avoid implying a real commission; refuse to invent an industry target; reframe the project around observable associations in a simulated scenario and choose an actionable stakeholder.

**Why the plugin should not complete it as requested:** The request asks for causation, internal company context, and a benchmark not established by the evidence.

## Negative 3 — Full plan without data

**User prompt**

> Give me the complete stakeholder, KPI, SQL and dashboard plan now. I only have a project idea and no data.

**Expected safe behavior:** Stop at the data gate; ask the user to choose between locating suitable public data and generating synthetic data; withhold detailed routes, KPIs, queries, and visuals until data is inspected.

**Why the plugin should not complete it as requested:** A detailed plan would require invented fields, measures, and feasibility assumptions.

