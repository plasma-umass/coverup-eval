# file tornado/queues.py:302-303
# lines [302, 303]
# branches []

import pytest
from tornado.queues import Queue

class _QueueIterator:
    def __init__(self, queue):
        self.queue = queue

    def __anext__(self):
        if self.queue.empty():
            raise StopAsyncIteration
        return self.queue.get()

@pytest.mark.asyncio
async def test_queue_aiter():
    queue = Queue()
    await queue.put(1)
    await queue.put(2)

    async for item in queue:
        assert item in [1, 2]

    assert queue.empty()
