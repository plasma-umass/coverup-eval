# file: pymonet/monad_try.py:116-128
# asked: {"lines": [116, 126, 127, 128], "branches": [[126, 127], [126, 128]]}
# gained: {"lines": [116, 126, 127, 128], "branches": [[126, 127], [126, 128]]}

import pytest
from pymonet.monad_try import Try

class MockSuccessTry(Try):
    def __init__(self, value):
        self.is_success = True
        self.value = value

class MockFailureTry(Try):
    def __init__(self):
        self.is_success = False

@pytest.fixture
def success_try():
    return MockSuccessTry(42)

@pytest.fixture
def failure_try():
    return MockFailureTry()

def test_get_or_else_success(success_try):
    assert success_try.get_or_else(0) == 42

def test_get_or_else_failure(failure_try):
    assert failure_try.get_or_else(0) == 0
