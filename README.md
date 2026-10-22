# PODKLADY_KURZU: skilly a podklady pro tvorbu kurzů PRAKTIK-AI

Projekt TQ23000092 PRAKTIK-AI (UJEP + OU). Repozitář drží vše, co metodičky a metodici potřebují k tvorbě kurzů s Claudem: šest skillů, návody pro Claude Desktop, text k videomanuálu a aktuální podklady.

## Začněte tady

1. **Metodička / metodik:** stručný návod [2026_10_18_NavodMetodikyTvorbaKurzu.docx](2026_10_18_NavodMetodikyTvorbaKurzu.docx) (verze 2.0), instalace a práce v kartě Code v [NAVOD_metodicky_Claude_Desktop.md](NAVOD_metodicky_Claude_Desktop.md). Pracovní cesta je karta Code: instalační skript je ve složce `scripts`, zdrojové skilly ve složce `skills`. Zipy ve složce `zips` jsou záloha pro práci v chatu.
2. **Výroba videa:** [VIDEO_manual_text_a_screenshoty.md](VIDEO_manual_text_a_screenshoty.md).

## Skilly

| Skill | Účel | Reference uvnitř |
|---|---|---|
| `skills/praktik` | rozcestník postupu | přehled kroků |
| `skills/praktik-rozhovor` | protokol rozhovoru s autorem (14 otázek) → zadání kurzu | protokol, výpis katalogu |
| `skills/praktik-kurz` | generování kurzu ve struktuře Matrice v7.2, kostra → moduly | kánon, číselníky NP/FMT/KRAUU, katalog, šablona, vzor A0601 |
| `skills/praktik-qa` | kontrola proti Definition of Done, formuláři oponenta a systémovým pravidlům | DoD, formulář, pravidla, kánon |
| `skills/kontrola-kurzu` | kontrola kurzu vygenerovaného na platformě proti KURZ.md a originálním zdrojům | – |
| `skills/praktik-export` | Word v domácím stylu (`skills/praktik-export/scripts/export_docx.py`, po instalaci `%USERPROFILE%\.claude\skills\praktik-export\scripts\`; potřebuje `python-docx`) | styl docx |

Postup: rozhovor → kurz → kontrola → export → oponentura → Definition of Done → katalog → nasazení dle vlny. Video, audio a grafiky vyrábí samostatný skill `av-materialy` (mimo tento repozitář).

## Složky

- `skills/` zdrojové skilly (každý má `SKILL.md` a `references/`).
- `zips/` totéž zabalené pro nahrání do Claude Desktop (Settings → Capabilities → Skills → Upload skill); záložní cesta pro práci v chatu.
- `scripts/Nainstalovat_skilly.cmd` instalace dvojklikem (volá `install_skills.ps1`), `scripts/install_skills.ps1` totéž z PowerShellu — obojí kopíruje do `%USERPROFILE%\.claude\skills` pro kartu Code.
- `scripts/build_zips.py` přebalí `skills/` do `zips/`; pusťte po každé změně skillu.
- `MatriceVer7/` platná Matrice kurzu v7.2 a prompt Metodický architekt v3.0.
- `podklady/` kopie zdrojových dokumentů: návod Jak vytvořit kurz (verze 3, Matrice 7.2), katalog kurzů 2026-09, kurikulum v5.1, protokol rozhovoru, systémová pravidla, neurovědní principy.

## Aktualizace

Změny dělejte ve `skills/`, pak spusťte `python scripts/build_zips.py`, commit, push a zkopírujte složku na Disk do `09_Kurzy/PODKLADY_KURZU`. Verzi uveďte v hlavičce návodu.

Kontakt: Jana Pavlíková, jana.pavlikova@ujep.cz.
