# file tornado/locks.py:157-159
# lines [159]
# branches []

import pytest
from tornado.locks import Condition
from tornado.ioloop import IOLoop
from tornado import gen
from contextlib import contextmanager

# Create a context manager to run async tests with the IOLoop
@contextmanager
def run_test_with_ioloop():
    loop = IOLoop.current()
    loop.make_current()
    yield loop
    loop.clear_current()
    loop.close(all_fds=True)

@pytest.mark.gen_test
def test_condition_notify_all():
    condition = Condition()
    results = []

    @gen.coroutine
    def waiter():
        yield condition.wait()
        results.append(True)

    with run_test_with_ioloop() as loop:
        # Start two waiters that will wait for the condition to be notified
        loop.add_callback(waiter)
        loop.add_callback(waiter)

        # Ensure that the waiters are waiting
        loop.call_later(0.1, condition.notify_all)
        loop.call_later(0.2, loop.stop)
        loop.start()

    # Check that both waiters were notified
    assert len(results) == 2
    assert all(results)
