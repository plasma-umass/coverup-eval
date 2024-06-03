# file pymonet/maybe.py:73-85
# lines [83, 84, 85]
# branches ['83->84', '83->85']

import pytest
from pymonet.maybe import Maybe

def test_maybe_ap_nothing(mocker):
    # Mock the Maybe class to control the behavior of is_nothing and value
    mock_maybe = mocker.MagicMock(spec=Maybe)
    mock_maybe.is_nothing = True

    # Create an instance of Maybe and call the ap method
    result = Maybe.ap(mock_maybe, Maybe.just(lambda x: x))

    # Assert that the result is a Maybe.nothing()
    assert result.is_nothing

def test_maybe_ap_something(mocker):
    # Mock the Maybe class to control the behavior of is_nothing and value
    mock_maybe = mocker.MagicMock(spec=Maybe)
    mock_maybe.is_nothing = False
    mock_maybe.value = 5

    # Mock the applicative Maybe to return a function that adds 1
    mock_applicative = mocker.MagicMock(spec=Maybe)
    mock_applicative.map = lambda func: Maybe.just(lambda x: x + 1)

    # Create an instance of Maybe and call the ap method
    result = Maybe.ap(mock_maybe, mock_applicative)

    # Assert that the result is a Maybe with the correct value
    assert not result.is_nothing
    assert result.value(5) == 6
