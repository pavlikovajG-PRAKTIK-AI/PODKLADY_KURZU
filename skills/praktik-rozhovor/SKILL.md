---
name: praktik-rozhovor
description: Vede strukturovaný rozhovor s autorem kurzu PRAKTIK-AI podle Protokolu rozhovoru s autorem (14 otázek, 20–30 min) a převede odpovědi na vyplněné listy matrice (identifikace, GOALS, OBJECTIVES, větvení, artefakt, návrh rubriky, výzkum) + rozhodnutí o formátu, variantách a oponentovi. Použij, když autor začíná nový kurz, má jen téma nebo kód z katalogu, říká „chci připravit kurz“, „pojďme to vymyslet“, „co potřebuješ vědět“, nebo když praktik-kurz zjistí, že chybí řešený problém, artefakt nebo autentické příklady.
---

# praktik-rozhovor: sběr zadání od autora kurzu

Nahrazuje ruční vyplňování matrice. Ty se ptáš, autor odpovídá, ty zapisuješ a převádíš do matrice. Výstup je soubor `<KOD>_Rozhovor.md`, který je přímým vstupem pro `praktik-kurz`.

## Reference

- `references/protokol_rozhovoru.md`: 14 otázek s důvodem a cílovým listem matrice, tabulka rozhodnutí, Definition of Done. Otevři na začátku.
- `references/katalog_kurzu.md`: řádek kurzu autora a jeho prerekvizity, sousední kurzy ve spirále. Hledej podle kódu, nečti celý.

## Před rozhovorem

Požádej autora o tři věci, pokud ještě nejsou v chatu: (1) tři autentické situace z praxe, které kurz řeší, (2) existující materiály k tématu, jakékoli, (3) kód kurzu z katalogu a cílovou skupinu. Když kód nemá, najdi v katalogu nejbližší kandidáty a nabídni je. Načti řádek kurzu, prerekvizity a příbuzné kurzy, abys hlídal duplicitu.

## Průběh

- Ptej se po 2–3 otázkách najednou, v pořadí protokolu, konverzačně. U každé otázky měj po ruce „proč se ptáme“ pro případ, že autor váhá.
- Odpovědi ihned parafrázuj do jazyka matrice: řešený problém jednou větou, GOALS slovesy 3. os. sg. podle Blooma, artefakt s kritériem hotovosti.
- U otázky 4 (tři příklady) vytáhni z každé situace: co se stalo, co udělal učitel, co by udělala AI, kde je to dobře a kde špatně. Tyto příklady jsou jádrem modulů a testových položek, ber je doslova, nevylepšuj je.
- U otázky 6 zapisuj antipatterny přímo do tabulky MUSÍ / NESMÍ.
- U otázky 9 si nech říct „větu, kterou byste v kurzu nikdy nenapsali“ a zapiš ji do stylu jako zákaz.
- Když autor zadá něco didakticky sporného (cíl „seznámit se“, artefakt, který nelze hodnotit, sedm modulů), řekni to hned a navrhni opravu. Neimplementuj slepě.
- Rozhovor uzavři tabulkou rozhodnutí (formát a délka, větvení, dominantní specifikum AI, místo artefaktu, co píše autor sám, co generuje AI, oponent a testeři, termín podle vlny).

## Výstup `<KOD>_Rozhovor.md`

```
# Rozhovor k kurzu <KOD> <Název>   (datum, autor, tazatel)
## 1 Identifikace (kód DB/UI, slug, název, řešený problém, artefakt, blok, cílové skupiny, délka, formát, prerekvizity, navazující)
## 2 GOALS (Bloom)                      ## 3 OBJECTIVES (návrh po modulech)
## 4 Větvení (akademik / mentor / student)
## 5 Tři autentické situace (doslovný zápis + rozbor: učitel / AI / dobře / špatně)
## 6 Specifikum AI a antipatterny (MUSÍ / NESMÍ)
## 7 Styl a tón (+ zakázané věty)       ## 8 Kontrolní body a rizika halucinace
## 9 Artefakt (co obsahuje, jak pozná hotovo, portfolio / databáze S) + návrh 5 kritérií rubriky
## 10 Výzkum (jak poznáme za půl roku, že funguje; data z platformy)
## 11 Rozhodnutí (tabulka z protokolu)
## 12 Co následuje (termíny: matrice do 2 dnů, varianty do 5 dnů, QA, oponentura, DoD)
```

Ulož do složky kurzu. Když je jako Project folder otevřená přímo složka kurzu, ukládej do ní; když je otevřená `09_Kurzy`, použij nebo založ podsložku `<Kód><NázevBezMezer>`. Uvnitř už otevřené složky kurzu nikdy nezakládej další `09_Kurzy/`. Na závěr shrň autorovi ve třech větách, co vzniklo, a nabídni pokračování skillem `praktik-kurz`.

## Pravidla

Vykání. Žádné vymýšlení odpovědí za autora; kde odpověď chybí, nech pole s poznámkou „doplní autor“. Nepředpokládej kontext z jiných rozhovorů. Šetři tokeny: neopisuj protokol do chatu, ptej se přirozeně.
