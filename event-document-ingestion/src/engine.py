from __future__ import annotations
import hashlib
class Ingestor:
    def __init__(self):
        self.seen: set[str] = set()
        self.docs: list[str] = []
    def _hash(self, text: str) -> str:
        return hashlib.sha256(text.encode()).hexdigest()
    def ingest(self, text: str) -> dict:
        h = self._hash(text)
        if h in self.seen:
            return {"stored": False, "duplicate": True}
        self.seen.add(h)
        self.docs.append(text)
        return {"stored": True, "duplicate": False}
    def replay(self, events: list[str]) -> None:
        for e in events:
            self.ingest(e)
