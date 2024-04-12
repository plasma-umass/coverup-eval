# file tornado/queues.py:180-184
# lines [180, 181, 182, 184]
# branches ['181->182', '181->184']

import pytest
from tornado.queues import Queue

@pytest.mark.gen_test
async def test_queue_full():
    # Create a Queue with maxsize 1
    queue = Queue(maxsize=1)

    # The queue should not be full initially
    assert not queue.full()

    # Put an item into the queue, reaching maxsize
    await queue.put('item')

    # Now the queue should be full
    assert queue.full()

    # Clean up by getting the item back
    await queue.get()
    assert not queue.full()
