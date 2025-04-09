# file: tornado/locks.py:539-549
# asked: {"lines": [539, 546, 547, 548, 549], "branches": []}
# gained: {"lines": [539, 546, 547, 548, 549], "branches": []}

import pytest
from tornado.locks import Lock

@pytest.fixture
def lock():
    return Lock()

def test_lock_release_unlocked(lock):
    with pytest.raises(RuntimeError, match="release unlocked lock"):
        lock.release()

def test_lock_release_locked(lock):
    lock._block.acquire()  # Manually acquire the lock to simulate a locked state
    lock.release()
    assert lock._block._value == 1  # Ensure the lock is released

@pytest.fixture(autouse=True)
def cleanup_lock(lock):
    yield
    while lock._block._value < 1:
        lock._block.release()
