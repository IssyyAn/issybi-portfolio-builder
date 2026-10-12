# Sales dashboard example — v1.1.1

Self-contained local HTML with synthetic month × region × category records for Jan–Jun 2026. All values are illustrative. No libraries, remote fonts, network calls, authentication, or native Power BI model.

| Question | Visual | Metric | Interaction |
| --- | --- | --- | --- |
| What is selected revenue? | Metric strip | Sum of selected synthetic USD revenue; average / 6 months | Region/category filters and reset |
| How does revenue vary by month? | SVG line chart and textual monthly values | Monthly selected totals | Both filters |
| Which categories contribute most? | Sorted bars and shares | Category total / selected total | Both filters |
| What records support this? | Expandable table | Every selected synthetic record | Both filters and disclosure |

Known totals: all $476,400 / 30 records; North $271,800 / 18; Furniture $78,000 / 6; North + Technology $90,600 / 6; South + Furniture $0 / 0. Reset restores initial state. Average always uses six reporting months.

The embedded script passed tests/check_mockup.mjs under a DOM stub. Browser visual, native-control and keyboard verification remain pending because local file access was blocked. See DESIGN_REFERENCES.md for sources actually inspected and design changes.
