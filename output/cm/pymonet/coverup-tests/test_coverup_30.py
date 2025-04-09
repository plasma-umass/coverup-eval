# file pymonet/monad_try.py:116-128
# lines [116, 126, 127, 128]
# branches ['126->127', '126->128']

import pytest
from pymonet.monad_try import Try

class Success(Try):
    def __init__(self, value):
        self.is_success = True
        self.value = value

class Failure(Try):
    def __init__(self, exception):
        self.is_success = False
        self.value = exception

def test_try_get_or_else_success():
    success_value = 42
    success_try = Success(success_value)
    assert success_try.get_or_else(0) == success_value

def test_try_get_or_else_failure():
    default_value = 0
    failure_try = Failure(Exception("failure"))
    assert failure_try.get_or_else(default_value) == default_value
