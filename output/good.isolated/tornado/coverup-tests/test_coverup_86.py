# file tornado/queues.py:349-381
# lines [349, 350, 374, 375, 377, 378, 380, 381]
# branches []

import pytest
from tornado.queues import PriorityQueue
from tornado.ioloop import IOLoop
from tornado import gen

@pytest.mark.gen_test
def test_priority_queue_order():
    q = PriorityQueue()

    @gen.coroutine
    def put_items():
        yield q.put((1, 'medium-priority item'))
        yield q.put((0, 'high-priority item'))
        yield q.put((10, 'low-priority item'))

    IOLoop.current().spawn_callback(put_items)

    high_priority_item = yield q.get()
    assert high_priority_item == (0, 'high-priority item'), "The high-priority item should be first"

    medium_priority_item = yield q.get()
    assert medium_priority_item == (1, 'medium-priority item'), "The medium-priority item should be second"

    low_priority_item = yield q.get()
    assert low_priority_item == (10, 'low-priority item'), "The low-priority item should be third"

    # Clean up the queue to ensure it does not affect other tests
    yield q.put(None)  # Put a sentinel value to stop the get coroutine
    @gen.coroutine
    def cleanup():
        while True:
            item = yield q.get()
            if item is None:
                break
    IOLoop.current().spawn_callback(cleanup)
