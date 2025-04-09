# file tornado/locks.py:523-524
# lines [523, 524]
# branches []

import pytest
from tornado.locks import Lock
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
def test_lock_acquire_release():
    lock = Lock()

    @gen.coroutine
    def acquire_release():
        yield lock.acquire()
        assert lock._block._value == 0
        lock.release()
        assert lock._block._value == 1

    with run_test_with_ioloop() as loop:
        loop.run_sync(acquire_release)
