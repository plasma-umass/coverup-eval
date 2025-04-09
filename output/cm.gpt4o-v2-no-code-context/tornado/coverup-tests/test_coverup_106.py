# file: tornado/queues.py:73-78
# asked: {"lines": [73, 74, 75, 77, 78], "branches": []}
# gained: {"lines": [73, 74, 77], "branches": []}

import pytest
from tornado.queues import Queue
from typing import Awaitable

class _QueueIterator:
    def __init__(self, q: Queue) -> None:
        self.q = q

    def __anext__(self) -> Awaitable:
        return self.q.get()

@pytest.mark.asyncio
async def test_queue_iterator():
    q = Queue()
    iterator = _QueueIterator(q)
    
    # Put an item in the queue to be retrieved
    await q.put(42)
    
    # Retrieve the item using the iterator
    item = await iterator.__anext__()
    
    # Assert that the item retrieved is the one that was put in
    assert item == 42

    # Clean up the queue
    assert q.empty()
