from __future__ import annotations
class Vault:
    def __init__(self):
        self.rows: list[dict] = []
    def put(self, tenant: str, key: str, value: str) -> None:
        self.rows.append({"tenant": tenant, "key": key, "value": value})
    def get(self, tenant: str, key: str) -> str | None:
        for r in self.rows:
            if r["tenant"] == tenant and r["key"] == key:
                return r["value"]
        return None
