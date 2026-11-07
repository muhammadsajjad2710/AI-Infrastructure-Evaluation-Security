from src.engine import bench
def test_bench():
    m = bench([0.2, 0.5, 1.0, 1.5])
    assert m["mae_student"] < 0.5
