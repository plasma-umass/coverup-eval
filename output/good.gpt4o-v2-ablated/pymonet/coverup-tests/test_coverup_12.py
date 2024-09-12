# file: pymonet/monad_try.py:53-64
# asked: {"lines": [53, 62, 63, 64], "branches": [[62, 63], [62, 64]]}
# gained: {"lines": [53, 62, 63, 64], "branches": [[62, 63], [62, 64]]}

import pytest
from pymonet.monad_try import Try

class Success(Try):
    def __init__(self, value):
        self.value = value
        self.is_success = True

class Failure(Try):
    def __init__(self, exception):
        self.exception = exception
        self.is_success = False

def test_bind_success():
    success_instance = Success(10)
    def binder(x):
        return Success(x + 5)
    
    result = success_instance.bind(binder)
    assert isinstance(result, Success)
    assert result.value == 15

def test_bind_failure():
    failure_instance = Failure(Exception("error"))
    def binder(x):
        return Success(x + 5)
    
    result = failure_instance.bind(binder)
    assert isinstance(result, Failure)
    assert result.exception.args[0] == "error"
