# Evidence Contract

Use the smallest evidence set adequate for the requested work. Evidence adequacy depends on the claim, not on a universal requirement to upload a complete dataset.

| Available evidence | Permitted work | Limits to state |
| --- | --- | --- |
| Topic or idea only | Data search, provisional concept, proposed schema, illustrative mockup | No verified fields, feasibility, quality, or findings |
| Screenshot / report image | Layout, hierarchy, chart readability, visible story critique | No validation of measures, model, interactions, or underlying data |
| Schema / ERD / data dictionary | Conditional project plan, field mapping, proposed calculations and validation | Keys and types may be documented rather than tested; coverage, quality, and findings remain unknown |
| Sample rows / query extracts | Inspect sample types, grain clues, example transformations; provisional plan | Do not generalise missingness, uniqueness, distributions, or date coverage to the full source |
| Full accessible dataset / database | Profile relevant fields and relationships; execute analysis where authorised and tools permit | State filters, period, extraction limits, failed checks, and whether completeness is known |
| Existing analysis with outputs | Review results within their documented scope; reproduce where source and tools permit | Reading a result is not independently reproducing it |
| Synthetic data | Demonstration, prototype interactions, method testing | Generated results do not establish real organisational behaviour or impact |

## Inspection record

Keep a compact table or paragraph, proportionate to the task:

- **Evidence:** file or source identifier; inspected sheet, tables, fields, rows, period, filters, and whether complete, sampled, described, or synthetic.
- **Executed checks:** method plus actual result for checks performed. Useful checks include row grain, key uniqueness, join cardinality, missingness, valid ranges, and date coverage. Run only relevant checks available to the tools.
- **Unknown / pending:** checks not run, inaccessible sources, uncertain semantics, missing fields, or incomplete coverage.
- **Consequence:** which questions remain feasible, provisional, or blocked.

Do not turn a candidate primary key into a verified unique key or sample date range into dataset coverage. If a required file is inaccessible, say so and work from other supplied evidence within its limits.

## Trace questions to evidence

For each core question, identify source fields, row grain, filters, feasibility label, and necessary calculation or join. Reference the inspection record instead of repeating it. Document metric denominator, unit, aggregation, missing-data treatment, and time basis where relevant. Profit requires a defensible cost definition; revenue alone cannot establish it. A percentage without its denominator is not a complete metric.

Schema-only example: revenue by month is provisionally Derivable from a documented date, quantity, and price; execution must confirm types, row grain, discounts, returns, and duplication. It is not a finding about which month performed best.

## Safe evidence collection

Prefer portable database files, schema exports, ERDs, redacted rows, or bounded query extracts. Confirm the SQL dialect when SQL is needed. Never request passwords, secrets, unrestricted production access, or credential-bearing connection strings. Avoid copying private source data into public artifacts. Publication or installation is separate from creating a local deliverable.
