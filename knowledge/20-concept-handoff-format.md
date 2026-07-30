---
id: K16
title: Format för koncepthandoff
status: complete
owner_prompt: 10
primary_topics:
- all
related:
- K14
- K15
- K19
---
# Format för konceptöverlämning

## Syfte

Ett koncept ska kunna lämnas vidare till en människa, en annan GPT eller ett produktionsflöde utan att kärnbesluten försvinner. Överlämningen ska vara både lättläst och maskinläsbar.

## Överlämningspaket

Ett fullständigt handoff-paket kan innehålla:

1. **Sammanfattning** – vad konceptet är och varför designen ser ut som den gör.
2. **Konceptspecifikation** – strukturerade beslut och status.
3. **Referensbilder** – endast godkända bilder med tydliga roller.
4. **Style Bible-utdrag** – regler som är relevanta för motivet.
5. **Öppna frågor** – sådant som ännu inte ska antas.
6. **Produktionsmål** – vad nästa mottagare ska skapa.
7. **Acceptanskriterier** – hur resultatet kan kontrolleras.
8. **Ändringshistorik** – viktiga revisioner och orsaker.

## Människoläsbar sammanfattning

Sammanfattningen bör besvara:

- Vad är motivet?
- Vilken funktion har det?
- Vad gör det visuellt unikt?
- Vilka egenskaper är låsta?
- Vad får variera?
- Vilka bilder är auktoritativa?
- Vad ska göras härnäst?

## Maskinläsbar specifikation

Rekommenderat YAML-format:

```yaml
schema_version: 1
concept:
  id: chr-lighthouse-keeper-001
  name: Fyrvaktaren
  version: 1.0.0
  type: character
  status: locked
  medium: game
  intended_use:
    - playable_character_reference

purpose:
  narrative_role: ensam väktare av en översvämmad kust
  production_goal: underlag för sprites och porträtt

visual_identity:
  silhouette: lång och smal med stora rundade axlar
  proportions:
    height_heads: 7.5
    notes: långa ben och kompakt huvud
  dominant_shapes:
    - vertical_rectangles
    - circles
  asymmetry:
    - vänster arm är större och industriell

palette:
  primary: faded_yellow
  secondary: oxidized_dark_steel
  accent: warm_amber
  distribution: gul torso, mörka leder, bärnstensljus i huvud och bröst

materials:
  - id: painted_steel
    finish: matte_worn
  - id: cloudy_glass
    finish: internally_lit

fixed_features:
  - lantern_shaped_head
  - circular_chest_hatch
  - asymmetric_arms

allowed_variation:
  - pose
  - minor_tools
  - surface_wear
  - lighting

forbidden_changes:
  - human_facial_features
  - glossy_clean_surfaces
  - symmetrical_arms

open_questions:
  - exakt konstruktion på ryggens servicepanel

references:
  - id: ref-front-01
    role: authoritative_front_view
    status: approved
  - id: ref-hero-01
    role: mood_and_presentation_only
    status: approved

handoff:
  recipient: game_graphics_creator
  requested_outputs:
    - character_sprite_specification
    - portrait_reference
  acceptance_criteria:
    - silhuetten ska vara läsbar i spelkamerans storlek
    - fasta kännetecken ska bevaras
```

## Auktoritet hos referenser

Varje bild ska få en roll:

- `authoritative_design_reference` – styr form, proportion och detaljer.
- `authoritative_color_reference` – styr färg och material.
- `mood_reference` – styr stämning men inte exakta detaljer.
- `composition_reference` – styr bildupplägg.
- `exploration_only` – får inte behandlas som låst design.
- `deprecated` – äldre referens som inte längre ska användas.

Det förhindrar att en dramatisk bild oavsiktligt blir sanningskälla för detaljer den aldrig var avsedd att definiera.

## Handoff till Game Graphics Creator

Överlämningen bör särskilt ange:

- kamera och projektion,
- önskad asset-typ,
- storlek och läsavstånd,
- silhuettkrav,
- färg- och materialregler,
- animations- eller variationsbehov,
- vilka referenser som är auktoritativa,
- vilka delar som får förenklas,
- tekniska mått som redan är beslutade,
- vad som fortfarande ska lösas av mottagaren.

Visual Concept Designer ska inte låtsas att concept art redan är en tekniskt färdig asset.

## Handoff till serieproduktion

Ange:

- reproducerbara vyer,
- återkommande ansikts- och kroppskännetecken,
- detaljnivå för normala paneler,
- svartvit eller färgad läsbarhet,
- uttryck och posebehov,
- förenklingar för återkommande teckning.

## Handoff till animation

Ange:

- turnaround-status,
- volym- och proportionregler,
- rörliga respektive fasta delar,
- material som deformeras,
- ansiktskontroller eller uttryck,
- typiska poser och rörelsespråk,
- detaljer som kan förenklas för rigg eller animation.

## Acceptanskriterier

Acceptanskriterier ska vara observerbara. Undvik vaga formuleringar som “ska kännas cool”. Skriv hellre:

- silhuetten ska kunna skiljas från övriga fraktionsmedlemmar,
- tre fasta färgfält ska behållas,
- huvudets bredd ska vara ungefär 60 % av axelbredden,
- inga mänskliga ögon får läggas till,
- dörrar och passager ska visa rätt skala för användaren.

## Ändringshistorik

Varje avsiktlig revision bör dokumentera:

- datum eller versionsnummer,
- ändrad egenskap,
- tidigare värde,
- nytt värde,
- orsak,
- vilka referenser som ersätts.


## Projektpaket för längre arbetsflöden

När flera koncept och bilder utvecklas över tid ska handoff kunna utökas till en komplett projekt-zip. Följ `workflow/project-bundle-workflow.md`. Paketet ska innehålla projektmanifest, konceptmanifest, bildmanifest, textbeskrivningar, godkända och explorativa bilder, Style Bible, changelog och eventuella produktionshandoffs. Den senaste godkända zippen är auktoritativ källa; enskilda tidigare chattmeddelanden eller bilder får inte antas ersätta paketet.

Varje bild ska registreras med stabilt ID, filsökväg, koncept-ID, status, roll, vad den definierar och vad den inte får definiera. Ersatta bilder ska markeras `deprecated`, inte tyst skrivas över.

## Minsta handoff

När ett fullständigt paket är onödigt ska GPT:n åtminstone leverera:

- konceptets namn och ID,
- status,
- fem viktigaste fasta egenskaper,
- tillåten variation,
- auktoritativa referenser,
- nästa mottagare och önskad leverans,
- öppna frågor.

## Vanliga fallgropar

- lämna över alla bilder utan att ange deras roller,
- blanda låsta beslut och idéer under utforskning,
- glömma öppna frågor,
- ange stilord utan observerbara designregler,
- sakna acceptanskriterier,
- behandla concept art som färdig produktionsfil,
- skriva en så stor specifikation att det viktigaste försvinner.

## Kvalitetskontroll

En bra handoff ska låta mottagaren:

- förstå konceptets funktion och identitet,
- veta vad som är låst,
- veta vad som får lösas fritt,
- välja rätt referenser,
- upptäcka avvikelser,
- skapa nästa leverans utan att fråga om redan fattade beslut.

## Korsreferenser

- `14-reference-sheet-methods.md`
- `15-style-bible-and-consistency.md`
- `19-sketch-analysis-and-refinement.md`
