#!/usr/bin/env python3
from pathlib import Path
import re
import yaml

ROOT = Path(__file__).resolve().parents[1]

def main() -> int:
    errors = []
    contract = yaml.safe_load((ROOT / "gpt-builder-1.5-contract.yaml").read_text(encoding="utf-8"))
    project = yaml.safe_load((ROOT / "gpt-project.yaml").read_text(encoding="utf-8"))
    canonical = (ROOT / project["instructions"]["canonical"]).read_bytes()
    legacy = (ROOT / project["instructions"]["legacy_source"]).read_bytes()
    instruction_text = canonical.decode("utf-8")
    version = (ROOT / "VERSION").read_text(encoding="utf-8").strip()
    manifest = (ROOT / "knowledge/knowledge-manifest.yaml").read_text(encoding="utf-8")
    knowledge_files = re.findall(r"^\s*file:\s*(.+?)\s*$", manifest, flags=re.M)

    if contract["builder"]["target_version"] != "1.5.0":
        errors.append("target builder version must be 1.5.0")
    if contract["builder"]["behavior_preserving"] is not True:
        errors.append("migration must remain behavior-preserving")
    if canonical != legacy:
        errors.append("canonical and legacy instruction must remain byte-identical during migration")
    if version != "1.0.0":
        errors.append(f"VERSION changed during migration: {version!r}")
    if len(knowledge_files) != 20:
        errors.append(f"knowledge manifest must contain exactly 20 files, found {len(knowledge_files)}")
    for name in knowledge_files:
        if not (ROOT / "knowledge" / name).is_file():
            errors.append(f"knowledge file missing: {name}")

    required_markers = [
        "Anropa sedan alltid **Image generation**",
        "Använd aldrig Code Interpreter, Python, SVG, HTML, Canvas, diagram eller programmatisk filgenerering som ersättning för konstnärliga bilder.",
        "Designspecifikationen är sanningskällan",
        "Analysera eller ändra bara en bild som finns i konversationen.",
        "Lås endast efter användarens bekräftelse.",
    ]
    for marker in required_markers:
        if marker not in instruction_text:
            errors.append(f"canonical instruction missing critical behavior marker: {marker}")

    behavior = contract["behavior"]
    if behavior["image_generation_required_for_artistic_images"] is not True:
        errors.append("artistic image generation must require Image generation")
    if behavior["programmatic_art_substitute_allowed"] is not False:
        errors.append("programmatic art substitutes must remain forbidden")
    if behavior["missing_image_may_be_invented"] is not False:
        errors.append("missing image target must never be invented")
    if behavior["design_specification_is_source_of_truth"] is not True:
        errors.append("design specification must remain source of truth")
    if behavior["old_prompt_may_override_new_specification"] is not False:
        errors.append("old prompt may not override new specification")
    if behavior["locked_design_requires_user_confirmation"] is not True:
        errors.append("design lock must require user confirmation")
    if behavior["retry_policy"]["image_generation_max_retries_after_failure"] != 1:
        errors.append("image generation retry policy must remain exactly one retry")

    artifacts = contract["contracts"]["artifacts"]["required"]
    if artifacts["generated_image"]["generation_tool"] != "image_generation":
        errors.append("generated_image must use image_generation")
    if artifacts["generated_image"]["programmatic_substitute_allowed"] is not False:
        errors.append("generated_image must forbid programmatic substitute")
    if artifacts["project_bundle"]["authority"] != "latest_explicitly_approved_bundle":
        errors.append("project bundle authority changed")
    if artifacts["project_bundle"]["overwrite_original"] is not False:
        errors.append("project bundle must not overwrite original")

    if errors:
        print("GPT BUILDER 1.5 CONTRACT: FAIL")
        for error in errors:
            print("-", error)
        return 1

    print("GPT BUILDER 1.5 CONTRACT: PASS")
    print("Canonical behavior, Image generation routing, 20/20 Knowledge and VERSION 1.0.0 preserved")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
