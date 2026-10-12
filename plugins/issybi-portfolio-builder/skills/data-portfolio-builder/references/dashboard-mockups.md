# Dashboard Mockups and Interactive Prototypes

Use when the user requests dashboard design, a mockup, wireframe, visual redesign, or interactive prototype. Produce a concrete artifact using available file/UI tools. Keep this workflow portable: do not require a particular proprietary tool, plugin, renderer, or paid asset.

## 1. Establish enough of the brief

Use supplied audience, decision, questions, metrics, target tool, screenshots, and brand references. Ask only for a missing choice that would materially change the design; otherwise state reasonable defaults and proceed. Preserve accepted project decisions. A design-only request need not wait for full data access.

Select the requested fidelity:

- **Static mockup:** shows layout and states; controls are labelled as proposed, not functional.
- **Interactive prototype:** filters, navigation, sort, drill, reset, and tooltips actually work within a local demonstration. Implement only interactions relevant to the brief.
- **Production dashboard:** requires actual model/data integration and platform testing; a browser prototype does not establish Power BI functionality.

Default to a self-contained local HTML/CSS/JS prototype when interactions matter and file creation is available. Use a static artifact when requested or appropriate. If the runtime cannot create artifacts, provide a bounded layout specification and state the limitation. Do not substitute a raster image for working interaction.

## 2. Keep evidence and illustrative content distinct

Use verified values only when their provenance and calculations are established. If data is missing, create small synthetic records or labelled placeholders appropriate to the concept; visibly label the entire artifact **Illustrative / synthetic data — not real findings**. Label individual illustrative values in mixed-evidence views. Never invent actual-vs-target comparisons, causes, confidential details, savings, or company results.

For a functional prototype, calculate cards and charts from the same demonstration records. Do not hard-code impressive KPIs that stay unchanged when filters move. Define denominator, unit, date basis, and missing-value handling. Show which controls are implemented versus proposed. Do not imply live refresh, authentication, persistence, export, or RLS unless implemented and tested. Avoid upload controls or network calls unless the user requests them.

## 3. Ground the style in real references

Reuse the user's supplied references, examples already inspected in this conversation, or the documented direction in [design-references.md](design-references.md). Do not reopen all reference sites on every request. When fresh research is requested or needed to resolve a material design choice, inspect a small relevant set from Tableau.com/Tableau Public, Dribbble or Figma's official dashboard gallery/accessible Community files. Prioritise the user's named sources and disclose any coverage gaps. Keep one coherent visual direction.

Record actual pages inspected and whether visual inspection succeeded. A search snippet or template listing is not visual inspection of a file. If a source is inaccessible, use accessible previews or another relevant example and disclose the gap; do not pretend a blocked file was reviewed. Do not let an inaccessible reference block useful design work.

Translate the references into concrete decisions: grid and density, type sizes/weights, spacing, palette/semantic colours, border/radius treatments, chart styling, filter placement and selected/hover/focus states. Use Tableau for analytical legibility and drill/filter patterns; Dribbble for composition and craft; Figma for reusable component states and spacing. Treat those as prompts for inspection, not proof that every example is good.

Avoid the default AI dashboard pattern: oversized marketing headline, identical rounded KPI tiles, arbitrary gradients, decorative sidebars, fake avatars/notifications, and repeated generic chart cards. Use a compact report header, proportional visual hierarchy, aligned numerical typography, quiet boundaries and meaningful density when appropriate. Do not ban cards or a colour categorically; use them deliberately. Do not copy logos, exact layouts or unlicensed assets. Adapt design principles to the analytical brief.

## 4. Design for the decision and visual quality

Give the page a deliberate visual concept appropriate to the audience, rather than a generic wall of cards. Use a readable type scale, coherent spacing, alignment, restrained palette, and one clear accent. Use brand references when supplied; otherwise choose and state a suitable default.

- Lead with the question or decision, scope/period, and most useful contextual measures.
- Make the primary analytical comparison prominent; place detail and exceptions below or behind a meaningful drill action.
- Prefer direct labels, useful units, sorted comparisons, visible scale, and concise annotations grounded in the displayed evidence.
- Use colour consistently for meaning. Avoid red/green-only distinctions, low contrast, tiny text, decorative gradients, 3D charts, and ornamental graphics that obscure values.
- Use whitespace and grouping to separate overview, diagnosis, and detail. Avoid forcing a fixed number of KPIs or pages.
- Include selected filters and reset close together, a clear empty state, and data/source status where useful.

Accessibility: use semantic controls with labels, visible keyboard focus, logical tab order, text or shape cues alongside colour, and textual chart summaries or data tables. Aim for WCAG AA contrast (4.5:1 normal text; 3:1 large text and meaningful UI graphics). Do not claim compliance from intent alone. Reflow at narrow widths or document the target platform's separate mobile layout; avoid clipped labels and controls.

## 5. Specify and implement behaviour

For each implemented control, specify affected visuals, default selection, reset behaviour, and relevant empty state. Filtering should recompute totals, ratios, comparisons, and details consistently. Navigation should change visible content; drill actions should preserve understandable context and provide a return path. Show unavailable functionality as proposed/disabled rather than simulating success.

Prefer semantic HTML and local data with no build step for portable demos. Use deterministic synthetic data so results are reproducible. Avoid remote fonts, libraries, or imagery unless needed and available. Use responsive SVG or native layout for charts, with accessible text/table alternatives.

## 6. Verify the artifact

Open the actual artifact in an available browser or renderer and inspect the rendered result. Test relevant filters individually and together, reset, navigation/drill/sort if present, no-match states, and keyboard access. Compare at least one filtered and unfiltered aggregate with the source records independently of the rendering logic. Inspect the intended desktop viewport and a narrow viewport for overflow and legibility. Fix observable issues and repeat only affected checks. Compare the rendered design with the chosen references for hierarchy, density, alignment, chart readability, and component consistency. Record concrete differences; “looks professional” alone is not a visual acceptance check.

Distinguish executed checks from design intentions. If browser/rendering tools are unavailable, deliver the source with visual and interaction verification clearly pending. Do not claim that a native .pbix or BI deployment was created when only HTML, SVG, or a design specification exists.

## 7. Deliver design and handoff

Return the local artifact, a short account of the visual concept and implemented controls, evidence status, and material limitations. Include a compact implementation map: question -> visual -> source/metric -> interaction. For Power BI, identify candidate native visuals, slicers, relationships, and measure logic; mark any platform-specific behaviour as requiring implementation/testing. Keep those technical notes outside the dashboard user's main flow.

A mockup can become portfolio evidence of UX and analytical design. It is not proof of a functioning production data model or improved business outcomes.
