# file: tornado/queues.py:302-303
# asked: {"lines": [302, 303], "branches": []}
# gained: {"lines": [302], "branches": []}

import pytest
from tornado.queues import Queue
from tornado.ioloop import IOLoop
from tornado import gen

@pytest.mark.asyncio
async def test_queue_aiter():
    q = Queue(maxsize=2)

    async def producer():
        for item in range(3):
            await q.put(item)

    async def consumer():
        items = []
        async for item in q:
            items.append(item)
            if len(items) == 3:
                break
        return items

    IOLoop.current().spawn_callback(producer)
    items = await consumer()
    assert items == [0, 1, 2]
