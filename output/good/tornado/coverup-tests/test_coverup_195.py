# file tornado/locks.py:286-335
# lines [286, 287]
# branches []

import pytest
from tornado.locks import Semaphore
from tornado.ioloop import IOLoop
from tornado import gen

@pytest.mark.gen_test
async def test_semaphore_acquire_release():
    sem = Semaphore(0)

    # Test that acquire waits for a release
    acquire_future = sem.acquire()

    assert not acquire_future.done()
    sem.release()
    await acquire_future
    assert acquire_future.done()

    # Test that acquire does not wait when value is positive
    sem.release()
    acquire_future = sem.acquire()
    assert acquire_future.done()

    # Test that semaphore value does not go below zero
    sem = Semaphore(0)
    acquire_future1 = sem.acquire()
    acquire_future2 = sem.acquire()
    sem.release()
    await acquire_future1
    assert not acquire_future2.done()

    # Clean up
    sem.release()
    await acquire_future2
    assert acquire_future2.done()
