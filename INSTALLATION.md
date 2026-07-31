# Installation av Visual Concept Designer

## 1. Skapa GPT:n

Skapa en ny anpassad GPT och använd:

- **Namn och beskrivning:** `gpt/gpt-name-and-description.md`
- **Instruktioner:** `gpt/gpt-instructions.md`
- **Conversation starters:** `gpt/conversation-starters.md`
- **Capabilities:** `gpt/capabilities-and-settings.md`

## 2. Aktivera funktioner

Aktivera bildgenerering. Webbsökning är valfri och bör främst användas när aktuell eller exakt extern fakta behövs. Kodverktyg behövs inte för kärnflödet men kan vara användbart för maskinläsbara leveranser och filpaketering.

## 3. Ladda upp knowledge-filer

Ladda upp filerna i `knowledge/` enligt `knowledge/knowledge-manifest.yaml`. Om plattformen begränsar antalet filer kan närliggande filer kombineras utan att rubrikstrukturen ändras. Prioritera då:

1. K01–K03 och K06 för kärnprocess och grunddesign.
2. Relevant motivfil K04–K08.
3. Relevant värld/genre K09–K12.
4. K13–K15 för presentation, referens och konsekvens.
5. Relevant mediefil K16–K18.
6. K19–K20 för skissläge och handoff.

## 4. Lägg inte in projektfiler som knowledge

Mapparna `tests/`, `examples/`, `templates/` och `product/` är utvecklings- och referensmaterial. De behöver normalt inte laddas upp som GPT-knowledge.

## 5. Kontrollera konfigurationen

Kör minst följande testfall manuellt:

- T01 – vag karaktärsidé,
- T03 – expertsnabbspår,
- T12 – skissbevarande,
- T13 – rough före refined,
- T16 – konsekvens över tid,
- T18 – produktionshandoff.

Dokumentera resultatet med `tests/test-run-template.md`.

## Projekt-zippar

Aktivera Data Analysis/Code Interpreter för att GPT:n ska kunna importera, validera, skapa och exportera versionsmärkta projekt-zippar.


## Bildverktyg

Aktivera både **Image generation** och **Code Interpreter & Data Analysis**. Prompt Compiler ser till att Code Interpreter endast används för projektfiler och zip-paket, medan konstnärliga bilder alltid går till Image generation.
