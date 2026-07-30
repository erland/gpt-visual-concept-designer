# Problem och fynd

## Metod

Prompt 13 har genomförts som en statisk testanalys: varje tests `must`, kritiska fel och bedömningsdimensioner har spårats mot styrande instruktioner, arbetsflöden, knowledge-filer och mallar. Där faktisk bildgenerering eller en uppladdad skiss krävs har resultatet markerats som fortsatt manuellt verifieringsbehov.

## Prioriterade fynd

### F1 – Otydlig gräns mellan direkt bildbegäran och guidad designprocess

**Risk:** GPT:n kunde lägga in ett onödigt godkännandesteg även när en erfaren användare gav en komplett brief och uttryckligen bad om en bild.

**Berör:** T03, T14.

**Rotorsak:** Reglerna sade både “text före bild” och “direktläge”, men prioriteten mellan explicit bildbegäran och explorativ hjälp var inte tillräckligt explicit.

**Åtgärd:** Huvudinstruktionen och bildpolicyn skiljer nu på direkt bildbegäran med tydlig brief och en begäran om designhjälp.

### F2 – Saknat explicit tillgänglighetssteg för uppladdade skisser

**Risk:** GPT:n kunde resonera om en skiss som användaren hänvisar till trots att den inte faktiskt finns tillgänglig.

**Berör:** T12 och alla framtida bildredigeringstester.

**Rotorsak:** Instruktionen beskrev hur en skiss analyseras, men inte tydligt vad som händer när bildmålet saknas.

**Åtgärd:** Ett obligatoriskt tillgänglighetssteg har lagts till i huvudinstruktion, bildpolicy och K19.

### F3 – Frågebegränsningen var kvalitativ men inte operativ

**Risk:** Nybörjarflödet kunde kännas som ett formulär.

**Berör:** T01, T02, T04.

**Rotorsak:** “Ställ få frågor” saknade en konkret gräns och standardbeteende vid “jag vet inte”.

**Åtgärd:** Normalt högst tre frågor åt gången, bara frågor som kan ändra resultatet, samt ett rekommenderat standardspår.

### F4 – Bekräftade beslut kunde tappas mellan iterationer

**Risk:** GPT:n kunde fråga om samma sak igen eller oavsiktligt ändra tidigare val.

**Berör:** T13, T14, T16, T18.

**Rotorsak:** Designlås fanns, men det saknades ett lättviktigt minne före full låsning.

**Åtgärd:** En beslutslogg med `bekräftat`, `rekommenderat` och `öppet` har införts.

### F5 – Låsningsförslag kunde blandas ihop med användarbeslut

**Risk:** Rekommenderade egenskaper kunde presenteras som redan låsta.

**Berör:** T14, T16, T18.

**Rotorsak:** Instruktionen krävde bekräftelse men specificerade inte hur föreslagna låsningar ska märkas.

**Åtgärd:** Låsningssammanfattningar ska nu separera bekräftat, rekommenderat och öppet.

## Kvarstående manuella risker

- Faktisk bildkvalitet och efterlevnad av en visuell brief.
- Konsekvens mellan flera genererade vyer av samma låsta koncept.
- Hur väl bildverktyget kan hålla turnaround-vyer ortografiska och reproducerbara.
- Hur väl en verklig uppladdad skiss bevaras vid stil- eller realismtest.
- Upplevelsen av frågemängd i en verklig flerstegsdialog.
