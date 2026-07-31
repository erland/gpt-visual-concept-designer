# T29 — Single compressed retry

## Scenario
The first Image generation call fails after a long design process.

## Expected
- The GPT creates a minimal brief containing subject, composition, 3–7 fixed traits, style and lighting.
- Secondary details and most negative constraints are removed.
- It retries exactly once using Image generation.
- It does not switch to SVG, Python or another renderer.

## Fail
- No retry is attempted.
- More than one retry loop is started.
- A programmatic illustration is substituted.
