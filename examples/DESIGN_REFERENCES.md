# Dashboard design revision — v1.1.1

## References and access

- [Tableau Dashboard Showcase](https://www.tableau.com/data-insights/dashboard-showcase): visible previews of Super Sample Superstore and Profitability and Shipping KPIs inspected in the browser. Adapted compact analytical hierarchy, prominent primary chart and supporting detail. Full workbook interactions were not tested.
- [Sales Analytics Dashboard UI/UX — Sahin Mia / Pixelean](https://dribbble.com/shots/27017983-Sales-Analytics-Dashboard-UI-UX): shot visually inspected in the browser. Adapted differentiation between primary plot, supporting metrics and compact record details. No logo, screenshot assets, device frames or exact design copied.
- [Figma dashboard design templates](https://www.figma.com/templates/dashboard-designs/): official gallery listing reviewed, including Simple dashboard mockup and layout/component options. Linked Community file was blocked by robots policy; no visual inspection of that file is claimed. Component consistency is a design objective here, not a claim derived from an inspected Figma file.

## Applied changes

- Compact report header and real anchor navigation in place of the oversized question/header.
- Shared metric strip with fine dividers in place of repeated large rounded tiles.
- Dominant SVG monthly line chart with zero baseline, labelled units, gridlines and textual monthly values.
- Narrower ranked category contribution view with aligned values and shares.
- Quiet borders, restrained blue/slate palette, aligned numerical typography and consistent spacing.
- Expandable records and metric definitions keep detail available without overwhelming the opening view.
- Visible synthetic-data status; no invented targets, growth badges, avatars, notification counts or live-data claims.

## Function and evidence

Region/category filters affect every metric, plot and detail row. Reset restores all records. South + Furniture gives a no-match state. Average monthly revenue = selected total / 6 reporting months. Records use deterministic month adjustments summing to zero, creating variation without changing aggregate acceptance totals.

Executed: package structural checks; existing prototype logic suite passed against the revised embedded script, including known unfiltered/filtered totals, row counts, empty state and reset.

Not executed: rendered browser layout, narrow viewport, keyboard interaction or accessibility conformance. The browser rejected access to the local file URL. No workaround or alternate browser was used to bypass that policy. Refresh the locally opened HTML in your own browser to inspect the revision.

This is an HTML design prototype, not a native Power BI file. The skill now instructs future runs to inspect real references when accessible and to check the rendered composition against the chosen reference direction.
