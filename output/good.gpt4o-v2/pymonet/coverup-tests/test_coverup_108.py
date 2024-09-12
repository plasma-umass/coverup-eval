# file: pymonet/either.py:153-162
# asked: {"lines": [153, 162], "branches": []}
# gained: {"lines": [153, 162], "branches": []}

import pytest
from pymonet.either import Right, Either

def test_right_map():
    # Arrange
    right_instance = Right(10)
    mapper = lambda x: x + 5

    # Act
    result = right_instance.map(mapper)

    # Assert
    assert isinstance(result, Right)
    assert result.value == 15

def test_right_map_with_string():
    # Arrange
    right_instance = Right("hello")
    mapper = lambda x: x.upper()

    # Act
    result = right_instance.map(mapper)

    # Assert
    assert isinstance(result, Right)
    assert result.value == "HELLO"
