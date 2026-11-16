# goldvalleyltd.github.io

GoldValley Engineering Lab — the org's GitHub Pages home: the lab homepage,
the interactive-tool index, the `/guides/` whitepapers, `robots.txt`,
`sitemap.xml`, and the Google Search Console verification file.

## How the site is built (Plan B — Python static compiler)

- Guides live as Markdown with YAML frontmatter in `content/guides/`.
- `scripts/build.py` renders them through `templates/` into static HTML
  (`index.html`, `tools/`, `guides/<slug>/`) and regenerates `sitemap.xml`.
- Build with the persistent venv (has `markdown` + `pyyaml`):

```bash
~/workspace/tools/ghpages-venv/bin/python scripts/build.py
```

- The build enforces quality gates and fails on violation: missing
  frontmatter, unconfirmed claims (3000 sqm, 20+ years, Disney FAMA,
  ISO 9001, NBCUniversal), forbidden material wording (8.9 g/cm³ for brass,
  "pure brass", "eco-friendly zinc alloy"), or main-site links not using
  `https://www.goldvalleyltd.com/`.
- Generated HTML is committed to `main`; GitHub Pages serves the repo root.
- To add a guide: write `content/guides/<slug>.md`, run the build, verify
  locally, commit + push. The homepage guide index and sitemap update
  automatically.

> **Do not remove the GSC verification file (`google*.html`) or the meta tag**
> (in `templates/base.html`, rendered onto every page) — they keep the
> Search Console property verified. The build never touches `google*.html`
> or `robots.txt`.
