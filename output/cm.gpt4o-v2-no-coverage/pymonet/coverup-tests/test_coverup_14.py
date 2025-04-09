# file: pymonet/monad_try.py:40-51
# asked: {"lines": [40, 49, 50, 51], "branches": [[49, 50], [49, 51]]}
# gained: {"lines": [40, 49, 50, 51], "branches": [[49, 50], [49, 51]]}

import pytest
from pymonet.monad_try import Try

def test_try_map_success():
    # Arrange
    initial_value = 10
    try_instance = Try(initial_value, True)
    mapper = lambda x: x * 2

    # Act
    result = try_instance.map(mapper)

    # Assert
    assert result.is_success
    assert result.value == 20

def test_try_map_failure():
    # Arrange
    initial_value = 10
    try_instance = Try(initial_value, False)
    mapper = lambda x: x * 2

    # Act
    result = try_instance.map(mapper)

    # Assert
    assert not result.is_success
    assert result.value == initial_value
