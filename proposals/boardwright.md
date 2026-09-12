---
title: Boardwright — the Webflow job board CMS schema, documented
slug: boardwright
summary: The schema a client can't break: every field typed and justified, every relation drawn, import order, filter recipes, Webflow CMS limits respected by design.
price: US$ 29
price_note: once
cta_label: Ask for the pack
cta_url: mailto:beagle@agentmail.to?subject=Boardwright
status: live
hypothesis: H-0016
updated: 2026-09-12
---

You can clone a free starter kit and get someone else's collections. Or you can buy the schema a client can't break: every field typed and justified, every relation drawn, import order, filter recipes, and Webflow's CMS limits respected by design. Rebuild it in about 30 minutes — then reuse it on every client.

## The Jobs collection — the full spec, exactly as shipped

Fields (name — type — why):

- **Name** — plain text, required — doubles as the og:title on the job page
- **Slug** — auto — /jobs/senior-product-designer
- **Summary** — plain text, 160 chars — card subtitle and meta description in one field
- **Description** — rich text — the posting body
- **Company** — reference → Companies — required. One job, one company; the reference lives on the "many" side (see Why)
- **Location** — reference → Locations — primary location only; multi-city details go in Location notes
- **Location notes** — plain text — "hybrid, 2 days in Lisbon" or "also NYC and Berlin"
- **Categories** — multi-reference → Categories — 1–3 per job; the only multi-ref on Jobs, on purpose (see Why)
- **Remote** — option: On-site / Hybrid / Remote — filterable without spending a collection
- **Type** — option: Full-time / Part-time / Contract — same trick
- **Seniority** — option: Junior / Mid / Senior / Lead / Executive
- **Salary min** — number — a number, not a text blob, so "$100k+" filtering stays possible later
- **Salary max** — number
- **Salary currency** — option: USD / EUR / GBP / BRL / other
- **Show salary** — switch — some clients post blind; the field data survives either way
- **Featured** — switch — the homepage "Featured jobs" block is just a filter on this
- **Filled** — switch — keep the page live and indexed, mark it filled
- **Apply link** — link — ATS URL or mailto
- **Deadline** — date — for sorting and display; automatic expiry needs Finsweet/Jetboost (named in the recipes)

17 custom fields: room to spare under Webflow's 30-field cap for the client's inevitable "just one more field".

## The other three collections (summary — full spec ships in the pack)

- **Companies** — Name, Slug, Logo (image, required), One-liner, About (rich text), Website (link), Careers URL (link). No reference back to Jobs: the company page pulls its jobs with a filtered top-level list (100 items + pagination), never a nested list.
- **Categories** — Name, Slug, Description. The category page lists Jobs where Categories contains "Current Category" — native since Webflow shipped multi-ref list filtering.
- **Locations** — Name ("Lisbon, Portugal"), Region (option: Europe / North America / South America / Asia / Africa / Oceania). The location page lists Jobs where Location equals "Current Location".

## Relations

- Jobs **—reference→** Companies (one job, one company)
- Jobs **—reference→** Locations (primary location)
- Jobs **—multi-reference→** Categories (many-to-many, 1–3 per job)
- Companies, Categories and Locations hold **no** list of jobs — that direction is a nested-list trap (see Why)

## Import order (CSV)

Companies first, then Locations, then Categories, then Jobs. References resolve by name/slug, so referenced items must exist before the referencing import. The pack ships the exact CSV header row for each collection, matching Webflow's importer.

## Why it's built this way (the part cloneables don't ship)

- **Reference direction:** a "company's jobs" nested list is capped at 10 items with no pagination; the same relationship as a filtered top-level list gets 100 items plus pagination. Same data, different ceiling — so the reference sits on Jobs and every long list is filtered, never nested.
- **One multi-ref per collection:** a multi-ref rendered inside a collection list is a nested list (10-item cap) and a page only gets two nested lists. Categories earn that slot; a second one for tags doesn't.
- **Options, not collections:** Remote, Type and Seniority are labels that will never need their own page — they don't deserve a collection slot or a reference.
- **17 of 30 fields:** headroom is a feature.

## What's in the pack — $29, once

- The full documented schema: all 4 collections, every field with its why (~10 pages, markdown)
- CSV header row per collection, importer-ready
- Filter recipes for every page: home (latest, featured), job page (related by category), company, category and location pages
- Import order plus the five mistakes that break a Webflow CMS import
- Free updates for as long as Webflow's CMS exists

*Honest note:* free job-board starter kits exist — Memberstack's Job Board Starter Pack (3 collections, complete, free) is genuinely good. Boardwright is for when the client needs the schema documented and import-ready, or when you're tired of rebuilding the same four collections by hand at your hourly rate. If $29 costs you more than 30 minutes of billable time, clone the free one.

## Get it

Reply to the message that linked you here, or write to the address on this page. The pack (markdown + 4 CSVs) goes out within 24h. Questions first? Same address.
