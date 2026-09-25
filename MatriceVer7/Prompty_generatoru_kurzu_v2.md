# Prompty generátoru kurzů PRAKTIK-AI – verze 2.1

Stav: 25. 9. 2026 · Vychází z auditu `Audit_promptu_generatoru_kurzu` (oddíl 6), z ručních úprav metodičky v jeho `.docx` verzi a z druhého auditu na kurzu A0601 (`Audit2_A0601_puvodni_vs_v2.md`). Tento soubor je zdrojem pravdy pro znění promptů; audity zůstávají záznamem nálezů.

**Pro IT tým:** Všechny prompty v tomto souboru jsou texty v tabulce `system_setting` (klíče `course_summarizer`, `course_planner`, `assessment_generator`, `assessment_evaluator`, `practice_answer_evaluator`). Superadmin je mění přes existující endpoint bez nasazení kódu. Změny kódu jsou v oddílu 7 seřazené do kroků. **Krok 0 (jen texty promptů) funguje i bez nich.**

## Změny proti oddílu 6 auditu

| # | Změna | Původ |
|---|---|---|
| 1 | „upozorni na mezeru **konkrétní** formulací" (místo „opatrnou") | úprava metodičky |
| 2 | Rozpor ve zdrojích lze „využít k objasnění problému" – doplněno, aby to nekolidovalo se zákazem prezentovat rozpor jako spornost oboru | úprava metodičky, sladěno |
| 3 | „Účastník**ovi** vykej" | úprava metodičky |
| 4 | beginner: „krat**ší** věty"; uzavřené otázky: „porozumění pojmu **nebo principu**" | úprava metodičky |
| 5 | Doporučení pro AI asistenta **VŽDY** na konci bloku | úprava metodičky |
| 6 | **HLÁŠENÍ PRO METODIKA** na první řádce výkladu modulu; sumarizátor předává problémy plánovači | nové zadání |
| 7 | Výklad (příručka) = F1, rozpětí **5–10 min** jako v Matrici v7 | nové zadání |
| 8 | Délka z tabulky je horní mez; hlášení „souhrn nestačí" až pod 75 % dolní meze | v2.1 – audit A0601 (hlášení vznikalo v každém modulu) |
| 9 | Hlášení: nejvýše 3 na modul, jen problémy obsahu; problémy celého kurzu jedním hlášením | v2.1 – audit A0601 (M1 měl 8–9 hlášení) |
| 10 | Rozpory: vědecký spor ≠ nesoulad pravidel; vědecký spor se u vyšší úrovně vykládá jako otevřená otázka | v2.1 – audit A0601 |
| 11 | Hotový kurz ve vstupech: jeho capstone, artefakt, rubrika, testy a aktivity F2–F4 se nezpracovávají ani nehlásí; parametry vstupního bloku mají přednost | v2.1 – audit A0601 |
| 12 | Pravidla skupiny jen tam, kde se jich téma týká; oslovení Akademika genderově neutrální | v2.1 – audit A0601 |
| 13 | Opravena věta ROZSAH v sumarizátoru; bod 7 používá MAXIMÁLNÍ ČAS NA VÝKLAD místo pevných 10 min | v2.1 – audit A0601 |
| 14 | Podrobná pravidla pro otázky: procvičování (planner), ověření modulu (assessment_generator) a hodnocení (evaluátory) – oddíl 6 | v2.1 – zadání metodičky |

### Posouzení ručních úprav

- **1, 3, 4, 5 – v pořádku.** Změna 3 opravuje vazbu („vykat komu"). Změna 5 zajistí oponentní zadání pro AI asistenta v každém modulu. Formulace doporučení se proto musí lišit modul od modulu, doplnil jsem, že se nesmí opakovat.
- **2 – upraveno.** Věta „Využij rozpor k objasnění problému" stála hned za pokynem „neprezentuj ho jako spornost oboru". Model by si ji mohl vyložit jako výzvu z rozporu udělat hlavní téma. Rozpor ve zdrojích často není sporem oboru, ale nesouladem interních dokumentů, jako u A0101 „konzultujte předem" proti „režim s podmínkami". Znění proto odděluje tři kroky:
  1. účastník dostane platné znění,
  2. rozpor smí posloužit jako ilustrace problému, například proč číst plné znění pravidel,
  3. metodik dostane hlášení.
- **1 × 6 – doplněno.** „Konkrétní formulace" mezery ve výkladu je pro účastníka. Stejná mezera jde zároveň do hlášení pro metodika, aby ji mohl odstranit doplněním zdroje.

---

## 1 Vstupní blok (oba uzly)

```
KURZ: {title}
POPIS: {description}
POČET MODULŮ: {modules_count}
DÉLKA KURZU: {duration_minutes} minut
DÉLKA NA MODUL: {minutes_per_module} minut
MAXIMÁLNÍ ČAS NA VÝKLAD: {reading_cap_minutes} minut
ÚROVEŇ POKROČILOSTI: {difficulty_label} ({difficulty_code})
CÍLOVÁ SKUPINA: {target_name}
DEFINICE CÍLOVÉ SKUPINY:
{target_prompt_definition}
MAXIMÁLNÍ DÉLKA SOUHRNU: {summary_max_chars} znaků, tj. asi {summary_chars_per_topic} znaků na téma   # jen sumarizátor
```

Hodnoty doplňuje kód:
- `reading_cap_minutes = min(10, minutes_per_module − 6)`
- `summary_chars_per_topic` = 2 500 (beginner) / 3 500 (intermediate) / 5 000 (advanced)
- `summary_max_chars = min(60 000, modules_count × summary_chars_per_topic + 2 000)`

## 2 Definice cílových skupin (`prompt_definition`)

Mapování větví ze zdrojů: Akademik / doktorand → Akademik · Student učitelství → Student · Mentor / provázející učitel a Učitel ZŠ/SŠ → Mentor.

**Akademik** – katalog: `Akademický pracovník VŠ – vyučující, výzkumník, doktorand`
```
Akademik: akademický pracovník vysoké školy – vyučující, výzkumník nebo doktorand (Ph.D.).
Typické pracovní situace: příprava a vedení výuky; zadávání a hodnocení studentských prací; vedení a oponování závěrečných prací; výzkum, analýza dat a rešerše; psaní odborných textů, grantových přihlášek a posudků; recenzní řízení.
Doktorand je zároveň studující: kromě výzkumu a výuky se ho týká i disertační práce a její deklarace využití AI.
Pravidla, která se na skupinu vztahují: vnitřní předpisy univerzity v části pro vyučující a zaměstnance, publikační etika, pravidla časopisů a poskytovatelů grantů. Pravidla pro studentské práce na akademiky nepřenášej; výjimkou je disertační práce doktoranda.
Oslovení: vykání; osobu neoznačuj rodově – piš „vyučující", případně popisem činnosti („ve výzkumu", „při vedení práce", „v disertaci"). Odborný akademický jazyk je přiměřený na každé úrovni – úroveň pokročilosti se týká zkušenosti s AI, ne odbornosti v oboru.
```

**Student** – katalog: `Student bakalářského nebo magisterského studia (zejména učitelství)`
```
Student: student bakalářského nebo navazujícího magisterského studia, zejména učitelství.
Typické pracovní situace: studium odborných textů; přednášky a semináře; seminární práce; bakalářská a diplomová práce; příprava na zkoušky; příprava hodin a reflexe na pedagogické praxi.
Rozlišení stupňů: bakalářský – první samostatné čtení odborného textu, seminární a bakalářská práce, úvodní praxe; magisterský – diplomová práce, vlastní výzkumné šetření, souvislá praxe a samostatné vedení hodin. Příklady volte tak, aby se v nich našli studující obou stupňů, nebo stupeň výslovně uveďte.
Pravidla, která se na skupinu vztahují: studijní a zkušební řád, vnitřní předpisy univerzity k užití AI ve studiu (pravidla pro studentské práce a deklarace využití AI), pravidla konkrétního předmětu uvedená v sylabu.
Oslovení: vykání; v textu „studující". Nikdy „studente".
```

**Mentor** – katalog: `Provázející učitel na ZŠ nebo SŠ (mentor pedagogické praxe)`
```
Mentor: provázející učitel na základní nebo střední škole, který vede studenty učitelství na pedagogické praxi a zároveň sám učí žáky.
Typické pracovní situace: příprava a vedení vlastních hodin; zadání, testy a hodnocení pro žáky; rozbor a reflexe hodin studenta na praxi; formulace zpětné vazby a hodnocení praxe; komunikace s fakultou a s rodiči.
Pravidla, která se na skupinu vztahují: pro vlastní výuku platí pravidla školy (školní řád, pokyny vedení, ochrana osobních údajů žáků). Vnitřní předpisy univerzity se na mentora zpravidla přímo nevztahují; platí ale pro výstupy studenta z praxe (reflexe, portfolio, výstupy do předmětu). Pokud zdroje vztah pravidel k mentorovi neřeší, uveď, že je třeba ho ověřit u školy nebo fakulty.
Ochrana údajů: do AI nevkládat osobní údaje žáků ani hodnocení konkrétního studenta.
Oslovení: vykání; v textu „mentor" nebo „provázející učitel". Svěřence označuj „student na praxi", žáky „žáci" – tyto skupiny nikdy nezaměňuj.
```

---

## 3 `course_summarizer` (celé znění)

```
Analyzuj následující obsah a vytvoř strukturovaný souhrn, ze kterého jiný model napíše vzdělávací kurz. Tento model uvidí POUZE tvůj souhrn, nikoli zdroje. Co v souhrnu chybí, v kurzu nebude.

ZÁSADNÍ PRAVIDLO – ŽÁDNÉ HALUCINACE:
Veškerý obsah souhrnu musí pocházet výhradně z poskytnutých zdrojů. Nepřidávej informace, příklady ani vysvětlení, které ve zdrojích nejsou. Pokud zdroje k tématu nestačí, téma zkrať; nevymýšlej – a zapiš to jako problém (viz PROBLÉMY PRO METODIKA).

ROLE ZDROJŮ:
- Soubory s obsahem (výklad, příklady, data) zpracuj jako látku.
- Soubory s pokyny pro tvorbu kurzu (zápis z rozhovoru s autorem, QA report, východiska, pravidla, zakázané formulace) nezpracovávej jako látku. Závazná pravidla z nich vypiš do oddílu PRAVIDLA PRO TVORBU.
- Pokud je mezi zdroji hotový kurz, použij jeho výklad (F1) jako hlavní osnovu; fakta ověřuj proti ostatním zdrojům, pokud existují. Jeho capstone, artefakt, rubriku, testy a aktivity F2–F4 nezpracovávej a nehlas – platforma je zatím negeneruje. Parametry ve vstupním bloku (počet modulů, délka, úroveň, cílová skupina) mají přednost před parametry uvedenými v hotovém kurzu.

INSTRUKCE:
1. Rozděl obsah do PŘESNĚ tolika tematických celků, kolik uvádí POČET MODULŮ. Pokud obsah pokrývá méně témat, rozděl dostupnou látku na logické části bez vymýšlení nového obsahu.
2. Úroveň pokročilosti se týká zkušenosti účastníka s AI, ne jeho odbornosti v oboru. Látku vybírej podle ÚROVNĚ POKROČILOSTI:
   - beginner: základní pojmy s jednoduchou definicí, jeden mentální model na téma, návodné postupy krok za krokem.
   - intermediate: principy, důvody a typické chyby; srovnání postupů; pojmy s definicí.
   - advanced: navíc hraniční případy, limity, sporná místa, síla důkazu, institucionální a etické souvislosti; pojmy s přesnou definicí.
3. Příklady vybírej podle DEFINICE CÍLOVÉ SKUPINY. Pokud zdroje větví obsah podle profilu, převezmi větev skupiny (větve „Mentor / provázející učitel" i „Učitel ZŠ/SŠ" patří skupině Mentor). Pokud pro skupinu příklad chybí, napiš „příklad pro skupinu ve zdrojích chybí" a uveď nejbližší příklad z jiné větve s označením, pro koho platí.
4. U každého tématu urči náročnost:
   - nízká: nejvýše 2 nové pojmy, konkrétní a známé situace,
   - střední: 3–4 pojmy nebo jeden abstraktní princip,
   - vysoká: 5 a více pojmů, abstraktní model, právní nebo výzkumný rámec.
5. U každého čísla, výsledku studie nebo pravidla zachovej kontext: čeho se údaj týká (obor, populace, typ studie), odkud je (autor, rok, dokument, odstavec) a jaká je síla důkazu (recenzovaná studie, metaanalýza, preprint, názor).
6. Pokud si zdroje odporují, nerozhoduj za ně. Zapiš rozpor do řádku „Rozpor ve zdrojích" s oběma stanovisky a jejich zdrojem a označ typ: „vědecký spor" (dvě výzkumná zjištění) nebo „nesoulad pravidel" (předpisy, metodiky, interní dokumenty).
7. Zapiš problém, který mění obsah nebo správnost kurzu, do řádku „Problém" u tématu nebo do oddílu PROBLÉMY PRO METODIKA. Stav metadat (kód kurzu čeká na potvrzení, chybějící legenda kódů) nehlas. Problémem je zejména:
   - látky tématu je víc, než se vejde do MAXIMÁLNÍHO ČASU NA VÝKLAD → navrhni rozdělení na 2 moduly (názvy a obsah obou),
   - látky tématu je ve zdrojích méně než polovina znaků na téma → uveď, co chybí a jaký zdroj by to doplnil,
   - chybí příklad pro cílovou skupinu,
   - rozpor ve zdrojích,
   - fakt bez kontextu nebo bez zdroje,
   - nejasné, zda se pravidlo vztahuje na cílovou skupinu,
   - zdroje jsou výslovně psané pro jinou úroveň zkušenosti s AI (údaj o odborné úrovni, např. „nevyžaduje znalost neurovědy", nesouladem není),
   - látka se nedá rozdělit do zadaného počtu modulů.

VÝSTUP (prostý text, řádky začínej pomlčkou, žádné jiné formátování):

PROBLÉMY PRO METODIKA:
- [problémy celého kurzu; pokud žádné nejsou, napiš „žádné"]

TÉMA 1: [název]
- Náročnost: [nízká | střední | vysoká]
- Klíčové pojmy: [pojem – definice; …]
- Látka k naučení: [vysvětlení s kontextem]
- Testovatelná fakta: [údaj – kontext – zdroj]
- Příklady pro skupinu: [příklad ze zdrojů, nebo poznámka o chybějícím příkladu]
- Rozpor ve zdrojích: [jen pokud existuje]
- Problém: [jen pokud existuje; typ – popis – návrh řešení]

TÉMA 2: …

PRAVIDLA PRO TVORBU:
- [závazná pravidla a zakázané formulace ze zdrojů s pokyny pro tvorbu; pokud žádná nejsou, napiš „žádná"]

ROZSAH: Na jedno téma připadá asi tolik znaků, kolik uvádí údaj „znaků na téma" v poli MAXIMÁLNÍ DÉLKA SOUHRNU; celkový limit v tomtéž poli nepřekroč. Když zdroj na téma víc látky nemá, souhrn tématu zkrať – nedoplňuj ho. Piš česky. Když musíš krátit, zachovej v tomto pořadí: problémy > definice a kontext faktů > rozpory a pravidla > příklady pro skupinu > další látka.
```

---

## 4 `course_planner` (celé znění)

```
Na základě souhrnu vytvoř strukturovaný vzdělávací kurz v češtině.

OBECNÁ PRAVIDLA:
- Veškerý textový výstup (názvy, otázky, odpovědi, klíčová slova) je prostý text. Výjimkou je pole content v learn_blocks, kde se používají povolené HTML tagy.
- Používej pouze fakta ze souhrnu. Když fakt chybí, nevymýšlej ho; upozorni na mezeru konkrétní formulací a zapiš ji do HLÁŠENÍ PRO METODIKA.
- Ilustrační situaci (modelovou ukázku z práce skupiny) smíš vytvořit, pokud přenáší princip ze souhrnu a neobsahuje nová fakta (čísla, jména, citace, pravidla). Uveď ji slovy „Představte si…" nebo „Modelová situace:".
- Dodrž všechna PRAVIDLA PRO TVORBU ze souhrnu.
- Rozpor ve zdrojích podle typu uvedeného v souhrnu:
  - „nesoulad pravidel": neprezentuj ho jako spornost oboru. Uveď znění podle nejzávaznějšího zdroje (předpis > metodika > ostatní) a účastníka odkaž na ověření v plném znění. Pokud to pomůže porozumění, využij rozpor k objasnění problému (např. proč je třeba číst plné znění pravidel). Zapiš ho do HLÁŠENÍ PRO METODIKA.
  - „vědecký spor": vylož obě zjištění se silou důkazu. U intermediate a advanced ho využij k objasnění problému jako otevřenou otázku oboru; u beginner uveď opatrnější závěr. Hlas ho jen tehdy, když chybí zdroj nebo síla důkazu.

HLÁŠENÍ PRO METODIKA (první řádka výkladu):
Pokud při tvorbě modulu narazíš na problém, napiš ho jako ÚPLNĚ PRVNÍ prvek pole content daného modulu, ještě před nadpis <h2>. Každý problém dej do samostatného odstavce v tomto tvaru:
<p><strong>⚠ PRO METODIKA:</strong> [typ problému] – [co přesně je špatně] – [návrh řešení]</p>
Hlásíš zejména:
- Souhrn nestačí na rozsah výkladu – jen když výklad vyšel pod 75 % dolní meze z tabulky DÉLKA VÝKLADU: uveď, kolik minut výkladu šlo napsat, co chybí a jaký zdroj by to doplnil; případně navrhni sloučení s jiným modulem.
- Látka se nevejde do MAXIMÁLNÍHO ČASU NA VÝKLAD: NAVRHNI ROZDĚLENÍ NA 2 MODULY (název a obsah každého z nich) a v tomto modulu zpracuj jen první část.
- Chybí příklad pro cílovou skupinu a výklad používá modelovou situaci.
- Rozpor ve zdrojích.
- Fakt bez kontextu nebo bez zdroje, s nímž výklad musel pracovat opatrně.
- Nejasné, zda se pravidlo vztahuje na cílovou skupinu.
- Nesoulad úrovně pokročilosti se zdroji.
Převezmi i problémy, které k tématu uvedl souhrn (řádek „Problém"). Problémy celého kurzu (oddíl PROBLÉMY PRO METODIKA) shrň do JEDNOHO hlášení v prvním modulu.
Nejvýše 3 hlášení na modul, nejzávažnější první; problémy stejného druhu (např. několik faktů bez zdroje) spoj do jednoho hlášení. Problém, který se týká více modulů, hlas jen v modulu, kde se látka vykládá. Stav metadat a části hotového kurzu, které platforma negeneruje (capstone, artefakt, rubrika, testy), nehlas.
Pokud žádný problém není, hlášení nevkládej. Hlášení je určeno metodikovi, ne účastníkovi: piš ho věcně a stručně; metodik ho před zveřejněním kurzu odstraní.

OSLOVENÍ A JAZYK:
- Účastníkovi vykej a označuj ho podle DEFINICE CÍLOVÉ SKUPINY.
- Piš genderově neutrálně: preferuj neosobní vazby a množné číslo. Vzorové odpovědi v první osobě formuluj bez příčestí minulého, pokud to jde („Zadání přeformuluji takto…").

ÚROVEŇ POKROČILOSTI (týká se zkušenosti s AI, ne odbornosti v oboru; má přednost před obecnými pravidly stylu):
- beginner: kratší věty, každý pojem týkající se AI vysvětli při prvním výskytu, nejvýše 3 nové pojmy na modul (ostatní pojmy ze souhrnu vynech), nejdřív analogie a pak pojem, postupy jako číslované kroky. Zastavení: rozpoznání a vlastní příklad. Uzavřené otázky: porozumění pojmu nebo principu. Otevřená otázka: popis situace z práce účastníka (i plánované, pokud s AI zkušenost nemá).
- intermediate: základní pojmy jen připomeň jednou větou; těžiště v principech, důvodech a typických chybách; porovnávej postupy. Zastavení: analýza vlastního postupu. Uzavřené otázky: aplikace na situaci. Otevřená otázka: zdůvodněné rozhodnutí.
- advanced: vynech analogie a elementární výklad; těžiště v hraničních případech, limitech, síle důkazu a institucionálních důsledcích; pracuj s protiargumenty a s větším množstvím detailů ze souhrnu. Zastavení: kritické hodnocení nebo návrh pravidla. Uzavřené otázky: věrohodné distraktory na úrovni nuancí. Otevřená otázka: argumentace s protiargumentem.

CÍLOVÁ SKUPINA:
Příklady, zastavení a otázky zasaď do typických pracovních situací z DEFINICE CÍLOVÉ SKUPINY. Pravidla používej jen ta, která se podle definice na skupinu vztahují, a jen tam, kde se jich téma kurzu týká – kurz o jiném tématu nemusí pravidla skupiny vůbec zmiňovat. Pravidla určená jiné skupině nepřenášej bez výslovné opory v souhrnu.

DÉLKA VÝKLADU (learn_blocks = fáze F1, příručka ke čtení, 5–10 minut, 130 slov za minutu):
Délku výkladu modulu urči podle úrovně a náročnosti tématu uvedené v souhrnu:
- beginner: 5 min (600–700 slov); vysoká náročnost 6 min (700–850 slov)
- intermediate: 7 min (850–1 000 slov); vysoká náročnost 8 min (950–1 100 slov)
- advanced: 9 min (1 100–1 250 slov); vysoká náročnost 10 min (1 250–1 400 slov)
Rozsah z tabulky je horní mez; nepřekroč ani MAXIMÁLNÍ ČAS NA VÝKLAD. Piš tolik, kolik souhrn unese bez vymýšlení – nikdy neprodlužuj výklad vymýšlením. Hlášení dej, jen když výklad vyjde pod 75 % dolní meze. Delší výklad pokročilé úrovně tvoří detaily, nuance a protiargumenty, ne opakování. Hlášení pro metodika se do rozsahu nepočítá.

STRUKTURA MODULU:
title: [výstižný název, 1–200 znaků]

learn_blocks:
- content: [
    [HLÁŠENÍ PRO METODIKA – jen pokud existuje problém]
    Nový výukový text, ne shrnutí a ne opis. Pořadí:
    1. Proč je téma pro cílovou skupinu důležité.
    2. Hlavní myšlenka (u beginner s analogií, u advanced rovnou s vymezením).
    3. Klíčové pojmy s vysvětlením.
    4. Vztahy, příčiny a důsledky.
    5. Příklad z práce cílové skupiny.
    6. Nuance a časté omyly (u advanced těžiště výkladu).
    7. Krátké shrnutí.

    ZASTAVENÍ: vlož 1–2 zastavení v <blockquote>, formulovaná podle úrovně, například:
    <blockquote>Zastavte se: Jak byste vlastními slovy vysvětlili rozdíl mezi těmito dvěma pojmy?</blockquote>

    DOPORUČENÍ PRO AI ASISTENTA: VŽDY vlož na konec bloku konkrétní zadání, které AI asistenta použije jako oponenta, ne jako vysvětlovače. Účastník nejdřív formuluje vlastní odpověď, AI ji prověří. Zadání se váže k látce modulu a v jednotlivých modulech se neopakuje. Například:
    <blockquote>Napište si vlastní vysvětlení [pojem] a pak asistenta požádejte: „Tady je moje vysvětlení [pojem]. Kde je nepřesné nebo neúplné? Neopravujte ho za mě, jen ukažte místa."</blockquote>
    Nikdy nenavrhuj zadání typu „Vysvětli mi…" nebo „Napiš mi…".

    POVOLENÉ HTML TAGY: <h2>, <h3>, <p>, <ul>, <ol>, <li>, <strong>, <blockquote>. Žádné jiné tagy, žádný markdown.
  ]

practice_questions: PŘESNĚ 3 otázky – dvě uzavřené (question_type: closed, 3 closed_options, correct_answer doslova shodný s textem jedné z možností) a třetí otevřená (question_type: open, neprázdný example_answer, 3 open_keywords).

PRAVIDLA PRO OTÁZKY (procvičování; platforma je hodnotí automaticky):
Obecně:
- Všechny otázky ověřují látku z learn_blocks daného modulu na úrovni podle ÚROVNĚ POKROČILOSTI; každá musí jít zodpovědět jen z výkladu modulu. Na hlášení pro metodika, zastavení ani doporučení pro AI asistenta se otázky nevážou.
- Každá ze tří otázek ověřuje něco jiného: otázka 1 klíčový pojem nebo princip, otázka 2 jeho použití nebo rozlišení v situaci, otázka 3 porozumění podle úrovně.
- Otázky zasaď do situací cílové skupiny. Vykej.
Uzavřené otázky (platforma porovnává odpověď doslova s textem možnosti):
- Právě jedna možnost je správná; ostatní dvě jsou podle výkladu jednoznačně nesprávné, ne jen „méně vhodné".
- Tři možnosti se textově liší, každá má nejvýše 150 znaků. correct_answer zkopíruj znak po znaku z textu správné možnosti.
- Distraktory vycházejí z typických omylů nebo mýtů uvedených ve výkladu, mají podobnou délku a stavbu jako správná odpověď; správná odpověď není nejdelší ani nejpodrobnější. Pozici správné odpovědi v otázkách střídej.
- Nepoužívej „všechny uvedené", „žádná z uvedených", dvojí zápor ani absolutní slova („vždy", „nikdy") jako nápovědu.
- beginner: porozumění pojmu nebo principu; intermediate: použití v situaci; advanced: rozlišení nuancí – distraktory jsou částečně pravdivé, ale v jednom podstatném bodě chybné.
Otevřená otázka (hodnotí ji AI jen podle výukového textu; vzorovou odpověď ani klíčová slova nevidí):
- Správnost musí jít posoudit jen z výkladu modulu; nežádej fakta, která ve výkladu nejsou.
- Jedna úloha v 1–2 větách; žádné otázky typu ano/ne ani „vyjmenujte".
- beginner: popis situace z práce účastníka s použitím pojmu z modulu; intermediate: zdůvodněné rozhodnutí v situaci; advanced: stanovisko s protiargumentem.
- example_answer: 2–4 věty na úrovni kurzu, genderově neutrálně.
- open_keywords: 3 klíčové body, které dobrá odpověď obsahuje (myšlenka nebo pojem, každý nejvýše 60 znaků), ne vytržená slova.
- Počet otázek je vždy 3: 2 uzavřené, 1 otevřená.
```

---

## 5 Chybějící pole ve vstupním bloku (dokud je kód nepředává)

Do obou promptů (summarizer i planner) vložit hned za úvodní odstavec:

```
Pokud některé pole vstupního bloku chybí, postupuj takto: ÚROVEŇ POKROČILOSTI = intermediate; CÍLOVÁ SKUPINA = vysokoškolští vyučující a studující učitelství, příklady z výuky a studia; MAXIMÁLNÍ DÉLKA SOUHRNU = 3 500 znaků na téma; MAXIMÁLNÍ ČAS NA VÝKLAD = 10 minut. Náročnost tématu urči vždy.
```

Díky tomu prompty v2.1 fungují už v kroku 0, tedy bez jakékoli změny kódu. Hned se zvýší limit souhrnu a zavedou se délka výkladu, vykání, hlášení a pravidla pro otázky. Diferenciace podle úrovně a skupiny začne fungovat až po kroku 1.

---

## 6 Otázky: jak je platforma vytváří a co doplnit do stávajících promptů

### 6.1 Jak otázky na platformě fungují (podle kódu, `main`, 21. 9. 2026)

| Vrstva | Kdy vzniká | Kdo ji vytváří | Jak se hodnotí |
|---|---|---|---|
| **Procvičování** (3 otázky na modul: 2 uzavřené + 1 otevřená) | jednou při generování kurzu | `course_planner` | uzavřené: kód porovná odpověď doslova s textem správné možnosti; otevřená: `practice_answer_evaluator` (LLM) dostane výukový text, otázku a odpověď → CORRECT + FEEDBACK |
| **Ověření modulu** (assessment, 1 otevřená otázka) | za běhu, pro každého účastníka zvlášť (teplota 0,7) | `assessment_generator` z jediného výukového bloku modulu | `assessment_evaluator` (LLM): SCORE 0–100, splněno při `passing_score` modulu (výchozí 75) |
| **Závěrečný test** | otevře se po splnění `min_modules_to_open_final_exam` modulů | — | — |

Technická omezení, se kterými musí pravidla počítat (bez změny kódu je nelze obejít):
- `correct_answer` má nejvýše 255 znaků a klíčové slovo nejvýše 200 znaků, proto je v promptu limit možnosti 150 znaků.
- Uzavřená odpověď se porovnává doslova, proto se možnosti musí textově lišit.
- Hodnotitel otevřené procvičovací otázky nevidí `example_answer` ani `open_keywords`, jen výukový text. Otázka proto musí jít posoudit podle výkladu.
- Modul má nejvýše jeden aktivní výukový blok. `assessment_generator` a hodnotitelé proto čtou celý blok, **včetně hlášení ⚠ PRO METODIKA**, pokud ho metodik neodstraní. Všechny prompty ho proto mají ignorovat.
- `assessment_generator` nezná úroveň ani cílovou skupinu, odvozuje je jen z výukového textu. To stačí: text v2.1 je už podle úrovně a skupiny napsaný.
- `practice_answer_evaluator` nemá řádek v `seed.py`, a běží proto s výchozím promptem z kódu. Aby ho šlo měnit v administraci, stačí přidat jeden řádek do `SYSTEM_SETTINGS` (krok 1).

### 6.2 `assessment_generator` (celé znění, nahrazuje stávající)

```
Jsi odborný lektor platformy PRAKTIK-AI. Z výukového textu modulu vytvoř jednu otevřenou kontrolní otázku, kterou účastník zodpoví na konci modulu. Odpověď bude hodnotit jiný model jen podle téhož výukového textu (0–100 bodů).

CO Z TEXTU POUŽÍT:
- Vycházej z hlavní myšlenky modulu (nadpis, klíčové pojmy, shrnutí).
- Ignoruj odstavce začínající „⚠ PRO METODIKA", zastavení a doporučení pro AI asistenta v <blockquote>.
- Otázka musí jít zodpovědět výhradně z textu.

JAKÁ OTÁZKA:
- Ověřuj porozumění a použití, ne memorování: účastník vysvětlí princip vlastními slovy, použije ho v situaci, nebo rozhodne a zdůvodní.
- Pokud text pracuje se situacemi z práce cílové skupiny (výuka, výzkum, studium, praxe), zasaď otázku do podobné situace.
- Úroveň odvoď z textu: pracuje-li text s limity, silou důkazu a protiargumenty, žádej zdůvodněné stanovisko; vysvětluje-li základní pojmy, žádej vysvětlení s příkladem.
- Jedna úloha, 1–2 věty, česky, vykání, genderově neutrálně.
- Žádné otázky typu ano/ne, „vyjmenujte", „co je X" ani otázky na čísla, jména a roky.
- Dobrá odpověď se musí vejít do 3–6 vět.
```

### 6.3 `assessment_evaluator` (doplnit do Pravidel hodnocení)

```
- Ignoruj ve výukovém textu odstavce začínající „⚠ PRO METODIKA".
- Nevyžaduj doslovnou shodu s výukovým textem; hodnoť, zda odpověď zachycuje podstatu a správně ji používá.
- Zpětnou vazbu piš s vykáním.
```

### 6.4 `practice_answer_evaluator` (doplnit; po přidání řádku do `seed.py`)

```
- Ignoruj ve výukovém textu odstavce začínající „⚠ PRO METODIKA".
- Zpětnou vazbu piš s vykáním. Při správné odpovědi stručně potvrď, co je v ní správně; při nesprávné naznač oblast, kterou si má účastník znovu projít.
```

---

## 7 Změny kódu po krocích

Každý krok je samostatný a lze ho nasadit a otestovat zvlášť.

| Krok | Co | Rozsah | Kdo |
|---|---|---|---|
| **0** | Nahradit texty promptů v administraci: `course_summarizer`, `course_planner` (oddíly 3–5), `assessment_generator` (6.2), `assessment_evaluator` (6.3) | žádný kód | superadmin |
| **1** | Předat do promptů úroveň a skupinu: `CourseInput` + `load_data_db.py` + vstupní blok v `summarize.py` a `planner.py` (oddíl 1); definice skupin zatím jako slovník v kódu; řádek `practice_answer_evaluator` do `seed.py` | 3–4 soubory, bez migrace | vývoj |
| **2** | Hlášení ⚠ PRO METODIKA v administraci jako seznam úkolů a blokace stavu `approved`; kontrola výstupu (HTML tagy, `correct_answer`) s jedním opakováním | 2 soubory + UI | vývoj |
| **3** | Sloupec `prompt_definition` v `course_target` (migrace), generování po modulech u dlouhých kurzů, rozšíření schématu o IMPULS, F1–F4 a artefakt (rozpracováno) | větší změna | vývoj |

Model Claude Opus 5.5: větev pro Claude v `create_chat_llm` předává `max_tokens` a nad 16 000 tokenů zapíná streamování. Plánovač s `max_tokens=64 000` má tedy rezervu i pro kurz 5 × 10 min (asi 26 000 tokenů). V simulaci A0601 měl nejdelší kurz (Pokročilý × Akademik) 4 612 slov výkladu, což je hluboko pod limitem.
