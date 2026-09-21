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
- **Navazování kurzů se v první desítce kurzů nepoužívá.** V textu pro uživatele se neodkazuje na jiné kurzy — ani jako na prerekvizitu, ani jako na pokračování. Pole „Navazující kurzy (kódy)" zůstává prázdné a routing v rubrice (11.3) míří na konkrétní modul, fázi nebo sekci artefaktu **téhož kurzu**, nikoli na jiný kurz. Důvod: prvních deset kurzů se nasazuje souběžně, jejich číslování není finální a odkaz na kurz, který účastník nemá k dispozici, je slib bez krytí. Odkazy mezi kurzy se doplní, až bude katalog uzavřen.

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
| „Tento kurz je první, který otevřete." / „Tímto kurzem začíná vaše cesta platformou." | Věta o kurzu místo o obsahu. Popisuje zařazení v platformě, které účastník vidí sám, a v textu nenese žádnou informaci. Platí pro celou třídu meta-vět o pořadí, cestě, modulech, které přijdou, a o tom, co kurz „nabízí". |
| „Na tento kurz navazuje kurz X." | V první desítce kurzů se navazování nepoužívá (oddíl 2). Odkaz na kurz, který účastník nemá k dispozici, je slib bez krytí. |

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

## 7. ANOTACE KURZU

**Anotace je objektivní profesionální stručný popis kurzu.** Slouží k založení kurzu na platformě a do katalogu — potřebuje ji člověk, který kurz zakládá, ne účastník, který ho studuje. Je povinnou součástí souboru `<KOD>_<Nazev>_KURZ.md` a agent ji po dokončení podkladu **vypíše i do chatu**, aby byla hned po ruce.

### 7.1 Formát

- **Nejvýše 500 znaků** včetně mezer.
- **Tři části v tomto pořadí:**
  1. **Jedna věta** — pro koho kurz je a co ten člověk chce zvládnout.
  2. **`Témata:`** — 4–6 témat oddělených čárkami, formulovaných jako obsah, ne jako sliby.
  3. **`Výstupy:`** — artefakt a výčet toho, co obsahuje.
- Bez nadpisu, bez odrážek, bez zvýraznění. Dva odstavce, čistý text ke zkopírování do formuláře.

### 7.2 Co v anotaci nikdy není

| Nepatří tam | Proč |
|---|---|
| Kód a název kurzu | Jsou to samostatná pole formuláře; v anotaci by se zdvojily. |
| **Délka, počet modulů, počet fází** | Samostatná pole. Anotace neslibuje čas — slíbený a skutečný čas se rozcházejí a je to nejčastější důvod nedokončení. |
| Druhá osoba a oslovení („projdete", „odnesete si", „abyste") | Anotace je neosobní popis. Vykání patří do kurzu, ne do katalogu. |
| Popis deficitu účastníka („nemají jak poznat", „neumějí") | Popisujte **záměr** čtenáře, ne jeho nedostatek: „chtějí poznat", „potřebují rozhodnout". |
| Slogan, pointa, závěrečná teze | To je anchor text, ne anotace. Anotace nekončí efektem. |
| Rozsah artefaktu ve stranách nebo slovech | „dokument", nikoli „dvoustránkový dokument" — rozsah se mění a v katalogu zastarává. |
| Superlativy a přísliby („naučíte se", „získáte jistotu", „jedinečný") | Anotace popisuje, co kurz obsahuje, nikoli co způsobí. |
| Vyprávění a narativní přechody | Návěští `Témata:` a `Výstupy:` nesou strukturu; vyprávění ji rozmělňuje. |

**Oddíl 6 (Věty, které nikdy nezazní) platí i pro anotaci**, včetně tří testů v 6.9.

### 7.3 Anotace, anchor text a informační nota — tři různé texty

| Text | Pro koho | Podoba | Kde |
|---|---|---|---|
| **Anotace** | člověk zakládající kurz, katalog | neosobní, ≤ 500 znaků, `Témata:` / `Výstupy:` | vlastní blok v `<KOD>_KURZ.md` + do chatu |
| **Anchor text** | účastník v rozhraní | vykání, 2–3 věty, pojmenuje problém, smí provokovat | list 1.4 matrice |
| **Informační nota** | účastník před spuštěním | vykání, prerekvizity, cílová skupina, co si připravit | list 1.4 matrice |

Nezaměňovat a needitovat jeden podle druhého.

### 7.4 Vzor (kurz A0101, 464 znaků)

```
Vstupní kurz pro všechny, kdo AI běžně používají a chtějí poznat, kdy jejímu výstupu věřit. Témata: jak model vytváří odpověď, proč plynulost není přesnost, jak zadání přeformulovat ze zrcadla na oponenta, co si nechat pro sebe a co dovoluje Směrnice rektora č. 7/2026.
Výstupy: osobní protokol práce s AI — dokument s vlastním ověřeným tvrzením, třemi přepsanými zadáními, mapou úloh (které delegovat a které ne), a hotovou deklarací využití AI pro vlastní práci.
```

---

*Pravidla odvozena z práce na kurzu B0201 (Zušťáková). Platí pro všechny nové kurzy.*
*Oddíl 6 doplněn 20. 9. 2026 při přípravě kurzu A0101 (Liegertová, Pavlíková). Platí zpětně pro všechny kurzy.*
*Oddíl 7 doplněn 20. 9. 2026 na základě autorského přepracování anotace kurzu A0101. Platí zpětně pro všechny kurzy.*
*Srovnáno s Matricí v6.0 dne 20. 9. 2026: záhlaví, tvar ID OBJECTIVES a oddíl 5 (číselník CIS_Pojmy, mediální přílohy jako sekce 10).*
