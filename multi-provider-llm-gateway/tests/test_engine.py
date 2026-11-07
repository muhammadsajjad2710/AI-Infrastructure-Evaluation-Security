from src.engine import route
def test_cost_cap():
    assert route("cloud-large", 0.001)["provider"] == "local"
    assert route("cloud-small", 0.01)["provider"] == "cloud-small"
