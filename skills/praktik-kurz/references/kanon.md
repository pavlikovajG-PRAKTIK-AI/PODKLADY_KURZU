# Kánon PRAKTIK-AI: závazná pravidla pro tvorbu kurzu

Projekt TQ23000092 PRAKTIK-AI (UJEP + OU). Platforma vzdělává akademiky, studenty učitelství, mentory, učitele ZŠ/SŠ a vedení škol v AI gramotnosti. Tento soubor shrnuje, co musí každý kurz splňovat. Podrobnosti a kódy jsou v `ciselniky.md`, konkrétní kurzy v `katalog_kurzu.md`, hotový vzor v `vzor_A0601_modul1.md`.

## 1 Terminologie (závazná, nezaměňovat)

| Správně | Význam | Zakázáno |
|---|---|---|
| KURZ | ucelený celek: identifikace, GOALS, M0 skip, 1–5 modulů, capstone, ARTEFAKT | „lekce“, „školení“ |
| GOALS | výkonové cíle kurzu podle Blooma (3. os. sg., sloveso + objekt + podmínka) | „cíle kurzu“, „výsledky učení“ |
| OBJECTIVES | dílčí cíle modulu, ID `KÓD-Onn` (např. A0601-O3), 1–3 na modul | „VL“, „dílčí cíle“ |
| IMPULS | úvodní věta nebo otázka modulu, překvapení, mýtus, situace z praxe | „vstupní hák“, „úvod“ |
| F1 PREZENTACE | výklad, max. 5 min čtení, začíná IMPULSEM | „expozice“, „výklad“ |
| F2 PROCVIČENÍ | aktivita s AI jako partnerem, výchozí formát dialogický | „aktivita“, „cvičení“ |
| F3 OVĚŘENÍ | 2–4 položky ověřující OBJECTIVES modulu + 1 metakognitivní otázka | „test“, „kvíz“ |
| F4 APLIKACE | tvorba jedné sekce ARTEFAKTU, nelze přeskočit | „projekt“, „tvorba“ |
| ARTEFAKT | výstup kurzu skládaný po sekcích ve F4, jde do portfolia, případně do databáze S | „výstup“, „produkt“ |
| CAPSTONE | závěrečný modul: varianta A (zjednodušený F1–F4) nebo B (jen finální ověření rubrikou) | „závěr“ |
| SKIP-TEST | vstupní test modulu, práh 80 %, jen deklarativní obsah | „pretest“ |
| Anchor text | 2–3 věty pro uživatele, pojmenuje problém, vykání, žádné KRAUU ani akademický žargon | |
| Informační nota | prerekvizity, cílová skupina, zařazení v kurikulu | |

V textech pro uživatele pište „Modul 1“ celým slovem; kódy M1–M5 a F1–F4 patří do matrice a instrukcí pro agenta.

## 2 Struktura kurzu

```
1 IDENTIFIKACE (kód DB, kód UI, slug, název pro certifikát, řešený problém, artefakt,
  blok, verze, délka, úroveň, povinnost, EQF, ECTS, prerekvizity, navazující kurzy,
  typ kurzu, anchor text, informační nota, skip pravidla, styl a tón, rozložení fází,
  text certifikátu)
2 GOALS (Bloom 2–6, pokrytí moduly)
3 OBJECTIVES (ID, text, typ, testovatelný, modul, vazba na GOAL)
4 Větvení dle profilu (akademik / mentor / student)
5 Neurovědní principy kurzu (kódy NP)      6 AI principy kurzu
7 KRAUU kompetence (interní)                8 Vzory a antipatterns pro agenta
MODUL 1–5: hlavička · IMPULS · F1 · F2 · F3 · F4
CAPSTONE (A nebo B)
9 ARTEFAKT (definice + šablona povinných sekcí, každá sekce vzniká v konkrétním F4)
11 RUBRIKA 5 × 5 (závazné názvy úrovní, váhy, práh badge 75 %, routing)
12 Výzkumná poznámka
Procvičovací test (volitelný) · Závěrečný test (finální ověření, práh 75 %)
ZDROJE (ověřeno k datu)
```

## 3 Časy a rozsahy

- Kurz 60–105 min, mikrokurz 30–45 min, pilotní kurz ZŠ 120 min. Délka celkem = součet modulů + capstone.
- Modul 15–20 min (tvrdý strop 30 min). Typické rozložení: F1 5 · F2 4 · F3 3 · F4 3.
- F1 nikdy přes 5 min čtení, tedy zhruba 250–400 slov. Jeden modul = jeden jasný poznatek.
- Max. 5 obsahových modulů. Modul 1 = proč je to problém, moduly 2–4 = obsah od jednoduššího ke složitějšímu, modul 5 = aplikace a reflexe.
- Rozsah jednoho vygenerovaného modulu v chatu: max. 2 normostrany (3 600 znaků) bez tabulek.

## 4 Politika hodnocení: AI je partner, ne hlídač

- Výchozí formát F2 je dialogický: FMT-SOK, FMT-VLA, FMT-PRO, FMT-OTA, FMT-MIK. Uzavřené formáty (FMT-MCQ, FMT-TF, FMT-MTC, FMT-SA) patří do F3 tam, kde se ověřuje faktografie, a do skip-testů.
- Každý modul má alespoň jednu otevřenou nebo reflexivní položku („Zamyslete se…“, „Formulujte vlastními slovy…“). Kurz složený jen z uzavřených položek je chyba.
- F3 končí metakognitivní otázkou (co překvapilo, co bylo nejtěžší, jak jistě tomu rozumím).
- F4 vždy uvádí roli AI (konzultant, zrcadlo, partner) a co AI nesmí: nepřepisuje text za uživatele.
- U každého formátu je krátká instrukce pro agenta kurzívou: jak vyhodnotit, kdy neprozradit závěr, max. počet výměn.
- Průběžné hodnocení neovlivňuje badge. Badge = finální ověření ≥ 75 % + odevzdaný artefakt.

## 5 Neurovědní principy

Vyber 4–12 principů z NP-01 až NP-20 pro kurz, u každého modulu 2–5 s určením fáze. Principy nepojmenovávej uživateli, zabuduj je: vybavení bez opory (NP-03), návrat pojmu v jiném modulu jinak (NP-02), „proč“ místo „co“ (NP-08), vlastní verze před vzorem (NP-09), obraz nebo schéma v F1 (NP-06), F1 do 5 min (NP-07), záměrně obtížnější položka (NP-04), reflexe na konci (NP-15), vazba na vlastní praxi, ukotvení v situaci z praxe. IMPULS stavěj na překvapení (NP-11).

## 6 Jazyk a styl

- Výhradně vykání, i v anchor textu, IMPULSU a instrukcích pro agenta.
- Rejstřík zhruba 80/20 populárně-akademický: terminologie přímo, bez omluvných parafráz; tvrzení nesou zdroj (autor, rok, časopis) a kalibrovanou jistotu (preprint ≠ RCT ≠ metaanalýza), přímo v textu.
- Jména v příkladech česká, v jednom kurzu střídat; zakázána cizí jména (zejména Natalia). Obory v příkladech humanitní (dějepis, psychologie, pedagogika, filozofie, sociologie, čeština, dějiny umění, etika), střídat; zakázány právo, biologie, ekonomie, medicína, informatika, obchodní komunikace, pokud nejde o oborový kurz daného předmětu.
- Anchor text: konkrétní problém, přímý, trochu provokativní, bez floskulí. Nikdy „V tomto kurzu se naučíte…“.
- Názvy modulů akční a konkrétní: „Proč X nestačí“, ne „Úvod do X“.
- Žádný AI balast a žádná zakázaná věta: řiď se oddílem 6 „Věty, které nikdy nezazní“ v `systemova_pravidla.md` (osm skupin: prázdné smíření, strašení, marketing, věty odnaučované samotným kurzem, rozpor se směrnicí, didaktické prázdno, balast, falešná blízkost). Na každou napsanou větu použij tři testy z oddílu 6.9: zaměnitelnost, vlastní pravidlo, doložitelnost.
- Jedna metafora na koncept, metafora doprovází termín, nikdy ho nenahrazuje; návratové schéma kurzu (NP-20).
- Neexplicitní KRAUU: kódy kompetencí nikdy v textu pro uživatele.

## 7 Zdroje a integrita

- Každé výzkumné tvrzení má zdroj. Seznam zdrojů na konci s DOI nebo URL a datem ověření. Preprint a rukopis označit.
- Kde existují nezdařené replikace nebo kritika, zmínit jednou větou v F1 i u zdroje.
- Nevymýšlet zdroje. Když zdroj nelze ověřit, přiznat to a nabídnout vyhledávací řetězec.
- Nedoporučovat komerční produkty, mluvit o kategoriích nástrojů a kritériích.
- Kurz obsahuje explicitní pravidla používání AI pro účastníky (co smí, co ne, jak deklarovat) a alespoň jeden explicitní limit nebo antipattern.

## 8 Vstupy, bez kterých kurz nevzniká

1. Kód kurzu z katalogu (nebo důvod, proč kurz v katalogu není) a cílová skupina.
2. Řešený problém jednou větou, jak by ho autor řekl kolegovi.
3. Artefakt: co si účastník odnese a jak pozná, že je hotový.
4. Tři autentické situace z praxe autora (zadání, chyba žáka, věta rodiče, konkrétní text). AI je nevymýšlí; když chybí, vyžádá si je.
5. Zdrojový text nebo materiály autora (článek, kapitola, prezentace, dřívější draft).

## 9 Pojmenování souborů a umístění

- Složka kurzu: `09_Kurzy/<Kód><NázevBezMezer>/`, např. `A0601VyvojDetskehoMozku/`. Cesta je uvedená vůči kořeni projektu; když už je složka kurzu otevřená jako pracovní, soubory patří přímo do ní.
- Kurz: `<KOD>_<NazevBezDiakritiky>_KURZ.md`, export `<KOD>_<Nazev>_KURZ.docx` (výstupy projektu jsou vždy docx, ne PDF).
- Rozhovor: `<KOD>_Rozhovor.md`. QA report: `<KOD>_QA_report.md`.
- Mediální přílohy: `<KOD>-M<n>-<typ>-<popis>.<ext>` (svg, png, mp3, mp4).
- Kód DB = písmeno + 4 číslice (A0601), kód UI = katalogový (A6), slug bez diakritiky s pomlčkami.
- V hlavičce kurzu vždy: verze, datum, autor podkladu, poznámka „K potvrzení garantem“ s otevřenými body.
- Dedikace: „Vzniklo v projektu TQ23000092 PRAKTIK-AI (TA ČR, program SIGMA).“
