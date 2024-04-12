# file tornado/queues.py:302-303
# lines [302, 303]
# branches []

import pytest
from tornado.queues import Queue
from tornado.ioloop import IOLoop
from tornado import gen

class TestQueueAsyncIterator:
    @pytest.mark.gen_test
    async def test_queue_aiter(self):
        q = Queue(maxsize=1)

        async def put_item():
            # Put an item in the queue
            await q.put(1)

        async def test_aiter():
            # Test the __aiter__ method
            async for item in q:
                assert item == 1
                break  # Exit after the first item to avoid infinite loop

        IOLoop.current().spawn_callback(put_item)
        await test_aiter()
        # Ensure the queue is empty before finishing the test
        assert q.qsize() == 0
