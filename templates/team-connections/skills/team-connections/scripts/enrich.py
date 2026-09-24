#!/usr/bin/env python3
"""Maintain the enriched dataset that lookup.py overlays: current title/company per person.

Subcommands (all paths default to ~/.claude/skill-data/team-connections/):
  ingest      Build/refresh enriched.csv from connections_*.csv. Keeps existing enrichment.
              --seed CSV imports enrichment from an older dataset with the same columns.
  status      Counts: usable (high+medium, fresh), stale, low, never attempted.
  queue       Write the next N rows to research as JSONL (pending.jsonl).
              --company X prioritizes people whose export company matches X.
  perplexity  Resolve a queue file via the Perplexity API (needs PERPLEXITY_API_KEY).
              Rate-limited, writes raw results to a results file; does not touch the CSV.
  merge       Fold a results JSONL into enriched.csv (backup first, validated, overrides win).

Standard library only; Python 3.8+.
"""
import argparse
import csv
import json
import os
import re
import shutil
import sys
import time
import urllib.request
from datetime import date, datetime

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lookup import company_matches, freshness, norm_url, read_linkedin_csv  # noqa: E402

HOME = os.path.expanduser("~/.claude/skill-data/team-connections")
COLS = ["linkedin_profile_url", "full_name", "export_title", "export_company", "contributors",
        "current_title", "current_company", "confidence", "resolved_at", "notes"]
CONFIDENCE = {"high", "medium", "low"}
CONTROL = re.compile(r"[\x00-\x08\x0b\x0c\x0e-\x1f\ufffd]")


def clean(v, limit=200):
    return CONTROL.sub("", str(v or "")).strip()[:limit]


def load(path):
    if not os.path.exists(path):
        return {}
    with open(path, newline="", encoding="utf-8", errors="replace") as f:
        return {norm_url(r.get("linkedin_profile_url")) or r.get("full_name", "").lower(): r
                for r in csv.DictReader(f)}


def save(path, rows):
    tmp = path + ".tmp"
    with open(tmp, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=COLS, extrasaction="ignore")
        w.writeheader()
        for r in rows.values():
            w.writerow({c: r.get(c, "") for c in COLS})
    os.replace(tmp, path)


def backup(path):
    if os.path.exists(path):
        os.makedirs(os.path.join(os.path.dirname(path), "backups"), exist_ok=True)
        dst = os.path.join(os.path.dirname(path), "backups",
                           f"enriched-{datetime.now():%Y%m%d-%H%M%S}.csv")
        shutil.copy2(path, dst)
        return dst


def apply_overrides(rows, path):
    if not os.path.exists(path):
        return 0
    n = 0
    for o in json.load(open(path)).get("overrides", []):
        m = o.get("match", {})
        for key, r in rows.items():
            hit = (m.get("linkedin_url") and norm_url(m["linkedin_url"]) == key) or (
                m.get("full_name") and m["full_name"].lower() == r.get("full_name", "").lower()
                and (not m.get("company_hint") or company_matches(m["company_hint"], r.get("export_company"))))
            if hit:
                r.update({k: o[k] for k in ("current_title", "current_company", "confidence", "notes") if k in o})
                r["resolved_at"] = r.get("resolved_at") or date.today().isoformat()
                n += 1
    return n


def cmd_ingest(a):
    rows = load(a.enriched)
    seed = load(a.seed) if a.seed else {}
    before = len(rows)
    for path in sorted(os.listdir(a.dir)):
        if not (path.startswith("connections_") and path.endswith(".csv")):
            continue
        who = path[len("connections_"):-4]
        for r in read_linkedin_csv(os.path.join(a.dir, path)):
            name = f"{r.get('First Name', '').strip()} {r.get('Last Name', '').strip()}".strip()
            key = norm_url(r.get("URL")) or name.lower()
            if not key:
                continue
            row = rows.setdefault(key, {"linkedin_profile_url": (r.get("URL") or "").strip(),
                                        "full_name": name, "contributors": ""})
            row["export_title"], row["export_company"] = r.get("Position", ""), r.get("Company", "")
            cs = set(filter(None, row.get("contributors", "").split(";"))) | {who}
            row["contributors"] = ";".join(sorted(cs))
            if key in seed and not row.get("resolved_at"):
                for c in ("current_title", "current_company", "confidence", "resolved_at", "notes"):
                    row[c] = seed[key].get(c, "")
    n_over = apply_overrides(rows, a.overrides)
    save(a.enriched, rows)
    print(json.dumps({"rows": len(rows), "new": len(rows) - before,
                      "seeded": sum(1 for k in seed if k in rows), "overrides_applied": n_over}))


def classify(r, a):
    if not r.get("resolved_at"):
        return "never_attempted"
    if (r.get("confidence") or "").lower() == "low":
        return "low"
    return freshness(r, a.fresh_days_high, a.fresh_days)


def cmd_status(a):
    rows = load(a.enriched)
    counts = {}
    for r in rows.values():
        k = classify(r, a)
        counts[k] = counts.get(k, 0) + 1
    print(json.dumps({"rows": len(rows), **counts}))


def cmd_queue(a):
    rows = load(a.enriched)
    kws = [k.strip().lower() for k in a.keywords.split(",") if k.strip()]

    def priority(r):
        state = classify(r, a)
        target = any(company_matches(c, r.get("export_company")) for c in a.company)
        return (not target, state == "low", -len(r.get("contributors", "").split(";")),
                not any(k in (r.get("export_title") or "").lower() for k in kws))

    todo = [r for r in rows.values() if classify(r, a) != "fresh"
            and (not a.company or any(company_matches(c, r.get("export_company")) for c in a.company))]
    todo.sort(key=priority)
    with open(a.out, "w") as f:
        for r in todo[:a.limit]:
            f.write(json.dumps({"linkedin_profile_url": r["linkedin_profile_url"],
                                "full_name": r["full_name"], "company_hint": r.get("export_company", ""),
                                "title_hint": r.get("export_title", "")}) + "\n")
    print(json.dumps({"queued": min(len(todo), a.limit), "remaining_after": max(0, len(todo) - a.limit),
                      "file": a.out}))


PPLX_PROMPT = """Find the CURRENT job title and employer of this person. Anchor identity on the
LinkedIn URL if given. Prefer blank over a guess: if ambiguous or not found, return confidence
"low" with empty title/company and say why in notes (under 150 chars).
Name: {full_name}
LinkedIn: {linkedin_profile_url}
Old hint (may be outdated): {title_hint} at {company_hint}
Return ONLY JSON: {{"current_title": "", "current_company": "", "confidence": "high|medium|low", "notes": ""}}"""


def cmd_perplexity(a):
    key = os.environ.get("PERPLEXITY_API_KEY")
    if not key:
        sys.exit("PERPLEXITY_API_KEY is not set — use the web-search subagent path instead.")
    items = [json.loads(l) for l in open(a.queue) if l.strip()]
    gap = 60.0 / a.rpm
    with open(a.out, "a") as out:
        for i, item in enumerate(items):
            body = json.dumps({"model": a.model, "temperature": 0,
                               "messages": [{"role": "user", "content": PPLX_PROMPT.format(**item)}]}).encode()
            result = {"linkedin_profile_url": item["linkedin_profile_url"], "full_name": item["full_name"]}
            for attempt in range(4):
                try:
                    req = urllib.request.Request("https://api.perplexity.ai/chat/completions", body, {
                        "Authorization": f"Bearer {key}", "Content-Type": "application/json"})
                    text = json.load(urllib.request.urlopen(req, timeout=60))["choices"][0]["message"]["content"]
                    result.update(json.loads(text[text.find("{"):text.rfind("}") + 1]))
                    break
                except Exception as e:  # 429s and malformed replies: back off, then record the error
                    result["error"] = clean(e)
                    time.sleep(2 ** (attempt + 1))
            else:
                result.setdefault("confidence", "low")
            out.write(json.dumps(result) + "\n")
            out.flush()
            print(f"{i + 1}/{len(items)} {item['full_name']}: {result.get('confidence')}", file=sys.stderr)
            time.sleep(gap)
    print(json.dumps({"processed": len(items), "results": a.out}))


def cmd_merge(a):
    rows = load(a.enriched)
    bk = backup(a.enriched)
    merged = skipped = 0
    for line in open(a.results):
        if not line.strip():
            continue
        try:
            r = json.loads(line)
        except ValueError:
            skipped += 1
            continue
        key = norm_url(r.get("linkedin_profile_url")) or (r.get("full_name") or "").lower()
        conf = (r.get("confidence") or "low").lower()
        executed = r.get("current_title") or r.get("current_company") or r.get("notes") or r.get("error")
        if key not in rows or conf not in CONFIDENCE or not executed:
            skipped += 1
            continue
        row = rows[key]
        if conf == "low" and (row.get("confidence") or "").lower() in ("high", "medium"):
            skipped += 1  # never downgrade a verified row with an inconclusive retry
            continue
        row.update(current_title=clean(r.get("current_title")), current_company=clean(r.get("current_company")),
                   confidence=conf, resolved_at=date.today().isoformat(),
                   notes=clean(r.get("notes") or r.get("error"), 150))
        merged += 1
    n_over = apply_overrides(rows, a.overrides)
    save(a.enriched, rows)
    print(json.dumps({"merged": merged, "skipped": skipped, "overrides_applied": n_over, "backup": bk}))


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--home", default=HOME)
    ap.add_argument("--fresh-days", type=int, default=90)
    ap.add_argument("--fresh-days-high", type=int, default=180)
    sub = ap.add_subparsers(dest="cmd", required=True)
    p = sub.add_parser("ingest"); p.add_argument("--seed", default="")
    sub.add_parser("status")
    p = sub.add_parser("queue")
    p.add_argument("--limit", type=int, default=20)
    p.add_argument("--company", action="append", default=[])
    p.add_argument("--keywords", default="")
    p.add_argument("--out", default="")
    p = sub.add_parser("perplexity")
    p.add_argument("--queue", default="")
    p.add_argument("--out", default="")
    p.add_argument("--rpm", type=float, default=40)
    p.add_argument("--model", default="sonar")
    p = sub.add_parser("merge"); p.add_argument("--results", default="")
    a = ap.parse_args()

    a.home = os.path.expanduser(a.home)
    a.dir = os.path.join(a.home, "connections")
    a.enriched = os.path.join(a.home, "enriched.csv")
    a.overrides = os.path.join(a.home, "overrides.json")
    if a.cmd == "queue":
        a.out = a.out or os.path.join(a.home, "pending.jsonl")
    if a.cmd == "perplexity":
        a.queue = a.queue or os.path.join(a.home, "pending.jsonl")
        a.out = a.out or os.path.join(a.home, "results.jsonl")
    if a.cmd == "merge":
        a.results = a.results or os.path.join(a.home, "results.jsonl")
    {"ingest": cmd_ingest, "status": cmd_status, "queue": cmd_queue,
     "perplexity": cmd_perplexity, "merge": cmd_merge}[a.cmd](a)


if __name__ == "__main__":
    main()
