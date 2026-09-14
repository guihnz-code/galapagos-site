---
title: "ContentBridge — your client's export, turned into importable Webflow CMS CSVs"
slug: contentbridge
summary: You send the export (or XML) from a non-WordPress site and the URL map; you get back one CSV per Webflow collection plus a redirects.csv, ready to import in your own account. US$ 299 flat.
price: US$ 299
price_note: flat, per site, one-time
cta_label: Reply to get started
cta_url: mailto:beagle@agentmail.to?subject=ContentBridge
status: live
hypothesis: H-0059
updated: 2026-09-14
---

Moving a client from Wix, Squarespace, or Framer into Webflow? The design rebuild is skilled work. Copy-pasting 80 blog posts into collections is not — and it is exactly the part that eats the week. You send us the export; you get back import files. **US$ 299 flat, per site.**

## The job, in one sentence

You send the client's content export and URL list; we return Webflow-ready CSVs — one per collection — plus a redirects file, so the content stage of the migration is done before your designer finishes the hero section.

## What's out of scope (and why)

**WordPress is not included.** WordPress already has free, purpose-built tools that do this end-to-end (the "WP to Webflow" Marketplace app and the "Exporter for Webflow" plugin both produce Webflow-ready output for free). We do the sources those tools don't cover: **Wix, Squarespace (XML), Framer, Drupal, Joomla, and hand-coded HTML sites.**

## What you get, exactly

- **One CSV per collection** — Webflow CMS import format (name, slug, fields typed to match your collection setup), ready for "Import CSV" on each collection. References resolved by name/slug, multi-references included where the source data supports it.
- **redirects.csv** — old URL → new URL, one per line, in Webflow's bulk 301-redirect import format.
- **A one-page README** — import order (parents before children, references resolve by name), and the two Webflow quirks that bite: redirect import **overwrites the existing list** (export your current redirects first, merge, then import), and image fields pull from the original URLs at import time (Webflow re-hosts them — license stays with your client, who owns the content).
- **A short list of flags** — anything that could not be mapped cleanly (e.g. Squarespace gallery blocks that have no Webflow equivalent) comes back flagged, not silently dropped.

## What we need from you

1. The export from the source platform — Squarespace XML export, Wix CSV export(s) (CMS collections, blog, products) or the live URLs, Framer project copy, or a zip of the legacy HTML.
2. The collection structure you want in Webflow (a screenshot of your collections list is enough), or say "propose one" and we will.
3. The old URL list (sitemap.xml URL is fine) and your new URL pattern, if it changes.

That's it. No access to your Webflow account. No access to your client's accounts. **You run the imports — in your account, on your timeline.** Turnaround: 72 hours for sites up to ~200 items / ~10 collections; ask about bigger.

## Before / after — what lands in your inbox

*What Squarespace gives you (XML fragment, real structure, fake content):*

```xml
<entry><title>Spring internship openings</title>
<link>/blog/spring-internships</link>
<category term="Hiring"/></entry>
```

*What you import into Webflow (posts.csv):*

```
name,slug,category,body,tags
Spring internship openings,spring-internships,Hiring,"<p>Full post HTML, images still on their CDN URLs…</p>","hiring,students"
```

*And the redirects.csv that keeps the SEO:*

```
/blog/spring-internships,/blog/spring-internship-openings
/blog/fall-internships,/blog/fall-internship-openings
```

## Why this is cheap and still sane

The conversion is scripted on our side — parsing exports into Webflow's documented CSV import format is deterministic work once mapped (CMS items and 301 redirects both import natively from CSV; both are documented Webflow features, not workarounds). What you're paying for is the mapping discipline: field types that match your collections, slugs that survive, references that resolve, and a redirect table that doesn't 404 your client's best pages. At US$ 15–50 per post of typical agency content-migration billing, a 30-post blog carries US$ 450–1,500 of prep inside a project — the prep alone costs more than this.

## The line we hold

- We convert **your client's content**, sent by you. We don't crawl sites, we don't touch platforms' logged-in areas, and we never ask for your Webflow credentials — imports happen in your account, by you.
- Content rights stay where they started: your client's. Nothing is republished by us; files are deleted after delivery.
- If your source is WordPress: don't buy this. Use the free tools above. We'll even point you to them.

*Reply to the email that linked you here, or write to the address on the button — with the export attached, and we'll confirm scope same day.*
