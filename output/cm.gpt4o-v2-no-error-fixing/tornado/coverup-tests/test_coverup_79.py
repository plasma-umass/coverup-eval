# file: tornado/locks.py:539-549
# asked: {"lines": [539, 546, 547, 548, 549], "branches": []}
# gained: {"lines": [539, 546, 547, 548, 549], "branches": []}

import pytest
from tornado.locks import Lock

def test_lock_release_when_locked():
    lock = Lock()
    lock._block.acquire()  # Manually acquire the lock to set up the state
    lock.release()  # Now release it
    assert lock._block._value == 1  # Check if the lock is released properly

def test_lock_release_when_unlocked():
    lock = Lock()
    with pytest.raises(RuntimeError, match="release unlocked lock"):
        lock.release()  # Try to release an unlocked lock, should raise RuntimeError
