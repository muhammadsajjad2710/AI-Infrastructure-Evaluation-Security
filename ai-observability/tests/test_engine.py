from src.engine import Tracer
def test_trace():
    t = Tracer()
    t.add("retrieve", 12, 0.9)
    t.add("generate", 40, 0.7)
    s = t.summary()
    assert s["count"] == 2 and s["avg_quality"] > 0.7
