# opencode: model

Visual Concept Designer använder en gemensam kanonisk Skill (`canonical/skills/visual-concept-design/behavior.md`).

Bildgenerering och analys av bilder kräver faktiska funktioner i värdmiljön. Distributionens ZIP garanterar inte att sådana funktioner finns eller är aktiverade.

Verifiera i respektive värdmiljö: att bildreferenser kan granskas, att originalbild kan genereras, att användarens ändringsinstruktioner kan omsättas i en ny bild samt att metadata och specifikation följer det faktiska resultatet. Om ett krav inte stöds ska assistenten förklara begränsningen och inte påstå att bilden genererats.

Paketet använder distributionsmålet `opencode` med inställningarna i `gpt-project.yaml`.
