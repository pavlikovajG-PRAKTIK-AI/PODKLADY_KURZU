# Videomanuál „Skilly PRAKTIK-AI v kartě Code“: průvodní text a seznam screenshotů

Cílová délka 3:00 až 3:30. Publikum: metodičky a metodici týmu, vysokoškolsky vzdělaní, Claude už používají. Tempo řeči +8 %, bez úvodních zdvořilostí. Každá scéna = jeden screenshot s jednou až dvěma anotacemi (šipka nebo rámeček). Titulní a závěrečný snímek nesou loga UJEP, TAČR (SIGMA) a PRAKTIK-AI.

Videomanuál ukazuje jedinou pracovní cestu: kartu Code v Claude Desktop. Zipy ve složce `zips` zůstávají záložní možností pro práci v chatu; ve videu se o nich mluví jednou větou a neukazují se.

## Průvodní text (voiceover)

**Scéna 1 (0:00–0:15) · titulní snímek**
Skilly PRAKTIK-AI. Pět malých balíčků instrukcí, které Claude načte, když tvoříte kurz. Nahrazují dlouhý prompt a hromadu dokumentů v projektu. Nainstalujete je jednou, používáte v každém kurzu.

**Scéna 2 (0:15–0:35) · přehled pěti skillů**
Praktik je rozcestník. Praktik-rozhovor s vámi projde čtrnáct otázek protokolu a zapíše zadání kurzu. Praktik-kurz vygeneruje kurz ve struktuře matrice v6: nejdřív kostru, po vašem souhlasu moduly. Praktik-qa kurz zkontroluje proti Definition of Done a formuláři oponenta. Praktik-export vyrobí Word v domácím stylu.

**Scéna 3 (0:35–0:50) · složka na Disku**
Všechno najdete na sdíleném Disku ve složce 09 Kurzy, podsložka PODKLADY_KURZU. Zkopírujte ji celou k sobě na počítač. Potřebujete z ní dvě věci: složku skills a složku scripts. Zipy vedle nich jsou záloha pro práci v chatu, tady je nepoužijeme.

**Scéna 4 (0:50–1:10) · instalace jedním dvojklikem**
Otevřete složku scripts a dvakrát klikněte na Nainstalovat skilly. Funguje to v Průzkumníku i v Total Commanderu. Skript zkopíruje pět skillů do vašeho uživatelského profilu, do složky tečka claude, skills. Claude Code tuhle složku sleduje, takže novou i opravenou verzi zachytí i v už rozdělané relaci. Restartovat nemusíte.

**Scéna 5 (1:10–1:30) · karta Code a Project folder**
V Claude Desktop přepněte na kartu Code. Ještě před první zprávou nastavte v řádku promptu Project folder a vyberte složku kurzu. Ta složka je Claudův pracovní prostor: soubory kurzu v ní rovnou vznikají a upravují se. Na cokoli mimo ni se vás Claude zeptá.

**Scéna 6 (1:30–1:55) · první zadání**
Přiložte zdrojový článek jako soubor. Napište: použij skill praktik-kurz, kód kurzu z katalogu, cílovou skupinu a tři autentické situace z vaší praxe. Bez těch tří situací skill kurz nezačne, protože autenticita je to jediné, co AI nevymyslí.

**Scéna 7 (1:55–2:15) · kostra kurzu**
Claude nejdřív vrátí kostru: identifikaci, GOALS, OBJECTIVES, blueprint artefaktu a názvy modulů s IMPULSY. Tady opravujte. Přepracování kostry stojí zlomek toho, co přepis hotových modulů. Když souhlasíte, napište „pokračuj“.

**Scéna 8 (2:15–2:35) · modul a kontrola**
Moduly přicházejí po jednom: IMPULS, F1 prezentace do pěti minut, F2 procvičení dialogickým formátem, F3 ověření, F4 část artefaktu. Před odesláním oponentovi napište „zkontroluj kurz“. Praktik-qa uloží report do stejné složky a vy řešíte jen označená místa.

**Scéna 9 (2:35–2:55) · export do Wordu**
„Exportuj do docx.“ Vedle markdownu vznikne Word s modrými záhlavími modulů, kurzivními závěry a zápatím s dedikací projektu. Nic nestahujete; soubor už leží ve složce kurzu. Export potřebuje Python s balíčkem python-docx, nainstalujete ho jednou.

**Scéna 10 (2:55–3:10) · co ve složce zůstane**
Na konci máte ve složce kurzu čtyři soubory: zápis rozhovoru, kurz v markdownu, QA report a Word pro oponenta a garanta. Všechny pojmenované kódem kurzu. Odsud je kopírujete na Disk.

**Scéna 11 (3:10–3:25) · závěr**
Pět skillů, jeden postup: rozhovor, kurz, kontrola, export. Návod v textové podobě a kontakt najdete ve stejné složce na Disku. Vzniklo v projektu TQ23000092 PRAKTIK-AI.

## Seznam screenshotů

Pořizujte v Claude Desktop na Windows, okno na celou obrazovku, měřítko 100 %, světlý režim, čeština rozhraní pokud je k dispozici (jinak angličtina, stejně pro všechny snímky). Rozlišení 1920 × 1080. Osobní údaje jiných osob v relacích rozmazat.

| # | Soubor | Co musí být vidět | Anotace |
|---|---|---|---|
| S01 | `S01_titul.png` | titulní grafika: název „Skilly PRAKTIK-AI v kartě Code“, loga UJEP, TAČR SIGMA, PRAKTIK-AI dole | žádná |
| S02 | `S02_prehled_skillu.png` | grafika: pět dlaždic praktik, praktik-rozhovor, praktik-kurz, praktik-qa, praktik-export se šipkami v pořadí postupu | popisky pod dlaždicemi |
| S03 | `S03_disk_slozka.png` | Google Disk, otevřená složka 09_Kurzy/PODKLADY_KURZU, viditelné podsložky skills, scripts, zips a soubor NAVOD | rámeček kolem skills a scripts |
| S04 | `S04_scripts_cmd.png` | Průzkumník, složka scripts, soubory `Nainstalovat_skilly.cmd` a `install_skills.ps1` | šipka na `Nainstalovat_skilly.cmd` |
| S05 | `S05_instalace_beh.png` | okno PowerShellu s pěti řádky „Nainstalovan skill: praktik…“ a závěrečnou hláškou | rámeček kolem pěti řádků |
| S06 | `S06_slozka_skills.png` | Průzkumník, `C:\Users\<jméno>\.claude\skills` s pěti složkami praktik* | rámeček kolem pěti složek |
| S07 | `S07_project_folder.png` | karta Code, řádek promptu s rozbaleným výběrem **Project folder**, vybraná složka kurzu | šipka na Project folder |
| S08 | `S08_lomitko_praktik.png` | karta Code, v řádku napsané `/praktik` s nabídkou pěti skillů | rámeček kolem nabídky |
| S09 | `S09_zadani.png` | karta Code, přiložené PDF (chip s názvem souboru), rozepsaná zpráva „Použij skill praktik-kurz. Kurz C1.5 … Tři situace z praxe: 1) … 2) … 3) …“ | šipka na přílohu, rámeček kolem tří situací |
| S10 | `S10_skill_nacten.png` | odpověď Claude, kde je vidět indikátor použití skillu praktik-kurz | šipka na indikátor |
| S11 | `S11_kostra.png` | odpověď s kostrou: tabulka IDENTIFIKACE, GOALS, tabulka modulů s IMPULSY, závěrečná otázka „Co měníte?“ | rámeček kolem tabulky modulů |
| S12 | `S12_modul1.png` | odpověď s modulem 1: nadpisy IMPULS, F1 PREZENTACE, F2 PROCVIČENÍ, F3 OVĚŘENÍ, F4 APLIKACE | rámeček kolem F4 |
| S13 | `S13_qa_report.png` | odpověď praktik-qa: verdikt, počty FAIL/WARN, tabulka s místem a změnou | rámeček kolem řádku verdiktu |
| S14 | `S14_export_docx.png` | zpráva „exportuj do docx“ a odpověď s cestou k vytvořenému `<KOD>_…_KURZ.docx` ve složce kurzu | šipka na cestu k souboru |
| S15 | `S15_word_nahled.png` | otevřený Word: modrý pruh „MODUL 1 …“, kurzivní IMPULS s modrým rámečkem, tabulka, zápatí s dedikací | rámeček kolem zápatí |
| S16 | `S16_slozka_kurzu.png` | Průzkumník, složka kurzu se soubory `<KOD>_Rozhovor.md`, `<KOD>_…_KURZ.md`, `<KOD>_QA_report.md`, `<KOD>_…_KURZ.docx` | rámeček kolem čtyř souborů |
| S17 | `S17_zaver.png` | závěrečná grafika: postup rozhovor → kurz → kontrola → export, odkaz na složku na Disku, kontakt, loga | žádná |

Pro scény 6 až 10 použijte reálný kurz z první vlny (např. C1.5 nebo C2.4), aby ukázka odpovídala katalogu. Text ve screenshotech musí být čitelný při 50 % náhledu; když ne, přibližte výřez.

## Výroba

Text voiceoveru namluvit podle skillu `pruvodni-text-prezentace` a `navodova-prezentace` (edge-tts nebo ElevenLabs, český hlas, tempo +8 %). Střih: statické snímky s anotacemi, přechody bez efektů, 1080p, MP4. Titulní snímek bílé pozadí kvůli logům. Uložit jako `PRAKTIK-AI_Skilly_navod.mp4` do 09_Kurzy/PODKLADY_KURZU.
