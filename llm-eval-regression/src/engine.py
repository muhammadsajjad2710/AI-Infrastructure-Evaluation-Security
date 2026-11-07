from __future__ import annotations
def grade(answer: str, must_include: list[str]) -> dict:
    missing = [w for w in must_include if w.lower() not in answer.lower()]
    return {"pass": not missing, "missing": missing}
def run_suite(cases: list[dict]) -> dict:
    results = [grade(c["answer"], c["must_include"]) for c in cases]
    return {"passed": sum(r["pass"] for r in results), "total": len(results), "results": results}
