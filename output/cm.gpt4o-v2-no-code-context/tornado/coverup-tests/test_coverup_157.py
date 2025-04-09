# file: tornado/queues.py:177-178
# asked: {"lines": [177, 178], "branches": []}
# gained: {"lines": [177, 178], "branches": []}

import pytest
from tornado.queues import Queue

@pytest.fixture
def empty_queue():
    return Queue()

@pytest.fixture
def non_empty_queue():
    q = Queue()
    q.put_nowait(1)
    return q

def test_empty_queue_is_empty(empty_queue):
    assert empty_queue.empty() is True

def test_non_empty_queue_is_not_empty(non_empty_queue):
    assert non_empty_queue.empty() is False
