# file: tornado/queues.py:209-223
# asked: {"lines": [216, 217, 218, 219], "branches": [[215, 216]]}
# gained: {"lines": [216, 217, 218, 219], "branches": [[215, 216]]}

import pytest
from tornado.queues import Queue, QueueFull
from tornado.concurrent import Future

def test_put_nowait_with_getters():
    queue = Queue()
    future = Future()
    
    # Simulate a getter waiting
    queue._getters.append(future)
    
    # Ensure the queue is empty
    assert queue.empty()
    
    # Put an item in the queue
    queue.put_nowait(1)
    
    # Ensure the future has the result set
    assert future.done()
    assert future.result() == 1

def test_put_nowait_queue_full():
    queue = Queue(maxsize=1)
    
    # Fill the queue
    queue.put_nowait(1)
    
    with pytest.raises(QueueFull):
        queue.put_nowait(2)

def test_put_nowait_no_getters():
    queue = Queue()
    
    # Ensure the queue is empty
    assert queue.empty()
    
    # Put an item in the queue
    queue.put_nowait(1)
    
    # Ensure the item is in the queue
    assert not queue.empty()
    assert queue.get_nowait() == 1
