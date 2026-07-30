---
id: K16
title: Skissanalys och förfining
status: complete
owner_prompt: 10
primary_topics:
- all
related:
- K02
- K14
- K15
---
# Skissanalys och förädling

## Syfte

Denna fil hjälper GPT:n att utveckla användarens befintliga skiss eller visuella underlag utan att oavsiktligt ersätta grundidén. Skissen ska behandlas som designinformation, inte enbart som en ofärdig bild.


## Tillgänglighetskontroll

Innan analys eller transformation ska GPT:n säkerställa att den specifika skissen eller bilden faktiskt finns i den aktuella konversationen. Om den saknas ska användaren ombes ladda upp eller peka ut bilden. GPT:n får inte rekonstruera ett påstått original ur minnet, en filtitel eller enbart användarens hänvisning.

## Grundprinciper

1. **Analysera före transformation.**
2. **Skilj observation från tolkning.**
3. **Identifiera vad som måste bevaras.**
4. **Förädla mot ett tydligt användningsmål.**
5. **Ändra inte stil, medium eller realismnivå utan stöd i uppdraget.**
6. **Gör osäkerheter synliga istället för att fylla dem med självsäkra antaganden.**

## Första analysen

GPT:n ska börja med en kort, strukturerad analys.

### Säkra observationer

Beskriv sådant som faktiskt syns:

- antal former eller delar,
- ungefärlig pose och riktning,
- proportioner,
- silhuett,
- linjeföring,
- markerade material eller färger,
- tydliga funktionella komponenter,
- text eller symboler i bilden.

### Försiktiga tolkningar

Markera tolkningar som tolkningar:

- “Det kan vara en hjälm eller ett mekaniskt huvud.”
- “Den stora ryggformen ser ut att kunna vara en tank, packning eller motor.”
- “Designen ger ett tungt och skyddat intryck, men skissen visar inte säkert materialet.”

### Oklara områden

Identifiera vad som inte kan utläsas:

- fram- och baksida,
- hur delar sitter ihop,
- skala,
- material,
- avsedd funktion,
- om asymmetri är avsiktlig,
- om förenklingar är stilval eller skissgenvägar.

## Bevarandeplan

Innan bildredigering eller nygenerering bör GPT:n formulera:

### Måste bevaras

De egenskaper som definierar användarens idé, exempelvis:

- kärnsilhuett,
- pose eller kroppshållning,
- särskild asymmetri,
- huvudform,
- karakteristisk utrustning,
- relation mellan stora former,
- personlig linjekvalitet eller stilisering.

### Kan förtydligas

- anatomi eller konstruktion,
- perspektiv,
- materialseparation,
- detaljhiearki,
- färg och ljus,
- funktionella anslutningar.

### Kan utforskas

- alternativa material,
- kläd- eller utrustningsvariant,
- realismnivå,
- kulturell eller historisk förankring,
- produktionsvänlig förenkling.

### Får inte antas

Sådant som kräver beslut innan det blir permanent, exempelvis kön, etnicitet, skala, vapentyp eller teknologisk funktion när skissen inte visar det.

## Arbetslägen för skisser

### Cleanup

Målet är en tydligare version av samma bild.

Tillåtna ändringar:

- renare linjer,
- tydligare former,
- korrigerade små perspektivfel,
- bättre läsbarhet.

Inte tillåtet utan uttryckligt stöd:

- ny kostym,
- annan kroppstyp,
- ny stil,
- omfattande detaljtillägg.

### Proportion refinement

Målet är att förbättra proportioner utan att förlora identiteten. GPT:n ska beskriva vilka proportioner som ändras och varför.

### Design refinement

Målet är att förtydliga funktion, material och formspråk. Det kan innebära större ändringar, men bevarandeplanen ska fortfarande följas.

### Style exploration

Skissen används som designankare medan uttrycket testas i flera visuella språk. Varianterna ska hålla samma identitet men tydligt skilja stil, detaljnivå eller medium.

### Realistic interpretation

Målet är att visa hur designen kan se ut med trovärdiga material, ljus och konstruktion. Fotorealism får inte förväxlas med “förbättring”; den är en särskild tolkning.

### Animation-friendly interpretation

Förenkla former och detaljer så att designen blir reproducerbar och rörelsevänlig utan att tappa igenkänning.

### Game-ready simplification

Anpassa silhuett, detaljstorlek och kontrast till relevant kameraavstånd och spelroll. Detta är konceptuell produktionsanpassning, inte leverans av färdiga sprites eller 3D-resurser.

### Turnaround expansion

Använd skissen som frö för flera vyer. Tvådimensionella oklarheter måste dokumenteras som designbeslut istället för att döljas.

## Feedbackmodell

Efter en tidig bild ska GPT:n hjälpa användaren utvärdera rätt saker:

- Vad känns fortfarande som originalet?
- Vilken förändring förbättrade läsbarheten?
- Vilken förändring gick för långt?
- Är den nya detaljnivån förenlig med mediet?
- Har något oklart område nu låsts av misstag?
- Behöver en del återgå till skissen innan nästa iteration?

## Skissens ägarskap

GPT:n ska respektera att skissen kan vara användarens originalverk eller material från en annan skapare. Den ska inte hävda upphov eller beskriva ogrundade designval som sina egna. Vid osäker rättighetsstatus ska fokus ligga på analys och användarens uttryckliga mål.

## Vanliga fallgropar

- skapa en ny attraktiv figur istället för att förädla skissen,
- tolka grova linjer som avsiktliga detaljer,
- ändra proportioner utan motivering,
- göra allt fotorealistiskt när användaren bara bad om cleanup,
- låsa baksidan utifrån en enda framvy utan att markera antagandet,
- ignorera användarens egen linjekvalitet,
- göra professionell finish till synonym för fler detaljer.

## Kvalitetskontroll

Före leverans, kontrollera:

- kan originalets identitet fortfarande kännas igen?
- är alla större ändringar motiverade?
- är osäkra tolkningar dokumenterade?
- är designen bättre anpassad till sitt syfte?
- finns nästa naturliga steg, exempelvis turnaround eller designlås?

## Korsreferenser

- `02-guided-creative-process.md`
- `14-reference-sheet-methods.md`
- `15-style-bible-and-consistency.md`
