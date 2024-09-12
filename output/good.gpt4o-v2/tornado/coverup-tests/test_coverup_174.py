# file: tornado/queues.py:177-178
# asked: {"lines": [177, 178], "branches": []}
# gained: {"lines": [177], "branches": []}

import pytest
from tornado.queues import Queue

@pytest.mark.asyncio
async def test_queue_empty():
    q = Queue()
    assert q.empty() == True  # Queue should be empty initially

    await q.put(1)
    assert q.empty() == False  # Queue should not be empty after putting an item

    await q.get()
    assert q.empty() == True  # Queue should be empty after getting the item
