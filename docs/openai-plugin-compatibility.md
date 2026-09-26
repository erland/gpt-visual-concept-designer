# OpenAI Plugin – compatibility assessment

Projekt: **Visual Concept Designer**  
GPT Byggaren: **1.5.0**

## Slutsats

OpenAI Plugin bedöms som **reduced**, **advisory-only** och lämnas **inte aktiv**.

Projektets designmetod, knowledge och textbaserade workflow kan representeras som skills/references. Full runtime-parity kan däremot inte garanteras för två kritiska delar av canonical-kontraktet:

1. **Konstnärlig bildgenerering** måste ske med ett faktiskt Image generation-verktyg. Kod, SVG, HTML, Canvas, diagram eller placeholders får inte användas som ersättning.
2. **Långlivat projekt-state** ska utgå från senaste uttryckligen godkända projektpaket/designspecifikation, inte enbart från chatthistorik.

Plugin v1 behandlas därför inte som en fullvärdig peer-runtime för detta projekt.

## Parity-bedömning

| Område | Bedömning |
|---|---|
| Behavior | reduced |
| Capability | reduced |
| Artifact | reduced |
| Workspace/state | reduced |
| Tool | reduced |

### Behavior

Designprocess, mognadstrappa, beslutsregler och handoff kan uttryckas som skills. När processen kräver faktisk bildgenerering uppstår dock en kritisk runtime-skillnad.

### Capability

Kritiska capabilities:
- `image_generation`
- `image_upload_and_analysis`

Pluginen får inte betraktas som equivalent utan en garanterad motsvarighet till projektets bildgenereringskontrakt.

### Artifact

Markdown, YAML, manifests och instruktioner kan hanteras som resurser. Konceptbilder och fullständiga versionsmärkta projektpaket är däremot delar av produktens faktiska leveransflöde och måste kunna skapas/uppdateras utan falska leveranspåståenden.

### Workspace/state

För längre projekt är senaste godkända projektpaket och aktuell designspecifikation auktoritativa. En plugin-implementation får inte falla tillbaka till chatthistorik som enda sanningskälla.

### Tool

Konstnärlig rendering får inte ersättas med lokal kod eller programmatisk grafik. Plugin-specifika scripts skulle endast vara tillåtna för strukturerade filer, manifest, validering och paketering.

## Aktiveringsbeslut

- status: `assessed_not_active`
- compatibility: `reduced`
- advisory_only: `true`
- blocker: `critical_image_generation_not_guaranteed`
- blocker: `persistent_project_state_not_guaranteed`

Ingen Plugin-distribution byggs eller publiceras i denna migrering.

## Framtida omprövning

Plugin kan omprövas om runtime kan uppfylla samma canonical kontrakt för:
1. faktisk Image generation,
2. analys/redigering av verkligt tillgängliga bilder,
3. persistent projekt-state utanför enbart chatthistorik,
4. versionsmärkta projektpaket utan falska filpåståenden,
5. samma failure/retry-policy.

Ingen canonical produktregel ändras av denna bedömning.
