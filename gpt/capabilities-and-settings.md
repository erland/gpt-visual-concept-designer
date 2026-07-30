# Rekommenderade capabilities och inställningar

## Obligatoriskt

### Bildgenerering

Ska vara aktiverad. GPT:n använder bilder som en del av en stegvis designprocess: exploration, refinement, hero art och reference material.

### Bilduppladdning och bildanalys

Ska kunna ta emot användarens skisser, tidigare konceptbilder, moodboards och referenser. En specifik bild ska analyseras och få en bevarandeplan innan den förändras.

### Knowledge

Ladda upp de 24 filerna i `knowledge/`. Använd även relevanta mallar om filgränsen tillåter det. Huvudinstruktionen innehåller kärnreglerna; knowledge-filerna ger ämnesdjup.

## Rekommenderat

### Webbsökning

Kan aktiveras för historiska, tekniska och kulturella referenser när aktuell eller exakt faktakontroll behövs. GPT:n ska skilja faktaunderlag från kreativ tolkning och inte använda webbsökning som ersättning för användarens designbeslut.

### Dataanalys/kod

Ska vara aktiverad när GPT:n ska skapa, importera, validera eller uppdatera projekt-zippar. Den används för strukturerade konceptspecifikationer, projekt- och bildmanifest, katalogkontroller, versionshantering och nedladdningsbara leveranspaket.

## Inte nödvändigt i första versionen

- externa Actions,
- direkt integration med spelmotor,
- automatisk 3D- eller animationsproduktion,
- teknisk asset-export.

## Rekommenderad språkhantering

- Svara på användarens språk.
- Knowledge-filerna är på svenska, men principerna kan användas även i engelska projekt.
- Bevara etablerade engelska produktionsbegrepp där de är tydligare, exempelvis `turnaround`, `hero art`, `reference sheet` och `Style Bible`, med kort svensk förklaring när det behövs.

## Rekommenderad konfigurationsordning

1. Ange namn och kort beskrivning.
2. Klistra in `gpt-instructions.md` som instruktion.
3. Aktivera bildgenerering och bilduppladdning.
4. Aktivera dataanalys/kod för Project Bundle Workflow.
5. Ladda upp knowledge-filerna enligt manifestet.
6. Lägg in fyra primära conversation starters.
7. Kör testpaketet från Prompt 12 innan release.
