# Prompt Compiler

## Syfte

Prompt Compiler översätter projektets fullständiga designspecifikation till en kort, robust bildbrief för Image generation. Den skiljer projektets sanningskälla från den tillfälliga instruktion som bildverktyget behöver.

## Innehåll som får följa med

Ta endast med uppgifter som direkt påverkar den aktuella bilden:

- motiv och handling,
- leveranstyp och visuell mognad,
- kamera, utsnitt och komposition,
- 3–7 identitetsbärande fasta drag,
- relevanta proportioner, material och färger,
- ljus, atmosfär och medium,
- bildens huvudsakliga valideringsmål,
- ett fåtal nödvändiga förbjudna avvikelser.

## Innehåll som ska bort

Skicka inte vidare:

- projektmanifest eller filvägar,
- koncept-ID annat än när det behövs för intern spårning,
- versionshistorik och changelog,
- beslutsloggar,
- avvisade alternativ,
- långa resonemang,
- upprepade stilord,
- metadata om zip, handoff eller bildstatus,
- instruktioner som inte kan synas i bilden.

## Kompileringsregler

1. Lös motsägelser enligt auktoritetsordningen: aktuell specifikation, auktoritativa bilder, Style Bible, leveransbrief.
2. Välj ett huvudsakligt valideringsmål per bild.
3. Formulera en sammanhängande brief, inte YAML eller punktvis projektdump.
4. Håll normalbriefen under cirka 600 ord; ofta räcker 150–350 ord.
5. Begränsa negativa krav till sådant som skyddar identiteten.
6. Visa inte briefen om användaren inte uttryckligen ber om export.

## Fallback vid fel

Om Image generation misslyckas:

1. skapa en minimal brief med motiv, komposition, 3–7 fasta drag, stil och ljus,
2. ta bort sekundära detaljer, alternativa formuleringar och de flesta negativa krav,
3. gör exakt ett nytt försök,
4. rapportera tydligt om även omförsöket misslyckas,
5. skapa aldrig SVG, diagram eller programmatisk illustration som ersättning.

## Resultatkontroll

Efter lyckad generering jämförs bilden med designspecifikationen. Bilden blir inte auktoritativ förrän användaren godkänner den och dess `defines` har registrerats.
