# Genomförda korrigeringar

## Huvudinstruktion

- Skiljer explicit mellan direkt bildbegäran och guidad designhjälp.
- Begränsar normalt dialogen till högst tre frågor åt gången.
- Kräver ett rekommenderat standardspår när användaren svarar “jag vet inte”.
- Inför en kort beslutslogg i längre arbetsflöden.
- Kräver att ett specifikt bildmål faktiskt är tillgängligt före analys eller redigering.
- Skiljer bekräftade låsningar från rekommenderade och öppna egenskaper.

## Arbetsflöde och knowledge

- `workflow/image-generation-policy.md` har fått en avsiktskontroll och ett saknat-bildmål-flöde.
- `knowledge/19-sketch-analysis-and-refinement.md` har fått en obligatorisk tillgänglighetskontroll.
- `templates/decision-log.md` har lagts till.

## Testdokumentation

- Statisk testspårbarhet och kvarstående manuella verifieringsbehov har dokumenterats.
- Resultaten skiljer mellan specifikationsmässigt stöd och empiriskt verifierad bildprestanda.
