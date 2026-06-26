# Curation Method

## Scope

- Topic: stock investment and AI-driven trading research across stock prediction, asset pricing, portfolio optimization, financial time series, market microstructure, risk, sentiment/news, and algorithmic trading.
- Period: 2000-2026.
- Candidate target: up to 1,000 papers per year.
- Final selection: top 100 papers per year by citation count from the audited yearly candidate pools.

## Data Source

Metadata comes from the free public Semantic Scholar Academic Graph bulk search endpoint. No paid API, paid LLM, paid translation, or paid compute was used.

## Ranking

Records are filtered to the requested publication year, screened for explicit stock-investment and AI-trading relevance in title/abstract/venue metadata, deduplicated by DOI, arXiv, PubMed, CorpusId, paperId, and normalized title, then ranked by citation count. Influential citation count and a deterministic metadata importance score are retained as audit fields.

## Enrichment

Taxonomy, key ideas, strengths, limitations, method tags, and keyword convention tags are generated with deterministic rules from public metadata. This repository is a metadata-driven citation map, not a full-text PDF systematic review.

## GitHub-Awesome Skill2 and Paper-Curation Provenance

This regeneration follows `github-awesome-skill2` in metadata-adapter mode for a large citation-ranked awesome repository. The workflow inspected the local `jehyunlee/paper-curation` checkout and is configured for Zotero-free folder-source PDF staging under `E:\조선대\연구\paper-curation\paper\awesome-trade`. Full PDF LLM review stages from paper-curation were not run because they require separate explicit approval for paid or metered APIs.
