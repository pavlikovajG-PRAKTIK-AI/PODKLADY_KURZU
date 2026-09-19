# Šablona kurzu PRAKTIK-AI (Markdown)

Vyplňuj bez placeholderů. Co nevíš, dej do poznámky „K potvrzení garantem“ v hlavičce. Formát odpovídá vzoru A0601, aby ho zpracoval export do docx i JSON.

```markdown
# NÁZEV KURZU VELKÝMI PÍSMENY

### Podtitul: jedna věta, která pojmenuje problém

**Kompletní textový základ kurzu dle PRAKTIK-AI Matrice v6.0**
Verze 1.0 | D. M. RRRR | Autor podkladu: Jméno Příjmení (e-mail)

> ⚠ **K potvrzení garantem:** pracovní kód kurzu **X0000** (blok, kolize s kurikulem), EQF, délka; otevřené body.

---

## 1 IDENTIFIKACE

| Klíč | Hodnota |
|---|---|
| Interní kód (DB) | X0000 |
| Zobrazovací kód (UI) | X0 |
| URL slug | nazev-bez-diakritiky |
| Plný název kurzu (certifikát) | … |
| Řešený problém | 2–4 věty: bolest praxe, dva zrcadlové omyly, co je v sázce |
| Výstup kurzu (artefakt) | **Název artefaktu** – jedna věta, „budovaný po sekcích v F4 každého modulu“ |
| Blok | A / B / C / D / Z |
| Verze kurzu | 1.0 |
| Délka celkem (min) | 90 (5 × 15 min modul + 15 min capstone) |
| Úroveň | Základní / Pokročilý |
| Povinnost | Povinný / Doporučený / Volitelný |
| EQF úroveň | 6 / 7 / 8 |
| ECTS (orientační) | 0,1 |
| Prerekvizity (kódy) | … |
| Navazující kurzy (kódy) | … |
| Typ kurzu | Obecný / Oborový / Průřezový / Vstupní kurz skupiny / Specializovaný |
| Skip povolen? | Ano – deklarativní moduly M…, práh 80 %; M… a všechny F4 přeskočit nelze |
| Při neúspěchu skip-testu | Uživatel prochází modul standardně |
| Styl psaní | Konverzační (vykání) + narativní; analytický u evidence |
| Typické rozložení fází (min) | F1: 5 · F2: 4 · F3: 3 · F4: 3 |

**Anchor text:**
*2–3 věty, vykání, pojmenovaný problém, bez KRAUU a žargonu.*

**Informační nota:**
Prerekvizity, komu je kurz určen, zařazení v kurikulu, doporučené pořadí.

**Text certifikátu:**
Absolvent/ka … (shrnutí GOALS jednou souvislou větou, slovesa 3. os. sg.).

---

## 2 GOALS (výkonové cíle kurzu)

| ✓ | Bloom | GOAL | Pokryto v modulech |
|---|---|---|---|
| X | 2 – Porozumět | **G2:** … | M1, M2 |
| X | 4 – Analyzovat | **G4:** … | M2–M4 |
| X | 5 – Hodnotit | **G5:** … | M3–M5 |
| X | 6 – Tvořit | **G6:** … artefakt … | M1–M5 (F4), Capstone |

## 3 OBJECTIVES (cíle modulů)

| ID | Text OBJECTIVE | Typ | Testovatelný? | Modul | Vazba na GOAL |
|---|---|---|---|---|---|
| X0000-O1 | … | znalostní | ano | M1 | G2 |
| X0000-O2 | … | analytický | ano | M2 | G2, G4 |
| … | | | | | |

## 4 Větvení dle profilu uživatele

| Modul | Akademik | Mentor / uvádějící učitel | Student učitelství |
|---|---|---|---|
| M1–M5 | … | … | … |
| Capstone | … | … | … |

## 5 Neurovědní principy kurzu (globální výběr)

Zaškrtnuto: **NP-xx** (kde a jak), …

## 6 AI principy kurzu

Zaškrtnuto: AI jako partner v dialogu (FMT-SOK v M…) · AI jako scaffold, ne náhrada · …

## 7 KRAUU kompetence

Zaškrtnuto: **x.y** (proč), …

## 8 Vzory a antipatterns pro agenta

| Typ | Pravidlo | Zdůvodnění | Kde |
|---|---|---|---|
| MUSÍ | … | … | globálně |
| NESMÍ | … | … | M… |

---

# MODUL 1 — Akční název

**Délka:** 15 min | **OBJECTIVES:** X0000-O1 | **Skip:** ano (80 %) | **Vazba na GOALS:** G2
**Neurovědní principy v modulu:** NP-xx (fáze, jak), …

## IMPULS

*Jedna věta nebo otázka. Překvapení, mýtus, situace z praxe. Nikdy definice.*

## F1 PREZENTACE (5 min)

Kontextový odstavec (kde jsme, proč teď). Obsahový odstavec se zdroji (autor, rok, časopis; kalibrovaná jistota). Tučně zvýrazněné 2–4 klíčové body nebo mechanismy.

*Zapamatujte si: jedna věta, praktický obraz nebo pravidlo.*

**Větvení:** Akademik – … Mentor – … Student – …

## F2 PROCVIČENÍ (4 min) — FMT-xxx (název formátu)

*Instrukce pro agenta: jak vést, co nevyzradit, jak vyhodnotit, max. počet výměn.*

Zadání pro uživatele. U párování tabulka + klíč. U dialogu startovní scénář.

## F3 OVĚŘENÍ (3 min) — FMT-xxx + FMT-xxx

1. **[MCQ]** … a) … b) … ✓ c) … d) …
2. **[T/F]** … — **Pravda/Nepravda** (zdůvodnění).
3. **[SA]** Vlastními slovy: …
4. **[Metakognice]** Co vás v modulu překvapilo / co bylo nejtěžší?

## F4 APLIKACE (3 min) — Artefakt, sekce 1

Uživatel vytvoří **Název sekce**: co přesně, v jakém rozsahu, s jakým zdůvodněním. *AI role: konzultant – max. 2 upřesňující otázky, nepřepisuje text za uživatele (FMT-VLA).*

---

# MODUL 2 — … (stejná struktura)

…

# CAPSTONE — Finální ověření (Varianta A/B)

**Délka:** 15 min | **Obsah:** kompletace artefaktu + závěrečný test + rubrika + reflexe.

1. **Kompletace artefaktu (5 min):** …  *AI role: zrcadlo – 2 reflexivní otázky.*
2. **Závěrečný test (8 min):** práh badge 75 %.
3. **Reflexivní poznámka (2 min):** … (jde výzkumnému týmu).

---

## 9 ARTEFAKT — Název

| Klíč | Hodnota |
|---|---|
| Typ artefaktu | ART-xxxx – … |
| Musí obsahovat | … |
| Nesmí obsahovat | … |
| Primární formát | … |
| Vstupuje do databáze scénářů? | Ano (anonymizovaně, pouze po souhlasu autora) / Ne |
| Podmínka badge | Závěrečné ověření ≥ 75 % + odevzdaný artefakt |

**Šablona artefaktu — povinné sekce:**

| # | Sekce | Co obsahuje | Povinná? | Vzniká v |
|---|---|---|---|---|
| 1 | … | … | ano | Capstone |
| 2 | … | … | ano | M1/F4 |
| … | | | | |

## 11 RUBRIKA (finální ověření artefaktu)

**Typ:** analytická 5 × 5 | **Hodnotitel:** … | **Práh badge:** 75 %

| Kritérium (váha) | Mistrovství 81–100 % | Zdatnost 61–80 % | Způsobilost 41–60 % | Rozvoj 21–40 % | Začátek 0–20 % |
|---|---|---|---|---|---|
| **1. … (25 %)** | … | … | … | … | … |
| … | | | | | |

**Routing (11.3):** Silný výkon ≥ 80 % → … Slabý výkon < 60 % → … Mezera v X0000-Ox → …

## 12 Výzkumná poznámka

Sledovaná proměnná, pre/post, co jde výzkumnému týmu.

---

# ZÁVĚREČNÝ TEST (finální ověření, práh 75 %)

8–12 položek napříč OBJECTIVES, mix formátů, alespoň 2 scénářové, 1 otevřená.

# ZDROJE (ověřeno D. M. RRRR)

**Tematická skupina**
1. Autor, A. (rok). Název. *Časopis, ročník*(číslo), strany. https://doi.org/… *(status evidence, poznámka)*

---
*Vzniklo v projektu TQ23000092 PRAKTIK-AI (TA ČR, program SIGMA). Pravidla používání AI pro účastníky: …*
```
