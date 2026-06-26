import csv
import re
from pathlib import Path

import build_awesome_trade as build


ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = ROOT / "data"
AUDIT_CSV = DATA_DIR / f"relevance_audit_selected_{build.YEAR_FILE_STEM}.csv"
REMOVED_CSV = DATA_DIR / f"relevance_removed_{build.YEAR_FILE_STEM}.csv"


def row_text(row):
    return " ".join(row.get(key) or "" for key in ("title", "abstract", "venue"))


def matched_evidence(row):
    title = row.get("title") or ""
    text = row_text(row)
    matches = []
    for pattern in getattr(build, "TITLE_RELEVANCE_PATTERNS", build.AI_RELEVANCE_PATTERNS):
        match = re.search(pattern, title, re.I)
        if match:
            matches.append(f"title:{match.group(0)}")
    for pattern in build.AI_RELEVANCE_PATTERNS:
        match = re.search(pattern, text, re.I)
        if match:
            matches.append(f"text:{match.group(0)}")
    deduped = []
    for match in matches:
        normalized = match.lower()
        if normalized not in {item.lower() for item in deduped}:
            deduped.append(match)
    return "; ".join(deduped[:8])


def rank_value(row):
    return row.get("rank") or row.get("\ufeffrank") or ""


def audit_rows():
    source = DATA_DIR / build.PAPERS_CSV
    with source.open(encoding="utf-8-sig", newline="") as handle:
        for row in csv.DictReader(handle):
            keep = build.is_relevant(row)
            evidence = matched_evidence(row)
            yield {
                "originalRank": rank_value(row),
                "yearRank": row.get("yearRank", ""),
                "candidateRank": row.get("candidateRank", ""),
                "year": row.get("year", ""),
                "title": row.get("title", ""),
                "venue": row.get("venue", ""),
                "citationCount": row.get("citationCount", ""),
                "category": row.get("category", ""),
                "keywordTags": row.get("keywordTags", ""),
                "verdict": "keep" if keep else "remove",
                "evidence": evidence if keep else "no stock-investment, trading, portfolio, market-microstructure, or financial-time-series evidence in title/abstract/venue",
                "sourceQueries": row.get("sourceQueries", ""),
                "semanticScholarUrl": row.get("semanticScholarUrl", ""),
                "url": row.get("url", ""),
                "abstractSnippet": (row.get("abstract", "") or "")[:500],
            }


def write_csv(path, rows):
    rows = list(rows)
    fields = [
        "originalRank",
        "yearRank",
        "candidateRank",
        "year",
        "title",
        "venue",
        "citationCount",
        "category",
        "keywordTags",
        "verdict",
        "evidence",
        "sourceQueries",
        "semanticScholarUrl",
        "url",
        "abstractSnippet",
    ]
    with path.open("w", encoding="utf-8-sig", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)


def main():
    audited = list(audit_rows())
    removed = [row for row in audited if row["verdict"] == "remove"]
    write_csv(AUDIT_CSV, audited)
    write_csv(REMOVED_CSV, removed)
    print(f"audited={len(audited)}")
    print(f"keep={len(audited) - len(removed)}")
    print(f"remove={len(removed)}")
    print(f"audit_csv={AUDIT_CSV}")
    print(f"removed_csv={REMOVED_CSV}")


if __name__ == "__main__":
    main()
