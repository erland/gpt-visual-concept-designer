# Release Notes – Visual Concept Designer v1.3.1

Denna korrigeringsversion skärper verktygsvalet för bildgenerering. Konstnärliga bilder ska alltid skapas med ChatGPTs Image generation. Code Interpreter får fortfarande användas för projekt-zippar och strukturerade filer, men aldrig för att skapa SVG-liknande konceptbilder eller placeholders.

## Konfiguration

- Aktivera **Image generation**.
- Aktivera **Code Interpreter & Data Analysis** för projektpaket.
- Sätt **GPT-5.6** som rekommenderad modell om den finns; annars välj den starkaste allmänna bildkapabla modellen.
- Canvas behövs inte.

## Validering

Releasepaketet verifierar instruktionens teckenlängd, 20 knowledge-filer, testmanifest och zip-integritet.
