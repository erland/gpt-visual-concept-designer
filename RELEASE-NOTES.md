# Release notes – v1.3.0

Denna version är upload-ready för en anpassad GPT: huvudinstruktionen ligger under 8 000 tecken och knowledge-biblioteket består av exakt 20 filer. Innehållet från de tidigare 24 filerna är bevarat genom fyra ämnesmässiga sammanslagningar. Project Manifest schema v2 fungerar som centralt index för ett växande visuellt konceptprojekt.

# Release Notes – Visual Concept Designer v1.3.0

Version 1.3.0 lägger till **Project Bundle Workflow** för längre kreativa projekt. GPT:n kan nu strukturera textbeskrivningar, konceptspecifikationer, bilder, Style Bible, manifest, changelog och handoff-material i en gemensam versionsmärkt zip.

## Viktigaste nyheterna

- Senaste godkända projekt-zip är auktoritativ källa.
- Bilder får stabila ID:n, status och avgränsade auktoritetsroller.
- Explorativa, godkända, ersatta och saknade bilder skiljs åt.
- Projekt kan importeras, valideras, uppdateras och exporteras som ny version.
- Mallar och scheman ingår för projekt- och bildmanifest.

## Begränsning

GPT:n kan bara paketera bilder och filer som faktiskt är tillgängliga i den aktuella arbetsmiljön. Tidigare chattbilder måste laddas upp igen när de inte längre är åtkomliga.

## Internal Prompt Engine

v1.3.0 tar bort behovet att kopiera en genererad bildprompt tillbaka till GPT:n. Efter designfasen frågar GPT:n om bilden ska skapas och använder därefter bildverktyget direkt. Prompten är intern och härleds från designspecifikationen. Den visas endast på uttrycklig begäran.
