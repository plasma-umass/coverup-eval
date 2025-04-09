# file: pymonet/utils.py:99-114
# asked: {"lines": [99, 110, 111, 112, 113], "branches": []}
# gained: {"lines": [99, 110, 111, 112, 113], "branches": []}

import pytest
from functools import reduce
from pymonet.utils import pipe

def test_pipe_single_function():
    def add_one(x):
        return x + 1

    result = pipe(1, add_one)
    assert result == 2

def test_pipe_multiple_functions():
    def add_one(x):
        return x + 1

    def multiply_by_two(x):
        return x * 2

    result = pipe(1, add_one, multiply_by_two)
    assert result == 4

def test_pipe_no_functions():
    result = pipe(1)
    assert result == 1

def test_pipe_with_non_callable():
    with pytest.raises(TypeError):
        pipe(1, 2)

def test_pipe_with_none_value():
    def return_none(x):
        return None

    result = pipe(None, return_none)
    assert result is None
