# Matrice kurzu v7.0 (PRAKTIK-AI)

Stav: 25. 9. 2026 · Podklad změn: audit promptů generátoru kurzů platformy (simulace A0101, 12 variant).

## Obsah složky

| Soubor | Obsah |
|---|---|
| `PRAKTIK-AI_Matrice_kurzu_v7.0.xlsx` | šablona matrice kurzu, verze 7.0 (vychází z v6.0, všechny listy, komentáře a validace zachovány) |
| `PRAKTIK-AI_Prompt_Metodicky_architekt_v3.0.md` / `.docx` | systémový prompt pro tvorbu matrice podle v7.0 (nahrazuje v2.2) |
| `Prompty_generatoru_kurzu_v2.md` | návrh promptů generátoru platformy (course_summarizer, course_planner) sladěný s v7.0 |

## Co je nového v Matrici v7.0

- **F1 PREZENTACE 5–10 min** (dříve max. 5). Délku určují úroveň a náročnost tématu (nový list `CIS_Urovne`). Na listech M1–M5 platí validace 5–10.
- **Úroveň (1_Identifikace, 1.2)** = zkušenost účastníka s AI: Začátečník / Středně pokročilý / Pokročilý (rozbalovací seznam).
- **Cílové skupiny**: Akademik (vč. doktorandů), Student (Bc., Mgr.), Mentor (provázející učitel ZŠ/SŠ). Definice pro generátor jsou v novém listu `CIS_Skupiny`. Hlavičky listu `4_Vetveni` jsou upravené.
- **1.8 Parametry pro generátor** (1_Identifikace, řádky 47–54): cílové skupiny (X), počet modulů, minut na modul (auto), úroveň pro generátor (auto), anotace pro platformu (max. 500 znaků) a počet jejích znaků (auto).
- **M1–M5, řádky 39–43**: Náročnost tématu, orientační rozsah F1 (auto), kontrola součtu fází (auto), **Otevřené problémy pro metodika** (hlášení ⚠ PRO METODIKA).
- **Nový list `14_Zdroje`**: soubory s rolí (Obsah / Pravidla pro tvorbu / Hotový kurz), co z nich brát, ověření a známé rozpory ve zdrojích.
- **13_Validace**: 19 nových automatických kontrol (č. 40–58) a 2 kvalitativní (č. 59–60). Souhrn se přesunul na řádek 66.
- `CIS_Pojmy`: F1 popsána jako výklad ke čtení („příručka") v rozsahu 5–10 min.

## Poznámky

- Pozor: změnily se hlavičky `4_Vetveni` (modré klíče). Agent a skilly, které čtou matrici v6, je potřeba sladit.
- Skilly `praktik-kurz` a `praktik-qa` (kánon, šablona) zatím počítají s F1 max. 5 min a s rozložením F1 5 · F2 4 · F3 3 · F4 3. Je třeba je aktualizovat na v7.0.
- Schéma výstupu generátoru na platformě (IMPULS, F1–F4, artefakt) se rozšiřuje; do té doby generátor vyrábí jen F1 (výukový blok) a otázky.
- Vzorce ve v7.0 nebyly přepočítány v Excelu. Při prvním otevření je Excel spočítá; doporučuji zkontrolovat list 13_Validace na prázdné matrici.

Vzniklo v projektu TQ23000092 PRAKTIK-AI (TA ČR, program SIGMA).
