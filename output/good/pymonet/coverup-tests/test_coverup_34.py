# file pymonet/monad_try.py:22-38
# lines [22, 23, 35, 36, 37, 38]
# branches []

import pytest
from pymonet.monad_try import Try

def test_try_of_success():
    def successful_function(x):
        return x + 1

    result = Try.of(successful_function, 1)
    assert isinstance(result, Try)
    assert result.is_success is True
    assert result.value == 2

def test_try_of_failure():
    def failing_function(x):
        raise ValueError("failure")

    result = Try.of(failing_function, 1)
    assert isinstance(result, Try)
    assert result.is_success is False
    assert isinstance(result.value, ValueError)
