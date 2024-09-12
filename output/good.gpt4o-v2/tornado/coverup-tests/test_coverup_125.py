# file: tornado/queues.py:47-50
# asked: {"lines": [47, 48, 50], "branches": []}
# gained: {"lines": [47, 48, 50], "branches": []}

import pytest
from tornado.queues import Queue, QueueEmpty

def test_queue_empty_exception():
    queue = Queue(maxsize=1)
    
    with pytest.raises(QueueEmpty):
        queue.get_nowait()

    # Clean up
    del queue
