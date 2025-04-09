# file: tornado/locks.py:526-527
# asked: {"lines": [526, 527], "branches": []}
# gained: {"lines": [526, 527], "branches": []}

import pytest
from tornado.locks import Lock

@pytest.fixture
def lock():
    return Lock()

def test_lock_repr(lock):
    repr_str = repr(lock)
    assert repr_str.startswith("<Lock _block=")
    assert repr_str.endswith(">")

