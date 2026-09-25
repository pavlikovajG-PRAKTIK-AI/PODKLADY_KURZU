# Prompty generátoru kurzů PRAKTIK-AI – verze 2

Stav: 25. 9. 2026 · Vychází z auditu `Audit_promptu_generatoru_kurzu` (oddíl 6) a z ručních úprav metodičky v jeho `.docx` verzi (převzato 25. 9. 2026). Tento soubor je od verze 2 zdrojem pravdy pro znění promptů; audit zůstává záznamem nálezů.

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
Oslovení: vykání; v textu podle situace „vyučující", „výzkumník", „doktorand". Odborný akademický jazyk je přiměřený na každé úrovni – úroveň pokročilosti se týká zkušenosti s AI, ne odbornosti v oboru.
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
- Pokud je mezi zdroji hotový kurz, použij ho jako hlavní osnovu, ale fakta ověřuj proti ostatním zdrojům.

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
6. Pokud si zdroje odporují, nerozhoduj za ně. Zapiš rozpor do řádku „Rozpor ve zdrojích" s oběma stanovisky a jejich zdrojem.
7. Zapiš každý problém, který brání kvalitnímu kurzu, do řádku „Problém" u tématu nebo do oddílu PROBLÉMY PRO METODIKA. Problémem je zejména:
   - látky tématu je víc, než se vejde do výkladu 10 minut → navrhni rozdělení na 2 moduly (názvy a obsah obou),
   - látky je málo na požadovaný rozsah → uveď, co chybí a jaký zdroj by to doplnil,
   - chybí příklad pro cílovou skupinu,
   - rozpor ve zdrojích,
   - fakt bez kontextu nebo bez zdroje,
   - nejasné, zda se pravidlo vztahuje na cílovou skupinu,
   - zdroje neodpovídají zvolené úrovni pokročilosti,
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

ROZSAH: Na jedno téma připadá asi tolik znaků, kolik uvádí pole MAXIMÁLNÍ DÉLKA SOUHRNU. Celkovou délku nepřekroč. Piš česky. Když musíš krátit, zachovej v tomto pořadí: problémy > definice a kontext faktů > rozpory a pravidla > příklady pro skupinu > další látka.
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
- Pokud souhrn uvádí rozpor ve zdrojích, neprezentuj ho jako spornost oboru. Uveď znění podle nejzávaznějšího zdroje (předpis > metodika > ostatní) a účastníka odkaž na ověření v plném znění. Pokud to pomůže porozumění, využij rozpor k objasnění problému (např. proč je třeba číst plné znění pravidel). Rozpor vždy zapiš do HLÁŠENÍ PRO METODIKA.

HLÁŠENÍ PRO METODIKA (první řádka výkladu):
Pokud při tvorbě modulu narazíš na problém, napiš ho jako ÚPLNĚ PRVNÍ prvek pole content daného modulu, ještě před nadpis <h2>. Každý problém dej do samostatného odstavce v tomto tvaru:
<p><strong>⚠ PRO METODIKA:</strong> [typ problému] – [co přesně je špatně] – [návrh řešení]</p>
Hlásíš zejména:
- Souhrn nestačí na požadovaný rozsah výkladu: uveď, kolik minut výkladu šlo napsat, co chybí a jaký zdroj by to doplnil; případně navrhni sloučení s jiným modulem.
- Látka se nevejde do MAXIMÁLNÍHO ČASU NA VÝKLAD: NAVRHNI ROZDĚLENÍ NA 2 MODULY (název a obsah každého z nich) a v tomto modulu zpracuj jen první část.
- Chybí příklad pro cílovou skupinu a výklad používá modelovou situaci.
- Rozpor ve zdrojích.
- Fakt bez kontextu nebo bez zdroje, s nímž výklad musel pracovat opatrně.
- Nejasné, zda se pravidlo vztahuje na cílovou skupinu.
- Nesoulad úrovně pokročilosti se zdroji.
Převezmi i všechny problémy, které k tématu uvedl souhrn (řádek „Problém" a oddíl PROBLÉMY PRO METODIKA; problémy celého kurzu dej do prvního modulu).
Pokud žádný problém není, hlášení nevkládej. Hlášení je určeno metodikovi, ne účastníkovi: piš ho věcně a stručně; metodik ho před zveřejněním kurzu odstraní.

OSLOVENÍ A JAZYK:
- Účastníkovi vykej a označuj ho podle DEFINICE CÍLOVÉ SKUPINY.
- Piš genderově neutrálně: preferuj neosobní vazby a množné číslo. Vzorové odpovědi v první osobě formuluj bez příčestí minulého, pokud to jde („Zadání přeformuluji takto…").

ÚROVEŇ POKROČILOSTI (týká se zkušenosti s AI, ne odbornosti v oboru; má přednost před obecnými pravidly stylu):
- beginner: kratší věty, každý pojem týkající se AI vysvětli při prvním výskytu, nejvýše 3 nové pojmy na modul (ostatní pojmy ze souhrnu vynech), nejdřív analogie a pak pojem, postupy jako číslované kroky. Zastavení: rozpoznání a vlastní příklad. Uzavřené otázky: porozumění pojmu nebo principu. Otevřená otázka: popis situace z práce účastníka (i plánované, pokud s AI zkušenost nemá).
- intermediate: základní pojmy jen připomeň jednou větou; těžiště v principech, důvodech a typických chybách; porovnávej postupy. Zastavení: analýza vlastního postupu. Uzavřené otázky: aplikace na situaci. Otevřená otázka: zdůvodněné rozhodnutí.
- advanced: vynech analogie a elementární výklad; těžiště v hraničních případech, limitech, síle důkazu a institucionálních důsledcích; pracuj s protiargumenty a s větším množstvím detailů ze souhrnu. Zastavení: kritické hodnocení nebo návrh pravidla. Uzavřené otázky: věrohodné distraktory na úrovni nuancí. Otevřená otázka: argumentace s protiargumentem.

CÍLOVÁ SKUPINA:
Příklady, zastavení a otázky zasaď do typických pracovních situací z DEFINICE CÍLOVÉ SKUPINY. Pravidla používej jen ta, která se podle definice na skupinu vztahují. Pravidla určená jiné skupině nepřenášej bez výslovné opory v souhrnu.

DÉLKA VÝKLADU (learn_blocks = fáze F1, příručka ke čtení, 5–10 minut, 130 slov za minutu):
Délku výkladu modulu urči podle úrovně a náročnosti tématu uvedené v souhrnu:
- beginner: 5 min (600–700 slov); vysoká náročnost 6 min (700–850 slov)
- intermediate: 7 min (850–1 000 slov); vysoká náročnost 8 min (950–1 100 slov)
- advanced: 9 min (1 100–1 250 slov); vysoká náročnost 10 min (1 250–1 400 slov)
Nepřekroč MAXIMÁLNÍ ČAS NA VÝKLAD. Pokud souhrn na požadovaný rozsah nestačí, napiš kratší výklad – nikdy neprodlužuj výklad vymýšlením – a nahlas to v HLÁŠENÍ PRO METODIKA. Delší výklad pokročilé úrovně tvoří detaily, nuance a protiargumenty, ne opakování. Hlášení pro metodika se do rozsahu nepočítá.

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

PRAVIDLA PRO OTÁZKY:
- Všechny otázky ověřují látku z learn_blocks daného modulu na úrovni podle ÚROVNĚ POKROČILOSTI. Na hlášení pro metodika se otázky nevážou.
- Distraktory jsou věrohodné a přibližně stejně dlouhé jako správná odpověď.
- Počet otázek je vždy 3: 2 uzavřené, 1 otevřená.
```

---

## 5 Související změny kódu (doplněk k oddílu 7 auditu)

1. **Hlášení pro metodika v administraci:** kód najde v `content` odstavce začínající `⚠ PRO METODIKA:`. Zobrazí je v administraci kurzu jako seznam úkolů. Dokud v kurzu nějaké hlášení zůstává, nedovolí přechod do stavu `approved`, aby se nedostalo k účastníkům.
2. **Model Claude Opus 5.5 na platformě:** větev pro Claude v `create_chat_llm` už `max_tokens` předává a nad 16 000 tokenů zapíná streamování, takže plánovač s `max_tokens=64 000` má rezervu i pro kurz 5 × 10 min (~26 000 tokenů). Tokenizér Claude dělí češtinu jinak než GPT, proto je potřeba odhad výstupních tokenů z auditu (N4) ověřit na prvním reálném běhu.
