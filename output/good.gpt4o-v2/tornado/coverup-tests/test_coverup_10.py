# file: tornado/locks.py:415-441
# asked: {"lines": [415, 416, 423, 424, 425, 426, 428, 429, 431, 432, 433, 434, 436, 437, 438, 439, 441], "branches": [[424, 425], [424, 428], [429, 431], [429, 441], [432, 433], [432, 434]]}
# gained: {"lines": [415, 416], "branches": []}

import pytest
from tornado.locks import Semaphore
from tornado.ioloop import IOLoop
from tornado import gen
from tornado.concurrent import Future
import datetime

@pytest.mark.gen_test
async def test_semaphore_acquire_no_timeout():
    sem = Semaphore(1)
    assert sem._value == 1

    waiter = sem.acquire()
    assert isinstance(waiter, Future)
    result = await waiter
    assert sem._value == 0
    assert isinstance(result, _ReleasingContextManager)

    sem.release()
    assert sem._value == 1

@pytest.mark.gen_test
async def test_semaphore_acquire_with_timeout():
    sem = Semaphore(0)
    assert sem._value == 0

    timeout = datetime.timedelta(seconds=1)
    waiter = sem.acquire(timeout=timeout)
    assert isinstance(waiter, Future)

    with pytest.raises(gen.TimeoutError):
        await waiter

    assert sem._value == 0

@pytest.mark.gen_test
async def test_semaphore_acquire_timeout_cleanup():
    sem = Semaphore(0)
    assert sem._value == 0

    timeout = datetime.timedelta(seconds=1)
    waiter = sem.acquire(timeout=timeout)
    assert isinstance(waiter, Future)

    io_loop = IOLoop.current()
    timeout_handle = io_loop.add_timeout(timeout, lambda: None)
    waiter.add_done_callback(lambda _: io_loop.remove_timeout(timeout_handle))

    with pytest.raises(gen.TimeoutError):
        await waiter

    assert sem._value == 0
    assert not io_loop._timeouts

@pytest.mark.gen_test
async def test_semaphore_acquire_release():
    sem = Semaphore(1)
    assert sem._value == 1

    waiter = sem.acquire()
    assert isinstance(waiter, Future)
    result = await waiter
    assert sem._value == 0
    assert isinstance(result, _ReleasingContextManager)

    sem.release()
    assert sem._value == 1

    waiter = sem.acquire()
    assert isinstance(waiter, Future)
    result = await waiter
    assert sem._value == 0
    assert isinstance(result, _ReleasingContextManager)

    sem.release()
    assert sem._value == 1
