# file: pymonet/either.py:164-173
# asked: {"lines": [164, 173], "branches": []}
# gained: {"lines": [164, 173], "branches": []}

import pytest
from pymonet.either import Right

def test_right_bind():
    # Arrange
    right_value = Right(10)
    mapper = lambda x: x + 5

    # Act
    result = right_value.bind(mapper)

    # Assert
    assert result == 15

    # Clean up
    del right_value
    del mapper
    del result
