from src.engine import assign, analyze
def test_ab():
    assert assign(2) == "A"
    out = analyze([
        {"arm": "A", "click": 0}, {"arm": "A", "click": 1},
        {"arm": "B", "click": 1}, {"arm": "B", "click": 1},
    ])
    assert out["winner"] == "B"
