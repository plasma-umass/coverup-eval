# file: tornado/locks.py:466-483
# asked: {"lines": [483], "branches": [[481, 483]]}
# gained: {"lines": [483], "branches": [[481, 483]]}

import pytest
from tornado.locks import BoundedSemaphore

def test_bounded_semaphore_release_within_limit():
    sem = BoundedSemaphore(value=2)
    sem.acquire()  # Decrement the counter to allow release
    sem.release()  # This should not raise an error
    assert sem._value == 2

def test_bounded_semaphore_release_exceeding_limit():
    sem = BoundedSemaphore(value=1)
    with pytest.raises(ValueError, match="Semaphore released too many times"):
        sem.release()
