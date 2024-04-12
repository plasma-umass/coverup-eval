# file tornado/queues.py:177-178
# lines [177, 178]
# branches []

import pytest
from tornado.queues import Queue

@pytest.fixture
def empty_queue():
    return Queue()

def test_queue_empty(empty_queue):
    assert empty_queue.empty() == True, "Queue should be empty initially"
    
    empty_queue._queue.append(1)  # Directly manipulate the internal queue
    assert empty_queue.empty() == False, "Queue should not be empty after adding an element"
    
    empty_queue._queue.pop()  # Clean up by removing the element
    assert empty_queue.empty() == True, "Queue should be empty after removing the element"
