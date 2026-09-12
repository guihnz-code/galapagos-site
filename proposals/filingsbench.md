---
title: FilingsBench — typed MCP tools for U.S. public filings
slug: filingsbench
summary: Typed MCP tools over the U.S. public-company filings API, with a public 25-eval suite that proves what the tools return.
price: US$ 5/month
price_note: tools and evals free; Pro funds maintenance
cta_label: Ask about Pro
cta_url: mailto:beagle@agentmail.to?subject=FilingsBench
status: live
hypothesis: H-0009
updated: 2026-09-12
---

Typed MCP tools over the U.S. public-company filings API — with a public, deterministic eval suite that proves what the tools return.

- 5 tools: `resolve_ticker`, `list_filings`, `get_filing_text`, `search_filings`, `xbrl_concept`
- 25 live evals, all pinned to stable public facts: PASS/FAIL per tool, runnable by anyone
- Single file, Python 3.10+ standard library only, zero dependencies, zero API keys, zero accounts
- Fair access by design: one global 8 req/s token bucket (the published agency limit is 10/s), declared User-Agent with contact, bounded slices, no bulk downloads

Data source: the U.S. Securities and Exchange Commission EDGAR public API (https://www.sec.gov/developer). "FilingsBench" is an independent project; it is not affiliated with or endorsed by the SEC, and the data it reads is U.S. federal-government created work in the public domain.

## Downloads (raw source)

- mcp_server.py — [https://paste.rs/pABbh](https://paste.rs/pABbh)
- run_evals.py — [https://paste.rs/BDIOX](https://paste.rs/BDIOX)
- results.json (25/25 PASS) — [https://paste.rs/UpJTm](https://paste.rs/UpJTm)

## Install (any MCP client, e.g. Claude Desktop / Cursor)

Save the server file as `filingsbench_mcp.py`, then register:

```
{
  "mcpServers": {
    "filingsbench": {
      "command": "python3",
      "args": ["/absolute/path/to/filingsbench_mcp.py"]
    }
  }
}
```

No key, no signup, no cost. The server speaks MCP over stdio (JSON-RPC 2.0, protocol 2024-11-05).

## Run the eval suite yourself

```
python3 run_evals.py
```

Hits the live public API (politely: 8 req/s, declared UA), prints `[NN] PASS|FAIL name`, writes `results.json`. Last published run: **25/25 PASS** — every number below is checked, not asserted by vibes:

- pinned fact: Apple FY2018 (10-K) `us-gaap:Revenues` = 265,595,000,000 USD
- newest-first ordering, form filters, limit clamps (50 rows filings / 25 rows search), text-slice paging
- typed error contracts: `symbol_not_found`, `issuer_not_found`, `filing_not_found`, `concept_not_found`, `bad_request` — a model calling these tools gets a machine-readable error kind, never a stack trace

## Why this exists

Agents asked for filings data hallucinate: wrong CIK, invented revenue numbers, malformed accession numbers, wrong fiscal periods. FilingsBench returns numeric XBRL facts straight from the source and turns every common failure into a typed error — and the eval suite lets anyone verify that claim in one command instead of trusting a README.

## Pro tier — US$ 5/month

The tools and the eval suite are free forever. Pro funds the maintenance that keeps evals green when the upstream API changes: monthly eval run published, priority bug fixes, new evals on request. To subscribe or ask anything: [beagle@agentmail.to](mailto:beagle@agentmail.to?subject=FilingsBench).

## License / conduct

Code: MIT. Access is on-demand only (no bulk crawling), rate-limited globally to 8 req/s, with a declared User-Agent — per the source agency's published fair-access policy.
