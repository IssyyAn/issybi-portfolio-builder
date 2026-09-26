# Project Modes

Choose the mode that best demonstrates the learner's intended skill and supports the selected decision.

Combine modes only when each component adds meaningful portfolio evidence.

## SQL investigation

First inspect the database or sufficient evidence of its structure.

Accept:

- safe accessible connection;
- database file;
- schema or ERD;
- table definitions with columns, data types, keys, and relationships; or
- representative redacted sample rows or query extracts.

Confirm the SQL dialect.

Never request passwords, secrets, unrestricted production access, or connection strings containing credentials. Prefer portable, redacted evidence.

Then plan the investigation, validation checks, queries, documented decisions, and concise findings output.

A dashboard is not required.

## Python or notebook analysis

Prioritise reproducibility.

Include appropriate:

- exploration;
- transformations;
- analytical or statistical reasoning;
- validation;
- visual evidence; and
- limitations.

Do not add modelling or statistical techniques merely to make the project appear advanced.

## Data cleaning or quality project

Focus on:

- profiling;
- documented quality issues;
- cleaning rules;
- before-and-after validation; and
- reusable quality checks or documentation.

The cleaning decisions and validation are the analytical evidence.

## Automation project

Establish:

- the manual problem;
- input and output;
- automated workflow;
- failure handling;
- validation; and
- measurable time or quality benefit when evidence exists.

Do not invent efficiency gains before they have been measured.

## Spreadsheet analysis

Prioritise:

- transparent formulas;
- appropriate controls;
- validation; and
- decision-focused analysis and summary.

Do not treat spreadsheets as inherently less analytical than other tools.

## BI report or dashboard

Use:

- an appropriate data model;
- a small set of decision-focused pages or views;
- measures tied to analytical questions; and
- visuals that support the selected decision.

Do not add pages or KPIs simply to fill the dashboard.

## Data story or research brief

Build a defensible narrative using:

- relevant analysis;
- charts;
- annotations;
- sources;
- uncertainty; and
- limitations.

Separate observed evidence from interpretation.

## Forecasting or experimentation

Use only when the data, design, and learner goal support the method.

State validation requirements and limitations.

Do not imply causal or predictive certainty beyond what the method and evidence justify.

## Visual selection

Recommend visuals only after understanding the question, relevant fields, grain, and audience.

Typical choices:

- trend over time: line chart or small multiples;
- ranked categorical comparison: sorted bar chart;
- composition: stacked bar when totals and components remain readable;
- distribution: histogram, box plot, or dot plot;
- relationship: scatter plot without implying causation;
- actual versus target or prior period: variance chart, bullet chart, or contextual KPI; and
- record-level exceptions: table or matrix.

Do not recommend a visual merely because compatible columns exist. Avoid decorative duplication.

## Synthetic datasets

When the user requests synthetic data:

1. Distinguish a proposed schema or data dictionary from a populated dataset.
2. Establish the intended project, approximate row count, date range, and important behaviours when they materially affect usefulness. Otherwise use and state reasonable defaults.
3. Create the populated dataset in a practical format such as CSV when file creation is available.
4. Clearly label it as synthetic.
5. Document generation assumptions, field definitions, intentional missingness or anomalies, and limitations.
6. Do not copy real personal data or represent synthetic results as genuine organisational evidence.
7. Reinspect the generated dataset before using it to produce the project plan.

