# file: tornado/queues.py:384-414
# asked: {"lines": [384, 385, 407, 408, 410, 411, 413, 414], "branches": []}
# gained: {"lines": [384, 385, 407, 408, 410, 411, 413, 414], "branches": []}

import pytest
from tornado.queues import LifoQueue

def test_lifo_queue():
    q = LifoQueue()
    q.put(3)
    q.put(2)
    q.put(1)

    assert q.get_nowait() == 1
    assert q.get_nowait() == 2
    assert q.get_nowait() == 3

def test_lifo_queue_init():
    q = LifoQueue()
    assert q._queue == []

def test_lifo_queue_put():
    q = LifoQueue()
    q._put(1)
    assert q._queue == [1]
    q._put(2)
    assert q._queue == [1, 2]

def test_lifo_queue_get():
    q = LifoQueue()
    q._put(1)
    q._put(2)
    assert q._get() == 2
    assert q._get() == 1
