# file: tornado/queues.py:209-223
# asked: {"lines": [216, 217, 218, 219], "branches": [[215, 216]]}
# gained: {"lines": [216, 217, 218, 219], "branches": [[215, 216]]}

import pytest
from tornado.queues import Queue, QueueFull
from tornado.concurrent import Future

@pytest.fixture
def queue():
    return Queue(maxsize=1)

def test_put_nowait_with_getters(queue, mocker):
    # Mock the _consume_expired method to do nothing
    mocker.patch.object(queue, '_consume_expired', return_value=None)
    
    # Create a future and add it to the _getters deque
    future = Future()
    queue._getters.append(future)
    
    # Ensure the queue is empty
    assert queue.empty()
    
    # Put an item into the queue
    queue.put_nowait(1)
    
    # Assert that the future has been set with the correct value
    assert future.done()
    assert future.result() == 1

def test_put_nowait_queue_full(queue, mocker):
    # Mock the _consume_expired method to do nothing
    mocker.patch.object(queue, '_consume_expired', return_value=None)
    
    # Fill the queue
    queue.put_nowait(1)
    
    # Ensure the queue is full
    assert queue.full()
    
    # Attempt to put another item into the queue and expect a QueueFull exception
    with pytest.raises(QueueFull):
        queue.put_nowait(2)
