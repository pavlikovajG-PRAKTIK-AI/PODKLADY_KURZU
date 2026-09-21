---
name: praktik-qa
description: Zkontroluje hotový nebo rozpracovaný kurz PRAKTIK-AI (soubor KOD_Nazev_KURZ.md) proti Definition of Done, deseti kritériím oponentního posudku, systémovým pravidlům a kánonu (terminologie, časy, F4 v každém modulu, dialogické formáty, vykání, jména a obory v příkladech, zdroje, KRAUU mimo texty pro uživatele) a vydá QA report s označenými místy k opravě. Použij, když autor chce „zkontrolovat kurz“, „projít Definition of Done“, „oponenturu nanečisto“, „co je špatně“, „připravit kurz na oponenta“, nebo před exportem.
---

# praktik-qa: kontrola kvality kurzu

Výstup je `<KOD>_QA_report.md` ve složce kurzu a stručné shrnutí v chatu. Kontroluješ, neopravuješ; opravy děláš jen když autor řekne „oprav“, a pak jako úpravy souboru, ne přegenerování.

## Reference

- `references/definition_of_done.md`: 9 podmínek DoD.
- `references/formular_oponenta.md`: 10 kritérií s tím, „na co se dívat“, škála 1–4.
- `references/systemova_pravidla.md`: identifikátory, časy, jazyk, terminologie.
- `references/kanon.md`: struktura, politika hodnocení, styl, zdroje (kopie z praktik-kurz).

## Postup

1. Načti soubor kurzu. Zjisti kód, počet modulů, deklarovanou délku.
2. Projdi kontroly A až D níže. Ke každé napiš PASS, FAIL nebo WARN, u FAIL a WARN přesné místo (sekce, modul, fáze) a jednu větu, co změnit.
3. Vyplň sebehodnocení podle formuláře oponenta (10 oblastí, škála 1–4) s jednou konkrétní připomínkou na oblast.
4. Simulovaný průchod: projdi kurz očima účastníka cílové skupiny po pracovní době. Zapiš, kde by odešel a proč, a odhad reálné délky.
5. Sepiš „Tři nejdůležitější změny“ v pořadí priority a „Co funguje, zachovat“.
6. Ulož report, v chatu shrň verdikt: připraven k oponentuře / vyžaduje úpravy (kolik FAIL) / nutné přepracování.

## A Formální kontroly (deterministické)

- Kód DB má formát písmeno + 4 číslice; kód UI odpovídá katalogu; slug bez diakritiky a mezer.
- Vyplněno: řešený problém, artefakt, anchor text, informační nota, text certifikátu, EQF, délka.
- **ANOTACE (oddíl 7 `systemova_pravidla.md`)**: existuje jako samostatný blok, **nejvýše 500 znaků** (spočítej je a uveď v reportu), struktura věta + `Témata:` + `Výstupy:`. FAIL, pokud chybí, přesahuje limit, nebo obsahuje délku kurzu, počet modulů, kód či název kurzu, druhou osobu (`projdete`, `odnesete si`, `abyste`, `naučíte se`), slogan, příslib, superlativ, rozsah artefaktu ve stranách nebo popis deficitu účastníka. Zkontroluj též, že anotace není totožná s anchor textem ani s informační notou — jsou to tři různé texty pro tři různé čtenáře (oddíl 7.3).
- GOALS: slovesa 3. os. sg. podle Blooma, poslední GOAL míří na artefakt; každý GOAL pokryt alespoň jedním modulem.
- OBJECTIVES: ID `<KOD>-Onn` unikátní, každý modul má 1–3, každá vazba na existující GOAL.
- Každý modul má: název, IMPULS, F1, F2 s kódem FMT, F3 s kódem FMT, F4 se sekcí artefaktu, NP kódy s fází. Součet minut fází = délka modulu; F1 ≤ 5 min; modul ≤ 30 min (cílově 15–20).
- Délka celkem = součet modulů + capstone a odpovídá formátu (kurz 60–105, mikrokurz 30–45, pilot ZŠ 120).
- Capstone má variantu A nebo B. Sekce 9 ARTEFAKT má šablonu sekcí a každá sekce má právě jedno „vzniká v“ — `M?/F4`, nebo `Capstone`. Počet sekcí = počet modulů + 1 úvodní sekce z capstone (5 modulů = 6 sekcí, jako ve vzoru A0601). Sekce, která by vznikala ve dvou modulech, je chyba: rozděl ji, nebo obě části slouč do jedné sekce jednoho F4.
- Rubrika: max. 5 kritérií, závazné názvy úrovní, váhy dávají 100 %, práh badge 75 %, routing silný / slabý / mezera.
- Zdroje: sekce existuje, má datum ověření, každý zdroj má DOI nebo URL; každé jméno autora citované v F1 je v seznamu.
- Žádný placeholder („doplňte“, „…“, „TBD“, „lorem“).

## B Definition of Done

Projdi 9 bodů DoD. U bodů, které nelze ověřit z textu (oponentura, zápis v katalogu, funkčnost odkazů), napiš „mimo rozsah QA, ověří autor / garant“. U autentických příkladů spočítej, kolik situací z praxe autora kurz skutečně používá (v IMPULSech, F2 scénářích, F3 položkách); méně než tři = FAIL.

## C Politika a styl

- Formáty: F2 každého modulu dialogický nebo aplikační (FMT-SOK, FMT-VLA, FMT-PRO, FMT-OTA, FMT-MIK, FMT-REF); uzavřené jen v F3 a skip-testech. Každý modul má alespoň jednu otevřenou nebo reflexivní položku a F3 končí metakognitivní otázkou. Instrukce pro agenta u každého F2/F3/F4 přítomna.
- F4 je formulováno jako instrukce k tvorbě konkrétní sekce a uvádí roli AI a co AI nesmí.
- Vykání všude (hledej tykání: „tvůj“, „zkus“, „ti“, „tě“). Terminologie jen kanonická (hledej „výsledky učení“, „VL“, „kvíz“ mimo F3, „aktivita“, „vstupní hák“, „M1“ v uživatelském textu).
- Jména v příkladech česká a střídaná; žádná Natalia. Obory v příkladech humanitní, žádné právo, biologie, ekonomie, medicína, informatika, obchodní komunikace (výjimka: oborový kurz daného předmětu).
- Žádné KRAUU kódy mimo sekci 7. Anchor text pojmenovává problém, není příslib („naučíte se“).
- **Zakázané věty (oddíl 6 `systemova_pravidla.md`)**: projdi všech osm skupin. Nález ze skupiny 6.4 (věty, které kurz sám odnaučuje) nebo 6.5 (rozpor se směrnicí a s doklady) = FAIL, ostatní skupiny = WARN. Hledej mimo jiné: „Skvělá“, „V dnešní době“, „Je důležité si uvědomit“, „Pojďme se podívat“, „revoluční“, „nesmírně“, „je tu a nikam nezmizí“, „jen nástroj“, „není otázka zda“, „stačí se správně zeptat“, „vezme vám práci“, „o krok napřed“, „detektor“, „poškozuje mozek“, „seznámíte se“, „si povíme“, „nebojte se“, „jednodušší, než si myslíte“, „zvládne to každý“, „první kurz“, „vaše cesta“, „navazuje kurz“.
- **Navazování kurzů (oddíl 2 `systemova_pravidla.md`)**: v první desítce kurzů se nepoužívá. Odkaz na jiný kurz v textu pro uživatele, vyplněné pole „Navazující kurzy (kódy)“ nebo routing v rubrice 11.3 mířící na jiný kurz = FAIL. Routing musí mířit na modul, fázi nebo sekci artefaktu téhož kurzu.
- Na sporné věty použij tři testy z oddílu 6.9 (zaměnitelnost, vlastní pravidlo, doložitelnost) a v reportu uveď, který test věta neprošla.
- Kalibrace jistoty: u preprintů a sporných efektů je v F1 poznámka o síle evidence. Komerční produkty se nedoporučují jménem.
- Pravidla používání AI pro účastníky existují (co smí, co ne, jak deklarovat). Dedikace TQ23000092 přítomna.
- Přístupnost: každá zmíněná grafika má popis nebo alt text; kurz je průchozí bez zvuku a videa.

## D Duplicita a spirála

Otevři v katalogu řádky příbuzných kurzů (hledej podle kódu a tématu). Označ pasáže, které duplicitně zpracovávají obsah jiného kurzu, a pojmy, které kurz předpokládá, ale sám nevysvětluje. **Výsledek této kontroly je poznámka pro garanta, nikoli pokyn doplnit do kurzu odkaz** — v první desítce kurzů se navazování nepoužívá (oddíl 2 systémových pravidel). Chybějící vysvětlení pojmu se řeší doplněním do kurzu, ne odkazem jinam.

## Formát reportu

```
# QA report <KOD> <Název>   (datum, verze kurzu)
Verdikt: … | FAIL: n | WARN: n | Odhad reálné délky: … min | Anotace: … znaků
## A Formální   (tabulka: kontrola | výsledek | místo | co změnit)
## B Definition of Done   (9 řádků)
## C Politika a styl
## D Duplicita a spirála
## Sebehodnocení podle formuláře oponenta (10 oblastí, 1–4, připomínka)
## Simulovaný průchod účastníkem (kde by odešel, proč)
## Tři nejdůležitější změny
## Co funguje, zachovat
```

Buď konkrétní a stručný: jeden řádek na kontrolu. Nechval, nekomentuj vlastní postup.
