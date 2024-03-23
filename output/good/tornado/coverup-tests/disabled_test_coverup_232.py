# file tornado/queues.py:349-381
# lines [375, 378, 381]
# branches []

import pytest
from tornado.queues import PriorityQueue
from tornado.ioloop import IOLoop
from tornado import gen

@pytest.fixture
def io_loop():
    loop = IOLoop.current()
    yield loop
    loop.clear_current()
    loop.close(all_fds=True)

@pytest.mark.gen_test
def test_priority_queue_full_coverage(io_loop):
    q = PriorityQueue()

    @gen.coroutine
    def put_items():
        yield q.put((1, 'medium-priority item'))
        yield q.put((0, 'high-priority item'))
        yield q.put((10, 'low-priority item'))

    @gen.coroutine
    def get_items():
        high_priority_item = yield q.get()
        assert high_priority_item == (0, 'high-priority item')
        medium_priority_item = yield q.get()
        assert medium_priority_item == (1, 'medium-priority item')
        low_priority_item = yield q.get()
        assert low_priority_item == (10, 'low-priority item')

    io_loop.run_sync(put_items)
    io_loop.run_sync(get_items)
