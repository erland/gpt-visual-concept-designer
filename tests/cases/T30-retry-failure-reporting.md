# T30 — Retry failure reporting

## Scenario
Both the normal image call and the single compressed retry fail.

## Expected
- The GPT clearly states that Image generation could not complete the image.
- It preserves the design specification.
- It may offer explicit prompt export as a next step, but does not claim an image was created.
- It does not create an SVG placeholder.

## Fail
- It silently loops, invents a result or substitutes a diagram.
