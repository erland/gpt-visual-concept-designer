# Testpaket

Testpaketet verifierar Visual Concept Designer som **guidande designpartner**, inte enbart som bildgenerator. Testerna bedömer dialog, val av arbetsläge, designresonemang, bildmognad, konsekvens och handoff.

## Körning

1. Konfigurera GPT:n enligt `gpt/capabilities-and-settings.md`.
2. Starta en ny konversation per testfall.
3. Använd testets startprompt och följ dess angivna användarrepliker.
4. Spara svar, skapade bilder och eventuella artefakter.
5. Bedöm med `assessment-rubric.md` och testets egna förväntningar.
6. Registrera utfallet i en kopia av `test-run-template.md`.

Testerna är huvudsakligen manuella eftersom flera centrala egenskaper gäller samtalskvalitet och visuell bedömning. Manifestet kan användas av ett framtida testverktyg.

## Resultatnivåer

- **PASS:** Inga kritiska fel, samtliga must-kriterier uppfyllda och tillräcklig totalpoäng.
- **PASS WITH NOTES:** Inga kritiska fel och alla must-kriterier uppfyllda, men mindre förbättringar finns.
- **FAIL:** Minst ett kritiskt fel, ett missat must-kriterium eller för låg totalpoäng.
- **BLOCKED:** Testet kan inte slutföras på grund av verktygs- eller miljöbegränsning.
