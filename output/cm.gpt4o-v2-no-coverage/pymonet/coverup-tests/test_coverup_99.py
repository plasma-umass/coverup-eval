# file: pymonet/either.py:164-173
# asked: {"lines": [164, 173], "branches": []}
# gained: {"lines": [164, 173], "branches": []}

import pytest
from pymonet.either import Right, Either

def test_right_bind():
    # Arrange
    right_value = Right(10)
    mapper = lambda x: Right(x + 5)
    
    # Act
    result = right_value.bind(mapper)
    
    # Assert
    assert isinstance(result, Right)
    assert result.value == 15

def test_right_bind_non_right():
    # Arrange
    right_value = Right(10)
    mapper = lambda x: x + 5  # This does not return a Right instance
    
    # Act
    result = right_value.bind(mapper)
    
    # Assert
    assert result == 15
