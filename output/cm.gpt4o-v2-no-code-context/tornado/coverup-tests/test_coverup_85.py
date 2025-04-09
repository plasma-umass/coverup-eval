# file: tornado/locks.py:262-283
# asked: {"lines": [262, 263, 271, 272, 274, 275, 277, 283], "branches": []}
# gained: {"lines": [262, 263, 271, 274, 277], "branches": []}

import pytest
from tornado.locks import Semaphore, Lock
from tornado.ioloop import IOLoop

class _ReleasingContextManager:
    def __init__(self, obj):
        self._obj = obj

    def __enter__(self):
        pass

    def __exit__(self, exc_type, exc_val, exc_tb):
        self._obj.release()

@pytest.fixture
def semaphore():
    return Semaphore(1)

@pytest.fixture
def lock():
    return Lock()

@pytest.mark.gen_test
async def test_releasing_context_manager_semaphore(semaphore):
    await semaphore.acquire()
    assert semaphore._value == 0
    with _ReleasingContextManager(semaphore):
        pass
    assert semaphore._value == 1

@pytest.mark.gen_test
async def test_releasing_context_manager_lock(lock):
    await lock.acquire()
    assert not lock._waiters.empty()
    with _ReleasingContextManager(lock):
        pass
    assert lock._waiters.empty()

@pytest.mark.gen_test
async def test_releasing_context_manager_semaphore_exception(semaphore):
    await semaphore.acquire()
    assert semaphore._value == 0
    try:
        with _ReleasingContextManager(semaphore):
            raise ValueError("Test exception")
    except ValueError:
        pass
    assert semaphore._value == 1

@pytest.mark.gen_test
async def test_releasing_context_manager_lock_exception(lock):
    await lock.acquire()
    assert not lock._waiters.empty()
    try:
        with _ReleasingContextManager(lock):
            raise ValueError("Test exception")
    except ValueError:
        pass
    assert lock._waiters.empty()
