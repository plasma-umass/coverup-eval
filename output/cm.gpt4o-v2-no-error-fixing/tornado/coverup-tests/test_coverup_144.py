# file: tornado/locks.py:523-524
# asked: {"lines": [523, 524], "branches": []}
# gained: {"lines": [523, 524], "branches": []}

import pytest
from tornado.locks import Lock
from tornado.locks import BoundedSemaphore

def test_lock_initialization():
    lock = Lock()
    assert isinstance(lock._block, BoundedSemaphore)
    assert lock._block._initial_value == 1
