"""Export kurzu z platformy PRAKTIK-AI přes veřejné API (bez přihlášení, bez stopy v účtu).

Použití:
  python export_kurz.py 9 -o vystup.md          # kurz podle ID
  python export_kurz.py --najdi A0601 -o vystup.md   # kurz podle kódu v názvu nahraného souboru

Výstup: Markdown s metadaty, příručkami očíslovanými po odstavcích (M1-1, M1-2 …)
a otázkami k procvičování s vyznačenou správnou odpovědí.
"""
import argparse
import json
import re
import sys
import urllib.request
from html.parser import HTMLParser

API = "https://test.praktik.ujep.cz/api/api/v1/courses/{}"


def nacti(cid):
    req = urllib.request.Request(API.format(cid), headers={"Accept": "application/json"})
    with urllib.request.urlopen(req, timeout=30) as r:
        return json.loads(r.read().decode("utf-8"))


def najdi(kod, maximum=60):
    for cid in range(1, maximum + 1):
        try:
            c = nacti(cid)
        except Exception:
            continue
        soubory = " ".join(f.get("filename", "") for f in c.get("files") or [])
        if kod.lower() in soubory.lower():
            return cid
    return None


class Text(HTMLParser):
    BLOKY = ("p", "li", "h1", "h2", "h3", "h4", "tr")

    def __init__(self):
        super().__init__()
        self.out, self.cur, self.tag = [], "", None

    def handle_starttag(self, t, a):
        if t in self.BLOKY:
            self.flush()
            self.tag = t
        if t == "img":
            self.flush()
            a = dict(a)
            self.out.append(("img", "[obrázek alt=\"%s\" soubor=%s]" % (a.get("alt", ""), (a.get("src") or "").split("/")[-1])))
        if t in ("strong", "b"):
            self.cur += "**"
        if t in ("td", "th"):
            self.cur += " | "
        if t == "br":
            self.cur += " "

    def handle_endtag(self, t):
        if t in ("strong", "b"):
            self.cur += "**"
        if t in self.BLOKY:
            self.flush()

    def handle_data(self, x):
        self.cur += x

    def flush(self):
        t = re.sub(r"\s+", " ", self.cur).strip().replace("****", "")
        if t:
            self.out.append((self.tag or "p", t))
        self.cur, self.tag = "", None


def kody(seznam, *klice):
    vysl = []
    for x in seznam or []:
        for k in klice:
            if x.get(k):
                vysl.append(str(x[k]))
                break
    return ", ".join(vysl)


def export(c):
    o = []
    meta = {k: v for k, v in c.items() if k != "modules"}
    o.append("# Export kurzu z platformy: %s (ID %s)\n" % (c.get("title"), c.get("course_id")))
    o.append("Stav: %s · aktualizováno: %s · nahraný soubor: %s\n" % (
        c.get("status"), c.get("updated_at"), ", ".join(f.get("filename", "") for f in c.get("files") or [])))
    o.append("## Metadata\n")
    o.append("| Pole | Hodnota |\n|---|---|")
    radky = [
        ("Popis (anotace)", (c.get("description") or "").replace("\n", " ⏎ ")),
        ("Blok", (c.get("course_block") or {}).get("name")),
        ("Cílová skupina", (c.get("course_target") or {}).get("name")),
        ("Obor", (c.get("course_subject") or {}).get("name")),
        ("Povinnost", (c.get("course_requirement") or {}).get("name")),
        ("EQF", (c.get("course_eqf_level") or {}).get("code")),
        ("Úroveň", (c.get("course_level") or {}).get("name")),
        ("Typ", (c.get("course_type") or {}).get("name")),
        ("Délka (min)", c.get("duration_minutes")),
        ("Obtížnost", c.get("difficulty")),
        ("Počet modulů", c.get("modules_count")),
        ("KRAUU", kody(c.get("krauu_competences"), "code")),
        ("Bloom", kody(c.get("bloom_levels"), "code")),
        ("Průřezové obory", kody(c.get("cross_subjects"), "code")),
    ]
    for k, v in radky:
        o.append("| %s | %s |" % (k, "—" if v in (None, "") else v))
    o.append("\n<details><summary>Úplná metadata (JSON)</summary>\n\n```json\n%s\n```\n</details>\n" % json.dumps(meta, ensure_ascii=False, indent=1))

    for i, m in enumerate(c.get("modules") or [], 1):
        o.append("\n# Modul %d (id %s): %s\n" % (i, m.get("module_id"), m.get("title")))
        o.append("_Perex:_ %s\n" % m.get("perex"))
        o.append("NP: %s · KRAUU: %s · Bloom: %s\n" % (
            kody(m.get("neuro_principles"), "code"), kody(m.get("krauu_competences"), "code"), kody(m.get("bloom_levels"), "code")))
        poradi_obr = 0
        for lb in m.get("learn_blocks") or []:
            p = Text()
            p.feed(lb.get("content") or "")
            p.flush()
            n = 0
            for t, x in p.out:
                if t in ("h1", "h2", "h3", "h4"):
                    o.append("\n## %s\n" % x)
                elif t == "img":
                    poradi_obr += 1
                    o.append("[M%d-obr%02d] %s\n" % (i, poradi_obr, x))
                else:
                    n += 1
                    o.append("[M%d-%d] %s\n" % (i, n, x))
        o.append("\n## Otázky k procvičování\n")
        for q in m.get("practice_questions") or []:
            o.append("- [%s] %s" % (q.get("question_type"), q.get("question")))
            for op in q.get("closed_options") or []:
                znak = "✓ " if op.get("text") == q.get("correct_answer") else ""
                o.append("   - %s%s" % (znak, op.get("text")))
            if q.get("example_answer"):
                o.append("   - VZOR: %s" % q["example_answer"])
            if q.get("open_keywords"):
                o.append("   - KLÍČ: " + " / ".join(k.get("keyword", "") for k in q["open_keywords"]))
    return "\n".join(o) + "\n"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("id", nargs="?", type=int)
    ap.add_argument("--najdi", help="kód kurzu v názvu nahraného souboru, např. A0601")
    ap.add_argument("-o", "--vystup", required=True)
    a = ap.parse_args()
    cid = a.id or (najdi(a.najdi) if a.najdi else None)
    if not cid:
        sys.exit("Kurz nenalezen. Zadejte ID kurzu (číslo z adresy test.praktik.ujep.cz/courses/ID).")
    c = nacti(cid)
    with open(a.vystup, "w", encoding="utf-8") as f:
        f.write(export(c))
    print("ID %s, %s moduly, ulozeno: %s" % (cid, len(c.get("modules") or []), a.vystup))


if __name__ == "__main__":
    main()
