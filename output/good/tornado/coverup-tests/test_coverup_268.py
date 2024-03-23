# file tornado/queues.py:349-381
# lines [375, 378, 381]
# branches []

import pytest
from tornado.queues import PriorityQueue

@pytest.fixture
def priority_queue():
    return PriorityQueue()

@pytest.mark.asyncio
async def test_priority_queue_methods(priority_queue):
    # Test _init method
    assert hasattr(priority_queue, '_queue')
    assert priority_queue._queue == []

    # Test _put method
    await priority_queue.put((2, 'medium-priority item'))
    await priority_queue.put((1, 'high-priority item'))
    await priority_queue.put((3, 'low-priority item'))
    assert list(priority_queue._queue) == [(1, 'high-priority item'), (2, 'medium-priority item'), (3, 'low-priority item')]

    # Test _get method
    high_priority_item = await priority_queue.get()
    assert high_priority_item == (1, 'high-priority item')
    priority_queue.task_done()

    medium_priority_item = await priority_queue.get()
    assert medium_priority_item == (2, 'medium-priority item')
    priority_queue.task_done()

    low_priority_item = await priority_queue.get()
    assert low_priority_item == (3, 'low-priority item')
    priority_queue.task_done()

    # Ensure the queue is empty now
    assert priority_queue.qsize() == 0

    # Clean up after the test
    await priority_queue.join()
