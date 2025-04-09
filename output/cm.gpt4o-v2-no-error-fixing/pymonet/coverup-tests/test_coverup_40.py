# file: pymonet/utils.py:99-114
# asked: {"lines": [99, 110, 111, 112, 113], "branches": []}
# gained: {"lines": [99, 110, 111, 112, 113], "branches": []}

import pytest
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

def test_pipe_with_string():
    def add_exclamation(s):
        return s + "!"

    result = pipe("hello", add_exclamation)
    assert result == "hello!"

def test_pipe_with_empty_iterable():
    def add_one(x):
        return x + 1

    result = pipe(1, *[])
    assert result == 1
