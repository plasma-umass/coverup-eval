# file: pymonet/either.py:164-173
# asked: {"lines": [164, 173], "branches": []}
# gained: {"lines": [164, 173], "branches": []}

import pytest
from pymonet.either import Right

def test_right_bind():
    # Arrange
    right_value = 10
    right_instance = Right(right_value)
    
    def mapper(x):
        return x * 2
    
    # Act
    result = right_instance.bind(mapper)
    
    # Assert
    assert result == 20

