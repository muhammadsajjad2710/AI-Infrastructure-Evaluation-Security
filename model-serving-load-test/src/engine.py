from __future__ import annotations
import time
def predict(x: float) -> float:
    return 2.0 * x + 1.0
def load_test(n: int = 200) -> dict:
    t0 = time.perf_counter()
    vals = [predict(i / 10) for i in range(n)]
    elapsed = time.perf_counter() - t0
    return {"n": n, "seconds": elapsed, "last": vals[-1]}
