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

@pytest.fixture
def mock_ioloop(mocker):
    loop = mocker.Mock(spec=IOLoop)
    mocker.patch.object(IOLoop, 'current', return_value=loop)
    return loop

@pytest.mark.gen_test
def test_condition_notify_all():
    condition = Condition()
    results = []

    @gen.coroutine
    def waiter():
        yield condition.wait()
        results.append(True)

    with run_test_with_ioloop() as loop:
        # Start two waiters
        loop.add_callback(waiter)
        loop.add_callback(waiter)
        loop.run_sync(lambda: gen.sleep(0.1))  # Allow waiters to start and wait

        # Notify all waiters
        condition.notify_all()
        loop.run_sync(lambda: gen.sleep(0.1))  # Allow notification to process

        # Check that both waiters were notified
        assert len(results) == 2
        assert all(results)
