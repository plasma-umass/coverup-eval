# file: tornado/queues.py:302-303
# asked: {"lines": [302, 303], "branches": []}
# gained: {"lines": [302], "branches": []}

import pytest
from tornado.queues import Queue

class _QueueIterator:
    def __init__(self, queue):
        self.queue = queue

    def __aiter__(self):
        return self

@pytest.mark.asyncio
async def test_queue_aiter():
    queue = Queue()
    aiter = queue.__aiter__()
    assert isinstance(aiter, _QueueIterator)
    assert aiter.queue is queue
