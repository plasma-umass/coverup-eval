# file: tornado/locks.py:415-441
# asked: {"lines": [415, 416, 423, 424, 425, 426, 428, 429, 431, 432, 433, 434, 436, 437, 438, 439, 441], "branches": [[424, 425], [424, 428], [429, 431], [429, 441], [432, 433], [432, 434]]}
# gained: {"lines": [415, 416], "branches": []}

import pytest
from tornado import gen, ioloop
from tornado.concurrent import Future
from tornado.locks import Semaphore
from unittest.mock import MagicMock
import datetime

class _ReleasingContextManager:
    def __init__(self, semaphore):
        self.semaphore = semaphore

@pytest.fixture
def semaphore():
    return Semaphore(1)

@pytest.mark.gen_test
async def test_acquire_with_value(semaphore):
    semaphore._value = 1
    result = await semaphore.acquire()
    assert isinstance(result, _ReleasingContextManager)
    assert semaphore._value == 0

@pytest.mark.gen_test
async def test_acquire_without_value_no_timeout(semaphore):
    semaphore._value = 0
    future = semaphore.acquire()
    assert not future.done()
    semaphore.release()
    result = await future
    assert isinstance(result, _ReleasingContextManager)
    assert semaphore._value == 0

@pytest.mark.gen_test
async def test_acquire_with_timeout(semaphore, monkeypatch):
    semaphore._value = 0
    timeout = datetime.timedelta(seconds=1)
    future = semaphore.acquire(timeout=timeout)
    assert not future.done()

    def mock_add_timeout(deadline, callback):
        callback()
        return MagicMock()

    monkeypatch.setattr(ioloop.IOLoop.current(), 'add_timeout', mock_add_timeout)
    await gen.sleep(0.1)
    with pytest.raises(gen.TimeoutError):
        await future

@pytest.mark.gen_test
async def test_acquire_with_timeout_and_release(semaphore, monkeypatch):
    semaphore._value = 0
    timeout = datetime.timedelta(seconds=1)
    future = semaphore.acquire(timeout=timeout)
    assert not future.done()

    def mock_add_timeout(deadline, callback):
        return MagicMock()

    monkeypatch.setattr(ioloop.IOLoop.current(), 'add_timeout', mock_add_timeout)
    semaphore.release()
    result = await future
    assert isinstance(result, _ReleasingContextManager)
    assert semaphore._value == 0
