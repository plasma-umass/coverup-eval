# file tornado/locks.py:526-527
# lines [526, 527]
# branches []

import pytest
from tornado.locks import Lock

class MockLock(Lock):
    def __init__(self):
        self._block = None

def test_lock_repr():
    lock = MockLock()
    repr_string = repr(lock)
    assert repr_string.startswith("<MockLock _block=")
    assert repr_string.endswith(">")
