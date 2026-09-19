---
name: praktik
description: Vstupní bod pro tvorbu kurzů platformy PRAKTIK-AI (projekt TQ23000092, UJEP + OU). Použij, když metodik/metodička mluví o kurzu, modulu, matrici, artefaktu, rubrice, oponentuře, katalogu kurzů nebo o PRAKTIK-AI a neřekne přímo, který krok chce. Rozhodne mezi praktik-rozhovor (sběr zadání od autora), praktik-kurz (generování kurzu), praktik-qa (kontrola kvality), praktik-export (docx) a av-materialy (video, audio, grafika).
---

# praktik: rozcestník tvorby kurzu PRAKTIK-AI

Postup tvorby kurzu má pět kroků. Zjisti, kde autor je, a pokračuj příslušným skillem. Neptej se na víc než jednu věc.

| Situace | Skill |
|---|---|
| Autor má téma nebo kód kurzu, ale ne řešený problém, artefakt a tři autentické situace z praxe | `praktik-rozhovor` |
| Autor má zadání (výstup rozhovoru nebo vyplněnou matrici) a zdrojový text, chce kurz nebo moduly | `praktik-kurz` |
| Existuje soubor `<KOD>_…_KURZ.md` a autor chce kontrolu, oponenturu nanečisto, Definition of Done | `praktik-qa` |
| Kurz je hotový a schválený, potřebuje docx pro oponenta a garanta | `praktik-export` |
| Kurz potřebuje video shrnutí, audio, animaci, infografiky | `av-materialy` |

## Pořadí a výstupy

```
1 rozhovor  →  <KOD>_Rozhovor.md          (2 pracovní dny po rozhovoru: matrice ke schválení)
2 kurz      →  <KOD>_<Nazev>_KURZ.md      (kostra → schválení → moduly po jednom)
3 qa        →  <KOD>_QA_report.md         (autor řeší jen označená místa)
4 export    →  .docx                      (docx oponentovi a garantovi)
5 av        →  mp4, mp3, svg, html        (skill av-materialy)
→ oponentura (Formulář oponenta) → zapracování → Definition of Done → katalog → nasazení dle vlny
```

## Co platí napříč kroky

- Zdroj pravdy o kurzech je katalog 2026-09 (kódy, artefakty, cílové skupiny, vlny). Kód kurzu vždy ověř, nevymýšlej.
- Vzorový kurz je A0601 „Vývoj dětského mozku v éře AI“. Když si autor není jistý formou, ukaž mu modul 1 ze vzoru.
- Šetři tokeny: čti jen potřebné reference, generuj kostru před moduly, změny dělej úpravou souboru.
- Terminologie, styl a pravidla jsou v `praktik-kurz/references/kanon.md`. Neduplikuj je, odkazuj.
- Vše česky, vykání, bez AI balastu.

Když si nejsi jistý, kde autor je, zeptej se: „Máte už kód kurzu z katalogu a tři autentické situace z praxe, nebo začneme rozhovorem?“
