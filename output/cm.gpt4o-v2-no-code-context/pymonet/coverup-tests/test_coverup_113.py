# file: pymonet/either.py:189-198
# asked: {"lines": [196, 198], "branches": []}
# gained: {"lines": [196, 198], "branches": []}

import pytest
from pymonet.either import Right
from pymonet.maybe import Maybe

def test_right_to_maybe(mocker):
    # Mock the Maybe class and its just method
    mock_just = mocker.patch('pymonet.maybe.Maybe.just', return_value='mocked_value')

    # Create a Right instance with a value
    right_instance = Right(42)

    # Call the to_maybe method
    result = right_instance.to_maybe()

    # Assert that Maybe.just was called with the correct value
    mock_just.assert_called_once_with(42)

    # Assert that the result is the return value of Maybe.just
    assert result == 'mocked_value'
