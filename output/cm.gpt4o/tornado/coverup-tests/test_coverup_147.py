# file tornado/queues.py:47-50
# lines [47, 48, 50]
# branches []

import pytest
from tornado.queues import Queue, QueueEmpty

def test_queue_empty_exception():
    queue = Queue()
    
    with pytest.raises(QueueEmpty):
        queue.get_nowait()
    
    assert queue.qsize() == 0
