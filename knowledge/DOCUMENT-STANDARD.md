# Dokumentstandard för knowledge-filer

## Syfte

Standarden gör filerna konsekventa, sökbara och lätta att underhålla inom GPT:ns begränsade knowledge-utrymme.

## Obligatorisk metadata

Varje fil börjar med YAML-frontmatter:

```yaml
id: K01
title: Visuella designgrunder
status: skeleton
owner_prompt: 5
primary_topics: []
related: []
```

## Obligatoriska huvudrubriker

1. **Syfte** – vilket designproblem filen hjälper till att lösa.
2. **Ansvar** – vad filen är auktoritativ källa för.
3. **Utanför omfattning** – vad som hör hemma i andra filer.
4. **Så ska GPT:n använda kunskapen** – frågor, analyser och rekommendationer som stöds.
5. **Planerat innehåll** – innehåll som skrivs i angiven PLAN2-prompt.
6. **Korsreferenser** – relaterade filer och varför de är relevanta.

Fullständiga filer bör dessutom innehålla:

- kärnprinciper,
- användarvänliga beslutsfrågor,
- rekommendationsmönster,
- vanliga fallgropar,
- korta exempel,
- konsekvens- eller kvalitetskontroll.

## Skrivregler

- Skriv på svenska men behåll etablerade engelska leveransnamn där de behövs.
- Förklara facktermer första gången.
- Presentera alternativ med konsekvenser, inte som absoluta regler.
- Undvik långa kataloger utan beslutstöd.
- Undvik varumärkes- eller konstnärsimitation som huvudsaklig stildefinition.
- Skilj tydligt mellan historisk fakta, vanlig konvention och kreativ rekommendation.
- Duplicera inte arbetsflödet från `workflow/`.
- Duplicera inte mallfält från `templates/`; förklara istället hur de används.

## Exempelstandard

Exempel ska vara korta och visa en princip. Ett exempel får inte bli en dold mall som gör alla resultat likadana.

## Korsreferenser

Använd filnamn i klartext. En fil ska länka till ett annat område när det kräver mer än en kort sammanfattning.
