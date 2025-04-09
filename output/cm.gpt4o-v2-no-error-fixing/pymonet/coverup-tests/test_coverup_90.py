# file: pymonet/either.py:153-162
# asked: {"lines": [153, 162], "branches": []}
# gained: {"lines": [153, 162], "branches": []}

import pytest
from pymonet.either import Right

def test_right_map():
    # Arrange
    right_instance = Right(10)
    mapper = lambda x: x + 5

    # Act
    result = right_instance.map(mapper)

    # Assert
    assert isinstance(result, Right)
    assert result.value == 15

    # Clean up
    del right_instance
    del mapper
    del result
