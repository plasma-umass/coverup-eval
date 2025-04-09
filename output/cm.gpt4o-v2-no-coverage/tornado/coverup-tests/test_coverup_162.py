# file: tornado/locks.py:526-527
# asked: {"lines": [526, 527], "branches": []}
# gained: {"lines": [526, 527], "branches": []}

import pytest
from tornado.locks import Lock

def test_lock_repr():
    lock = Lock()
    lock._block = "test_block"
    assert repr(lock) == "<Lock _block=test_block>"
