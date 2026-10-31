# Steg 2 – projektmodell och funktionskartläggning

## Arkitekturbeslut

**En Skill: `visual-concept-design`.** Det ursprungliga instruktionsträdet beskriver ett sammanhängande arbetsflöde från brief, skiss och specifikation till bildgenerering, granskning, designlåsning och handoff. Att skapa en Skill per motivtyp skulle bryta upp ett gemensamt beslutsspår.

Gemensam `canonical/core.md` innehåller GPT-identitet och roll. `canonical/skills/visual-concept-design/behavior.md` innehåller allt domänbeteende. Exakt sammanfogning av källfilerna motsvarar ursprunglig `assistant/instructions.md` byte för byte. Den äldre instruktionen och `gpt/gpt-instructions.md` bevaras som revisionskällor.

## Funktionskontrakt och hostkrav

| Förmåga | Krav | Runtime-beteende |
|---|---|---|
| Bildgenerering | Kritisk | Använd värdens riktiga bildgenereringsverktyg; skapa inte SVG/diagram som ersättning. Finns verktyget inte: redovisa begränsningen. |
| Analys av uppladdad bild | Kritisk | Kräver bildinmatning och multimodal analys; begär uppladdning om bilden saknas. |
| Designspecificering och beslut | Kärnfunktion | Textbaserat flöde, visuella kvalitetskriterier och designlåsning. |
| Projektpaket | Viktig | Kräver filhantering för manifest/ZIP; inget krav på persistent state för enstaka koncept. |
| Webbreferenser | Valfri | Använd när värdmiljö har webbsökning och användaren behöver faktakontroll. |

**Verktygskontrakt:** Bildgenerering är en *host capability*, inte ett Python-script eller ett påhittat Plugin-MCP-verktyg. Projektets `scripts/` innehåller validerings-/byggresurser; inget script deklareras som körbart Plugin-verktyg.

**Workspace/state:** Långlivade kreativa projekt kan ha versionsmärkt ZIP, manifest, beslut och design-specifikation som flyttbar sanningskälla. Engångsidéer kräver inte arbetsyta. Konversation kan hantera tillfälligt flöde, men vid paketleverans är senaste godkända projektpaketet auktoritativt. Nuvarande äldre YAML `workspace_state` bör harmoniseras med detta före slutligt bygge.

## Runtimebedömning (ej funktionstest)

- **Chat ZIP:** kandidat för fullständigt beteende om värd har bildgenerering, bildinmatning och filstöd.
- **Plugin:** Skill kan paketeras, men automatisk bildgenereringsåtkomst och persistent lagring har inte verifierats. Ingen automatisk aktivering.
- **Claude Projects / Claude Skills:** textinstruktioner möjliga; kritisk bildgenerering kan inte antas.
- **OpenCode:** text och filer möjliga; kritisk bildgenerering är beroende av separat värdverktyg.
- **Custom GPT:** historisk leverans, inte ett sjätte aktivt distributionsmål.

## Resursisolering och spårbarhet

Skillen refererar uttryckligen till befintliga Markdown-filer under `knowledge/` och inga scripts eller assets. `knowledge-manifest.yaml` är källprojektets inventering och inte en körbar resurs. Beroendetillgång per host återstår att verifiera efter paketering.

## Återstår

Installera originalmotor i projektet, kör modern lint och leveransvalidering, migrera/aktivera fem distributioner först efter verifiering, testa bildhandling i faktiska värdar och gör migrationshygien. Detta steg godkänner **projektmodell och källuppdelning**, inte runtime-paritet eller release.
