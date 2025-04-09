# file: tornado/queues.py:180-184
# asked: {"lines": [180, 181, 182, 184], "branches": [[181, 182], [181, 184]]}
# gained: {"lines": [180], "branches": []}

import pytest
from tornado.queues import Queue

@pytest.mark.asyncio
async def test_queue_full():
    # Test when maxsize is 0 (unbounded queue)
    q = Queue(maxsize=0)
    assert not q.full()

    # Test when maxsize is greater than 0 and queue is not full
    q = Queue(maxsize=2)
    assert not q.full()

    # Test when maxsize is greater than 0 and queue is full
    await q.put(1)
    await q.put(2)
    assert q.full()

    # Clean up
    await q.get()
    await q.get()
    assert not q.full()
