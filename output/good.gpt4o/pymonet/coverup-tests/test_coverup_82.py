# file pymonet/either.py:153-162
# lines [153, 162]
# branches []

import pytest
from pymonet.either import Either, Right

def test_right_map():
    # Arrange
    right_instance = Right(10)
    mapper = lambda x: x * 2

    # Act
    result = right_instance.map(mapper)

    # Assert
    assert isinstance(result, Right)
    assert result.value == 20
