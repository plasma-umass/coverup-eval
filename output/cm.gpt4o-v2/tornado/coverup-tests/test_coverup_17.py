# file: tornado/queues.py:336-346
# asked: {"lines": [336, 337, 338, 339, 340, 341, 342, 343, 344, 345, 346], "branches": [[338, 339], [338, 340], [340, 341], [340, 342], [342, 343], [342, 344], [344, 345], [344, 346]]}
# gained: {"lines": [336], "branches": []}

import pytest
from tornado.queues import Queue

@pytest.mark.asyncio
async def test_queue_format():
    q = Queue(maxsize=5)
    
    # Test with empty queue
    assert q._format() == "maxsize=5"
    
    # Add items to the queue
    await q.put(1)
    await q.put(2)
    
    # Test with items in the queue
    assert "queue=" in q._format()
    
    # Add getters
    getter = q.get()
    assert "getters[1]" in q._format()
    
    # Add putters
    putter = q.put(3)
    assert "putters[1]" in q._format()
    
    # Add unfinished tasks
    q._unfinished_tasks = 2
    assert "tasks=2" in q._format()
    
    # Clean up
    getter.cancel()
    putter.cancel()
    await q.get()
    await q.get()
    q.task_done()
    q.task_done()
