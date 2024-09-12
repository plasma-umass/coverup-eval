# file: tornado/locks.py:466-483
# asked: {"lines": [466, 467, 475, 476, 477, 479, 481, 482, 483], "branches": [[481, 482], [481, 483]]}
# gained: {"lines": [466, 467, 475, 479], "branches": []}

import pytest
from tornado.locks import Semaphore

class BoundedSemaphore(Semaphore):
    """A semaphore that prevents release() being called too many times.

    If `.release` would increment the semaphore's value past the initial
    value, it raises `ValueError`. Semaphores are mostly used to guard
    resources with limited capacity, so a semaphore released too many times
    is a sign of a bug.
    """

    def __init__(self, value: int = 1) -> None:
        super().__init__(value=value)
        self._initial_value = value

    def release(self) -> None:
        """Increment the counter and wake one waiter."""
        if self._value >= self._initial_value:
            raise ValueError("Semaphore released too many times")
        super().release()

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
    with pytest.raises(ValueError, match="Semaphore released too many times"):
        bounded_semaphore.release()

def test_bounded_semaphore_acquire_and_release(bounded_semaphore):
    bounded_semaphore.acquire()
    bounded_semaphore.acquire()
    assert bounded_semaphore._value == 0
    bounded_semaphore.release()
    assert bounded_semaphore._value == 1
    bounded_semaphore.release()
    assert bounded_semaphore._value == 2
    with pytest.raises(ValueError, match="Semaphore released too many times"):
        bounded_semaphore.release()
