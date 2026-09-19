# Skilly PRAKTIK-AI v aplikaci Claude Desktop: návod pro metodičky a metodiky

Verze 1.0 | 19. 9. 2026 | Projekt TQ23000092 PRAKTIK-AI

Skill je balíček instrukcí, který Claude načte, když ho potřebuje. Místo dlouhého promptu a hromady dokumentů v projektu máte pět malých skillů, které znají katalog kurzů, matrici v6, číselníky, vzorový kurz A0601 a Definition of Done. Nainstalujete je jednou, používáte v každém chatu.

| Skill | Co dělá | Kdy ho zavoláte |
|---|---|---|
| praktik | rozcestník, rozhodne, který krok je na řadě | když nevíte, čím začít |
| praktik-rozhovor | 14 otázek protokolu, zapíše zadání kurzu | nový kurz, máte jen téma nebo kód |
| praktik-kurz | vygeneruje kurz: nejdřív kostru, pak moduly | máte zadání a zdrojový text |
| praktik-qa | zkontroluje kurz proti Definition of Done a formuláři oponenta | před odesláním oponentovi |
| praktik-export | vyrobí Word v domácím stylu | kurz je schválený |

## Co potřebujete

- Aplikaci Claude Desktop (Windows nebo Mac) a účet, který má zapnuté skilly (Pro, Max, Team nebo Enterprise).
- Soubory ze složky **09_Kurzy/PODKLADY_KURZU** na sdíleném Disku: podsložka `zips` (pět souborů .zip) a podsložka `skills` (rozbalené skilly).

## Cesta A: chat v Claude Desktop (doporučeno pro většinu práce)

1. Otevřete Claude Desktop a přihlaste se.
2. Klikněte vlevo dole na své jméno nebo iniciály a zvolte **Settings** (Nastavení).
3. Otevřete kartu **Capabilities** (Funkce). Zapněte přepínač **Code execution and file creation** (Spouštění kódu a vytváření souborů). Bez něj se skilly nenabídnou.
4. Na stejné kartě sjeďte k části **Skills**. Klikněte na **Upload skill** (Nahrát skill) a vyberte soubor `praktik.zip` ze složky `zips`.
5. Krok 4 zopakujte pro `praktik-rozhovor.zip`, `praktik-kurz.zip`, `praktik-qa.zip` a `praktik-export.zip`.
6. Zkontrolujte, že v seznamu Skills vidíte všech pět skillů a že mají zapnutý přepínač.
7. Otevřete nový chat. Přiložte zdrojový text (PDF článku, kapitola) a napište například:

   > Použij skill praktik-kurz. Kurz C1.5 Literatura: interpretace, rozhovor s autorem a jeho limity. Cílová skupina učitelé ČJ na SŠ. Tři situace z praxe: …

   Claude načte skill a začne kostrou kurzu. Když skill nezmíníte, Claude ho zpravidla vybere sám podle zadání. Když ne, napište jeho název do zprávy.
8. Hotový text kurzu si nechte uložit jako soubor a stáhněte ho. Pro Word napište „exportuj do docx“; Claude použije skill praktik-export.

Volitelně si založte projekt **PRAKTIK-AI kurzy**: do pole Project instructions vložte obsah souboru `Projektove_instrukce_v2.md`. Do znalostí projektu nenahrávejte matrici ani kurikulum, skilly je už obsahují. Zdrojové články přikládejte do jednotlivých chatů, ne do znalostí projektu.

## Cesta B: karta Code v Claude Desktop (pro práci se soubory na disku)

Hodí se, když chcete, aby kurz vznikal rovnou ve složce `09_Kurzy` a aby Claude četl a upravoval soubory na vašem počítači.

1. Zkopírujte si složku **PODKLADY_KURZU** z Disku na svůj počítač.
2. Ve složce `scripts` klikněte pravým tlačítkem na `install_skills.ps1` a zvolte **Spustit v PowerShellu**. Skript zkopíruje skilly do `C:\Users\<vaše jméno>\.claude\skills\`. Na Macu zkopírujte složky ze `skills` ručně do `~/.claude/skills/`.
3. V Claude Desktop otevřete kartu **Code**, klikněte na **Open folder** a vyberte složku kurzu (například `09_Kurzy/C0105LiteraturaRozhovorSAutorem`).
4. Do řádku napište `/praktik` a zadání. Skill se spustí, kurz vzniká jako soubor `<KOD>_<Nazev>_KURZ.md` ve zvolené složce, Word vedle něj.

## Jak s Claudem pracovat, aby to šetřilo čas i tokeny

- Nejdřív kostra, pak moduly. Skill se po kostře zastaví a čeká na váš souhlas. Opravujte kostru, ne hotové moduly.
- Tři autentické situace z praxe pošlete hned v první zprávě. Bez nich skill kurz nezačne.
- Zdrojový text přiložte jako soubor. Nevkládejte ho do textu zprávy a nenechte si ho opisovat do chatu.
- Když chcete změnu, řekněte kde a co: „v modulu 3 zkrať F1 na 300 slov“. Neříkejte „přegeneruj celý kurz“.
- Kontrolu (praktik-qa) spusťte před tím, než kurz pošlete oponentovi. Řešíte jen označená místa.

## Aktualizace skillů

Když se skilly změní, dostanete nové zipy. V Settings → Capabilities → Skills starý skill smažte a nahrajte nový. Na kartě Code stačí znovu spustit `install_skills.ps1`.

## Když něco nefunguje

| Potíž | Řešení |
|---|---|
| Tlačítko Upload skill nevidím | Zapněte Code execution and file creation; ověřte, že váš tarif skilly podporuje |
| Nahrání zipu selže | Zip musí obsahovat složku se souborem `SKILL.md`; použijte zipy ze složky `zips`, nebalte je znovu |
| Claude skill nepoužil | Napište název skillu do zprávy („použij skill praktik-kurz“) |
| Kurz vzniká v jiné struktuře než A0601 | Skill nebyl načten; ověřte, že je v seznamu zapnutý, a začněte nový chat |
| Na kartě Code `/praktik` nic nenabízí | Zkontrolujte složku `C:\Users\<jméno>\.claude\skills\praktik\SKILL.md`, restartujte relaci |

Kontakt: Jana Pavlíková, jana.pavlikova@ujep.cz. Zdrojové soubory skillů a tento návod jsou v repozitáři PODKLADY_KURZU a ve složce 09_Kurzy/PODKLADY_KURZU na Disku.
