from __future__ import annotations
def assign(user_id: int) -> str:
    return "A" if user_id % 2 == 0 else "B"
def analyze(events: list[dict]) -> dict:
    arms = {"A": {"n": 0, "clicks": 0}, "B": {"n": 0, "clicks": 0}}
    for e in events:
        arm = e["arm"]
        arms[arm]["n"] += 1
        arms[arm]["clicks"] += int(e["click"])
    def rate(arm: str) -> float:
        n = arms[arm]["n"]
        return arms[arm]["clicks"] / n if n else 0.0
    return {"A": rate("A"), "B": rate("B"), "winner": "B" if rate("B") > rate("A") else "A"}
