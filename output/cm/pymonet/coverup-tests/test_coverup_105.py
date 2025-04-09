# file pymonet/monad_try.py:19-20
# lines [19, 20]
# branches []

import pytest
from pymonet.monad_try import Try

class Success(Try):
    def __init__(self, value):
        self.value = value
        self.is_success = True

class Failure(Try):
    def __init__(self, value):
        self.value = value
        self.is_success = False

def test_try_str_representation():
    success_value = Success(42)
    failure_value = Failure(Exception("Test exception"))

    assert str(success_value) == 'Try[value=42, is_success=True]'
    assert str(failure_value).startswith('Try[value=Test exception, is_success=False]')
