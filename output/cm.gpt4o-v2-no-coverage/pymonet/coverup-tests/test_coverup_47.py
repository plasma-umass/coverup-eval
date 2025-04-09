# file: pymonet/monad_try.py:22-38
# asked: {"lines": [22, 23, 35, 36, 37, 38], "branches": []}
# gained: {"lines": [22, 23, 35, 36, 37, 38], "branches": []}

import pytest
from pymonet.monad_try import Try

def test_try_of_success():
    def success_fn(x, y):
        return x + y

    result = Try.of(success_fn, 2, 3)
    assert result.value == 5
    assert result.is_success is True

def test_try_of_exception():
    def exception_fn(x, y):
        raise ValueError("An error occurred")

    result = Try.of(exception_fn, 2, 3)
    assert isinstance(result.value, ValueError)
    assert result.is_success is False
