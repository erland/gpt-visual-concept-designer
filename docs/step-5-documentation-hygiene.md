# Steg 5 – dokumentation och filhygien (2026-10-31)

## Genomfört

- README:s tidigare påstående om aktiv Custom GPT-distribution ersatt av fem
  faktiskt byggda peer-runtimes och modular_skills som aktiv instruktion.
- Installationstext uppdaterad för 1.6.33. Historiskt installationsmaterial
  kan fortfarande beskriva Custom GPT och ska inte användas som releaseinstruktion.
- PROJECT.md, STATUS.md, utvecklingsplan, checklista och verifieringsrapport
  harmoniserade med utfall i steg 3 och 4.
- GitHub Actions tar inte längre 1.5-monolitvalidatorn som obligatorisk gate,
  installerar PyYAML och anropar 1.6.33-byggaren med korrekt CLI.

## Historiska filer som medvetet behålls

- `assistant/instructions.md`, `gpt/gpt-instructions.md` och
  `gpt-builder-1.5-contract.yaml`: käll- och migrationsspårbarhet.
- `runtime-distribution-registry.yaml`, `migration-status-1.5.yaml` och
  `docs/gpt-builder-1.5-runtime-migration.md`: äldre beslut och adapterlogik.
- `scripts/validate_gpt_builder_1_5_*.py` och övriga 1.5-validatorer:
  potentiellt projektspecifika kontroller; ingen säker funktionsmässig
  ersättning bevisad. Ingen radering utförd.

## Återstående risker

- Bildskapande, analys och state-paritet är ej hostverifierade.
- CI-ändring behöver verifieras genom en faktisk GitHub Actions-körning.
- Versionspinning vid framtida motoruppdatering måste kontrolleras;
  projektets befintliga skript är den installerade 1.6.33-motorns kopior.
- Full release-gate behöver utföras separat.
