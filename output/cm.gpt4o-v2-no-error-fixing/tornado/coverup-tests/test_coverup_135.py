# file: tornado/queues.py:309-310
# asked: {"lines": [309, 310], "branches": []}
# gained: {"lines": [309, 310], "branches": []}

import pytest
from tornado.queues import Queue
from collections import deque

@pytest.fixture
def queue_with_items():
    q = Queue()
    q._queue = deque([1, 2, 3])
    return q

def test_get_method(queue_with_items):
    q = queue_with_items
    assert q._get() == 1
    assert list(q._queue) == [2, 3]
