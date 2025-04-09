# file tornado/queues.py:209-223
# lines [209, 214, 215, 216, 217, 218, 219, 220, 221, 223]
# branches ['215->216', '215->220', '220->221', '220->223']

import pytest
from tornado.queues import Queue, QueueFull
from tornado.concurrent import Future

def test_put_nowait_queue_full(mocker):
    queue = Queue(maxsize=1)
    queue.put_nowait(1)  # Fill the queue

    with pytest.raises(QueueFull):
        queue.put_nowait(2)  # This should raise QueueFull

def test_put_nowait_with_getters(mocker):
    queue = Queue(maxsize=1)
    future = Future()
    queue._getters.append(future)
    
    assert queue.empty(), "queue should be empty initially"
    
    queue.put_nowait(1)
    
    assert future.done(), "future should be done after put_nowait"
    assert future.result() == 1, "future result should be the item put in the queue"
    assert queue.empty(), "queue should be empty after putting item with waiting getter"

def test_put_nowait_normal(mocker):
    queue = Queue(maxsize=2)
    queue.put_nowait(1)
    
    assert not queue.empty(), "queue should not be empty after put_nowait"
    assert queue.qsize() == 1, "queue size should be 1 after put_nowait"
    
    queue.put_nowait(2)
    
    assert queue.full(), "queue should be full after putting two items"
    assert queue.qsize() == 2, "queue size should be 2 after putting two items"
