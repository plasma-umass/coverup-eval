# file: tornado/locks.py:415-441
# asked: {"lines": [415, 416, 423, 424, 425, 426, 428, 429, 431, 432, 433, 434, 436, 437, 438, 439, 441], "branches": [[424, 425], [424, 428], [429, 431], [429, 441], [432, 433], [432, 434]]}
# gained: {"lines": [415, 416], "branches": []}

import pytest
from tornado import gen, ioloop
from tornado.concurrent import Future
from tornado.locks import Semaphore, _ReleasingContextManager
from datetime import timedelta

@pytest.mark.asyncio
async def test_semaphore_acquire_no_timeout():
    sem = Semaphore(1)
    result = await sem.acquire()
    assert isinstance(result, _ReleasingContextManager)
    assert sem._value == 0

@pytest.mark.asyncio
async def test_semaphore_acquire_with_timeout(monkeypatch):
    sem = Semaphore(0)
    timeout = timedelta(seconds=1)
    
    future = sem.acquire(timeout=timeout)
    
    def mock_add_timeout(deadline, callback):
        callback()
        return object()
    
    monkeypatch.setattr(ioloop.IOLoop.current(), 'add_timeout', mock_add_timeout)
    
    with pytest.raises(gen.TimeoutError):
        await future

@pytest.mark.asyncio
async def test_semaphore_acquire_with_timeout_no_trigger(monkeypatch):
    sem = Semaphore(0)
    timeout = timedelta(seconds=1)
    
    future = sem.acquire(timeout=timeout)
    
    def mock_add_timeout(deadline, callback):
        return object()
    
    monkeypatch.setattr(ioloop.IOLoop.current(), 'add_timeout', mock_add_timeout)
    
    def mock_remove_timeout(handle):
        pass
    
    monkeypatch.setattr(ioloop.IOLoop.current(), 'remove_timeout', mock_remove_timeout)
    
    sem.release()
    result = await future
    assert isinstance(result, _ReleasingContextManager)
    assert sem._value == 0
