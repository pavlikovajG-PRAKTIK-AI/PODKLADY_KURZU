---
name: praktik-kurz
description: Vygeneruje kompletní kurz pro platformu PRAKTIK-AI (TQ23000092) ze zdrojového textu a zadání autora – ve struktuře Matrice v6 (IDENTIFIKACE, GOALS, OBJECTIVES, moduly IMPULS + F1–F4, capstone, artefakt, rubrika, zdroje), nejdřív kostru ke schválení, pak moduly po jednom. Použij, když metodik/metodička chce „vytvořit kurz“, „zpracovat článek/PDF jako kurz“, „napsat moduly“, „přidat modul“, „přepsat kurz do matrice“, mluví o kódu kurzu z katalogu (A6, B2, C1.5, Z2…) nebo o kurzu PRAKTIK-AI. Pro rozhovor s autorem před tvorbou použij praktik-rozhovor, pro kontrolu praktik-qa, pro export praktik-export.
---

# praktik-kurz: tvorba kurzu PRAKTIK-AI

Cíl: z podkladů autora vznikne kurz, který projde kontrolou `praktik-qa` bez zásadních oprav a odpovídá vzoru A0601. Pracuješ jako metodický architekt: hlídáš Bloomovy cíle, artefakt skládaný po modulech a politiku „AI jako partner, ne hlídač“.

## Reference (čti cíleně, ne všechno)

| Soubor | Kdy ho otevřít |
|---|---|
| `references/kanon.md` | vždy na začátku (terminologie, struktura, časy, styl, zdroje, pojmenování) |
| `references/systemova_pravidla.md` | vždy před psaním textu pro uživatele — oddíl 6 „Věty, které nikdy nezazní“ je zakazovací a platí pro všechny kurzy |
| `references/katalog_kurzu.md` | jen řádek zadaného kurzu a jeho prerekvizit (hledej podle kódu), plus vlnu |
| `references/ciselniky.md` | při výběru NP, FMT, KRAUU, typu artefaktu; tabulku otevři, kód opiš |
| `references/sablona_kurzu.md` | před psaním kostry |
| `references/vzor_A0601_modul1.md` | před prvním modulem (jen část „MODUL 1“), před rubrikou (jen část „RUBRIKA“) |

Nečti celý vzor ani celý katalog do kontextu. Zdrojový text autora čti celý, ale nevracej ho do chatu; pracuj s výpisky.

## Krok 0: vstupní kontrakt

Ověř, že máš pět vstupů z kánonu (kód kurzu a cílová skupina, řešený problém, artefakt, tři autentické situace, zdrojový text). Chybí-li víc než jeden, nabídni `praktik-rozhovor`. Chybí-li jeden, zeptej se jen na něj a vysvětli jednou větou, proč ho potřebuješ. Tři autentické situace si nikdy nevymýšlej; bez nich označ moduly jako „čeká na příklady autora“.

Když kód v katalogu neexistuje, napiš to a navrhni nejbližší kód nebo pracovní kód s poznámkou pro garanta. Pro mikrokurz (30–45 min) použij 2–3 moduly, pro pilotní kurz ZŠ (120 min) 5 modulů po 20 min + capstone.

## Krok 1: kostra (vždy nejdřív, vždy ke schválení)

Napiš do chatu a ulož jako `<KOD>_<Nazev>_KURZ.md` pouze:

1. Hlavičku a sekci 1 IDENTIFIKACE včetně anchor textu, informační noty a textu certifikátu.
2. GOALS (3–4, Bloom 2 až 6, poslední vždy „Tvořit“ a míří na artefakt).
3. OBJECTIVES (1–3 na modul, ID `<KOD>-Onn`, typ, testovatelnost, vazba).
4. Blueprint artefaktu: tabulka povinných sekcí a v kterém F4 vznikají. Součet sekcí = počet modulů + úvod v capstone; každá sekce vzniká v právě jednom F4. Když zadání z rozhovoru obsahuje víc položek, neslučuj je sám: napiš návrh sloučení do kostry a nech autora rozhodnout.
5. Názvy modulů, IMPULSY a plán formátů (F2 dialogický formát, F3 formáty, F4 sekce) v jedné tabulce.
6. Globální výběr NP, AI principů a KRAUU; návrh 4–8 vzorů a antipatternů pro agenta.
7. Seznam zdrojů, které ze zdrojového textu použiješ, a co v něm chybí (nutno dohledat).

Ukonči otázkou, co autor mění. Nepokračuj bez souhlasu. Přepracování kostry je levné, přepracování modulů drahé.

## Krok 2: moduly po jednom

Po schválení generuj modul 1, čekej na zpětnou vazbu, pak další (autor může říct „další dva“). Každý modul podle šablony:

- **Hlavička:** délka, OBJECTIVES, skip, vazba na GOALS, NP kódy s fázemi.
- **IMPULS:** jedna věta nebo otázka, překvapení nebo situace z praxe autora, kurzívou. Nikdy definice ani „V tomto modulu…“.
- **F1 PREZENTACE (max. 5 min, 250–400 slov):** kontext → mechanismus se zdroji (autor, rok, časopis, kalibrovaná jistota) → kurzívní „Zapamatujte si“. Tučně 2–4 klíčové body. Jedna metafora na koncept, návratové schéma kurzu. Zakonči řádkem **Větvení:** akademik / mentor / student.
- **F2 PROCVIČENÍ (3–5 min):** jeden dialogický nebo aplikační formát (FMT-SOK, FMT-VLA, FMT-PRO, FMT-OTA, FMT-MIK; FMT-MTC jen u znalostních cílů). Kurzívou instrukce pro agenta: co nevyzradit, jak vyhodnotit, max. výměn. Alespoň jeden modul kurzu použije autentickou situaci autora jako startovní scénář.
- **F3 OVĚŘENÍ (3 min):** 2–3 položky, jen tolik uzavřených, kolik ověřuje faktografii, vždy se správnou odpovědí a zdůvodněním; poslední položka metakognitivní. Distraktory smysluplné, žádné „všechny odpovědi jsou správné“.
- **F4 APLIKACE (3 min):** konkrétní sekce artefaktu podle blueprintu, formulovaná jako instrukce („Doplňte do svého dokumentu sekci X, která obsahuje Y“), s rolí AI a s tím, co AI nesmí.
- Zkontroluj součet minut fází = délka modulu.

Každý modul má alespoň jednu otevřenou nebo reflexivní položku. Klíčový pojem z modulu n se vrátí v modulu n+2 jinou formou (NP-02).

## Krok 3: závěr kurzu

Po posledním modulu vygeneruj capstone (varianta A nebo B podle rozhodnutí autora), sekci 9 ARTEFAKT s šablonou sekcí, 11 RUBRIKU 5 × 5 se závaznými názvy úrovní, váhami a routingem, 12 výzkumnou poznámku, závěrečný test (8–12 položek, práh 75 %), pravidla používání AI pro účastníky a ZDROJE s datem ověření. Preprinty označ. U tvrzení oslabených replikacemi přidej poznámku.

## Krok 4: předání

Ulož celý kurz jako `<KOD>_<Nazev>_KURZ.md` do složky kurzu (konvence v kánonu, sekce 9). Když je jako Project folder otevřená přímo složka kurzu, ukládej do ní; když je otevřená `09_Kurzy`, použij nebo založ podsložku `<Kód><NázevBezMezer>`. Uvnitř už otevřené složky kurzu nikdy nezakládej další `09_Kurzy/`. Pak nabídni:
- `praktik-qa` (kontrola vůči Definition of Done a formuláři oponenta),
- `praktik-export` (docx pro autora, garanta a oponenta),
- `av-materialy` (video, audio, grafiky).

## Pravidla psaní (zkratka kánonu)

Vykání. Česká jména, humanitní obory v příkladech, střídat. Žádný AI balast, žádné katastrofické ani bagatelizující věty o AI. KRAUU jen v sekci 7. Terminologie jen z kánonu (GOALS, OBJECTIVES, IMPULS, F1–F4, ARTEFAKT). Zdroje jen ověřitelné; když nelze ověřit, řekni to. Kurz mluví o kategoriích nástrojů, ne o produktech.

## Šetření tokenů

- Kostra před moduly. Moduly po jednom. Změny dělej jako úpravy souboru, ne přegenerováním celku.
- Z referencí otvírej jen potřebnou část. Katalog grepuj podle kódu.
- Zdrojový text necituj do chatu, jen odkaz „(zdroj, s. 12)“.
- Když autor chce více variant (profil, délka, tón), generuj varianty jen pro kostru a pro jeden modul, ne pro celý kurz.
