# file: pymonet/monad_try.py:22-38
# asked: {"lines": [22, 23, 35, 36, 37, 38], "branches": []}
# gained: {"lines": [22, 23, 35, 36, 37, 38], "branches": []}

import pytest
from pymonet.monad_try import Try

def test_try_of_success():
    def success_fn(x, y):
        return x + y

    result = Try.of(success_fn, 1, 2)
    assert result.is_success
    assert result.value == 3

def test_try_of_failure():
    def failure_fn(x, y):
        return x / y

    result = Try.of(failure_fn, 1, 0)
    assert not result.is_success
    assert isinstance(result.value, Exception)
