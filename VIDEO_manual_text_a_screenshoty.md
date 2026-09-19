# Videomanuál „Skilly PRAKTIK-AI v Claude Desktop“: průvodní text a seznam screenshotů

Cílová délka 3:00 až 3:30. Publikum: metodičky a metodici týmu, vysokoškolsky vzdělaní, Claude už používají. Tempo řeči +8 %, bez úvodních zdvořilostí. Každá scéna = jeden screenshot s jednou až dvěma anotacemi (šipka nebo rámeček). Titulní a závěrečný snímek nesou loga UJEP, TAČR (SIGMA) a PRAKTIK-AI.

## Průvodní text (voiceover)

**Scéna 1 (0:00–0:15) · titulní snímek**
Skilly PRAKTIK-AI. Pět malých balíčků instrukcí, které Claude načte, když tvoříte kurz. Nahrazují dlouhý prompt a hromadu dokumentů v projektu. Nainstalujete je jednou, používáte v každém chatu.

**Scéna 2 (0:15–0:35) · přehled pěti skillů**
Praktik je rozcestník. Praktik-rozhovor s vámi projde čtrnáct otázek protokolu a zapíše zadání kurzu. Praktik-kurz vygeneruje kurz ve struktuře matrice v6: nejdřív kostru, po vašem souhlasu moduly. Praktik-qa kurz zkontroluje proti Definition of Done a formuláři oponenta. Praktik-export vyrobí Word v domácím stylu.

**Scéna 3 (0:35–0:50) · složka na Disku**
Všechno najdete na sdíleném Disku ve složce 09 Kurzy, podsložka PODKLADY_KURZU. Pro chat potřebujete složku zips, pět souborů. Pro kartu Code složku skills a skript install.

**Scéna 4 (0:50–1:05) · Settings → Capabilities**
V Claude Desktop klikněte vlevo dole na své jméno, zvolte Settings a kartu Capabilities. Zapněte Code execution and file creation. Bez tohoto přepínače se skilly nenabídnou.

**Scéna 5 (1:05–1:25) · Upload skill**
Na téže kartě sjeďte k části Skills. Upload skill, vyberte praktik.zip. Zopakujte pro zbývající čtyři zipy. Seznam musí ukazovat pět skillů se zapnutým přepínačem.

**Scéna 6 (1:25–1:50) · první zadání v chatu**
Nový chat. Přiložte zdrojový článek jako soubor. Napište: použij skill praktik-kurz, kód kurzu z katalogu, cílovou skupinu a tři autentické situace z vaší praxe. Bez těch tří situací skill kurz nezačne, protože autenticita je to jediné, co AI nevymyslí.

**Scéna 7 (1:50–2:10) · kostra kurzu**
Claude nejdřív vrátí kostru: identifikaci, GOALS, OBJECTIVES, blueprint artefaktu a názvy modulů s IMPULSY. Tady opravujte. Přepracování kostry stojí zlomek toho, co přepis hotových modulů. Když souhlasíte, napište „pokračuj“.

**Scéna 8 (2:10–2:30) · modul a kontrola**
Moduly přicházejí po jednom: IMPULS, F1 prezentace do pěti minut, F2 procvičení dialogickým formátem, F3 ověření, F4 část artefaktu. Před odesláním oponentovi napište „zkontroluj kurz“. Praktik-qa vrátí report a vy řešíte jen označená místa.

**Scéna 9 (2:30–2:45) · export do Wordu**
„Exportuj do docx.“ Vznikne Word s modrými záhlavími modulů, kurzivními závěry a zápatím s dedikací projektu. Soubor pojmenovaný kódem kurzu uložte do složky kurzu na Disku.

**Scéna 10 (2:45–3:05) · karta Code, volitelně**
Když chcete, aby kurz vznikal rovnou ve složce na vašem disku, použijte kartu Code. Spusťte install_skills.ps1, otevřete složku kurzu a napište lomítko praktik. Soubory vznikají tam, kde je potřebujete.

**Scéna 11 (3:05–3:20) · závěr**
Pět skillů, jeden postup: rozhovor, kurz, kontrola, export. Návod v textové podobě a kontakt najdete ve stejné složce na Disku. Vzniklo v projektu TQ23000092 PRAKTIK-AI.

## Seznam screenshotů

Pořizujte v Claude Desktop na Windows, okno na celou obrazovku, měřítko 100 %, světlý režim, čeština rozhraní pokud je k dispozici (jinak angličtina, stejně pro všechny snímky). Rozlišení 1920 × 1080. Osobní údaje jiných osob v chatech rozmazat.

| # | Soubor | Co musí být vidět | Anotace |
|---|---|---|---|
| S01 | `S01_titul.png` | titulní grafika: název „Skilly PRAKTIK-AI v Claude Desktop“, loga UJEP, TAČR SIGMA, PRAKTIK-AI dole | žádná |
| S02 | `S02_prehled_skillu.png` | grafika: pět dlaždic praktik, praktik-rozhovor, praktik-kurz, praktik-qa, praktik-export se šipkami v pořadí postupu | popisky pod dlaždicemi |
| S03 | `S03_disk_slozka.png` | Google Disk, otevřená složka 09_Kurzy/PODKLADY_KURZU, viditelné podsložky zips, skills, scripts a soubor NAVOD | rámeček kolem zips a skills |
| S04 | `S04_settings_menu.png` | Claude Desktop, rozbalené menu po kliknutí na jméno vlevo dole, položka Settings | šipka na Settings |
| S05 | `S05_capabilities.png` | Settings, karta Capabilities, přepínač Code execution and file creation zapnutý | rámeček kolem přepínače |
| S06 | `S06_skills_sekce.png` | tatáž karta, část Skills s tlačítkem Upload skill, zatím bez skillů nebo s výchozími | šipka na Upload skill |
| S07 | `S07_vyber_zipu.png` | systémový dialog výběru souboru, složka zips s pěti zipy, vybraný praktik.zip | rámeček kolem pěti souborů |
| S08 | `S08_skills_nahrane.png` | část Skills se všemi pěti skilly praktik* a zapnutými přepínači | rámeček kolem seznamu |
| S09 | `S09_novy_chat_zadani.png` | nový chat, přiložené PDF (chip s názvem souboru), rozepsaná zpráva „Použij skill praktik-kurz. Kurz C1.5 … Tři situace z praxe: 1) … 2) … 3) …“ | šipka na přílohu, rámeček kolem tří situací |
| S10 | `S10_skill_nacten.png` | odpověď Claude, kde je vidět indikátor použití skillu praktik-kurz (řádek „Using skill“ nebo rozbalený krok) | šipka na indikátor |
| S11 | `S11_kostra.png` | odpověď s kostrou: tabulka IDENTIFIKACE, GOALS, tabulka modulů s IMPULSY, závěrečná otázka „Co měníte?“ | rámeček kolem tabulky modulů |
| S12 | `S12_modul1.png` | odpověď s modulem 1: nadpisy IMPULS, F1 PREZENTACE, F2 PROCVIČENÍ, F3 OVĚŘENÍ, F4 APLIKACE | rámeček kolem F4 |
| S13 | `S13_qa_report.png` | odpověď praktik-qa: verdikt, počty FAIL/WARN, tabulka s místem a změnou | rámeček kolem řádku verdiktu |
| S14 | `S14_export_docx.png` | zpráva „exportuj do docx“ a odpověď s odkazem na stažení souboru `<KOD>_…_KURZ.docx` | šipka na soubor |
| S15 | `S15_word_nahled.png` | otevřený Word: modrý pruh „MODUL 1 …“, kurzivní IMPULS s modrým rámečkem, tabulka, zápatí s dedikací | rámeček kolem zápatí |
| S16 | `S16_code_install.png` | Průzkumník, složka scripts, kontextové menu na install_skills.ps1 s položkou Spustit v PowerShellu; nebo okno PowerShellu s výpisem „Nainstalován skill: praktik…“ | šipka na položku |
| S17 | `S17_code_tab.png` | Claude Desktop, karta Code, otevřená složka kurzu, v řádku napsané `/praktik` s nabídkou skillů | rámeček kolem nabídky |
| S18 | `S18_zaver.png` | závěrečná grafika: postup rozhovor → kurz → kontrola → export, odkaz na složku na Disku, kontakt, loga | žádná |

Pro scény 6 až 9 použijte reálný kurz z první vlny (např. C1.5 nebo C2.4), aby ukázka odpovídala katalogu. Text ve screenshotech musí být čitelný při 50 % náhledu; když ne, přibližte výřez.

## Výroba

Text voiceoveru namluvit podle skillu `pruvodni-text-prezentace` a `navodova-prezentace` (edge-tts nebo ElevenLabs, český hlas, tempo +8 %). Střih: statické snímky s anotacemi, přechody bez efektů, 1080p, MP4. Titulní snímek bílé pozadí kvůli logům. Uložit jako `PRAKTIK-AI_Skilly_navod.mp4` do 09_Kurzy/PODKLADY_KURZU.
