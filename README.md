# Visual Concept Designer

**Version:** 1.0.0  
**Status:** Aktiv GPT-konfiguration  

Visual Concept Designer är en guidande visuell designpartner för TV-spel, serietidningar, animation, illustration, brädspel och pitchmaterial. GPT:n hjälper både nybörjare och erfarna kreatörer att gå från vag idé eller befintlig skiss till ett sammanhängande visuellt koncept och ett användbart produktionsunderlag.

## Kärnbeteende

- börjar normalt i text och hjälper användaren precisera avsikten,
- ställer högst tre frågor åt gången som normalregel,
- ger konkreta alternativ när användaren inte vet vad den vill,
- använder rough exploration före hög detaljnivå när riktningen är osäker,
- skiljer tydligt mellan exploration, refinement, locked design och production reference,
- kan arbeta från uppladdad skiss utan att ersätta kärnidén,
- dokumenterar bekräftade beslut, öppna frågor och rekommendationer,
- skapar handoff till mänskliga kreatörer eller specialiserade GPT:er.

## Projektstruktur

- `product/` – mål, avgränsning, designprinciper och definition of done.
- `workflow/` – arbetslägen, process, bildpolicy och skiss/lås/handoff-flöde.
- `models/` – motivmodeller och leveranstyper.
- `templates/` – briefar, Style Bible, skissanalys och kvalitetskontroller.
- `schemas/` – maskinläsbar konceptspecifikation.
- `knowledge/` – 20 aktuella knowledge-filer.
- `gpt/` – huvudinstruktion, namn, beskrivning, starters och inställningar.
- `tests/` – aktuella regressionstest, bedömningsmatris och validering.
- `examples/` – aktuella exempelprojekt och låsta konceptspecifikationer.
- `release/` – aktuell validerare för projektpaket.

## Installera GPT:n

Följ `INSTALLATION.md`. Börja med att kopiera `gpt/gpt-instructions.md` till GPT:ns instruktioner och ladda därefter upp knowledge-filerna enligt `knowledge/knowledge-manifest.yaml`.

## Användning

Se `USAGE.md` för nybörjarflöde, expertsnabbspår, skissläge, designlåsning och handoff.

## Kvalitetssäkring

- 20 av 20 Knowledge-filer är definierade i manifestet.
- Huvudinstruktionen valideras mot plattformens teckengräns.
- Regressionstester och paketvaliderare finns kvar som aktuella QA-verktyg.
- Historiska testresultat, preflight-rapporter, changelog och äldre release notes finns i Git-historiken och lagras inte längre i working tree.

## Project Bundle Workflow (v1.1)

GPT:n kan skapa och uppdatera versionsmärkta projekt-zippar som samlar konceptbeskrivningar, specifikationer, Style Bible, bilder, bildroller, manifest, changelog och handoff-material. Senaste godkända projekt-zip används som auktoritativ källa vid fortsatt arbete. Se `workflow/project-bundle-workflow.md`.

## Bildflöde i v1.4.0

Designspecifikationen är projektets sanningskälla. När en riktning är klar frågar GPT:n om den ska skapa bilden och genererar den direkt. Bildprompten byggs internt och visas bara om användaren ber om prompt-export.


## Bildgenerering i v1.4.0

Bildprompter kompileras internt från designspecifikationen. Endast bildrelevanta uppgifter skickas till Image generation. Vid fel görs ett enda omförsök med en minimal brief.


## Distributionspaket

Repositoryt kan bygga två distributionsformat från samma aktuella GPT-konfiguration:

- `visual-concept-designer-custom-gpt-vX.Y.Z.zip` för installation/uppdatering av Custom GPT.
- `visual-concept-designer-chat-vX.Y.Z.zip` för att bifogas direkt i en vanlig ChatGPT-konversation.

Kör lokalt:

```bash
python3 scripts/build_distributions.py
python3 scripts/validate_distributions.py
```

Vanliga byggen använder `VERSION`. Vid en publicerad GitHub Release används release-taggen som versionskälla. En release `v1.1.0` producerar alltså automatiskt båda `...v1.1.0.zip` och bifogar dem till releasen.

Custom GPT-paketets huvudinstruktion, conversation starters och 20 numrerade Knowledge-filer kopieras utan innehållsförändring från de kanoniska källorna.
