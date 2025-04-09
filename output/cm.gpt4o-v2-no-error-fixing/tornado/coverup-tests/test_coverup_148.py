# file: tornado/queues.py:256-272
# asked: {"lines": [264, 265, 266, 267, 268, 272], "branches": [[263, 264], [269, 272]]}
# gained: {"lines": [264, 265, 266, 267, 268, 272], "branches": [[263, 264], [269, 272]]}

import pytest
from tornado.queues import Queue, QueueEmpty
from tornado.concurrent import Future

def test_get_nowait_with_putters():
    queue = Queue(maxsize=1)
    future = Future()
    queue._putters.append((42, future))
    
    # Fill the queue to trigger the putter logic
    queue._queue.append(1)
    
    result = queue.get_nowait()
    
    assert result == 1
    assert queue.qsize() == 1
    assert future.done()

def test_get_nowait_with_items():
    queue = Queue()
    queue._queue.append(1)
    
    result = queue.get_nowait()
    
    assert result == 1
    assert queue.qsize() == 0

def test_get_nowait_empty():
    queue = Queue()
    
    with pytest.raises(QueueEmpty):
        queue.get_nowait()
