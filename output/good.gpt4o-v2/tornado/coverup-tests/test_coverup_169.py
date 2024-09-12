# file: tornado/queues.py:302-303
# asked: {"lines": [302, 303], "branches": []}
# gained: {"lines": [302], "branches": []}

import pytest
from tornado.queues import Queue, _QueueIterator

@pytest.mark.asyncio
async def test_queue_aiter():
    queue = Queue()
    aiter = queue.__aiter__()
    assert isinstance(aiter, _QueueIterator)
    assert aiter.q is queue
