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

# MODUL 2 — Pozornost: úzké hrdlo učení

**Délka:** 15 min | **OBJECTIVES:** A0601-O2 | **Skip:** ano (80 %) | **Vazba na GOALS:** G2, G4
**Neurovědní principy:** NP-07 + NP-13 (obsah modulu), NP-04 (F2 — dialog bez nápovědy), NP-18 (okamžitá ZV), NP-06 (grafika úzkého hrdla).

## IMPULS

*Telefon vašeho žáka nemusí ani zazvonit, aby ho rozptýlil. Podle experimentů stačí, když leží na lavici — displejem dolů.*

## F1 PREZENTACE (5 min)

Bez pozornosti není kódování do paměti (NP-13). A pozornost školáka teče úzkým hrdlem: **pracovní paměť udrží zhruba 4 ± 1 prvky** — u dětí spíše méně, protože ji hostí dozrávající PFC (modul 1). Teorie kognitivní zátěže říká: přetížíme-li hrdlo, učení se zastaví, i když „obsah byl odučen".

Digitální prostředí toto hrdlo zatěžuje třemi mechanismy:

**1. Multitasking je iluze.** Mozek úlohy nestíhá paralelně, jen mezi nimi přepíná — a každé přepnutí stojí čas a chyby. Stanfordská studie (Ophir, Nass & Wagner, PNAS 2009) ukázala, že chroničtí mediální multitaskeři jsou paradoxně *horší* ve filtrování rušivých podnětů. (Poctivě: pozdější replikace nacházejí efekty slabší — směr je ale konzistentní: multitasking učení nepomáhá nikdy.)

**2. Pouhá přítomnost telefonu.** Experimenty Warda a kolegů (2017) naznačují „brain drain": část kapacity pracovní paměti se vyčerpává už tím, že vlastní telefon je v dosahu — mozek vynakládá zdroje na to, aby ho ignoroval. (I zde poctivě: metaanalýza z r. 2023 efekt zpochybňuje; jistota je nižší, než tvrdí titulky. Pro praxi však platí bezpečná asymetrie: telefon mimo dohled nic nestojí a nic neriskuje.)

**3. Notifikace a přerušovaná práce.** Každé přerušení znamená znovunaladění na úlohu; u dítěte s nezralou inhibicí trvá déle než u dospělého.

A pozor na čtvrtého hráče: **spánek**. Konsolidace paměti probíhá ve spánku (NP-12) — večerní obrazovky, které spánek zkracují a odsouvají, tedy sabotují i to, co se dítě přes den poctivě naučilo. Velké kohortové studie (ABCD, ~12 000 dětí) ukazují u nadměrného času u obrazovek zhoršený spánek a mírně horší školní výsledky; efekty jsou střízlivé velikosti — o to víc záleží na tom *co* a *kdy*, ne jen *kolik minut*.

*Zapamatujte si: pozornost je nejvzácnější zdroj třídy. Nechráníme děti před technologiemi — chráníme úzké hrdlo, kterým teče všechno učení.*

**Větvení:** Akademik — rozdíl korelace/kauzalita v ABCD datech. Mentor — jak nastavit pravidla pro telefony, která obstojí před rodiči. Student — vlastní studijní multitasking jako nejbližší experimentální materiál.

## F2 PROCVIČENÍ (4 min) — FMT-SOK (sokratovský dialog)

*Instrukce pro agenta: Veď uživatele otázkami k vlastnímu závěru, že problém scénáře není obsah, ale struktura pozornosti. Odpověď neprozrazuj. Max. 5 výměn. Startovní scénář:* „Učitelka pustí žákům 7. třídy výukové video. Žáci mají zároveň na tabletech vyplňovat pracovní list k videu a učitelka jim dovolila nechat si telefony na lavici, ‚protože je stejně nepoužívají'. Polovina třídy si z videa nepamatuje nic. Co se stalo?" *Cílové poznatky: dvojí souběžná úloha = přepínání; telefon na lavici = brain drain; řešení = fázovat (nejdřív video, pak list) a telefony mimo dosah.*

## F3 OVĚŘENÍ (3 min) — FMT-SA + FMT-TF

1. **[Short answer]** Vysvětlete vlastními slovy, proč „poslouchám výklad a zároveň píšu zprávu" nemůže fungovat. *(Klíč: pracovní paměť 4±1, přepínání úloh místo paralelního zpracování, náklady přepnutí.)*
2. **[T/F]** Vypnutí zvuku notifikací zcela odstraní vliv telefonu na pozornost. — **Nepravda** (evidence naznačuje náklady i u pouhé přítomnosti; jistější je fyzická vzdálenost).
3. **[T/F]** Nedostatek spánku poškozuje i učivo, které se dítě naučilo přes den. — **Pravda** (spánková konsolidace).

## F4 APLIKACE (3 min) — Artefakt, sekce 2

Uživatel napíše **Pravidla pro pozornost a prostředí** své cílové skupiny: 3–5 konkrétních, vymahatelných pravidel (kde jsou telefony, jak se fázují úlohy s technologiemi, co platí pro notifikace na školních zařízeních, doporučení k večernímu režimu pro rodiče). *AI role: hodnotitel proveditelnosti — u každého pravidla se zeptá „kdo to vymáhá a jak poznáte, že to funguje?"*

---

# MODUL 3 — Učení, které bolí (a proto funguje)

**Délka:** 15 min | **OBJECTIVES:** A0601-O3 | **Skip:** NE (jádrový modul) | **Vazba na GOALS:** G4, G5
**Neurovědní principy:** NP-04 + NP-09 + NP-10 (obsah i forma modulu), NP-03 (F2 protiargument), NP-18.

## IMPULS

*Studenti s ChatGPT vyřešili o 48 % více cvičných úloh. Pak jim ho vzali — a v testu byli o 17 % horší než ti, kteří AI nikdy neměli.*

## F1 PREZENTACE (5 min)

Mozek si trvale ukládá to, co sám **vygeneroval** (NP-09), co si musel **vybavit** (NP-03, NP-10) a co ho stálo **přiměřenou námahu** (NP-04, „žádoucí obtíže"). Přesně tuto námahu umí AI odstranit — a v tom je její dvojsečnost.

**Kognitivní offloading** — přenesení mentální práce na externí nástroj (Risko & Gilbert, 2016) — není nový jev: píšeme si nákupní seznamy, Sparrow a kolegové (Science, 2011) popsali „Google efekt" (pamatujeme si *kde* informaci najít místo informace samé). Nové je, že generativní AI umí offloadovat nikoli fakta, ale **samotné myšlení**: strukturování, formulaci, řešení.

Co o tom říká evidence u školáků?

**Terénní experiment Bastani et al. (PNAS, 2025):** ~1 000 středoškoláků v Turecku, výuka matematiky. Skupina s neomezeným ChatGPT („GPT Base") řešila cvičení o 48 % úspěšněji — ale v následném testu bez AI skórovala o 17 % *hůře* než kontrola bez technologií. Skupina s AI tutorem s zábradlím („GPT Tutor" — nápovědy, neprozrazuje řešení) byla ve cvičení lepší o 127 % a v testu srovnatelná s kontrolou. Závěr: **neřízená AI funguje jako berlička; AI s designem opory jako trenér.** Berlička neškodí tomu, kdo už chodit umí — u dítěte, které se chodit teprve učí, brání stavbě okruhů.

**EEG studie Kosmyna et al. (MIT Media Lab, 2025, preprint — zatím bez recenzního řízení a s publikovanou kritikou metodologie):** při psaní esejí s LLM vykazovali účastníci nejslabší konektivitu mozkových sítí (vs. vyhledávač a psaní „z hlavy") a horší vybavení vlastního textu; autoři mluví o „kognitivním dluhu". Berte jako varovný signál, ne rozsudek.

Do třetice motorika: psaní **rukou** aktivuje u dvanáctiletých rozsáhlejší, pro učení příznivé vzorce mozkové aktivity než psaní na klávesnici (Ose Askvik, van der Weel & van der Meer, 2020) a poznámky rukou vedou k hlubšímu zpracování než doslovný přepis na notebooku (Mueller & Oppenheimer, 2014; replikace efekt zmenšily, nezrušily).

*Zapamatujte si: rozhodující otázka u každého nasazení AI zní — kdo tady generuje? Pokud námahu nese stroj, mozek žáka nestaví.*

**Větvení:** Akademik — Bastani jako vzor RCT designu; co je „guardrail" v promptu. Mentor — jak poznat berličku při hospitaci (žák umí výsledek, neumí cestu). Student — vlastní zkušenost: kdy mi AI naposledy „pomohla" tak, že jsem se nic nenaučil/a?

## F2 PROCVIČENÍ (4 min) — FMT-PRO (protiargument)

*Instrukce pro agenta: Uživatel dostane tvrzení a formuluje protiargument opřený o evidenci z F1. Poté reaguj: uznej silné body, doplň, co chybí, rozvíjej max. 2 výměny.*

Tvrzení k rozporování: **„Zákaz ChatGPT ve škole je jediný způsob, jak ochránit učení dětí."**
*(Očekávané jádro: Bastani ukazuje, že problém není nástroj, ale absence zábradlí — GPT Tutor učení nepoškodil; zákaz navíc přesune užívání domů bez jakéhokoli vedení; cílem je design užití, ne zákaz. Silná odpověď zmíní i limity evidence.)*

## F3 OVĚŘENÍ (3 min) — FMT-MTC + FMT-MCQ

1. **[Matching]** Přiřaďte pojem k příkladu: 1. kognitivní offloading — C, 2. efekt generování — A, 3. žádoucí obtíž — D, 4. testovací efekt — B.
   A) Žák nejprve sám zformuluje definici, teprve pak vidí vzorovou. B) Místo dalšího čtení kapitoly si žák píše zpaměti, co si pamatuje. C) Žák nechá AI shrnout text a shrnutí si přečte. D) Učitel míchá typy úloh, ačkoli by „po blocích" šly rychleji.
2. **[MCQ]** Klíčový rozdíl mezi skupinami „GPT Base" a „GPT Tutor" (Bastani et al., 2025): a) verze modelu b) design opory: Tutor napovídal postup a neprozrazoval řešení ✓ c) délka přístupu d) věk žáků
3. **[MCQ]** Studie Kosmyna et al. (2025) je: a) recenzovaná metaanalýza b) preprint s malým vzorkem — varovný signál vyžadující replikaci ✓ c) longitudinální kohorta d) učebnicový konsenzus

## F4 APLIKACE (3 min) — Artefakt, sekce 3

Uživatel vytvoří **Zásady učení s AI** pro svou skupinu: tabulku se 3 řádky „AI ANO (scaffold)" a 3 řádky „AI NE (berlička)" pro konkrétní činnosti svého předmětu, každý řádek s jednovětým zdůvodněním přes princip (generování, vybavování, žádoucí obtíž). *AI role: partner — navrhne 1 hraniční případ a nechá uživatele rozhodnout.*

---

# MODUL 4 — Dospívající mozek online

**Délka:** 15 min | **OBJECTIVES:** A0601-O4 | **Skip:** ano (80 %) | **Vazba na GOALS:** G4, G5
**Neurovědní principy:** NP-11 (obsah — dopaminové učení; IMPULS), NP-15 (F2 reflexe případu), NP-06 (grafika dvou systémů), NP-10 (F3).

## IMPULS

*72 % amerických teenagerů už si povídalo s AI společníkem. Třetina z nich probrala s chatbotem vážnou věc raději než s člověkem.*

## F1 PREZENTACE (5 min)

Proč je dospívání zvlášť citlivé období pro sociální technologie? Model „dvou systémů" (Casey, Getz & Galván, 2008): subkortikální okruhy odměny (dopaminový systém) dozrávají a zesilují **dříve** než prefrontální kontrola. Mezi ~10. a 15. rokem tak jede motor citlivý na odměnu, novost a vrstevnické uznání na plný výkon — zatímco brzdy se teprve montují (modul 1). Sociální sítě i AI společníci jsou navrženi přesně pro tento motor: proměnlivé odměny (NP-11 — dopamin řídí *překvapení*), okamžitá odezva, nekonečná novost.

**AI společníci** jsou nová kapitola. Reprezentativní šetření Common Sense Media (2025, 13–17 let, USA): 72 % teenagerů AI společníka někdy použilo, 52 % opakovaně; třetina volila AI místo člověka pro vážný rozhovor, čtvrtina mu sdělila osobní údaje. Souběžné hodnocení s odborníky ze Stanfordu (Brainstorm Lab) uzavřelo, že sociální AI společníci představují pro nezletilé **nepřijatelné riziko** — snadno přitakávají, simulují intimitu, neumí spolehlivě zachytit krizi.

Neurovývojová logika rizika: dospívání je senzitivní periodou pro **sociální učení** — kalibruje se v něm čtení druhých, zvládání odmítnutí, reciprocita. AI společník je sociální partner bez tření: neodmítne, neunaví se, nemá vlastní potřeby. Trénink sociálních okruhů na partnerovi bez tření je jako posilovna bez závaží. A pozor na druhou stranu mince: tytéž vlastnosti (trpělivost, neúnavnost, nesoudí) mohou být cenné jako **doplněk** — např. bezpečný prostor pro nácvik konverzace v cizím jazyce. Červená linie nevede mezi „používá/nepoužívá", ale mezi **doplňkem a náhradou** lidských vztahů.

*Zapamatujte si: dospívající mozek má plynový pedál napřed a brzdy dodělávané za jízdy. Technologie navržené pro tento pedál vyžadují vnější zábradlí — a vztahy, které za to stojí, mají tření.*

**Větvení:** Akademik — metodologie prevalenčních šetření; co (ne)plyne z korelací u sociálních sítí. Mentor — signály, že žák nahrazuje vztahy chatbotem; kdy kontaktovat poradenské pracoviště. Student — vlastní hranice: co říct žákovi, který se svěří, že „kámoší" s AI.

## F2 PROCVIČENÍ (4 min) — FMT-MIK (mikroartefakt)

*Instrukce pro agenta: Uživatel napíše 3–5 vět. Poté navrhni max. 2 vylepšení; rozhodnutí nechej na uživateli.*

Zadání: „Žákyně 8. třídy vám řekne: ‚Povídám si večer s AI, je jediná, kdo mě poslouchá.' Napište, co jí odpovíte — tak, abyste nezesměšnili, neodsoudili, ale otevřeli dveře k lidskému kontaktu a pojmenovali jedno konkrétní riziko."

## F3 OVĚŘENÍ (3 min) — FMT-TF + FMT-MCQ

1. **[T/F]** Okruhy odměny dozrávají u dospívajících dříve než prefrontální kontrola. — **Pravda.**
2. **[T/F]** Podle šetření Common Sense Media (2025) používá AI společníky jen okrajová menšina teenagerů. — **Nepravda** (72 % aspoň jednou, 52 % opakovaně).
3. **[MCQ]** Hlavní neurovývojový argument, proč AI společník nemůže nahradit vrstevnické vztahy: a) AI lže o faktech b) sociální okruhy se kalibrují na interakcích „se třením" — s odmítnutím, vyjednáváním, reciprocitou ✓ c) AI nezná češtinu dost dobře d) dospívající AI nezajímá

## F4 APLIKACE (3 min) — Artefakt, sekce 4

Uživatel doplní **Sociálně-emoční zásady a červené linie**: 2–3 zásady pro svou skupinu (např. pravidlo doplněk-ne-náhrada, signály k zpozornění, kam eskalovat) + 1 větu, jak téma otevřít s rodiči bez paniky. *AI role: oponent — zkusí jednu zásadu napadnout z pozice „přehnané ochrany" a nechá uživatele obhájit či upravit.*

---

# MODUL 5 — AI hygiena: od zákazů k designu

**Délka:** 15 min | **OBJECTIVES:** A0601-O5 | **Skip:** NE (syntéza + největší tvůrčí podíl) | **Vazba na GOALS:** G5, G6
**Neurovědní principy:** NP-08 (propojení všech modulů do rámce), NP-15 (metakognice — plán obsahuje sebekontrolní otázky), NP-18, NP-02 (plán počítá s opakováním, ne jednorázovou kampaní).

## IMPULS

*UNESCO doporučuje nepouštět generativní AI k samostatné konverzaci s dětmi pod 13 let. Průměrný český třeťák na základce přitom umí otevřít chatbota za osm vteřin. Kdo z těch dvou čeká na vaše rozhodnutí?*

## F1 PREZENTACE (5 min)

Vše z modulů 1–4 se skládá do jednoho rámce: **AI hygiena** — soubor návyků a pravidel, které chrání vyvíjející se mozek a zároveň využívají, co AI umí. Ne plošné zákazy, ne laissez-faire: design.

Mezinárodní kotva: **UNESCO — Guidance for Generative AI in Education and Research (2023)** doporučuje mj. minimální věk 13 let pro samostatné užívání konverzační generativní AI, ochranu dat dětí, přípravu učitelů před nasazením nástrojů a lidský dohled („human-centred approach"). To je dobrá výchozí čára — a národní pravidla i školní řády se od ní teprve odvíjejí.

**Pět principů AI hygieny** (odvozeno z modulů 1–4):

1. **Nejdřív mozek, pak stroj** (M3): žák generuje první verzi sám; AI vstupuje až do revize. Chráníme efekt generování.
2. **AI se ptá, neodpovídá** (M3): pro žáky 6–15 nastavujeme AI do role tutora s zábradlím — napovídá postup, neprozrazuje řešení (vzor GPT Tutor).
3. **Chráněné hrdlo** (M2): technologie do výuky vstupují fázovaně, jedna úloha v jednu chvíli, telefony mimo dosah, večer bez obrazovek kvůli konsolidaci.
4. **Doplněk, ne náhrada** (M4): AI nikdy nenahrazuje vztah, pohyb, spánek ani vlastní čtení; u sociálních AI společníků platí pro nezletilé stopka.
5. **Učitel jako stavební dozor** (M1): dokud PFC nedozrál, vnější struktura není buzerace, ale lešení. Pravidla se vysvětlují přes mozek („chráníme ti pracovní paměť"), ne přes moc.

A metakognitivní pojistka (NP-15): každé nasazení AI doprovází otázka pro žáka — *„Co jsem tu udělal/a já a co stroj?"* Kdo umí odpovědět, offloaduje vědomě; kdo ne, je offloadován.

*Zapamatujte si: AI hygiena = mýt si ruce, ne zakázat vodu. Pravidla odvozená z vývoje mozku přežijí jakoukoli novou aplikaci.*

**Větvení:** Akademik — jak z principů udělat kritéria pro posuzování EdTech nástrojů. Mentor — jak principy prosadit ve sborovně, která je rozdělená. Student — minimální verze pro první vlastní hodinu.

## F2 PROCVIČENÍ (4 min) — FMT-SOK (sokratovský dialog)

*Instrukce pro agenta: Sokratovsky, bez prozrazení, max. 5 výměn. Dilema:* „Ředitel navrhne: ‚Koupíme licenci AI asistenta a dáme ho všem žákům od 3. třídy, ať se učí s dobou.' Uživatel má dialogem dojít k min. třem otázkám, které je nutné zodpovědět před nasazením (věková hranice a UNESCO doporučení; režim tutor vs. odpovídač; ochrana dat; kdo učitele připraví; jak se pozná úspěch)."

## F3 OVĚŘENÍ (3 min) — FMT-MCQ (scénáře)

1. **[MCQ]** Žáci 9. třídy píší esej. Které nasazení AI nejlépe odpovídá principu „nejdřív mozek, pak stroj"? a) AI vygeneruje osnovu, žáci dopíší b) žáci odevzdají AI text a přiznají to c) žáci napíší první verzi sami, pak s AI konfrontují strukturu a protiargumenty ✓ d) AI se nepoužije vůbec
2. **[MCQ]** UNESCO (2023) doporučuje pro samostatné konverzace dětí s generativní AI minimální věk: a) 6 b) 10 c) 13 ✓ d) 18
3. **[MCQ]** „AI se ptá, neodpovídá" v praxi znamená: a) zakázat AI odpovědi b) systémový prompt/režim, v němž AI vede postup nápovědami a řešení neprozrazuje ✓ c) používat jen hlasové AI d) AI smí jen opravovat pravopis

## F4 APLIKACE (3 min) — Artefakt, sekce 5

Uživatel dopíše **Implementační plán**: pro každý z pěti principů jedno konkrétní opatření pro svou skupinu (co, kdo, od kdy) + krátký odstavec „jak to vysvětlím rodičům" (2–3 věty jazykem bez odborných termínů). *AI role: kontrolor úplnosti — zkontroluje, že žádný princip nezůstal bez opatření, a proveditelnost každého opatření ověří jednou otázkou.*

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

# PROCVIČOVACÍ TEST (samostatný, mimo moduly)

*20 úloh napříč moduly; AI vyhodnocuje průběžně, u chyby odkáže na modul. Neboduje se — slouží NP-02/NP-10.*

**A. Matching (2 sady)**

1. Přiřaďte oblast/proces k funkci: 1. prefrontální kůra — B; 2. dopaminový systém odměny — D; 3. myelin — A; 4. hipokampus a spánek — C.
   A) izolace axonů, rychlost signálu B) plánování, inhibice, pracovní paměť C) konsolidace paměti D) učení z překvapení, citlivost na novost
2. Přiřaďte studii k zjištění: 1. Gogtay 2004 — C; 2. Bastani 2025 — A; 3. Ward 2017 — D; 4. Common Sense Media 2025 — B.
   A) neřízená AI zlepší cvičení, zhorší samostatný test B) 72 % teenagerů zkusilo AI společníka C) kůra zraje odzadu dopředu, PFC naposled D) pouhá přítomnost telefonu může ubírat kapacitu pracovní paměti

**B. Multiple choice (6)**

3. „Use it or lose it" popisuje: a) myelinizaci b) synaptický pruning ✓ c) senzitivní periodu d) kognitivní zátěž
4. Pracovní paměť školáka udrží zhruba: a) 2 prvky b) 4 ± 1 prvky ✓ c) 7–9 prvků d) neomezeně, jde o motivaci
5. Multitasking při učení: a) trénuje pozornost b) je reálné paralelní zpracování c) je přepínání úloh s náklady na čas a chyby ✓ d) škodí jen dospělým
6. „GPT Tutor" v experimentu Bastani et al. se od běžného chatbota lišil tím, že: a) běžel na slabším modelu b) měl v promptu zábradlí — napovídal, neprozrazoval řešení ✓ c) byl placený d) fungoval jen ve škole
7. Google efekt (Sparrow 2011): pamatujeme si spíše: a) obsah informace b) kde informaci najít ✓ c) kdo nám ji řekl d) kdy jsme ji hledali
8. Nejsilnější vývojový argument pro věkovou hranici u konverzační AI: a) děti neumějí psát b) nezralá prefrontální regulace + neschopnost dítěte rozpoznat simulovanou intimitu a halucinace ✓ c) AI je drahá d) děti se u AI nudí

**C. Pravda / nepravda (5)**

9. Úbytek synapsí v dospívání je patologický. — **N**
10. Efekty času u obrazovek v ABCD studii jsou obrovské a jednoznačně kauzální. — **N** (střízlivé asociace, kauzalita neprokázána)
11. Psaní rukou aktivuje u dětí rozsáhlejší, pro učení příznivé vzorce mozkové aktivity než psaní na klávesnici. — **P**
12. AI společníci jsou dle Common Sense Media vhodní od 15 let. — **N** (doporučení: pro nezletilé nevhodné)
13. Vnější pravidla a struktura u žáků 6–15 nahrazují dosud nedostavěnou exekutivní regulaci. — **P**

**D. Krátká odpověď (3)**

14. Vysvětlete rozdíl mezi AI jako scaffoldem a AI jako berlou; ke každému jeden příklad. *(Klíč: scaffold podporuje generování žáka — nápověda postupu, otázky, ZV k vlastní verzi; berlička generuje místo žáka — hotová řešení, shrnutí místo čtení. Bastani: berlička = lepší cvičení, horší test.)*
15. Proč večerní obrazovky poškozují i to, co se dítě naučilo dopoledne? *(Klíč: konsolidace ve spánku; zkrácený/odsunutý spánek = přerušený zápis z hipokampu do neokortexu.)*
16. Jednou větou pro rodiče: proč „telefon jen leží na stole" není neutrální? *(Klíč: část kapacity pracovní paměti se spotřebuje na ignorování — laicky, bez žargonu.)*

**E. Tvorba otázek (FMT-OTA)**

17. Napište 3 otázky, které byste položili dodavateli AI aplikace pro 2. stupeň ZŠ. *(AI posoudí hloubku: očekávané okruhy — režim tutor/odpovídač, data dětí, věková přiměřenost, evidence účinnosti, role učitele.)*

**F. Protiargument (FMT-PRO)**

18. Rozporujte: „Dnešní děti jsou digitální domorodci — jejich mozky jsou na technologie stavěné, dospělí jim nemají co mluvit do používání AI." *(Klíč: architektura mozku se za jednu generaci nemění; PFC dozrává stejně pomalu; „domorodost" = obratnost v ovládání, ne v seberegulaci a kritickém hodnocení.)*

**G. Mikroscénář (FMT-MIK)**

19. Navrhněte 4 věty, jimiž třídní učitel 6. třídy zavádí pravidlo „telefony přes vyučování v šatní skříňce" — se zdůvodněním přes mozek, ne přes moc.

**H. Sokratovský dialog (FMT-SOK)**

20. *Zadání pro agenta: max. 6 výměn, neprozrazovat.* Výchozí otázka uživateli: „Sedmák tvrdí: ‚Když mi AI vysvětlí úlohu líp než učitelka, proč bych ji neměl používat pořád?' V čem má pravdu — a jaká past se v té větě skrývá?" *Cíl: uživatel sám dojde k rozlišení vysvětlení (scaffold, legitimní) vs. vyřešení (berlička) a k otázce, kdo kontroluje, že porozumění vzniklo (testovací efekt).*

---

# ZÁVĚREČNÝ TEST (finální ověření, práh 75 %)

*Podklad pro platformu: část I (uzavřené, 60 % váhy) hodnotí AI automaticky; část II (produkční, 40 % váhy) hodnotí AI dle klíče + lektor potvrzuje. Celkové skóre s rubrikou artefaktu rozhoduje o badge.*

**Část I — uzavřené úlohy (15)**

1. **[MCQ]** Poslední dozrávající oblastí kůry je: a) zraková b) motorická c) prefrontální ✓ d) sluchová
2. **[MCQ]** Senzitivní perioda je: a) věk povinné školní docházky b) okno zvýšené plasticity pro určitou funkci ✓ c) puberta d) doba zkoušení
3. **[MCQ]** Který jev NENÍ kognitivní offloading? a) nákupní seznam b) AI shrnutí místo četby c) vybavování zpaměti před spaním ✓ d) navigace místo orientace
4. **[MCQ]** Výsledek skupiny s neomezeným ChatGPT (Bastani 2025) v testu bez AI: a) +48 % b) −17 % ✓ c) +127 % d) beze změny
5. **[MCQ]** Žádoucí obtíže fungují, protože: a) frustrace motivuje b) hlubší zpracování při přiměřené námaze posiluje trvalou stopu ✓ c) delší čas = víc látky d) žáci si stěžují méně
6. **[MCQ]** Dvě křivky modelu Casey et al. (2008): a) jazyk × matematika b) systém odměny (dřív) × prefrontální kontrola (později) ✓ c) paměť × pozornost d) levá × pravá hemisféra
7. **[MCQ]** UNESCO 2023 mj. doporučuje: a) zákaz AI ve školách b) min. věk 13 let pro samostatnou konverzační AI + přípravu učitelů před nasazením ✓ c) AI od 1. třídy povinně d) ponechat na trhu
8. **[MCQ]** Správné pořadí dle „nejdřív mozek, pak stroj": a) AI osnova → žák text b) žák první verze → AI oponentura → žák revize ✓ c) AI text → žák úprava d) AI text i úprava
9. **[T/F]** Pruning řídí mj. to, které činnosti dítě opakovaně vykonává. — **P**
10. **[T/F]** Přepínání mezi úlohami je zdarma, pokud jsou obě snadné. — **N**
11. **[T/F]** Studie Kosmyna et al. (2025) je recenzovaným důkazem trvalého poškození mozku. — **N** (preprint, konektivita při úloze, nutná replikace)
12. **[T/F]** AI společník bez tření může u dospívajících oslabovat trénink reálných sociálních dovedností. — **P**
13. **[T/F]** Kvalitní AI tutor podle evidence zhoršuje výsledky vždy. — **N** (GPT Tutor: cvičení +127 %, test srovnatelný)
14. **[Matching]** 1. NP-09 efekt generování — C; 2. NP-10 testovací efekt — A; 3. NP-07 kognitivní zátěž — D; 4. NP-12 konsolidace ve spánku — B.
    A) F3 v každém modulu B) pravidlo večera bez obrazovek C) žák píše první verzi sám D) F1 max 5 minut
15. **[Matching]** Přiřaďte princip AI hygieny k situaci: 1. Nejdřív mozek, pak stroj — B; 2. AI se ptá, neodpovídá — D; 3. Chráněné hrdlo — A; 4. Doplněk, ne náhrada — C.
    A) telefony do skříňky, jedna úloha najednou B) esej: vlastní draft před AI oponenturou C) chatbot nesmí být jediný „důvěrník" žáka D) tutor napovídá postup, řešení nedává

**Část II — produkční úlohy (3)**

16. **[Řešení problému]** *Případová studie:* „ZŠ zavedla pro 4.–9. třídu AI asistenta v režimu volného chatu. Po půl roce: domácí úkoly bez chyb, čtvrtletní písemky výrazně horší, dvě třídní učitelky hlásí žáky, kteří se ‚radí s AI o osobních věcech'. Ředitelka zvažuje úplný zákaz." Napište (10–14 vět): (a) diagnózu přes pojmy kurzu, (b) proč úplný zákaz problém nevyřeší, (c) 3 konkrétní opatření s vývojovým zdůvodněním. *(Klíč: berlička/offloading → iluze kompetence vs. testovací efekt; volný chat u nezletilých vs. věkové hranice a AI společníci; zákaz = přesun domů bez vedení; opatření: režim tutora, fázování a pravidla prostředí, pravidlo doplněk-ne-náhrada + komunikace s rodiči.)*
17. **[Sokratovský dialog — FMT-SOK]** *Zadání pro agenta: max. 6 výměn; hodnotí se, zda uživatel v dialogu sám formuluje cílové rozlišení; neprozrazovat.* Výchozí situace: „Rodič na schůzce: ‚Platíme dceři AI doučovatele, od té doby má jedničky z domácích cvičení. Nechápu, proč jí píšete, že zaostává.'" AI vede uživatele k vysvětlení rozporu (výkon s oporou ≠ kompetence; testovací efekt; jak AI doučovatele nastavit jako tutora) a k formulaci doporučení pro rodiče.
18. **[Krátká syntéza]** Vyberte jedno tvrzení z kurzu, u něhož je evidence nejslabší, zdůvodněte proč — a vysvětlete, proč přesto (ne)patří do vašeho akčního plánu. *(Klíč: očekává se Kosmyna preprint či brain drain vs. metaanalýza 2023; hodnotí se kalibrace jistoty a argument bezpečné asymetrie.)*

---

# 3' VIDEO — skript a storyboard

**Název:** Staveniště v hlavě | **Stopáž:** ~3:00 | **Formát:** 1920×1080, voiceover (cs-CZ), animované scény z grafiky kurzu
**Soubory:** `A0601-KURZ-video-shrnuti.mp4` (hotové video), `A0601-KURZ-audio-shrnuti.mp3` (samostatný voiceover pro platformu / posluchače s dyslexií), `A0601-KURZ-anim-shrnuti.html` (interaktivní verze)

| # | Čas | Scéna (obraz) | Voiceover |
|---|---|---|---|
| 1 | 0:00–0:20 | Titulek na tmavém pozadí; obrys dětské hlavy, v ní jeřáb a lešení; título kurzu | Mozek vašeho žáka je staveniště. Stavba běží od narození do pětadvaceti let — a právě na ni dorazila umělá inteligence. Bez ohlášení. Tři minuty o tom, co by měl vědět každý, kdo učí děti od šesti do patnácti. |
| 2 | 0:20–0:50 | Animace: síť synapsí houstne a pak se prořezává; časová osa 6→15→25; PFC se rozsvěcí poslední | Zaprvé: stavba má řád. Dětský mozek si vytvoří nadbytek spojení a pak škrtá — co se používá, sílí, co ne, mizí. Use it or lose it. Kůra zraje odzadu dopředu: dispečink stavby, prefrontální kůra se sebekontrolou a plánováním, dozrává jako poslední. Proto dítě ví, že nemá koukat do telefonu — a stejně kouká. Brzdy se teprve montují. |
| 3 | 0:50–1:15 | Trychtýř „4±1"; ikony: telefon na lavici, notifikace, rozdvojená šipka multitaskingu | Zadruhé: všechno učení teče úzkým hrdlem. Pracovní paměť udrží čtyři plus mínus jeden prvek. Multitasking je přepínání, ne paralelka — a platí se za něj chybami. Experimenty naznačují, že i telefon, který jen leží na lavici, ukrajuje kapacitu. Pozornost je nejvzácnější zdroj třídy. Chraňte ji. |
| 4 | 1:15–1:50 | Graf Bastani: cvičení +48 % / test −17 %; vedle druhý sloupec Tutor +127 % / test OK; váha „berlička × trenér" | Zatřetí: mozek staví jen to, co sám vygeneroval. Tisíc středoškoláků dostalo ChatGPT k matematice. Ve cvičeních zazářili — o čtyřicet osm procent lépe. Pak jim ho vzali: v testu byli o sedmnáct procent horší než třída, která AI nikdy neměla. Ale stejná studie ukázala i řešení: AI nastavená jako tutor, který napovídá a neprozrazuje, učení nepoškodila. Rozdíl není v nástroji. Je v designu. |
| 5 | 1:50–2:15 | Dvě křivky: odměna (dřív) × kontrola (později); ikona chatbota se srdíčkem; údaj 72 % | Začtvrté: dospívající mozek má plyn napřed a brzdy dodělávané za jízdy. Sociální sítě i AI společníci míří přesně na ten plyn. Sedmdesát dva procent amerických teenagerů už si s AI společníkem psalo — a třetina s ním probrala vážné věci raději než s člověkem. Vztah bez tření ale sociální svaly netrénuje. Tady vede červená linie: doplněk ano, náhrada ne. |
| 6 | 2:15–2:45 | Pět ikon principů AI hygieny se skládá do štítu | Co s tím? AI hygiena. Pět pravidel: Nejdřív mozek, pak stroj — první verzi tvoří žák. AI se ptá, neodpovídá — režim tutora. Chráněné hrdlo — telefony z dosahu, jedna úloha najednou, večer bez obrazovek. Doplněk, ne náhrada — u vztahů absolutně. A učitel jako stavební dozor — vnější struktura je lešení, dokud vnitřní nedoroste. |
| 7 | 2:45–3:00 | Štít se zavírá do loga kurzu; závěrečný titulek s CTA | AI hygiena znamená mýt si ruce — ne zakázat vodu. V kurzu si sestavíte vlastní akční plán pro svou třídu. Mozek vašich žáků se staví právě teď. Stavte s rozmyslem. |

*Poznámka k výrobě: MP4 generováno z grafik kurzu + neurální hlas cs-CZ (edge-tts, Vlasta). Pro budoucí lidský dabing je skript připraven po scénách; alternativně lze audio stopu nahradit v NotebookLM/HeyGen.*

---

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
8. Sparrow, B., Liu, J., & Wegner, D. M. (2011). Google effects on memory. *Science, 333*(6043), 776–778. https://doi.org/10.1126/science.1207745
9. Bastani, H., Bastani, O., Sungu, A., Ge, H., Kabakcı, Ö., & Mariman, R. (2025). Generative AI without guardrails can harm learning: Evidence from high school mathematics. *PNAS, 122*(26). https://doi.org/10.1073/pnas.2422633122
10. Kosmyna, N., et al. (2025). Your Brain on ChatGPT: Accumulation of cognitive debt when using an AI assistant for essay writing task. *arXiv preprint.* https://arxiv.org/abs/2506.08872 *(preprint — bez recenzního řízení; existuje publikovaná metodologická kritika)*
11. Mueller, P. A., & Oppenheimer, D. M. (2014). The pen is mightier than the keyboard. *Psychological Science, 25*(6), 1159–1168. https://doi.org/10.1177/0956797614524581
12. Ose Askvik, E., van der Weel, F. R., & van der Meer, A. L. H. (2020). The importance of cursive handwriting over typewriting for learning in the classroom: A high-density EEG study of 12-year-old children and young adults. *Frontiers in Psychology, 11*, 1810. https://doi.org/10.3389/fpsyg.2020.01810

**Efektivní učení (pozadí neurovědních principů)**
13. Roediger, H. L., & Karpicke, J. D. (2006). Test-enhanced learning. *Psychological Science, 17*(3), 249–255. https://doi.org/10.1111/j.1467-9280.2006.01693.x
14. Dunlosky, J., et al. (2013). Improving students' learning with effective learning techniques. *Psychological Science in the Public Interest, 14*(1), 4–58. https://doi.org/10.1177/1529100612453266

**AI, děti a politiky**
15. UNESCO (2023). *Guidance for generative AI in education and research.* https://www.unesco.org/en/articles/guidance-generative-ai-education-and-research
16. Common Sense Media (2025). *Talk, Trust, and Trade-Offs: How and why teens use AI companions.* https://www.commonsensemedia.org/research/talk-trust-and-trade-offs-how-and-why-teens-use-ai-companions
17. Common Sense Media (2025). *AI companions decoded: Safety standards* (se Stanford Brainstorm Lab). https://www.commonsensemedia.org/press-releases/ai-companions-decoded-common-sense-media-recommends-ai-companion-safety-standards
