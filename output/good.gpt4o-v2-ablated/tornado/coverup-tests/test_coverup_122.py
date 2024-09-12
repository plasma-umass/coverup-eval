# file: tornado/locks.py:466-483
# asked: {"lines": [481, 482, 483], "branches": [[481, 482], [481, 483]]}
# gained: {"lines": [481, 482, 483], "branches": [[481, 482], [481, 483]]}

import pytest
from tornado.locks import BoundedSemaphore

@pytest.fixture
def bounded_semaphore():
    return BoundedSemaphore(2)

def test_bounded_semaphore_initial_value(bounded_semaphore):
    assert bounded_semaphore._value == 2
    assert bounded_semaphore._initial_value == 2

def test_bounded_semaphore_acquire(bounded_semaphore):
    bounded_semaphore.acquire()
    assert bounded_semaphore._value == 1

def test_bounded_semaphore_release(bounded_semaphore):
    bounded_semaphore.acquire()
    bounded_semaphore.release()
    assert bounded_semaphore._value == 2

def test_bounded_semaphore_release_too_many_times(bounded_semaphore):
    bounded_semaphore.acquire()
    bounded_semaphore.release()
    with pytest.raises(ValueError, match="Semaphore released too many times"):
        bounded_semaphore.release()

def test_bounded_semaphore_multiple_acquire_release(bounded_semaphore):
    bounded_semaphore.acquire()
    bounded_semaphore.acquire()
    assert bounded_semaphore._value == 0
    bounded_semaphore.release()
    assert bounded_semaphore._value == 1
    bounded_semaphore.release()
    assert bounded_semaphore._value == 2
    with pytest.raises(ValueError, match="Semaphore released too many times"):
        bounded_semaphore.release()
