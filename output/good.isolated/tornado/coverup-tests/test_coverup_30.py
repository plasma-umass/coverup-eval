# file tornado/locks.py:145-155
# lines [145, 147, 148, 149, 150, 151, 152, 154, 155]
# branches ['148->149', '148->154', '150->148', '150->151', '154->exit', '154->155']

import pytest
from tornado.locks import Condition
from tornado.ioloop import IOLoop
from tornado import gen
from concurrent.futures import Future

@pytest.mark.gen_test
def test_condition_notify():
    condition = Condition()
    results = []

    @gen.coroutine
    def waiter():
        yield condition.wait()
        results.append(True)

    # Start 3 waiters
    IOLoop.current().add_callback(waiter)
    IOLoop.current().add_callback(waiter)
    IOLoop.current().add_callback(waiter)

    yield gen.moment  # Allow waiters to start and wait

    # Notify only 2 waiters
    condition.notify(2)

    yield gen.moment  # Allow notified waiters to run

    assert len(results) == 2, "Only two waiters should have been notified"

    # Clean up: Notify the remaining waiter to prevent it from blocking the IOLoop
    condition.notify(1)
    yield gen.moment  # Allow the last waiter to run

    assert len(results) == 3, "All waiters should have been notified after cleanup"
