# file: tornado/queues.py:180-184
# asked: {"lines": [180, 181, 182, 184], "branches": [[181, 182], [181, 184]]}
# gained: {"lines": [180], "branches": []}

import pytest
from tornado.queues import Queue

@pytest.mark.asyncio
async def test_queue_full():
    # Test when maxsize is 0 (unbounded)
    q_unbounded = Queue(maxsize=0)
    assert not q_unbounded.full()

    # Test when maxsize is greater than 0 and queue is not full
    q_not_full = Queue(maxsize=2)
    await q_not_full.put(1)
    assert not q_not_full.full()

    # Test when maxsize is greater than 0 and queue is full
    q_full = Queue(maxsize=1)
    await q_full.put(1)
    assert q_full.full()
