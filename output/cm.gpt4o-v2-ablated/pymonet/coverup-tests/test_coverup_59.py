# file: pymonet/either.py:153-162
# asked: {"lines": [153, 162], "branches": []}
# gained: {"lines": [153, 162], "branches": []}

import pytest
from pymonet.either import Either, Right

def test_right_map():
    # Test that the map function correctly applies the mapper function
    right = Right(10)
    result = right.map(lambda x: x + 5)
    assert isinstance(result, Right)
    assert result.value == 15

    # Test that the map function works with different types
    right = Right("hello")
    result = right.map(lambda x: x.upper())
    assert isinstance(result, Right)
    assert result.value == "HELLO"

    # Test that the map function works with a more complex function
    right = Right([1, 2, 3])
    result = right.map(lambda x: [i * 2 for i in x])
    assert isinstance(result, Right)
    assert result.value == [2, 4, 6]

    # Test that the map function works with an empty list
    right = Right([])
    result = right.map(lambda x: [i * 2 for i in x])
    assert isinstance(result, Right)
    assert result.value == []

    # Test that the map function works with a None value
    right = Right(None)
    result = right.map(lambda x: x)
    assert isinstance(result, Right)
    assert result.value is None
