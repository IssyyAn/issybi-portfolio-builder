# Test Assets

- BEHAVIORAL_CASES.md: current v1.1 cases and acceptance conditions.
- VALIDATION_RESULTS.md: actual executed checks and limitations.
- evidence/: actual isolated planning and strong-prompt outputs, plus fixture.
- check_mockup.mjs: reproducible embedded-script checks against known totals and filter/reset/empty states; not a browser test.
- Portfolio_Builder_Skill_Test_Plan_v1.0.xlsx: historical 67-case coverage and eight submission cases; not a v1.1 pass record. Exact-two-route and absolute data-gate expectations are superseded.

Run package structure checks with Python tools/validate_release.py. Run example logic checks with Node tests/check_mockup.mjs. Follow docs/TESTING.md for fresh-context comparison and installed-host acceptance.
