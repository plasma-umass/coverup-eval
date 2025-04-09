# file: tornado/queues.py:177-178
# asked: {"lines": [178], "branches": []}
# gained: {"lines": [178], "branches": []}

import pytest
from tornado.queues import Queue

@pytest.fixture
def queue():
    return Queue()

def test_queue_empty(queue):
    assert queue.empty() == True
    queue.put_nowait(1)
    assert queue.empty() == False
    queue.get_nowait()
    assert queue.empty() == True
