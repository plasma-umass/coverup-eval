# file: tornado/queues.py:173-175
# asked: {"lines": [173, 175], "branches": []}
# gained: {"lines": [173, 175], "branches": []}

import pytest
from tornado.queues import Queue

@pytest.fixture
def queue():
    return Queue()

def test_qsize_empty_queue(queue):
    assert queue.qsize() == 0

def test_qsize_non_empty_queue(queue):
    queue.put_nowait(1)
    assert queue.qsize() == 1

def test_qsize_multiple_items(queue):
    queue.put_nowait(1)
    queue.put_nowait(2)
    queue.put_nowait(3)
    assert queue.qsize() == 3

def test_qsize_after_get(queue):
    queue.put_nowait(1)
    queue.put_nowait(2)
    queue.get_nowait()
    assert queue.qsize() == 1
