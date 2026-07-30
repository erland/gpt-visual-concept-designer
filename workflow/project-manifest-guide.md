# Centralt Project Manifest

`project.yaml` är projektpaketets navigationsindex. Det ersätter inte detaljmanifesten utan pekar ut vad som är aktivt och auktoritativt.

Det ska hålla ihop:

- projektidentitet och paketversion,
- alla aktiva eller historiska koncept,
- relationer mellan karaktärer, miljöer, props och andra motiv,
- auktoritativa bilder per visuell roll,
- Style Bibles och beslutsloggar,
- status och mål för produktionshandoff.

## Uppdateringsregel

Vid varje projektändring ska GPT:n uppdatera berörda detaljfiler först och därefter synkronisera `project.yaml`. Ett koncept eller en bild får inte markeras som godkänt eller auktoritativt utan ett uttryckligt användarbeslut. Den senast exporterade projekt-zippen är auktoritativ källa.

## Navigeringsregel

Börja med `project.yaml`, följ sedan sökvägarna till koncept- och bildmanifest. Läs endast de detaljfiler som behövs för aktuell uppgift.
