---
id: K13
title: Style Bible och konsekvens
status: complete
owner_prompt: 10
primary_topics:
- all
related:
- K14
- K19
- K20
---
# Style Bible och konsekvens

## Syfte

Denna fil hjälper GPT:n att omvandla ett godkänt visuellt koncept till en tydlig uppsättning regler som kan bevaras mellan bilder, scener, medier och produktionssteg. Målet är inte att frysa all kreativitet utan att skilja identitet från tillåten variation.

## Kärnprincip: identitet före detalj

En konsekvent design känns igen även när pose, kamera, ljus, ålder eller situation förändras. GPT:n ska därför rangordna egenskaper efter hur viktiga de är för igenkänning:

1. **Identitetsbärande** – får inte ändras utan uttryckligt beslut.
2. **Stabilt definierade** – bör normalt bevaras men kan revideras genom en ny designversion.
3. **Kontrollerat varierbara** – får ändras inom angivna ramar.
4. **Situationsberoende** – pose, smuts, väder, ljus och liknande.
5. **Odefinierade** – ännu inte beslutade och får inte behandlas som låsta.

## Designstatus

Använd följande statusmodell:

- `exploration`: flera riktningar är fortfarande öppna.
- `selected`: en riktning är vald men större ändringar är möjliga.
- `refinement`: identiteten är tydlig och detaljer förfinas.
- `locked`: kärnidentiteten är beslutad.
- `production_reference`: underlaget är tillräckligt tydligt för fortsatt produktion.
- `deprecated`: ersatt av en ny version men sparad för spårbarhet.

GPT:n ska inte kalla en design låst enbart för att en bild blev lyckad. Låsning kräver att användaren har godkänt de centrala egenskaperna eller tydligt bett GPT:n att fastställa dem.

## Style Bible – minsta användbara innehåll

En praktisk Style Bible bör minst innehålla:

### Projektets visuella löfte

- medium och målgrupp,
- ton och känslomässig riktning,
- realism- eller stiliseringsnivå,
- visuell särart,
- sådant projektet medvetet inte ska likna.

### Form och silhuett

- dominerande formfamiljer,
- proportioner och skala,
- rytm mellan stora, mellanstora och små former,
- typiska respektive förbjudna silhuetter,
- läsbarhet vid relevant visningsstorlek.

### Färg, ljus och material

- primär, sekundär och accentpalett,
- kontrastprinciper,
- typisk ljussättning,
- materialens ytegenskaper,
- slitage, smuts och åldrande,
- avvikelser som kräver särskild motivering.

### Världs- och tekniklogik

- bygg- och tillverkningsmetoder,
- energikällor,
- underhåll och reparation,
- kulturella eller historiska influenser,
- hur funktion syns i designen.

### Kamera och presentation

- föredragna perspektiv,
- objektiv- eller bildkänsla,
- neutrala referensvyer,
- hero-art-kompositioner,
- typisk bakgrund och bildrymd.

## Designlås för ett enskilt koncept

Varje låst koncept ska dokumentera:

- `concept_id` och namn,
- aktuell version,
- status,
- avsedd användning,
- identitetsbärande egenskaper,
- fasta proportioner,
- färg- och materialregler,
- funktionella krav,
- tillåten variation,
- förbjudna förändringar,
- ännu olösta frågor,
- godkända referensbilder.

## Fasta och fria egenskaper

### Fasta egenskaper

Exempel:

- huvudets grundform,
- asymmetri mellan armar,
- antal fenor eller hjul,
- central färgfördelning,
- relation mellan över- och underkropp,
- byggnadens bärande struktur,
- farkostens huvudsakliga framdrivningsprincip.

### Tillåten variation

Exempel:

- pose och ansiktsuttryck,
- mindre verktyg eller tillbehör,
- väder och ljus,
- grad av slitage,
- lokala dekaler,
- årstidsanpassning,
- kostymvariant inom samma designspråk.

### Förbjuden variation

Exempel:

- att symmetrisera en avsiktligt asymmetrisk design,
- att byta materialfamilj utan berättelsemässig orsak,
- att lägga till mänskliga ansiktsdrag på en ansiktslös robot,
- att ändra silhuetten så att fraktionen inte längre känns igen,
- att flytta funktionella delar till platser där de inte kan fungera.

## Konsekvens mellan bilder

Före en ny bild ska GPT:n sammanfatta de mest kritiska reglerna som en kort **consistency anchor**. Den bör normalt omfatta 5–10 punkter, inte hela Style Bible.

Efter bilden ska GPT:n kontrollera:

1. Är silhuetten fortfarande igenkännbar?
2. Har proportionerna glidit?
3. Har fasta detaljer bytt sida, antal eller form?
4. Följer färgfördelningen den låsta designen?
5. Ser materialen ut att höra till samma värld?
6. Har teknisk, historisk eller magisk logik förändrats?
7. Är avvikelsen avsiktlig eller oavsiktlig?

## Avvikelsehantering

När en ny bild avviker ska GPT:n klassificera avvikelsen:

- `presentation_variation`: ofarlig förändring i pose, ljus eller kamera.
- `acceptable_design_variation`: variation inom uttryckligen tillåtna ramar.
- `unresolved_interpretation`: tidigare odefinierad detalj har tolkats på nytt.
- `consistency_error`: låst egenskap har ändrats.
- `intentional_revision`: användaren har beslutat att ändra designen.

En avvikelse ska inte tyst skrivas in i designen. Vid `intentional_revision` ska versionsnumret höjas och ändringen dokumenteras.

## Versionshantering

Rekommenderad modell:

- patch: förtydligande utan visuell identitetsförändring,
- minor: ny tillåten variant eller märkbar men kompatibel förfining,
- major: förändrad kärnidentitet eller ny designriktning.

Exempel:

- `chr-lighthouse-keeper@1.0.0`
- `chr-lighthouse-keeper@1.2.0` – vinterutrustning tillagd.
- `chr-lighthouse-keeper@2.0.0` – huvudsilhuetten omarbetad.

## Frågebank

- Vilka tre egenskaper gör motivet omedelbart igenkännbart?
- Vad får variera utan att identiteten går förlorad?
- Vilken egenskap är lättast för en bildmodell att råka ändra?
- Vilka vyer saknas för att lösa tvetydigheter?
- Vilka material måste alltid skiljas visuellt?
- Är designen tillräckligt enkel att reproduceras i valt medium?
- Behöver en ny variant skapas eller ska grunddesignen ändras?

## Vanliga fallgropar

- låsa för tidigt efter en enda attraktiv bild,
- dokumentera färger men inte färgfördelning,
- lista detaljer utan att rangordna deras betydelse,
- behandla alla avvikelser som fel,
- kalla en dramatisk hero image för fullständigt referensunderlag,
- blanda projektets Style Bible med ett enskilt objekts designlås,
- ändra låsta egenskaper utan versionsspårning.

## Kvalitetskontroll

En användbar Style Bible ska göra det möjligt för en annan person eller GPT att:

- förstå projektets visuella mål,
- återskapa konceptets identitet,
- skilja fasta regler från fri variation,
- upptäcka tydliga avvikelser,
- skapa nya bilder utan att kopiera exakt samma pose,
- dokumentera avsiktliga förändringar.

## Korsreferenser

- `14-reference-sheet-methods.md`
- `19-sketch-analysis-and-refinement.md`
- `20-concept-handoff-format.md`
