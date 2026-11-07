from __future__ import annotations
INJECTION = ("ignore previous", "system prompt", "developer message", "override instructions")
LEAKAGE = ("api key", "password is", "secret=", "ssn")
def scan(text: str) -> dict:
    low = text.lower()
    inj = [p for p in INJECTION if p in low]
    leak = [p for p in LEAKAGE if p in low]
    return {"injection": bool(inj), "leakage": bool(leak), "hits": inj + leak}
def should_block(text: str) -> bool:
    s = scan(text)
    return s["injection"] or s["leakage"]
