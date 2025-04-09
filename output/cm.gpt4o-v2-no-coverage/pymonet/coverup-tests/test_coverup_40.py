# file: pymonet/utils.py:99-114
# asked: {"lines": [99, 110, 111, 112, 113], "branches": []}
# gained: {"lines": [99, 110, 111, 112, 113], "branches": []}

import pytest
from pymonet.utils import pipe

def test_pipe_no_functions():
    result = pipe(5)
    assert result == 5

def test_pipe_single_function():
    result = pipe(5, lambda x: x + 1)
    assert result == 6

def test_pipe_multiple_functions():
    result = pipe(5, lambda x: x + 1, lambda x: x * 2, lambda x: x - 3)
    assert result == 9

def test_pipe_with_string():
    result = pipe("hello", str.upper, lambda x: x + " WORLD")
    assert result == "HELLO WORLD"

def test_pipe_with_empty_string():
    result = pipe("", str.upper, lambda x: x + "EMPTY")
    assert result == "EMPTY"

def test_pipe_with_list():
    result = pipe([1, 2, 3], lambda x: [i * 2 for i in x], sum)
    assert result == 12
