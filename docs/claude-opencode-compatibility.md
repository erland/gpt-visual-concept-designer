# Claude Projects och OpenCode – runtime compatibility

Projekt: **Visual Concept Designer**  
GPT Byggaren: **1.5.0**

## Slutsats

Både Claude Projects och OpenCode bedöms som **reduced** och lämnas **inte aktiva** i denna migrering.

Skälet är inte textinstruktioner eller Knowledge-material; de kan representeras i båda miljöerna. Blockeraren är projektets kritiska capability-kontrakt: konstnärliga bilder ska skapas genom ett faktiskt bildgenereringsverktyg, och kod/SVG/HTML/Canvas/diagram får uttryckligen inte användas som ersättning.

Att paketera projektet för en runtime utan garanterad motsvarande Image generation skulle därför ge skenbar distribution-parity men ändra produktens kärnbeteende.

## Parity-bedömning

| Område | Claude Projects | OpenCode |
|---|---|---|
| Behavior | reduced | reduced |
| Capability | reduced | reduced |
| Artifact | reduced | reduced |
| Workspace/state | equivalent | equivalent |
| Tool | reduced | reduced |

### Behavior

Instruktion, designprocess, designspecifikation, sketch-preservation och handoff kan representeras. Men den direkta regeln att skapa konstnärlig bild när arbetsflödet kräver det kan inte behandlas som equivalent utan ett runtimeverktyg med motsvarande funktion.

### Capability

Kritiska capabilities enligt `gpt-builder-1.5-contract.yaml`:

- `image_generation`
- `image_upload_and_analysis`

Bildanalys kan vara möjlig beroende på runtime, men den konstnärliga bildgenereringen är blockerande för full parity.

### Artifact

Textartefakter, YAML, Markdown, manifest och projektpaket kan representeras. Genererad konceptkonst är däremot en obligatorisk artefakttyp i relevanta flöden och får inte ersättas programmässigt.

### Workspace/state

Båda runtime-kandidaterna kan i princip arbeta med filer/projektstruktur på ett sätt som passar projektets state-kontrakt. Detta räcker dock inte för aktivering när en kritisk capability saknar garanterad parity.

### Tool

Projektet kräver ett konstnärligt bildgenereringsverktyg. Kodverktyg får endast användas för manifest, validering, filer och zip-paket.

## Aktiveringsbeslut

### Claude Projects

- compatibility: `reduced`
- activation: `not_active`
- blocker: `critical_image_generation_not_guaranteed`

### OpenCode

- compatibility: `reduced`
- activation: `not_active`
- blocker: `critical_image_generation_not_guaranteed`

## Framtida omprövning

En runtime kan aktiveras senare om den kan uppfylla samma kritiska kontrakt:
1. faktisk konstnärlig bildgenerering,
2. ingen programmatisk ersättningsbild,
3. bildanalys/redigering mot faktisk tillgänglig bild,
4. bevarad designspecifikation som source of truth,
5. samma failure/retry-policy.

Ingen canonical produktregel ändras av denna bedömning.
