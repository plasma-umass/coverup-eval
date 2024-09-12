# file: tornado/locks.py:523-524
# asked: {"lines": [523, 524], "branches": []}
# gained: {"lines": [523], "branches": []}

import pytest
from tornado.locks import BoundedSemaphore

class Lock:
    def __init__(self) -> None:
        self._block = BoundedSemaphore(value=1)

def test_lock_initialization():
    lock = Lock()
    assert isinstance(lock._block, BoundedSemaphore)
    assert lock._block._value == 1
