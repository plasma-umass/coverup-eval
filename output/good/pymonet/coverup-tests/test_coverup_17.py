# file pymonet/monad_try.py:53-64
# lines [53, 62, 63, 64]
# branches ['62->63', '62->64']

import pytest
from pymonet.monad_try import Try

class Success(Try):
    def __init__(self, value):
        self.is_success = True
        self.value = value

class Failure(Try):
    def __init__(self, exception):
        self.is_success = False
        self.exception = exception

def test_try_bind_success():
    def binder(value):
        return Success(value * 2)

    success_try = Success(10)
    result = success_try.bind(binder)
    assert isinstance(result, Try)
    assert result.is_success
    assert result.value == 20

def test_try_bind_failure():
    def binder(value):
        return Success(value * 2)

    failure_try = Failure(Exception("Test Error"))
    result = failure_try.bind(binder)
    assert isinstance(result, Try)
    assert not result.is_success
    assert isinstance(result.exception, Exception)
    assert str(result.exception) == "Test Error"
