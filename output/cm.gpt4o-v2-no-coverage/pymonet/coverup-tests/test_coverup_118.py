# file: pymonet/utils.py:81-96
# asked: {"lines": [92, 93, 94, 95], "branches": []}
# gained: {"lines": [92, 93, 94, 95], "branches": []}

import pytest
from pymonet.utils import compose

def test_compose_single_function():
    def add_one(x):
        return x + 1

    result = compose(1, add_one)
    assert result == 2

def test_compose_multiple_functions():
    def add_one(x):
        return x + 1

    def multiply_by_two(x):
        return x * 2

    result = compose(1, add_one, multiply_by_two)
    assert result == 3  # (1 * 2) + 1

def test_compose_no_functions():
    result = compose(1)
    assert result == 1

def test_compose_with_string():
    def add_exclamation(s):
        return s + "!"

    def to_upper(s):
        return s.upper()

    result = compose("hello", add_exclamation, to_upper)
    assert result == "HELLO!"

def test_compose_with_empty_string():
    def add_exclamation(s):
        return s + "!"

    result = compose("", add_exclamation)
    assert result == "!"

def test_compose_with_noop_function():
    def noop(x):
        return x

    result = compose(1, noop)
    assert result == 1
