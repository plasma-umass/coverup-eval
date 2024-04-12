# file pymonet/monad_try.py:40-51
# lines [40, 49, 50, 51]
# branches ['49->50', '49->51']

import pytest
from pymonet.monad_try import Try

def test_try_map_success():
    # Arrange
    initial_value = 10
    mapper_function = lambda x: x * 2
    expected_value = initial_value * 2
    success_try = Try(initial_value, True)

    # Act
    result_try = success_try.map(mapper_function)

    # Assert
    assert result_try.is_success
    assert result_try.value == expected_value

def test_try_map_failure():
    # Arrange
    initial_value = "error"
    mapper_function = lambda x: x * 2
    failure_try = Try(initial_value, False)

    # Act
    result_try = failure_try.map(mapper_function)

    # Assert
    assert not result_try.is_success
    assert result_try.value == initial_value
