# T25 – Ny designspecifikation över äldre prompt

## Scenario
En äldre exporterad prompt säger brun läderrock. Användaren ändrar den bekräftade designen till mörkblå vaxad canvas och ber om en ny bild.

## Förväntat
- uppdaterar designspecifikationen först,
- bygger nästa interna prompt från den nya specifikationen,
- återanvänder inte den gamla materialbeskrivningen,
- skapar bilden direkt när begäran är tydlig.

## Fail
Den äldre prompten behandlas som auktoritativ och den bruna läderrocken återkommer.
