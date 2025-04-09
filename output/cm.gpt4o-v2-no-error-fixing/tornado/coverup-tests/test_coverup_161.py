# file: tornado/locks.py:526-527
# asked: {"lines": [527], "branches": []}
# gained: {"lines": [527], "branches": []}

import pytest
from tornado.locks import Lock

def test_lock_repr():
    lock = Lock()
    repr_str = repr(lock)
    assert repr_str.startswith("<Lock _block=")
    assert repr_str.endswith(">")

