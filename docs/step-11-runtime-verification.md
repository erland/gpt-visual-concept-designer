# Runtimeverifiering efter migrering till GPT Byggaren 1.6.33

## Automatiskt verifierbart
GitHub Actions kör nu `tests/verify_image_workflow_contract.py` separat före distributionsbygget. Testet kontrollerar ursprunglig instruktion (byte-identitet) och bildarbetsflödets centrala regler. Detta är ett **statiskt kontraktstest**, inte en bildgenereringskörning. CI bygger och validerar dessutom de fem distributionerna.

## Test i riktig värdmiljö
Kör scenarierna i `tests/image-workflow-e2e-scenarios.md` och fyll i runtime-matrisen utifrån observationer. Värdmiljön måste ha den aktuella distributionen installerad och relevant bildverktyg aktiverat. Notera exempelvis datum, version, använd prompt, bilder, faktisk respons, PASS/FAIL/BLOCKED och eventuell artefakt-ID.

Första prioritet:
1. **ChatGPT Chat:** E2E-01 (konceptidé), E2E-02 (faktisk bildgenerering), E2E-03 (uppladdad skiss), E2E-04 (iterativ bildändring).
2. **OpenAI Plugin:** samma tester där bildverktyg och filinmatning finns tillgängliga. Markera annars BLOCKED med orsak, aldrig PASS.
3. **Claude Projects, Claude Skills och OpenCode:** kör endast flöden som den aktuella värden kan utföra. Dokumentera verkliga capability-gap utan att ersätta konstnärlig bildgenerering med SVG eller kod.

## Releasestatus
Ingen funktionell bildtestkörning har ännu dokumenterats. `release_ready: false` gäller tills runtimebevis och nödvändiga releasekontroller föreligger. En grön CI-körning är **inte** bevis för full runtimeparitet.

## Nästa manuella moment
För bild-E2E krävs att en testare aktiverar/installera distributionen i den valda värden och kör scenerna. GitHub Actions saknar åtkomst till den interaktiva bildgeneratorns faktiska användarsession.
