# file tornado/queues.py:81-130
# lines [81, 82]
# branches []

import pytest
from tornado import gen
from tornado.ioloop import IOLoop
from tornado.queues import Queue

@pytest.mark.asyncio
async def test_queue_full_coverage():
    q = Queue(maxsize=2)

    async def consumer():
        async for item in q:
            try:
                assert item in range(5)
                await gen.sleep(0.01)
            finally:
                q.task_done()

    async def producer():
        for item in range(5):
            await q.put(item)
            assert q.qsize() <= 2

    async def main():
        IOLoop.current().spawn_callback(consumer)
        await producer()
        await q.join()
        assert q.empty()

    await IOLoop.current().run_sync(main)
