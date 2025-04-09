# file pymonet/maybe.py:114-125
# lines [114, 121, 123, 124, 125]
# branches ['123->124', '123->125']

import pytest
from pymonet.maybe import Maybe
from pymonet.either import Left, Right

def test_maybe_to_either(mocker):
    # Test when Maybe is nothing
    mock_nothing = mocker.MagicMock(spec=Maybe)
    mock_nothing.is_nothing = True
    mock_nothing.to_either = Maybe.to_either.__get__(mock_nothing, Maybe)
    result = mock_nothing.to_either()
    assert isinstance(result, Left)
    assert result.value is None

    # Test when Maybe has a value
    mock_value = mocker.MagicMock(spec=Maybe)
    mock_value.is_nothing = False
    mock_value.value = 42
    mock_value.to_either = Maybe.to_either.__get__(mock_value, Maybe)
    result = mock_value.to_either()
    assert isinstance(result, Right)
    assert result.value == 42
