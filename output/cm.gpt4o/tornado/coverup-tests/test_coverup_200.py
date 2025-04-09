# file tornado/locks.py:526-527
# lines [526, 527]
# branches []

import pytest
from tornado.locks import Lock

@pytest.fixture
def lock():
    return Lock()

def test_lock_repr(lock):
    # Mock the _block attribute to ensure the __repr__ method is executed
    lock._block = "mock_block"
    repr_str = repr(lock)
    assert repr_str == "<Lock _block=mock_block>"

    # Clean up
    del lock._block
