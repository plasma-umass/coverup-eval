# file: pymonet/utils.py:81-96
# asked: {"lines": [81, 92, 93, 94, 95], "branches": []}
# gained: {"lines": [81, 92, 93, 94, 95], "branches": []}

import pytest
from functools import reduce
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

def test_compose_with_non_callable():
    with pytest.raises(TypeError):
        compose(1, 2)

def test_compose_with_none_value():
    def return_none(x):
        return None

    result = compose(None, return_none)
    assert result is None

def test_compose_with_empty_functions():
    result = compose(1, *[])
    assert result == 1
