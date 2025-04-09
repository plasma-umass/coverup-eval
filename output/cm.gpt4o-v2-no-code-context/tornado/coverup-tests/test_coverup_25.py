# file: tornado/queues.py:256-272
# asked: {"lines": [256, 262, 263, 264, 265, 266, 267, 268, 269, 270, 272], "branches": [[263, 264], [263, 269], [269, 270], [269, 272]]}
# gained: {"lines": [256, 262, 263, 264, 265, 266, 267, 268, 269, 270, 272], "branches": [[263, 264], [263, 269], [269, 270], [269, 272]]}

import pytest
from tornado.queues import Queue, QueueEmpty

@pytest.fixture
def queue():
    return Queue(maxsize=1)

def test_get_nowait_with_item_in_queue(queue):
    queue.put_nowait(1)
    assert queue.get_nowait() == 1

def test_get_nowait_with_putters_waiting(queue):
    queue.put_nowait(1)
    putter_future = queue.put(2)
    assert queue.full()
    assert not putter_future.done()
    assert queue.get_nowait() == 1
    assert putter_future.done()
    assert queue.get_nowait() == 2

def test_get_nowait_empty_queue(queue):
    with pytest.raises(QueueEmpty):
        queue.get_nowait()
