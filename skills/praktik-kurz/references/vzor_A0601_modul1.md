# Vzor: kurz A0601 „Vývoj dětského mozku v éře AI“ (výběr)

Referenční výstup skillu. Ukazuje hlavičku kurzu (sekce 1–8), kompletní modul 1, capstone, artefakt, rubriku a formát zdrojů. Plný kurz: `09_Kurzy/BrainDevelopment/A0601_VyvojDetskehoMozku_KURZ.md` (50 tis. znaků, obsahuje i moduly 2–5, procvičovací a závěrečný test a skript videa).

Čti jen pasáž, kterou právě potřebuješ: hlavičku před psaním kostry, modul 1 před psaním prvního modulu, rubriku před psaním rubriky.

---

# VÝVOJ DĚTSKÉHO MOZKU V ÉŘE AI

### Co se děje v hlavě žáka 6–15 let — a co s tím dělá umělá inteligence

**Kompletní textový základ kurzu dle PRAKTIK-AI Matrice v6.0**
Verze 1.0 | 28. 8. 2026 | Autor podkladu: Jana Pavlíková (jana.pavlikova@ujep.cz)

> ⚠ **K potvrzení garantem:** pracovní kód kurzu **A0601** (Blok A — kontext a principy AI-asistovaného učení; ověřit kolizi s kurikulem), EQF 7, délka 90 min. Vše ostatní vyplněno bez placeholderů.

---

## 1 IDENTIFIKACE

| Klíč | Hodnota |
|---|---|
| Interní kód (DB) | A0601 *(pracovní — potvrdí garant)* |
| Zobrazovací kód (UI) | A6 |
| URL slug | vyvoj-detskeho-mozku-v-ere-ai |
| Plný název kurzu (certifikát) | Vývoj dětského mozku v éře AI: neurovědní základy pro pedagogickou praxi |
| Řešený problém | Pedagogové rozhodují o zapojení AI a digitálních technologií u žáků 6–15 let intuitivně — bez znalosti toho, jak vyvíjející se mozek na tyto nástroje reaguje. Výsledkem jsou dva zrcadlové omyly: plošné zákazy, které promarní reálné příležitosti, a nekritické nasazení, které u dětí buduje kognitivní dluh místo kompetencí. |
| Výstup kurzu (artefakt) | **Akční plán AI hygieny** — vývojově ukotvený plán zdravého zapojení AI a digitálních technologií pro konkrétní třídu / věkovou skupinu, budovaný po sekcích v F4 každého modulu. |
| Blok | A — Kontext a principy AI-asistovaného učení |
| Verze kurzu | 1.0 |
| Délka celkem (min) | 90 (5 × 15 min modul + 15 min capstone) |
| Úroveň | Základní — nevyžaduje předchozí znalost neurovědy |
| Povinnost | Doporučený |
| EQF úroveň | 7 |
| ECTS (orientační) | 0,1 |
| Prerekvizity (kódy) | žádné |
| Navazující kurzy (kódy) | kurz *Mozek a jazyk* (sesterský, Blok A); kurzy bloku B (redesign zadání a hodnocení) |
| Typ kurzu | Obecný — platí pro všechny obory; průřezový přesah do bloku C |
| Skip povolen? | Ano — deklarativní moduly M1, M2, M4 (práh 80 %); M3, M5 a všechny F4 přeskočit nelze |
| Při neúspěchu skip-testu | Uživatel prochází modul standardně |
| Styl psaní | Konverzační (vykání) + narativní — situace z reálné třídy; analytický tam, kde jde o evidenci |
| Typické rozložení fází (min) | F1: 5 | F2: 4 | F3: 3 | F4: 3 |

**Anchor text:**
*Mozek vašich žáků je staveniště, které se zavře až kolem pětadvacítky. Umělá inteligence na to staveniště právě dorazila — bez ohlášení a bez stavebního dozoru. Tento kurz vám dá to, co dozor potřebuje: znalost plánů stavby a evidenci o tom, co ji posiluje a co podkopává.*

**Informační nota:**
Kurz nevyžaduje předchozí znalost neurovědy ani AI. Je určen pedagogům všech aprobací, mentorům a studentům učitelství, kteří pracují se žáky 6–15 let nebo jejich učitele připravují. Zařazen v bloku A jako kontextový kurz; doporučeno absolvovat před kurzy bloků B a C.

**Text certifikátu:**
Absolvent/ka vysvětlí klíčové procesy zrání mozku ve věku 6–15 let a jejich důsledky pro učení, analyzuje dopady AI a digitálních technologií na vyvíjející se kognitivní a sociálně-emoční funkce s oporou o výzkumnou evidenci, kriticky zhodnotí vhodnost konkrétního AI nástroje pro danou vývojovou fázi a navrhne vývojově ukotvený akční plán AI hygieny pro konkrétní skupinu žáků.

---

## 2 GOALS (výkonové cíle kurzu)

| ✓ | Bloom | GOAL | Pokryto v modulech |
|---|---|---|---|
| X | 2 — Porozumět | **G2:** Vysvětlí klíčové procesy zrání mozku ve věku 6–15 let (synaptický pruning, myelinizace, dozrávání prefrontální kůry, senzitivní periody) a jejich důsledky pro učení. | M1, M2 |
| X | 4 — Analyzovat | **G4:** Porovná dopady konkrétních způsobů užívání AI a digitálních technologií na vyvíjející se kognitivní funkce s oporou o výzkumnou evidenci, včetně jejích limitů. | M2, M3, M4 |
| X | 5 — Hodnotit | **G5:** Kriticky zhodnotí vhodnost AI nástroje či praktiky pro danou vývojovou fázi a své stanovisko zdůvodní evidencí, nikoli dojmem. | M3, M4, M5 |
| X | 6 — Tvořit | **G6:** Navrhne akční plán AI hygieny pro konkrétní skupinu žáků 6–15 let, ukotvený ve vývojové neurovědě a proveditelný v reálné škole. | M1–M5 (F4), Capstone |

## 3 OBJECTIVES (cíle modulů)

| ID | Text OBJECTIVE | Typ | Testovatelný? | Modul | Vazba na GOAL |
|---|---|---|---|---|---|
| A0601-O1 | Popíše tři klíčové procesy zrání mozku 6–15 let (synaptický pruning, myelinizace, dozrávání prefrontální kůry) a vysvětlí, proč záleží na senzitivních periodách. | znalostní | ano | M1 | G2 (Bloom 2) |
| A0601-O2 | Vysvětlí limity pozornosti a pracovní paměti školního dítěte a analyzuje, jak konkrétní prvky digitálního prostředí (notifikace, multitasking, přítomnost telefonu) tyto limity zatěžují. | analytický | ano | M2 | G2, G4 (Bloom 4) |
| A0601-O3 | Rozliší na konkrétních příkladech, kdy AI funguje jako opora učení (scaffold) a kdy jako náhrada myšlení (kognitivní offloading), s odkazem na výzkumnou evidenci. | analytický | ano | M3 | G4 (Bloom 4) |
| A0601-O4 | Posoudí rizika a příležitosti AI společníků a sociálních technologií pro sociálně-emoční vývoj dospívajících a zdůvodní, kde vede červená linie. | hodnoticí | ano | M4 | G5 (Bloom 5) |
| A0601-O5 | Navrhne pro konkrétní věkovou skupinu zásady zdravého zapojení AI do učení, opřené o mezinárodní doporučení a evidenci. | tvůrčí | ano (rubrikou) | M5 | G5, G6 (Bloom 6) |

## 4 Větvení dle profilu uživatele

| Modul | Akademik | Mentor / uvádějící učitel | Student učitelství |
|---|---|---|---|
| M1–M5 | Příklady z přípravy budoucích učitelů; důraz na čtení primárních studií a metodologické limity | Příklady z hospitací a vedení začínajících kolegů; důraz na argumentaci vůči rodičům a vedení školy | Příklady z praxí; důraz na první samostatná rozhodnutí a sebeobranu proti „všichni to tak dělají" |
| Capstone | Plán pro seminární skupinu / kurz didaktiky | Plán pro svou třídu + doporučení pro sborovnu | Plán pro třídu z praxe (fiktivní zadání, pokud praxe neběží) |

## 5 Neurovědní principy kurzu (globální výběr)

Zaškrtnuto: **NP-02** (distribuované opakování — skip-testy a opakující se mikrotesty), **NP-03** (aktivní vybavování — F3 každého modulu), **NP-04** (žádoucí obtíže — M3 je na nich postaven obsahově i formálně), **NP-06** (duální kódování — každý modul má grafiku), **NP-07** (kognitivní zátěž — F1 max 5 minut, jeden koncept na obrazovku), **NP-09** (efekt generování — FMT-VLA a FMT-PRO v F2), **NP-10** (testovací efekt — F3 + závěrečný test), **NP-11** (predikční chyba — IMPULSy postavené na překvapivých datech), **NP-13** (pozornost a pracovní paměť — obsah M2), **NP-15** (metakognice — reflexe v F4 a capstone), **NP-18** (okamžitá zpětná vazba — AI hodnotí F2/F3 ihned), **NP-20** (schémata — kurz staví na metafoře staveniště, k níž se moduly vracejí).

## 6 AI principy kurzu

Zaškrtnuto: AI jako partner v dialogu (FMT-SOK v M2, M5) · AI jako scaffold, ne náhrada (obsahová páteř M3) · Kritické hodnocení AI výstupů · Rozpoznání halucinací a ověřování (práce se zdroji v F2 M3) · AI jako hodnotitel výstupu (F3, rubrika) · Sokratovský dialog s AI · AI jako zrcadlo pro reflexi (capstone).

## 7 KRAUU kompetence

Zaškrtnuto: **2.2** (poznává vzdělávací potřeby — vývojová specifika), **2.3** (podporuje zvídavost a motivaci — dopaminové učení, flow), **2.4** (efektivně vede výuku a zjišťuje porozumění), **3.3** (uspořádání fyzického a digitálního prostředí), **5.2** (spolupráce s rodiči — komunikační sekce artefaktu), **6.2** (odpovědná práce s informacemi), **6.3** (duševní zdraví a psychohygiena — spánek, AI společníci).

## 8 Vzory a antipatterns pro agenta

| Typ | Pravidlo | Zdůvodnění | Kde |
|---|---|---|---|
| MUSÍ | U každého výzkumného zjištění uvést zdroj a tam, kde existují nezdařené replikace či kritika, zmínit je jednou větou. | Kurz učí kritickou práci s evidencí — nesmí sám vytvářet iluzi jistoty. | globálně |
| MUSÍ | Držet metaforu „mozek = staveniště" jako návratové schéma všech modulů (NP-20). | Jednotné schéma snižuje kognitivní zátěž a zvyšuje retenci. | globálně |
| MUSÍ | V F2/F3 poskytovat zpětnou vazbu okamžitě a konkrétně: co je správně, co chybí, jedna otázka k domyšlení (NP-18). | Rychlá ZV opraví chybu před zafixováním. | globálně |
| MUSÍ | V sokratovském dialogu (FMT-SOK) klást otázky a NIKDY neprozradit cílový závěr dřív, než ho uživatel sám zformuluje aspoň částečně. | Efekt generování; smysl formátu. | M2, M5, závěrečný test |
| NESMÍ | Používat katastrofické formulace typu „AI ničí dětské mozky" ani bagatelizující „je to jen nástroj". | Kurz stojí na vyváženosti; obě zkratky podkopávají GOAL G5. | globálně |
| NESMÍ | Vydávat preprint (Kosmyna et al.) za recenzovanou jistotu — vždy označit status evidence. | Reliabilita obsahu je nepodkročitelná. | M3 |
| NESMÍ | Doporučovat konkrétní komerční produkty; mluví se o kategoriích nástrojů a kritériích. | Neutralita platformy; kritéria přežijí produkty. | M5, capstone |
| NESMÍ | Zadávat věkové normy jako přesné hranice („ve 12 letech mozek…"); vždy rámovat jako typická rozpětí s individuální variabilitou. | Vývojová neurověda popisuje trajektorie, ne termíny. | globálně |

---

---

# MODUL 1 — Stavba, která trvá čtvrt století

**Délka:** 15 min | **OBJECTIVES:** A0601-O1 | **Skip:** ano (80 %) | **Vazba na GOALS:** G2
**Neurovědní principy v modulu:** NP-06 (grafika zrání mozku v F1), NP-20 (založení schématu „staveniště"), NP-03 + NP-10 (F3), NP-11 (IMPULS — překvapivý fakt).

## IMPULS

*Mozek vašeho jedenáctiletého žáka má víc synapsí než ten váš. A přesto se právě teď rozhoduje, kterých se zbaví — podle toho, co s ním děláte vy, rodiče a jeho telefon.*

## F1 PREZENTACE (5 min)

Mozek dítěte mezi 6. a 15. rokem není malá verze dospělého mozku. Je to stavba v plném provozu, na níž běží tři procesy současně.

**1. Synaptický pruning — prořezávání.** Dětský mozek vytváří obrovský nadbytek synaptických spojení a poté je selektivně redukuje podle principu *use it or lose it*: spoje, které se používají, sílí; nepoužívané zanikají. Longitudinální MRI studie Gogtayové a kolegů (PNAS, 2004) ukázala, že šedá kůra zraje „odzadu dopředu" — nejprve senzorické a motorické oblasti, naposledy prefrontální kůra. Zkušenost dítěte tedy doslova spoluurčuje architekturu jeho mozku. To, čemu žák věnuje hodiny denně — čtení, sport, hraní, scrollování — není jen „trávení času". Je to hlasování o tom, které okruhy zůstanou.

**2. Myelinizace — zrychlování.** Axony se postupně obalují myelinem, který násobí rychlost vedení signálu. Proto starší žáci zvládají rychlejší, komplexnější operace — a proto mladší žáci objektivně *nemohou* některé věci dělat rychle, i kdyby chtěli.

**3. Dozrávání prefrontální kůry — dispečink přijde naposled.** Prefrontální kortex (PFC) — sídlo plánování, sebekontroly, odkládání odměny a pracovní paměti — dozrává jako poslední, do zhruba 25 let. Exekutivní funkce, které PFC hostí (inhibice, pracovní paměť, kognitivní flexibilita — Diamond, 2013), jsou u školáka rozestavěné. Důsledek pro éru AI: **žák 6–15 let nemá hotový vnitřní systém, který by sám reguloval lákavé technologie.** Sebekontrolu, kterou po něm chceme, mu musí zvenčí dodat prostředí — tedy my.

**A senzitivní periody?** Pro některé funkce (jazyk, čtení) existují okna zvýšené plasticity, kdy se mozek danou dovednost učí nejsnáze. Okna se nezabouchávají naráz — ale co do nich vložíme, staví se levněji a drží déle.

*Zapamatujte si: use it or lose it — architektura mozku 6–15 se staví z toho, co dítě opakovaně dělá. A stavební dozor (PFC) dorazí na stavbu jako poslední.*

**Větvení:** Akademik — Gogtay et al. jako ukázka longitudinálního designu (13 dětí, MRI po 2 letech, 8–10 let sledování): co z toho plyne a co ne. Mentor — jak vysvětlit pruning rodičům na třídní schůzce jednou větou. Student — proč „on je prostě líný" bývá neurovývojově nesmyslná věta.

## F2 PROCVIČENÍ (4 min) — FMT-MTC (matching)

*Instrukce pro agenta: Předlož párování, po odeslání okamžitě vyhodnoť, u chyb vysvětli jednou větou proč.*

Přiřaďte proces k důsledku pro praxi:

| Proces | | Důsledek pro praxi |
|---|---|---|
| 1. Synaptický pruning | A | Mladší žák potřebuje na tutéž operaci objektivně více času — nejde o lenost. |
| 2. Myelinizace | B | Pravidla a struktura musí zčásti přijít zvenčí — vnitřní regulace ještě není dostavěná. |
| 3. Pozdní dozrávání PFC | C | Opakovaná činnost posiluje okruhy; to, co dítě nedělá, mozek postupně „odepíše". |
| 4. Senzitivní periody | D | Některé dovednosti se v určitém věku budují snáze a levněji než později. |

**Klíč:** 1-C, 2-A, 3-B, 4-D.

## F3 OVĚŘENÍ (3 min) — FMT-MCQ + FMT-TF

1. **[MCQ]** Kortikální zrání postupuje podle Gogtay et al. (2004):
   a) od čela dozadu — nejprve plánování, pak vnímání
   b) odzadu dopředu — senzomotorické oblasti nejprve, prefrontální kůra naposled ✓
   c) rovnoměrně v celé kůře
   d) nejprve v levé, pak v pravé hemisféře
2. **[T/F]** Úbytek synapsí ve školním věku je známkou poruchy vývoje. — **Nepravda** (pruning je zdravý mechanismus specializace).
3. **[MCQ]** Že třináctiletý žák „ví, že nemá koukat do telefonu, ale stejně kouká", nejlépe vysvětluje:
   a) nedostatek inteligence
   b) rozestavěná prefrontální kůra a z ní plynoucí slabší inhibice ✓
   c) chybějící senzitivní perioda
   d) nadměrná myelinizace

## F4 APLIKACE (3 min) — Artefakt, sekce 1

Uživatel vyplní **Vývojový profil mé cílové skupiny**: zvolí věkovou skupinu (např. „4. třída, 9–10 let"), třemi větami popíše, co je pro ni vývojově typické (stav pruningu, exekutivních funkcí, senzitivních oken), a jednou větou uvede, co z toho plyne pro roli technologií. *AI role: konzultant — položí max. 2 upřesňující otázky, nepřepisuje text za uživatele (FMT-VLA).*

---

---

# CAPSTONE — Finální ověření (Varianta B)

**Délka:** 15 min | **Obsah:** kompletace artefaktu + závěrečný test + rubrika + reflexe.

1. **Kompletace artefaktu (5 min):** platforma složí sekce 1–5 z F4 modulů do jednoho dokumentu „Akční plán AI hygieny". Uživatel doplní úvodní odstavec (pro koho plán je a proč) a zkontroluje soudržnost. *AI role: zrcadlo — přečte plán a položí 2 reflexivní otázky (např. „Které opatření nejspíš narazí první a co pak?").*
2. **Závěrečný test (8 min):** viz kapitola Závěrečný test níže; práh badge 75 %.
3. **Reflexivní poznámka (2 min):** „Co ve vašem pohledu na děti a technologie tento kurz změnil? Jedno opatření, které zavedete do 30 dnů." (jde výzkumnému týmu, viz list 12).

---

## 9 ARTEFAKT — Akční plán AI hygieny

| Klíč | Hodnota |
|---|---|
| Typ artefaktu | Strukturovaný akční plán (dokument) |
| Musí obsahovat | Určení cílové skupiny; 5 sekcí z F4 (vývojový profil, pravidla pozornosti, zásady učení s AI, sociálně-emoční zásady, implementační plán); u každého opatření zdůvodnění přes vývojový princip; odstavec pro rodiče |
| Nesmí obsahovat | Plošné zákazy bez zdůvodnění; doporučení konkrétních komerčních produktů; tvrzení bez opory v obsahu kurzu; katastrofickou či bagatelizující rétoriku |
| Primární formát | Textový dokument (šablona platformy; export PDF) |
| Vstupuje do databáze scénářů? | Ano (anonymizovaně, se souhlasem) |
| Podmínka badge | Závěrečné ověření ≥ 75 % + odevzdaný artefakt |

**Šablona artefaktu — povinné sekce:**

| # | Sekce | Co obsahuje | Povinná? | Vzniká v |
|---|---|---|---|---|
| 1 | Pro koho a proč | Cílová skupina + úvodní odstavec | ano | Capstone |
| 2 | Vývojový profil skupiny | Typický stav zrání + důsledek pro technologie | ano | M1/F4 |
| 3 | Pravidla pro pozornost a prostředí | 3–5 vymahatelných pravidel | ano | M2/F4 |
| 4 | Zásady učení s AI | Tabulka scaffold/berlička se zdůvodněními | ano | M3/F4 |
| 5 | Sociálně-emoční zásady a červené linie | Zásady, signály, eskalace | ano | M4/F4 |
| 6 | Implementační plán + komunikace s rodiči | Opatření k 5 principům; odstavec pro rodiče | ano | M5/F4 |

## 11 RUBRIKA (finální ověření artefaktu)

**Typ:** analytická 5 × 5 | **Hodnotitel:** Kombinace — AI předhodnotí, lektor potvrzuje | **Práh badge:** 75 %

| Kritérium (váha) | Mistrovství 81–100 % | Zdatnost 61–80 % | Způsobilost 41–60 % | Rozvoj 21–40 % | Začátek 0–20 % |
|---|---|---|---|---|---|
| **1. Vývojová ukotvenost (25 %)** | Každé opatření je explicitně svázáno s konkrétním vývojovým principem a věkem skupiny; terminologie přesná. | Většina opatření vývojově zdůvodněna; drobné nepřesnosti. | Zdůvodnění přítomna, ale obecná („je to dobré pro mozek"). | Vývojová logika jen ojedinělá; opatření odtržena od věku. | Plán vývoj mozku nereflektuje. |
| **2. Práce s evidencí (20 %)** | Opatření opřena o zjištění z kurzu vč. rozlišení síly evidence (preprint vs. RCT); žádné tvrzení bez opory. | Evidence citována správně; síla evidence rozlišena jen zčásti. | Evidence zmíněna, občas nepřesně či bez zdroje. | Evidence zaměněna za dojmy; věcné chyby. | Tvrzení bez jakékoli opory nebo v rozporu s evidencí. |
| **3. Konkrétnost a proveditelnost (25 %)** | Každé opatření má aktéra, termín a způsob ověření; realistické pro danou školu. | Opatření konkrétní, ojediněle chybí aktér či ověření. | Směs konkrétních a vágních opatření. | Převažují deklarace („budeme dbát na…"). | Plán nelze podle textu vykonat. |
| **4. Vyváženost (15 %)** | Plán pracuje s riziky i příležitostmi AI; nikde plošné zákazy ani adorace bez argumentu; červené linie zdůvodněné. | Vyvážený, jedna strana mírně převažuje bez argumentační škody. | Znatelný příklon k zákazům či k nekritickému nasazení. | Jednostranný, druhá perspektiva chybí. | Ideologický pamflet jedním či druhým směrem. |
| **5. Komunikovatelnost (15 %)** | Odstavec pro rodiče je srozumitelný laikovi, bez žargonu, s respektem; celek čtivý a strukturovaný. | Srozumitelné, ojedinělý žargon. | Rodičovská část přítomna, ale odborně zahlcená. | Rodičovská část formální či nesrozumitelná. | Rodičovská část chybí. |

**Routing (11.3):** Silný výkon ≥ 80 % → kurzy bloku B (redesign zadání a hodnocení) — plán je hotový, teď zadání, která ho naplní. Slabý výkon < 60 % → sesterský kurz *Mozek a jazyk* (Blok A) pro upevnění neurovědních základů, poté opakování capstone. Mezera v A0601-O3 → cílené opakování M3 + F2 protiargument s novým tvrzením.

## 12 Výzkumná poznámka

Sledovaná proměnná: posun postojů pedagogů od prohibičního/laissez-faire pólu ke stanovisku „design užití" (pre/post škála 7 položek) + kvalita transferu (podíl artefaktů s opatřením zavedeným do 30 dnů — follow-up otázka). Reflexivní poznámka uživatele z capstone jde výzkumnému týmu.

---
---

---

# ZDROJE (formát)

# ZDROJE (ověřeno 28. 8. 2026)

**Vývoj mozku a exekutivní funkce**
1. Gogtay, N., et al. (2004). Dynamic mapping of human cortical development during childhood through early adulthood. *PNAS, 101*(21), 8174–8179. https://doi.org/10.1073/pnas.0402680101
2. Diamond, A. (2013). Executive functions. *Annual Review of Psychology, 64*, 135–168. https://doi.org/10.1146/annurev-psych-113011-143750
3. Casey, B. J., Getz, S., & Galván, A. (2008). The adolescent brain. *Developmental Review, 28*(1), 62–77. https://doi.org/10.1016/j.dr.2007.08.003

**Pozornost, paměť, technologie**
4. Ophir, E., Nass, C., & Wagner, A. D. (2009). Cognitive control in media multitaskers. *PNAS, 106*(37), 15583–15587. https://doi.org/10.1073/pnas.0903620106
5. Ward, A. F., Duke, K., Gneezy, A., & Bos, M. W. (2017). Brain drain: The mere presence of one's own smartphone reduces available cognitive capacity. *Journal of the Association for Consumer Research, 2*(2), 140–154. https://doi.org/10.1086/691462 *(pozn.: metaanalýza 2023 efekt zpochybňuje — v kurzu uvedeno)*
6. Paulich, K. N., et al. (2021). Screen time and early adolescent mental health, academic, and social outcomes… (ABCD Study). *PLOS ONE, 16*(9), e0256591. https://doi.org/10.1371/journal.pone.0256591

**Učení, offloading, AI**
7. Risko, E. F., & Gilbert, S. J. (2016). Cognitive offloading. *Trends in Cognitive Sciences, 20*(9), 676–688. https://doi.org/10.1016/j.tics.2016.07.002
8. Sparrow, B., Liu, J., & Wegner, D. M. (2011). Google effects on memory. *Science, 333*(6043), 776–778. https://doi.o …

Pravidlo: každý zdroj má autora, rok, časopis, DOI nebo URL a datum ověření v nadpisu sekce. Preprint nebo rukopis je označen. U tvrzení, která pozdější výzkum oslabil, je poznámka přímo u zdroje i v textu F1.
