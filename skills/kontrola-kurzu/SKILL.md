---
name: kontrola-kurzu
description: Zkontroluje kurz PRAKTIK-AI tak, jak ho vygenerovala platforma test.praktik.ujep.cz, proti schválenému KURZ.md a originálním zdrojům (předpisy, studie, DOI) a uloží report do složky kurzu. Použij, když uživatelka chce „zkontrolovat kurz na platformě“, „zhodnotit hotový kurz“, „podívat se na výsledek na platformě“, „projít kurz po vygenerování“, pošle odkaz test.praktik.ujep.cz/courses/… nebo /modules/…, nebo chce zopakovat kontrolu po opravách. Pro kontrolu KURZ.md před nahráním použij praktik-qa.
---

# kontrola-kurzu: kurz na platformě proti zdrojům

Kontroluje **výsledek po vygenerování**. `praktik-qa` kontroluje KURZ.md **před nahráním**; obě kontroly se doplňují. Kurz se na platformu dostává tak, že ho platforma z KURZ.md vygeneruje pomocí AI a autor výstup ručně doopraví přímo v platformě. Obrázky se vkládají ručně.

## Zásady

1. **Kurz nikdy neprocházej v prohlížeči jako uživatel.** Průchod zanechá stopu: platforma kurz může vzít jako dokončený a uživatel do něj ztratí přístup. Obsah čti jen přes veřejné API skriptem níže (bez přihlášení). Části, které API bez přihlášení nevydá (Test, nahraný soubor KURZ.md), uveď v revizním protokolu jako nezkontrolované.
2. **Odchylka metadat není automaticky chyba.** Autor mohl při zadávání kurzu rozhodnout jinak než KURZ.md. Metadata uváděj jako přehled porovnání platforma × KURZ.md, bez hodnocení; chybou je jen rozpor uvnitř platformy (např. kompetence modulu, kterou kurz nemá).
3. **Normativní text se ověřuje proti oficiálnímu znění**, ne proti KURZ.md (směrnice z webu instituce, ne pracovní verze).
4. Řiď se pravidly práce se zdroji z `OSOBNOST.md`: nic nepřidávat, nezesilovat, u každého nálezu místo a citace zdroje.
5. Na platformě ani v KURZ.md nic neměň. Výstupem je report.

## Postup

1. **Najdi kurz a stáhni ho:**
   `python -I "${CLAUDE_SKILL_DIR}/scripts/export_kurz.py" <ID> -o <scratchpad>/export_<KOD>.md`
   nebo `--najdi <KOD>` (hledá kód v názvu nahraného souboru). ID je číslo z adresy `test.praktik.ujep.cz/courses/ID`. Export obsahuje metadata, příručky očíslované po odstavcích (`M1-1`, `M1-2` …, obrázky `M1-obr01`) a otázky k procvičování se správnou odpovědí. Přečti ho celý.
2. **Soupis zdrojů:** KURZ.md ve složce kurzu (přečti celý), rešerše, oficiální znění předpisů, které kurz vykládá. **Uveď rozdíl verzí:** datum nahrání na platformu (pole `updated_at` a datum souboru) proti datu místního KURZ.md. Když se liší, napiš, že srovnáváš s místní verzí, a co se mezi verzemi prokazatelně změnilo (např. anotace).
3. **Metadata:** tabulka platforma × KURZ.md (oddíl „Údaje pro založení kurzu“ nebo 1 IDENTIFIKACE): anotace, cílová skupina, povinnost, EQF, délka, obtížnost, typ, blok, KRAUU, Bloom, průřezové obory, počet modulů. Zvlášť: KRAUU a Bloom modulů, které nejsou ve výběru kurzu; počet neurovědních principů u modulů proti KURZ.md.
4. **Věrnost obsahu:** příručky a otázky věta po větě proti KURZ.md (F1, větvení, modelové situace, klíče F3):
   - věty, které generátor **přidal** (vysvětlení, hodnocení, údaje), a věty, které **posunul** (modalita „může“ → „pomáhá“, „podle autorů naznačují“ → tvrzení, „vysoká statistická síla“ přenesená na jiný objekt),
   - **vynechané** výhrady a podmínky,
   - porušení antipatterns z oddílu 8 KURZ.md (zakázaná čísla, studie bez statusu),
   - **poznámky pro autora v textu pro účastníky** („podklady kurzu neuvádějí“, „čísla odstavců je třeba ověřit“),
   - označení modelových situací,
   - české překlady v uvozovkách, které vypadají jako citace.
5. **Předpisy:** u každého odkazu na článek nebo odstavec ověř číslo i obsah v oficiálním znění.
6. **Reference:** DOI přes `https://api.crossref.org/works/<DOI>`, preprinty přes `https://export.arxiv.org/api/query?id_list=<id>`. Stažené soubory ukládej do samostatné podsložky scratchpadu a Python spouštěj s `-I`.
7. **Otázky k procvičování:** správný klíč i distraktory proti výkladu a zdroji.
8. **Jazyk:** v reportu jen hlavní nálezy (dublety, rysy AI stylu, nadpisy). Úplnou korekturu skillem `cestina-korektura` nad exportem nabídni; když ji uživatelka chce, přidej ji do téhož souboru jako samostatný oddíl.
9. **Report** ulož do složky kurzu jako `yyyy_mm_dd_<KOD>_Report.md` (formát níže).
10. **Kontrola věrnosti reportu:** spusť skill `kontrola-vernosti` naslepo (agent dostane report a zdroje, ne tvé úvahy). Každý nález ověř ve zdroji, potvrzené zapracuj a v revizním protokolu uveď, co se opravilo a co zamítlo.

## Opakovaná kontrola (po opravách)

Když ve složce kurzu je starší report: stáhni nový export, projdi body z oddílů „K opravě“ a „Posuny“ starého reportu a ke každému napiš **opraveno / zůstává / změněno jinak** s citací nového znění. Nové nálezy uveď zvlášť. Nový report ulož s dnešním datem, starý nepřepisuj.

## Formát reportu

```
# <KOD> <Název>: hodnocení kurzu na platformě
Datum · Kurz (URL, ID modulů, stav) · Zdroje pro porovnání (verze a datum)
## Obsah
1. Celkové hodnocení            (3–5 vět, nejzávažnější nález)
2. K opravě (věcné chyby)       (tabulka: # | kde | platforma | zdroj | proč je to chyba)
3. Posuny a doplňky proti zdroji (tabulka: kde | platforma | zdroj | posun)
4. Poznámky pro autora v textu pro účastníky
5. Jazyk (hlavní nálezy)
6. Metadata: přehled porovnání  (tabulka: pole | KURZ.md | platforma)
7. Stav zdrojového souboru KURZ.md (otevřené úkoly, placeholdery)
8. Ověření citovaných zdrojů
9. Podněty pro IT (nálezy, které nejsou chybou autora, ale generátoru)
10. Revizní protokol           (co zkontrolováno, co ne, rozdíl verzí, výsledek kontroly věrnosti)
```

Místa označuj modulem a nadpisem oddílu (a číslem odstavce z exportu), u KURZ.md číslem řádku. Citace doslovně. Celý text reportu česky, věcně, bez rysů AI stylu.

## Známé vlastnosti platformy (stav 18. 10. 2026)

- Generátor přiděluje každému modulu jen jeden neurovědní princip a někdy kompetence KRAUU nebo úrovně Blooma mimo výběr kurzu.
- Úvodní nadpisy modulů se liší modul od modulu („Začněme otázkou“, „Téma v realitě“ …).
- Generátor vkládá do textu pro účastníky poznámky typu „podklady kurzu neuvádějí“.
- Část Test byla u modulů A0601 prázdná (endpoint `modules/{id}/assessment` po přihlášení vrací „Žádná assessment otázka pro tento modul“; bez přihlášení ho API nevydá); capstone a artefakt platforma zatím nemá. To jsou výchozí stav první vlny testování, ne nálezy.
- Mediální přílohy se značí `<KOD>-M<n>-<NN>-<typ>-<popis>.<ext>` s pořadím v modulu; v exportu zkontroluj, zda počet a pořadí obrázků odpovídá sekci 10 KURZ.md.
