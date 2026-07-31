# Release Notes — Visual Concept Designer v1.4.0

## Huvudnyhet: Prompt Compiler

Den fullständiga designspecifikationen skickas inte längre direkt till bildverktyget. En intern kompilator skapar i stället en kort, sammanhängande bildbrief med endast sådant som påverkar den aktuella bilden.

Det minskar risken för bildfel efter långa planeringssessioner och bevarar samtidigt designspecifikationen som projektets sanningskälla.

## Kontrollerad fallback

Om första bildanropet misslyckas skapas en minimal brief med motiv, komposition, 3–7 fasta identitetsdrag, stil och ljus. GPT:n gör exakt ett nytt försök. Vid fortsatt fel rapporteras detta tydligt; SVG eller annan programmatisk ersättning är förbjuden.

## Kompatibilitet

- 20 knowledge-filer
- GPT-instruktion under 8 000 tecken
- 30 testfall
- Image generation och Code Interpreter kan fortsatt vara aktiverade samtidigt

