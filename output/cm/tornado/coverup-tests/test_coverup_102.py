# file tornado/locks.py:539-549
# lines [539, 546, 547, 548, 549]
# branches []

import pytest
from tornado.locks import Lock

@pytest.fixture
def lock():
    return Lock()

def test_lock_release_when_not_locked(lock):
    with pytest.raises(RuntimeError, match="release unlocked lock"):
        lock.release()

def test_lock_acquire_and_release(lock):
    assert lock.acquire()  # Acquire the lock
    lock.release()  # Release the lock
    with pytest.raises(RuntimeError, match="release unlocked lock"):
        lock.release()  # Attempt to release again should raise RuntimeError
