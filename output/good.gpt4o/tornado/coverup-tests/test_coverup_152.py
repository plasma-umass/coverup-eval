# file tornado/queues.py:53-56
# lines [53, 54, 56]
# branches []

import pytest
from tornado.queues import Queue, QueueFull

def test_queue_full_exception():
    queue = Queue(maxsize=1)
    
    # Put one item in the queue to fill it
    queue.put_nowait(1)
    
    # Attempt to put another item should raise QueueFull exception
    with pytest.raises(QueueFull):
        queue.put_nowait(2)
    
    # Clean up the queue
    queue.get_nowait()
