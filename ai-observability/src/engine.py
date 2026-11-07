from __future__ import annotations
class Tracer:
    def __init__(self):
        self.spans: list[dict] = []
    def add(self, name: str, ms: float, quality: float) -> None:
        self.spans.append({"name": name, "ms": ms, "quality": quality})
    def summary(self) -> dict:
        if not self.spans:
            return {"count": 0}
        return {
            "count": len(self.spans),
            "p_latency": sorted(s["ms"] for s in self.spans)[len(self.spans) // 2],
            "avg_quality": sum(s["quality"] for s in self.spans) / len(self.spans),
        }
