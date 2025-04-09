# file: tornado/queues.py:73-78
# asked: {"lines": [73, 74, 75, 77, 78], "branches": []}
# gained: {"lines": [73, 74, 77], "branches": []}

import pytest
import asyncio
from tornado.queues import Queue

from tornado.queues import _QueueIterator

@pytest.mark.asyncio
async def test_queue_iterator_anext():
    q = Queue()
    iterator = _QueueIterator(q)
    
    # Put an item in the queue
    await q.put(1)
    
    # Ensure __anext__ retrieves the item
    item = await iterator.__anext__()
    assert item == 1
    
    # Ensure the queue is now empty
    assert q.empty()

@pytest.mark.asyncio
async def test_queue_iterator_empty_queue():
    q = Queue()
    iterator = _QueueIterator(q)
    
    # Ensure __anext__ waits for an item
    async def put_item():
        await asyncio.sleep(0.1)
        await q.put(2)
    
    asyncio.create_task(put_item())
    
    item = await iterator.__anext__()
    assert item == 2
    
    # Ensure the queue is now empty
    assert q.empty()
