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
    
    # Test with non-empty queue
    q._queue = [1, 2, 3]
    assert q._format() == "maxsize=5 queue=[1, 2, 3]"
    
    # Test with getters
    q._getters.append("getter1")
    assert q._format() == "maxsize=5 queue=[1, 2, 3] getters[1]"
    
    # Test with putters
    q._putters.append("putter1")
    assert q._format() == "maxsize=5 queue=[1, 2, 3] getters[1] putters[1]"
    
    # Test with unfinished tasks
    q._unfinished_tasks = 2
    assert q._format() == "maxsize=5 queue=[1, 2, 3] getters[1] putters[1] tasks=2"
    
    # Clean up
    q._queue = None
    q._getters.clear()
    q._putters.clear()
    q._unfinished_tasks = 0
