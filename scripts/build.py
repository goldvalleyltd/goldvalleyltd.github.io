#!/usr/bin/env python3
"""Static site compiler for goldvalleyltd.github.io (Plan B, Phase 2).

Reads Markdown guides from content/guides/, renders them through templates/,
and generates: index.html, tools/index.html, guides/<slug>/index.html,
sitemap.xml. Run from the repo root:

    ~/workspace/tools/ghpages-venv/bin/python scripts/build.py

Requires: markdown, pyyaml (installed in ~/workspace/tools/ghpages-venv).
Generated HTML is committed to main; GitHub Pages serves the repo root.

Quality gates (build fails on violation):
- every guide must carry frontmatter: title, slug, description, date,
  tool (lab URL), tool_name
- no unconfirmed claims in guide bodies (3000 sqm, 20+ years, Disney FAMA,
  ISO 9001, NBCUniversal) and no forbidden material wording (8.9 g/cm3 for
  brass, "pure brass", "eco-friendly zinc alloy")
- outbound links to the main site must use https://www.goldvalleyltd.com/

Never touches google*.html (GSC verification) or robots.txt.
"""
import io
import re
import sys
from datetime import date
from pathlib import Path

import markdown
import yaml

ROOT = Path(__file__).resolve().parent.parent
CONTENT = ROOT / "content" / "guides"
TEMPLATES = ROOT / "templates"
SITE = "https://goldvalleyltd.github.io"
MAIN_SITE = "https://www.goldvalleyltd.com"

GSC_META = ('<meta name="google-site-verification" '
            'content="7lYSJzwFEwVVvmBxMrC_s2HmvsHmRAUf4DjqhZ7b164" />')

# Strings that must never appear in published guide copy (unconfirmed claims
# or forbidden material wording). Checked against the rendered page text.
FORBIDDEN = [
    "3000", "Disney", "FAMA", "ISO 9001", "NBCUniversal",
    "20+ years", "20 years", "8.9 g/cm", "pure brass",
    "eco-friendly zinc", "eco-friendly brass",
]

TOOLS = [
    {
        "name": "Challenge Coin & Medal Weight Lab",
        "url": SITE + "/medal-coin-weight-lab/",
        "blurb": ("Estimate net metal weight, volume and DFM rating for "
                  "challenge coins and finisher medals from diameter, "
                  "thickness, relief and alloy — with a live 3D preview."),
    },
    {
        "name": "Wine Stopper Physics Lab",
        "url": SITE + "/winestopper-physics-lab/",
        "blurb": ("Check bore fit, centre of gravity, tip-over safety and "
                  "mass for metal wine stoppers — with a live 3D preview."),
    },
]


def slugify(text):
    text = text.strip().lower()
    text = re.sub(r"[^a-z0-9 _-]+", "", text)
    return re.sub(r"\s+", "-", text)


def load_template(name):
    return io.open(TEMPLATES / name, encoding="utf-8").read()


def render_template(tpl, **kw):
    from string import Template
    return Template(tpl).substitute(**kw)


def parse_guide(path):
    text = io.open(path, encoding="utf-8").read()
    m = re.match(r"^---\n(.*?)\n---\n(.*)$", text, re.S)
    if not m:
        sys.exit(f"ERROR: {path.name} has no YAML frontmatter block")
    meta = yaml.safe_load(m.group(1))
    body = m.group(2)
    for key in ("title", "slug", "description", "date", "tool", "tool_name"):
        if not meta.get(key):
            sys.exit(f"ERROR: {path.name} frontmatter missing '{key}'")
    # Drop a leading H1 if it duplicates the frontmatter title.
    body = re.sub(r"^# .+\n+", "", body, count=1)
    # Strip HTML comments (FACT-CHECK audit notes stay in the .md source,
    # never in the published page).
    body = re.sub(r"<!--.*?-->", "", body, flags=re.S)
    return meta, body


def build_toc(body):
    items = []
    for line in body.splitlines():
        if line.startswith("## "):
            heading = line[3:].strip()
            items.append((slugify(heading), heading))
    if not items:
        return ""
    links = "".join(
        f'<li><a href="#{slug}">{heading}</a></li>' for slug, heading in items)
    return f'<nav class="toc"><p>Contents</p><ul>{links}</ul></nav>'


def check_body(path, html):
    text = re.sub(r"<[^>]+>", " ", html)
    for bad in FORBIDDEN:
        if bad.lower() in text.lower():
            sys.exit(f"ERROR: forbidden string {bad!r} in {path.name}")
    for url in re.findall(r'href="(https?://[^"]+)"', html):
        if "goldvalleyltd.com" in url and not url.startswith(MAIN_SITE):
            sys.exit(f"ERROR: main-site link must use {MAIN_SITE}: {url}")


def json_ld_article(meta, url):
    return ('{"@context":"https://schema.org","@type":"TechArticle",'
            f'"headline":{json_str(meta["title"])},'
            f'"description":{json_str(meta["description"])},'
            f'"datePublished":"{meta["date"]}","author":{{"@type":'
            '"Organization","name":"GoldValley Ltd"},"publisher":{"@type":'
            '"Organization","name":"GoldValley Ltd"},'
            f'"mainEntityOfPage":"{url}"}}')


def json_str(s):
    import json
    return json.dumps(str(s))


def write(path, content):
    path.parent.mkdir(parents=True, exist_ok=True)
    io.open(path, "w", encoding="utf-8").write(content)
    print(f"wrote {path.relative_to(ROOT)}")


def main():
    base = load_template("base.html")
    guide_tpl = load_template("guide.html")
    home_tpl = load_template("home.html")
    tools_tpl = load_template("tools.html")

    guides = []
    for path in sorted(CONTENT.glob("*.md")):
        meta, body = parse_guide(path)
        html = markdown.markdown(
            body, extensions=["extra", "toc", "sane_lists"],
            extension_configs={"toc": {"toc_depth": "2-3"}})
        check_body(path, html)
        url = f"{SITE}/guides/{meta['slug']}/"
        page = render_template(
            guide_tpl,
            title=meta["title"],
            date=str(meta["date"]),
            description=meta["description"],
            toc=build_toc(body),
            tool_url=meta["tool"],
            tool_name=meta["tool_name"],
            content=html,
            guide_url=url,
        )
        full = render_template(
            base, title=meta["title"], description=meta["description"],
            canonical=url, og_type="article", body=page,
            json_ld=json_ld_article(meta, url), gsc_meta=GSC_META,
        )
        write(ROOT / "guides" / meta["slug"] / "index.html", full)
        guides.append((meta, url))

    guides.sort(key=lambda g: str(g[0]["date"]), reverse=True)
    cards = "".join(
        f'<a class="card" href="{url}"><h2>{m["title"]}</h2>'
        f'<p>{m["description"]}</p><span>{m["date"]}</span></a>'
        for m, url in guides)
    tool_cards = "".join(
        f'<a class="card" href="{t["url"]}"><h2>{t["name"]}</h2>'
        f'<p>{t["blurb"]}</p></a>' for t in TOOLS)

    home_body = render_template(home_tpl, tool_cards=tool_cards,
                                guide_cards=cards)
    home = render_template(
        base, title="GoldValley Engineering Lab — Interactive DFM Tools "
                   "for Custom Metal Products",
        description=("Free interactive engineering tools and whitepapers "
                     "from GoldValley: challenge coin and medal weight "
                     "estimation, wine stopper physics, and DFM guides."),
        canonical=SITE + "/", og_type="website", body=home_body,
        json_ld=('{"@context":"https://schema.org","@type":"WebSite",'
                 '"name":"GoldValley Engineering Lab",'
                 f'"url":"{SITE}/"}}'),
        gsc_meta=GSC_META)
    write(ROOT / "index.html", home)

    tools_body = render_template(tools_tpl, tool_cards=tool_cards)
    tools = render_template(
        base, title="Interactive Tools — GoldValley Engineering Lab",
        description=("Free interactive DFM tools: challenge coin and medal "
                     "weight lab, wine stopper physics lab."),
        canonical=SITE + "/tools/", og_type="website", body=tools_body,
        json_ld=('{"@context":"https://schema.org","@type":"WebPage",'
                 '"name":"Interactive Tools — GoldValley Engineering Lab",'
                 f'"url":"{SITE}/tools/"}}'),
        gsc_meta=GSC_META)
    write(ROOT / "tools" / "index.html", tools)

    today = date.today().isoformat()
    urls = [(SITE + "/", today, "1.0"),
            (SITE + "/tools/", today, "0.8")]
    for t in TOOLS:
        urls.append((t["url"], today, "0.8"))
    for m, url in guides:
        urls.append((url, str(m["date"]), "0.8"))
    sm = ['<?xml version="1.0" encoding="UTF-8"?>',
          '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    for loc, lastmod, prio in urls:
        sm.append(f"  <url><loc>{loc}</loc><lastmod>{lastmod}</lastmod>"
                  f"<priority>{prio}</priority></url>")
    sm.append("</urlset>")
    write(ROOT / "sitemap.xml", "\n".join(sm) + "\n")
    print(f"OK: {len(guides)} guide(s), sitemap has {len(urls)} URLs")


if __name__ == "__main__":
    main()
