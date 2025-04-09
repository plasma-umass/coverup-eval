# file: tornado/queues.py:384-414
# asked: {"lines": [384, 385, 407, 408, 410, 411, 413, 414], "branches": []}
# gained: {"lines": [384, 385, 407, 408, 410, 411, 413, 414], "branches": []}

import pytest
from tornado.queues import LifoQueue

@pytest.fixture
def lifo_queue():
    return LifoQueue()

def test_lifo_queue_init(lifo_queue):
    assert lifo_queue._queue == []

def test_lifo_queue_put(lifo_queue):
    lifo_queue._put(1)
    assert lifo_queue._queue == [1]
    lifo_queue._put(2)
    assert lifo_queue._queue == [1, 2]

def test_lifo_queue_get(lifo_queue):
    lifo_queue._put(1)
    lifo_queue._put(2)
    assert lifo_queue._get() == 2
    assert lifo_queue._get() == 1
    assert lifo_queue._queue == []

def test_lifo_queue_integration(lifo_queue):
    lifo_queue.put(3)
    lifo_queue.put(2)
    lifo_queue.put(1)
    assert lifo_queue.get_nowait() == 1
    assert lifo_queue.get_nowait() == 2
    assert lifo_queue.get_nowait() == 3
