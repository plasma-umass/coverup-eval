# file: tornado/queues.py:180-184
# asked: {"lines": [180, 181, 182, 184], "branches": [[181, 182], [181, 184]]}
# gained: {"lines": [180, 181, 182, 184], "branches": [[181, 182], [181, 184]]}

import pytest
from tornado.queues import Queue

@pytest.fixture
def queue():
    return Queue(maxsize=5)

def test_queue_full_when_maxsize_zero():
    queue = Queue(maxsize=0)
    assert not queue.full()

def test_queue_full_when_not_full(queue):
    assert not queue.full()

def test_queue_full_when_full(queue):
    for _ in range(5):
        queue.put_nowait(1)
    assert queue.full()

def test_queue_full_when_almost_full(queue):
    for _ in range(4):
        queue.put_nowait(1)
    assert not queue.full()
