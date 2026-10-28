# Grafika ke kurzu PRAKTIK-AI

Postup ověřený na kurzu B10 / B1001 (28. 10. 2026). Grafika nese obsah F1 (NP-06 duální kódování). Kurz se bez ní musí dát projít, ale s ní se mu rozumí rychleji. Dekorace bez obsahu do kurzu nepatří.

## 0 Paleta a identifikace platformy (STAV: čeká na J. Pavlíkovou)

Barevné kódování a identifikaci platformy (logo, název, barvy) dodá J. Pavlíková. **Dokud tento oddíl obsahuje text „čeká na J. Pavlíkovou“, připomeň jí to hned na začátku tvorby každého kurzu** (v první odpovědi, jednou větou), a do té doby používej neutrální paletu z oddílu 4. Po dodání sem zapiš barvy (hex), pravidla pro logo a umístění identifikace a skript `grafika_zaklad.py` uprav podle nich.

## 1 Kdy grafika vzniká

1. **Kostra:** ke každému modulu navrhni 1–2 grafiky. Návrh vypiš **hned do chatu** jako tabulku (soubor · kam patří · co na obrázku je), uživatelka podle ní pracuje. Do kostry ho zapiš jako sekci 10.
2. **Moduly:** na místo obrázku v textu vlož samostatný řádek `![alt text](<název souboru>)` (kánon oddíl 9). Polohu určuje místo v textu.
3. **Po kontrole věrnosti a korektuře textu** grafiku vykresli. Texty grafiky berou znění z hotového, ověřeného kurzu, ne z kostry.
4. **Po každé změně textu kurzu**, která se týká grafiky, uprav skript a vykresli znovu. Grafika a text se nesmějí rozejít.

## 2 Co se hodí na obrázek

| Typ | Kdy | Příklad z B10 |
|---|---|---|
| schéma postupu (šipky, větvení) | rozhodování krok za krokem | postup, když deklarace chybí |
| srovnání dvou variant vedle sebe | dvě formulace, dvě oblasti, před × po | obecné × konkrétní pravidlo |
| řádky „vstup → mezikrok → výsledek“ | vazba příčiny a důsledku | úkol → co má prokázat → režim |
| formulář nebo karta | co má účastník vyplnit | deklarace se čtyřmi údaji |
| obraz návratové metafory kurzu | schéma, ke kterému se moduly vracejí (NP-20) | semafor režimů |

Nehodí se: odstavec textu převedený do obrázku, fotografie bez informace, ilustrace „pro náladu“, grafy bez zdrojových dat.

## 3 Obsah grafiky

- Na obrázku je jen to, co říká ověřený text kurzu. **Žádné nové tvrzení.** Každý text grafiky projde stejnou kontrolou věrnosti jako F1.
- Předpis cituj doslovně (názvy režimů, údaje deklarace), odkaz na odstavec dej do textu nebo do patičky.
- Patička nese zdroj: „Podle odst. 5.1 Směrnice rektora UJEP č. 7/2026.“ U vlastního příkladu „Příklad: …“.
- Nejvýše zhruba 60 slov na obrázek. Co se nevejde, patří do textu F1.
- Česká typografie: české uvozovky „…“, žádná jednopísmenná předložka ani spojka (v, k, s, z, o, u, a, i) na konci řádku, „odst. 5.1“ nedělit, rozsahy s pomlčkou bez mezer.
- Alt text v značce i v sekci 10 popisuje obsah obrázku tak, aby ho pochopil člověk, který obrázek nevidí.

## 4 Vizuální pravidla

| Prvek | Pravidlo |
|---|---|
| formát | PNG 1600 × 900 px (16 : 9); kreslí se ve 2× rozlišení a zmenšuje (hladké hrany) |
| pozadí | vždy světlé (#FFFFFF, panely #F5F7FA); nikdy tmavý režim |
| text | vždy tmavý: hlavní #1F2933, vedlejší #52606D; vysoký kontrast |
| akcentní barvy | střídmě a **nikdy pro text**: jen rámeček, šipka, značka, kruh; neutrální paleta: modrá #1F5FA8, červená #C62828, jantarová #E0A100, zelená #2E7D32; barva vždy nese význam (např. semafor režimů) a v celém kurzu stejný |
| písmo | jen Segoe UI ve dvou řezech: Regular (text) a Semibold (nadpisy, popisky); žádný Bold, žádná kurzíva |
| velikosti | pevná škála: titulek 44 · velký nadpis 36 · nadpis 30 · text 27 · patička 22 px; jiné velikosti nepoužívat |
| čáry | rámeček 2 px (#CBD2D9) · zvýrazněný rámeček 3 px (akcent) · šipka 4 px; jiné tloušťky nepoužívat |
| rozvržení | okraje 70 px, titulek nahoře s linkou pod ním, patička se zdrojem dole, zarovnání do mřížky; rámečky se zaoblením 18 px |
| symboly | kreslit tvary (políčko, fajfka, křížek, šipka), ne znaky písma (☐ ✓ Segoe UI nemá) |

## 5 Výroba

1. Ve složce kurzu založ podsložku `grafika` a zkopíruj do ní `references/grafika_zaklad.py` jako `vykresli_grafiku.py`.
2. Pro každý obrázek napiš funkci, která kreslí pomocí připravených pomocníků (`new`, `box`, `arrow`, `text_block`, `footer`, `save`) a stylů z oddílu 4. Souřadnice zadávej v logických pixelech 1600 × 900.
3. Názvy souborů podle kánonu: `<KOD>-M<n>-<NN>-<typ>-<popis>.png` (typ: grafika, schema).
4. Spusť `python vykresli_grafiku.py` ze složky `grafika`.

## 6 Kontrola (každý obrázek, vždy)

Každý PNG si prohlédni (nástroj Read) a projdi:

- [ ] text nikde nepřetéká z rámečku ani z plochy
- [ ] žádná jednopísmenná předložka na konci řádku, „odst.“ u čísla
- [ ] jen dva řezy písma a velikosti ze škály; tloušťky čar ze škály
- [ ] akcentní barva není použitá pro text
- [ ] text grafiky odpovídá ověřenému znění kurzu (citace doslovně, čísla odstavců)
- [ ] patička se zdrojem; alt text v značce i v sekci 10 sedí na obsah
- [ ] název souboru = název ve značce `![…](…)` = název v sekci 10

Po vykreslení pošli uživatelce obrázky do chatu (SendUserFile, zobrazit) a stručně uveď, co se proti návrhu změnilo.
