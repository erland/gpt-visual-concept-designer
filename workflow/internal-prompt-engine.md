# Intern promptmotor och direkt bildflöde

## Syfte

Visual Concept Designer skapar bilder från en strukturerad designspecifikation utan att användaren behöver hantera bildprompten. Prompt Compiler komprimerar specifikationen före varje bildanrop.

## Auktoritetsordning

1. Bekräftad designspecifikation
2. Auktoritativa bilder med avgränsade `defines`
3. Style Bible och projektbeslut
4. Aktuell leveransbrief
5. Internt kompilerad bildbrief

En äldre prompt får aldrig överstyra en senare specifikation.

## Flöde

### 1. Readiness

Kontrollera motiv, användning, vald riktning, valideringsmål, fasta drag, tillåten variation och leveranstyp. En rough kräver mindre detalj än ett reference pack.

### 2. Bildbeslut

- Vid designprocess: fråga kort om bilden ska skapas.
- Vid explicit bildbegäran och komplett brief: skapa direkt.
- Vid ren prompt-export: exportera text men anropa inte bildverktyget.

### 3. Prompt Compiler

Bygg en kort bildbrief enligt `workflow/prompt-compiler.md`. Ta bara med synliga och relevanta uppgifter. Normalbriefen ska vara sammanhängande, motsägelsefri och normalt under cirka 600 ord.

### 4. Direkt generering

Anropa Image generation. Visa inte den interna briefen och be inte användaren klistra in den.

### 5. Kontrollerad fallback

Vid fel: kompilera en minimal brief och försök exakt en gång till. Misslyckas även det, rapportera felet. Skapa ingen SVG- eller diagramersättning.

### 6. Resultatkontroll

Bedöm vad som stämmer, vad som avviker, om avvikelsen är tillåten, vad bilden får definiera och vilket nästa steg är. Godkänn inte bilden automatiskt som auktoritativ.

## Exporterad prompt

Exportera endast på uttrycklig begäran. Ange målverktyg, konceptversion, leveranstyp, prompt och centrala begränsningar. Exporten är reproduktionsunderlag, inte sanningskälla.

## Projektpaket

Spara designspecifikationen. Interna engångsbriefar behöver normalt inte sparas. Bevarade exporter läggs i `prompts/exported/` med konceptversion och manifestpost.
