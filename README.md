# PODKLADY_KURZU: skilly a podklady pro tvorbu kurzů PRAKTIK-AI

Projekt TQ23000092 PRAKTIK-AI (UJEP + OU). Repozitář drží vše, co metodičky a metodici potřebují k tvorbě kurzů s Claudem: pět skillů, návod pro Claude Desktop, text k videomanuálu, aktuální podklady a analýzu původního promptu.

## Začněte tady

1. **Metodička / metodik:** čtěte [NAVOD_metodicky_Claude_Desktop.md](NAVOD_metodicky_Claude_Desktop.md). Zipy k nahrání jsou ve složce `zips`, skript pro kartu Code ve složce `scripts`.
2. **Správce projektu v Claude:** instrukce projektu v [Projektove_instrukce_v2.md](Projektove_instrukce_v2.md).
3. **Výroba videa:** [VIDEO_manual_text_a_screenshoty.md](VIDEO_manual_text_a_screenshoty.md).
4. **Proč to vzniklo:** [ANALYZA_promptu_v1_a_navrh_zmen.md](ANALYZA_promptu_v1_a_navrh_zmen.md).

## Skilly

| Skill | Účel | Reference uvnitř |
|---|---|---|
| `skills/praktik` | rozcestník postupu | přehled kroků |
| `skills/praktik-rozhovor` | protokol rozhovoru s autorem (14 otázek) → zadání kurzu | protokol, výpis katalogu |
| `skills/praktik-kurz` | generování kurzu ve struktuře matrice v6, kostra → moduly | kánon, číselníky NP/FMT/KRAUU, katalog, šablona, vzor A0601 |
| `skills/praktik-qa` | kontrola proti Definition of Done, formuláři oponenta a systémovým pravidlům | DoD, formulář, pravidla, kánon |
| `skills/praktik-export` | Word v domácím stylu (`scripts/export_docx.py`, potřebuje `python-docx`) | styl docx |

Postup: rozhovor → kurz → kontrola → export → oponentura → Definition of Done → katalog → nasazení dle vlny. Video, audio a grafiky vyrábí samostatný skill `av-materialy` (mimo tento repozitář).

## Složky

- `skills/` zdrojové skilly (každý má `SKILL.md` a `references/`).
- `zips/` totéž zabalené pro nahrání do Claude Desktop (Settings → Capabilities → Skills → Upload skill).
- `scripts/install_skills.ps1` instalace do `%USERPROFILE%\.claude\skills` pro kartu Code.
- `podklady/` kopie zdrojových dokumentů: katalog kurzů 2026-09, matrice v6.0, protokol rozhovoru, formulář oponenta, systémová pravidla, univerzální struktura kurzu, podklad pro IT v2, neurovědní principy, kurikulum v5.1, workflow tvorby matric, vzorový kurz A0601.

## Aktualizace

Změny dělejte ve `skills/`, pak spusťte `python scripts/build_zips.py`, commit, push a zkopírujte složku na Disk do `09_Kurzy/PODKLADY_KURZU`. Verzi uveďte v hlavičce návodu.

Kontakt: Jana Pavlíková, jana.pavlikova@ujep.cz.
