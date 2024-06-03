# file tornado/queues.py:173-175
# lines [173, 175]
# branches []

import pytest
from tornado.queues import Queue

@pytest.fixture
def queue():
    return Queue()

def test_qsize_empty_queue(queue):
    assert queue.qsize() == 0

def test_qsize_non_empty_queue(queue):
    queue.put_nowait(1)
    queue.put_nowait(2)
    assert queue.qsize() == 2

def test_qsize_after_get(queue):
    queue.put_nowait(1)
    queue.put_nowait(2)
    queue.get_nowait()
    assert queue.qsize() == 1

def test_qsize_after_clear(queue):
    queue.put_nowait(1)
    queue.put_nowait(2)
    queue._queue.clear()
    assert queue.qsize() == 0
