# SQL-only portfolio plan: category review for regional sales operations

Build a PostgreSQL analysis that helps a regional sales operations lead identify categories worth investigating. Deliver SQL files and a short decision memo; no dashboard is needed. With schema only, the useful output now is a conditional analysis design and runnable query templates, not findings or category rankings.

The supplied `sales_line` table is documented as one row per order line, with order and line identifiers, date, region, category, quantity, unit price, and a discount amount per line. That grain has not been verified. There are no costs, customer identifiers, targets, or returns fields.

## What this project can answer

- Which region/category combinations contribute the most recorded net sales and units?
- Which categories have declining sales or units across comparable periods?
- Where do discount rates, realized unit prices, or category sales concentration merit review?

Use “recorded net sales” to mean `quantity * unit_price - discount_amount`. This assumes unit price is the pre-discount price, discounts apply once per line, and all amounts share a comparable currency. It does not account for unrecorded returns, taxes, shipping, or cancellations. Confirm those definitions before treating the result as business revenue.

## Requested metrics and the evidence boundary

| Request | Feasibility with this schema | Useful treatment |
|---|---|---|
| Profit margin | Not computable: there is no cost information. | Explain `(net sales - attributable costs) / net sales`, with cost scope agreed in advance. Discount rate is a separate measure, not a margin substitute. |
| Repeat purchase rate | Not computable: orders cannot be connected to customers. | Specify a future cohort measure: customers placing another distinct order within 90 days of their first observed order, divided by eligible customers with a complete 90-day follow-up. First observed does not necessarily mean first-ever purchase. |
| Why low prices cause repeat purchases | Unsupported: neither repeat purchases nor a causal effect is identifiable here. | Treat affordability encouraging another purchase as a hypothesis. A later randomized price or promotion experiment could test it, with customer linkage, follow-up, and safeguards against confounding discount effects with price effects. An observational association alone would not establish causation. |

## SQL workflow

1. **Validate before aggregating.** Write checks for duplicate `(order_id, line_id)` values, null identifiers/dates/dimensions/measures, nonpositive quantities, negative prices or discounts, and discounts above gross line sales. Investigate exceptions; negative quantities could encode returns and should not be silently removed. Check whether each order maps consistently to a region/date and whether order IDs are globally unique. Report date coverage and monthly row/order counts. These checks are planned, not completed.
2. **Create a transparent line calculation.** Preserve source fields and add gross line sales and recorded net sales. Do not silently replace missing amounts with zero. If validations fail, document and repair the definition or quarantine exceptions with counts and amounts before using the summaries.
3. **Aggregate monthly by region/category.** Include distinct order count, units, gross sales, discounts, recorded net sales, weighted discount rate, and realized sales per unit. Category order counts overlap when an order contains multiple categories, so they are not additive across categories. Ratios should use sums rather than averages of line ratios.
4. **Compare complete, comparable periods.** Parameterize the dates for a business-confirmed complete month or quarter. Compare prior periods and, when coverage permits, the same period a year earlier. Missing months are unknown until source completeness is confirmed, not automatic zero sales. Category mix changes can affect average unit prices because there is no product identifier.
5. **Produce a review queue.** Show the component measures and supporting volumes. Flag categories conditionally when recorded sales decline materially, discounts rise without unit growth, or a large sales share makes a decline consequential. Set thresholds with the lead later; label initial thresholds as exploratory, not targets or proven underperformance. Keep small-volume categories visible but mark their instability. A flag prompts investigation, not a price recommendation.

Example monthly summary, usable only after the assumptions and quality checks above pass:

```sql
-- :start_date inclusive; :end_date exclusive.
-- Substitute bound parameters through the chosen SQL client.
WITH lines AS (
    SELECT date_trunc('month', order_date)::date AS month,
           region, category, order_id, quantity,
           quantity * unit_price AS gross_sales,
           discount_amount,
           quantity * unit_price - discount_amount AS net_sales
    FROM sales_line
    WHERE order_date >= :start_date::date
      AND order_date < :end_date::date
)
SELECT month, region, category,
       count(DISTINCT order_id) AS category_orders,
       sum(quantity) AS units,
       sum(gross_sales) AS gross_sales,
       sum(discount_amount) AS discounts,
       sum(net_sales) AS recorded_net_sales,
       sum(discount_amount) / nullif(sum(gross_sales), 0)
           AS weighted_discount_rate,
       sum(net_sales) / nullif(sum(quantity), 0)
           AS realized_sales_per_unit
FROM lines
GROUP BY month, region, category
ORDER BY month, region, recorded_net_sales DESC;
```

PostgreSQL aggregate functions can ignore null measures and produce misleading partial totals; the preceding quality checks are a prerequisite, not optional cleanup.

## Portfolio deliverables and honest completion criteria

Prepare `01_quality_checks.sql`, `02_line_metrics.sql`, `03_category_trends.sql`, and `04_review_queue.sql`, plus a README with the business question, metric definitions, assumptions, execution order, and unresolved validation. Include a concise memo template linking each eventual review flag to its numbers, alternative explanations, and a next investigation.

Without rows or database access, label the portfolio **schema-grounded design, not executed analysis**. Do not fabricate findings, profit margins, repeat rates, or successful query execution. A small optional synthetic SQL fixture can demonstrate expected calculations, but must be labeled synthetic and cannot validate production behavior. This still makes a useful project now: it demonstrates decision framing, SQL design, and disciplined limits on what the data can support.
