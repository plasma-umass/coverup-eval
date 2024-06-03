# file tornado/queues.py:177-178
# lines [177, 178]
# branches []

import pytest
from tornado.queues import Queue

@pytest.fixture
def queue():
    return Queue()

def test_queue_empty(queue):
    # Test that a new queue is empty
    assert queue.empty() == True

    # Add an item to the queue and test that it is not empty
    queue.put_nowait(1)
    assert queue.empty() == False

    # Remove the item and test that the queue is empty again
    queue.get_nowait()
    assert queue.empty() == True

    # Clean up the queue to ensure no side effects
    while not queue.empty():
        queue.get_nowait()
