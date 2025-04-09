# file: tornado/queues.py:168-171
# asked: {"lines": [168, 169, 171], "branches": []}
# gained: {"lines": [168, 169, 171], "branches": []}

import pytest
from tornado.queues import Queue

@pytest.fixture
def queue():
    return Queue(maxsize=5)

def test_queue_maxsize(queue):
    assert queue.maxsize == 5

def test_queue_maxsize_default():
    q = Queue()
    assert q.maxsize == 0
