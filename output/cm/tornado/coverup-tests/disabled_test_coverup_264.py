# file tornado/locks.py:262-283
# lines [275, 283]
# branches []

import pytest
from tornado.locks import Semaphore
from tornado.ioloop import IOLoop
from tornado import gen
from contextlib import contextmanager

# Create a context manager to run async code in a synchronous way
@contextmanager
def run_sync():
    loop = IOLoop.current()
    try:
        yield loop.run_sync
    finally:
        loop.clear_current()
        loop.close(all_fds=True)

@pytest.fixture
def semaphore():
    return Semaphore()

@pytest.mark.gen_test
def test_releasing_context_manager(semaphore):
    @gen.coroutine
    def acquire_and_release():
        with (yield semaphore.acquire()):
            pass  # The __enter__ method is called here, but does nothing (line 275)
        # The __exit__ method is called here, releasing the semaphore (line 283)

    with run_sync() as run:
        run(acquire_and_release)

    assert semaphore._value == 1  # Postcondition: semaphore should be released
