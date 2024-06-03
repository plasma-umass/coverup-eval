# file pymonet/maybe.py:140-151
# lines [147, 149, 150, 151]
# branches ['149->150', '149->151']

import pytest
from pymonet.maybe import Maybe
from pymonet.lazy import Lazy

def test_maybe_to_lazy(mocker):
    # Mocking the Lazy class to verify the lambda functions
    mock_lazy = mocker.patch('pymonet.lazy.Lazy', autospec=True)

    # Test when Maybe is nothing
    maybe_nothing = Maybe.nothing()
    result = maybe_nothing.to_lazy()
    mock_lazy.assert_called_once_with(mocker.ANY)
    assert result == mock_lazy.return_value
    assert mock_lazy.call_args[0][0]() is None

    # Reset mock for the next test
    mock_lazy.reset_mock()

    # Test when Maybe has a value
    value = 42
    maybe_just = Maybe.just(value)
    result = maybe_just.to_lazy()
    mock_lazy.assert_called_once_with(mocker.ANY)
    assert result == mock_lazy.return_value
    assert mock_lazy.call_args[0][0]() == value
