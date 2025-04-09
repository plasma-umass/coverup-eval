# file: tornado/locks.py:466-483
# asked: {"lines": [466, 467, 475, 476, 477, 479, 481, 482, 483], "branches": [[481, 482], [481, 483]]}
# gained: {"lines": [466, 467, 475, 476, 477, 479, 481, 482, 483], "branches": [[481, 482], [481, 483]]}

import pytest
from tornado.locks import BoundedSemaphore

@pytest.fixture
def bounded_semaphore():
    return BoundedSemaphore(2)

def test_bounded_semaphore_initial_value(bounded_semaphore):
    assert bounded_semaphore._initial_value == 2

def test_bounded_semaphore_release_within_limit(bounded_semaphore):
    bounded_semaphore.acquire()
    bounded_semaphore.release()
    assert bounded_semaphore._value == 2

def test_bounded_semaphore_release_exceeding_limit():
    sem = BoundedSemaphore(1)
    sem.acquire()
    sem.release()
    with pytest.raises(ValueError, match="Semaphore released too many times"):
        sem.release()

def test_bounded_semaphore_cleanup():
    sem = BoundedSemaphore(1)
    sem.acquire()
    sem.release()
    assert sem._value == 1
    with pytest.raises(ValueError, match="Semaphore released too many times"):
        sem.release()
    # Clean up
    sem._value = 0
    assert sem._value == 0
