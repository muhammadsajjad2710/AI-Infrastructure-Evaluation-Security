from src.engine import run_suite
def test_eval():
    out = run_suite([
        {"answer": "Paris is the capital of France", "must_include": ["Paris", "France"]},
        {"answer": "I do not know", "must_include": ["Paris"]},
    ])
    assert out["passed"] == 1 and out["total"] == 2
