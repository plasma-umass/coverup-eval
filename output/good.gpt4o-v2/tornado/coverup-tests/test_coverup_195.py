# file: tornado/locks.py:523-524
# asked: {"lines": [523, 524], "branches": []}
# gained: {"lines": [523, 524], "branches": []}

import pytest
from tornado.locks import Lock, BoundedSemaphore

@pytest.fixture
def lock():
    return Lock()

def test_lock_initialization(lock):
    assert isinstance(lock._block, BoundedSemaphore)
    assert lock._block._initial_value == 1
