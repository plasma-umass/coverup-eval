# file: tornado/queues.py:309-310
# asked: {"lines": [309, 310], "branches": []}
# gained: {"lines": [309, 310], "branches": []}

import pytest
from collections import deque
from tornado.queues import Queue

@pytest.fixture
def queue():
    q = Queue()
    q._queue = deque()
    return q

def test_get_from_non_empty_queue(queue):
    queue._queue.append(1)
    assert queue._get() == 1
    assert len(queue._queue) == 0

def test_get_from_empty_queue(queue):
    with pytest.raises(IndexError):
        queue._get()
