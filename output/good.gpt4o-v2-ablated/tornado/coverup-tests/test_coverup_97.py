# file: tornado/queues.py:306-307
# asked: {"lines": [306, 307], "branches": []}
# gained: {"lines": [306, 307], "branches": []}

import pytest
from tornado.queues import Queue
import collections

@pytest.fixture
def queue():
    return Queue()

def test_queue_init(queue):
    queue._init()
    assert isinstance(queue._queue, collections.deque)
    assert len(queue._queue) == 0
