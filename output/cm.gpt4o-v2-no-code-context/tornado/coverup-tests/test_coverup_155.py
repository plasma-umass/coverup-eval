# file: tornado/queues.py:306-307
# asked: {"lines": [306, 307], "branches": []}
# gained: {"lines": [306, 307], "branches": []}

import pytest
from tornado.queues import Queue
import collections

@pytest.fixture
def queue():
    return Queue()

def test_queue_init(queue):
    # Call the _init method directly to ensure lines 306-307 are executed
    queue._init()
    
    # Verify that the _queue attribute is initialized as a deque
    assert isinstance(queue._queue, collections.deque)
    
    # Clean up by resetting the _queue attribute
    queue._queue = None
