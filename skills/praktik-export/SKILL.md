---
name: praktik-export
description: Exportuje hotový kurz PRAKTIK-AI (soubor KOD_Nazev_KURZ.md) do Wordu (.docx) v domácím stylu platformy – modrá záhlaví modulů #1F5C99, Arial 11, kurzivní závěry s modrým rámečkem, zápatí se zdrojem a dedikací TQ23000092. Použij, když autor chce „export do docx/Wordu“, „poslat oponentovi“, „vygenerovat dokument“, „udělej z toho Word“, nebo když praktik-qa skončí verdiktem „připraven k oponentuře“. Exportuje až po schválení obsahu; obsah nemění. Výstup projektu je vždy docx, nikdy PDF ani JSON.
---

# praktik-export: docx z kurzu

Vstup je Markdown kurzu ve struktuře vzoru A0601 (sekce 1–12, moduly `# MODUL n — Název` s `## IMPULS`, `## F1…F4`, capstone, testy, zdroje). Výstup jde do složky kurzu vedle zdrojového `.md`.

## Postup

1. Ověř, že soubor existuje a že autor obsah schválil (nebo že QA skončilo bez FAIL). Když ne, řekni to a nabídni `praktik-qa`.
2. Spusť `python "${CLAUDE_SKILL_DIR}/scripts/export_docx.py" <cesta_k_md> [--out <cesta_docx>] [--zdroj "text do zápatí"]`. Cestu ke skriptu piš vždy takto absolutně: skript leží ve složce skillu (`%USERPROFILE%\.claude\skills\praktik-export\scripts\`), ne ve složce kurzu, kterou má autor otevřenou jako Project folder. Skript potřebuje `python-docx`; když ohlásí, že chybí, spusť `pip install python-docx` a export zopakuj. Do `--zdroj` dej zdrojový materiál kurzu (článek, kapitola), jak ho uvádí autor.
3. Zkontroluj výsledek: počet modulů (modré pruhy), tabulky, kurzivní bloky, zápatí. Když skript selže, uveď chybu doslova; oprav vstupní Markdown, pokud chyba není ve skriptu.
4. Pojmenování: `<KOD>_<Nazev>_KURZ.docx`, stejná složka jako `.md`. Předchozí verzi přepiš jen na výslovné přání, jinak přidej `_v2`.
5. Nahlaš cestu a dvě čísla: počet modulů a počet zdrojů. Nic víc.

## Styl docx (závazný, detail v `references/styl_docx.md`)

- Písmo Arial 11 pt, odstavce F1 zarovnané do bloku.
- Název kurzu: Arial 20 tučně, modrá #1F5C99. Podtitul kurzívou šedě.
- Záhlaví modulů (`# MODUL n`, `# CAPSTONE`, `# ZÁVĚREČNÝ TEST`, `# ZDROJE`): tučné, bílé písmo na modrém podkladu #1F5C99.
- Nadpisy sekcí (`## …`): Arial 13 tučně, modrá; nadpisy fází F1–F4 se spodní linkou.
- Kurzivní odstavce (IMPULS, „Zapamatujte si“, instrukce pro agenta): kurzíva, odsazení zleva 0,8 cm, světle modrý levý rámeček #9DC3E6.
- Poznámka pro garanta (`> ⚠ …`): žlutý podklad, zlatý levý rámeček.
- Tabulky: Table Grid, záhlaví tučně na #DEEAF6, písmo 10 pt.
- Zápatí: „Zdroj: <materiál> · Vzniklo v projektu TQ23000092 PRAKTIK-AI (TA ČR, program SIGMA) · <KOD> v<verze>, <datum> | Strana n“.

## Pravidla

Export nic nepřepisuje ani nevylepšuje. Když v Markdownu chybí sekce, docx ji prostě neobsahuje; napiš to autorovi jednou větou. Diakritika a české uvozovky zůstávají. Žádné PDF, žádný JSON; když si někdo JSON vyžádá pro IT, odkaž ho na vedoucí metodického týmu.
