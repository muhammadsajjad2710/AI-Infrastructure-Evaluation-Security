from __future__ import annotations
PROVIDERS = {"local": {"cost": 0.0}, "cloud-small": {"cost": 0.002}, "cloud-large": {"cost": 0.02}}
def route(prefer: str, max_cost: float) -> dict:
    if prefer in PROVIDERS and PROVIDERS[prefer]["cost"] <= max_cost:
        return {"provider": prefer, "cost": PROVIDERS[prefer]["cost"]}
    options = [n for n, p in PROVIDERS.items() if p["cost"] <= max_cost]
    if not options:
        return {"error": "no_provider"}
    name = min(options, key=lambda n: PROVIDERS[n]["cost"])
    return {"provider": name, "cost": PROVIDERS[name]["cost"]}
