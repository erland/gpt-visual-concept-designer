# Rekommenderade capabilities och inställningar

## Obligatoriskt

### Bildgenerering

Måste vara aktiverad. Konstnärliga bilder ska alltid skapas med den inbyggda funktionen Image generation, aldrig med Code Interpreter, SVG, HTML, Canvas eller diagramverktyg.

### Bilduppladdning och bildanalys

Ska kunna ta emot användarens skisser, tidigare konceptbilder, moodboards och referenser. En specifik bild ska analyseras och få en bevarandeplan innan den förändras.

### Knowledge

Ladda upp de 20 numrerade filerna i `knowledge/`. Använd även relevanta mallar om filgränsen tillåter det. Huvudinstruktionen innehåller kärnreglerna; knowledge-filerna ger ämnesdjup.

## Rekommenderat

### Webbsökning

Kan aktiveras för historiska, tekniska och kulturella referenser när aktuell eller exakt faktakontroll behövs. GPT:n ska skilja faktaunderlag från kreativ tolkning och inte använda webbsökning som ersättning för användarens designbeslut.

### Dataanalys/kod

Aktivera för projekt-zippar, strukturerade specifikationer, manifest, validering och filhantering. Den får aldrig användas för att rendera konceptkonst eller ersätta misslyckad bildgenerering med SVG eller diagram.

## Inte nödvändigt i första versionen

- externa Actions,
- direkt integration med spelmotor,
- automatisk 3D- eller animationsproduktion,
- teknisk asset-export.


## Rekommenderad modell

Ange en rekommenderad modell. Välj **GPT-5.6** om den finns i GPT-editorn; annars den starkaste tillgängliga allmänna modellen som stöder Image generation. Undvik att rekommendera en Codex-/kodfokuserad modell för denna GPT. Modellvalet förbättrar följsamheten men ersätter inte capabilityn Image generation, som fortfarande måste vara aktiverad. Användare kan byta modell och ChatGPT kan välja en liknande modell om den rekommenderade saknas.

## Rekommenderad språkhantering

- Svara på användarens språk.
- Knowledge-filerna är på svenska, men principerna kan användas även i engelska projekt.
- Bevara etablerade engelska produktionsbegrepp där de är tydligare, exempelvis `turnaround`, `hero art`, `reference sheet` och `Style Bible`, med kort svensk förklaring när det behövs.

## Rekommenderad konfigurationsordning

1. Ange namn och kort beskrivning.
2. Klistra in `gpt-instructions.md` som instruktion.
3. Aktivera Image generation och bilduppladdning.
4. Aktivera dataanalys/kod endast för Project Bundle Workflow.
5. Välj GPT-5.6 som rekommenderad modell om den finns.
6. Ladda upp knowledge-filerna enligt manifestet.
7. Lägg in fyra primära conversation starters.
8. Kör testpaketet från Prompt 12 innan release.
