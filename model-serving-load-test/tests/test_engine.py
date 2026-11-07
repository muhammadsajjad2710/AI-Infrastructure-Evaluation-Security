from src.engine import load_test, predict
def test_load():
    assert predict(3) == 7
    out = load_test(50)
    assert out["n"] == 50 and out["seconds"] >= 0
