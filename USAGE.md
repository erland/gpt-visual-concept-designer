# Användarguide

## Nybörjarflöde

Beskriv idén med vardagliga ord. GPT:n ska hjälpa till att precisera syfte, medium och motiv utan att kräva designtermer. När något är oklart erbjuder den normalt två till fyra tydligt skilda riktningar och rekommenderar nästa steg.

Exempel:

> Jag vill skapa en huvudperson till ett äventyrsspel men vet inte hur den ska se ut.

## Expertsnabbspår

Ge en tydlig brief, definiera vad som redan är låst och ange önskad leverans. GPT:n ska då hoppa över onödig introduktion.

Exempel:

> Designen är låst. Skapa en animationsvänlig turnaround med neutral belysning. Ändra inte proportioner, kläder eller palett.

## Skissläge

Ladda upp skissen och ange vad som måste bevaras. GPT:n analyserar först säkra observationer, tolkningar och oklarheter. Den ska inte påstå sig analysera en skiss som inte faktiskt finns i konversationen.

## Bildmognad

1. Textbrief och designriktningar.
2. Silhuett, thumbnail eller rough exploration.
3. Val och riktad feedback.
4. Refined concept.
5. Designlåsning.
6. Hero art eller production reference.

En direkt och tydlig bildbegäran får genomföras utan hela processen, men GPT:n ska inte låtsas att designen därmed är låst eller produktionsklar.

## Designlåsning

Ett designlås bör ange:

- fasta egenskaper,
- tillåtna variationer,
- förbjudna förändringar,
- palett och material,
- funktion och narrativ roll,
- auktoritativa referenser.

Föreslagna låsningar är inte användarbekräftade förrän användaren accepterat dem.

## Handoff

Be om en handoff när konceptet ska lämnas till en illustratör, animatör, 3D-artist eller Game Graphics Creator. Handoff bör innehålla mänskligt läsbar Markdown och vid behov YAML enligt `schemas/concept-spec.schema.yaml`.

## Arbeta med ett löpande projektpaket

1. Be GPT:n starta ett nytt concept project eller ladda upp senaste projekt-zippen.
2. Utveckla koncept och bilder som vanligt.
3. Ange när bilder ska vara exploration, candidate, approved eller deprecated.
4. Ange vilka egenskaper en godkänd bild får styra.
5. Be om en uppdaterad projekt-zip efter en större iteration.
6. Använd alltid den senaste zippen som underlag i en ny chatt.

Exempel: `Importera denna projekt-zip, markera den nya frontbilden som auktoritativ för proportioner och ge mig en uppdaterad zip.`
