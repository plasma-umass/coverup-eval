# file: tornado/queues.py:177-178
# asked: {"lines": [177, 178], "branches": []}
# gained: {"lines": [177, 178], "branches": []}

import pytest
from tornado.queues import Queue

@pytest.fixture
def queue():
    return Queue()

def test_queue_empty_initial(queue):
    assert queue.empty() == True

def test_queue_not_empty_after_put(queue):
    queue.put_nowait(1)
    assert queue.empty() == False

def test_queue_empty_after_get(queue):
    queue.put_nowait(1)
    queue.get_nowait()
    assert queue.empty() == True

def test_queue_empty_after_multiple_puts_and_gets(queue):
    queue.put_nowait(1)
    queue.put_nowait(2)
    queue.get_nowait()
    queue.get_nowait()
    assert queue.empty() == True
