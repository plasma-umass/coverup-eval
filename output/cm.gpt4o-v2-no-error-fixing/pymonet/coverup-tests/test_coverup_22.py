# file: pymonet/monad_try.py:22-38
# asked: {"lines": [22, 23, 35, 36, 37, 38], "branches": []}
# gained: {"lines": [22, 23, 35, 36, 37, 38], "branches": []}

import pytest
from pymonet.monad_try import Try

def test_try_of_success():
    def success_fn(x):
        return x * 2

    result = Try.of(success_fn, 5)
    assert result.is_success
    assert result.value == 10

def test_try_of_failure():
    def failure_fn(x):
        raise ValueError("An error occurred")

    result = Try.of(failure_fn, 5)
    assert not result.is_success
    assert isinstance(result.value, ValueError)
    assert str(result.value) == "An error occurred"
