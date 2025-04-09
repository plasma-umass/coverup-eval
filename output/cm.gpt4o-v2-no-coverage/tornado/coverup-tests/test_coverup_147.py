# file: tornado/queues.py:173-175
# asked: {"lines": [173, 175], "branches": []}
# gained: {"lines": [173, 175], "branches": []}

import pytest
from tornado.queues import Queue

@pytest.fixture
def queue():
    return Queue()

def test_qsize(queue):
    assert queue.qsize() == 0
    queue.put_nowait(1)
    assert queue.qsize() == 1
    queue.get_nowait()
    assert queue.qsize() == 0
