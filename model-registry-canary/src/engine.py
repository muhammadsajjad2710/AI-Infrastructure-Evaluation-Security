from __future__ import annotations
class Registry:
    def __init__(self):
        self.prod = None
        self.canary = None
    def promote(self, name: str) -> None:
        self.prod = name
    def set_canary(self, name: str) -> None:
        self.canary = name
    def route(self, request_id: int) -> str:
        if self.canary and request_id % 10 == 0:
            return self.canary
        return self.prod or "none"
