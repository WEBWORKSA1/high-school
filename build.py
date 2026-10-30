#!/usr/bin/env python3
"""Build the High.School static site.

    python3 build.py

Generates every page into the repo root (GitHub Pages serves main / root),
plus sitemap.xml, robots.txt, ads.txt, search-index.json and the web manifest.
Edit content in src/*.py, then rebuild and commit.
"""
import json, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "src"))

import kit, subjects, testprep, tools, college, guides, core, community, legal  # noqa: E402


def write(name, text):
    with open(os.path.join(HERE, name), "w", encoding="utf-8") as f:
        f.write(text)


def main():
    for mod in (core, subjects, testprep, tools, college, guides, community, legal):
        mod.build()

    pages = sorted(kit.PAGES, key=lambda p: (p["u"].count("/"), p["u"]))
    today = kit.TODAY.isoformat()
    urls = "\n".join(
        f"  <url><loc>{p['loc']}</loc><lastmod>{today}</lastmod><changefreq>{'weekly' if p['u'] in ('', 'tools/', 'study/') else 'monthly'}</changefreq><priority>{'1.0' if p['u'] == '' else ('0.9' if p['u'].startswith('tools/') or p['u'] == 'get-matched/' else '0.7')}</priority></url>"
        for p in pages)
    write("sitemap.xml", f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n{urls}\n</urlset>\n')
    write("robots.txt", f"User-agent: *\nAllow: /\nDisallow: /thank-you/\nDisallow: /search/\n\nSitemap: {kit.BASE_URL}/sitemap.xml\n")
    write("ads.txt", "google.com, pub-6620975821265271, DIRECT, f08c47fec0942fa0\n")
    write("search-index.json", json.dumps([{k: p[k] for k in ("u", "t", "d", "k")} for p in pages], ensure_ascii=False))
    write(".nojekyll", "")
    write("manifest.webmanifest", json.dumps({
        "name": "High.School", "short_name": "High.School", "start_url": "./", "display": "standalone",
        "background_color": "#fbfaf5", "theme_color": "#14213d",
        "icons": [{"src": "assets/img/icon-192.png", "sizes": "192x192", "type": "image/png"},
                  {"src": "assets/img/icon-512.png", "sizes": "512x512", "type": "image/png"}]}, indent=2))
    print(f"Built {len(pages)} indexed pages (+ search, thank-you, 404).")


if __name__ == "__main__":
    main()
