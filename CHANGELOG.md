# Changelog

## 1.3.0

- Konsoliderade knowledge-biblioteket från 24 till exakt 20 uppladdningsbara filer utan att ta bort ämnesinnehåll.
- Slog ihop karaktär + roller, fordon + props, visuellt berättande + färg/ljus/material samt spel + serier.
- Införde Project Manifest schema v2 som centralt index för koncept, relationer, auktoritativa referenser, Style Bibles och handoff-status.
- Lade till arbetsflödesguide för manifest-synkronisering och auktoritetsregler.
- Uppdaterade validering och dokumentation för GPT:s 20-filsgräns.

## 1.3.0 – Project Bundle Workflow

- Lagt till versionsmärkta projekt-zippar som auktoritativ källa.
- Lagt till projekt-, koncept- och bildmanifest.
- Lagt till bildstatus, auktoritetsroller och regler för ersatta eller saknade bilder.
- Lagt till mallar och JSON Schema-baserade YAML-scheman.
- Uppdaterat GPT-instruktion, capabilities, usage och handoff-kunskap.
- Lagt till fyra tester för projektpaket och bildauktoritet.

## 1.0.0 – 2026-07-30

### Added

- installations- och användarguide,
- slutlig definition of done,
- tre kompletta end-to-end-exempelprojekt,
- preflight-rapport och release notes,
- slutlig releasevaliderare.

### Changed

- version och knowledge-manifest synkroniserade till 1.0.0,
- README uppdaterad för stabil release,
- releasepaketet rensat från mellanversionsvalideringar.

### Validation

- huvudinstruktion under 8 000 tecken,
- 24 kompletta knowledge-filer,
- 18 strukturellt giltiga testfall,
- tre kompletta exempelprojekt,
- zip-integritet verifierad.

# Ändringshistorik

## 0.13.0-rc1 – [PLAN2] Prompt 13

- Genomförde en specifikationsbaserad torrkörning av samtliga 18 testfall.
- Dokumenterade fem rotorsaker och kvarstående empiriska verifieringsbehov.
- Förtydligade direkt bildbegäran kontra guidad designprocess.
- Lade till obligatorisk tillgänglighetskontroll för skisser och bilder.
- Begränsade normal frågemängd till högst tre frågor åt gången.
- Lade till beslutslogg för bekräftat, rekommenderat och öppet.
- Förtydligade att rekommenderade designlås inte får presenteras som användarbekräftade.
- Uppdaterade testmanifest, README, version och validering.

## 0.12.0 – [PLAN2] Prompt 12

- Lade till ett systematiskt testpaket med 18 testfall.
- Markerade åtta testfall som critical path.
- Lade till bedömningsmatris med tio dimensioner och poängtrösklar.
- Definierade kritiska fel, pass/fail-regler och releasekrav.
- Lade till mall för manuella testkörningar och rotorsaksanalys.
- Täckte nybörjar- och expertflöden, motivtyper, historia, fantasy, science fiction, skissläge, bildmognad, referensark, konsekvens, medieanpassning och produktionshandoff.
- Uppdaterade README, version och projektstatus.

## 0.11.0 – [PLAN2] Prompt 11

- Lade till färdig huvudinstruktion för GPT-konfigurationen.
- Definierade namn, kort och längre beskrivning samt produktpositionering.
- Lade till primära conversation starters och alternativa kandidater.
- Dokumenterade rekommenderade capabilities och konfigurationsordning.
- Lade till välkomsttext.
- Kontrollerade att huvudinstruktionen är kompakt och att detaljkunskap fortsatt ligger i knowledge-filerna.
- Uppdaterade README, version och projektstatus.

# Changelog

## 0.10.0 – Prompt 10: Skissläge, designlåsning och handoff

### Added

- Fullständig knowledge-fil för Style Bible och konsekvens.
- Fullständig knowledge-fil för skissanalys och förädling.
- Fullständig knowledge-fil för konceptöverlämning.
- Bevarandeplan som skiljer observation, tolkning och oklarhet.
- Designstatus, fasta egenskaper, tillåten variation och förbjudna förändringar.
- Konsekvensankare, avvikelseklassificering och versionshantering.
- Människo- och maskinläsbart handoff-format.
- Auktoritetsroller för referensbilder.
- `workflow/sketch-lock-handoff-workflow.md`.
- Style Bible-, skissanalys-, handoff- och konsekvensmallar.
- `schemas/concept-spec.schema.yaml`.
- Exempel på låst karaktär, miljö och fordon.

### Changed

- K15, K19 och K20 ändrade från `skeleton` till `complete`.
- Knowledge-manifestet uppdaterat till version 0.10.0 och status `complete`.
- README och versionsinformation uppdaterade för Prompt 10.

## 0.9.0 – Prompt 9: Medieanpassning och bildpipeline

- Färdigställde K13–K14 och K16–K18.
- Lade till mediespecifika regler för spel, serier och animation.
- Lade till pitch art och presentationsprinciper.
- Ersatte den preliminära bildpolicyn med en fullständig policy.
- Lade till `workflow/visual-maturity-pipeline.md`.
- Lade till `templates/reference-sheet-brief.md`.
- Uppdaterade knowledge-manifestet till 21 kompletta filer.

## 0.8.0 – Prompt 8: Fantasy och science fiction

### Added
- Fullständig knowledge-fil för fantasydesign.
- Fullständig knowledge-fil för science fiction och framtidsdesign.
- Praktiskt stöd för magisystem, genrelogik, tekniklivscykler och samhällskonsekvenser.
- `templates/fantasy-logic-checklist.md`.
- `templates/future-technology-logic-checklist.md`.
- `templates/fantasy-scifi-genre-matrix.md`.

### Changed
- K11 och K12 markerade som `complete`.
- Knowledge-bibliotekets version höjd till 0.8.0.

## 0.7.0 – Prompt 7: Historia och materiell kultur

### Added

- Fullständig knowledge-fil för historiska perioder.
- Tre nivåer för historisk korrekthet.
- Fullständig knowledge-fil för materiell kultur och teknik.
- Periodmatris, historisk konsekvenschecklista och riktlinjer för kulturella influenser.
- Stöd för materialflöden, energi, tillverkning, transport, underhåll och återbruk.

### Changed

- Knowledge-manifest uppdaterat till 0.7.0.
- K09 och K10 markerade som complete.

Alla betydande förändringar i projektet dokumenteras här.

## [0.6.0] – 2026-07-30

### Added

- Fullständig knowledge-fil för miljö- och världsdesign.
- World logic-modell för funktion, klimat, resurser, system, samhälle och synliga konsekvenser.
- Stöd för miljöskalor från region till enskild scen.
- Metoder för miljöberättande och historiska lager.
- Fullständig knowledge-fil för arkitektur och scenografi.
- Beslutsstöd för funktion, konstruktion, flöden, zoner, skala, exteriörer och interiörer.
- Utökade miljö- och arkitekturbriefar.
- Ny `world-logic-checklist.md`.

### Changed

- K06 och K07 ändrade från `skeleton` till `complete`.
- `knowledge-manifest.yaml` uppdaterat till biblioteksversion 0.6.0.
- README och versionsinformation uppdaterade för Prompt 6.

### Status

Genomför [PLAN2] Prompt 6 – Miljö och arkitektur.

## 0.5.0 – Knowledge-arkitektur

- Skapade `knowledge/` som separat domänlager.
- Definierade ursprungligen 24 knowledge-filer med unika ansvarsområden; v1.3.0 konsoliderar dem till 20 uppladdningsbara filer.
- Lade till `knowledge-manifest.yaml` med ID, status, ägarprompt, ämnen och relationer.
- Lade till gemensam dokumentstandard för metadata, rubriker och skrivregler.
- Lade till routing-, ägarskaps- och konfliktprioritetsregler.
- Skapade filskal för Prompt 5–10 utan att föregripa det fullständiga innehållet.
- Uppdaterade README och versionsnummer till 0.5.0.

Alla betydande förändringar i projektet dokumenteras här.

## [0.3.0] – 2026-07-30

### Added

- Sju motivmodeller för karaktärer, varelser, miljöer, byggnader, fordon/farkoster, vapen och props.
- Motivspecifika designmål, frågor, risker och rekommenderade leveranser.
- Regler för uppdrag som kombinerar flera motiv.
- Nitton definierade leveranstyper från textbrief och silhouette exploration till production reference pack och handoff.
- Matris som kopplar motivtyper till exploration, refinement, presentation och produktionsreferenser.
- Rekommenderad arbetsordning per motivtyp.
- Briefmallar för koncept, karaktär, varelse, miljö, arkitektur, fordon/farkost och prop.
- Mediumjustering för spel, serier, animation och pitch på modellnivå.

### Changed

- README uppdaterad med motivtyper, leveranstyper och ny projektstruktur.
- Projektstatus uppdaterad till genomförd [PLAN2] Prompt 3.

### Status

Genomför [PLAN2] Prompt 3 – Motiv- och leveransmodeller.

## [0.2.0] – 2026-07-30

### Added

- Åtta definierade arbetslägen från Guided Discovery till Consistency Follow-up.
- Regler för automatiskt val och växling av arbetsläge.
- Fullständigt flexibelt standardarbetsflöde från orientering till handoff.
- Mermaid-flödesschema för konceptprocessen.
- Full guidning, samarbetsläge och direktläge för olika användarbehov.
- Snabbspår för tydliga briefar, låsta koncept och skissbaserad förädling.
- Vägledning för hur GPT:n rekommenderar nästa steg i varje fas.
- Preliminär bildgenereringspolicy och fyra mognadsnivåer för bilder.
- Regler för återgång när grunddesignen eller briefen visar sig vara fel.

### Changed

- README uppdaterad med arbetslägen, standardprocess och ny projektstruktur.
- Projektstatus uppdaterad till genomförd [PLAN2] Prompt 2.

### Status

Genomför [PLAN2] Prompt 2 – Arbetslägen och standardprocess.

## [0.1.0] – 2026-07-30

### Added

- Grundläggande produktdefinition för Visual Concept Designer.
- Definition av primära och sekundära målgrupper.
- Omfattning och avgränsning mot Game Graphics Creator och Game Designer & Developer.
- Tjugo vägledande designprinciper.
- Preliminär definition av färdig version 1.0.
- Grundläggande projektstruktur och versionsfil.

### Status

Genomför [PLAN2] Prompt 1 – Produktdefinition och arkitektur.

## [0.5.0] - 2026-07-30

### Added

- Fullständig kunskapsfil för visuella designgrunder.
- Guidningsprinciper för nybörjare, delad guidning och expertläge.
- Karaktärsdesign med silhuett, proportion, rörelse och identitet.
- Beslutsstöd för berättelseroller, praktiska roller och arketyper.
- Funktionell design av kläder, rustningar och utrustning.
- Ekologiskt och beteendemässigt grundad varelse- och monsterdesign.
- Funktions-, energi- och underhållsbaserad fordons- och farkostdesign.
- Ergonomisk och narrativ design av vapen, verktyg och props.
- Frågebanker, fallgropar och kvalitetskontroller i samtliga nya kunskapsfiler.

### Changed

- `knowledge-manifest.yaml` uppdaterat till version 0.5.0 och status `partially-populated`.
- K01–K05, K08 och K08 ändrade från `skeleton` till `complete`.
- README och versionsinformation uppdaterade för Prompt 5.

## 1.3.0

- Inför intern promptmotor där designspecifikationen är sanningskälla.
- Bildprompt visas endast vid uttrycklig export.
- Efter accepterad riktning frågar GPT:n om bilden ska skapas och anropar sedan bildverktyget direkt.
- Lägger till readiness-kontroll, resultatkontroll och prompt-exportregler.
- Lägger till tre testfall för direkt generering, prompt-export och specifikationsauktoritet.
