# Protokol rozhovoru s autorem kurzu (verze 1.1, 18. 10. 2026)

Projekt TQ23000092 PRAKTIK-AI. Strukturovaný 20–30minutový rozhovor, který nahrazuje ruční vyplňování Matrice kurzu v7.2. Autor odpovídá, tazatel (metodický architekt nebo AI asistent) zapisuje a převádí do matrice. Použití před tvorbou každého kurzu (bloky A–D, Z). Pro rodinu příbuzných kurzů lze vést jeden rozhovor a odlišnosti doplnit v části rozhodnutí.

Výstup: vyplněné listy 00_Zalozeni (0.1 hlavička), 1_Identifikace včetně 1.8, 14_Zdroje, 2_GOALS, 3_OBJECTIVES, 4_Větvení, 9_Artefakt, 11_Rubrika (návrh) a 12_Výzkum + seznam tří autentických příkladů + rozhodnutí o variantách.

## Před rozhovorem (autor pošle den předem)

- Tři autentické situace z praxe, které kurz řeší (zadání, chyba žáka či studenta, věta rodiče, konkrétní text). Bez nich kurz nevzniká.
- Existující materiály k tématu (prezentace, sylabus, článek, dřívější draft), cokoli, i nedokončené. U každého materiálu jeho roli (obsah kurzu / pravidla pro tvorbu / hotový kurz ke konverzi) a známé rozpory mezi zdroji (list 14_Zdroje; generátor platformy přijímá jen .md a .docx).
- Kód kurzu z katalogu (např. C1.6) a cílovou skupinu (Akademik / Student / Mentor); když kurz v katalogu není, krátký důvod, proč vzniká.

Tazatel si předem načte katalog, kurikulum bloku a příbuzné kurzy (spirála), aby nevznikal duplicitní obsah.

## Otázky

| # | Otázka autorovi | Proč se ptáme | List matrice |
|---|---|---|---|
| 1 | Jaký konkrétní problém z praxe má účastník po kurzu umět vyřešit? Popište ho jednou větou, jako byste ho říkali kolegovi. | Kurz = řešený problém, ne předmět. Věta se stane „Řešeným problémem“ a základem GOAL. | 1_Identifikace, 2_GOALS |
| 2 | Co si účastník z kurzu odnese do ruky (artefakt)? Jak pozná, že je hotový a dobrý? Z čeho se skládá? | Artefakt je důkaz kompetence, jde do portfolia nebo databáze S; kritéria = základ rubriky. Vyjmenované části rovnou rozdělte na sekce: kolik modulů, tolik sekcí + jedna úvodní z capstone, a každá sekce vzniká v právě jednom F4. Když autor vyjmenuje víc částí, slučte je s ním hned na místě — původní položky zůstanou jako obsah sekce, nic se neztratí. Slaďte s odpovědí na otázku 7. | 9_Artefakt, 11_Rubrika |
| 3 | Kdo je účastník? Akademik (vč. doktorandů), Student (Bc., Mgr.), Mentor (provázející učitel ZŠ/SŠ)? Jakou má zkušenost s AI: začátečník, středně pokročilý, pokročilý? Co si o AI myslí? | Určuje větvení, tón, prerekvizity, délku F1 a profil výkladu. Úroveň se týká zkušenosti s AI, ne odbornosti v oboru. Různé profily = různé příklady, ne různé cíle. Učitel ZŠ/SŠ patří pod Mentora; vedení školy číselník nemá (uvádět jen v příkladech). | 1_Identifikace 1.2 Úroveň, 1.8, 4_Větvení |
| 4 | Projděme vaše tři příklady: co se v nich stalo, co udělal učitel, co by udělala AI a kde je to špatně nebo dobře? | Autenticita je to jediné, co AI nevymyslí. Příklady se stanou jádrem modulů a testových položek. | M1–M12, 8_Vzory |
| 5 | Jaké je v tomto tématu specifikum AI: nástroj učitele, předmět výuky, dialogický partner, riziko, nebo tvůrčí spolupracovník? Co z toho je hlavní? | Určuje dominantní osu kurzu a brání „obecnému kurzu o AI“. | 2_GOALS, 6_AI_principy |
| 6 | Co v tomto oboru s AI neplatí nebo je tabu? Jaká je typická past, do které učitelé padají? | Antipatterny a limity odlišují kurz od komerčního školení. | 8_Vzory_antipatterns |
| 7 | Co by účastník měl zvládnout na konci každého modulu (kroky k artefaktu, jeden na modul)? Který krok je pojmově nejnáročnější? Kde může zkušený přeskočit testem? | Cíle modulů (Bloom), náročnost tématu (určuje délku F1), skip logika, návaznost. | 3_OBJECTIVES, 1.5 Skip, M1–M12 (Náročnost tématu) |
| 8 | Jaká je přijatelná délka a formát? Kurz 60–90 min, mikrokurz 30–45 min, 2 h pro ZŠ? Chcete audio nebo video shrnutí (video jen mimo platformu)? | Délka je hlavní příčina nedokončení. Mikroformát a multimodalita zvyšují dokončování. | 1.2 Parametry, 1.8 Počet modulů, 10_Mediální_přílohy |
| 9 | Jakým hlasem má kurz mluvit (konverzační, narativní, instruktážní, analytický)? Věta, kterou byste v kurzu nikdy nenapsali? | Tón a „ne-věty“ chrání před AI balastem a uniformitou. | 1.6 Styl a tón |
| 10 | Co musí účastník ověřit sám (fakta, nástroje, právní rámec) a kde je riziko halucinace? | Kontrolní body a povinné ověřování; podklad pro QA. | 6_AI_principy, 13_Validace |
| 11 | Na jaké kurzy navazujete a co z nich předpokládáte? Co naopak necháváte jiným kurzům? | Spirála bez opakování; prerekvizity; hranice kurzu. | 1.2 Prerekvizity, Navazující |
| 12 | Jak poznáme za půl roku, že kurz funguje? Jaká data z platformy nebo od účastníků k tomu potřebujete? | Evaluace a výzkum (indikátory 40/200, pre-post, logy) se plánují od začátku. | 12_Výzkum |
| 13 | Který váš absolvent (učitel z praxe, doktorand) nebo kolega z jiné katedry by byl vhodný oponent a kdo by měl kurz testovat jako první? | Oponenti = absolventi UJEP a interní kolegové, ne placení externisté; viz katalog, sloupec Oponent – doporučení. | — |
| 14 | Co byste chtěli, aby za vás udělala AI, a co si chcete napsat sami? | Vlastnictví kurzu: autor rozhoduje, co je jeho hlas. Vše ostatní se generuje ve variantách. | — |

## Rozhodnutí na konci rozhovoru (zapsat)

| Rozhodnutí | Volba autora |
|---|---|
| Formát a délka | kurz 60–90 min / mikrokurz 30–45 min / pilotní kurz ZŠ 2 h / audio-video shrnutí |
| Větvení podle profilu | jeden kurz s větvením / samostatné varianty pro: … |
| Dominantní specifikum AI | N nástroj / P předmět / D dialog / R riziko / T tvůrčí |
| Artefakt a jeho místo | portfolio / databáze S (veřejné) / oba |
| Co píše autor sám | … |
| Co generuje AI ve variantách | … |
| Oponent / první testeři | … |
| Termín 1. verze k výběru variant | … (vlna dle katalogu: V…) |

## Co následuje po rozhovoru

1. Do 2 pracovních dnů: vyplněná matrice (listy 00, 1–4, 9, 11, 12, 14) + rešerše podkladů a mapování na DigCompEdu / UNESCO AI CF → autor schválí nebo opraví (15 min).
2. Do 5 pracovních dnů: kurz vygenerován ve 2–3 variantách (profil / délka / tón) + jednostránkové srovnání → autor vybere a doplní vlastní pasáže.
3. Automatická kontrola kvality (číselníky, časy, odkazy, citace, balast, duplicita) + simulovaný průchod studentem → autor řeší jen označená místa.
4. Oponentura (absolvent / interní kolega) dle formuláře → zapracování → Definition of Done → nasazení do pilotu.

## Definition of Done (kurz je hotový, když…)

- Řešený problém, GOAL a artefakt jsou konzistentní a artefakt je použitelný ve výuce bez dalších úprav.
- Kurz obsahuje ≥ 3 autentické příklady autora a ≥ 1 explicitní limit / antipattern.
- Délka v limitu formátu; moduly obvykle 15–25 min, nejvýše 30 min; každý modul má cíl a kontrolu porozumění.
- Všechny nástroje, odkazy a citace ověřeny (existují, fungují, jsou aktuální k datu vydání).
- Pravidla používání AI pro účastníky jsou explicitní (co smí, co ne, jak deklarovat).
- Přístupnost: alternativní text k obrázkům, čitelnost, varianta bez zvuku a videa.
- Mapování na DigCompEdu / UNESCO AI CF a dedikace projektu TQ23000092 doplněny.
- Oponentní posudek s verdiktem „doporučuji“ nebo „doporučuji s úpravami“ a úpravy zapracovány.
- Zapsáno v katalogu: verze, datum, autor, oponent, vlna nasazení.
