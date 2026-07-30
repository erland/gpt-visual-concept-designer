# Pass/fail-kriterier

## Obligatoriskt för hela testsviten

- GPT:n kan guida en nybörjare från vag idé till en tydlig brief.
- En erfaren användare med tydlig brief kan få ett snabbspår utan överdriven intervju.
- “Jag vet inte” möts med valbara, begripliga rekommendationer.
- Exploration, refinement, locked design och production reference hålls isär.
- Motivspecifika frågor används för karaktär, miljö, byggnad, fordon, prop och varelse.
- Historisk korrekthet hanteras som vald nivå, inte som automatisk dogm.
- Fantasy och science fiction behandlas som system med konsekvenser, inte endast ytestetik.
- Bildgenerering har ett uttalat valideringssyfte.
- En uppladdad skiss analyseras före förändring och dess kärnidentitet kan bevaras.
- Låsta koncept kan överlämnas i ett användbart handoff-format.

## Svittens releasekrav

För release candidate krävs:

- 100 % PASS eller PASS WITH NOTES på critical-path-tester.
- Minst 85 % PASS eller PASS WITH NOTES totalt.
- Inga öppna kritiska fel.
- Alla återkommande fel har en identifierad rotorsak.
- Regressionstest finns för varje korrigerat kritiskt eller större fel.
