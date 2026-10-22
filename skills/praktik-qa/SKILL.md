---
name: praktik-qa
description: Zkontroluje hotový nebo rozpracovaný kurz PRAKTIK-AI (soubor KOD_Nazev_KURZ.md) proti Definition of Done, deseti kritériím oponentního posudku, systémovým pravidlům, kánonu a Matrici kurzu v7.2 (terminologie, hlavička a údaje pro platformu, úroveň a délka F1, cílové skupiny, časy, F4 v každém modulu, dialogické formáty, vykání, jména a obory v příkladech, zdroje, KRAUU mimo texty pro uživatele) a vydá QA report s označenými místy k opravě. Použij, když autor chce „zkontrolovat kurz“, „projít Definition of Done“, „oponenturu nanečisto“, „co je špatně“, „připravit kurz na oponenta“, nebo před exportem.
---

# praktik-qa: kontrola kvality kurzu

Výstup je `<KOD>_QA_report.md` ve složce kurzu a stručné shrnutí v chatu. Kontroluješ, neopravuješ; opravy děláš jen když autor řekne „oprav“, a pak jako úpravy souboru, ne přegenerování.

## Reference

- `references/definition_of_done.md`: 9 podmínek DoD.
- `references/formular_oponenta.md`: 10 kritérií s tím, „na co se dívat“, škála 1–4.
- `references/systemova_pravidla.md`: identifikátory, časy, jazyk, terminologie (kopie z praktik-kurz).
- `references/kanon.md`: struktura, politika hodnocení, styl, zdroje (kopie z praktik-kurz).
- `references/ciselniky.md`: výpis číselníků – kódy formátů FMT a typy OBJECTIVES (`obj.*`) podle číselníku platformy, úrovně a délka F1, cílové skupiny a jejich oslovení podle Matrice v7.2 (kopie z praktik-kurz).

Tři kopie z praktik-kurz se mění jen společně s originálem v praktik-kurz.

**Číselník platformy.** Soubor `09_Kurzy/TEST1_PodkladyKurzu/PRAKTIK-AI_ciselniky.xlsx` (15. 10. 2026) používají programátoři platformy. Je závazný pro kódy a výčty, které čte platforma (např. `target.a`, `target.s`, `target.m`, `level.1`–`level.3`). Obsah, který xlsx nemá nebo má ve stavu Matrice v6 (F1 max. 5 min, staré popisy NP, nevyplněný typ OBJECTIVE), se řídí Maticí v7.2. Metodici xlsx nemění.

## Postup

1. Načti soubor kurzu. Zjisti kód, počet modulů, deklarovanou délku, úroveň (1.2) a cílové skupiny (1.8).
2. Projdi kontroly A až D a P níže. Ke každé napiš PASS, FAIL nebo WARN, u FAIL a WARN přesné místo (sekce, modul, fáze) a jednu větu, co změnit.
3. Vyplň sebehodnocení podle formuláře oponenta (10 oblastí, škála 1–4) s jednou konkrétní připomínkou na oblast. U oblastí 3 a 5 posuď i soulad s úrovní kurzu (profily úrovní v `ciselniky.md`), cílové skupiny posuzuj podle 1.8.
4. Simulovaný průchod: projdi kurz očima účastníka každé cílové skupiny zvolené v 1.8, na deklarované úrovni, po pracovní době. Zapiš, kde by odešel a proč, a odhad reálné délky (F1 čtení 130 slov/min).
5. Sepiš „Tři nejdůležitější změny“ v pořadí priority a „Co funguje, zachovat“.
6. Ulož report, v chatu shrň verdikt: připraven k oponentuře / vyžaduje úpravy (kolik FAIL) / nutné přepracování.

## A Formální kontroly (deterministické)

- Kód DB má formát písmeno + 4 číslice; kód UI odpovídá katalogu; slug bez diakritiky a mezer.
- **Hlavička 0.1** (Matrice v7.2, 00_Zalozeni): název, podtitul, verze, datum, autoři podkladu příjmením (hlavní autor první), zdrojový podklad, poznámka „K potvrzení garantem“.
- **Blok 0.2 Údaje pro založení kurzu na platformě** existuje a má všechna pole formuláře; název nejvýše 120 znaků; počet modulů = skutečný počet obsahových modulů; délka = 1.2 Délka celkem; popis = ANOTACE; doporučená obtížnost = úrovně platformy podle úrovně kurzu (`ciselniky.md`).
- Vyplněno: řešený problém, artefakt, anchor text, informační nota, text certifikátu, EQF, délka. **Úroveň** jen Začátečník / Středně pokročilý / Pokročilý (jiná hodnota, např. „Základní“ = FAIL). **Oddíl 1.8:** cílové skupiny jen Akademik / Student / Mentor, alespoň jedna (jiné skupiny, např. vedení školy, = FAIL); počet modulů nejvýše 12; minut na modul; úroveň pro generátor odpovídá úrovni (beginner / intermediate / advanced).
- **ANOTACE (oddíl 7 `systemova_pravidla.md`)**: existuje jako samostatný blok, **nejvýše 500 znaků** (spočítej je a uveď v reportu), struktura: věta, pro koho kurz je, jedna až dvě věty o obsahu v širších celcích (návěští `Témata:` nepovinné) a `Výstupy:`. FAIL, pokud chybí, přesahuje limit, nebo obsahuje délku kurzu, počet modulů, kód či název kurzu, názvy modulů nebo výčet témat, druhou osobu (`projdete`, `odnesete si`, `abyste`, `naučíte se`), slogan, příslib, superlativ, rozsah artefaktu ve stranách nebo popis deficitu účastníka. Zkontroluj též, že anotace není totožná s anchor textem ani s informační notou — jsou to tři různé texty pro tři různé čtenáře (oddíl 7.3).
- GOALS: slovesa 3. os. sg. podle Blooma, poslední GOAL míří na artefakt; každý GOAL pokryt alespoň jedním modulem.
- OBJECTIVES: ID `<KOD>-Onn` unikátní, každý modul má 1–3, každá vazba na existující GOAL. Každý OBJECTIVE má alespoň jeden typ s kódem z číselníku platformy: `obj.know`, `obj.anal`, `obj.skill`, `obj.create`, `obj.eval`, `obj.refl` (víc typů u jednoho OBJECTIVE je v pořádku). Chybějící typ nebo typ mimo tento výčet (např. deklarativní, aplikační, hodnoticí z Matrice v7.2) = FAIL s návrhem kódu podle `ciselniky.md`. Skip-test smí ověřovat jen OBJECTIVES typu `obj.know`; skip u modulu, jehož skip-test ověřuje jiný typ, = FAIL.
- Sekce 4 Větvení má sloupce Akademik (vč. doktorandů) / Mentor (provázející učitel ZŠ/SŠ) / Student (Bc., Mgr.); staré názvy větví = WARN.
- Každý modul má: název, IMPULS, F1, F2 s kódem FMT, F3 s kódem FMT (kódy jen z `ciselniky.md`; staré FMT-OTA a FMT-PRO = FAIL, náhrada FMT-PRB a FMT-DVL), F4 se sekcí artefaktu, NP kódy s fází a v hlavičce náročnost tématu (nízká / střední / vysoká), orientační rozsah F1, průběžné hodnocení (formát, hodnotitel) a pole „Otevřené problémy pro metodika“. Součet minut fází = délka modulu.
- **Délka modulu:** obvykle 15–25 min, nad 30 min = FAIL. Odchylka délky modulu od plánu do ±5 min je v pořádku, větší odchylka = WARN; délka není primární kritérium, rozhoduje kvalita obsahu a metodika (pokyn J. Pavlíkové, 18. 10. 2026).
- **F1:** 5–10 min, mimo tento rozsah = FAIL. Spočítej slova F1 a porovnej je s řádkem tabulky úrovní pro úroveň kurzu a náročnost tématu (`ciselniky.md`); odchylka = WARN, ne FAIL.
- Délka celkem = součet modulů + capstone a odpovídá délce v katalogu a formátu (mikrokurz 30–45, pilotní kurz ZŠ 120); odchylka od katalogu = WARN. Nejvýše 12 obsahových modulů.
- Capstone má variantu A nebo B. Sekce 9 ARTEFAKT má šablonu sekcí a každá sekce má právě jedno „vzniká v“ — `M?/F4`, nebo `Capstone`. Počet sekcí = počet modulů + 1 úvodní sekce z capstone (5 modulů = 6 sekcí, jako ve vzoru A0601). Sekce, která by vznikala ve dvou modulech, je chyba: rozděl ji, nebo obě části slouč do jedné sekce jednoho F4.
- Rubrika: max. 5 kritérií, závazné názvy úrovní, váhy dávají 100 %, práh badge 75 %, routing silný / slabý / mezera.
- Zdroje: sekce existuje, má datum ověření, každý zdroj má DOI nebo URL; každé jméno autora citované v F1 je v seznamu.
- **Sekce 14 Zdrojové soubory a jejich role** existuje; každý soubor má formát md nebo docx a roli Obsah / Pravidla pro tvorbu / Hotový kurz; tabulka „Známé rozpory ve zdrojích“ existuje; rozpor bez rozhodnutí autora = WARN.
- Žádný placeholder („doplňte“, „…“, „TBD“, „lorem“).
- **Hlášení pro metodika:** „⚠“ nebo „PRO METODIKA“ v IMPULSU, F1–F4, capstone nebo testech = FAIL (Matrice v7.2, 13_Validace č. 60). Neprázdné pole „Otevřené problémy pro metodika“ = FAIL (před schválením kurzu musí být prázdné), nahrání ale nezastaví.

## B Definition of Done

Projdi 9 bodů DoD. U bodů, které nelze ověřit z textu (oponentura, zápis v katalogu, funkčnost odkazů), napiš „mimo rozsah QA, ověří autor / garant“. U autentických příkladů spočítej, kolik situací z praxe autora kurz skutečně používá (v IMPULSech, F2 scénářích, F3 položkách); méně než tři = FAIL.

## C Politika a styl

- Formáty: F2 každého modulu dialogický nebo aplikační (FMT-SOK, FMT-VLA, FMT-DVL, FMT-PRB, FMT-MIK, FMT-REF); uzavřené jen v F3 a skip-testech. Každý modul má alespoň jednu otevřenou nebo reflexivní položku a F3 končí metakognitivní otázkou. Instrukce pro agenta u každého F2/F3/F4 přítomna.
- F4 je formulováno jako instrukce k tvorbě konkrétní sekce a uvádí roli AI a co AI nesmí.
- Vykání všude (hledej tykání: „tvůj“, „zkus“, „ti“, „tě“). Terminologie jen kanonická (hledej „výsledky učení“, „VL“, „kvíz“ mimo F3, „aktivita“, „vstupní hák“, „M1“ v uživatelském textu).
- **Oslovení skupin** (`ciselniky.md`, Cílové skupiny): hledej „studente“, rodové označení akademika místo „vyučující“, záměnu „student na praxi“ a „žáci“ = WARN.
- **Profil úrovně:** výklad a otázky F3 odpovídají profilu úrovně kurzu (`ciselniky.md`; např. Začátečník: každý pojem AI vysvětlen při prvním výskytu, nejvýše 3 nové pojmy na modul; Pokročilý: bez elementárního výkladu a analogií). Nesoulad = WARN s místem.
- **Názvy modulů** a nadpisy vyjadřují, co účastník rozhoduje nebo čeho dosahuje, ne úkon s nástrojem; test: lze-li název nahradit pokynem ke kliknutí, je příliš zjednodušený; jazyk spisovný (Matrice v7.2, 0_Návod, 13_Validace č. 82). Nevyhovující název = WARN s návrhem.
- Jména v příkladech česká a střídaná; žádná Natalia. Obory v příkladech humanitní, žádné právo, biologie, ekonomie, medicína, informatika, obchodní komunikace (výjimka: oborový kurz daného předmětu).
- Žádné KRAUU kódy mimo sekci 7. Anchor text pojmenovává problém, není příslib („naučíte se“).
- **Zakázané věty (oddíl 6 `systemova_pravidla.md`)**: projdi všech osm skupin. Nález ze skupiny 6.4 (věty, které kurz sám odnaučuje) nebo 6.5 (rozpor se směrnicí a s doklady) = FAIL, ostatní skupiny = WARN. Hledej mimo jiné: „Skvělá“, „V dnešní době“, „Je důležité si uvědomit“, „Pojďme se podívat“, „revoluční“, „nesmírně“, „je tu a nikam nezmizí“, „jen nástroj“, „není otázka zda“, „stačí se správně zeptat“, „vezme vám práci“, „o krok napřed“, „detektor“, „poškozuje mozek“, „seznámíte se“, „si povíme“, „nebojte se“, „jednodušší, než si myslíte“, „zvládne to každý“, „první kurz“, „vaše cesta“, „navazuje kurz“.
- **Navazování kurzů (oddíl 2 `systemova_pravidla.md`)**: v první desítce kurzů se nepoužívá. Odkaz na jiný kurz v textu pro uživatele, vyplněné pole „Navazující kurzy (kódy)“ nebo routing v rubrice 11.3 mířící na jiný kurz = FAIL. Routing musí mířit na modul, fázi nebo sekci artefaktu téhož kurzu.
- Na sporné věty použij tři testy z oddílu 6.9 (zaměnitelnost, vlastní pravidlo, doložitelnost) a v reportu uveď, který test věta neprošla.
- **Fakta ve F1** (Matrice v7.2, 13_Validace č. 59): každé výzkumné tvrzení má zdroj, kontext (obor, populace, typ studie) a sílu důkazu; u preprintů a sporných efektů poznámku o síle evidence. Chybějící kontext nebo síla důkazu = WARN s místem, tvrzení bez zdroje = FAIL. Komerční produkty se nedoporučují jménem.
- **Odkazy na kurzy autorů** (KAJ/7033, KAJ/7135, jiné předměty v Moodlu) ve finálním podkladu = FAIL; obsah ano, odkaz ne (pokyn J. Pavlíkové, 18. 10. 2026).
- Pravidla používání AI pro účastníky existují (co smí, co ne, jak deklarovat). Dedikace TQ23000092 přítomna.
- Přístupnost: každá zmíněná grafika má popis nebo alt text; kurz je průchozí bez zvuku a videa.
- **Mediální přílohy:** každá má název s pořadím v modulu (`<KOD>-M<n>-<NN>-…`, kánon oddíl 9) a v sekci 10 přesnou pozici (modul, fáze, nadpis oddílu). Obrázky se na platformu vkládají ručně; chybějící pořadí nebo pozice = WARN. Formáty pro platformu PNG, SVG, MP3; MP4 uvedené jako příloha pro platformu = WARN (video jen mimo platformu).

## P Předpisy (normativní texty)

Když kurz vykládá normativní text (směrnice UJEP, AI Act, GDPR, zákon, studijní řád), vyžádej si jeho **oficiální znění** (PDF z webu instituce, ne pracovní verzi ani výklad) a ověř každé číslo článku nebo odstavce a obsah, který mu kurz přisuzuje: výchozí pravidla, podmínky, výjimky, okruh adresátů. Rozpor se zněním = FAIL. Oficiální znění není k dispozici = FAIL „nelze ověřit“. Příklad z 18. 10. 2026: A0101 přisuzoval odst. 5.1 Směrnice rektora č. 7/2026 povinnost předchozí konzultace, ačkoli odst. 5.1 stanoví výchozí režim „AI povolena s podmínkami“ a konzultaci ukládá jen odst. 5.3 u zadaných prací.

## D Duplicita a spirála

Otevři v katalogu řádky příbuzných kurzů (hledej podle kódu a tématu). Označ pasáže, které duplicitně zpracovávají obsah jiného kurzu, a pojmy, které kurz předpokládá, ale sám nevysvětluje. **Výsledek této kontroly je poznámka pro garanta, nikoli pokyn doplnit do kurzu odkaz** — v první desítce kurzů se navazování nepoužívá (oddíl 2 systémových pravidel). Chybějící vysvětlení pojmu se řeší doplněním do kurzu, ne odkazem jinam.

## Formát reportu

```
# QA report <KOD> <Název>   (datum, verze kurzu)
Nahrát na platformu: ANO / NE   (NE ze čtyř důvodů níže; pod řádkem výčet, co chybí)
Verdikt: … | FAIL: n | WARN: n | Odhad reálné délky: … min | Anotace: … znaků
Úroveň: … | Cílové skupiny: … | Modulů: n
## A Formální   (tabulka: kontrola | výsledek | místo | co změnit)
   Moduly   (tabulka: modul | délka | F1 min | F1 slov | náročnost | rozsah podle tabulky úrovní | výsledek)
## B Definition of Done   (9 řádků)
## C Politika a styl
## D Duplicita a spirála
## P Předpisy   (odstavec | co mu kurz přisuzuje | oficiální znění | výsledek)
## Sebehodnocení podle formuláře oponenta (10 oblastí, 1–4, připomínka)
## Simulovaný průchod účastníkem (za každou skupinu: kde by odešel, proč)
## Tři nejdůležitější změny
## Co funguje, zachovat
```

Buď konkrétní a stručný: jeden řádek na kontrolu. Nechval, nekomentuj vlastní postup.

## Řádek „Nahrát na platformu“

Odpověď NE vychází jen ze čtyř důvodů: (1) zdroje nejsou ověřené (chybí datum ověření, „Stav ověření: neověřeno“, chybějící DOI nebo URL), (2) v textu zůstal placeholder („K doplnění“, „doplňte“, „TBD“), (3) FAIL v oddílu P Předpisy, (4) v textu pro účastníky zůstalo hlášení „⚠ PRO METODIKA“ (platforma by ho vygenerovala do kurzu). Neprázdné pole „Otevřené problémy pro metodika“, délka, styl a ostatní WARN nahrání nezastaví. O nahrání rozhoduje autor nebo garant; řádek je doporučení, ne technická zábrana. Kurz se na platformu nahrává tak, že ho platforma z KURZ.md vygeneruje pomocí AI a autor výstup ručně doopraví, takže část oprav už touto kontrolou znovu neprojde.

Při odpovědi ANO připiš: „Po vygenerování kurzu na platformě spusťte `kontrola-kurzu`.“
