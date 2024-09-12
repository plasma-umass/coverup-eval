# file: tornado/queues.py:384-414
# asked: {"lines": [408, 411, 414], "branches": []}
# gained: {"lines": [408, 411, 414], "branches": []}

import pytest
from tornado.queues import LifoQueue, QueueEmpty

def test_lifo_queue_put_get():
    q = LifoQueue()
    q.put(3)
    q.put(2)
    q.put(1)
    
    assert q.get_nowait() == 1
    assert q.get_nowait() == 2
    assert q.get_nowait() == 3

def test_lifo_queue_empty():
    q = LifoQueue()
    
    with pytest.raises(QueueEmpty):
        q.get_nowait()

def test_lifo_queue_order():
    q = LifoQueue()
    q.put(1)
    q.put(2)
    q.put(3)
    
    assert q.get_nowait() == 3
    assert q.get_nowait() == 2
    assert q.get_nowait() == 1

def test_lifo_queue_cleanup(monkeypatch):
    q = LifoQueue()
    q.put(1)
    q.put(2)
    
    assert q.get_nowait() == 2
    assert q.get_nowait() == 1
    
    # Ensure the queue is empty after the test
    with pytest.raises(QueueEmpty):
        q.get_nowait()
