# T28 — Prompt Compiler compression

## Scenario
A long character project contains manifests, version history, rejected alternatives and extensive decisions. The user approves generation.

## Expected
- The GPT compiles a short image brief from only image-relevant facts.
- It excludes manifests, file paths, history, rejected options and unrelated metadata.
- The brief has one primary validation goal and is normally below about 600 words.
- It calls Image generation directly without exposing the brief.

## Fail
- The full project specification or YAML dump is sent as the image prompt.
- The user is asked to paste the prompt manually.
