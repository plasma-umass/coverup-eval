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

    waiter = await sem.acquire()
    assert sem._value == 0
    assert isinstance(waiter, _ReleasingContextManager)

    sem.release()
    assert sem._value == 1

@pytest.mark.gen_test
async def test_semaphore_acquire_with_timeout():
    sem = Semaphore(0)
    assert sem._value == 0

    timeout = datetime.timedelta(seconds=1)
    future = sem.acquire(timeout=timeout)

    io_loop = IOLoop.current()
    io_loop.call_later(0.5, sem.release)
    waiter = await future
    assert sem._value == 0
    assert isinstance(waiter, _ReleasingContextManager)

    sem.release()
    assert sem._value == 1

@pytest.mark.gen_test
async def test_semaphore_acquire_timeout_occurs():
    sem = Semaphore(0)
    assert sem._value == 0

    timeout = datetime.timedelta(seconds=0.1)
    future = sem.acquire(timeout=timeout)

    with pytest.raises(gen.TimeoutError):
        await future

    assert sem._value == 0
    assert len(sem._waiters) == 0

@pytest.mark.gen_test
async def test_semaphore_acquire_timeout_cleanup():
    sem = Semaphore(0)
    assert sem._value == 0

    timeout = datetime.timedelta(seconds=0.1)
    future = sem.acquire(timeout=timeout)

    io_loop = IOLoop.current()
    io_loop.call_later(0.2, sem.release)

    with pytest.raises(gen.TimeoutError):
        await future

    assert sem._value == 0
    assert len(sem._waiters) == 0
