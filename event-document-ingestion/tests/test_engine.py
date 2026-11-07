from src.engine import Ingestor
def test_dedup_and_replay():
    i = Ingestor()
    assert i.ingest("hello")["stored"]
    assert i.ingest("hello")["duplicate"]
    i.replay(["hello", "world"])
    assert i.docs == ["hello", "world"]
