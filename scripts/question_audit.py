#!/usr/bin/env python3
"""Census question entry types across canonical Kami research domains.

This measures classification coverage and structural integrity, NOT question
quality, passage relevance, experimental success, or demonstrated competence.
Run from anywhere: python3 scripts/question_audit.py [--json] [--strict]
"""
import argparse
from collections import Counter
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TYPES = (
    "explanation", "execution", "verification", "diagnosis",
    "decomposition", "design", "empirical_investigation", "transfer"
)
SCOPES = ("conceptual", "open_goal", "capability_family", "specified_instance")


def scan():
    reports, problems = [], []
    for path in sorted((ROOT / "Investigations").glob("*/investigation.json")):
        data = json.loads(path.read_text(encoding="utf-8"))
        if "curiosity_atlas" not in data:
            continue
        domain = path.parent.name
        entries = data["curiosity_atlas"].get("entries", [])
        atlas = data["curiosity_atlas"]
        families = {f["id"] for f in atlas.get("families", [])}
        redirects = atlas.get("redirects", {})
        entry_ids = {q.get("id") for q in entries}
        for old_id, new_id in redirects.items():
            if old_id in entry_ids or new_id not in entry_ids:
                problems.append(f"{domain}: invalid question redirect {old_id!r} -> {new_id!r}")
        bridges = {b["id"]: b for b in data.get("navigation_bridges", [])}
        technical = {n["id"] for n in data.get("nodes", [])}
        for included in data.get("include_files", []):
            sub = json.loads((path.parent / included).read_text(encoding="utf-8"))
            technical.update(n["id"] for n in sub.get("nodes", []))
            for qid in sub.get("question_ids", []):
                if qid not in entry_ids:
                    problems.append(f"{domain}/{included}: noncanonical family question ID {qid}")
        types, scopes, seen = Counter(), Counter(), set()
        criteria = targets = resolved_bridges = 0
        for q in entries:
            qid = q.get("id")
            if not qid or qid in seen:
                problems.append(f"{domain}: duplicate or missing entry ID: {qid!r}")
            seen.add(qid)
            if q.get("family_id") not in families:
                problems.append(f"{domain}/{qid}: unknown question family")
            typ, scope = q.get("question_type"), q.get("task_scope")
            types[typ or "UNTAGGED"] += 1
            scopes[scope or "UNTAGGED"] += 1
            if typ not in TYPES:
                problems.append(f"{domain}/{qid}: missing or unknown question_type: {typ!r}")
            if scope not in SCOPES:
                problems.append(f"{domain}/{qid}: missing or unknown task_scope: {scope!r}")
            secondaries = q.get("secondary_question_types", [])
            if any(t not in TYPES or t == typ for t in secondaries):
                problems.append(f"{domain}/{qid}: invalid secondary_question_types")
            if scope == "capability_family" and q.get("success_criterion"):
                criteria += 1
            if scope == "capability_family" and not q.get("success_criterion"):
                problems.append(f"{domain}/{qid}: capability family missing success_criterion")
            ids = q.get("bridge_ids", [])
            if ids and all(b in bridges for b in ids):
                resolved_bridges += 1
            else:
                problems.append(f"{domain}/{qid}: missing or unresolved navigation bridge")
            if q.get("target_ids"):
                targets += 1
                missing = set(q["target_ids"]) - technical
                if missing:
                    problems.append(f"{domain}/{qid}: unresolved technical targets: {sorted(missing)}")
                reachable = {target for bid in ids if bid in bridges
                             for choice in bridges[bid].get("choices", [])
                             for target in choice.get("targets", [])}
                unreachable = set(q["target_ids"]) - reachable
                if unreachable:
                    problems.append(f"{domain}/{qid}: technical targets absent from question bridges: {sorted(unreachable)}")
        reports.append({
            "domain": domain, "entries": len(entries),
            "typed": len(entries) - types["UNTAGGED"],
            "types": dict(types), "scopes": dict(scopes),
            "capability_criteria": criteria,
            "resolved_bridges": resolved_bridges,
            "with_technical_targets": targets,
            "separate_question_index_nodes": len(data.get("question_nodes", []))
        })
    total = {
        "entries": sum(x["entries"] for x in reports),
        "typed": sum(x["typed"] for x in reports),
        "types": dict(sum((Counter(x["types"]) for x in reports), Counter())),
        "scopes": dict(sum((Counter(x["scopes"]) for x in reports), Counter())),
        "capability_criteria": sum(x["capability_criteria"] for x in reports),
        "resolved_bridges": sum(x["resolved_bridges"] for x in reports),
        "separate_question_index_nodes": sum(x["separate_question_index_nodes"] for x in reports)
    }
    return {"total": total, "domains": reports, "problems": problems}


def markdown(report):
    rows = report["domains"]
    print("# Canonical entry-question coverage")
    print()
    print("| Domain | Tagged / total | Conceptual | Open goal | Capability | Criterion | Bridges | Separate question-index nodes |")
    print("| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |")
    for r in rows:
        s = r["scopes"]
        print(f"| {r['domain']} | {r['typed']}/{r['entries']} | {s.get('conceptual',0)} | {s.get('open_goal',0)} | {s.get('capability_family',0)} | {r['capability_criteria']} | {r['resolved_bridges']} | {r['separate_question_index_nodes']} |")
    print()
    print("| Domain | " + " | ".join(TYPES) + " |")
    print("| --- | " + " | ".join("---:" for _ in TYPES) + " |")
    for r in rows:
        print("| " + r["domain"] + " | " + " | ".join(str(r["types"].get(t, 0)) for t in TYPES) + " |")
    t = report["total"]
    print(f"\nTotals: {t['typed']}/{t['entries']} entries classified, "
          f"{t['capability_criteria']} capability contracts, "
          f"{t['resolved_bridges']} entry-to-bridge references resolved.")
    print(f"Separate question-index nodes (NOT added to these totals): {t['separate_question_index_nodes']}.")
    print("These are navigation/metadata diagnostics, not evidence of answer quality or verified book passages.")
    if report["problems"]:
        print("\nStructural findings:")
        for p in report["problems"]:
            print("- " + p)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--json", action="store_true", help="Machine-readable report")
    parser.add_argument("--strict", action="store_true", help="Fail on structural findings")
    args = parser.parse_args()
    result = scan()
    if args.json:
        print(json.dumps(result, ensure_ascii=False, indent=2))
    else:
        markdown(result)
    return int(args.strict and bool(result["problems"]))


if __name__ == "__main__":
    raise SystemExit(main())
