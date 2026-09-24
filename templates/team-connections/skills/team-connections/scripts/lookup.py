#!/usr/bin/env python3
"""Warm-path lookup across a team's LinkedIn connection exports.

Reads every connections_<name>.csv in --dir (LinkedIn's standard export, with or
without its "Notes:" preamble), optionally overlays an enriched dataset keyed by
LinkedIn URL, and prints JSON matches for each --company / --person target plus a
title-keyword scan. Standard library only; Python 3.8+.

Examples:
  lookup.py --dir ~/.claude/skill-data/team-connections/connections --company "Acme Corp"
  lookup.py --dir ... --company Acme --company Globex --keywords "head of ai,chief ai"
  lookup.py --dir ... --person "Jane Smith"
"""
import argparse
import csv
import glob
import json
import os
import re
import sys
from datetime import date, datetime

SUFFIXES = {"inc", "llc", "ltd", "corp", "corporation", "co", "company", "plc", "gmbh",
            "the", "group", "holdings", "lp", "llp", "sa", "ag"}


def norm_company(s):
    words = re.sub(r"[^a-z0-9 ]+", " ", (s or "").lower()).split()
    return " ".join(w for w in words if w not in SUFFIXES)


def company_matches(target, company):
    t, c = norm_company(target), norm_company(company)
    if not t or not c:
        return False
    if len(t) < 3:
        return t == c
    return re.search(r"\b" + re.escape(t) + r"\b", c) is not None or (
        len(c) >= 3 and re.search(r"\b" + re.escape(c) + r"\b", t) is not None)


def norm_url(u):
    u = (u or "").strip().lower().rstrip("/")
    return re.sub(r"^https?://(www\.)?", "", u)


def parse_date(s):
    for fmt in ("%d %b %Y", "%Y-%m-%d", "%m/%d/%Y", "%d-%b-%y"):
        try:
            return datetime.strptime((s or "").strip()[:11].strip(), fmt).date()
        except ValueError:
            pass
    try:
        return datetime.fromisoformat((s or "").strip()[:19]).date()
    except ValueError:
        return None


def read_linkedin_csv(path):
    with open(path, newline="", encoding="utf-8-sig", errors="replace") as f:
        lines = f.read().splitlines()
    start = next((i for i, l in enumerate(lines) if l.startswith("First Name")), None)
    if start is None:
        return []
    return list(csv.DictReader(lines[start:]))


def load_people(csv_dir):
    people, contributors = {}, []
    for path in sorted(glob.glob(os.path.join(os.path.expanduser(csv_dir), "connections_*.csv"))):
        who = os.path.basename(path)[len("connections_"):-len(".csv")]
        rows = read_linkedin_csv(path)
        contributors.append({"contributor": who, "rows": len(rows)})
        for r in rows:
            name = f"{r.get('First Name', '').strip()} {r.get('Last Name', '').strip()}".strip()
            url = (r.get("URL") or "").strip().rstrip("/")
            key = norm_url(url) or name.lower()
            if not key:
                continue
            p = people.setdefault(key, {"name": name, "url": url, "company": r.get("Company", ""),
                                        "title": r.get("Position", ""), "via": []})
            connected = parse_date(r.get("Connected On", ""))
            p["via"].append({"contributor": who,
                             "connected_on": connected.isoformat() if connected else None})
    return people, contributors


def overlay_enriched(people, path):
    if not path or not os.path.exists(os.path.expanduser(path)):
        return None
    with open(os.path.expanduser(path), newline="", encoding="utf-8", errors="replace") as f:
        rows = list(csv.DictReader(f))
    for r in rows:
        key = norm_url(r.get("linkedin_profile_url") or r.get("url"))
        if key in people:
            people[key]["enriched"] = {k: r.get(k) for k in
                                       ("current_title", "current_company", "confidence", "resolved_at")}
    return {"rows": len(rows), "resolved": sum(1 for r in rows if r.get("resolved_at"))}


def freshness(enriched, fresh_days_high, fresh_days_other):
    if not enriched or not enriched.get("resolved_at"):
        return "unresolved"
    d = parse_date(enriched["resolved_at"])
    if not d or (enriched.get("confidence") or "").lower() == "low":
        return "stale"
    limit = fresh_days_high if (enriched.get("confidence") or "").lower() == "high" else fresh_days_other
    return "fresh" if (date.today() - d).days <= limit else "stale"


def describe(p, args):
    e = p.get("enriched")
    out = {"name": p["name"], "url": p["url"], "export_title": p["title"],
           "export_company": p["company"], "via": sorted(p["via"], key=lambda v: v["connected_on"] or "9999")}
    if e:
        out.update(current_title=e.get("current_title"), current_company=e.get("current_company"),
                   confidence=e.get("confidence"), resolved_at=e.get("resolved_at"),
                   freshness=freshness(e, args.fresh_days_high, args.fresh_days))
    oldest = out["via"][0]["connected_on"]
    if oldest:
        out["years_connected"] = round((date.today() - date.fromisoformat(oldest)).days / 365.25, 1)
    return out


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--dir", required=True, help="folder holding connections_<name>.csv files")
    ap.add_argument("--company", action="append", default=[])
    ap.add_argument("--person", action="append", default=[])
    ap.add_argument("--keywords", default="", help="comma-separated title keywords to scan everyone for")
    ap.add_argument("--enriched", default="", help="optional enriched CSV keyed by linkedin_profile_url")
    ap.add_argument("--fresh-days", type=int, default=90)
    ap.add_argument("--fresh-days-high", type=int, default=180)
    args = ap.parse_args()

    people, contributors = load_people(args.dir)
    if not contributors:
        sys.exit(f"No connections_*.csv files found in {args.dir}")
    enriched_meta = overlay_enriched(people, args.enriched)

    result = {"contributors": contributors, "enriched": enriched_meta, "companies": {}, "people": {},
              "keyword_hits": []}
    matched_urls = set()

    for target in args.company:
        hits = []
        for p in people.values():
            cur = (p.get("enriched") or {}).get("current_company")
            now_there = company_matches(target, cur) if cur else company_matches(target, p["company"])
            was_there = bool(cur) and company_matches(target, p["company"]) and not now_there
            if now_there or was_there:
                d = describe(p, args)
                d["status"] = "current" if now_there else "moved_on"
                hits.append(d)
                matched_urls.add(p["url"])
        hits.sort(key=lambda h: (h["status"] != "current", -(h.get("years_connected") or 0)))
        result["companies"][target] = hits

    for target in args.person:
        toks = target.lower().split()
        result["people"][target] = [describe(p, args) for p in people.values()
                                    if all(t in p["name"].lower() for t in toks)]

    kws = [k.strip().lower() for k in args.keywords.split(",") if k.strip()]
    if kws:
        for p in people.values():
            title = ((p.get("enriched") or {}).get("current_title") or p["title"]).lower()
            if p["url"] not in matched_urls and any(k in title for k in kws):
                result["keyword_hits"].append(describe(p, args))

    json.dump(result, sys.stdout, indent=1)
    print()


if __name__ == "__main__":
    main()
