# Project Bundle Workflow

## Syfte

Ett längre konceptprojekt ska kunna bevara både textuella beslut och bildmaterial i ett versionsmärkt, portabelt projektpaket. Paketet gör projektets aktuella tillstånd oberoende av en enskild konversation.

## Auktoritativ källa

- Den senaste uttryckligen godkända projekt-zippen är projektets auktoritativa källa.
- En ny chatt ska utgå från den senaste zippen eller ett komplett motsvarande projektunderlag.
- Äldre zippar och bilder får inte antas vara aktuella när en nyare version finns.
- GPT:n ska aldrig påstå att en fil eller bild ingår i paketet utan att den faktiskt har kunnat läsa eller skriva filen.
- Saknas en tidigare bild i tillgängligt material ska GPT:n be användaren ladda upp den eller markera den som saknad i manifestet.

## Standardstruktur

```text
concept-project/
├── README.md
├── project.yaml
├── CHANGELOG.md
├── concepts/
│   ├── characters/
│   ├── creatures/
│   ├── environments/
│   ├── architecture/
│   ├── vehicles/
│   └── props/
├── world/
│   ├── style-bible.md
│   ├── palette.yaml
│   └── world-notes.md
├── references/
│   ├── user-sketches/
│   ├── mood/
│   └── external/
├── handoff/
├── manifests/
│   ├── concepts.yaml
│   └── images.yaml
└── archive/
    └── deprecated/
```

Varje koncept får en egen mapp med stabilt `concept_id`:

```text
concepts/characters/chr-example-001/
├── concept.md
├── concept-spec.yaml
├── decisions.md
├── style-rules.md
└── images/
    ├── exploration/
    ├── approved/
    ├── reference/
    └── deprecated/
```

## Projektlivscykel

### 1. Starta projekt

Skapa projekt-ID, titel, medium, status, versionsnummer och katalogstruktur. Skapa tomma koncept- och bildmanifest.

### 2. Importera befintligt projekt

- Packa upp senaste zippen.
- Läs `project.yaml`, manifest och changelog först.
- Kontrollera att refererade filer finns.
- Rapportera saknade eller dubbla filer innan större ändringar.
- Ändra aldrig originalzippen; skapa en ny projektversion.

### 3. Lägg till eller uppdatera koncept

- Skapa eller återanvänd stabilt koncept-ID.
- Uppdatera textbeskrivning, specifikation och beslutslogg.
- Lägg bilder i rätt statusmapp.
- Uppdatera båda manifesten och changelog.

### 4. Godkänn referenser

En bild får bara bli auktoritativ efter uttryckligt användargodkännande. Ange exakt vad den styr, exempelvis silhuett, färg, material, proportion eller stämning.

### 5. Exportera ny zip

- Höj projektversionen.
- Kör manifest- och filkontroll.
- Flytta ersatta filer till `deprecated/` eller markera dem som ersatta.
- Skapa en komplett ny zip.
- Sammanfatta ändringarna och länka den nya filen.

## Bildstatus och roller

Status:

- `exploration` – tidig variant; får förändras.
- `candidate` – möjlig riktning som utvärderas.
- `approved` – godkänd för angiven roll.
- `deprecated` – ersatt och får inte användas som aktuell referens.
- `missing` – refererad men inte tillgänglig i paketet.

Roller:

- `authoritative_design_reference`
- `authoritative_color_reference`
- `authoritative_material_reference`
- `authoritative_proportion_reference`
- `mood_reference`
- `composition_reference`
- `exploration_only`

En bild kan ha flera roller, men dess auktoritet ska vara avgränsad med `defines` och `must_not_define`.

## Filnamn

Rekommenderat format:

```text
<concept-id>__<stage>__<view-or-purpose>__v<revision>.<ext>
```

Exempel:

```text
chr-keeper-001__rough__silhouette-a__v01.png
chr-keeper-001__reference__front__v03.png
env-harbor-001__hero__storm-night__v02.png
```

## Versionsregler

- Projektversion beskriver hela paketet.
- Konceptversion beskriver ett enskilt motiv.
- Bildrevision beskriver en specifik bildfil.
- Bumpa patch för dokumentation och mindre tillägg.
- Bumpa minor när nya koncept, leveranstyper eller större designbeslut tillkommer.
- Bumpa major när låsta identitetsdrag bryts avsiktligt.

## Kommandon som ska förstås

- Starta ett nytt concept project.
- Importera denna projekt-zip och sammanfatta nuläget.
- Lägg till detta som ett nytt koncept.
- Spara bilden som explorativ referens.
- Markera bilden som auktoritativ för silhuetten.
- Ersätt tidigare färgreferens men behåll den som deprecated.
- Lås konceptversion 1.0.
- Skapa handoff för Game Graphics Creator.
- Ge mig en uppdaterad projekt-zip.

## Minsta export

En giltig projekt-zip måste minst innehålla:

- `README.md`
- `project.yaml`
- `CHANGELOG.md`
- `manifests/concepts.yaml`
- `manifests/images.yaml`
- minst en konceptmapp eller en tydlig tom projektstatus

## Kvalitetskontroll

Före export ska GPT:n kontrollera:

- att alla manifestposter har unika ID:n,
- att varje filsökväg i manifesten finns eller har status `missing`,
- att deprecated bilder inte är auktoritativa,
- att godkända bilder anger vad de definierar,
- att låsta koncept har fasta och fria egenskaper,
- att changelog beskriver ändringarna,
- att zippen innehåller hela projektroten och inte bara lösa filer.
