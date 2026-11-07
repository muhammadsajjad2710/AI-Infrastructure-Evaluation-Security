from src.engine import Registry
def test_canary_split():
    r = Registry()
    r.promote("v1")
    r.set_canary("v2")
    paths = [r.route(i) for i in range(10)]
    assert paths.count("v2") == 1 and paths.count("v1") == 9
