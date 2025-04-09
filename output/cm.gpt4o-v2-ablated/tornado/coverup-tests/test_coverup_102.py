# file: tornado/queues.py:330-331
# asked: {"lines": [330, 331], "branches": []}
# gained: {"lines": [330, 331], "branches": []}

import pytest
from tornado.queues import Queue

@pytest.fixture
def queue():
    return Queue()

def test_queue_repr(queue):
    repr_str = repr(queue)
    assert repr_str.startswith("<Queue at ")
    assert repr_str.endswith(">")
    assert "Queue" in repr_str
    assert hex(id(queue)) in repr_str

def test_queue_format(monkeypatch, queue):
    def mock_format(self):
        return "mock_format"
    
    monkeypatch.setattr(Queue, "_format", mock_format)
    repr_str = repr(queue)
    assert "mock_format" in repr_str
