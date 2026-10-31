# Projektspecifika E2E-scenarier för bildarbetsflöden

**Status:** Ej körda i en verklig värdmiljö. Dessa är manuellt reproducerbara acceptanstester, inte dokumentation av passerade bildtester. Kör dem separat för varje aktiverad runtime, och notera tillgängliga verktyg.

För varje scenario: dokumentera runtime/version, datum, körande testare, exakt prompt och bifogad bild, observerad modellrespons, eventuellt bildartefakt-ID, avvikelse, PASS/FAIL/BLOCKED och skärmbild/logg. PASS kräver observerat beteende, inte enbart rätt instruktionstext.

| ID | Förutsättning och instruktion till assistenten | Godkännandekriterium |
|---|---|---|
| E2E-01 | Ny chatt: ”Jag vill skapa en mystisk skogsvarelse men vet inte hur den ska se ut.” | Få relevanta frågor, möjliga kreativa riktningar, ingen obegärd låsning |
| E2E-02 | Ny chatt: ”Skapa nu en konceptbild av en liten mekanisk fågel i koppar på neutral bakgrund.” | Faktisk bildgenerering via värdens bildverktyg; ingen text/SVG/HTML som låtsas vara en bild; tydligt fel vid saknad generator |
| E2E-03 | Bifoga egen enkel skiss av ett föremål. Säg: ”Behåll silhuetten, förfina materialen.” | Skissen analyseras och bevarandekrav redovisas innan generering; uppladdad fil ska faktiskt gå att läsa |
| E2E-04 | Efter E2E-02: ”Behåll fågelns näbb och vingar, ändra bara färgen till blå.” | Ny bild med låsta former bevarade och ändrad färg; avvikelser identifieras |
| E2E-05 | Efter designiteration: ”Lås designen.” och därefter begär reference sheet. | Design låses enbart efter uttrycklig bekräftelse; ett riktigt referensblad skapas om värdens generator stöder detta |
| E2E-06 | Be om export av beslutad designspecifikation och tillhörande bildreferenser. | Versionsmärkt projektunderlag med spårbar identitet; ingen påhittad fil eller referens |
| E2E-07 | I miljö utan bildgenerering: ”Skapa en konceptbild nu.” | Begränsningen anges, ingen falsk bildleverans, användbart textalternativ utan att utge det för bild |
| E2E-08 | Framkalla ett kontrollerat generatorfel om värden stöder felinjektion. | Exakt ett komprimerat återförsök; sedan tydligt felbesked, ingen SVG-placeholder |

## Runtime-matris (ska fyllas med observerade resultat)

| Runtime | E2E-01 | E2E-02 | E2E-03 | E2E-04 | E2E-05 | E2E-06 | E2E-07 | E2E-08 |
|---|---|---|---|---|---|---|---|---|
| ChatGPT Chat | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN |
| OpenAI Plugin | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN |
| Claude Projects | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN |
| Claude Skills | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN |
| OpenCode | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN |

**Viktigt:** Ett BLOCKED kan vara ett korrekt konstaterat värdberoende; det är inte PASS. Testerna för bildinmatning och bildgenerering kräver verkligen fungerande verktyg i respektive värd.
