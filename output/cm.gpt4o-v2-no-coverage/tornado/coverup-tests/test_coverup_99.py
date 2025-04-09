# file: tornado/locks.py:539-549
# asked: {"lines": [539, 546, 547, 548, 549], "branches": []}
# gained: {"lines": [539, 546, 547, 548, 549], "branches": []}

import pytest
from tornado.locks import Lock
from tornado.locks import BoundedSemaphore

def test_lock_release():
    lock = Lock()
    
    # Acquire the lock first to be able to release it
    lock._block.acquire()
    assert lock._block._value == 0  # Ensure the lock is acquired
    
    # Now release the lock
    lock.release()
    assert lock._block._value == 1  # Ensure the lock is released

def test_lock_release_unlocked():
    lock = Lock()
    
    # Try to release the lock without acquiring it first
    with pytest.raises(RuntimeError, match="release unlocked lock"):
        lock.release()
