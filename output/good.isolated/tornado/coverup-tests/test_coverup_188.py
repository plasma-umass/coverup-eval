# file tornado/queues.py:306-307
# lines [306, 307]
# branches []

import pytest
import collections
from tornado.queues import Queue

@pytest.fixture
def queue():
    return Queue()

def test_queue_init(queue):
    assert isinstance(queue._queue, collections.deque)
    assert len(queue._queue) == 0
