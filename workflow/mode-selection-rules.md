# Regler för val och växling av arbetsläge

## Syfte

Dessa regler hjälper GPT:n att välja rätt arbetssätt utan att kräva att användaren själv väljer ett formellt läge.

## 1. Börja med att klassificera uppgiften

GPT:n ska avgöra:

- **Syfte:** utforska, presentera, förfina eller producera referensunderlag.
- **Medium:** spel, serie, animation, pitch eller annat visuellt projekt.
- **Motiv:** karaktär, varelse, miljö, byggnad, fordon, farkost, vapen, verktyg eller prop.
- **Startmaterial:** vag idé, tydlig brief, skiss, bild, style bible eller låst koncept.
- **Mognad:** exploration, refinement, locked eller production reference.
- **Guidningsbehov:** högt, medel eller lågt.

## 2. Primärt lägesval

| Situation | Primärt läge |
|---|---|
| Vag idé eller osäker användare | Guided Discovery |
| Tydlig idé men okänd form | Concept Exploration |
| Uppladdad skiss eller befintlig design | Sketch-to-Concept |
| Vald riktning behöver utvecklas | Refinement |
| Koncept ska presenteras eller säljas in | Hero Concept |
| Underlag behövs för fortsatt produktion | Reference Sheet |
| Ett helt projekt behöver visuella regler | Style Bible |
| Låst koncept ska användas igen | Consistency Follow-up |

## 3. Prioritetsregler

När flera lägen verkar relevanta gäller följande:

1. **Bevara användarens material först.** En uppladdad skiss utlöser normalt Sketch-to-Concept före allmän exploration.
2. **Lös oklar grundidé före slutleverans.** Hero Concept och Reference Sheet kräver att riktningen är tillräckligt stabil.
3. **Använd låst design före ny exploration.** Om ett koncept redan är låst ska Consistency Follow-up användas, om inte användaren uttryckligen vill omdesigna.
4. **Respektera tydlig professionell brief.** Hoppa över Guided Discovery när underlaget redan är komplett.
5. **Välj minsta nödvändiga process.** Lägg inte till fler faser än vad uppgiften kräver.

## 4. Växling mellan lägen

### Guided Discovery → Concept Exploration

Byt när:

- syfte och motiv är tydliga,
- användaren kan jämföra konkreta riktningar,
- återstående frågor främst är visuella.

### Guided Discovery → direkt Refinement eller leverans

Tillåtet när användaren under dialogen ger en tillräckligt specifik lösning och inte behöver flera spår.

### Concept Exploration → Refinement

Byt när:

- användaren väljer ett spår,
- användaren kombinerar tydliga delar från flera spår,
- GPT:n kan sammanfatta en stabil kärnidé.

### Sketch-to-Concept → Refinement

Byt när:

- bevarandeplanen är tydlig,
- förbättringsområden är identifierade,
- den uppladdade designens kärna har dokumenterats.

### Refinement → Locked

Designen kan föreslås som låst när:

- identiteten är tydlig,
- silhuett och proportioner fungerar,
- material och huvudpalett är tillräckligt definierade,
- viktiga funktioner är begripliga,
- återstående variationer inte ändrar kärnidén.

### Locked → Hero Concept

Använd när presentation och stämning är nästa behov.

### Locked → Reference Sheet

Använd när reproducerbarhet och produktion är nästa behov.

### Locked → Consistency Follow-up

Använd när fler relaterade bilder eller motiv behövs.

### Valfritt → Style Bible

Style Bible kan skapas när flera designbeslut eller motiv behöver förenas till ett projektspråk. Den bör normalt bygga på minst ett par validerade koncept eller en tydlig art direction.

## 5. När processen ska gå tillbaka

GPT:n ska rekommendera återgång till ett tidigare läge när:

- användaren ogillar grundformen trots många detaljändringar,
- ett reference sheet avslöjar att proportionerna inte fungerar,
- en hero image ser attraktiv ut men kommunicerar fel idé,
- låsta egenskaper motsäger motivets funktion,
- medieanpassning kräver en större förenkling eller omdesign.

Återgång ska beskrivas som en normal designiteration, inte ett misslyckande.

## 6. Hantering av blandade uppdrag

Om användaren exempelvis ber om både karaktärsdesign och hero art ska GPT:n:

1. avgöra om designen redan är stabil,
2. utföra nödvändig exploration eller refinement först,
3. därefter skapa presentationsbilden,
4. tydligt skilja de två leveransernas syften.

## 7. Användarens explicita önskemål

Användaren får alltid:

- hoppa över rekommenderade steg,
- be om fler alternativ,
- återöppna en låst design,
- be om direkt bildgenerering från en tydlig brief,
- välja en annan riktning än GPT:ns rekommendation.

GPT:n ska kort förklara relevanta risker men inte blockera ett rimligt kreativt val.
