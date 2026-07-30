# Knowledge-bibliotek

Detta bibliotek innehåller kunskapsunderlaget för Visual Concept Designer. I version 0.5.0 är arkitekturen fastställd och varje fil har fått ett avgränsat ansvar. Filerna är ännu inte fullständigt utvecklade; innehållet fylls på i [PLAN2] Prompt 5–10.

## Principer

1. **Ett primärt ansvar per fil.** En fil ska vara den auktoritativa platsen för sitt område.
2. **Hänvisa istället för att duplicera.** När ett angränsande område behövs används korsreferens.
3. **Designstöd framför uppslagsbok.** Materialet ska hjälpa GPT:n att fråga, analysera, rekommendera och förklara konsekvenser.
4. **Principer före kataloger.** Exempel och genretermer får stödja resonemang men ska inte ersätta funktionell designlogik.
5. **Fakta och kreativ tolkning skiljs åt.** Historiska eller tekniska påståenden ska inte blandas ihop med förslag.
6. **Huvudinstruktionen äger beteendet.** Knowledge-filerna stödjer beteendet men får inte ensamma bära kritiska arbetsregler.

## Läsordning

GPT:n ska normalt använda minsta relevanta kombination:

- Börja med en motivfil, exempelvis `03-character-design-and-roles.md`.
- Lägg till mediumfil när slutmediet påverkar designen.
- Lägg till historik-, fantasy- eller framtidsfil endast när premissen kräver det.
- Använd `17`, `18`, `23` och `24` vid referens-, konsekvens-, skiss- och handoffarbete.

## Dokumentstandard

Alla knowledge-filer följer strukturen i `DOCUMENT-STANDARD.md`. `knowledge-manifest.yaml` är den maskinläsbara katalogen och anger ägarskap, status, planerad prompt och relationer.

## Statusvärden

- `skeleton`: ansvar och framtida innehåll är definierat.
- `draft`: användbart första innehåll finns men behöver testas.
- `reviewed`: innehållet har konsistenskontrollerats.
- `stable`: innehållet är testat och godkänt för release.

## Status efter Prompt 5

Filerna K01–K05, K08 och K08 är kompletta. Övriga filer är fortfarande filskal och fylls i under Prompt 6–10.
