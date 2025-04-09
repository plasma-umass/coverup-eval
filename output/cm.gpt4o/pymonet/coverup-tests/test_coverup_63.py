# file pymonet/maybe.py:153-164
# lines [153, 160, 162, 163, 164]
# branches ['162->163', '162->164']

import pytest
from pymonet.maybe import Maybe
from pymonet.monad_try import Try

def test_maybe_to_try(mocker):
    # Mocking the Try class to ensure it is called correctly
    mock_try = mocker.patch('pymonet.monad_try.Try', autospec=True)

    # Test when Maybe is nothing
    maybe_nothing = Maybe(None, True)
    result = maybe_nothing.to_try()
    mock_try.assert_called_once_with(None, is_success=False)
    assert result == mock_try.return_value

    # Reset the mock for the next test
    mock_try.reset_mock()

    # Test when Maybe has a value
    maybe_value = Maybe('some_value', False)
    result = maybe_value.to_try()
    mock_try.assert_called_once_with('some_value', is_success=True)
    assert result == mock_try.return_value
