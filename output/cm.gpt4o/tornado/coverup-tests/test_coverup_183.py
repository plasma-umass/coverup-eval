# file tornado/queues.py:312-313
# lines [312, 313]
# branches []

import pytest
from tornado.queues import Queue

def test_queue_put():
    queue = Queue()
    item = "test_item"
    
    # Ensure the queue is initially empty
    assert len(queue._queue) == 0
    
    # Put an item in the queue
    queue._put(item)
    
    # Verify the item is in the queue
    assert len(queue._queue) == 1
    assert queue._queue[0] == item
    
    # Clean up
    queue._queue.clear()
    assert len(queue._queue) == 0
