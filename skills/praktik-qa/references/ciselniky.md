# Číselníky PRAKTIK-AI (výpis z Matrice kurzu v7.2)

Read-only. Odkazuj kódy (NP-xx, FMT-xxx, KRAUU x.y), nikdy celým textem. Zdroj: `MatriceVer7/PRAKTIK-AI_Matrice_kurzu_v7.2.xlsx`, listy CIS_*.

**Závaznost (rozhodnutí J. Pavlíkové, 18. 10. 2026):** kódy a výčty, které čte platforma, určuje soubor programátorů `09_Kurzy/TEST1_PodkladyKurzu/PRAKTIK-AI_ciselniky.xlsx` (15. 10. 2026); metodici ho nemění. Obsah, který tento soubor nemá nebo má ve stavu Matrice v6, se řídí Maticí v7.2. Proto zde platí kódy FMT-PRB a FMT-DVL (Matrice v7.2 uvádí FMT-OTA a FMT-PRO) a šest typů OBJECTIVES s kódy `obj.*` (Matrice v7.2 uvádí tři typy).

## Neurovědní principy (NP-01 až NP-20)

V kurzu vyber 4–12 principů, u každého modulu uveď 2–5 kódů s fází, kde se uplatní. Principy se uživateli nikdy nepojmenovávají, jsou zabudované ve struktuře aktivit. Popisy jsou z Matrice v7.2 a drží míru jistoty doložených zjištění; v textu kurzu je nezesiluj. Sloupec příkladů se upravuje později (u NP-11 příklad tvrdí víc než popis: kurz netvrdí, že překvapení zlepší zapamatování).

| Kód | Princip | EN | Popis | Příklad využití při učení s AI |
|---|---|---|---|---|
| NP-01 | Neuroplasticita | Neuroplasticity | Zkušenost a učení mění nervové spoje; strukturní přestavba mozku (prořezávání synapsí, zrání bílé hmoty) pokračuje do rané dospělosti. | Pravidelné dialogy s AI nad jedním tématem (např. denní debata o ML konceptech) postupně utvářejí stabilní expertní okruhy. |
| NP-02 | Distribuované opakování | Spaced Repetition | Učení rozložené v čase vede k trvalejšímu zapamatování než nárazové studium díky opakovanému přepisování paměťové stopy. | AI plánuje Anki-styl připomínky (1 den, 3 dny, 7 dní, 21 dní) na klíčové pojmy z předchozí konverzace. |
| NP-03 | Aktivní vybavování | Active Recall / Retrieval Practice | Vědomé vybavování informace z paměti posiluje paměťovou stopu výrazně více než pasivní opětovné čtení. | AI nevykládá rovnou odpověď, ale vede uživatele sokratovskými otázkami: „Co si myslíš, že se stane, když…? |
| NP-04 | Žádoucí obtíže | Desirable Difficulties | Obtíže při učení mohou zlepšit dlouhodobé zapamatování a transfer, pokud je učící se dokáže zvládnout; jinak přestávají být žádoucí (Bjork). | AI postupně zvyšuje náročnost úloh, místo aby okamžitě poskytla zjednodušené řešení. |
| NP-05 | Prokládání | Interleaving | Střídání podobných typů úloh nebo příkladů může zlepšit rozlišování pojmů; účinek závisí na materiálu (u výkladových textů nejednoznačný, u slovíček opačný). | AI při procvičování matematiky míchá derivace, integrály a limity místo blokového řešení jednoho typu. |
| NP-06 | Duální kódování | Dual Coding | Kombinace slovní a obrazové reprezentace může usnadnit zapamatování (teorie duálního kódování, Paivio). | AI doplní textové vysvětlení diagramem, schématem nebo ASCII vizualizací procesu. |
| NP-07 | Kognitivní zátěž | Cognitive Load Theory | Pracovní paměť má pro nové informace omezenou kapacitu (zhruba 3–5 bloků); přetížení zhoršuje učení. Pro informace z dlouhodobé paměti toto omezení prakticky neplatí. | AI rozloží komplexní úlohu (např. návrh API) do dílčích kroků a neřeší vše naráz. |
| NP-08 | Elaborativní kódování | Elaborative Encoding | Propojení nové informace s již existujícími znalostmi tvoří hustší síť asociací a usnadňuje budoucí vybavení. | AI se ptá: „K čemu z toho, co už znáš, by se to dalo přirovnat?“ a buduje analogie. |
| NP-09 | Efekt generování | Generation Effect | Informace, kterou si člověk sám vytvoří či odvodí, se pamatuje lépe než přečtená; velikost efektu závisí na tom, jak volné je zadání. | AI vyzve uživatele k prvnímu pokusu o řešení, teprve pak komentuje a opraví. |
| NP-10 | Testovací efekt | Testing Effect | Samotné testování (nikoli jen studium) je silným nástrojem konsolidace dlouhodobé paměti. | AI po každé lekci generuje krátký kvíz nebo praktickou úlohu k ověření porozumění. |
| NP-11 | Predikční chyba | Reward Prediction Error | Dopaminový systém reaguje na rozdíl mezi očekáváním a výsledkem (doloženo u primátů, Schultz); že překvapení zlepší zapamatování ve výuce, je přenos, ne doložené zjištění. | AI nechá uživatele hádat výsledek experimentu před jeho odhalením — překvapení posílí zapamatování. |
| NP-12 | Konsolidace ve spánku | Sleep-Dependent Consolidation | Spánek po učení podporuje upevnění paměti (metaanalýza: střední účinek u epizodické paměti). Podle převládajícího modelu se při hlubokém spánku stopy reaktivují a přesouvají z hipokampu do neokortexu. | AI doporučí naučit se klíčové pojmy večer a otestovat je ráno; plánuje opakování přes noční pauzu. |
| NP-13 | Pozornost a pracovní paměť | Attention & Working Memory | Pozornost je předpokladem kódování; dělení pozornosti mezi úlohy zhoršuje porozumění, zejména při časové tísni. Pracovní paměť je úzkým hrdlem učení. | AI navrhne 25minutové zaměřené bloky (Pomodoro) bez paralelního multitaskingu. |
| NP-14 | Slučování do bloků (chunking) | Chunking | Sdružování dílčích informací do smysluplných bloků zvyšuje efektivní kapacitu pracovní paměti. | AI pomůže vytvořit mnemotechnické zkratky či vzorce, kterými se nahradí dlouhé seznamy detailů. |
| NP-15 | Metakognice | Metacognition | Schopnost přemýšlet o vlastním myšlení a sledovat porozumění; zásadní pro samostatné a hluboké učení. | AI se průběžně ptá: „Na škále 1–5, jak jistě tomu rozumíš? Co je nejasné?“ |
| NP-16 | Zrcadlové neurony / observační učení | Mirror Neurons / Observational Learning | Lidé se učí i pozorováním postupu a výsledků druhých (observační učení). Zrcadlové neurony podle přehledů souvisejí hlavně se zpracováním pozorovaných pohybů, ne s porozuměním záměrům či myšlení. | AI demonstruje řešení formou „myslím nahlas“ (chain-of-thought), který může uživatel napodobit. |
| NP-17 | Stav plynutí (flow) | Flow State | Prožitek plynutí (Csíkszentmihályi) souvisí se studijními výsledky; jde o korelační data, kauzální vliv na učení doložen není. | AI dynamicky kalibruje obtížnost úloh podle úspěšnosti uživatele, aby udržela engagement. |
| NP-18 | Okamžitá zpětná vazba | Immediate Feedback Loops | Zpětná vazba účinkuje tím víc, čím víc informace nese (co a jak zlepšit); samotná odměna nebo pochvala má malý účinek. Výhodu okamžité zpětné vazby před odloženou metaanalýzy netestovaly. | AI hned po odpovědi vysvětlí, proč je správná/chybná, a navrhne konkrétní opravu. |
| NP-19 | Vtělené poznávání | Embodied Cognition | Gesta mohou pomoci při učení slovní zásoby cizího jazyka; pozorování gest bylo stejně účinné jako jejich provádění. Obecnější tvrzení (řeč nahlas, kreslení) nejsou ověřena. | AI vybízí uživatele, aby vysvětlil problém vlastními slovy nahlas nebo si jej načrtl na papír. |
| NP-20 | Schémata | Schema Theory | Znalosti jsou v paměti organizovány do schémat; nové informace se snáze ukládají, lze-li je připojit k existujícímu schématu. | AI pomáhá tvořit pojmové mapy a hierarchie, do nichž se postupně doplňují další detaily. |

## Formáty interakce F2/F3 (FMT)

Výchozí volba pro F2 je dialogický formát (FMT-SOK, FMT-VLA, FMT-DVL, FMT-PRB, FMT-MIK). Uzavřené formáty patří do F3 tam, kde se ověřuje faktografie, a do skip-testů. FMT-RUB a FMT-ART jsou jen pro finální ověření.

| Kód | Kategorie | Název | Popis | Role AI | Náročnost IT |
|---|---|---|---|---|---|
| FMT-MCQ | Uzavřený | Multiple choice | Výběr z možností; testuje faktografii a porozumění konceptům. | Generátor + hodnotitel | Nízká |
| FMT-TF | Uzavřený | True / false | Pravda / nepravda; rychlé ověření klíčových tvrzení. | Generátor + hodnotitel | Nízká |
| FMT-MTC | Uzavřený | Matching | Párování pojmů s definicemi nebo příklady. | Generátor + hodnotitel | Nízká |
| FMT-SA | Uzavřený | Short answer | Krátká otevřená odpověď; testuje porozumění vlastními slovy. | Hodnotitel odpovědi | Nízká |
| FMT-SOK | Dialogický | Sokratovský dialog s AI | AI vede uživatele otázkami k vlastnímu závěru; nevyřkne odpověď přímo. | Partner v dialogu | Střední |
| FMT-PRB | Dialogický | Tvorba otázek k tématu | Uživatel formuluje 3 otázky k tématu; AI posoudí přesnost a hloubku. | Posuzovatel formulace | Nízká |
| FMT-DVL | Dialogický | Protiargument (ďáblův advokát) | Uživatel vytvoří protiargument k tvrzení; AI reaguje a rozvíjí diskusi. | Diskutér | Střední |
| FMT-REF | Dialogický | Reflexe přinesené práce | Uživatel přinese vlastní výstup; AI klade reflektivní otázky. Pouze F2/F3 nebo průběžné — ne finální ověření. | Diskutér nad prací | Nízká |
| FMT-VLA | Dialogický | Vlastní formulace před AI verzí | Uživatel nejprve vytvoří vlastní verzi, pak vidí AI/vzor a porovná. | Konzultant, ne arbitr | Nízká |
| FMT-MIK | Komplexní | Mikroartefakt | Krátký tvůrčí výstup (věta, definice, mikroscénář). AI navrhne zlepšení, uživatel rozhodne. | Konzultant, ne arbitr | Střední |
| FMT-RUB | Komplexní (finální) | Rubrika | Vícekriteriální hodnocení; sebehodnocení / AI / lektor / garant / kombinace — volba autora kurzu. | Posuzovatel podle kritérií | Střední |
| FMT-ART | Komplexní (finální) | Artefakt | Komplexní produkt skládaný postupně přes F4 aplikace modulů; partner v tvorbě + hodnotitel finální podoby. | Partner + hodnotitel | Vyšší |
| FMT-JIN | Otevřený | Jiné | Volný formát mimo katalog. Popište přesně v poli 'Konkrétní znění / instrukce'. | Dle popisu | Dle popisu |

## KRAUU (Kompetenční rámec absolventa učitelství, MŠMT 2023)

Interní mapování, uživateli se nezobrazuje. Kurz mapuje 3–8 kompetencí.

| Kód | Oblast | Kompetence | Popis |
|---|---|---|---|
| 1.1 | 1 Obsah a didaktika | Rozumí vyučovaným oborům a dále se v nich rozvíjí | Učitel/ka rozumí oborům, které vyučuje, a systematicky se v nich rozvíjí. |
| 1.2 | 1 Obsah a didaktika | Didakticky zprostředkovává obsah žákům | Zprostředkovává obsah žákům v souladu s jejich vzdělávacími potřebami. |
| 2.1 | 2 Plánování, vedení a reflexe výuky | Nastavuje cíle výuky | Stanovuje srozumitelné cíle a vede k jejich nastavování i žáky a žákyně. |
| 2.2 | 2 Plánování, vedení a reflexe výuky | Poznává vzdělávací potřeby a plánuje výuku | Plánuje výuku tak, aby každý žák mohl aktivně dosahovat stanovených cílů. |
| 2.3 | 2 Plánování, vedení a reflexe výuky | Podporuje zvídavost a motivaci žáků | Podporuje u žáků zvídavost a motivaci k učení. |
| 2.4 | 2 Plánování, vedení a reflexe výuky | Efektivně vede výuku a zjišťuje porozumění | Vede výuku efektivně, zjišťuje porozumění a reaguje na potřeby žáků. |
| 2.5 | 2 Plánování, vedení a reflexe výuky | Reflektuje výuku | Reflektuje vlastní výuku a vyhodnocuje dosahování cílů. |
| 3.1 | 3 Prostředí pro učení | Vytváří bezpečné prostředí pro učení | Vytváří fyzicky i psychicky bezpečné prostředí pro učení. |
| 3.2 | 3 Prostředí pro učení | Vede žáky k chování podporujícímu učení | Vede žáky k chování podporujícímu vlastní učení i spolupráci. |
| 3.3 | 3 Prostředí pro učení | Uspořádání fyzického a digitálního prostředí | Zajišťuje vhodné uspořádání fyzického a digitálního prostředí učení. |
| 4.1 | 4 Zpětná vazba a hodnocení | Hodnotí na základě kritérií | Hodnotí žáky na základě jasných kritérií a vede k tomu i žáky. |
| 4.2 | 4 Zpětná vazba a hodnocení | Poskytuje a přijímá zpětnou vazbu | Poskytuje žákům konstruktivní zpětnou vazbu a sám přijímá ZV od žáků. |
| 4.3 | 4 Zpětná vazba a hodnocení | Vede žáky k reflexi jejich učení | Vede žáky k reflexi vlastního učení a samostatné metakognici. |
| 5.1 | 5 Profesní spolupráce | Spolupracuje s kolegy a kolegyněmi | Spolupracuje s kolegy ve prospěch žáků a společného profesního růstu. |
| 5.2 | 5 Profesní spolupráce | Spolupracuje s rodiči a širší komunitou školy | Spolupracuje s rodiči a širší komunitou v zájmu žáků. |
| 6.1 | 6 Profesní sebepojetí, rozvoj, etika a duševní zdraví | Utváření profesního sebepojetí a rozvoj | Systematicky pracuje na utváření profesního sebepojetí a vlastním rozvoji. |
| 6.2 | 6 Profesní sebepojetí, rozvoj, etika a duševní zdraví | Odpovědná práce s informacemi a demokratické hodnoty | Odpovědně pracuje s informacemi a digitálními nástroji, vede k etice. |
| 6.3 | 6 Profesní sebepojetí, rozvoj, etika a duševní zdraví | Duševní zdraví a psychohygiena | Systematicky pečuje o své duševní zdraví a psychohygienu. |

## Bloomova taxonomie (slovesa pro GOALS a OBJECTIVES, 3. os. sg.)

| Úroveň | Název | Slovesa |
|---|---|---|
| 1 | Zapamatovat | vyjmenuje, popíše, identifikuje, rozpozná, zopakuje |
| 2 | Porozumět | vysvětlí, shrne, klasifikuje, interpretuje, přeloží |
| 3 | Aplikovat | použije, provede, řeší, demonstruje, implementuje |
| 4 | Analyzovat | porovná, rozliší, zhodnotí strukturu, rozloží, prozkoumá |
| 5 | Hodnotit | posoudí, obhájí, kriticky zhodnotí, doporučí, zdůvodní |
| 6 | Tvořit | navrhne, sestaví, vytvoří, zkonstruuje, naplánuje |

## Typy OBJECTIVES

Šest typů podle číselníku platformy (`PRAKTIK-AI_ciselniky.xlsx`, list Objective New). Jeden OBJECTIVE smí mít víc typů. Matrice v7.2 uvádí tři typy (deklarativní / aplikační / hodnoticí); platí kódy platformy. Jen znalostní obsah (`obj.know`) smí do skip-testu.

| Kód | Typ | Co uživatel zvládne | Vhodné formáty | Role AI | Vyhodnocení |
|---|---|---|---|---|---|
| obj.know | znalostní | pochopí koncept, definici, princip nebo faktografii („vím, co to je a proč“) | FMT-MCQ, FMT-TF, FMT-MTC, FMT-SA | hlídač, posuzuje správnost | správně / špatně |
| obj.anal | analytický | porovná, rozliší, identifikuje vzorce, odhalí problém („vidím rozdíl a umím ho pojmenovat“) | FMT-SOK, FMT-PRB, FMT-DVL, FMT-MTC | partner nebo oponent, nekontroluje správnost | kvalitativní |
| obj.skill | dovednostní | zvládne postup krok za krokem („umím to provést“) | FMT-SA, FMT-MIK, FMT-VLA | průvodce, koriguje provedení, nedělá to za uživatele | posouzení provedení |
| obj.create | tvůrčí | vytvoří něco nového – artefakt, materiál, plán, aktivitu | FMT-MIK, FMT-ART, FMT-VLA, FMT-RUB (evaluace výstupu) | partner v tvorbě, rozhodnutí je na uživateli | bez průběžného hodnocení |
| obj.eval | hodnoticí | posoudí kvalitu výstupu, procesu, materiálu nebo AI odpovědi podle kritérií a zdůvodní | FMT-PRB, FMT-REF, FMT-RUB, FMT-DVL | facilitátor, ptá se na zdůvodnění, nekoriguje úsudek | kvalitativní |
| obj.refl | reflexivní | reflektuje vlastní praxi, postoj, rozhodnutí nebo proces | FMT-REF, FMT-SOK, FMT-SA | partner, navazuje a ptá se, nehodnotí | bez průběžného hodnocení |

## Úrovně pokročilosti a délka F1 (CIS_Urovne)

Úroveň = zkušenost účastníka s AI, ne odbornost v oboru. F1 = výklad ke čtení, 130 slov/min.

| Úroveň | Náročnost tématu | F1 (min) | F1 (slov) | Profil generátoru | Úrovně platformy |
|---|---|---|---|---|---|
| Začátečník | nízká / střední | 5 | 600–700 | beginner | complete_beginner, beginner |
| Začátečník | vysoká | 6 | 700–850 | beginner | complete_beginner, beginner |
| Středně pokročilý | nízká / střední | 7 | 850–1 000 | intermediate | slightly_advanced, intermediate |
| Středně pokročilý | vysoká | 8 | 950–1 100 | intermediate | slightly_advanced, intermediate |
| Pokročilý | nízká / střední | 9 | 1 100–1 250 | advanced | advanced, expert |
| Pokročilý | vysoká | 10 | 1 250–1 400 | advanced | advanced, expert |

**Náročnost tématu** (pole v každém modulu): nízká = nejvýše 2 nové pojmy, známá situace · střední = 3–4 pojmy nebo 1 abstraktní princip · vysoká = 5+ pojmů, abstraktní model, právní či výzkumný rámec.

**Doporučená obtížnost na platformě:** platforma má 6 úrovní, matrice 3; uveď obě úrovně platformy z tabulky, vybere metodik.

**Profily úrovní:**
- **Začátečník:** Kratší věty, každý pojem týkající se AI vysvětlen při prvním výskytu, nejvýše 3 nové pojmy na modul, nejdřív analogie, postupy v číslovaných krocích. Otázky: porozumění pojmu nebo principu; otevřená otázka = popis situace z vlastní práce.
- **Středně pokročilý:** Základní pojmy jen připomenuty; těžiště v principech, důvodech a typických chybách; srovnání postupů. Otázky: aplikace na situaci; otevřená otázka = zdůvodněné rozhodnutí.
- **Pokročilý:** Bez elementárního výkladu a analogií; hraniční případy, limity, síla důkazu, institucionální důsledky, protiargumenty, víc detailů. Otázky: distraktory na úrovni nuancí; otevřená otázka = argumentace s protiargumentem.

## Cílové skupiny (CIS_Skupiny)

Platforma rozlišuje tři skupiny (kódy a, s, m); THP a Host zatím mimo číselník.

| Kód | Skupina | Kdo to je | Oslovení a označení |
|---|---|---|---|
| a | Akademik | akademický pracovník VŠ – vyučující, výzkumník, doktorand | vykání; osobu neoznačuj rodově – „vyučující“, případně popisem činnosti („ve výzkumu“, „při vedení práce“, „v disertaci“) |
| s | Student | student bakalářského nebo navazujícího magisterského studia, zejména učitelství | vykání; v textu „studující“; nikdy „studente“ |
| m | Mentor | provázející učitel na ZŠ nebo SŠ (mentor pedagogické praxe), který zároveň sám učí | vykání; „mentor“ nebo „provázející učitel“; svěřence „student na praxi“, žáky „žáci“ – nezaměňovat |

Plné definice pro generátor (typické situace, platná pravidla) jsou v Matrici v7.2, list CIS_Skupiny, sloupec E. Pravidla pro studentské práce se na akademiky nepřenášejí (výjimka: disertace doktoranda); vnitřní předpisy univerzity se na mentora zpravidla přímo nevztahují, platí ale pro výstupy studenta z praxe; do AI nevkládat osobní údaje žáků.

## Typy artefaktů

| Kód | Typ | Příklady |
|---|---|---|
| ART-PLAN | Plánování výuky | scénáře, plány hodin, diferencované plány |
| ART-TASK | Zadání a úkoly | přepracovaná zadání, odstupňovaná dle AI-rezistence |
| ART-EVAL | Hodnocení a zpětná vazba | rubriky, checklisty, formativní otázky |
| ART-REFL | Analýza a reflexe | srovnání nástrojů, anotované halucinace, reflexivní deník |
| ART-PRMT | Prompty a šablony | sady promptů s iteracemi, prompt library předmětu |
| ART-PROF | Profesní rozvoj a spolupráce | etické kodexy, plány změny, komunikace s rodiči |
| ART-STUD | Materiály pro studenty | metakognitivní aktivity, návody, sebehodnoticí listy |

## Další číselníky

- **Blok:** A Kontext a principy · B Transformace (pedagogická aplikace) · C Oborová aplikace · D Škola a systém · Z Pilot ZŠ.
- **Specifikum AI:** N nástroj · P předmět · D dialog · R riziko · T tvůrčí (každý kurz má jedno dominantní).
- **Cílové skupiny (katalog):** AK akademik · ST student učitelství · ME mentor / provázející učitel · UČ učitel ZŠ/SŠ · VŠ vedení školy · AB absolvent. Převod na skupiny platformy (CIS_Skupiny): AK → Akademik, ST → Student, ME a UČ → Mentor. VŠ a AB číselník nemá: u kurzů bloku D pracuj se skupinou Mentor a vedení školy uváděj jen v příkladech, dokud číselník skupinu nedoplní.
- **Povinnost:** Povinný · Doporučený · Volitelný. **Typ kurzu:** Obecný · Oborový · Průřezový · Vstupní kurz skupiny · Specializovaný.
- **EQF:** 6–8 (vydavatel UJEP). **ECTS:** orientačně 0,1 na 60–90 min kurz.
- **Capstone:** varianta A = zjednodušený blok F1–F4 (zadání, tvorba, ověření artefaktu), varianta B = pouze finální ověření přes rubriku.
- **Hodnotitel rubriky:** User (sebehodnocení) · Lektor · Garant · AI · Kombinace. **Práh badge:** 75 %. **Skip-test:** 80 %, jen znalostní obsah (`obj.know`).
- **Úrovně rubriky (závazné názvy):** Mistrovství 81–100 % · Zdatnost 61–80 % · Způsobilost 41–60 % · Rozvoj 21–40 % · Začátek 0–20 %. Max. 5 kritérií, váhy v %.
- **Role na platformě:** ROLE-01 User · ROLE-02 Lektor · ROLE-03 Garant · ROLE-04 Super admin.
- **Mediální přílohy:** názvy `[KOD]-[Mx]-[NN]-[typ]-[popis].[ext]` (NN = pořadí přílohy v modulu, 01, 02 …; pořadí upřesňuje Matrici v7.2, list 10, která ho zatím neuvádí; obrázky se vkládají ručně, v sekci 10 vždy uvést modul, fázi a nadpis oddílu, za který patří), formáty PNG, SVG, MP3 (video platforma zatím nepodporuje, shrnutí se dodává jako MP4 mimo platformu).
