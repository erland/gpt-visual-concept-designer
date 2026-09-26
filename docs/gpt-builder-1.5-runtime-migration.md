# GPT Byggaren 1.5.0 – migreringsplan

Projekt: **Visual Concept Designer**

## Utgångsläge

Projektet är ett fungerande legacy-GPT-projekt med:
- version **1.0.0**
- canonical-liknande instruktion i `gpt/gpt-instructions.md`
- exakt **20 Knowledge-filer**
- Custom GPT- och Chat ZIP-distribution
- regressionstestmaterial och distributionsvalidering
- kritiskt beroende av **Image generation**
- Project Bundle Workflow för strukturerade filer/zip

Det saknar GPT Byggaren 1.5.0:s canonical projektkontrakt, generiska runtime-kontrakt och deklarativa runtime-registry.

## Preserve-first

Migreringen ska bevara:
- nuvarande kreativa beteende och arbetsflöde
- instruktionens regler för Image generation
- regeln att Code Interpreter inte får ersätta konstnärlig bildgenerering
- sketch-preservation och design-specification-as-source-of-truth
- 20/20 Knowledge-filer
- befintliga tester och exempel
- VERSION `1.0.0`
- nuvarande Chat- och Custom GPT-funktionalitet

`assistant/instructions.md` införs som canonical källa genom byte-identisk kopia av `gpt/gpt-instructions.md`. Legacy-filen behålls under migreringen och får inte divergera.

## Runtime-målbild

### Aktiva baseline-runtimes
1. ChatGPT Chat
2. ChatGPT Custom GPT

### Ska bedömas
- Claude Projects
- OpenCode
- OpenAI Plugin

Eftersom Image generation är en kritisk capability får ingen ytterligare runtime aktiveras som equivalent om den inte kan uppfylla bildgenereringskontraktet utan att ändra produktbeteendet.

## Steg

### 1. Baseline och canonical källa
Inför `gpt-project.yaml`, separat migrationsstatus och canonical `assistant/instructions.md` utan beteendeförändring.

### 2. Normalisera 1.5-kontrakten
Definiera capability-, artifact-, workspace/state- och tool-kontrakt samt maskinell validering.

### 3. Normalisera Chat och Custom GPT
Bygg båda från canonical projektdata, bevara 20 Knowledge-filer och verifiera image-generation-reglerna.

### 4. Bedöm Claude Projects och OpenCode
Gör requirement-parity för behavior, capability, artifact, workspace/state och tool. Aktivera endast runtimes som klarar kritiska krav; annars dokumentera reduced/not active.

### 5. Bedöm OpenAI Plugin
Avgör om skills-first-plugin kan bevara det kritiska bildflödet och projektpaketshanteringen utan runtime-specifika specialregler.

### 6. Generalisera build, parity, CI och release
Inför deklarativ runtime-registry som source of truth för byggmål och release-artifacts.

### 7. Slutlig readiness och dokumentationssynk
Synka README/INSTALLATION/USAGE/status, kör final hygiene och lägg explicit 7/7-migrationsgate.

## Klart-kriterium

Migreringen är klar när:
- canonical beteende är bevarat,
- 20/20 Knowledge är bevarade,
- Chat och Custom GPT valideras från samma canonical källa,
- övriga runtimes har explicit compatibilitybeslut,
- build/CI/release inte har dolda hårdkodade runtime-antaganden,
- VERSION fortfarande är `1.0.0`,
- slutlig CI är grön.
