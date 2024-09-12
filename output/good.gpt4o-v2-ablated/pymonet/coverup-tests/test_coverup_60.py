# file: pymonet/monad_try.py:19-20
# asked: {"lines": [19, 20], "branches": []}
# gained: {"lines": [19, 20], "branches": []}

import pytest
from pymonet.monad_try import Try

class MockTry(Try):
    def __init__(self, value, is_success):
        self.value = value
        self.is_success = is_success

def test_try_str():
    try_instance = MockTry(value="test_value", is_success=True)
    assert str(try_instance) == 'Try[value=test_value, is_success=True]'

    try_instance = MockTry(value=None, is_success=False)
    assert str(try_instance) == 'Try[value=None, is_success=False]'
