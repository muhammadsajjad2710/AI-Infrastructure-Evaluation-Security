from __future__ import annotations
def teacher(x: float) -> float:
    return round(x * 1.7 + 0.3, 4)
def student(x: float) -> float:
    return round(x * 1.6 + 0.4, 4)
def quantized(x: float) -> float:
    return int(x * 17 + 3) / 10
def bench(xs: list[float]) -> dict:
    t = [teacher(x) for x in xs]
    s = [student(x) for x in xs]
    q = [quantized(x) for x in xs]
    mae_s = sum(abs(a - b) for a, b in zip(t, s)) / len(xs)
    mae_q = sum(abs(a - b) for a, b in zip(t, q)) / len(xs)
    return {"mae_student": mae_s, "mae_quant": mae_q}
