# PRAKTIK-AI — Systémová pravidla projektu
## Platná pro všechny kurzy a metodiky | Matrice v6.0

---

## 1. IDENTIFIKÁTORY A ČÍSLOVÁNÍ

- **ID OBJECTIVES** = `[kód kurzu]-O[pořadí]` — např. `B0201-O1`, `A0101-O3`, `C0601-O7`
  - Prefix = kód kurzu (DB); unikátnost napříč celým kurikulem je zaručena automaticky, bez centrální evidence
  - Číslování začíná od 1 v každém kurzu nezávisle, průběžně přes všechny moduly
  - Tvar `A0101_03` pochází z Matrice v4.0 a už se nepoužívá; kánon i kontrola `praktik-qa` očekávají `A0101-O3`
- **Interní kód (DB)** a **zobrazovací kód (UI)** ověřovat s IT před finalizací
- **Navazující kurzy (kódy)** doplňovat po konzultaci s vedoucím metodického týmu

---

## 2. STRUKTURA KURZU

- **Maximální délka modulu** = 30 min (závazně pro nové kurzy)
- **Capstone** není modul — pravidlo 30 min se na něj nevztahuje
- **Maximální počet obsahových modulů** = 5 (bez M0 a Capstone)
- **Parametr „Délka celkem"** musí vždy odpovídat součtu délek všech modulů + Capstone

---

## 3. JAZYK A OSLOVOVÁNÍ

- **Výhradně vykání** napříč celým projektem — nikdy tykání (ani v anchor textu, ani v impulsech, ani v instrukcích pro agenta)
- **Jména postav v příkladech**: česká jména, v rámci jednoho kurzu střídat
  - Zakázány rusismy a jména cizího původu — zejména: Natalia
- **Obory v příkladech**: humanitní obory, střídat (dějepis, psychologie, pedagogika, filozofie, sociologie, čeština, dějiny umění, etika…)
  - Zakázány: právo, biologie, ekonomie, medicína, informatika, obchodní komunikace

---

## 4. ZÁVAZNÁ TERMINOLOGIE

| Správně | Zakázáno |
|---|---|
| OBJECTIVES | výsledky učení, VL |
| GOALS | cíle kurzu |
| IMPULS | vstupní hák, VSTUP |
| F1 PREZENTACE | expozice, výklad |
| F2 PROCVIČENÍ | aktivita, cvičení |
| F3 OVĚŘENÍ | test, kvíz |
| F4 APLIKACE | tvorba, projekt |
| Modul X (celým slovem) | M1, M2… (v textech pro uživatele a cross-referencích) |

---

## 5. ŠABLONA A FORMÁT

- **Platná šablona** = Matrice kurzu v6.0
- **Pojmy a zkratky** jsou v číselníku `CIS_Pojmy` (referenční přehled systémových termínů) — jen se z něj čte, needituje se. Samostatná sekce „✦ Slovník pojmů“ z v4.0 v matrici v6.0 není
- **Sloupec „Schválil"** v sekci 10 (Mediální přílohy) — ponechává se prázdný, doplňuje vedoucí metodického týmu před publikací. Pozor: v v6.0 je sekce 9 ARTEFAKT, mediální přílohy se přesunuly do sekce 10
- **Databáze scénářů** — pokud ☑ ano, vždy doplnit: „anonymizovaně, pouze po souhlasu autora"

---

## 6. VĚTY, KTERÉ NIKDY NEZAZNÍ

Platí pro **všechny kurzy**, všechny fáze, anchor texty, impulsy, mediální přílohy i texty pro uživatele. Seznam je zakazovací: uvedená znění ani jejich varianty se nepoužívají. Skupiny 1–8 jsou důvody, proč věta škodí; agent podle nich zobecňuje i na věty zde neuvedené.

### 6.1 Prázdné smíření

| Nikdy | Proč |
|---|---|
| „AI je tu a nikam nezmizí." | Není to tvrzení, je to povzdech. Neříká nic o tom, co má účastník dělat. |
| „AI je jen nástroj, záleží na tom, jak ho použijete." | Tautologie, která vypadá jako teze. Kurzy existují právě proto, že „jak" je celá ta těžká část. |
| „Není otázka zda, ale jak." | Tutéž myšlenku nese struktura kurzu. Vyslovená nahlas zní jako konferenční slogan. |

### 6.2 Strašení

| Nikdy | Proč |
|---|---|
| „AI vám vezme práci." | Kurzy nejsou o zaměstnanosti a nemají k tomu doklady. |
| „Studenti podvádějí ve velkém." | Data ukazují rozšířené používání, ne rozšířené podvádění. Záměna obojího je věcná chyba. |
| „Musíte být o krok napřed před studenty." | Staví vztah jako závod. Metodika platformy stojí na opaku: studenti mapují hranici spolu s vyučujícím. |

### 6.3 Nadšení a marketing

| Nikdy | Proč |
|---|---|
| „AI přináší revoluci ve vzdělávání." | Tvrzení bez důkazu v kurzu, který učí vyžadovat důkazy. |
| „Ušetří vám čas na to podstatné." | Úspora času je někdy ztráta porozumění; věta popírá obsah kurzů o kognitivním offloadingu. |
| „Stačí se správně zeptat." | Spolupráce člověka s AI není automaticky přínosná. „Stačí" je nepravda. |

### 6.4 Věty, které kurz sám odnaučuje

Nejdůležitější skupina. Kurz, který ve F1 PREZENTACE učí oponentní formulaci a ve F2 PROCVIČENÍ použije zrcadlovou, ztrácí důvěryhodnost okamžitě.

| Nikdy | Místo toho |
|---|---|
| „Zeptejte se AI, jestli je to správně." | „Požádejte AI, ať ukáže, jak se můžete mýlit." |
| „Nechte si od AI shrnout, co jste přečetli." | „Napište si vlastní shrnutí a nechte AI najít, kde se rozchází s textem." |
| „AI vám to vysvětlí lépe." | „Zkuste to vysvětlit sami a nechte se vyzkoušet." |

### 6.5 Věty v rozporu se směrnicí nebo s doklady

| Nikdy | Proč |
|---|---|
| „Detektor AI vám pomůže odhalit…" | Detektory nejsou spolehlivé (Směrnice rektora UJEP č. 7/2026, odst. 6.2) a znevýhodňují nerodilé mluvčí. Kritérium 7 oponentního formuláře to kontroluje výslovně. |
| „AI poškozuje mozek." / „Výzkum MIT prokázal…" | Preprint, ~54 účastníků, doložená metodologická kritika. Citovat bez těchto údajů znamená porušit pravidlo kalibrace jistoty. |
| „Vygenerujte si seznam literatury." | Generování citací je nepřípustné (odst. 5.2); model uvádí neexistující zdroje. |
| „Deklarujte to a je to v pořádku." | Deklarace nemění nepřípustné použití na přípustné. Nejčastější nedorozumění, jaké směrnice vyvolává. |

### 6.6 Didaktické prázdno

| Nikdy | Proč |
|---|---|
| „Seznámíte se s možnostmi AI." | Cíl formulovaný slovesem, které nelze ověřit. Matrice takové cíle nepřipouští. |
| „V tomto modulu si povíme o…" | Ohlašuje výklad místo toho, aby začal. F1 PREZENTACE začíná IMPULSEM, ne anotací. |
| „Nyní si ukážeme praktický příklad." | Věta, která pouze zabírá čas mezi dvěma obsahy. |

### 6.7 AI balast

Zakázáno jako třída, nejen v uvedeném znění:

- „V dnešní rychle se měnící době…"
- „Je důležité si uvědomit, že…"
- „Pojďme se společně podívat na…"
- „Nezapomeňte, že klíčem k úspěchu je…"
- „Skvělá otázka." a jakákoli pochvala zadání
- Jakýkoli odstavec, který shrnuje, co bude následovat, aniž by to zároveň říkal.

### 6.8 Falešná blízkost

| Nikdy | Proč |
|---|---|
| „Nebojte se!" | Kurzy nepracují se strachem, ale s úsudkem. Konejšení podsouvá, že důvod k obavám existuje. |
| „Je to jednodušší, než si myslíte." | Popírá princip žádoucích obtíží: náročnost je někdy součástí učení. |
| „Zvládne to každý." | Snižuje hodnotu toho, co se účastník právě naučil. |

### 6.9 Tři testy pro zobecnění

Agent je použije na každou větu, kterou napíše:

1. **Test zaměnitelnosti.** Mohla by ta věta stát v kurzu o libovolném jiném nástroji a o libovolném jiném tématu? Pak do tohoto kurzu nepatří.
2. **Test vlastního pravidla.** Kdyby účastník tuto větu použil jako zadání pro AI, porušil by tím něco, co ho kurz právě naučil?
3. **Test doložitelnosti.** Tvrdí ta věta něco o světě? Pak musí jít dohledat, jak silný důkaz za ní stojí — a ten údaj musí být v kurzu uveden.

---

*Pravidla odvozena z práce na kurzu B0201 (Zušťáková). Platí pro všechny nové kurzy.*
*Oddíl 6 doplněn 20. 9. 2026 při přípravě kurzu A0101 (Liegertová, Pavlíková). Platí zpětně pro všechny kurzy.*
*Srovnáno s Matricí v6.0 dne 20. 9. 2026: záhlaví, tvar ID OBJECTIVES a oddíl 5 (číselník CIS_Pojmy, mediální přílohy jako sekce 10).*
