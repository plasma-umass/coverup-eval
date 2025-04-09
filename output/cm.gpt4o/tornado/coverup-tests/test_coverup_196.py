# file tornado/locks.py:523-524
# lines [523, 524]
# branches []

import pytest
from tornado.locks import BoundedSemaphore, Lock

@pytest.fixture
def lock():
    return Lock()

def test_lock_initialization(lock):
    assert isinstance(lock._block, BoundedSemaphore)
    assert lock._block._value == 1
