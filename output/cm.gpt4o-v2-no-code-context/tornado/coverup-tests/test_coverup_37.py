# file: tornado/locks.py:466-483
# asked: {"lines": [466, 467, 475, 476, 477, 479, 481, 482, 483], "branches": [[481, 482], [481, 483]]}
# gained: {"lines": [466, 467, 475, 476, 477, 479, 481, 482, 483], "branches": [[481, 482], [481, 483]]}

import pytest
from tornado.locks import BoundedSemaphore

def test_bounded_semaphore_initial_value():
    sem = BoundedSemaphore(2)
    assert sem._initial_value == 2
    assert sem._value == 2

def test_bounded_semaphore_acquire_release():
    sem = BoundedSemaphore(2)
    sem.acquire()
    assert sem._value == 1
    sem.release()
    assert sem._value == 2

def test_bounded_semaphore_release_too_many_times():
    sem = BoundedSemaphore(1)
    sem.acquire()
    assert sem._value == 0
    sem.release()
    assert sem._value == 1
    with pytest.raises(ValueError, match="Semaphore released too many times"):
        sem.release()

@pytest.fixture
def bounded_semaphore():
    return BoundedSemaphore(1)

def test_bounded_semaphore_cleanup(bounded_semaphore):
    sem = bounded_semaphore
    sem.acquire()
    assert sem._value == 0
    sem.release()
    assert sem._value == 1
    with pytest.raises(ValueError, match="Semaphore released too many times"):
        sem.release()
