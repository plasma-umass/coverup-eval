# file tornado/queues.py:81-130
# lines [81, 82]
# branches []

import pytest
from tornado.queues import Queue
from tornado import gen, ioloop

@pytest.mark.gen_test
async def test_queue_full_coverage():
    q = Queue(maxsize=1)

    @gen.coroutine
    def consumer():
        while True:
            item = yield q.get()
            try:
                assert item is not None
            finally:
                q.task_done()

    @gen.coroutine
    def producer():
        for item in range(3):
            yield q.put(item)
            if q.full():
                break

    ioloop.IOLoop.current().spawn_callback(consumer)
    yield producer()
    yield q.join()  # Wait for consumer to process items

    assert q.empty()
