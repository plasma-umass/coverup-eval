# file: tornado/locks.py:454-455
# asked: {"lines": [454, 455], "branches": []}
# gained: {"lines": [454], "branches": []}

import pytest
from tornado.locks import Semaphore
from tornado.ioloop import IOLoop
from tornado.concurrent import Future
from tornado import gen

class _ReleasingContextManager:
    def __init__(self, semaphore):
        self.semaphore = semaphore

    async def __aenter__(self):
        pass

    async def __aexit__(self, exc_type, exc, tb):
        self.semaphore.release()

class _TimeoutGarbageCollector:
    def _garbage_collect(self):
        pass

@pytest.mark.asyncio
async def test_semaphore_aenter():
    semaphore = Semaphore()
    semaphore._value = 1
    semaphore._waiters = []

    async with semaphore:
        assert semaphore._value == 0

    assert semaphore._value == 1
    assert len(semaphore._waiters) == 0

@pytest.mark.asyncio
async def test_semaphore_aenter_with_wait():
    semaphore = Semaphore()
    semaphore._value = 0
    semaphore._waiters = []

    acquire_future = Future()
    semaphore._waiters.append(acquire_future)

    async def acquire_later():
        await gen.sleep(0.1)
        semaphore.release()

    IOLoop.current().add_callback(acquire_later)

    async with semaphore:
        assert semaphore._value == 0

    assert semaphore._value == 1
    assert len(semaphore._waiters) == 0
