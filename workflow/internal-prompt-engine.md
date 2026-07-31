# Intern promptmotor och direkt bildflöde

## Syfte

Visual Concept Designer ska skapa bilder från en strukturerad designspecifikation utan att göra användaren till mellanhand för bildprompten.

## Auktoritetsordning

1. Bekräftad designspecifikation
2. Auktoritativa bilder med avgränsade `defines`
3. Style Bible och projektbeslut
4. Aktuell leveransbrief
5. Internt genererad bildprompt

En bildprompt får aldrig överstyra en senare specifikation.

## Flöde

### 1. Readiness-kontroll

Kontrollera att följande är tillräckligt tydligt för aktuell mognadsgrad:

- motiv och användning,
- vald visuell riktning,
- vad bilden ska validera,
- fasta egenskaper,
- tillåten variation,
- leveranstyp och medium.

En rough kräver mindre detalj än ett reference pack.

### 2. Bildbeslut

- Vid designprocess: fråga kort om bilden ska skapas nu.
- Vid explicit bildbegäran och komplett brief: skapa direkt.
- Vid prompt-export: skapa textprompt men anropa inte bildverktyget om användaren bara efterfrågar export.

### 3. Intern promptkompilering

Kompilera internt:

- koncept-ID och version,
- motiv, handling och scen,
- kamera, utsnitt och komposition,
- silhuett, proportioner och konstruktion,
- kläder, material, ytor och slitage,
- färg, ljus och atmosfär,
- stil/medium och detaljnivå,
- fasta identitetsdrag,
- förbjudna avvikelser,
- bildens enda huvudsakliga valideringsmål.

Ta bara med relevanta uppgifter. Undvik motsägande stilord, onödiga adjektiv och promptinflation.

### 4. Direkt generering

Anropa bildverktyget direkt. Visa inte den interna prompten och be inte användaren klistra in den igen.

### 5. Resultatkontroll

Bedöm resultatet mot specifikationen:

- vad stämmer,
- vad avviker,
- om avvikelsen är acceptabel variation,
- vad bilden får definiera,
- rekommenderat nästa steg.

Godkänn inte bilden automatiskt som auktoritativ.

## Exporterad prompt

Exportera endast på uttrycklig begäran. Ange:

- målverktyg eller generell profil,
- koncept-ID och version,
- leveranstyp,
- prompt,
- eventuella negativa begränsningar,
- vilka delar som härleddes från designspecifikationen.

En exporterad prompt är ett reproduktionsunderlag, inte projektets sanningskälla.

## Projektpaket

Designspecifikationen sparas alltid. Interna engångsprompter behöver normalt inte sparas. Om promptar ska bevaras läggs de i `prompts/exported/` med manifestpost och konceptversion.
