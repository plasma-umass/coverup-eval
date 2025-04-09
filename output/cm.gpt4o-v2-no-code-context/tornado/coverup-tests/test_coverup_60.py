# file: tornado/queues.py:384-414
# asked: {"lines": [384, 385, 407, 408, 410, 411, 413, 414], "branches": []}
# gained: {"lines": [384, 385, 407, 408, 410, 411, 413, 414], "branches": []}

import pytest
from tornado.queues import LifoQueue, QueueEmpty

def test_lifo_queue_put_and_get():
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

def test_lifo_queue_multiple_puts():
    q = LifoQueue()
    q.put(1)
    q.put(2)
    q.put(3)
    q.put(4)
    
    assert q.get_nowait() == 4
    assert q.get_nowait() == 3
    assert q.get_nowait() == 2
    assert q.get_nowait() == 1

def test_lifo_queue_put_and_get_with_cleanup(monkeypatch):
    q = LifoQueue()
    q.put(1)
    q.put(2)
    q.put(3)
    
    assert q.get_nowait() == 3
    assert q.get_nowait() == 2
    assert q.get_nowait() == 1
    
    # Clean up
    monkeypatch.setattr(q, '_queue', [])
    assert q._queue == []
