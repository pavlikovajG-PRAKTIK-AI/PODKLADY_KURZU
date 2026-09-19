# Analýza promptu „Příprava testovacích materiálů platformy PRAKTIK-AI“ (v1.0, duben 2026) a návrh změn

Datum analýzy: 19. 9. 2026. Podklad: složka 09_Kurzy na Disku (katalog kurzů 2026-09, protokol rozhovoru s autorem, formulář oponenta, univerzální struktura kurzu, podklad pro IT v2, aktualizace promptu Metodického architekta v2.2, systémová pravidla, kurzy A0601, A0602, A0701).

## Závěr

Prompt v1.0 je zastaralý ve třech ohledech. Tým od dubna vyrobil kurzy v mnohem bohatší struktuře (matrice v6, vzor A0601), přijal protokol rozhovoru s autorem s Definition of Done a schválil politiku „AI jako partner, ne hlídač“. Prompt generuje jiný typ materiálu, než jaký tým dnes považuje za standard. Náhradou je sada skillů praktik-* v tomto repozitáři a zkrácená instrukce projektu (`Projektove_instrukce_v2.md`).

## Co se od dubna změnilo a prompt to neznal

- Katalog kurzů 2026-09: kódy A0–A12, B1–B15, C1.1–C19.1, D1–D3, Z1–Z4; cílové skupiny AK, ST, ME, UČ, VŠ, AB; formáty kurz / mikrokurz / pilotní kurz ZŠ; vlny V0–V4; autoři a oponenti.
- Protokol rozhovoru s autorem: bez tří autentických situací z praxe kurz nevzniká. Prompt přijímal jen „název kurzu nebo téma“.
- Hotové kurzy používají IDENTIFIKACI (kód DB, kód UI, slug, text certifikátu, EQF, ECTS), GOALS podle Blooma, OBJECTIVES s ID, u modulů IMPULS a fáze F1–F4, kódy FMT a NP, větvení rolí, capstone, rubriku 5 × 5 a ověřené zdroje.
- Systémová pravidla: terminologie, vykání, česká jména, povolené obory v příkladech, limit 30 min na modul.

## Slabiny promptu v1.0

1. Chybí F4 APLIKACE. Prompt slibuje artefakt, ale nemá mechanismus, jak vzniká po modulech.
2. Šablona pěti otázek je ze čtyř pětin uzavřená. Podklad pro IT v2, který prompt sám uvádí jako závazný, říká, že kvíz je okrajový formát a výchozí jsou dialogické formáty.
3. Záměna pojmů: F2/F3 nejsou „formáty otázek“, jsou to fáze modulu; formáty mají kódy FMT.
4. Žádná práce se zdroji, kalibrace jistoty ani anti-halucinační pravidlo.
5. Chybí M0 skip test, capstone, větvení rolí akademik / student / mentor.
6. Číslo projektu TQ23000092N versus TQ23000092 v ostatních dokumentech.
7. Placeholder pro vzorový výstup zůstal prázdný; A0601 modul 1 je hotový few-shot příklad.
8. Příkaz „vždy prohledej všechny dokumenty před odpovědí“ stojí tokeny při každé otázce; znalostní báze obsahuje 18 MB PDF KRAUU, 190 kB xlsx matrice a dokumenty, jejichž obsah je už v promptu.

Co zachovat: anchor text a informační nota (A0601 je převzal), pravidla anchor textu, export do docx v domácím stylu.

## Úspora tokenů

- Tři vrstvy znalostí: kánon v instrukci nebo skillu, malé referenční soubory (číselníky, výpis katalogu), velké dokumenty jen na vyžádání.
- Dvoufázové generování: kostra ke schválení, pak moduly po jednom.
- Zdrojový článek do konverzace, ne do znalostí projektu.
- Skilly místo znalostní báze: skill načte jen svůj hlavní soubor a reference otevírá podle potřeby. Znalostní báze projektu se posílá stále dokola.

## Co vzniklo

Skilly `praktik`, `praktik-rozhovor`, `praktik-kurz`, `praktik-qa`, `praktik-export` (složka `skills`, zipy ve složce `zips`), instalační skript, návod pro metodičky, text a seznam screenshotů pro videomanuál, kopie podkladů. Výstup projektu je docx; JSON pro IT se nevyrábí.
