# Knowledge-arkitektur

## Lager

Projektet separerar fyra typer av information:

1. `product/` definierar produktens mål, avgränsning och designprinciper.
2. `workflow/` definierar dialog, lägen, sekvens och bildbeslut.
3. `models/` definierar motiv och leveranstyper.
4. `knowledge/` ger domänkunskap som används inom processen.
5. `templates/` definierar återanvändbara in- och utdataformat.

## Routingprincip

När ett uppdrag analyseras väljer GPT:n:

- en primär motivfil,
- högst ett nödvändigt genre- eller historiklager,
- en mediumfil om produktionen kräver särskild anpassning,
- en leverans-/konsekvensfil när arbetet når referens eller handoff.

Detta minskar risken att för många delvis relevanta filer blandas in och ger generiska eller motsägelsefulla råd.

## Ägarskapsregel

Varje begrepp ska ha en huvudsaklig ägare. Exempel:

- silhuettens grundprinciper: K01,
- karaktärsspecifik silhuett: K03,
- läsbarhet i spelkamera: K16,
- presentation av silhuett i referensark: K14.

Sekundära filer får sammanfatta sambandet med en eller två meningar och ska sedan hänvisa till ägarfilen.

## Prioritet vid konflikt

1. Användarens uttryckliga mål och låsta beslut.
2. Produktens säkerhets- och avgränsningsregler.
3. Arbetsflödets beteenderegler.
4. Motiv- och leveransmodell.
5. Specialistkunskap.
6. Generella designkonventioner.

Knowledge-filer får alltså inte skriva över ett medvetet kreativt val. De ska beskriva konsekvenser och möjliga alternativ.

## Utvecklingsordning

- Prompt 5: K01–K05, K08–K08
- Prompt 6: K06–K07
- Prompt 7: K09–K10
- Prompt 8: K11–K12
- Prompt 9: K13–K14, K16–K18
- Prompt 10: K15, K19–K20
