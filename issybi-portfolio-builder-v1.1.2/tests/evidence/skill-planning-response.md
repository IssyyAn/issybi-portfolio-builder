# Regional category review: SQL investigation plan

Build a SQL-only portfolio investigation for a simulated regional sales operations lead deciding which categories warrant further review. PostgreSQL is confirmed. The deliverable is a ranked category table and a concise written decision brief, with SQL and validation evidence; no dashboard. The aim is to demonstrate defensible metric design, joins and aggregation, and honest analytical limits. No deadline was supplied; use three implementation passes rather than inventing a time commitment.

## Evidence inspected

I read `../sales-schema.md`: `sales_line`, documented as one row per order line, with `order_id`, `line_id`, `order_date`, `region`, `category`, `quantity`, `unit_price`, and `discount_amount`. The dictionary specifies discounts as amounts per line and identifies PostgreSQL. It explicitly excludes costs, customer identifiers, targets, returns, and accessible rows.

Completed checks: inspected the documented fields, grain, discount semantics, missing inputs, and dialect. No database queries or row-level checks ran. Uniqueness, join cardinality, nulls, valid ranges, date coverage, and completeness remain unverified. Consequently, the plan below is conditional; it contains no findings about category performance.

## Decision and feasible questions

| Question | Source, grain and calculation | Feasibility |
| --- | --- | --- |
| Which categories account for the largest observed sales amounts within a region? | Aggregate order lines by region/category over a chosen complete period. Sum `quantity * unit_price - discount_amount`; also count distinct `order_id`. | Provisionally Derivable; validate pricing and order semantics first. |
| Which categories have declining sales or increasing discount intensity? | Same grain, compared across equal, complete periods using `order_date`; retain both levels and changes. | Provisionally Derivable if date coverage supports comparable periods. |
| What is each category's profit margin? | Requires a defensible cost input absent from this schema. | Not supported. |
| What is each category's repeat purchase rate? | Requires a stable customer identifier absent from this schema. | Not supported. |
| Do low prices cause repeat purchases? | Requires customer-level outcomes and a credible causal design, neither available. | Not supported. |

The core investigation can nominate categories for review based on sales movement and discount exposure. It cannot determine unprofitability, retention, target attainment, or which category deserves a price change.

## Measures and rules

For a selected region and explicit half-open date window (`order_date >= start_date AND order_date < end_date`), calculate:

- **Observed sales amount after recorded discounts:** sum of `quantity * unit_price - discount_amount`. Subtract the discount once per line. Currency is unspecified, so label this as source currency and confirm comparability before combining regions. This is not verified accounting revenue: returns, taxes, cancellations, and other adjustments are unknown.
- **Gross line amount:** sum of `quantity * unit_price` before recorded discounts.
- **Discount intensity:** sum of `discount_amount` divided by summed gross line amount, expressed as a percentage. Return null when the denominator is zero; do not average line percentages.
- **Category order count:** distinct `order_id` within region/category/window. An order containing multiple categories contributes to each category, so these counts are not additive across categories.
- **Period sales change:** current-period sales minus prior-period sales, plus percentage change using prior sales as denominator. Report percentage change as undefined when the prior value is zero; show absolute change alongside it. Use equally complete periods rather than comparing a partial month with a full month.

Quarantine and count records with null required inputs instead of silently converting unknown values to zero. Preserve and review negative quantities, prices, or discounts before deciding whether they are valid adjustments. Keep null region/category records in an explicit exception output. Do not assume `order_id` is globally unique across regions or that an order has one consistent date until tested.

Requested measures remain documented extensions, outside the core results:

- **Profit margin:** `(sales after relevant adjustments - attributable cost) / sales after relevant adjustments * 100`. A defensible cost definition, currency basis, allocation rules, and compatible grain are required. If costs later arrive at product level, a product identifier and an effective-date mapping would also be needed; those are not supplied fields. Avoid substituting discount intensity for margin.
- **Repeat purchase rate:** proposed definition is the percentage of customers with a category purchase in a baseline period who place a later, distinct order in that same category within 90 days. The denominator is eligible baseline customers with a full 90-day observation window; the numerator is those with a qualifying later purchase. This 90-day window is a portfolio assumption, not a business benchmark. It needs a stable customer-to-order mapping, reliable order dates, history/coverage rules, and a decision on cancellations and returns. Repeated order IDs or lines cannot stand in for returning customers.

Low prices might make purchases more affordable, but that is a possible mechanism, not an established explanation here. Product mix, promotions, seasonality, customer preferences, and purchase frequency could affect both prices and repeat buying. Even a future price/repeat association would not establish causation. A properly designed randomized pricing experiment, with assignment and outcome data and suitable safeguards, could address the causal question; it is outside this schema-only project.

## Build and validate when data becomes available

1. Write `01_profile.sql` to test nulls and duplicates of the documented candidate line key `(order_id, line_id)`, inspect order consistency across dates/regions, profile value ranges and discount anomalies, and count lines by month. Treat each as a pending check, not an assumed pass.
2. Write `02_category_metrics.sql` with parameterized region and date boundaries. Prepare a line-level calculation CTE, aggregate categories and periods separately, and join those aggregates by region/category. The supplied single-table core needs no external join. Use `numeric` arithmetic and `NULLIF` for percentage denominators.
3. Write `03_review_candidates.sql` to compare periods and expose supporting measures. Show categories with sales declines or rising discount intensity, ordered by absolute sales decline within region, with discount movement and sales scale visible. This is a review queue, not proof of a problem; categories without comparable coverage must be flagged. Do not invent targets or pass/fail cutoffs.
4. Write `04_validation.sql` to reconcile aggregate sales with eligible line totals, verify that period joins do not multiply rows, report excluded records and zero denominators, and confirm that complete categories/periods survive the comparison. Do not sum category order counts to reconcile overall order count.
5. Export the review table and write findings only after execution. Explain which candidates merit investigation and what additional operational context is needed before taking action.

Until rows become available, save the SQL specifications and assumptions as unexecuted work. If independently requested later, synthetic data can demonstrate query mechanics, but it cannot supply real category findings or causal evidence.

## Portfolio package

Include the schema and its provenance/licensing status, a short stakeholder brief, the SQL scripts, metric definitions, assumptions, validation queries and their eventual outputs, a bounded results extract, and a one-page decision memo. With the current evidence, label the package a schema-based investigation design. Leave findings and validation results explicitly pending. Disclose AI assistance in drafting the plan and distinguish your own analytical choices from results verified by execution. Do not claim realized commercial impact.

Next action: implement the profiling and aggregation scripts against this documented schema, keeping their execution status visible. The conditional plan is usable now without production access or a questionnaire.
