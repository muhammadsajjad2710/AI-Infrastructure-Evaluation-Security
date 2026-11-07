from src.engine import Vault
def test_isolation():
    v = Vault()
    v.put("a", "note", "alpha-secret")
    v.put("b", "note", "beta-secret")
    assert v.get("a", "note") == "alpha-secret"
    assert v.get("a", "note") != v.get("b", "note")
    assert v.get("a", "missing") is None
