# Skilly PRAKTIK-AI v kartě Code v Claude Desktop: návod pro metodičky a metodiky

Verze 1.4 | 19. 9. 2026 | Projekt TQ23000092 PRAKTIK-AI

Skill je balíček instrukcí, který Claude načte, když ho potřebuje. Místo dlouhého promptu a hromady dokumentů v projektu máte pět malých skillů, které znají katalog kurzů, matrici v6, číselníky, vzorový kurz A0601 a Definition of Done. Nainstalujete je jednou, používáte v každém kurzu.

| Skill | Co dělá | Kdy ho zavoláte |
|---|---|---|
| praktik | rozcestník, rozhodne, který krok je na řadě | když nevíte, čím začít |
| praktik-rozhovor | 14 otázek protokolu, zapíše zadání kurzu | nový kurz, máte jen téma nebo kód |
| praktik-kurz | vygeneruje kurz: nejdřív kostru, pak moduly | máte zadání a zdrojový text |
| praktik-qa | zkontroluje kurz proti Definition of Done a formuláři oponenta | před odesláním oponentovi |
| praktik-export | vyrobí Word v domácím stylu | kurz je schválený |

## Co potřebujete

- Aplikaci Claude Desktop s kartou **Code** a placený tarif Claude (Pro, Max, Team nebo Enterprise). Skilly v kartě Code žádný přepínač v nastavení nepotřebují; stačí, že jejich složky leží na disku.
- Nainstalovaný **Python** s balíčkem `python-docx` (`pip install python-docx`). Potřebuje ho jen export do Wordu.
- Celou složku **09_Kurzy/PODKLADY_KURZU** zkopírovanou z Disku na svůj počítač.

Pracujeme výhradně v kartě Code: Claude tam čte a upravuje soubory přímo ve složce kurzu na vašem počítači, kurz vzniká rovnou jako soubor a nemusíte nic ručně stahovat ani nahrávat.

## Instalace skillů (uděláte jednou)

1. Zkopírujte si složku **PODKLADY_KURZU** z Disku na svůj počítač.
2. Ve složce `scripts` dvakrát klikněte na `Nainstalovat_skilly.cmd`. Funguje to v Průzkumníku i v jiných správcích souborů (např. Total Commander), kde volba „Spustit v PowerShellu“ v kontextovém menu chybí. Skript zkopíruje skilly do `C:\Users\<vaše jméno>\.claude\skills\`. Na Macu skilly nainstalujte ručně: zkopírujte složky ze `skills` do `~/.claude/skills/`.
3. Hotovo. Claude Code složku se skilly sleduje a novou i změněnou verzi zachytí i v už běžící relaci; restartovat nemusíte. Když se skill přesto nenabídne, otevřete novou relaci.

## Práce s kurzem

1. V Claude Desktop otevřete kartu **Code**. Ještě před odesláním první zprávy nastavte v řádku promptu **Project folder** a vyberte složku kurzu (například `09_Kurzy/C0105LiteraturaRozhovorSAutorem`). Když složka kurzu ještě neexistuje, vyberte `09_Kurzy` a nechte ji Clauda založit podle konvence `<Kód><NázevBezMezer>`. Ve stejném řádku se nastavuje prostředí, model a režim oprávnění.
2. Vybraná složka je Claudův pracovní prostor: soubory kurzu v ní vznikají a upravují se rovnou. Na cokoli mimo ni se Claude ptá na svolení, takže se sám nedostane ke zbytku disku.
3. Do řádku napište zadání a přiložte zdrojový text jako soubor (PDF článku, kapitola), například:

   > Použij skill praktik-kurz. Kurz C1.5 Literatura: interpretace, rozhovor s autorem a jeho limity. Cílová skupina učitelé ČJ na SŠ. Tři situace z praxe: …

   Claude načte skill a začne kostrou kurzu. Když skill nezmíníte, Claude ho zpravidla vybere sám podle zadání; když ne, napište jeho název do zprávy (nebo rovnou `/praktik`). Kurz vzniká jako soubor `<KOD>_<Nazev>_KURZ.md` ve zvolené složce.
4. Pro Word napište „exportuj do docx“; Claude použije skill praktik-export a soubor uloží vedle `.md`.

## Jak s Claudem pracovat, aby to šetřilo čas i tokeny

- Nejdřív kostra, pak moduly. Skill se po kostře zastaví a čeká na váš souhlas. Opravujte kostru, ne hotové moduly.
- Tři autentické situace z praxe pošlete hned v první zprávě. Bez nich skill kurz nezačne.
- Zdrojový text přiložte jako soubor. Nevkládejte ho do textu zprávy a nenechte si ho opisovat do chatu.
- Když chcete změnu, řekněte kde a co: „v modulu 3 zkrať F1 na 300 slov“. Neříkejte „přegeneruj celý kurz“.
- Kontrolu (praktik-qa) spusťte před tím, než kurz pošlete oponentovi. Řešíte jen označená místa.

## Aktualizace skillů

Když se skilly změní, dostanete novou složku `PODKLADY_KURZU` (nebo jen podsložku `skills`). Nahraďte jí tu starou u sebe na počítači a ve složce `scripts` znovu spusťte `Nainstalovat_skilly.cmd` — přepíše starou verzi novou. Nová verze platí hned, i v otevřené relaci.

## Když něco nefunguje

| Potíž | Řešení |
|---|---|
| Kartu Code v Claude Desktop nevidím | Ověřte, že máte placený tarif (Pro, Max, Team nebo Enterprise) a aktuální verzi aplikace |
| `install_skills.ps1` / `Nainstalovat_skilly.cmd` se nespustí | Zkuste druhý ze souborů — `.cmd` funguje dvojklikem v libovolném správci souborů, `.ps1` jen v Průzkumníku přes „Spustit v PowerShellu“ |
| Na kartě Code `/praktik` nic nenabízí | Zkontrolujte, že existuje soubor `C:\Users\<jméno>\.claude\skills\praktik\SKILL.md`; když existuje, otevřete novou relaci |
| V Settings → Skills vidím jen některé skilly | Ten seznam ukazuje skilly nahrané do účtu Claude (pro chat), ne složku na disku, ze které čte karta Code. Instalaci ověřte v kartě Code: napište / a v nabídce musí být všech pět praktik* |
| Claude skill nepoužil | Napište název skillu do zprávy („použij skill praktik-kurz“) |
| Kurz vzniká v jiné struktuře než A0601 | Skill nebyl načten; ověřte, že soubory jsou v `C:\Users\<jméno>\.claude\skills\`, a začněte novou relaci |
| Export do docx skončí hláškou „Chybí python-docx“ | Nechte Clauda spustit `pip install python-docx` a export zopakujte |

Kontakt: Jana Pavlíková, jana.pavlikova@ujep.cz. Zdrojové soubory skillů a tento návod jsou ve složce 09_Kurzy/PODKLADY_KURZU na sdíleném Disku.
